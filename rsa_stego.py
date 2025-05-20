from typing import Tuple, List, Union
import numpy as np
from scipy.fftpack import dct, idct
import soundfile as sf
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class RSADCTStego:
    """
    A class implementing RSA encryption combined with DCT-based audio steganography.
    Provides methods for embedding encrypted messages in audio files and extracting them.
    """
    
    @staticmethod
    def generate_keys(key_size: int = 2048) -> Tuple[bytes, bytes]:
        """Generate RSA key pair.
        
        Args:
            key_size: Size of RSA key in bits
            
        Returns:
            Tuple containing (public_key, private_key) as bytes
        """
        key = RSA.generate(key_size)
        return key.publickey().export_key(), key.export_key()

    @staticmethod
    def rsa_encrypt(message: str, public_key_bytes: bytes) -> bytes:
        """Encrypt a message using RSA-OAEP.
        
        Args:
            message: Plain text message to encrypt
            public_key_bytes: Public key in bytes format
            
        Returns:
            Encrypted message as bytes
        """
        public_key = RSA.import_key(public_key_bytes)
        cipher = PKCS1_OAEP.new(public_key)
        return cipher.encrypt(message.encode())

    @staticmethod
    def rsa_decrypt(ciphertext: bytes, private_key_bytes: bytes) -> str:
        """Decrypt an RSA-OAEP encrypted message.
        
        Args:
            ciphertext: Encrypted message bytes
            private_key_bytes: Private key in bytes format
            
        Returns:
            Decrypted message as string
        """
        private_key = RSA.import_key(private_key_bytes)
        cipher = PKCS1_OAEP.new(private_key)
        return cipher.decrypt(ciphertext).decode()

    @staticmethod
    def embed_audio(
        audio_path: str,
        ciphertext: bytes,
        output_path: str,
        dct_coeff: int = 3,
        block_size: int = 1024,
        alpha: float = 5.0
    ) -> str:
        """Embed encrypted message in audio file using DCT.
        
        Args:
            audio_path: Path to input audio file
            ciphertext: Encrypted message to embed
            output_path: Path to save modified audio
            dct_coeff: DCT coefficient to modify
            block_size: Size of audio blocks for DCT
            alpha: Strength of embedding
            
        Returns:
            Path to output audio file
            
        Raises:
            ValueError: If audio file is too short for message
        """
        # Load and prepare audio
        audio, sr = sf.read(audio_path)
        audio = np.mean(audio, axis=1) if audio.ndim > 1 else audio

        # Prepare message bits
        header = len(ciphertext).to_bytes(4, 'big')
        data = header + ciphertext
        bits = np.unpackbits(np.frombuffer(data, dtype=np.uint8))

        # Check capacity
        max_bits = len(audio) // block_size
        if len(bits) > max_bits:
            raise ValueError(
                f"Audio too short. Maximum capacity: {max_bits} bits, "
                f"required: {len(bits)} bits"
            )

        # Embed bits
        audio_modified = audio.copy()
        for i in range(0, len(audio) - block_size, block_size):
            if i//block_size >= len(bits):
                break
                
            block = audio[i:i+block_size]
            dct_block = dct(block, norm='ortho')
            
            # Modify coefficient based on bit value
            dct_block[dct_coeff] += alpha if bits[i//block_size] else -alpha
            audio_modified[i:i+block_size] = idct(dct_block, norm='ortho')

        sf.write(output_path, audio_modified, sr, subtype='FLOAT')
        return output_path

    @staticmethod
    def extract_audio(
        audio_path: str,
        dct_coeff: int = 3,
        block_size: int = 1024
    ) -> bytes:
        """Extract embedded message from audio file.
        
        Args:
            audio_path: Path to steganographic audio file
            dct_coeff: DCT coefficient used in embedding
            block_size: Size of audio blocks used
            
        Returns:
            Extracted encrypted message as bytes
            
        Raises:
            ValueError: If embedded data is invalid or incomplete
        """
        # Load and prepare audio
        audio, _ = sf.read(audio_path)
        audio = np.mean(audio, axis=1) if audio.ndim > 1 else audio

        # Extract bits
        bits = []
        for i in range(0, len(audio) - block_size, block_size):
            block = audio[i:i+block_size]
            dct_block = dct(block, norm='ortho')
            bits.append(1 if dct_block[dct_coeff] >= 0 else 0)

        # Validate header
        if len(bits) < 32:
            raise ValueError("Insufficient data to read message length header.")

        # Parse message length from header
        header_bits = bits[:32]
        msg_len = int(''.join(map(str, header_bits)), 2)
        expected_bits = msg_len * 8

        # Validate message length
        if len(bits) < 32 + expected_bits:
            raise ValueError(
                f"Insufficient data: {len(bits)} bits available, "
                f"need {expected_bits} bits for message"
            )

        # Extract and convert message bits to bytes
        message_bits = bits[32:32 + expected_bits]
        ciphertext = bytes(
            int(''.join(map(str, message_bits[i:i+8])), 2)
            for i in range(0, len(message_bits), 8)
        )
        
        return ciphertext
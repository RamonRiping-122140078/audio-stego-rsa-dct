"""
RSA + DCT Audio Steganography
Main program for encrypting messages and embedding them in audio files.
"""

import os
import numpy as np
import soundfile as sf
from typing import Optional
from rsa_stego import RSADCTStego

# === CONFIG ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RSA_DIR = os.path.join(BASE_DIR, "RSA")
OUTPUT_DIR = os.path.join(RSA_DIR, "output1")
INPUT_DIR = os.path.join(RSA_DIR, "input")
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
INPUT_AUDIO = os.path.join(INPUT_DIR, "c.wav")
STEGO_AUDIO = os.path.join(OUTPUT_DIR, "stego.wav")
PUBLIC_KEY_PATH = os.path.join(OUTPUT_DIR, "public.pem")
PRIVATE_KEY_PATH = os.path.join(OUTPUT_DIR, "private.pem")
MAX_MESSAGE_LENGTH = 190  # Safe limit for RSA-2048 with PKCS1_OAEP padding

def generate_dummy_audio(path: str, duration_sec: float = 60.0, sample_rate: int = 44100) -> None:
    """Generate a mono sine wave audio file."""
    print("🎧 Generating dummy audio file...")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    t = np.linspace(0, duration_sec, int(sample_rate * duration_sec), endpoint=False)
    # Generate a more complex waveform with multiple frequencies
    audio = 0.3 * np.sin(2 * np.pi * 440 * t)  # 440Hz (A4 note)
    audio += 0.3 * np.sin(2 * np.pi * 554.37 * t)  # 554.37Hz (C#5 note)
    audio += 0.3 * np.sin(2 * np.pi * 659.25 * t)  # 659.25Hz (E5 note)
    # Normalize to prevent clipping
    audio = audio / np.max(np.abs(audio))
    sf.write(path, audio, sample_rate)
    print(f"✅ Dummy audio saved at: {path}")

def ensure_input_audio() -> None:
    """Ensure the input directory and audio file exist."""
    if not os.path.exists(INPUT_AUDIO):
        print(f"⚠️ Input audio not found: {INPUT_AUDIO}")
        generate_dummy_audio(INPUT_AUDIO)

def ensure_keys() -> None:
    """Generate RSA key pair if they don't exist."""
    if not os.path.exists(PUBLIC_KEY_PATH) or not os.path.exists(PRIVATE_KEY_PATH):
        print("🔑 Key not found. Generating new RSA key pair...")
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        pub_key, priv_key = RSADCTStego.generate_keys()
        with open(PUBLIC_KEY_PATH, "wb") as f:
            f.write(pub_key)
        with open(PRIVATE_KEY_PATH, "wb") as f:
            f.write(priv_key)
        print("✅ Keys generated.")
    else:
        print("🔑 Keys already exist. Skipping generation.")

def encrypt_flow() -> Optional[bool]:
    """Handle the encryption and embedding process."""
    ensure_keys()
    ensure_input_audio()

    message = input(f"📨 Enter secret message to encrypt (Max: {MAX_MESSAGE_LENGTH} Letters): ")
    if len(message.encode('utf-8')) > MAX_MESSAGE_LENGTH:
        print(f"❌ Message too long! Maximum {MAX_MESSAGE_LENGTH} bytes "
              "(non-ASCII characters count as multiple bytes).")
        return None

    try:
        with open(PUBLIC_KEY_PATH, "rb") as f:
            pub_key = f.read()
        ciphertext = RSADCTStego.rsa_encrypt(message, pub_key)

        RSADCTStego.embed_audio(INPUT_AUDIO, ciphertext, STEGO_AUDIO)
        print("✅ Message encrypted and embedded successfully.")
        print(f"🧊 Send this file to receiver: {STEGO_AUDIO}")
        return True
    except Exception as e:
        print(f"❌ Error during encryption: {e}")
        return None

def decrypt_flow() -> Optional[str]:
    """Handle the extraction and decryption process."""
    if not os.path.exists(STEGO_AUDIO):
        print(f"❌ Stego audio file not found: {STEGO_AUDIO}")
        return None

    if not os.path.exists(PRIVATE_KEY_PATH):
        print(f"❌ Private key not found: {PRIVATE_KEY_PATH}")
        return None

    try:
        with open(PRIVATE_KEY_PATH, "rb") as f:
            priv_key = f.read()

        ciphertext = RSADCTStego.extract_audio(STEGO_AUDIO)
        plaintext = RSADCTStego.rsa_decrypt(ciphertext, priv_key)

        print("✅ Message successfully decrypted!")
        print("📩 Decrypted message:", plaintext)
        return plaintext
    except Exception as e:
        print(f"❌ Error during decryption: {e}")
        return None

def main() -> None:
    """Main program loop."""
    print("🎯 RSA + DCT Audio Steganography")
    print("1. Encrypt & Embed")
    print("2. Extract & Decrypt")
    print("3. Exit")

    while True:
        choice = input("Choose option (1/2/3): ")

        if choice == "1":
            encrypt_flow()
        elif choice == "2":
            decrypt_flow()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

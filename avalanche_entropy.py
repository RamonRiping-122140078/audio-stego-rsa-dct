from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from collections import Counter
import math

def to_bitstring(data: bytes) -> str:
    return ''.join(format(byte, '08b') for byte in data)

def avalanche_effect(msg1: str, msg2: str, public_key) -> float:
    cipher = PKCS1_OAEP.new(public_key)
    c1 = cipher.encrypt(msg1.encode())
    c2 = cipher.encrypt(msg2.encode())

    bits1 = to_bitstring(c1)
    bits2 = to_bitstring(c2)

    bit_diff = sum(b1 != b2 for b1, b2 in zip(bits1, bits2))
    total_bits = len(bits1)
    return (bit_diff / total_bits) * 100

def calculate_entropy(ciphertext: bytes) -> float:
    freq = Counter(ciphertext)
    total = len(ciphertext)
    return -sum((count/total) * math.log2(count/total) for count in freq.values())

# Generate RSA keys
key = RSA.generate(2048)
pub_key = key.publickey()

# Test
plain1 = "Halo, ini pesan rahasia!"
plain2 = "Halo, ini pesan rahasia!"

cipher = PKCS1_OAEP.new(pub_key)
ct = cipher.encrypt(plain1.encode())

print("🔐 Avalanche Effect:", avalanche_effect(plain1, plain2, pub_key), "%")
print("🔐 Entropi Ciphertext:", calculate_entropy(ct), "bits")

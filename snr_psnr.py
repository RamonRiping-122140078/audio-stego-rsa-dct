import soundfile as sf
import numpy as np

def compute_snr(original, stego):
    noise = original - stego
    signal_power = np.sum(original ** 2)
    noise_power = np.sum(noise ** 2)
    return 10 * np.log10(signal_power / noise_power)

def compute_psnr(original, stego):
    mse = np.mean((original - stego) ** 2)
    if mse == 0:
        return float('inf')
    max_val = np.max(original)
    return 10 * np.log10((max_val ** 2) / mse)

# Load WAV mono 16-bit
original_audio, _ = sf.read('RSA/input/c.wav')
stego_audio, _ = sf.read('RSA/output1/stego.wav')

min_len = min(len(original_audio), len(stego_audio))
original_audio = original_audio[:min_len]
stego_audio = stego_audio[:min_len]

print("🎧 SNR:", compute_snr(original_audio, stego_audio), "dB")
print("🎧 PSNR:", compute_psnr(original_audio, stego_audio), "dB")

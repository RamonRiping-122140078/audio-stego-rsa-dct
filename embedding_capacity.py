import soundfile as sf

def calculate_embedding_capacity(wav_path, bits_per_block=8, ratio=0.25):
    audio_data, samplerate = sf.read(wav_path)
    
    if audio_data.ndim > 1:
        audio_data = audio_data[:, 0]  # ambil channel pertama jika stereo

    total_samples = len(audio_data)
    embeddable_samples = int(total_samples * ratio)

    total_bits = embeddable_samples * bits_per_block
    total_bytes = total_bits // 8

    return total_bytes, total_bits

file_path = "RSA/input/c.wav"
capacity_bytes, capacity_bits = calculate_embedding_capacity(file_path)

print(f"📦 Estimasi Embedding Capacity:")
print(f"- {capacity_bits} bits")
print(f"- {capacity_bytes} bytes (~{capacity_bytes // 8} karakter ASCII)")

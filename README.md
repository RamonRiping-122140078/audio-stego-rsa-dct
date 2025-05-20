# 🔐 Steganografi Audio dengan RSA + DCT

Proyek ini menyembunyikan pesan rahasia ke dalam file audio menggunakan **enkripsi RSA** dan **steganografi berbasis DCT (Discrete Cosine Transform)**.

## 📦 Fitur
- Generate pasangan kunci publik dan privat RSA
- Enkripsi pesan dan sisipkan ke dalam file audio WAV
- Ekstrak dan dekripsi pesan dari audio yang telah dimodifikasi
- Antarmuka menu sederhana lewat `main.py`

---

## 🚀 Cara Menjalankan

### 1. Clone atau Unduh Proyek

```bash
git clone https://github.com/nama-anda/audio-stego-rsa.git
cd audio-stego-rsa
```

### 2. Buat Virtual Environment

```bash
python -m venv venv
```

### Aktifkan virtual environment:

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

📌 Cara Menggunakan
🔏 Menyisipkan dan Mengenkripsi Pesan
Pastikan file audio RSA/input/c.wav tersedia.

Jalankan program:

```bash
python main.py
```

Pilih:

1. Enkripsi & Sisipkan
Masukkan pesan yang ingin disembunyikan.

Hasilnya akan muncul sebagai RSA/output1/stego.wav.

🔓 Mengekstrak dan Mendekripsi Pesan
Pastikan file RSA/output1/stego.wav sudah ada.

Jalankan kembali program:

```bash
python main.py
```

Pilih:

2. Ekstrak & Dekripsi
Pesan akan ditampilkan di terminal setelah berhasil didekripsi.

⚠️ Catatan
Gunakan file WAV mono agar proses lebih akurat.

Panjang file audio harus cukup untuk menampung pesan.

Jika kunci belum ada, program akan otomatis membuatnya.

🛠 Kebutuhan
Terdapat pada requirements.txt:

- numpy
- scipy
- pycryptodome
- soundfile

📬 Lisensi
MIT – bebas digunakan dan dimodifikasi.

🤝 Terima Kasih
Dibuat dengan ❤️ menggunakan:

- PyCryptodome
- SciPy DCT
- SoundFile
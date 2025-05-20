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

### 3. Aktifkan virtual environment:

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependensi

```bash
pip install -r requirements.txt
```

## 📌 Cara Menggunakan
### 🔏 Menyisipkan dan Mengenkripsi Pesan
1. Pastikan file audio `RSA/input/c.wav` tersedia.
2. Jalankan program:

```bash
python main.py
```

3. Pilih opsi:

```bash
1. Enkripsi & Sisipkan
```

4. Masukkan pesan yang ingin disembunyikan.
5. File hasil akan tersimpan di `RSA/output1/stego.wav`.

## 🔓 Mengekstrak dan Mendekripsi Pesan
1. Pastikan file `RSA/output1/stego.wav` sudah ada.
2. Jalankan kembali program:

```bash
python main.py
```

3. Pilih opsi:

```bash
Ekstrak & Dekripsi
```

4. Pesan akan ditampilkan di terminal setelah berhasil diekstraksi & didekripsi.
---
## ⚠️ Catatan
- Gunakan file WAV mono agar proses lebih akurat.
- Panjang file audio harus cukup untuk menampung pesan.
- Jika kunci belum ada, program akan otomatis membuatnya.
---
🛠 Kebutuhan
Dependensi pada `requirements.txt`:
- numpy
- scipy
- pycryptodome
- soundfile
---
📬 Lisensi
MIT – bebas digunakan dan dimodifikasi.
---
🤝 Terima Kasih
Dibuat dengan ❤️ menggunakan:
- PyCryptodome
- SciPy DCT
- SoundFile
---
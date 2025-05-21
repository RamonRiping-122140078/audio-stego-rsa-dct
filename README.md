# 🔐 Audio Steganography: RSA + DCT (Python)

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
---
## 📌 Cara Menggunakan
### 🔏 Menyisipkan dan Mengenkripsi Pesan
1. Jika `RSA/input/c.wav` belum ada, program akan otomatis membuatnya saat dijalankan.
2. Jalankan program:

```bash
python main.py
```

3. Pilih opsi `1. Enkripsi & Sisipkan` di menu.
4. Masukkan pesan yang ingin disembunyikan.
5. Berikut merupakan contoh outputnya :
```bash
📥 Contoh:
Masukkan pesan: `Halo, ini pesan rahasia!`

📤 Output:
✅ Message encrypted and embedded successfully.
🧊 Send this file to receiver: RSA/output1/stego.wav
```

6. File hasil akan tersimpan di `RSA/output1/stego.wav`.
---
## 🔓 Mengekstrak dan Mendekripsi Pesan
1. Pastikan file `RSA/output1/stego.wav` sudah ada.
2. Jalankan kembali program:

```bash
python main.py
```

3. Pilih opsi `2. Ekstrak & Dekripsi` di menu.
4. Pesan akan ditampilkan di terminal setelah berhasil diekstraksi & didekripsi.
```bash
📤 Output:
✅ Message successfully decrypted!
📩 Decrypted message: `Halo, ini pesan rahasia!`
```
---
## 📊 Cara Menjalankan Evaluasi
### 🔐 Uji Keamanan Kriptografi: Avalanche Effect & Entropi
Menjalankan simulasi perubahan 1-bit dan menghitung entropi dari ciphertext RSA.

```bash
python avalanche_entropy.py
```

📤 Contoh output:

```bash
🔐 Avalanche Effect: 50.78 %
🔐 Entropi Ciphertext: 7.14 bits
```

### 🎧 Uji Transparansi Steganografi: SNR & PSNR
Mengukur kualitas audio setelah penyisipan pesan menggunakan perbandingan sinyal asli dan stego.

```bash
python snr_psnr.py
```

📤 Contoh output:

```bash
🎧 SNR: 9.29 dB
🎧 PSNR: 17.06 dB
```

### 💾 Uji Kapasitas Penyimpanan: Embedding Capacity
Menghitung berapa banyak bit yang dapat disisipkan dalam file audio berdasarkan panjang dan DCT.

```bash
python embedding_capacity.py
```

📤 Contoh output:

```bash
📦 Estimasi Embedding Capacity:
- 5,292,000 bits
- 661,500 bytes (~82,687 karakter ASCII)
```
---
## ⚠️ Catatan
- Jika tidak memiliki file audio, anda tetap bisa menjalankannya tanpa mengunduh file audio dari luar karena audio akan digenerate dari program.
- Jika ingin menggunakan audio dari luar, gunakan file WAV mono agar proses lebih akurat.
- Panjang file audio harus cukup untuk menampung pesan.
- Jika kunci belum ada, program akan otomatis membuatnya.
---
## ⚠️ Batasan dan Tips Penggunaan
### 🔒 Batas Panjang Pesan:
- Karena menggunakan enkripsi RSA 2048-bit, pesan maksimal yang bisa disisipkan adalah sekitar 190 byte (sekitar 190 karakter ASCII atau lebih sedikit untuk karakter Unicode seperti emoji atau huruf non-Latin).
- Jika pesan terlalu panjang, aplikasi akan memberi peringatan.

### 🎧 Batasan Audio:
- Pastikan file audio dalam format WAV mono (1 channel), berdurasi minimal 1 detik dengan sample rate 16kHz atau lebih.
- Jika audio terlalu pendek, proses penyisipan bisa gagal karena tidak cukup ruang untuk menyimpan pesan terenkripsi.

### 🛠 Tips:
- Gunakan audio berdurasi 2–5 detik untuk hasil yang lebih stabil.
- Jangan kompres audio ke format seperti MP3 setelah penyisipan, karena bisa merusak data tersembunyi.
- Gunakan file c.wav yang di-generate otomatis jika belum memiliki audio sendiri.

---
## 🛠 Kebutuhan
Dependensi pada `requirements.txt`:
- numpy
- scipy
- pycryptodome
- soundfile
---
## 📬 Lisensi
MIT – bebas digunakan dan dimodifikasi.

---
## 🤝 Terima Kasih
Dibuat dengan ❤️ menggunakan:
- PyCryptodome
- SciPy DCT
- SoundFile
---
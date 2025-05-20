# 🎧 Panduan Penggunaan Folder RSA

Folder `RSA/` berisi file input dan output untuk proses steganografi audio berbasis RSA + DCT.

## 📂 Struktur Folder
RSA/
├── input/ # Tempat file audio mentah (input) disimpan
│ └── c.wav # File audio yang akan disisipi pesan
├── output1/ # Tempat file stego dan kunci RSA disimpan
│ ├── stego.wav
│ ├── public.pem
│ └── private.pem
└── README.md # Panduan ini

---
## ❓ Masalah Umum: Tidak Ada File `c.wav`

Karena file audio WAV bisa sangat besar, **kami tidak menyertakan file audio dalam repositori ini** agar ukuran tetap ringan dan GitHub tidak menolak unggahan.

Namun, **kamu tetap bisa menjalankan program tanpa perlu mengunduh file besar**, dengan beberapa alternatif berikut:

---

## ✅ Solusi yang Bisa Kamu Pilih

### 🛠 1. Biarkan Program Membuat File Dummy Otomatis

Jika file `RSA/input/c.wav` tidak ditemukan saat program dijalankan, sistem akan otomatis membuat file audio dummy (1 detik, suara sine wave 440 Hz).

Tidak perlu melakukan apa pun. Cukup jalankan:

```bash
python main.py
```

Jika c.wav belum ada, kamu akan melihat pesan:

less
```bash
⚠️ Input audio not found: .../RSA/input/c.wav
🎧 Generating dummy audio file...
✅ Dummy audio saved at: .../RSA/input/c.wav
```

### 🎙️ 2. Buat Sendiri File Audio Mono Secara Manual
Jika kamu ingin menggunakan audio buatan sendiri, kamu bisa membuat file .wav mono dengan perintah berikut (butuh SoX):

```bash
sox -n -r 16000 -c 1 RSA/input/c.wav synth 1 sine 440
```

Atau gunakan audio rekaman sendiri dan ubah menjadi mono dan 16kHz (dengan tools seperti Audacity).

---
## ⚠️ Catatan Penting
- File harus berformat WAV, bukan MP3/OGG.
- Gunakan audio mono untuk hasil terbaik.
- Panjang audio menentukan jumlah data yang bisa disisipkan. Audio pendek hanya bisa menyimpan pesan singkat.

---
## 📩 Output
Setelah proses enkripsi dan penyisipan berhasil, file output akan tersedia di:

```bash
RSA/output1/stego.wav
```
Bersama dengan file kunci:
- `public.pem`
- `private.pem`

---
## 📌 Tips
- Jangan langsung menghapus file input/output. File tersebut digunakan kembali saat dekripsi.
- Jika ingin mencoba ulang, hapus stego.wav dan jalankan kembali program.

---
🛠 Dibuat agar mudah dicoba, tanpa perlu mengunduh file besar.
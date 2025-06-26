# Panduan Setup Proyek

Ikuti langkah-langkah di bawah ini untuk mengatur dan menjalankan proyek:

## 1. Membuat dan Mengaktifkan Virtual Environment Python

Disarankan untuk menggunakan virtual environment untuk mengelola dependensi proyek.

```bash
py -m venv venv
```

Untuk mengaktifkan virtual environment:

- **Di Windows:**
  ```bash
  .\venv\Scripts\activate
  ```

- **Di macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

## 2. Menginstal Dependensi

Setelah virtual environment aktif, instal semua dependensi yang diperlukan dari `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 3. Menjalankan Aplikasi Utama

Untuk menjalankan aplikasi utama, pastikan virtual environment Anda aktif, lalu jalankan:

```bash
python main.py
```

Jika semua berjalan dengan benar, Anda akan melihat output dari `main.py` di konsol Anda.

## 4. Mengakses Uji Coba Model Melalui API (FastAPI)

Setelah aplikasi utama berjalan, Anda dapat menguji model melalui antarmuka API (FastAPI).

1.  Buka peramban web Anda dan kunjungi alamat berikut untuk mengakses dokumentasi API interaktif (Swagger UI):
    -   **http://127.0.0.1:8888/docs**

2.  Pada halaman dokumentasi API, cari endpoint `POST /predict`.

3.  Klik tombol "Try it out".

4.  Pada bagian "query", masukkan teks yang ingin Anda uji. Contoh:
    ```json
    {
      "teks_baru": "Jakarta Adalah Ibukota Negara Republik Indonesia"
    }
    ```

5.  Klik tombol "Execute".

6.  Periksa "Response body" dan "Response status code". Jika "Response status code" adalah `200`, berarti semua konfigurasi berhasil dan model dapat diakses melalui API.
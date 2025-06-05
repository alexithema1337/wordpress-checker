# WordPress Login Checker
---
WordPress Login Checker adalah sebuah tool sederhana berbasis Python untuk melakukan pengecekan login pada situs WordPress secara massal menggunakan kombinasi URL, username, dan password yang diberikan. Tool ini mendukung beberapa format input dan menjalankan pengecekan secara paralel menggunakan threading.
---
## Screenshot

Berikut contoh tampilan saat menjalankan tool ini:

![Screenshot WordPress Checker](https://raw.githubusercontent.com/alexithema1337/wordpress-checker/refs/heads/main/preview.jpg)

---

## Fitur

- Mendukung berbagai format separator input (`:`, `|`, `#,@`, `@,#`).
- Multithreading untuk mempercepat proses pengecekan (maksimal 10 thread).
- Menyimpan hasil login yang berhasil ke file output.
- Tampilkan status login secara real-time dengan warna yang mudah dibaca.
- Auto-handle redirect dan captcha sederhana untuk menghindari false positive.

---

## Prasyarat

- Python 3.x
- Library `requests`

Instalasi dependencies:

```bash
pip install requests
````

---

## Cara Penggunaan

1. Siapkan file daftar target dengan format salah satu separator yang didukung, contohnya:

```
https://example.com:admin:password123
https://example.com|admin|password123
https://example.com#admin@password123
https://example.com/wp-login.php@admin#password123
```

2. Jalankan script:

```bash
python wordpress_checker.py
```

3. Ikuti instruksi input pada terminal:

* Masukkan path file list target
* Masukkan nama file hasil output
* Masukkan jumlah thread (maksimal 10)
* Pilih format separator yang sesuai dengan file list Anda

4. Script akan menjalankan pengecekan dan menampilkan hasilnya secara langsung, serta menyimpan hasil login yang berhasil ke file output.

---

## Struktur File

* `wordpress_checker.py` — Script utama untuk menjalankan pengecekan login.
* `screenshots/` — Folder tempat menyimpan screenshot demo (buat sendiri folder ini dan simpan screenshot di dalamnya).

---

## Lisensi

Hak cipta © 2025 Alexithema 1337
Distribusi bebas untuk tujuan edukasi dan riset.

---

## Kontak

* Telegram: [@avxxr00t](https://t.me/avxxr00t)

---

Selamat mencoba dan semoga bermanfaat!


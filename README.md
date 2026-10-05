# Minpro-2-DDP-Sistem-manajemen-antrian-servis-elektronik



Nama : Muhammad Fikri


Nim : 2609116095


Kelas C

-----

Program ini dibuat untuk mengelola antrian servis perangkat elektronik, sebagai contoh perangkat laptop atau hp. setiap perangkat yg masuk akan di catat dengan no antrian otomatis, nama penyervis, jenis perangkat, kerusakan perangkat, status servis, dan waktu penservis. status servis dibagi menjadi 3 yaitu menunggu, diproses, dan selesai. program ini juga memiliki 2 jenis pengguna yaitu admin dan user, sistem login, fitur CRUD, dan data disimpan permanen ke file JSON.

---

1. Program dimulai
2. Program menyiapkan daftar akun lalu membaca data antrian dari file JSON. jika file belum ada, data dimulai dari 0
3. pengguna memasukkan username dan password
4. program akan mengecek apakah username dan oassword cocok. jika salah input maksimal 3 kali, program akan berhenti, jika benar program akan lanjut ke langkah berikutnya
5. program akan mengecek jenis akun jika rolenya admin akan masuk ke menu admin (CRUD). jika bukan akan masuk ke menu user hanya bisa menambah dan melihat saja
6. menu sesuai role akan ditampilkan, lalu pengguna memilih nomor menu
7. program akan menhecek apakah pilihan yg di ketik ada, jika tidak ada program akan kembali ke menu awal dan terus berulang hingga yg dimasukkan benar
8. program akan menjalankan fitur yg dipilih jika ada perubahan data langsung tersimpan di file JSON
9. hasil proses ditampilkan misalnya tabel antrian
10. program akan mengecek apakah pengguna memilih menu 0 yaitu keluuar, jika tidak memilih menu tersebut akan kembali ke menu, jika ya program akan berakhir
11. program berhenti

<img width="534" height="794" alt="Cuplikan layar 2026-10-05 060245" src="https://github.com/user-attachments/assets/2c7893e9-64ef-4d3d-8e2f-5b76c0ef795f" />

-----

Untuk program python ini menggunakan library JSON untuk menyimpan data, library OS untuk mengecek file dan membersihkan layar, library DATETIME untuk mencatat waktu antrian dan library Getpass digunakan agar password tidak terlihat saat di input.
Untuk Struktur datanya setiap antrian akan disimpan dalam dictionary berisi nomor, nama perangkat, keluhan, status, dan waktu. semua antrian dikumpulkan dalam sebuah list bernama data_antrian. akun login juga disimpan dalam dictionary bernama user.
lalu fungsi validasi input ini berupa "input_teks" menolak input kosong, "input_angka" memakai "try_except" agar program tidak eror jika pengguna menginput huruf, "pilih_status" hanya menerima angka 1 2 atau 3



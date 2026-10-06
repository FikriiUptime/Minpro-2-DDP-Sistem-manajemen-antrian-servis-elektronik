## Minpro-2-DDP-Sistem-manajemen-antrian-servis-elektronik



**Nama : Muhammad Fikri**


**Nim : 2609116095**


**Kelas C**

-----

Program ini dibuat untuk mengelola antrian servis perangkat elektronik, sebagai contoh perangkat laptop atau hp. setiap perangkat yg masuk akan di catat dengan no antrian otomatis, nama penyervis, jenis perangkat, kerusakan perangkat, status servis, dan waktu penservis. status servis dibagi menjadi 3 yaitu menunggu, diproses, dan selesai. program ini juga memiliki 2 jenis pengguna yaitu admin dan user, sistem login, fitur CRUD, dan data disimpan permanen ke file JSON.


penjelasan flowchart
--
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


fungsi selanjutnya yaitu file JSON muat_data membaca data saat program mulai. Kalau file belum ada atau rusak, data dimulai dari kosong. simpan_data menulis data ke file setiap ada perubahan.


fungsi login. Program memakai perulangan for untuk memberi 3 kali kesempatan. Kalau username dan password cocok, program mengembalikan username beserta rolenya. Kalau gagal 3 kali, program berhenti. 


lalu fitur CRUD.

-Create, yaitu tambah_data. Pengguna mengisi nama, perangkat, dan kerusakan. Nomor antrian dibuat otomatis, status awalnya   "Menunggu", dan waktu terisi otomatis.

-Read, yaitu tampilkan_data. Semua antrian ditampilkan dalam bentuk tabel beserta total antrian.

-Update, yaitu ubah_data. Admin memilih nomor antrian, lalu mengubah status menjadi Menunggu, Diproses, atau Selesai, dan    boleh mengubah keluhan.

-Delete, yaitu hapus_data. Sebelum data dihapus, program meminta konfirmasi y atau n agar tidak terhapus karena salah input.


dan menu berdasarkan role. Menu disimpan dalam dictionary, dengan kunci berupa nomor menu dan nilai berupa label serta fungsinya. Jadi program tidak perlu if elif yang panjang. Cukup memilih menu sesuai role, lalu memanggil fungsinya.


Terakhir, fungsi main. Fungsi ini memuat data, menjalankan login, lalu menampilkan menu dalam perulangan while sampai pengguna memilih keluar.

---

## Konsep Python yang saya gunakan di program ini
 
| Konsep | Dipakai di |
|--------|-----------|
| Variabel & tipe data | `FILE_DATA`, `LEBAR`, `users`, `data_antrian` |
| List | `data_antrian` untuk menyimpan semua antrian |
| Dictionary | `users`, data tiap pelanggan, dan menu |
| Percabangan (`if-elif-else`) | `pilih_status()`, `main()`, `login()` |
| Perulangan (`for`, `while`) | `login()`, `tampilkan_data()`, `main()` |
| Fungsi | Seluruh fitur dipisah menjadi fungsi |
| Error handling (`try-except`) | `input_angka()`, `muat_data()`, `simpan_data()` |
| File handling (JSON) | `muat_data()` dan `simpan_data()` |
| Library | `json`, `os`, `datetime`, `getpass` |
 
---

## berikut hasil dari program saya

---

<img width="1919" height="1042" alt="Cuplikan layar 2026-10-06 002741" src="https://github.com/user-attachments/assets/d5a819f4-67a4-4aa8-8b3c-7a9a5ef500bd" />

gambar diatas jika user ingin menambahkan data antrian servis dengan login sebagai user



---


selanjutnya jika kita login sebagai admin, kita bisa membuka list, dan mengubah atau mengupdate status servis seperti gambar dibawah


<img width="1919" height="1036" alt="Cuplikan layar 2026-10-06 002846" src="https://github.com/user-attachments/assets/4fa09c3a-9f54-4d41-abe5-656dd4312bc0" />

<img width="1920" height="1040" alt="Cuplikan layar 2026-10-06 002918" src="https://github.com/user-attachments/assets/2184411f-81a5-434b-bac3-78a6d98e6e29" />

---


gambar dbawah jika role kita sebagai admin bisa juga menambah data antrian servis


<img width="1920" height="1040" alt="Cuplikan layar 2026-10-06 003021" src="https://github.com/user-attachments/assets/da196c5c-1745-4ab7-b730-e7454dfc670b" />

---


berikut jika status sudah di update melalui admin dan user melihat status servisan

<img width="1920" height="1040" alt="Cuplikan layar 2026-10-06 003122" src="https://github.com/user-attachments/assets/fe06f282-c1f9-4da3-8e92-32857df68d96" />


lalu disini sebagai admin kita bisa menghapus data antrian yg diinginkan seperti gambar berikut

<img width="1920" height="1040" alt="Cuplikan layar 2026-10-06 003347" src="https://github.com/user-attachments/assets/3ff6c539-af6b-4e8a-9780-55907bf57b4d" />


selanjutnya jika kita menambah antrian servis dengan role user maupun role admin akan dibuat otomatis ke file JSON seperti gambar di bawah

<img width="1920" height="1040" alt="Cuplikan layar 2026-10-06 003551" src="https://github.com/user-attachments/assets/a882a9ed-0647-41fd-bec7-20a2979d99a8" />


jika saat login salah menginput atau memasukkan role admin maupun user akan terjadi pengulangan sebanyak 3 kali dan jika gagal login program akan berhenti seperti gambar di bawah ini

<img width="409" height="394" alt="Cuplikan layar 2026-10-06 002520" src="https://github.com/user-attachments/assets/5783c07f-24ee-47a6-88b8-93ca25588776" />

---


## penjelasan singkat program saya

<img width="644" height="294" alt="Cuplikan layar 2026-10-06 000054" src="https://github.com/user-attachments/assets/5d9b9f9c-277d-4f0b-bfbb-37109f769b14" />

- FILE_DATA adalah nama file tempat data disimpan.
- LEBAR adalah lebar garis dan tabel agar tampilan rapi.
- users adalah **dictionary** berisi akun. Setiap akun punya password dan role.
- data_antrian adalah **list** kosong yang nanti diisi data pelanggan. Setiap pelanggan disimpan sebagai dictionary.

--

<img width="547" height="313" alt="Cuplikan layar 2026-10-06 011509" src="https://github.com/user-attachments/assets/0a17c68e-4f60-4ea8-98b7-e3fdb47f71a5" />

- cetak_garis() digunakan untuk mencetak garis sepanjang 85 karakter.
- tampilkan_header() di gunakan untuk mencetak judul di tengah, diapit dua garis.
- bersihkan_layar() untuk menghapus tampilan terminal. Windows menggunakan cls.

--






## sekian terimakasih

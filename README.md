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

### 1. Import Library dan Variabel Awal
<img width="644" height="294" alt="Cuplikan layar 2026-10-06 000054" src="https://github.com/user-attachments/assets/5d9b9f9c-277d-4f0b-bfbb-37109f769b14" />

- FILE_DATA adalah nama file tempat data disimpan.
- LEBAR adalah lebar garis dan tabel agar tampilan rapi.
- users adalah **dictionary** berisi akun. Setiap akun punya password dan role.
- data_antrian adalah **list** kosong yang nanti diisi data pelanggan. Setiap pelanggan disimpan sebagai dictionary.

--

### 2. Fungsi Tampilan
<img width="547" height="313" alt="Cuplikan layar 2026-10-06 011509" src="https://github.com/user-attachments/assets/0a17c68e-4f60-4ea8-98b7-e3fdb47f71a5" />

- cetak_garis() digunakan untuk mencetak garis sepanjang 85 karakter.
- tampilkan_header() di gunakan untuk mencetak judul di tengah, diapit dua garis.
- bersihkan_layar() untuk menghapus tampilan terminal. Windows menggunakan cls.

--

### 3. Fungsi Validasi Input

<img width="563" height="245" alt="Cuplikan layar 2026-10-06 050140" src="https://github.com/user-attachments/assets/29a197f3-f5fd-4fbc-a735-dae5e00c19dc" />

Fungsi ini meminta pengguna mengisi teks. Jika kosong, pengguna diminta untuk mengulang. .strip() menghapus spasi di awal dan akhir.

<img width="669" height="219" alt="Cuplikan layar 2026-10-06 050823" src="https://github.com/user-attachments/assets/445ad045-8850-4b7c-83a4-ff9834a7448e" />

Fungsi ini memakai **try-except**. Jika pengguna mengetik huruf (misalnya "abc"), Python akan error ValueError. Error tersebut di ambil, lalu program menampilkan pesan dan meminta input ulang, sehingga program tidak berhenti.

<img width="690" height="335" alt="Cuplikan layar 2026-10-06 051143" src="https://github.com/user-attachments/assets/46907ad0-7949-4093-9ca1-811cdaaad222" />

Fungsi ini digunakan saat mengubah status servis. Pengguna memilih angka 1–3 dan fungsi mengembalikan teks status yang sesuai. Selain 1/2/3 ditolak dengan **if-elif-else**.

--

### 4. Fungsi Membaca dan Menyimpan Data (JSON)

<img width="762" height="264" alt="Cuplikan layar 2026-10-06 051357" src="https://github.com/user-attachments/assets/c5e69af3-0c8b-45d8-b643-919b749334f5" />

- Jika file JSON belum ada (pertama kali program dijalankan), program mengembalikan list kosong.
- Jika file ada, isinya dibaca dengan json.load.
- Jika file rusak, program tidak error, tetapi dimulai dengan dengan data kosong.

<img width="585" height="201" alt="Cuplikan layar 2026-10-06 052809" src="https://github.com/user-attachments/assets/910ed4bf-4f99-4a5d-a831-4276c17fec66" />

Fungsi ini menulis isi data_antrian ke file JSON. indent=4 membuat isi file rapi dan mudah dibaca. Fungsi ini dipanggil setiap kali ada data yang ditambah, diubah, atau dihapus.

--

### 5. Fungsi Login

<img width="719" height="327" alt="Cuplikan layar 2026-10-06 053336" src="https://github.com/user-attachments/assets/529f5de9-6676-4ef0-ab66-5237e0688b68" />

Cara kerjanya:
1. Perulangan for berjalan **3 kali** (sisa = 2, 1, 0), jadi pengguna punya 3 kali kesempatan.
2. Pengguna mengisi username dan password. Password memakai getpass sehingga tidak terlihat saat diketik.
3. Program mengecek: apakah username ada di users **dan** password-nya cocok?
4. Jika cocok, fungsi mengembalikan data akun (username dan role).
5. Jika 3 kali salah, fungsi mengembalikan None dan program berhenti.

### 6. Fungsi Pencarian dan Nomor Otomatis

<img width="555" height="288" alt="image" src="https://github.com/user-attachments/assets/37a59ede-f75a-41e5-ba31-05deb293ffbe" />

- cari_antrian() mencari data berdasarkan nomor antrian. Jika ketemu, data dikembalikan. Jika tidak, hasilnya None.
- nomor_berikutnya() membuat nomor antrian baru. Jika data masih kosong, nomornya 1. Jika sudah ada, diambil dari nomor terbesar lalu ditambah 1. Cara ini menjamin nomor tidak bentrok walaupun ada data yang dihapus.

--

### 7. CREATE, Tambah Data

<img width="690" height="335" alt="Cuplikan layar 2026-10-06 054249" src="https://github.com/user-attachments/assets/3eb9b2be-c793-46a1-a69d-e4e165d286cb" />

Pengguna mengisi nama, jenis perangkat, dan kerusakan. Data lain dibuat otomatis:

- no > nomor antrian otomatis
- status > selalu diawali **"Menunggu"**
- waktu > tanggal dan jam saat ini

Data dimasukkan ke list dengan append() lalu disimpan ke JSON.

--

### 8. READ, Tampilkan Data

<img width="676" height="349" alt="Cuplikan layar 2026-10-06 054608" src="https://github.com/user-attachments/assets/2cb20c7d-f8ab-443a-bbe1-2985402a93a1" />

- Jika data kosong, muncul tulisan "Belum ada data antrian" dan fungsi mengembalikan False.
- Jika ada data, ditampilkan dalam bentuk tabel. Tanda :<15 artinya teks rata kiri dengan lebar 15 karakter, supaya kolom sejajar.
- Fungsi mengembalikan True jika ada data. Nilai True/False ini dipakai fungsi ubah dan hapus untuk mengecek apakah ada data yang bisa diproses.

--

### 9. UPDATE, Ubah Data (Role Admin)

<img width="746" height="395" alt="image" src="https://github.com/user-attachments/assets/d0503d20-a03c-45a9-9209-72a6b7a52f59" />

Langkah-langkahnya:
1. Tampilkan semua data. Jika kosong, berhenti.
2. Minta nomor antrian yang ingin diubah.
3. Cari datanya. Jika tidak ada, tampilkan pesan dan berhenti.
4. Tampilkan data saat ini, lalu pilih status baru.
5. Keluhan boleh diubah. Jika dikosongkan (tekan ENTER), keluhan lama dipertahankan.
6. Simpan ke JSON.

--

### 10. DELETE, Hapus Data (Role Admin)

<img width="765" height="387" alt="Cuplikan layar 2026-10-06 060124" src="https://github.com/user-attachments/assets/d686c58a-b86d-40fb-a357-3e94ef501928" />

Sebelum menghapus, program meminta **konfirmasi** (y/n) agar data tidak terhapus karena salah input. Jika y, data dihapus dengan remove() lalu disimpan. Jika bukan, penghapusan dibatalkan.

## 11. Menu berdasarkan Role

<img width="564" height="345" alt="Cuplikan layar 2026-10-06 060555" src="https://github.com/user-attachments/assets/050156aa-9233-48b4-9ad4-12ff5a98936f" />

Menu dibuat dalam bentuk **dictionary**. Kuncinya adalah nomor menu, nilainya berisi pasangan **(nama menu, fungsi yang dijalankan)**. Dengan cara ini program tidak perlu menulis banyak if-elif untuk setiap menu. Dictionary MENU_PER_ROLE memilih menu mana yang dipakai sesuai role pengguna.

--

## 12.Fungsi utama 'main()'

<img width="775" height="637" alt="image" src="https://github.com/user-attachments/assets/543db4d9-3a31-4120-b0ce-e98a6c4a5be2" />

Ini ialah "otak" program, urutannya sama dengan flowchart:
1. Muat data dari JSON.
2. Jalankan login. Jika gagal 3 kali, program berhenti.
3. Pilih menu sesuai role (admin atau user).
4. Masuk perulangan while True yang menampilkan menu terus-menerus.
5. Jika pilihan 0 > keluar (break). Jika pilihan ada di menu > jalankan fungsinya. Jika tidak > tampilkan "Pilihan tidak valid".
6. Setelah selesai, pengguna menekan ENTER untuk kembali ke menu.

<img width="686" height="214" alt="image" src="https://github.com/user-attachments/assets/07c407ba-aa26-4bec-934a-aafbd2cdab91" />

Bagian ini menjalankan main() hanya jika file dijalankan langsung. Jika pengguna menekan Ctrl + C, program berhenti dengan pesan yang rapi, bukan error yang panjang.

--

## sekian terimakasih

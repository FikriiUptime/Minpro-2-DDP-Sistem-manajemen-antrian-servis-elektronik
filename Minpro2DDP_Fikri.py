import json                      
import os                        
from datetime import datetime    
from getpass import getpass      

FILE_DATA = "data_antrian.json"
LEBAR = 85

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
}

data_antrian = []

def cetak_garis():
    print("-" * LEBAR)


def tampilkan_header(judul):
    cetak_garis()
    print(judul.center(LEBAR))
    cetak_garis()


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def input_teks(prompt):
    """Input teks, tidak boleh kosong."""
    while True:
        nilai = input(prompt).strip()
        if nilai == "":
            print(">> Input tidak boleh kosong. Coba lagi.")
        else:
            return nilai


def input_angka(prompt):
    """Input angka dengan error handling (try-except)."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(">> Input harus berupa angka. Coba lagi.")


def pilih_status():
    """Memilih status baru dengan validasi conditional."""
    print("1. Menunggu\n2. Diproses\n3. Selesai")
    while True:
        pilihan = input("Pilih status (1/2/3): ").strip()
        if pilihan == "1":
            return "Menunggu"
        elif pilihan == "2":
            return "Diproses"
        elif pilihan == "3":
            return "Selesai"
        else:
            print(">> Pilihan tidak valid, masukkan 1, 2, atau 3.")


def muat_data():
    if not os.path.exists(FILE_DATA):
        return []
    try:
        with open(FILE_DATA, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print(">> File data rusak/tidak terbaca, memulai dengan data kosong.")
        return []


def simpan_data():
    try:
        with open(FILE_DATA, "w", encoding="utf-8") as f:
            json.dump(data_antrian, f, indent=4)
    except OSError:
        print(">> Gagal menyimpan data ke file.")


def login():
    """Login maksimal 3 kali. Mengembalikan dictionary akun atau None."""
    tampilkan_header("LOGIN SISTEM ANTRIAN SERVIS ELEKTRONIK")
    for sisa in range(2, -1, -1):
        username = input_teks("Username : ")
        password = getpass("Password : ")

        if username in users and users[username]["password"] == password:
            print(f">> Login berhasil. Selamat datang, {username} "
                  f"({users[username]['role']}).")
            return {"username": username, "role": users[username]["role"]}
        print(f">> Username/password salah. Sisa percobaan: {sisa}\n")
    return None

def cari_antrian(nomor):
    for item in data_antrian:
        if item["no"] == nomor:
            return item
    return None


def nomor_berikutnya():
    if len(data_antrian) == 0:
        return 1
    return max(item["no"] for item in data_antrian) + 1


def tambah_data(): 
    tampilkan_header("TAMBAH DATA ANTRIAN SERVIS")
    data_baru = {
        "no": nomor_berikutnya(),
        "nama": input_teks("Nama Pelanggan  : "),
        "perangkat": input_teks("Jenis Perangkat : "),
        "keluhan": input_teks("Kerusakan       : "),
        "status": "Menunggu",
        "waktu": datetime.now().strftime("%d-%m-%Y %H:%M"),
    }
    data_antrian.append(data_baru)
    simpan_data()
    print(f">> Data berhasil ditambahkan. No. Antrian: {data_baru['no']}")


def tampilkan_data():                                # READ
    tampilkan_header("DAFTAR ANTRIAN SERVIS ELEKTRONIK")
    if len(data_antrian) == 0:
        print("Belum ada data antrian.")
        return False
    print(f"{'No':<5}{'Nama':<15}{'Perangkat':<15}{'Keluhan':<22}"
          f"{'Status':<10}{'Waktu':<18}")
    cetak_garis()
    for d in data_antrian:
        print(f"{d['no']:<5}{d['nama']:<15}{d['perangkat']:<15}"
              f"{d['keluhan']:<22}{d['status']:<10}{d['waktu']:<18}")
    cetak_garis()
    print(f"Total antrian: {len(data_antrian)}")
    return True


def ubah_data():
    if not tampilkan_data():
        return
    nomor = input_angka("Masukkan No. Antrian yang diubah: ")
    item = cari_antrian(nomor)
    if item is None:
        print(f">> Data No. {nomor} tidak ditemukan.")
        return

    print(f"\nData saat ini: {item['nama']} | {item['perangkat']} | "
          f"{item['keluhan']} | {item['status']}")
    item["status"] = pilih_status()
    keluhan_baru = input("Update keluhan (kosongkan jika tidak berubah): ").strip()
    if keluhan_baru != "":
        item["keluhan"] = keluhan_baru
    simpan_data()
    print(">> Data berhasil diubah.")


def hapus_data():
    if not tampilkan_data():
        return
    nomor = input_angka("Masukkan No. Antrian yang dihapus: ")
    item = cari_antrian(nomor)
    if item is None:
        print(f">> Data No. {nomor} tidak ditemukan.")
        return

    konfirmasi = input(f"Yakin hapus data No. {nomor}? (y/n): ").strip().lower()
    if konfirmasi == "y":
        data_antrian.remove(item)
        simpan_data()
        print(">> Data berhasil dihapus.")
    else:
        print(">> Penghapusan dibatalkan.")

def lihat_data():
    tampilkan_data()

MENU_ADMIN = {
    "1": ("Tambah Data Antrian", tambah_data),
    "2": ("Tampilkan Semua Data", tampilkan_data),
    "3": ("Ubah Data Antrian", ubah_data),
    "4": ("Hapus Data Antrian", hapus_data),
}

MENU_USER = {
    "1": ("Daftar Antrian Servis", tambah_data),
    "2": ("Lihat Daftar Antrian", lihat_data),
}

MENU_PER_ROLE = {"admin": MENU_ADMIN, "user": MENU_USER}


def main():
    global data_antrian
    data_antrian = muat_data()

    akun = login()
    if akun is None:
        print(">> Gagal login 3 kali. Program berhenti.")
        return

    menu = MENU_PER_ROLE[akun["role"]]

    while True:
        tampilkan_header(f"MENU {akun['role'].upper()} - ANTRIAN SERVIS ELEKTRONIK")
        for kode, (label, _) in menu.items():
            print(f"{kode}. {label}")
        print("0. Keluar")
        cetak_garis()

        pilihan = input("Pilih menu: ").strip()
        if pilihan == "0":
            print(">> Terima kasih telah menggunakan sistem ini.")
            break
        elif pilihan in menu:
            menu[pilihan][1]()
        else:
            print(">> Pilihan tidak valid!")

        input("\nTekan ENTER untuk kembali ke menu...")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n>> Program dihentikan oleh pengguna.")

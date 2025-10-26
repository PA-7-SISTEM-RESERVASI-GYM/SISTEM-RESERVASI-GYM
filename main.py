import os
import json
from pwinput import pwinput
from prettytable import PrettyTable
from datetime import datetime

os.system('cls' if os.name == 'nt' else 'clear')

def menu_utama():

    print("================================================================")
    print("|                           Menu Utama                         |")
    print("================================================================")
    print("| 1. Login                                                     |")
    print("| 2. Registrasi                                                |")
    print("| 3. Keluar Aplikasi                                           |")
    print("================================================================")
    pilihan_utama = input("Masukkan pilihan Anda : ")

    while True:
        if pilihan_utama == '1':
            login()
        elif pilihan_utama == '2':
            registrasi()
            menu_utama() 
        elif pilihan_utama == '3':
            print("Keluar dari aplikasi.")
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            menu_utama()

def registrasi():
    print("================================================================")
    print("|                         Registrasi                           |")
    print("================================================================")
    try:
        with open('users.json', 'r') as f:
            data_users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data_users = []
    username = input("Masukkan username baru: ")
    while any(u["username"].lower() == username.lower() for u in data_users):
        print("Username sudah digunakan. Silakan pilih username lain.")
        username = input("Masukkan username baru: ")
    password = pwinput("Masukkan password: ")
    konfirmasi_password = pwinput("Konfirmasi password: ")
    while konfirmasi_password != password:
        print("Password tidak cocok! Silakan ulangi.")
        password = pwinput("Masukkan password: ")
        konfirmasi_password = pwinput("Konfirmasi password: ")
    id_user = f"U{len(data_users) + 1:03d}"
    data_users.append({
        "id_user": id_user,
        "username": username,
        "password": password,
        "saldo": 0 
    })
    with open('users.json', 'w') as f:
        json.dump(data_users, f, indent=4)
    print("\nRegistrasi berhasil!")
    print(f"Selamat datang, {username}!\n")
    print("Silakan login untuk melanjutkan.\n")

def login():
    kesempatan = 3
    while kesempatan > 0:
    # os.system('cls' if os.name == 'nt' else 'clear')
        print("================================================================")
        print("|                           Menu Login                         |")
        print("================================================================")
        username = input("Masukkan username : ")
        password = pwinput("Masukkan password : ")
        with open('login.json', 'r') as file:
            data_login = json.load(file)
        if username in data_login and password == data_login[username]['pass']:
            print("Login berhasil!")
            if username == 'admin':
                print("Selamat datang, Admin!")
            admin()  # panggil menu admin
            break
        else:
            with open('users.json', 'r') as file:
                data_users = json.load(file)
                # cari username di users.json
                found = None
                for u in data_users:
                    if u["username"] == username and u["password"] == password:
                        found = u
                        break
                if found:
                    print(f"\nLogin berhasil! Selamat datang, {found['username']}!")
                    menu_user(found["username"])  # panggil menu user beneran
                    break
                else:
                    kesempatan -= 1
                    print("\nUsername atau password salah!")
                    if kesempatan > 0:
                        print(f"Kesempatan tersisa: {kesempatan}")
                    else:
                        print("Maaf, kesempatan Anda habis!")
                        exit()

def admin():
    print("================================================================")
    print("|                           Menu Admin                         |")
    print("================================================================")
    print("| 1. Manajemen Produk                                          |")
    print("| 2. Manajemen Membership                                      |")
    print("| 3. Manajemen Reservasi                                       |")
    print("| 4. Manajemen Top Up                                          |")
    print("| 5. Kembali                                                   |")
    print("================================================================")

    while True:
        pilihan_admin = input("Masukkan pilihan Anda : ")
        if pilihan_admin == '1':
            manajemen_produk()
        elif pilihan_admin == '2':
            manajemen_member()
        elif pilihan_admin == '3':
            manajemen_reservasi()
        elif pilihan_admin == '4':
            manajemen_topup()
        elif pilihan_admin == '5':
            menu_utama()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            pilihan_admin = input("Masukkan pilihan Anda : ")

# Manajemen Produk
def manajemen_produk():
    print("================================================================")
    print("|                      Manajemen Produk                        |")
    print("================================================================")
    print("| 1. Lihat Produk                                              |")
    print("| 2. Tambah Produk                                             |")
    print("| 3. Edit Produk                                               |")
    print("| 4. Hapus Produk                                              |")
    print("| 5. Kembali                                                   |")
    print("================================================================")
    json_file = 'produk.json'
    while True:
        pilihan_admin = input("Masukkan pilihan Anda : ")
        if pilihan_admin == '1':
            Lihat_produk(json_file)
            manajemen_produk()
        elif pilihan_admin == '2':
            Tambah_produk(json_file)
            manajemen_produk()
        elif pilihan_admin == '3':
            edit_produk(json_file)
            manajemen_produk()
        elif pilihan_admin == '4':
            Hapus_produk(json_file)
            manajemen_produk()
        elif pilihan_admin == '5':
            admin()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def Lihat_produk(json_file):
    print("================================================================")
    print("|                      Daftar Produk Tersedia                  |")
    print("================================================================")
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    if not data:
        print("\nBelum ada produk yang tersimpan.\n")
        return data
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Produk", "Harga", "Stok", "Kategori"]
    for item in data:
        tabel.add_row([
            item.get("id", "-"),
            item.get("nama_produk", "-"),
            item.get("harga", "-"),
            item.get("stok", "-"),
            item.get("kategori", "-")
        ])
    print(tabel)
    return data

def Tambah_produk(json_file):
    print("================================================================")
    print("|                      Tambah Produk                           |")
    print("================================================================")
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = [] 
    Id = input("Masukkan ID produk: ")
    nama_produk = input("Masukkan nama produk: ")
    while True:
        try:
            harga = int(input("Masukkan harga: "))
            if harga < 0:
                print("Angka tidak boleh negatif!")
            else:
                break
        except ValueError:
            print("Tolong masukkan angka yag benar ya!")
    while True:
        try:
            stok = int(input("Masukkan stok: "))
            if stok  < 0:
                print("Angka tidak boleh negatif!")
            else:
                break
        except ValueError:
            print("Tolong masukkan angka yag benar ya!")
    kategori = input("Masukkan kategori: ")
    for item in data:
        if item.get("id") == Id or item.get("nama_produk").lower() == nama_produk.lower():
            print("\nProduk sudah ada!\n")
            return
    data.append({
        "id": Id,
        "nama_produk": nama_produk,
        "harga": harga,
        "stok": stok,
        "kategori": kategori
    })
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)
    print("\nProduk Baru berhasil ditambahkan!")
    Lihat_produk(json_file)

def edit_produk(json_file):
    print("================================================================")
    print("|                      Edit Produk                             |")
    print("================================================================")
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File tidak ditemukan!")
        return
    data = Lihat_produk(json_file)
    Id = input("Masukkan ID produk yang ingin diedit: ")
    found = False
    for item in data:
        if item.get("id") == Id:
            found = True
            print("\nData lama:")
            for kunci, nilai in item.items():
                print(f"- {kunci}: {nilai}")
            print("\nTekan ENTER jika ingin lewati ya!.\n")
            nama_produk = input(f"Masukkan nama produk [{item.get('nama_produk')}]: ") or item.get("nama_produk")
            while True:
                harga_input = input(f"Masukkan harga [{item.get('harga')}]: ")
                if harga_input.strip() == "":
                    harga = item.get("harga")
                    break
                try:
                    harga = int(harga_input)
                    if harga < 0:
                        print("Angka tidak boleh negatif!")
                    else:
                        break
                except ValueError:
                    print("Tolong masukkan angka yang benar ya!")
            while True:
                stok = input(f"Masukkan stok [{item.get('stok')}]: ")
                if stok.strip() == "":
                    stok = item.get("stok")
                    break
                try:
                    stok = int(stok)
                    if stok < 0:
                        print("Angka tidak boleh negatif!")
                    else:
                        break
                    break
                except ValueError:
                    print("Tolong masukkan angka yang benar ya!")
            kategori = input(f"Masukkan kategori produk [{item.get('kategori')}]: ") or item.get("kategori")
            item.update({
                "nama_produk": nama_produk,
                "harga": harga,
                "stok": stok,
                "kategori": kategori
            })
            break  
    if found:
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)
        print("\nProduk berhasil diedit!\n")
    else:
        print("\nProduk dengan ID tersebut tidak ditemukan!\n")

def Hapus_produk(json_file):
    print("================================================================")
    print("|                      Hapus Produk                            |")
    print("================================================================")
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = [] 
    data = Lihat_produk(json_file)
    Id = input("Masukkan ID produk yang ingin dihapus: ")
    found = False
    for item in data:
        if item.get("id") == Id:
            found = True
            data.remove(item)
    konfirmasi = input("Konfirmasi hapus (ya/tidak): ").lower()
    if konfirmasi == "tidak":
        print("Batal Menghapus Produk")
        return
    elif found:
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)
        print("\nProduk berhasil dihapus!\n")
        Lihat_produk(json_file)
    else:
        print("\nProduk dengan ID tersebut tidak ditemukan!\n")

# Manajemen Membership
def manajemen_member():
    print("================================================================")
    print("|                      Manajemen Membership                    |")
    print("================================================================")
    print("| 1. Lihat Membership                                          |")
    print("| 2. Tambah Membership                                         |")
    print("| 3. Edit Membership                                           |")
    print("| 4. Hapus Membership                                          |")
    print("| 5. Kembali                                                   |")
    print("================================================================")
    json_file2 = 'member.json'
    while True:
        pilihan_admin = input("Masukkan pilihan Anda : ")
        if pilihan_admin == '1':
            Lihat_member(json_file2)
            manajemen_member()
        elif pilihan_admin == '2':
            Tambah_member(json_file2)
            manajemen_member()
        elif pilihan_admin == '3':
            Edit_member(json_file2)
            manajemen_member()
        elif pilihan_admin == '4':
            Hapus_member(json_file2)
            manajemen_member()
        elif pilihan_admin == '5':
            admin()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def Lihat_member(json_file2):
    print("================================================================")
    print("|              Daftar Paket Membership Tersedia                |")
    print("================================================================")
    try:
        with open(json_file2, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    if not data:
        print("\nBelum ada paket membership yang tersimpan.\n")
        return data
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Paket", "Durasi", "Harga", "Stok", "Deskripsi"]
    for item in data:
        tabel.add_row([
            item.get("id", "-"),
            item.get("nama_paket", "-"),
            item.get("durasi", "-"),
            item.get("harga", "-"),
            item.get("stok", "-"),
            item.get("deskripsi", "-")
        ])
    print(tabel)
    return data

def Tambah_member(json_file2):
    print("================================================================")
    print("|                  Tambah Paket Membership                     |")
    print("================================================================")
    try:
        with open(json_file2, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = [] 
    Id = input("Masukkan ID paket membership: ")
    nama_paket = input("Masukkan nama paket: ")
    durasi = input("Masukkan lama durasi: ")
    while True:
        try:
            harga = int(input("Masukkan harga: "))
            if harga < 0:
                print("Angka tidak boleh negatif!")
            else:
                break
        except ValueError:
            print("Tolong masukkan angka yag benar ya!")
    while True:
        try:
            stok = int(input("Masukkan stok: "))
            if stok  < 0:
                print("Angka tidak boleh negatif!")
            else:
                break
        except ValueError:
            print("Tolong masukkan angka yag benar ya!")
    deskripsi = input("Masukkan deskripsi: ")
    for item in data:
        if item.get("id") == Id or item.get("nama_paket").lower() == nama_paket.lower():
            print("\nPaket sudah ada!\n")
            return
    data.append({
        "id": Id,
        "nama_paket": nama_paket,
        "durasi": durasi,
        "harga": harga,
        "stok": stok,
        "deskripsi": deskripsi
    })
    with open(json_file2, 'w') as f:
        json.dump(data, f, indent=4)
    print("\nPaket Membership Baru berhasil ditambahkan!")
    Lihat_member(json_file2)

def Edit_member(json_file2):
    print("================================================================")
    print("|                    Edit Paket Membership                     |")
    print("================================================================")
    try:
        with open(json_file2, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File tidak ditemukan!")
        return
    data = Lihat_member(json_file2)
    Id = input("Masukkan ID paket membership yang ingin diedit: ")
    found = False
    for item in data:
        if item.get("id") == Id:
            found = True
            print("\nData lama:")
            for kunci, nilai in item.items():
                print(f"- {kunci}: {nilai}")
            print("\nTekan ENTER jika ingin lewati ya!.\n")
            nama_paket = input(f"Masukkan nama paket membership [{item.get('nama_paket')}]: ") or item.get("nama_paket")
            durasi = input(f"Masukkan lama durasi [{item.get('durasi')}]: ") or item.get("durasi")
            while True:
                harga_input = input(f"Masukkan harga [{item.get('harga')}]: ")
                if harga_input.strip() == "":
                    harga = item.get("harga")
                    break
                try:
                    harga = int(harga_input)
                    if harga < 0:
                        print("Angka tidak boleh negatif!")
                    else:
                        break
                except ValueError:
                    print("Tolong masukkan angka yang benar ya!")
            while True:
                stok = input(f"Masukkan stok [{item.get('stok')}]: ")
                if stok.strip() == "":
                    stok = item.get("stok")
                    break
                try:
                    stok = int(stok)
                    if stok < 0:
                        print("Angka tidak boleh negatif!")
                    else:
                        break
                    break
                except ValueError:
                    print("Tolong masukkan angka yang benar ya!")
            deskripsi = input(f"Masukkan deskripsi [{item.get('deskripsi')}]: ") or item.get("deskripsi")
            item.update({
                "nama_paket": nama_paket,
                "durasi": durasi,
                "harga": harga,
                "stok": stok,
                "deskripsi": deskripsi
            })
            break  
    if found:
        with open(json_file2, 'w') as f:
            json.dump(data, f, indent=4)
        print("\nPaket berhasil diedit!\n")
    else:
        print("\nPaket dengan ID tersebut tidak ditemukan!\n")

def Hapus_member(json_file2):
    print("================================================================")
    print("|                   Hapus Paket Membership                     |")
    print("================================================================")
    try:
        with open(json_file2, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = [] 
    data = Lihat_member(json_file2)
    Id = input("Masukkan ID paket membership yang ingin dihapus: ")
    found = False
    for item in data:
        if item.get("id") == Id:
            found = True
            data.remove(item)
    konfirmasi = input("Konfirmasi hapus (ya/tidak): ").lower()
    if konfirmasi == "tidak":
        print("Batal Menghapus Paket Membership")
        return
    elif found:
        with open(json_file2, 'w') as f:
            json.dump(data, f, indent=4)
        print("\nPaket berhasil dihapus!\n")
        Lihat_member(json_file2)
    else:
        print("\nPaket dengan ID tersebut tidak ditemukan!\n")

# Manajemen Reservasi
def manajemen_reservasi():
    print("================================================================")
    print("|                      Manajemen Reservasi                     |")
    print("================================================================")
    print("| 1. Lihat Reservasi                                           |")
    print("| 2. Tambah Reservasi                                          |")
    print("| 3. Edit Reservasi                                            |")
    print("| 4. Hapus Reservasi                                           |")
    print("| 5. Kembali                                                   |")
    print("================================================================")
    json_file1 = 'reservasi.json'
    while True:
        pilihan_admin = input("Masukkan pilihan Anda : ")
        if pilihan_admin == '1':
            Lihat_reservasi(json_file1)
            manajemen_reservasi()
        elif pilihan_admin == '2':
            Tambah_reservasi(json_file1)
            manajemen_reservasi()
        elif pilihan_admin == '3':
            edit_reservasi(json_file1)
            manajemen_reservasi()
        elif pilihan_admin == '4':
            Hapus_reservasi(json_file1)
            manajemen_reservasi()
        elif pilihan_admin == '5':
            admin()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def Lihat_reservasi(json_file1):
    print("================================================================")
    print("|                      Daftar Kelas Tersedia                   |")
    print("================================================================")
    try:
        with open(json_file1, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    if not data:
        print("\nBelum ada kelas yang tersimpan.\n")
        return data
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Kelas", "Hari", "Waktu", "Trainer", "Kapasitas", "Harga", "Lokasi", "Peserta Terdaftar"]
    for item in data:
        tabel.add_row([
            item.get("id", "-"),
            item.get("nama_kelas", "-"),
            item.get("hari", "-"),
            item.get("waktu", "-"),
            item.get("trainer", "-"),
            item.get("kapasitas", "-"),
            item.get("harga", "-"),
            item.get("lokasi", "-"),
            item.get("peserta_terdaftar", "-")
        ])
    print(tabel)
    return data

def Tambah_reservasi(json_file1):
    print("================================================================")
    print("|                      Tambah Reservasi                        |")
    print("================================================================")
    try:
        with open(json_file1, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = [] 
    Id = input("Masukkan ID kelas: ")
    nama_kelas = input("Masukkan nama kelas: ")
    hari = input("Masukkan hari: ")
    waktu = input("Masukkan waktu kelas: ")
    trainer = input("Masukkan nama trainer: ")
    while True:
        try:
            kapasitas = int(input("Masukkan kapasitas: "))
            if kapasitas < 0:
                print("Angka tidak boleh negatif!")
            else:
                break
        except ValueError:
            print("Tolong masukkan angka yag benar ya!")
    while True:
        try:
            harga = int(input("Masukkan harga: "))
            if harga < 0:
                print("Angka tidak boleh negatif!")
            else:
                break
        except ValueError:
            print("Tolong masukkan angka yag benar ya!")
    lokasi = input("Masukkan lokasi kelas: ")
    while True:
        try:
            peserta_terdaftar = int(input("Masukkan peserta yang sudah terdaftar: "))
            if peserta_terdaftar < 0:
                print("Angka tidak boleh negatif!")
            else:
                break
        except ValueError:
            print("Tolong masukkan angka yag benar ya!")
    for item in data:
        if item.get("id") == Id or item.get("nama_kelas").lower() == nama_kelas.lower():
            print("\nKelas sudah ada!\n")
            return
    data.append({
        "id": Id,
        "nama_kelas": nama_kelas,
        "hari": hari,
        "waktu": waktu,
        "trainer": trainer,
        "kapasitas": kapasitas,
        "harga": harga,
        "lokasi": lokasi,
        "peserta_terdaftar": peserta_terdaftar
    })
    with open(json_file1, 'w') as f:
        json.dump(data, f, indent=4)
    print("\nKelas Baru berhasil ditambahkan!")
    Lihat_reservasi(json_file1)

def edit_reservasi(json_file1):
    print("================================================================")
    print("|                      Edit Reservasi                          |")
    print("================================================================")
    try:
        with open(json_file1, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File tidak ditemukan!")
        return
    data = Lihat_reservasi(json_file1)
    Id = input("Masukkan ID kelas yang ingin diedit: ")
    found = False
    for item in data:
        if item.get("id") == Id:
            found = True
            print("\nData lama:")
            for kunci, nilai in item.items():
                print(f"- {kunci}: {nilai}")
            print("\nTekan ENTER jika ingin lewati ya!.\n")
            nama_kelas = input(f"Masukkan nama kelas [{item.get('nama_kelas')}]: ") or item.get("nama_kelas")
            hari = input(f"Masukkan hari [{item.get('hari')}]: ") or item.get("hari")
            waktu = input(f"Masukkan waktu kelas [{item.get('waktu')}]: ") or item.get("waktu")
            trainer = input(f"Masukkan nama trainer [{item.get('trainer')}]: ") or item.get("trainer")
            while True:
                kapasitas_input = input(f"Masukkan kapasitas [{item.get('kapasitas')}]: ")
                if kapasitas_input.strip() == "":
                    kapasitas = item.get("kapasitas")
                    break
                try:
                    kapasitas = int(kapasitas_input)
                    if kapasitas < 0:
                        print("Angka tidak boleh negatif!")
                    else:
                        break
                except ValueError:
                    print("Tolong masukkan angka yang benar ya!")
            while True:
                harga_input = input(f"Masukkan harga [{item.get('harga')}]: ")
                if harga_input.strip() == "":
                    harga = item.get("harga")
                    break
                try:
                    harga = int(harga_input)
                    if harga < 0:
                        print("Angka tidak boleh negatif!")
                    else:
                        break
                except ValueError:
                    print("Tolong masukkan angka yang benar ya!")
            lokasi = input(f"Masukkan lokasi kelas [{item.get('lokasi')}]: ") or item.get("lokasi")
            while True:
                peserta_input = input(f"Masukkan peserta yang sudah terdaftar [{item.get('peserta_terdaftar')}]: ")
                if peserta_input.strip() == "":
                    peserta_terdaftar = item.get("peserta_terdaftar")
                    break
                try:
                    peserta_terdaftar = int(peserta_input)
                    if peserta_terdaftar < 0:
                        print("Angka tidak boleh negatif!")
                    else:
                        break
                except ValueError:
                    print("Tolong masukkan angka yang benar ya!")
            item.update({
                "nama_kelas": nama_kelas,
                "hari": hari,
                "waktu": waktu,
                "trainer": trainer,
                "kapasitas": kapasitas,
                "harga": harga,
                "lokasi": lokasi,
                "peserta_terdaftar": peserta_terdaftar
            })
            break  
    if found:
        with open(json_file1, 'w') as f:
            json.dump(data, f, indent=4)
        print("\nKelas berhasil diedit!\n")
    else:
        print("\nKelas dengan ID tersebut tidak ditemukan!\n")

def Hapus_reservasi(json_file1):
    print("================================================================")
    print("|                      Hapus Reservasi                         |")
    print("================================================================")
    try:
        with open(json_file1, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = [] 
    data = Lihat_reservasi(json_file1)
    Id = input("Masukkan ID kelas yang ingin dihapus: ")
    found = False
    for item in data:
        if item.get("id") == Id:
            found = True
            data.remove(item)
    konfirmasi = input("Konfirmasi hapus (ya/tidak): ").lower()
    if konfirmasi == "tidak":
        print("Batal Menghapus Kelas")
        return
    elif found:
        with open(json_file1, 'w') as f:
            json.dump(data, f, indent=4)
        print("\nKelas berhasil dihapus!\n")
        Lihat_reservasi(json_file1)
    else:
        print("\nKelas dengan ID tersebut tidak ditemukan!\n")

# Manajemen Topup
def manajemen_topup():
    print("================================================================")
    print("|                    Manajemen Top Up Saldo                    |")
    print("================================================================")
    print("| 1. Lihat Daftar Top Up                                       |")
    print("| 2. Tambah Kode Top Up                                        |")
    print("| 3. Edit Kode Top Up                                          |")
    print("| 4. Hapus Kode Top Up                                         |")
    print("| 5. Kembali                                                   |")
    print("================================================================")
    json_file4 = 'topup.json'
    while True:
        pilihan_admin = input("Masukkan pilihan Anda : ")
        if pilihan_admin == '1':
            Lihat_topup(json_file4)
            manajemen_topup()
        elif pilihan_admin == '2':
            Tambah_topup(json_file4)
            manajemen_topup()
        elif pilihan_admin == '3':
            Edit_topup(json_file4)
            manajemen_topup()
        elif pilihan_admin == '4':
            Hapus_topup(json_file4)
            manajemen_topup()
        elif pilihan_admin == '5':
            admin()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def Lihat_topup(json_file4):
    print("================================================================")
    print("|                         Daftar Top Up                        |")
    print("================================================================")
    try:
        with open(json_file4, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    if not data:
        print("\nBelum ada data kode top up yang tersimpan.\n")
        return data
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Kode Top Up", "Nominal"]
    for item in data:
        tabel.add_row([
            item.get("id_topup", "-"),
            item.get("kode_topup", "-"),
            item.get("nominal", "-")
        ])
    print(tabel)
    return data

def Tambah_topup(json_file4):
    print("================================================================")
    print("|                        Tambah Top up                         |")
    print("================================================================")
    try:
        with open(json_file4, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = [] 
    Id = input("Masukkan ID top up: ")
    kode = input("Masukkan kode top up: ")
    while True:
        try:
            nominal = int(input("Masukkan nominal: "))
            if nominal < 0:
                print("Angka tidak boleh negatif!")
            else:
                break
        except ValueError:
            print("Tolong masukkan angka yag benar ya!")
    for item in data:
        if item.get("id_topup") == Id or item.get("kode_topup").lower() == kode.lower():
            print("\nKode Top up dengan ID tersebut sudah ada!\n")
            return
    data.append({
        "id_topup": Id,
        "kode_topup": kode,
        "nominal": nominal
    })
    with open(json_file4, 'w') as f:
        json.dump(data, f, indent=4)
    print("\nTop Up Baru berhasil ditambahkan!")
    Lihat_topup(json_file4)

def Edit_topup(json_file4):
    print("================================================================")
    print("|                      Edit Data Top Up                        |")
    print("================================================================")
    try:
        with open(json_file4, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("File tidak ditemukan!")
        return
    data = Lihat_topup(json_file4)
    Id = input("Masukkan ID Top Up yang ingin diedit: ")
    found = False
    for item in data:
        if item.get("id_topup") == Id:
            found = True
            print("\nData lama:")
            for kunci, nilai in item.items():
                print(f"- {kunci}: {nilai}")
            print("\nTekan ENTER jika ingin lewati ya!.\n")
            kode = input(f"Masukkan koe topup [{item.get('kode_topup')}]: ") or item.get("kode_topup")
            while True:
                nominal_input = input(f"Masukkan nominal [{item.get('nominal')}]: ")
                if nominal_input.strip() == "":
                    nominal = item.get("nominal")
                    break
                try:
                    nominal = int(nominal_input)
                    if nominal < 0:
                        print("Angka tidak boleh negatif!")
                    else:
                        break
                except ValueError:
                    print("Tolong masukkan angka yang benar ya!")
            item.update({
                "kode_topup": kode,
                "nominal": nominal,
            })
            break  
    if found:
        with open(json_file4, 'w') as f:
            json.dump(data, f, indent=4)
        print("\nData Top Up berhasil diedit!\n")
    else:
        print("\nData Top Up dengan ID tersebut tidak ditemukan!\n")

def Hapus_topup(json_file4):
    print("================================================================")
    print("|                     Hapus Data Top Up                        |")
    print("================================================================")
    try:
        with open(json_file4, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = [] 
    data = Lihat_topup(json_file4)
    Id = input("Masukkan ID data top up yang ingin dihapus: ")
    found = False
    for item in data:
        if item.get("id_topup") == Id:
            found = True
            data.remove(item)
    konfirmasi = input("Konfirmasi hapus (ya/tidak): ").lower()
    if konfirmasi == "tidak":
        print("Batal Menghapus Data Top Up")
        return
    if found:
        with open(json_file4, 'w') as f:
            json.dump(data, f, indent=4)
        print("\nData Top Up berhasil dihapus!\n")
        Lihat_topup(json_file4)
    else:
        print("\nData Top Up dengan ID tersebut tidak ditemukan!\n")

def load_json(nama_file):
    try:
        with open(nama_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_json(nama_file, data):
    with open(nama_file, 'w') as f:
        json.dump(data, f, indent=4)

def menu_user(username):
    print("================================================================")
    print("|                        Menu User                             |")
    print("================================================================")
    print("| 1. Beli Produk                                               |")
    print("| 2. Reservasi                                                 |")
    print("| 3. Top Up Saldo                                              |")
    print("| 4. Lihat Invoice                                             |")
    print("| 5. Kembali                                                   |")
    print("================================================================")

    while True:
        pilihan_member = input("Masukkan pilihan Anda : ")
        if pilihan_member == '1':
            beli_produk(username)
            struk_terbaru(username)
            menu_user(username)
        elif pilihan_member == '2':
            reservasi_kelas(username)
            struk_terbaru(username)
            menu_user(username)
        elif pilihan_member == '3':
            top_up_saldo(username)
            menu_user(username)
        elif pilihan_member == '4':
            lihat_invoice(username)
            menu_user(username)
        elif pilihan_member == '5':
            menu_utama()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            pilihan_member = input("Masukkan pilihan Anda : ")

def beli_produk(username):
    print("================================================================")
    print("|                      Daftar Produk Tersedia                  |")
    print("================================================================")
    produk = load_json('produk.json')
    users = load_json('users.json')
    invoice = load_json('invoice.json')
    user = next((u for u in users if u["username"] == username), None)
    if not user:
        print("User tidak ditemukan.")
        return
    if not produk:
        print("Belum ada produk tersedia.")
        return
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Produk", "Harga", "Stok", "Kategori"]
    for p in produk:
        tabel.add_row([p["id"], p["nama_produk"], p["harga"], p["stok"], p["kategori"]])
    print(tabel)
    id_produk = input("Masukkan ID produk yang ingin dibeli: ").strip()
    item = next((p for p in produk if p["id"] == id_produk), None)
    if not item:
        print("Produk tidak ditemukan!")
        return
    if item["stok"] <= 0:
        print("Stok produk habis!")
        return
    while True:
        try:
            jumlah = int(input("Masukkan jumlah produk yang ingin dibeli: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0.")
            elif jumlah > item["stok"]:
                print("Stok tidak cukup!")
            else:
                break
        except ValueError:
            print("Masukkan angka yang valid.")
    total = jumlah * item["harga"]
    print(f"Total harga: Rp{total:,}")
    konfirmasi = input("Konfirmasi pembelian (ya/tidak): ").lower()
    if konfirmasi == "tidak":
        print("Pembelian dibatalkan.")
        return
    elif user["saldo"] < total:
        print("Saldo tidak cukup!")
        menu_user(username)
        return
    else:
        user["saldo"] -= total
        item["stok"] -= jumlah
    id_invoice = f"INV{len(invoice)+1:03d}"
    invoice.append({
        "id_invoice": id_invoice,
        "id_user": user["id_user"],
        "username": user["username"],
        "tanggal": datetime.now().strftime("%Y-%m-%d"),
        "jenis_transaksi": "Produk",
        "deskripsi": item["nama_produk"],
        "jumlah": jumlah,
        "total": total
    })
    save_json('users.json', users)
    save_json('produk.json', produk)
    save_json('invoice.json', invoice)
    print(f"Pembelian berhasil! Saldo tersisa: Rp{user['saldo']:,}")
    print(f"Invoice berhasil dibuat dengan ID: {id_invoice}")

def reservasi_kelas(username):
    print("================================================================")
    print("|                           Reservasi                          |")
    print("================================================================")
    users = load_json('users.json')
    kelas = load_json('reservasi.json')
    invoice = load_json('invoice.json')
    user = next((u for u in users if u["username"] == username), None)
    if not user:
        print("User tidak ditemukan.")
        return
    if not kelas:
        print("Belum ada kelas tersedia.")
        return
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Kelas", "Hari", "Waktu", "Trainer", "Harga", "Kapasitas", "Peserta"]
    for k in kelas:
        tabel.add_row([k["id"], k["nama_kelas"], k["hari"], k["waktu"], k["trainer"], k["harga"], k["kapasitas"], k["peserta_terdaftar"]])
    print(tabel)
    id_kelas = input("Masukkan ID kelas yang ingin dipesan: ").strip()
    item = next((k for k in kelas if k["id"] == id_kelas), None)
    if not item:
        print("Kelas tidak ditemukan!")
        return
    if item["peserta_terdaftar"] >= item["kapasitas"]:
        print("Kelas penuh!")
        return
    while True:
        try:
            jumlah = int(input("Masukkan jumlah orang yang akan reservasi: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0.")
            elif jumlah > item["kapasitas"]:
                print("Kapasitas tidak cukup!")
            else:
                break
        except ValueError:
            print("Masukkan angka yang valid.")
    total = jumlah * item["harga"]
    print(f"Total harga: Rp{total:,}")
    konfirmasi = input(f"Biaya reservasi Rp{item['harga']:,}. Konfirmasi (ya/tidak): ").lower()
    if konfirmasi == "tidak":
        print("Reservasi dibatalkan.")
        return
    elif user["saldo"] < item["harga"]:
        print("Saldo tidak cukup!")
        menu_user(username)
        return
    else:
        user["saldo"] -= item["harga"]
        item["peserta_terdaftar"] += 1
    id_invoice = f"INV{len(invoice)+1:03d}"
    invoice.append({
        "id_invoice": id_invoice,
        "id_user": user["id_user"],
        "username": user["username"],
        "tanggal": datetime.now().strftime("%Y-%m-%d"),
        "jenis_transaksi": "Kelas",
        "deskripsi": item["nama_kelas"],
        "jumlah": jumlah,
        "total": total
    })
    save_json('users.json', users)
    save_json('reservasi.json', kelas)
    save_json('invoice.json', invoice)
    print(f"Reservasi berhasil! Saldo tersisa: Rp{user['saldo']:,}")

def top_up_saldo(username):
    topup = load_json('topup.json')
    users = load_json('users.json')
    user = next((u for u in users if u["username"].lower() == username.lower()), None)
    if not user:
        print("User tidak ditemukan.")
        return
    print(f"\nSaldo saat ini: Rp{user['saldo']:,}")
    kode = input("Masukkan kode top-up: ").strip().upper()
    data_topup = next((t for t in topup if t["kode_topup"].upper() == kode), None)
    if not data_topup:
        print("Kode top-up tidak valid atau tidak ditemukan.")
        return
    nominal = data_topup["nominal"]
    print(f"Nominal top-up: Rp{nominal:,}")
    konfirmasi = input("Konfirmasi top-up (ya/tidak): ").strip().lower()
    if konfirmasi == "tidak":
        print("Top-up dibatalkan.")
        return
    else:
        user["saldo"] += nominal
        save_json('users.json', users)
    print("Top-up berhasil!")
    print(f"Saldo baru: Rp{user['saldo']:,}")

def struk_terbaru(username):
    invoices = load_json('invoice.json')
    user_invoices = [i for i in invoices if i.get("username", "").lower() == username.lower()]
    invoice_terbaru = user_invoices[-1]
    print("\n==================== STRUK TRANSAKSI ====================")
    print(f"ID Invoice     : {invoice_terbaru['id_invoice']}")
    print(f"Tanggal        : {invoice_terbaru['tanggal']}")
    print(f"Nama Pelanggan : {username}")
    print("----------------------------------------------------------")
    print(f"Jenis Transaksi: {invoice_terbaru['jenis_transaksi']}")
    print(f"Deskripsi      : {invoice_terbaru['deskripsi']}")
    print(f"Jumlah Item    : {invoice_terbaru['jumlah']}")
    print(f"Total Harga    : Rp{invoice_terbaru['total']:,}")
    print("----------------------------------------------------------")
    print(f"Waktu Cetak    : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("==========================================================")
    print("     Terima kasih telah bertransaksi di GymFit!\n")

def lihat_invoice(username):
    invoices = load_json('invoice.json')
    user_invoices = [i for i in invoices if i.get("username", "").lower() == username.lower()]
    if not user_invoices:
        print("Belum ada transaksi untuk user ini.")
        return
    print("\n==================== STRUK TRANSAKSI ====================")
    print(f"Nama Pelanggan : {username}")
    print(f"Tanggal Cetak  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("==========================================================")
    total_semua = 0
    for inv in user_invoices:
        print(f"ID Invoice     : {inv['id_invoice']}")
        print(f"Tanggal        : {inv['tanggal']}")
        print(f"Jenis Transaksi: {inv['jenis_transaksi']}")
        print(f"Deskripsi      : {inv['deskripsi']}")
        print(f"Jumlah Item    : {inv['jumlah']}")
        print(f"Total Harga    : Rp{inv['total']:,}")
        print("----------------------------------------------------------")
        total_semua += inv['total']
    print(f"Total Keseluruhan: Rp{total_semua:,}")
    print("==========================================================")
    print("Terima kasih telah bertransaksi di GymFit!\n")

while True:
    try:
        menu_utama()
        break
    except KeyboardInterrupt:
        print("\nJangan tekan-tekan Ctrl + C ya!")
    except EOFError:
        print("\nJangan tekan-tekan Ctrl + Z ya!")

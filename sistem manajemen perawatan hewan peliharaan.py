import json
import os
import time
import pwinput
import sys
from prettytable import PrettyTable
os.system("cls")

def clear():
    os.system("cls")

# ===============================================================
# +                       DATABASE PRODUK                       +
# ===============================================================
def bacadata():
    if not os.path.exists("data HAE.json"):
        data = {"produk": []}
        with open("data HAE.json", "w") as file:
            json.dump(data, file, indent=4)
        return data
    
    with open("data HAE.json", "r") as file:
        data = json.load(file)
    
    if "produk" not in data:
        data["produk"] = []
        with open("data HAE.json", "w") as file:
            json.dump(data, file, indent=4)
    
    return data
    
def simpanproduk(data):
    with open("data HAE.json", "w") as file:
        json.dump({"produk": data.get("produk", [])}, file, indent=4)

# ===============================================================
# +                       DATABASE USER + HEWAN                 +
# ===============================================================
def bacadatauser():
    try:
        with open("users.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return {"akunuser": [], "datahewan": []}
    
    if isinstance(data, list):
        data = {"akunuser": data, "datahewan": []}
    
    if "akunuser" not in data:
        data["akunuser"] = []
    if "datahewan" not in data:
        data["datahewan"] = []
    
    return data

def simpanuser(data):
    if "akunuser" not in data:
        data["akunuser"] = []
    if "datahewan" not in data:
        data["datahewan"] = []
    with open("users.json", "w") as file:
        json.dump(data, file, indent=4)

# ===============================================================
# +                       REGISTER/DAFTAR                       +
# ===============================================================

def register():
    datauser = bacadatauser()

    usernamvalid = False
    while not usernamvalid:
        try:
            username = input("username baru: ").strip()
            if len(username) < 3 or len(username) > 20:
                clear()
                print("minimal 3 - 20 karakter")
            elif any(u['username'] == username for u in datauser["akunuser"]):
                clear()
                print("username sudah digunakan")
            else:
                usernamvalid = True
        except (ValueError, KeyboardInterrupt):
            clear()
            print("\n===============================================================")
            print("+                      INPUT TIDAK VALID                      +")
            print("===============================================================")
            return

    passvalid = False
    while not passvalid:
        try:
            password = input("password baru: ").strip()
            if len(password) < 3 or len(password) > 16:
                clear()
                print("minimal 3 - 16 karakter")
            else:
                passvalid = True
        except (ValueError, KeyboardInterrupt):
            clear()
            print("\n===============================================================")
            print("+                      INPUT TIDAK VALID                      +")
            print("===============================================================")
            return

    datauser["akunuser"].append({
        "username": username,
        "password": password,
        "role": "user",
        "saldo": 0,
        "hewan": [],
        "keranjang": []
    })
    simpanuser(datauser)
    print("data berhasil dibuat")
    input("enter untuk kembali")
    clear()

# ===============================================================
# +                          LOGIN/MASUK                        +
# ===============================================================
def masuk():
    kesempatan = 3
    while kesempatan > 0:
        try:
            username = input("masukkan username: ").strip()
            password = pwinput.pwinput("masukkan password: ").strip()

            if len(username or password) < 3 or len(username or password) > 20:
                clear()
                print("minimal 3 - 20 karakter")
                continue
            else:
                data = bacadatauser()
                for user in data["akunuser"]:
                    if user["username"] == username and user["password"] == password:
                        if "keranjang" not in data:
                            user["keranjang"] = []
                        print(f"\nSELAMAT DATANG ==> {username} <==")
                        time.sleep(2)
                        clear()
                        return user
                kesempatan -= 1
                print(f"\nLogin gagal! Sisa percobaan: {kesempatan}")
                if kesempatan == 0:
                    print("Tunggu 5 detik untuk mencoba lagi...")
                    for detik in range(5, 0, -1):
                        sys.stdout.write(f"\r{detik} detik...")
                        sys.stdout.flush()
                        time.sleep(1)
                    kesempatan = 3
                    clear()
                continue

        except (ValueError, KeyboardInterrupt):
            clear()
            print("\n===============================================================")
            print("+                      INPUT TIDAK VALID                      +")
            print("===============================================================")
            return None
    return None

# ===============================================================
# +                        MENU UTAMA                           +
# ===============================================================
def menuutama():
    while True:
        try:
            print("================================================================")
            print("|+  S E L A M A T   D A T A N G   D I  H A E   P E T S H O P  +|")
            print("================================================================")
            print("\n===========================================================")
            print("+                      1. Daftar                          +")
            print("+                      2. Masuk                           +")
            print("+                      3. keluar                          +")
            print("===========================================================")

            pilihan = input("pilih menu (1/2/3): ").strip()

            if pilihan == "":
                clear()
                print("=========================================")
                print("|        INPUT TIDAK BOLEH KOSONG       |")
                print("=========================================\n")
                continue
            elif not pilihan.isdigit():
                clear()
                print("=========================================")
                print("|          INPUT ANDA TIDAK VALID       |")
                print("=========================================\n")
                continue
            elif pilihan == '1':
                clear()
                register()
            elif pilihan == '2':
                clear()
                user = masuk()
                if user is not None:
                    if user['role'] == 'admin':
                        adminmenu()
                    else:
                        menuuser(user)
            elif pilihan == '3':
                clear()
                print("=================================================")
                print("| TERIMA KASIH TELAH BERKUNJUNG KE HAE PETSHOP |")
                print("=================================================")
                break
            else:
                clear()
                print("=========================================")
                print("|          INPUT ANDA TIDAK VALID       |")
                print("=========================================")

        except(ValueError,KeyboardInterrupt):
            clear()
            print("\n===============================================================")
            print("+                      INPUT TIDAK VALID                      +")
            print("===============================================================")
            menuutama()

# ===============================================================
# +                        MENU ADMIN                           +
# ===============================================================
def adminmenu():
    while True:
        try:
            print("================================================================")
            print("|+  S E L A M A T   D A T A N G   D I  H A E   P E T S H O P  +|")
            print("================================================================")
            print("\n===========================================================")
            print("+                      MENU ADMIN                         +")
            print("===========================================================")
            print("+                      1. tambah data                     +")
            print("+                      2. lihat data                      +")
            print("+                      3. ubah data                       +")
            print("+                      4. hapus data                      +")
            print("+                      5. kembali                         +")
            print("===========================================================")

            pilihan = input("pilih menu (1/2/3/4/5): ").strip()

            if pilihan == "":
                clear()
                print("=========================================")
                print("|        INPUT TIDAK BOLEH KOSONG       |")
                print("=========================================")
                continue
            elif not pilihan.isdigit():
                clear()
                print("=========================================")
                print("|          INPUT ANDA TIDAK VALID       |")
                print("=========================================")
            elif pilihan == '1':
                while True:
                    clear()
                    print("1. Tambah Barang\n2. Tambah Hewan\n3. Kembali")
                    p = input("Pilih: ").strip()
                    if p == "1":
                        clear()
                        tambahbarang()
                        break
                    elif p == "2":
                        clear()
                        tambahhewanadmin()
                        break
                    elif p == "3":
                        clear()
                        break
                    else:
                        print(" Pilihan tidak valid!")
                        time.sleep(1)
            elif pilihan == '2':
                clear()
                lihatdata()
            elif pilihan == '3':
                while True:
                    clear()
                    print("1. Ubah Data Barang\n2. Ubah Data Hewan\n3. Kembali")
                    p = input("Pilih: ").strip()
                    if p == "1":
                        clear()
                        ubahbarang()
                        break
                    elif p == "2":
                        clear()
                        ubahhewan()
                        break
                    elif p == "3":
                        clear()
                        break
                    else:
                        print(" Pilihan tidak valid!")
                        time.sleep(1)
            elif pilihan == '4':
                while True:
                    clear()
                    print("1. Hapus Data Barang\n2. Hapus Data Hewan\n3. Kembali")
                    p = input("Pilih: ").strip()
                    if p == "1":
                        clear()
                        hapusbarang()
                        break
                    elif p == "2":
                        clear()
                        hapushewan()
                        break
                    elif p == "3":
                        clear()
                        break
                    else:
                        print(" Pilihan tidak valid!")
                        time.sleep(1)
            elif pilihan == '5':
                clear()
                menuutama()
                return
            else:
                clear()
                print("=========================================")
                print("|          INPUT ANDA TIDAK VALID       |")
                print("=========================================")

        except(ValueError,KeyboardInterrupt):
            clear()
            print("\n===============================================================")
            print("+                      INPUT TIDAK VALID                      +")
            print("===============================================================")
            input("                    tekan enter untuk lanjut.....              ")
            clear()
        adminmenu()

"======================================================================================================================================="
def tambahbarang():
    data = bacadata()

    namavalid = False
    while not namavalid:
        nama = input("Nama barang: ").strip()
        if nama == "":
            print(" Tidak boleh kosong!")
        else:
            namavalid = True

    kategorivalid = False
    while not kategorivalid:
        print("KATEGORI: ")
        print("1. kebutuhan")
        print("2. makanan")
        kategori = input("pilih kategori: ").strip()
        if kategori == "":
            print(" Tidak boleh kosong!")
        elif kategori == '1':
            kategori = "kebutuhan"
            kategorivalid = True
        elif kategori == '2':
            kategori = "makanan"
            kategorivalid = True
        else:
            print(" Pilih 1 atau 2")

    print("minimal harga Rp10.000 dan maksimal harga Rp2.000.000")
    hargavalid = False
    while not hargavalid:
        try:
            harga = int(input("Harga: Rp"))
            if harga < 10000 or harga > 2000000:
                print("harga dimulai dari Rp10.000 - Rp2.000.000")
            else:
                hargavalid = True
        except ValueError:
            print("> input anda tidak valid!")

    print("\n--- DATA BARANG ---")
    print(f"Nama     : {nama}")
    print(f"Kategori : {kategori}")
    print(f"Harga    : Rp{harga:,}")
    konfirmasi = input("\nApakah data sudah benar? (y/n): ").strip().lower()
    if konfirmasi == 'y':
        data["produk"].append({"nama": nama, "kategori": kategori, "harga": harga})
        simpanproduk(data)
        print("> Barang berhasil ditambahkan!")
    else:
        print("> Penambahan barang dibatalkan.")
    input("Enter untuk kembali...")
    clear()
    adminmenu()
"======================================================================================================================================="

"======================================================================================================================================="
def tambahhewanadmin():
    datauser = bacadatauser()

    namavalid = False
    while not namavalid:
        nama = input("Nama hewan: ").strip()
        if nama == "":
            print("> Tidak boleh kosong!")
        else:
            namavalid = True

    jenisvalid = False
    while not jenisvalid:
        jenis = input("Jenis: ").strip()
        if jenis == "":
            print("> Tidak boleh kosong!")
        else:
            jenisvalid = True

    umurvalid = False
    while not umurvalid:
        try:
            umur = int(input("Umur (bulan, 5-24): "))
            if umur < 5 or umur > 24:
                print("> Umur harus 5–24 bulan!")
            else:
                umurvalid = True
        except ValueError:
            print("> input anda tidak valid!")

    pemilikvalid = False
    while not pemilikvalid:
        pemilik = input("Pemilik (username): ").strip()
        if pemilik == "":
            print("> Tidak boleh kosong!")
        else:
            pemilikvalid = True

    print("\n--- DATA HEWAN ---")
    print(f"Nama     : {nama}")
    print(f"Jenis    : {jenis}")
    print(f"Umur     : {umur} bulan")
    print(f"Pemilik  : {pemilik}")
    konfirmasi = input("\nApakah data sudah benar? (y/n): ").strip().lower()
    if konfirmasi == 'y':
        datauser["datahewan"].append({
            "nama": nama, "jenis": jenis, "umur": umur, "pemilik": pemilik
        })
        for user in datauser["akunuser"]:
            if user["username"] == pemilik:
                if nama not in user["hewan"]:
                    user["hewan"].append(nama)
                break
        simpanuser(datauser)
        print("> Hewan berhasil ditambahkan!")
        input("Enter...")
        clear()
        adminmenu()
    else:
        print("> Penambahan hewan dibatalkan.")
    input("Enter untuk kembali...")
    clear()
"======================================================================================================================================="

"======================================================================================================================================="
def lihatdata():
    clear()
    dataproduk = bacadata()
    datauser = bacadatauser()
    
    print("=== DATA BARANG ===")
    if dataproduk["produk"]:
        tabel = PrettyTable(["No", "Nama", "Kategori", "Harga"])
        for i, p in enumerate(dataproduk["produk"], 1):
            tabel.add_row([i, p["nama"], p["kategori"], f"Rp{p['harga']:,}"])
        print(tabel)
    else:
        print("Belum ada barang.")

    print("\n=== DATA HEWAN ===")
    if datauser["datahewan"]:
        tabel = PrettyTable(["No", "Nama", "Jenis", "Umur (bulan)", "Pemilik"])
        for i, h in enumerate(datauser["datahewan"], 1):
            tabel.add_row([i, h["nama"], h["jenis"], h["umur"], h["pemilik"]])
        print(tabel)
    else:
        print("Belum ada hewan.")
    input("\nEnter untuk kembali...")
    clear()
    adminmenu()
"======================================================================================================================================="

"======================================================================================================================================="
def ubahbarang():
    data = bacadata()
    if not data["produk"]:
        print("Tidak ada barang!")
        input("Enter..."); return
    tabel = PrettyTable(["No", "Nama", "Kategori", "Harga"])
    for i, p in enumerate(data["produk"], 1):
        tabel.add_row([i, p["nama"], p["kategori"], f"Rp{p['harga']:,}"])
    print(tabel)
    try:
        no = int(input("Nomor barang yang diubah: ")) - 1
        if 0 <= no < len(data["produk"]):
            p = data["produk"][no]
            nama = input(f"Nama ({p['nama']}): ").strip()
            kategorivalid = False
            while not kategorivalid:
                print("KATEGORI: ")
                print("1. kebutuhan")
                print("2. makanan")
                kategoriinput = input(f"Kategori ({p['kategori']}): ").strip()
                if kategoriinput == "":
                    kategori = p["kategori"]
                    kategorivalid = True
                elif kategoriinput == '1':
                    kategori = "kebutuhan"
                    kategorivalid = True
                elif kategoriinput == '2':
                    kategori = "makanan"
                    kategorivalid = True
                else:
                    print("> Pilih 1 atau 2!")
            print("minimal harga Rp10.000 dan maksimal harga Rp2.000.000")
            hargavalid = False
            while not hargavalid:
                try:
                    hargainput = input(f"Harga saat ini: Rp{p['harga']:,}\nMasukkan harga baru (kosong untuk tidak ubah): Rp")
                    if hargainput == "":
                        harga = p["harga"]
                        hargavalid = True
                    else:
                        harga = int(hargainput)
                        if harga < 10000 or harga > 2000000:
                            print("harga dimulai dari 10.000 - 2.000.000")
                        else:
                            hargavalid = True
                except ValueError:
                    print("> Harga harus angka!")
            print("\n--- DATA BARU ---")
            print(f"Nama     : {nama if nama else p['nama']}")
            print(f"Kategori : {kategori}")
            print(f"Harga    : Rp{harga:,}")
            konfirmasi = input("\nApakah data sudah benar? (y/n): ").strip().lower()
            if konfirmasi == 'y':
                p["nama"] = nama if nama else p["nama"]
                p["kategori"] = kategori
                p["harga"] = harga
                simpanproduk(data)
                print("Barang diupdate!")
                input("Enter...")
                clear()
                adminmenu()
            else:
                print("Perubahan dibatalkan.")
        else:
            clear()
            print("Nomor tidak valid!")
    except ValueError:
        print("Input tidak valid!")
    input("Enter...")
    clear()
    ubahbarang()
"======================================================================================================================================="

"======================================================================================================================================="
def ubahhewan():
    datauser = bacadatauser()
    if not datauser["datahewan"]:
        print("> Tidak ada hewan!")
        input("Enter..."); return
    tabel = PrettyTable(["No", "Nama", "Jenis", "Umur (bulan)", "Pemilik"])
    for i, h in enumerate(datauser["datahewan"], 1):
        tabel.add_row([i, h["nama"], h["jenis"], h["umur"], h["pemilik"]])
    print(tabel)
    try:
        no = int(input("Nomor hewan yang diubah: ")) - 1
        if 0 <= no < len(datauser["datahewan"]):
            h = datauser["datahewan"][no]
            nama = input(f"Nama ({h['nama']}): ").strip()
            jenis = input(f"Jenis ({h['jenis']}): ").strip()
            umurvalid = False
            while not umurvalid:
                try:
                    umurinput = input(f"Umur ({h['umur']}): ").strip()
                    if umurinput == "":
                        umur = h["umur"]
                    else:
                        umur = int(umurinput)
                    if 5 <= umur <= 24:
                        umurvalid = True
                    else:
                        print("> Umur harus 5–24 bulan!")
                except ValueError:
                    print("> Umur harus angka!")
            pemilik = input(f"Pemilik ({h['pemilik']}): ").strip()
            print("\n--- DATA HEWAN BARU ---")
            print(f"Nama     : {nama if nama else h['nama']}")
            print(f"Jenis    : {jenis if jenis else h['jenis']}")
            print(f"Umur     : {umur} bulan")
            print(f"Pemilik  : {pemilik if pemilik else h['pemilik']}")
            konfirmasi = input("\nApakah data sudah benar? (y/n): ").strip().lower()
            if konfirmasi == 'y':
                h["nama"] = nama if nama else h["nama"]
                h["jenis"] = jenis if jenis else h["jenis"]
                h["umur"] = umur
                h["pemilik"] = pemilik if pemilik else h["pemilik"]
                if pemilik != h["pemilik"]:
                    for user in datauser["akunuser"]:
                        if user["username"] == h["pemilik"]:
                            if h["nama"] in user["hewan"]:
                                user["hewan"].remove(h["nama"])
                            break
                    for user in datauser["akunuser"]:
                        if user["username"] == pemilik:
                            if h["nama"] not in user["hewan"]:
                                user["hewan"].append(h["nama"])
                            break
                simpanuser(datauser)
                print(" Hewan diupdate")
                input("Enter...")
                clear()
                adminmenu()
            else:
                print(">Perubahan dibatalkan")
        else:
            clear()
            print("Nomor tidak valid!")
    except ValueError:
        print("Input tidak valid!")
    input("Enter...")
    clear()
    ubahhewan()
"======================================================================================================================================="

"======================================================================================================================================="
def hapusbarang():
    data = bacadata()
    if not data["produk"]:
        print(" Tidak ada barang")
        input("Enter..."); return
    tabel = PrettyTable(["No", "Nama", "Kategori", "Harga"])
    for i, p in enumerate(data["produk"], 1):
        tabel.add_row([i, p["nama"], p["kategori"], f"Rp{p['harga']:,}"])
    print(tabel)
    try:
        no = int(input("Nomor barang yang dihapus: ")) - 1
        if 0 <= no < len(data["produk"]):
            data["produk"].pop(no)
            simpanproduk(data)
            print("> Barang dihapus!")
            input("Enter...")
            clear()
            adminmenu()
        else:
            clear()
            print("> Nomor tidak valid!")
    except ValueError:
        print("> Input tidak valid!")
    input("Enter...")
    clear()
    hapusbarang()
"======================================================================================================================================="

"======================================================================================================================================="
def hapushewan():
    datauser = bacadatauser()
    if not datauser["datahewan"]:
        print("> Tidak ada hewan!")
        input("Enter..."); return
    tabel = PrettyTable(["No", "Nama", "Jenis", "Umur (bulan)", "Pemilik"])
    for i, h in enumerate(datauser["datahewan"], 1):
        tabel.add_row([i, h["nama"], h["jenis"], h["umur"], h["pemilik"]])
    print(tabel)
    try:
        no = int(input("Nomor hewan yang dihapus: ")) - 1
        if 0 <= no < len(datauser["datahewan"]):
            hewandihapus = datauser["datahewan"][no]
            namahewan = hewandihapus["nama"]
            pemilik = hewandihapus["pemilik"]
            for user in datauser["akunuser"]:
                if user["username"] == pemilik:
                    if namahewan in user["hewan"]:
                        user["hewan"].remove(namahewan)
                    break
            datauser["datahewan"].pop(no)
            simpanuser(datauser)
            print("> Hewan dihapus!")
            input("Enter...")
            clear()
            adminmenu()
        else:
            clear()
            print("> Nomor tidak valid!")
    except ValueError:
        print("> Input tidak valid!")
    input("Enter...")
    clear()
"======================================================================================================================================="

# ===============================================================
# +                        MENU USER                            +
# ===============================================================
def menuuser(user):
    while True:
        clear()
        print("================================================================")
        print("|+  S E L A M A T   D A T A N G   D I  H A E   P E T S H O P  +|")
        print("================================================================")
        print("\n===========================================================")
        print("+                      MENU USER                          +")
        print("===========================================================")
        print("+                   1. kelola hewan                       +")
        print("+                   2. belanja kebutuhan hewan            +")
        print("+                   3. perawatan                          +")
        print("+                   4. rincian pembelian                  +")
        print("+                   5. transaksi                         +")
        print("+                   6. kembali                            +")
        print("===========================================================")

        pilihan = input("pilih menu (1/2/3/4/5/6): ").strip()

        if pilihan == "":
            clear()
            print("=========================================")
            print("|        INPUT TIDAK BOLEH KOSONG       |")
            print("=========================================")
        elif not pilihan.isdigit():
            clear()
            print("=========================================")
            print("|          INPUT ANDA TIDAK VALID       |")
            print("=========================================")
        elif pilihan == '1':
            clear()
            kelolahewan(user)
        elif pilihan == '2':
            clear()
            belanja(user)
        elif pilihan == '3':
            clear()
            perawatan(user)
        elif pilihan == '4':
            clear()
            rincianpembelian(user)
        elif pilihan == '5':
            clear()
            transaksi(user)
        elif pilihan == '6':
            clear()
            return
        else:
            clear()
            print("=========================================")
            print("|          INPUT ANDA TIDAK VALID       |")
            print("=========================================")

"======================================================================================================================================="
def daftarhewan(user):
    datauser = bacadatauser()

    namavalid = False
    while not namavalid:
        nama = input("Nama hewan: ").strip()
        if nama == "":
            print("Tidak boleh kosong!")
        else:
            namavalid = True

    jenisvalid = False
    while not jenisvalid:
        jenis = input("Jenis: ").strip()
        if jenis == "":
            print("Tidak boleh kosong!")
        else:
            jenisvalid = True

    umurvalid = False
    while not umurvalid:
        try:
            umur = int(input("Umur (bulan): "))
            if umur <= 0:
                print("> Umur harus > 0!")
            else:
                umurvalid = True
        except ValueError:
            print("Umur harus angka")

    print("\n--- DATA HEWAN ---")
    print(f"Nama     : {nama}")
    print(f"Jenis    : {jenis}")
    print(f"Umur     : {umur} bulan")
    konfirmasi = input("\nApakah data sudah benar? (y/n): ").strip().lower()
    if konfirmasi == 'y':
        datauser["datahewan"].append({
            "nama": nama, "jenis": jenis, "umur": umur, "pemilik": user["username"]
        })
        for u in datauser["akunuser"]:
            if u["username"] == user["username"]:
                u["hewan"].append(nama)
                break
        simpanuser(datauser)
        print("> Hewan berhasil didaftarkan!")
    else:
        print("> Pendaftaran hewan dibatalkan.")
    input("Enter...")
    clear()
"======================================================================================================================================="

"======================================================================================================================================="
def lihathewansaya(user):
    datauser = bacadatauser()
    hewansaya = [h for h in datauser["datahewan"] if h["pemilik"] == user["username"]]
    if hewansaya:
        tabel = PrettyTable(["No", "Nama", "Jenis", "Umur (bulan)"])
        for i, h in enumerate(hewansaya, 1):
            tabel.add_row([i, h["nama"], h["jenis"], h["umur"]])
        print(tabel)
    else:
        print("> Anda belum memiliki hewan.")
    input("Enter...")
    clear()

def kelolahewan(user):
    while True:
        print("1. Daftarkan Hewan\n2. Lihat Hewan Saya\n3. Kembali")
        pilih = input("Pilih: ").strip()
        if pilih == "1":
            clear()
            daftarhewan(user)
        elif pilih == "2":
            clear()
            lihathewansaya(user)
        elif pilih == "3":
            clear()
            break
        else:
            print("> Pilihan tidak valid!")
            time.sleep(1)
            clear()
"======================================================================================================================================="

"======================================================================================================================================="
def belanja(user):
    data = bacadata()
    if not data["produk"]:
        print("> Belum ada produk.")
        input("Enter...")
        clear()
        return

    tabel = PrettyTable(["No", "Nama", "Kategori", "Harga"])
    for i, p in enumerate(data["produk"], 1):
        tabel.add_row([i, p["nama"], p["kategori"], f"Rp{p['harga']:,}"])
    print(tabel)

    try:
        no = int(input("Pilih nomor barang (0 untuk batal): ")) - 1
        if no == -1:
            return
        if 0 <= no < len(data["produk"]):
            barang = data["produk"][no]
            jumlahvalid = False
            while not jumlahvalid:
                try:
                    jumlah = int(input("Jumlah (1-10): "))
                    if 1 <= jumlah <= 10:
                        jumlahvalid = True
                    else:
                        print(" input anda tidak benar!")
                except ValueError:
                    print(" Input harus angka!")

            user["keranjang"].append({
                "jenis": "barang",
                "nama": barang["nama"],
                "harga": barang["harga"],
                "jumlah": jumlah
            })
            print(f"> {jumlah}x {barang['nama']} ditambahkan ke keranjang!")
        else:
            print("> Nomor tidak valid!")
    except ValueError:
        print("> Input tidak valid!")
    input("Enter...")
    clear()
    menuuser(user)
"======================================================================================================================================="

"======================================================================================================================================="
def perawatan(user):
    print("================================================================")
    print("|+  S E L A M A T   D A T A N G   D I  H A E   P E T S H O P  +|")
    print("================================================================")
    print("\n===========================================================")
    print("+                      MENU PERAWATAN                     +")
    print("===========================================================")
    
    layanan = [
        {"nama": "Vaksin", "deskripsi": "Paket vaksinasi lengkap untuk melindungi hewan dari penyakit umum.", "harga": 75000},
        {"nama": "Grooming", "deskripsi": "Paket perawatan bulu, kuku, dan kebersihan hewan peliharaan.", "harga": 150000},
        {"nama": "Check Up Kesehatan", "deskripsi": "Pemeriksaan kesehatan hewan secara menyeluruh", "harga": 200000}
    ]
    
    tabel = PrettyTable(["No", "Layanan", "Deskripsi", "Harga"])
    for i, l in enumerate(layanan, 1):
        tabel.add_row([i, l["nama"], l["deskripsi"], f"Rp{l['harga']:,}"])
    print(tabel)
    print("===========================================================")

    pilih = input("Pilih layanan (1-3) atau 0 untuk kembali: ").strip()
    if pilih in ["1", "2", "3"]:
        layanan_pilih = layanan[int(pilih)-1]
        jumlahvalid = False
        while not jumlahvalid:
            try:
                jumlah = int(input("Jumlah hewan (1-10): "))
                if 1 <= jumlah <= 10:
                    jumlahvalid = True
                else:
                    print("> input anda tidak benar!")
            except ValueError:
                print("> Input harus angka!")

        user["keranjang"].append({
            "jenis": "perawatan",
            "layanan": layanan_pilih["nama"],
            "deskripsi": layanan_pilih["deskripsi"],
            "harga": layanan_pilih["harga"],
            "jumlah": jumlah
        })
        print(f"\n> {jumlah} hewan akan menjalani '{layanan_pilih['nama']}'!")
    elif pilih == "0":
        clear()
        return
    else:
        print("> Pilihan tidak valid.")
    input("Enter untuk kembali...")
    clear()
"======================================================================================================================================="

"======================================================================================================================================="
def rincianpembelian(user):
    while True:
        if "keranjang" not in user:
            user["keranjang"] = []
        keranjang = user["keranjang"]
        if not keranjang:
            print("> Keranjang Anda kosong.")
            input("Enter...")
            clear()
            return

        tabel = PrettyTable(["No", "Jenis", "Nama/Layanan", "Harga Satuan", "Jumlah", "Total"])
        total_bayar = 0
        for i, item in enumerate(keranjang, 1):
            if item["jenis"] == "barang":
                nama = item["nama"]
                harga_satuan = item["harga"]
            else:
                nama = item["layanan"]
                harga_satuan = item["harga"]
            jumlah = item["jumlah"]
            total_item = harga_satuan * jumlah
            total_bayar += total_item
            tabel.add_row([i, item["jenis"], nama, f"Rp{harga_satuan:,}", jumlah, f"Rp{total_item:,}"])
        print(tabel)
        print(f"\nTotal yang harus dibayar: Rp{total_bayar:,}")
        print("\n1. Hapus Item\n2. Kembali")
        pilih = input("Pilih: ").strip()
        if pilih == "1":
            try:
                no_hapus = int(input("Nomor item yang dihapus: ")) - 1
                if 0 <= no_hapus < len(keranjang):
                    item_hapus = keranjang[no_hapus]
                    konfirmasi = input(f"Hapus {item_hapus.get('nama', item_hapus.get('layanan', ''))}? (y/n): ").strip().lower()
                    if konfirmasi == 'y':
                        keranjang.pop(no_hapus)
                        user["keranjang"] = keranjang
                        # Simpan perubahan
                        datauser = bacadatauser()
                        for u in datauser["akunuser"]:
                            if u["username"] == user["username"]:
                                u["keranjang"] = keranjang
                                break
                        simpanuser(datauser)
                        print("> Item berhasil dihapus!")
                    else:
                        print("> Penghapusan dibatalkan.")
                else:
                    print("> Nomor tidak valid!")
            except ValueError:
                print("> Input harus angka!")
            input("Enter...")
        elif pilih == "2":
            clear()
            return
        else:
            print("> Pilihan tidak valid!")
            time.sleep(1)
            clear()
            rincianpembelian()
"======================================================================================================================================="

"======================================================================================================================================="
def transaksi(user):
    while True:
        print("1. Cek Saldo\n2. Top Up\n3. Bayar Keranjang\n4. Kembali")
        pilih = input("Pilih: ").strip()
        if pilih == "1":
            print(f"> Saldo Anda: Rp{user['saldo']:,}")
            input("Enter...")
            clear()
        elif pilih == "2":
            print("minimal topup Rp50.000 dan maksimal topup Rp2.000.000")
            try:
                nominal = int(input("jumlah topup: Rp"))
                if nominal < 50000:
                    print("> Minimal topup adalah Rp50.000!")
                elif nominal > 2000000:
                    print("> Maksimal topup adalah Rp2.000.000!")
                else:
                    user["saldo"] += nominal
                    datauser = bacadatauser()
                    for u in datauser["akunuser"]:
                        if u["username"] == user["username"]:
                            u["saldo"] = user["saldo"]
                            u["keranjang"] = user.get("keranjang", [])
                            break
                    simpanuser(datauser)
                    print(f"> Saldo berhasil ditambahkan! Saldo sekarang: Rp{user['saldo']:,}")
            except ValueError:
                print("> Input harus berupa angka!")
            input("Enter...")
            clear()
            transaksi(user)
        elif pilih == "3":
            if "keranjang" not in user:
                user["keranjang"] = []
            keranjang = user["keranjang"]
            if not keranjang:
                print("> Keranjang kosong!")
                input("Enter...")
                clear()
                continue
            total = sum(item["harga"] * item["jumlah"] for item in keranjang)
            if user["saldo"] >= total:
                user["saldo"] -= total

                # === NOTA PEMBAYARAN ===
                waktu_bayar = time.strftime("%d-%m-%Y %H:%M:%S")
                nota = []
                nota.append("="*60)
                nota.append("                HAE PET SHOP - NOTA PEMBAYARAN")
                nota.append("="*60)
                nota.append(f"Tanggal     : {waktu_bayar}")
                nota.append(f"Pelanggan   : {user['username']}")
                nota.append("-"*60)
                nota.append(f"{'No':<3} {'Jenis':<12} {'Nama/Layanan':<20} {'Jumlah':<8} {'Total':<12}")
                nota.append("-"*60)
                total_bayar = 0
                for i, item in enumerate(keranjang, 1):
                    if item["jenis"] == "barang":
                        nama = item["nama"]
                    else:
                        nama = item["layanan"]
                    jumlah = item["jumlah"]
                    subtotal = item["harga"] * jumlah
                    total_bayar += subtotal
                    nota.append(f"{i:<3} {item['jenis']:<12} {nama:<20} {jumlah:<8} Rp{subtotal:,}")
                nota.append("-"*60)
                nota.append(f"{'TOTAL':>48} Rp{total_bayar:,}")
                nota.append("="*60)
                nota.append("Terima kasih telah berbelanja di HAE Pet Shop!")
                nota.append("")

                # munculkan nota di layar
                for baris in nota:
                    print(baris)
                input("\nTekan Enter untuk kembali...")
                clear()

                datauser = bacadatauser()
                for u in datauser["akunuser"]:
                    if u["username"] == user["username"]:
                        u["saldo"] = user["saldo"]
                        u["keranjang"] = []
                        break
                simpanuser(datauser)
                user["keranjang"] = []
            else:
                print(" Saldo tidak cukup!")
            input("Enter...")
            clear()
        elif pilih == "4":
            clear()
            break
        else:
            print(" Pilihan tidak valid!")
            time.sleep(1)

menuutama()
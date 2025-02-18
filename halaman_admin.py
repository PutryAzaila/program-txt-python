def halaman_admin(username):
    print(f"Halo {username}, Selamat Datang Di Halaman Admin!")
    while True:
        print("\nMenu Admin")
        print("1. Lihat Produk")
        print("2. Tambah Produk")
        print("3. Edit Produk")
        print("4. Hapus Produk")
        print("5. Keluar")
        
        pilih_menu = int(input("Pilih Menu gunakan angka: "))
        if pilih_menu == 1:
            data_produk, daftar_harga = baca_produk()
            if not data_produk:
                print("Tidak Ada Produk Yang Tersedia")
            else:
                print("List Produk")
                for produk in data_produk:
                    print(f"ID: {produk} Nama: {data_produk[produk]}, Harga: {daftar_harga[produk]}")
        elif pilih_menu == 2:
            tambah_produk()
        elif pilih_menu == 3:
             edit_produk()
        elif pilih_menu == 4:
             hapus_produk()
        elif pilih_menu == 5:
            print("Keluar Dari Halaman Admin")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi!")

def baca_produk():
    data_produk = {}
    daftar_harga = {}
    with open("produk.txt", "r") as file:
        for line in file:
            proha = line.strip().split(",")  
            if len(proha) == 3:  
                id_produk = int(proha[0])
                nama_produk = proha[1]
                harga_produk = int(proha[2])
                data_produk[id_produk] = nama_produk
                daftar_harga[id_produk] = harga_produk
    return data_produk, daftar_harga

def tambah_produk():
    id_produk = int(input("Masukkan ID Produk: "))
    nama_produk = input("Masukkan Nama Produk: ")
    harga = int(input("Masukkan Harga Produk: "))
        
    with open("produk.txt", "a") as file:
        file.write(f"{id_produk},{nama_produk},{harga}\n")
    print("Produk berhasil ditambahkan")
    
def edit_produk():
    data_produk, daftar_harga = baca_produk()

    print("Daftar Produk:")
    for id_produk in data_produk:
        print(f"ID: {id_produk}, Nama: {data_produk[id_produk]}, Harga: {daftar_harga[id_produk]}")

    edit = int(input("Masukkan ID produk yang ingin diedit: "))
        
    if edit in data_produk:  
        
        print(f"Produk ditemukan: ID: {edit}, Nama: {data_produk[edit]}, Harga: {daftar_harga[edit]}")
        
        nama_baru = input("Masukkan Nama Produk Baru: ")
        harga_baru = int(input("Masukkan Harga Produk Baru: "))

        data_produk[edit] = nama_baru
        daftar_harga[edit] = harga_baru

        with open("produk.txt", "w") as file:
            for id_produk in data_produk:
                file.write(f"{id_produk},{data_produk[id_produk]},{daftar_harga[id_produk]}\n")
        
        print("Produk Berhasil Diedit!")
    else:
        print("Produk Tidak Ditemukan")

def hapus_produk():
    data_produk, daftar_harga = baca_produk()

    print("\nDaftar Produk:")
    for id_produk in data_produk:
        print(f"ID: {id_produk}, Nama: {data_produk[id_produk]}, Harga: {daftar_harga[id_produk]}")

    hapus = int(input("Masukkan ID Produk Yang Ingin Dihapus: "))
    
    if hapus in data_produk:
        print(f"Produk Yang Ingin Dihapus: ID: {hapus}, Nama: {data_produk[hapus]}, Harga: {daftar_harga[hapus]}")

        del data_produk[hapus]
        
        with open("produk.txt", "w") as file:
            for id_produk in data_produk:
                file.write(f"{id_produk},{data_produk[id_produk]},{daftar_harga[id_produk]}\n")
        
        print("Produk berhasil dihapus!")
    else:
        print("Produk tidak ditemukan")
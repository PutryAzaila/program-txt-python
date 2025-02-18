def halaman_pembeli(username):
    print(f"Halo {username}, Selamat Berbelanja!")
    while True:
        print("Menu Pembelian: \n1. List Produk\n2. Pembelian\n3. Keluar")
        pilihan = input("Pilih Menu: ")
        if pilihan == "1":
            data_produk, daftar_harga = baca_produk()
            if not data_produk:
                print("Tidak Ada Produk Yang Tersedia")
            else:
                print("List Produk")
                for produk in data_produk:
                    print(f"ID: {produk} Nama: {data_produk[produk]}, Harga: {daftar_harga[produk]}")
        elif pilihan == "2":
            proses_pembelian()
        elif pilihan == "3":
            print("Keluar Dari Halaman Pembelian")
            break

def baca_produk():
    data_produk = {}
    daftar_harga = {}
    with open("produk.txt", "r") as file:
        for proha in file:
            proha = proha.strip().split(",")
            if len(proha) == 3:
                id_produk = int(proha[0])
                nama_produk = proha[1]
                harga_produk = int(proha[2])
                data_produk[id_produk] = nama_produk
                daftar_harga[id_produk] = harga_produk
    return data_produk, daftar_harga

def proses_pembelian():
    data_produk, daftar_harga = baca_produk()

    daftar_belanja = []
    total_harga = 0  

    while True:
        print("List Produk")
        for produk in data_produk:
            print(f"ID: {produk} Nama: {data_produk[produk]}, Harga: {daftar_harga[produk]}")
            
        id_produk = int(input("Pilih ID Produk (0 Untuk Selesai): "))
        if id_produk == 0:
            break
        jumlah = int(input(f"Jumlah Untuk {data_produk[id_produk]}: "))
        daftar_belanja.append((id_produk, jumlah))
        total_harga += daftar_harga[id_produk] * jumlah  

        print(f"{data_produk[id_produk]} Sebanyak {jumlah} Telah Ditambahkan")

    if daftar_belanja:
        print("Daftar Belanjaan:")
        for id_produk, jumlah in daftar_belanja:
            total = daftar_harga[id_produk] * jumlah
            print(f"Produk: {data_produk[id_produk]}, Jumlah: {jumlah}, Total Harga: {total}")
        
        print(f"Total Harga Semua Produk: {total_harga}")  

    print("Metode Pembayaran:")
    print("1. Kredit")
    print("2. Virtual Account")
    print("3. Transfer Bank")
    print("4. Pembayaran digagalkan")
    metode_pembayaran = input("Pilih metode pembayaran (1/2/3/4): ")

    if metode_pembayaran == "1":
        print("Pembayaran berhasil menggunakan Kredit.")
    elif metode_pembayaran == "2":
        print("Pembayaran berhasil menggunakan Virtual Account.")
    elif metode_pembayaran == "3":
        print("Pembayaran berhasil menggunakan Transfer Bank.")
    else:
        print("Pilihan tidak valid. Pembayaran batal.")

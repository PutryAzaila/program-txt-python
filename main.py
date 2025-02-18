import halaman_admin
import halaman_pembeli
def login(username, password):
    sukses = False
    role = None
    with open("logindatabase.txt", "r") as file:
        for i in file:
            i = i.strip()
            if "," in i:
                upr = i.split(",", 2)
                if len(upr) == 3:
                    u, p, r = upr
                    p = p.strip()
                    if u == username and p == password:
                        sukses = True
                        role = r.strip()
                        break
                    
    if sukses:
        print(f"Login Berhasil. Selamat Datang {username} dengan role {role}")
        if role == "admin":
            halaman_admin.halaman_admin(username)
        elif role == "pembeli":
            halaman_pembeli.halaman_pembeli(username)
    else:
        print("Login gagal, username atau password salah atau belum mempunyai akun")

def cek_username(username):
    with open("logindatabase.txt", "r") as file:
        for i in file :
            i = i.strip()
            if  i:
                upr = i.split(",", 2)
                if len(upr) == 3:
                    u, _, _ = upr
                    if u == username:
                        return True
        return False
    
def register(username, password):
    if cek_username(username):
        akses("register")
        return False
    else:
        role = input("Masukkan role Anda (admin atau pembeli):").lower()
        with open("logindatabase.txt", "a") as file:
            file.write( "\n" + username + "," + password + "," + role)
        print("Register berhasil, silahkan masuk")
        return True
        
def akses(option):
    if option == "login":
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        login(username, password)

    else:
        while True:
            username = input("Masukkan username: ")
            if cek_username(username):
                print("Username sudah terdaftar, pilih username yang lain!")
            else:
                break

        password = input("Masukkan Password: ")
        register(username, password)

        pilihanlogin = input("Apakah ingin login sekarang (ya/tidak)? ")
        if pilihanlogin.lower() == "ya":
            akses("login")
        
def awal():
    print("Selamat Datang Di Toko Online!")
    print("Ketik 'login' jika sudah mempunyai akun")
    print("Ketik 'reg' jika belum mempunyai akun")
    option = input("Silahkan pilih (login/reg) :").lower()
    if option != "login" and option != "reg":
        print("Pilihan tidak valid, silahkan coba lagi!")
        awal()
    else:
        akses(option)
awal()
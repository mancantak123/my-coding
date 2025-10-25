import os
def menu():
    x =["masukan nilai siswa " , "membaca nilai siswa" , "menghapus nilai siswa" , "keluar"]

    for i in range(len(x)):
        print(f"{i + 1} , {x[i]}" )

while true :
    x = input("masuk aplikasi atau tidak : ")
    if x == "masuk" :
        print("6*=selamat datang aplikasi input nilai siswa 6*= ")
        break
    elif x =="keluar" :
        quit()
    
    else :
        print("terjadinya kesalahan")
        contine

while True :
    y = int(input("pilih mana :"))
    if y == 1 :
        print("masukan nilai siswa")
        A = input("siapa nama siswa :")
        B = int(input("berapa nilai siswa :"))
        with open("aplikasi input nilai siswa/nilai_siswa" , "a") as file :
            file.write(f" {A} : {B}\n")
        continue
    elif y == 2 :
        with open("aplikasi input nilai siswa/nilai_siswa" , "r") as file :
            print(file.read())
            continue
    elif y == 3 :
        with open("aplikasi input nilai siswa/nilai_siswa", "r") as file:
            baris = file.readlines()   # ambil isi file per baris

        for line in baris:
            print(line, end="")   # end="" supaya tidak ada baris kosong tambahan

        
        # minta input user (baris ke berapa yang mau dihapus)
        z = int(input("Masukkan nomor baris yang ingin dihapus: "))

        # baca semua isi file
        with open("aplikasi input nilai siswa/nilai_siswa", "r") as file:
            baris = file.readlines()

        # tulis ulang kecuali baris yang dipilih
        with open("aplikasi input nilai siswa/nilai_siswa", "w") as file:
            for i, line in enumerate(baris, start=1):  # start=1 supaya baris dimulai dari 1
                if i != z:
                    file.write(line)
        print(f"Baris ke-{z} berhasil dihapus!")
        continue
    else :
        break
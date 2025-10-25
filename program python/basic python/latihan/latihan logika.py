import time
print("ayo kita test kemampuan dengan jawab pertanyaan ini!! ")
print(" ")
print("ketik iya atau tidak dibawah ini(huruf kecil semua)")

mulai = input("ikut atau tidak = ")
if mulai == "iya"  :
    print("mulai") 
else :
    quit()

print("bersiap lah dalam 10 detik")

x = 1

while x <= 10 :
    print(x)
    x += 1
    time.sleep(0.5)

print("berapa perkalian  dari 5 kali 5(angka) ")
soal1 = int(input("jawab : "))
if soal1 == 25 :
    print("benar")
else :
    print("salah")
    quit()
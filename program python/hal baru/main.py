print("selamat datang di program ini!!")

while True :
    x = float(input("pembilang :"))
    y = float(input("penyebut :"))
    if y == 0 :
        print("penyebut tidak boleh angka nol")
        continue
    else :
        hasil= x/y
        print(f"hasil pembagian : {hasil}")
        lanjut = input("lanjut? (y/n) :").lower()
        if lanjut == "n" :
            break
print("program selesai")
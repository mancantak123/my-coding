print("selamat datang di program ini!!")

while True :
    x = float(input("pembilang :"))
    y = float(input("penyebut :"))
    try :
        hasil = x/y
        print(f"hasil pembagian : {hasil}")
    except :
        print("penyebut tidak boleh nol!!")
    lanjut = input("lanjut? (y/n) :").lower()
    if lanjut == "n" :
        break
print("program selesai")
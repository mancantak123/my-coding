def data() :
    barang = ["baju merah" , "baju biru" , "baju hijau" , "baju hitam" , "baju kuning" ]
    harga  = [ 125000 , 200000 , 85500 , 250000 , 150000 , 95000 ]

    for i  in range(len(barang)) :
        print(f"{i + 1},{barang[i]:15} Rp {harga[i] : ,}")

    return barang , harga

def pembayaran(user) :
    y = input("pilih baju , (pakai angka) :")
    b = input("masukan nominal :")

    return y , b


print("== selamat datang di aplikasi kasir ==")
x = input("masuk atau tidak : ")

if x == "tidak" :
    quit()
else :
    data()
    pembayaran(user= 1)


data_stok = ["baju merah" , "baju biru" , "baju hijau" , "baju hitam" , "baju kuning" ]
data_stok_harga = [ 125.000 , 200.000 , 85.500 , 250.000 , 150.000 ]


print("== selamat datang di aplikasi kasir ==")
x = input("masuk atau tidak : ")

if x == "tidak" :
    quit()
else :
    print("silahkan masuk")

print("ayo pilih baju : ")
for index , i in enumerate(data_stok) :
    print(index , i)

y = int(input("masukan data no :"))
a = int(input("masukan nominal pembayaran : "))

harga = data_stok_harga[y]

pembayaran = a - harga
print(pembayaran , "transaksi berhasil")
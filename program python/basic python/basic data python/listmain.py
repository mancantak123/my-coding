buah = ["mangga", "apel" , "anggur" , "jeruk" , "katela"]

print(buah)
print(buah[2]) #akses element ketiga
print(buah[0])  # akses elemsn pertama

buah[3] = "madu" #ubah data list
print(buah)

buah.append("madu") #tambah data list (append(). bagian akhir)
print(buah)

# insert(index , value) ditambah diposisi tertentu

buah.remove("mangga") # menghapus data
print(buah)

# in adalah variabel untuk mengechek data
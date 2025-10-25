file = open("basic data base python/data.txt" , "w")
file.write("halo , ini adalah baris pertama ku")
file.close()

# jika mau membuat file/data ada 3 komponen penting yaitu :
# fungsi open 
# mode
# ditutup


# mode umumnya ada :
# "w" write = digunakan untuk membuat file atau menimpa
# "a" menambah bagian akhir = digunakan untuk file baru dibagian akhir untuk tidak menimpa file
# "r" remove = digunakan untuk menghapus file
# namun terdapat trik menggunakan membuat data/file yaitu menguunakan syntax with
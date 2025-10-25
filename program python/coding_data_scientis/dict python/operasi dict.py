# operator

data_dict = {
    'ud':'udin',
    'ot':'totong',
    'dd':'dudung',
}

# panjang (len)
lendict =  len(data_dict)

print(f"panjang data_dict adalah : {lendict}")

# mengechek ky dalam dictionary

kay = "pp"
chek = kay in data_dict
print(f'apakah nilai key {kay} didalam data_dict : {chek}')

# mengakses value dengan .get

print(data_dict.get("ud"))


print(data_dict.get("ud" , "key tidak ditemukan")) # chek key dengan massage "key tidak ditemukan" 

#data_dict.update({}) == digunakan untuk mengupdate data
import pandas as pd

data = {
    'nama' : ["nadi" , "budi" , "ucup"],
    'kelas': ["x-a" , "x-b" , "x-c"],
    'nilai': [90 , 76 , 100]
}

data_hasil = pd.DataFrame(data)

print(data_hasil)



print(f"nilai rata-rata mereka adalah : {int(data_hasil["nilai"].mean())}")
print(f"nilai tertinggi mereka adalah : {data_hasil["nilai"].max()}")
print(f"nilai terendah mereka adalah : {data_hasil["nilai"].min()}")
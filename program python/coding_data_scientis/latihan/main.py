import pandas as pd
import os
main = {
    'nama' : '' ,
    'kelas': '',
    'nilai' : '',
}

def menu() :
    print(f"="*50)
    print(f"selamat datang".center(50))
    print("="*50)
    print("daftar menu")
    x = ['input nama']
    for i in range(len(x)) :
        print(f"{i +1}.{x[i]}")

print("="*50)
print("login".center(50))
print("="*50)
login = input("silahkan login (y/n) :")

if login == 'y' :
    menu()
    main['nama'] = input("nama :")
    main['kelas']= input("kelas :")
    main['nilai']= input('nilai :')
    data = pd.DataFrame([main])
    print(data.to_string(index=False , justify='center'))
elif login == 'n' :
    quit()
else :
    print('terjadinya kesalahan')


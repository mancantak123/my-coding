import math

class Kubus :
    def __init__(self , rusuk_kubus , volume):
        self.rusuk_kubus = rusuk_kubus
        self.volume = volume

    def Volume(self , RUSUK):
        self.volume = RUSUK**3
    
    def Rusuk_kubus(self , VOLUME):
         self.rusuk_kubus = math.pow(VOLUME, 1/3)
    

def menu():
    menu = ['volume kubus' , 'rusuk kubus' , 'keluar']
    print('selamat datang program kubus')
    for i in range(len(menu)):
        print(f'{1 + i}.{menu[i]}')

kubus1 = Kubus(0 , 0)

while True :
    menu()
    input_menu = input('silahkan pilih menu berdasarkan nomor : ')
    if input_menu == '1' :
        input_rusuk_kubus = int(input('silahkan masukan nilai rusuk kubus :'))
        kubus1.Volume(input_rusuk_kubus)
        print(f'\tvolume kubus : {kubus1.volume} cm^3')
        print('\n')
        continue
    elif input_menu == '2' :
        input_volume_kubus = int(input('silahkan masukan nilai volume : '))
        kubus1.Rusuk_kubus(input_volume_kubus)
        print(f'\trusuk kubus : {kubus1.rusuk_kubus} cm')
        print('\n')
        continue
    elif input_menu == '3':
        
        quit()
    else :
        print("terjadinya kesalah tolong coba lagi!!")
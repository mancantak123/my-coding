class Balok :
    def __init__(self , volume , panjang , lebar , tinggi):
        self.__volume = volume
        self.__panjang = panjang
        self.__lebar = lebar
        self.__tinggi = tinggi

    def info_Volume(self):
        return self.__volume
    
    def info_Panjang(self):
        return self.__panjang
    
    def info_Lebar(self):
        return self.__lebar
    
    def info_tinggi(self):
        return self.__tinggi
    
    def set_panjang(self , PANJANG):
        self.__panjang = PANJANG

    def set_Lebar(self ,LEBAR):
        self.__lebar = LEBAR
    
    def set_Tinggi(self , TINGGI):
        self.__tinggi = TINGGI
    
    def set_Volume(self , VOLUME):
        self.__volume = VOLUME
    
    def VOLUME_BALOK(self):
        self.__volume = self.__panjang*self.__lebar*self.__tinggi
        return self.__volume
    
    def sisi_panjang(self):
        self.__panjang = self.__volume/(self.__lebar*self.__tinggi)
        return self.__panjang
    
    def sisi_Lebar(self):
        self.__lebar = self.__volume/(self.__panjang*self.__lebar)
        return self.__lebar
    
    def sisi_Tinggi(self):
        self.__tinggi = self.__volume/(self.__panjang*self.__lebar)
        return self.__tinggi


Balok1 = Balok(0,0,0,0)

def menu():
    menu = ['volume Balok' , 'panjang sisi balok' , 'lebar sisi balok' , 'tinggi sisi balok' , 'keluar']
    print('selamat datang program Balok')
    for i in range(len(menu)):
        print(f'{1 + i}.{menu[i]}')


while True :
    menu()
    input_masuk = input('silahkan pilih salah satu menu menggunakan angka : ')
    if input_masuk == '1' :
        print('silahkan isi bagian panjang , lebar , dan tinggi')
        
        try :
            input_panjang = int(input('panjang : '))
            input_lebar = int(input('lebar : '))
            input_Tinggi = int(input('tinggi : '))

            if input_panjang <= 0 or input_lebar <= 0 or input_Tinggi <= 0 :
                raise ValueError('Salah satu input tidak boleh 0 atau tidak boleh negatif!!!')
            Balok1.set_panjang(input_panjang)
            Balok1.set_Lebar(input_lebar)
            Balok1.set_Tinggi(input_Tinggi)
            print(f'\t volume balok adalah : {Balok1.VOLUME_BALOK()} cm^3')
            continue
        
        except ValueError as e :
            print(f'\nterjadinya kesalahan: {e}')
            print('\tsilahkan masukan angka positif atau lebih dari nol. \n ')
    elif input_masuk =='2':
        print('silahkan masukan VOLUME , LEBAR DAN TINGGI')
        try :
            input_VOLUME2 = int(input('Volume :'))
            input_lebar2 = int(input('Lebar : '))
            input_Tinggi2 = int(input('Tinggi : '))
            if input_VOLUME2 <= 0 or input_lebar2 <= 0 or input_Tinggi2 <= 0 :
                raise ValueError('salah satu input tidak boleh nol atau negatif')
            Balok1.set_Volume(input_VOLUME2)
            Balok1.set_Lebar(input_lebar2)
            Balok1.set_Tinggi(input_Tinggi2)
            print(f'panjang balok adalah : {Balok1.sisi_panjang()} cm')
            continue

        except ValueError as a :
            print(f'\nterjadinya kesalahan: {a}')
            print('\tsilahkan masukan angka positif atau lebih dari nol. \n ')
            
    elif input_masuk =='3':
        print('silahkan masukan VOLUME , PANJANG DAN TINGGI')
        try :
            input_VOLUME3 = int(input('Volume :'))
            input_panjang3 = int(input('PANJANG : '))
            input_Tinggi3 = int(input('Tinggi : '))
            if input_VOLUME3 <= 0 or input_panjang3 <= 0 or input_Tinggi3 <= 0 :
                raise ValueError('salah satu input tidak boleh nol atau negatif')
            Balok1.set_Volume(input_VOLUME3)
            Balok1.set_panjang(input_panjang3)
            Balok1.set_Tinggi(input_Tinggi3)
            print(f'panjang balok adalah : {Balok1.sisi_Lebar()} cm')
            continue
        except ValueError as a :
            print(f'\nterjadinya kesalahan: {a}')
            print('\tsilahkan masukan angka positif atau lebih dari nol. \n ')

    elif input_masuk =='4':
        print('silahkan masukan VOLUME , PANJANG , LEBAR')
        try :
            input_VOLUME4 = int(input('Volume :'))
            input_panjang4 = int(input('panjang : '))
            input_lebar4 = int(input('lebar : '))
            if input_VOLUME4 <= 0 or input_panjang4 <= 0 or input_lebar4 <= 0 :
                raise ValueError('salah satu input tidak boleh nol atau negatif')
            Balok1.set_Volume(input_VOLUME4)
            Balok1.set_panjang(input_panjang4)
            Balok1.set_Lebar(input_lebar4)
            print(f'panjang balok adalah : {Balok1.sisi_Tinggi()} cm')
            continue
        except ValueError as a :
            print(f'\nterjadinya kesalahan: {a}')
            print('\tsilahkan masukan angka positif atau lebih dari nol. \n ')

    elif input_masuk == '5':
        print('\n\t program telah selesai terima kasih telah mencoba :)')
        quit()
    else :
        print('terjadinya kesalahan input menu silahkan kembali')
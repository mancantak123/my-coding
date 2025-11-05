import math

class Tabung :
    def __init__(self , volume , jari_jari , tinggi , keliling , luas_permukaan):
        self.__volume = volume
        self.__jari_jari = jari_jari
        self.__tinggi = tinggi
        self.__keliling = keliling
        self.__luas_permukaan = luas_permukaan
    
    def info_Volume(self):
        return self.__volume
    
    def info_Jari_jari(self):
        return self.__jari_jari
    
    def info_Tinggi(self):
        return self.__tinggi
    
    def info_Keliling(self):
        return self.__keliling
    
    def info_Volume(self):
        return self.__luas_permukaan
    
    def set_Volume(self , VOLUME):
        self.__volume = VOLUME
        return self.__volume

    def set_Jari_jari(self , JARI_JARI):
        self.__jari_jari = JARI_JARI
        return self.__jari_jari

    def set_Tingi(self , TINGGI):
        self.__tinggi = TINGGI
        return self.__tinggi

    def set_keliling(self , KELILING):
        self.__keliling = KELILING
        return self.__keliling

    def set_Luas_Permukan(self , Luas_permukaan):
        self.__luas_permukaan = Luas_permukaan
        return self.__keliling
    
    def VOLUME_TABUNG(self):
        self.__volume = math.pi*self.__jari_jari**2*self.__tinggi
        return self.__volume
    
    def LUAS_PERMUKAAN_TABUNG(self):
        self.__luas_permukaan = 2*math.pi*self.__jari_jari*(self.__jari_jari+self.__tinggi)
        return self.__luas_permukaan
    
    def KELILING_TABUNG_ALAS(self):
        self.__keliling = 2*math.pi*self.__jari_jari
        return self.__keliling
    
    def TINGGI_VOLUME_TABUNG(self):
        self.__tinggi = self.__volume/(math.pi*self.__jari_jari**2)
        return self.__tinggi
    
    def JARI_JARI_VOLUME_TABUNG(self):
        self.__jari_jari = math.sqrt(self.__volume/(math.pi*self.__jari_jari))
        return self.__jari_jari
    
    def JARI_JARI_KELILING_TABUNG(self):
        self.__jari_jari = self.__keliling/(2*math.pi)
        return self.__jari_jari
    
    def TINGGI_LUAS_PERMUKAAN_TABUNG(self):
        self.__tinggi = self.__luas_permukaan/(2*math.pi*self.__jari_jari)-self.__jari_jari
        return self.__tinggi

tabung1 = Tabung(0,0,0,0,0)

def menu():
    menu = ['Volume Tabung' , 'Luas permukaan Tabung' , 'Keliling alas Tabung' , 'Tinggi volume tabung' , 'jari-jari volume tabung' , 'jari-jari keliling tabung' , 'tinggi luas permukaan tabung' , 'keluar']
    print('selamat datang program Tabung ')
    for i in range(len(menu)):
        print(f'{1 + i}.{menu[i]}')

while True:
    menu()
    input_masuk = input('silahkan inpust berdasarkan nomor dimenu :')

    if input_masuk == '1':
        try :
            input_volume_tabung_jari_jari = int(input('Jari-jari :'))
            input_volume_tabung_Tinggi = int(input('TInggi : '))

            if input_volume_tabung_jari_jari <= 0 or input_volume_tabung_Tinggi <= 0:
                ValueError('terjadinya kesalahan di input , jangan masukkan angka negatif atau nol!!')
            
            tabung1.set_Jari_jari(input_volume_tabung_jari_jari)
            tabung1.set_Tingi(input_volume_tabung_Tinggi)
            print(f'Volume tabung : {tabung1.VOLUME_TABUNG()} cm^3')
            continue
        except ValueError as e :
            print('terjadinya kesalahan : {e}')
            print('\tsilahkan masukan angka positif atau lebih dari nol. \n ')
        
    elif input_masuk == '2':
        try
            input_luas_permukaan_tabung_jari_jari = int(input('jari-jari :'))
            input_luas_permukaan_tabung_Tinggi = int(input('Tinggi :'))

            if input_volume_tabung_jari_jari <= 0 or input_volume_tabung_Tinggi <= 0:
                ValueError('terjadinya kesalahan di input , jangan masukkan angka negatif atau nol!!')
            
            tabung1.set_Jari_jari(input_luas_permukaan_tabung_jari_jari)
            tabung1.set_Tingi(input_luas_permukaan_tabung_Tinggi)
            print(f'luas permukaan tabung : {tabung1.LUAS_PERMUKAAN_TABUNG} cm')
        except ValueError as e :
            print('terjadinya kesalahan : {e}')
            print('\tsilahkan masukan angka positif atau lebih dari nol. \n ')


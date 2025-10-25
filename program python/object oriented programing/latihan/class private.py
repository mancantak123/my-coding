# data siswa
class data_siswa :

    def __init__(self , nama , nilai):
        self.__nama = nama
        self.__nilai = nilai

    def info_nama(self) :
        print('atas nama : ' , self.__nama)

    def info_nilai(self) :
        print(f'\t atas nama {self.__nama} dengan nilai :' , self.__nilai)
    
    def validasi(self) :
        if 0 < self.__nilai < 100 :
            print(f'\t data atas nama {self.__nama} dengan nilainya dinyatakan valid')
        else :
            print(f'\t atas nama {self.__nama} dengan nilainya dinyatakan tidak valid')
    #dibawah ini merupakan setter!!
    def kkm(self) :
        if 75 <= self.__nilai < 100 :
            print(f'\t atas nama {self.__nama} : lulus')
        elif 0 < self.__nilai <75 :
            print(f'\t atas nama {self.__nama} : tidak lulus')
        else :
            print(f'\t atas nama {self.__nama} nilainya terjadi kesalahan')

udin = data_siswa('udin' , 95)
udin.info_nama()
udin.info_nilai()
udin.validasi()
udin.kkm()
print('\n')
marin = data_siswa('marin',59)
marin.info_nama()
marin.info_nilai()
marin.validasi()
marin.kkm()
print('\n')
ucup = data_siswa('ucup' , -1)
ucup.info_nama()
ucup.info_nilai()
ucup.validasi()
ucup.kkm()
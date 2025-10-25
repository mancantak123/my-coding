# kendaraan

class kendaraan :
    def __init__(self , bensin , kecepatan):
        self.__bensin = bensin
        self.__kecepatan = kecepatan
    
    def get_bensin(self):
        return self.__bensin
    def get_kecepatan(self):
        return self.__kecepatan
    
    def set_bensin(self , isi):
        if isi <= 0 :
            print('bensin tidak nol atau minus')
        else :
            self.__bensin = isi
    
    def set_kecepatan(self , ulang):
        if self.__bensin < 0 :
            print('bensin anda habis')
        else :
            self.__kecepatan = ulang
    
    def jalan(self):
        if self.__bensin <= 0:
            print('Bensin habis! Tidak bisa jalan.')
        else:
            penggunaan = 5 * self.__kecepatan
            if penggunaan > self.__bensin:
                print('Bensin tidak cukup untuk kecepatan ini.')
            else:
                self.__bensin -= penggunaan
                print(f'Kendaraan berjalan dengan kecepatan {self.__kecepatan}.')
                print(f'Sisa bensin: {self.__bensin}')


mobil = kendaraan(100 , 2)

print(mobil.get_bensin())
print(mobil.get_kecepatan())
print('\n')

mobil.set_kecepatan(5)
print(mobil.get_kecepatan())

print('\n')
mobil.jalan()

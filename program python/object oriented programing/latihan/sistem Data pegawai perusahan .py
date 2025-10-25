# inheritance , private variable , getter & setter

class Pegawai :
    def __init__(self , nama , gaji):
        self.__nama = nama
        self.__gaji = gaji

    def get_ambil_gaji(self ,ambil):
        if ambil > self.__gaji :
            return f'pengambilan gaji atas nama {self.__nama} diatas gaji {self.format_rupiah(self.__gaji)}'
        else :
            return  f'gaji atas nama {self.__nama} telah diambil'
    
    def set_atur_gaji(self , atur):
        if atur == self.__gaji or atur <= 0 :
            return f'anda bikin kebijakan salah'
        else :
            self.__gaji = atur
            return f'gaji sudah atur : {self.format_rupiah(self.__gaji)}'
    def info(self) :
        print(f'atas nama karyawan :{self.__nama} \n\t Gaji : {self.format_rupiah(self.__gaji)}')
    
    def format_rupiah(self , n) :
        return f'{n:,} Rp'.replace(',', ',')

class departemen(Pegawai):
    def __init__(self, nama, gaji , manajer):
        super().__init__(nama, gaji)
        self.manajer = manajer
        
    
udin = Pegawai('udin' , 1000000)

udin.info()
udin.set_atur_gaji(2000000)
udin.info()
print(udin.get_ambil_gaji(10000000))

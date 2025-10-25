# siswa
class siswa :

    def __init__(self , nama , nilai):
        self.nama = nama
        self.nilai = nilai
    
    def info(self) :
        print('nama siswa :' , self.nama)
        print('nilai siswa :' , self.nilai)
    
    def status_kkm(self) :
        if self.nilai >= 75 :
            print('siswa dengan nama ' , self.nama , ' telah lulus')
        else :
            print('siswa dengan nama ' , self.nama , ' tidak lulus')
    #def __str__(self):
        #return f'Nama: {self.nama}, nilai:{self.nilai}'


siswa1 = siswa('udin' , 75)
siswa2 = siswa('ucup' , 65)

siswa1.info()
siswa1.status_kkm()
print('\n')
siswa2.info()
siswa2.status_kkm()
# pribadi
class pribadi :
    def __init__(self , nama , umur):
        self.__nama = nama
        self.__umur = umur

    def get_nama(self):
        return self.__nama
    
    def set_nama(self , nama_baru):
        if nama_baru == '' :
            print( 'nama gak boleh kosong!!.')
        else :
            self.__nama = nama_baru

    def get_umur(self):
        return self.__umur
    
    def set_umur(self , umur_baru):
        if umur_baru <= 0 :
            print('umur gak boleh nol')
        else :
            self.__umur = umur_baru

udin = pribadi('udin' , 20)

print(udin.get_nama())
udin.set_nama('ucup')
print(udin.get_nama())

print('\n')

print(udin.get_umur())
udin.set_umur(30)
print(udin.get_umur())


    

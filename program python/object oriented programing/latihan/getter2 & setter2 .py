# rekening bank

class bank :
    def __init__(self , saldo ):
        self.__saldo = saldo
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self , saldo_baru):
        if saldo_baru <= 0:
            print('saldo gak boleh nol')
        else :
             self.__saldo = saldo_baru
    
    def deposit(self ,jumlah):
        if jumlah <=0 :
            print('deposit gak boleh nol atau minus')
        else :
            self.__saldo += jumlah
            print('\t deposit telah sukses')
    
    def penarikan(self , tarik):
        if tarik <= 0 or tarik > self.__saldo :
            print('eror')
        else :
            self.__saldo -= tarik
            print('\t penarikan telah sukses')

rekening = bank(50000)

print(rekening.get_saldo() , 'Rp')
rekening.set_saldo(100000)
print(rekening.get_saldo(), 'Rp')

print('\n')

rekening.deposit(20000)
print(rekening.get_saldo(), 'Rp')
rekening.penarikan(90000)
print(rekening.get_saldo(), 'RP')
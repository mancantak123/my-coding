#super()
#hewan

class Hewan :
    def __init__(self , nama):
        self.nama = nama
        print(f"Hewan {self.nama} sudah dibuat")

class kucing(Hewan):
    def __init__(self, nama , warna):
        super().__init__(nama)
        self.warna = warna
        print(f'kucing bernama {nama} dengan warna {self.warna} sudah dibuat')

mimi = kucing('mimi' , 'oren')
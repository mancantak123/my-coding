import numpy as np

a = np.arange(10)**3

print(a)

print('elemen ke 1 adalah : ' , a[0])
print('elemen ke 7 adalah : ' , a[6])
print('elemen ke akhir adalah : ' , a[-1])

for i in a :
    print('value : ' , i)
# enumerate adalah jika perulangan sekaligus no urut dan index

data_user = []

while True :
    x = input("masukan data user : ")
    if x == "udah" :
        print("program berhenti")
        break
    else :
        data_user.append(x)

for index  , i in enumerate(data_user, start= 1) :
    print( index ,i)
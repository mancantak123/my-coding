data_user = []

while True :
    data = input("masukan data : ")

    if data == "udah" :
        print("program berhenti")
        break

    else :
        data_user.append(data)

print("data yang dimasukan sebagai berikut")
for item in data_user :
    print("-" , item)
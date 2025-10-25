import time

# Kunci jawaban
check = [100, 25, 12, 15, 50]

# Soal kuis
def soal_kuis():
    return [
        "10 pangkat 2 :",
        "5 kali 5 :",
        "akar dari 144 :",
        "25 - 10 :",
        "100 - 50 :"
    ]

# Ajak user ikut kuis
print("Ayo ikut kuis kompetisi!")
x = input("Ikut atau tidak? (ketik 'ikut' atau 'tidak'): ").lower()

if x == "tidak":
    quit()
else:
    print("Ayo mulai!")

# Countdown
print("Bersiaplah dalam 10 detik!")
for x in range(10, 0, -1):
    print(x)
    time.sleep(1)  # waktu lebih wajar: 1 detik

# Menjalankan kuis
data_user = []  # Menyimpan skor (1 = benar, -1 = salah)
soal_list = soal_kuis()

for i in range(len(soal_list)):
    print(soal_list[i])
    try:
        jawaban = int(input("Jawab: "))
    except ValueError:
        print("Jawaban harus angka! Dihitung salah.")
        data_user.append(-1)
        continue

    if jawaban == check[i]:
        data_user.append(1)
    else:
        data_user.append(-1)

# Hitung nilai akhir
nilai = data_user.count(1) * 20  # Misal tiap soal 20 poin

print("\nJawaban kamu:", data_user)
print("Nilai kamu adalah:", nilai, "dari 100")

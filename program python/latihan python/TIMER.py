import time

x = int(input("masukan timernya : "))

while x > 0 :
    print(x)
    x -= 1
    time.sleep(1)

print("waktu habis")
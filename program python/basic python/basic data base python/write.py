with open("data2" , "w") as file :
    file.write("ayo lakukan bersama-sama")

with open("data2" , "r") as file :
    print(file.read())

with open("data",  "a") as file :
    x = input()
    file.write(x)
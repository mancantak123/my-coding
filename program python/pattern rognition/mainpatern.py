import re


passwordd = [""
"password : admin123"
"password : abcjkdbdj123"
"password : rahasia1010"
]
string = "/n".join(passwordd)

pola = r"password :/s* [=\-] /s*(\s+)"

pencocok = re.findall(pola , string)

print("daftar  pw " , pencocok)
    
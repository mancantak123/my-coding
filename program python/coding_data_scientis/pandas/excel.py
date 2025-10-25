import pandas as pd


df = pd.read_excel("C:\coding_data_scientis/pandas/nilai_siswa_36_nama.xlsx")

def jika (x) :
    if x >= 75 :
        return "lulus"
    else :
        return "remedial"
    

df['status'] = df['Nilai'].apply(jika)
print(df)


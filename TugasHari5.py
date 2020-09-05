# soal no 1

Sebutkan perbedaan antara full outer join, inner join, dan left join

-Full Outer Join menghasilkan gabungan index baris dari setiap data yang di gabung
-Inner join ini akan menggabungkan data antara nilai key/referensi yang beririsan
-Left Outer Join menghasilkan seluruh data dari data yang kiri ditambah data kanan yang memiliki nilai key yang sama 
dengan data dari kiri.

# soal no 2

import pandas as pd
# read data
df1 = pd.read_csv('names1881.csv', header = None, names = ['Name', 'Gender', 'Count'])
df2 = pd.read_csv('names1981.csv', header = None, names = ['Name', 'Gender', 'Count'])

# periksa dimensi dari kedua data
print("Jumlah Dimensi data 'names1881.csv' :")
print(df1.shape)

print("Jumlah Baris data 'names1981.csv' :")
print(df2.shape)

# gabungkan data
df = pd.concat([df1, df2])
display(df)

# periksa dimensi data hasil gabungan
print("Jumlah dimensi data setelah penggabungan : ")
print(df.shape)

# soal no 3

import pandas as pd

data1 = {
    'id' : [1, 2, 3, 4],
    'Feature1' : ['a1', 'a2', 'a3', 'a4'],
    'Feature2' : ['b1', 'b2', 'b3', 'b4']
}

data2 = {
    'id' : [3, 4, 5 ,6, 7],
    'Feature3' : ['c1', 'c2', 'c3', 'c4', 'c5']
}

df1= pd.DataFrame(data1)
df2= pd.DataFrame(data2)

print(df1)
print(df2)

# join data
df_outer_join = pd.merge(df1, df2, on = 'id', how = 'outer')
print(df_outer_join)

df_inner_join = pd.merge(df1, df2, on = 'id', how = 'inner')
print(df_inner_join)

df_left_join = pd.merge(df1, df2, on = 'id', how = 'left')
print(df_left_join)

df_right_join = pd.merge(df1, df2, on = 'id', how = 'right')
print(df_right_join)

# soal no 4

data1 = {
    'key_data1' : [1, 2, 3, 4],
    'Feature1' : ['a1', 'a2', 'a3', 'a4'],
    'Feature2' : ['b1', 'b2', 'b3', 'b4']
}

data2 = {
    'key_data2' : [3, 4, 5 ,6, 7],
    'Feature3' : ['c1', 'c2', 'c3', 'c4', 'c5']
}

df1= pd.DataFrame(data1)
df2= pd.DataFrame(data2)

print(df1)
print(df2)

# Gabungkan kedua data tersebut
df_gabung = pd.merge(df1, df2, left_on = 'key_data1', right_on = 'key_data2')

df_gabung
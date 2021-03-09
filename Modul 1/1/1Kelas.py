print('Hello World')
#fungsi print adalah mencetak sesuatu
nama = 'Ridho' #string
umur = 29 #integer
pekerjaan = 'lecturer' #string juga
hobi = 'nonton youtube'
print(nama)
print(umur)
print(pekerjaan)
print(hobi)
print(type(nama))
print(type(umur))
hehe = (type(nama))
print(hehe)
nama = input('What is your name : ')
print('Hello, my name is ' + nama + ', umur saya ' + str(25)) # Jika + pake spasi. Jika + harus dengan tipe class yang sama.
print('Hello, my name is', nama, ',umur saya', 25) # Jika , (koma) gausa pake spasi. Jika , bisa flexible dengan class yang berbeda.


#Operasi matematika
print(2 + 1)
print(2 - 1)
print(3 * 2)
print(4 / 2) # data types nya float. Hasilnya 2.0
print(4 // 2) # data types nya integer. Hasilnya 2. Pembulatan kebawah.
print(5 % 2) # namanya modulo.
print(5 / 2)
print(8 // 3) # walaupun hasilnya 2.667 tapi hasilnya tetep pembulatan kebawah.
print(2**3) # power / pangkat.


# mengganti data types

x = '10'
print(type(x))

y = int(x)
print(type(y))

z = '25.5'
#print(int(z))
print(float(z))

a = 23
print(type(a))
print(str(a))
a_str = str(a)
print(type(a_str))

# Quiz 1

C = 2
print(float(C) + 10)

# Quiz 2

nama = input('Masukkan nama : ') # ketika menggunakan input, data types yang dihasilkan selalu dalam string.
umur = input('Masukkan umur : ')
print('Halo nama saya ' + nama + ' Umur saya 5 tahun ke depan adalah ' + str(int(umur)+5))
print('Halo nama saya',nama,',umur saya 5 tahun kedepan adalah', int(umur)+5)

nama = input('Masukkan nama : ') # ketika menggunakan input, data types yang dihasilkan selalu dalam string.
umur = int(input('Masukkan umur : '))
print('Halo nama saya ' + nama + ' Umur saya 5 tahun ke depan adalah ' + str(int(umur)+5))
print('Halo nama saya',nama,',umur saya 5 tahun kedepan adalah', umur+5)

usiaAndi = 30
#usiaAndi = usiaAndi + 5
usiaAndi **= 2 #bisa dikali, tambah, kurang, bagi, bagi (//), pangkat
print(usiaAndi)

# CARA 1 IMPORT, ini kalo yang dipake semua library 
import math 

print(math.pi)
print(math.fabs(-8.99)) # membuat absolute
print(math.pow(4,3.6)) # pangkat (x,y)
print(math.sqrt(25)) # akar

print(math.ceil(4.2)) # pembulatan keatas
print(math.floor(4.9)) # pemnbulatan kebawah
print(round(5.345256, 2)) # pembulatan, berapa angka dibelakang koma.

# CARA 2 IMPORT # ini kalo yang dipake cuman dikit dan gamau ribet pake math.
from math import pi, fabs, floor, ceil, pow

print(pi)
print(floor(5.3))
print(ceil(5.3))

# STRING

x = 'Halo Dunia Lain'
print(x)
print(type(x))
print(len(x))
print(x.index('a'))
print(x.count('a'))
print(x.split())
print(x.split('a')) #by default memisahkan antar spasi
print(x.lower())
print(x.upper())
print(x.capitalize())
print('halo dunia lain. apa kabar'.capitalize())
print(x.replace('Dunia', 'Bumi'))

# Boolean
print(True + True * True) #gabisa dikali. Sama aja tetep hasilnya 2
print(True + False)
jomblo = True
print(jomblo)
print(type(jomblo))
a = 1
b = 2
c = 1
print(a==b)
print(a==c)

print("Halo hari Jum'at")
print('''Halo hari "Jum'at"''')

# INDEXING AND SLICING
print(x[-1])
print(x[0])
print(x[:3])
print()
print(x[2:]) #lo Dunia Lain
print(x[0:4]) #Halo
print(x[5:]) #Dunia Lain
print(x[x.index('D'):]) #Dunia Lain
print(x[-7:]) #ia Lain
print(x[:x.index('Dunia')]) #Halo
print(x[0::2]) #Hl ui an. 2 itu dilompatin 
print(x[0::1])
print(x[::-1])# dibalik niaL ainuD olaH
print(x[-1:-5:-1]) #niaL
print(x[:]) #Halo Dunia Lain

a = '0123456789'
b=[]
for i,j in enumerate (a):
    if i == 0:
        b.append(j+'-')
    elif i == 2:
        b.append('--'+j)
    else:
        b.append(j)
print(b)
c=''.join(b)
print(c)
print(i)
if a[i] == '0':
    print ('asd')
if i == 2:
    print('fhg')
else:
    print(i)
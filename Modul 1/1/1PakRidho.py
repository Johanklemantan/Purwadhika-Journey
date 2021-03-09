# print('Hello World!')
# print(29)

# #fungsi print adalah mencetak sesuatu

# nama = 'Ridho' #string
# umur = 29 #int
# pekerjaan = 'lecturer' # string
# tinggi = 173.5 # float
# jomblo = False # Boolean = True / False

# print(nama)
# print(umur)
# print(pekerjaan)
# print(jomblo)
# print(type(jomblo))

# print(False + False)
# print(True + True)
# print(True + False)

# a = 1
# b = 2
# c = 1
# print(a == b)
# print(a == c)



# dtype_nama = type(nama) # = <class 'str'>
# dtype_umur = type(umur) # = <class 'int'>

# print(dtype_nama)
# print(dtype_umur)
# print(type(nama))

# nama = input('What is your name: ') # aryo
# print('Hello my name is ' + nama + 'umur saya ' + str(29)) # jika menggunakan + jangan lupa menambahkan spasi dalam string
# print('Hello my name is', nama, 'umur saya', 29) # jika menggunakan , maka tidak perlu ditambah spasi

# nama = 25
# print(nama)

# print(2 + 1) # penjumlahan
# print(2 - 1) # pengurangan
# print(3 * 2) # perkalian
# print(4 / 2) # pembagian 2.0 => float
# print(4 // 2) # pembagian 2 => int
# print(5 % 2) # modulo
# print(5 / 2)
# print(5 // 2)
# print(2 ** 3) # pangkat / power
# print(4 ** 0.5)

# # mengganti data types
# x = '10'
# print(type(x))
# y = int(x)
# print(type(y))

# z = '25.5'
# # print(int(z))
# print(float(z))

# a = 23
# a_str = str(a)
# print(a_str)
# print(type(a_str))

# b = 1.5
# b_str = str(b) 
# print(b_str)
# print(type(b_str))

# c = '2'
# print(float(c)+10)
# 12.0

# nama 'Randy' (input)
# nama = input('What is your name: ')
# # umur 26 (input)
# umur = input('Input your age: ') # ketika menggunakan input, datatypes yang kita terima selalu dalam bentuk string
# Halo nama saya Randy, umur saya 5 tahun ke depan adalah 31
# print('Halo nama saya', nama, ', umur saya 5 tahun ke depan adalah', int(umur)+5)

# print('Halo nama saya ' + nama + ', umur sata 5 tahun ke depan adalah ' + str(int(umur)+5))

# usiaAndi = 30
# # usiaAndi = usiaAndi + 5
# # usiaAndi += 5
# # usiaAndi *= 2
# # usiaAndi /= 2
# # print(usiaAndi)

import math # cara 1
# # from math import pi, fabs, pow, sqrt, ceil, floor cara 2
# import math as m


# print(m.pi)
# # print(pi)
# print(m.fabs(-4.7))
# print(m.pow(2, 4))
# print(m.sqrt(16))

# print(m.ceil(2.5))
# print(m.floor(2.5))
# print(round(5.57532, 0))

## STRING

# x = 'Halo Dunia Lain'
# print(x)
# print(type(x))
# print(len(x))
# print(x.index('H'))
# print(x.split('a'))
# print(x.lower())
# print(x.upper())
# print(x.capitalize())
# print('halo dunia lain. apa kabar'.capitalize())
# print(x.replace('Dunia', 'Apa'))

# print("Halo Hari Jum'at") # Double Quote
# # print('Halo Hari Jum'at')
# print('''Halo Hari "Jum'at"''') # Triple Quote

## Indexing and Slicing
# 0123456789
#             -3-2-1
# Halo Dunia Lain
# print(x[0]) # H
# print(x[3]) # o
# print(x[14]) # n
# print(x[-1]) # n
# print(x[-5]) #  
# print(x[-15]) # H
# # print(x[15])
 
# print(x[0:4]) # Halo
# print(x[5:15]) # Dunia Lain
# print(x[5:]) # Dunia Lain
# print(x[x.index('D'):]) # Dunia Lain
# print(x[:x.index('L')]) # Halo Dunia *ada spasinya*
# print(x[:11]) # Halo Dunia *ada spasinya*
# print(x[:-4]) # Halo Dunia *ada spasinya*
# #  start:stop:step
# print(x[0:15:3]) # Hl ui an
# print(x[0:15:1]) # Halo Dunia Lain
# print(x[::-1]) # niaL ainuD olaH
# print(x[-1:-5:-1]) # niaL
# print(x[:])
# print(x)


# Take Home Practice

# No 1
# x=4
# y=3
# z=2
# w=((x+y*z)/(x*y))**z
# print(w)

# No 2
# angka = int(input('Silahkan masukkan angka berapapun: '))
# pangkat = int(input('Silahkan masukkan angka berapapun untuk pemangkat: '))
# print("Pangkat", pangkat, "dari angka", angka, "adalah:", int(math.pow(angka,pangkat)))

# No 3
# total_hari = int(input('masukkan hari: '))
# tahun = str(math.floor(total_hari/360))
# bulan = str(math.floor((total_hari%360)/30))
# minggu = str(math.floor(((total_hari%360)%30)/7))
# hari = str(math.floor(((total_hari%360)%30)%7))

# print(str(total_hari) + ' = ' + tahun + ' tahun ' + bulan + ' bulan ' + minggu + ' minggu ' + hari + ' hari ')

# No 4
# total = int(input('Total umur Andi dan Budi: '))
# rasio = float(input('Rasio umur Andi dan Budi: '))

# umur_budi = (total * 10) / (10 + (rasio * 10))
# umur_andi = total - umur_budi
# print('Umur Andi 2 tahun lagi adalah: {}'.format(umur_andi + 2))
# print(f'Umur Budi 2 tahun lagi adalah: {umur_budi + 2}')

# print(1 + 0.5)
# print(2 * 0.5)
# print(round(10 // 5.5, 5))

# No. 5
# word = input('Masukkan kata / kalimat:').lower()
# cari = input(f"Input huruf yang ingin dicari jumlahnya dari '{word}': ").lower()
# word2 = word.replace(cari, '')
# print(f'huruf {cari} ada {len(word)-len(word2)} buah')

# No. 6

jarak_dalam_km = int(input("Jarak antara kendaraan: "))
kecepatan_a_km = int(input("Kecapatan A dalam km: "))
kecepatan_b_km = int(input("Kecapatan B dalam km: "))
jam_berangkat = int(input('Jam Berangkat?: '))
menit_berangkat = int(input('Menit Berangkat?: '))

waktu_tabrakan_dalam_menit = (jarak_dalam_km/(kecepatan_a_km + kecepatan_b_km))*60
print(str(waktu_tabrakan_dalam_menit) + 'menit')

print(waktu_tabrakan_dalam_menit/60)

jam = math.floor(waktu_tabrakan_dalam_menit/60) + jam_berangkat
menit = (menit_berangkat + (waktu_tabrakan_dalam_menit%60)) % 60

print('Waktu A dan B bertabrakan adalah jam {}:{} WIB'.format(int(jam), int(menit)))
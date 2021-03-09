x = 5
y = '5'
z = 6

# conditional statement
# print(x == float(y)) # sama dengan
# print(x == z)
# print(x != z) # tidak sama dengan
# print(x > z) # lebih besar
# print(x < z) # lebih kecil / smaller than
# print(x >= int(y)) # lebih besar sama dengan
# print(x <= z) # lebih kecil sama dengan
print(~(3))

# # and atau or
# #     False and False = False
# print(x == z and x == z)
# #     False or True = True
# print(x == z or x < z)

# rules and
# True and True = True
# True and False = False
# False and True = False
# False and False = False

# rules or
# True or True = True
# True or False = True
# False or True = True
# False or False = False

# print(True not True)

# nilai = int(input('Masukkan nilai siswa: ')) # 75

#  60 >= 80 False
# if nilai >= 80:
#     print('Murid Lulus')
# else:
#     print('Murid harus remedi')

#   75 >= 80 False and 75 <= 100 True = False
# if nilai >= 80 and nilai <= 100: # False
#     print('A')
# #     75 >= 70 True and 75 < 80 True = True
# elif nilai >=70 and nilai < 80: # False
#     print('B')
# elif nilai >=50 and nilai < 70: # False
#     print('C')
# else:
#     print('D')

'''
input = 5
print = angka 5 termasuk bilangan ganjil

input massa dalam kg
input tinggi dalam cm

imt = ((massa / tinggi)/tinggi)*10000
< 18.5
berat badan anda kurang
18.5 - 24.9
berat badan anda ideal
25 - 29.9
bb anda berlebih
30 - 39.9
sangat berlebih
40 <
Anda obesitas

final result
Massa Anda 60 kg dan tinggi anda 1.7 m
IMT = ___
Berat badan Anda ideal
'''

# x = '$'
# print(x.isdigit())
# print(x.isalpha())
# print(x.isalnum())
# print(x.isnumeric())
# print(x.isascii())
# print('a' == 'a')

# print('12345'.isdigit())
# print('12345'.isnumeric())
# print('一二三四五'.isdigit())
# print('一二三四五'.isnumeric())

# berat = input('Masukkan berat (kg): ')
# tinggi = input('Masukkan tinggi (cm): ')

# if berat.isnumeric() == False or tinggi.isnumeric() == False:
#     print('Input only numerical data')
#     # isalpha: apakah sebuah string mengandung alphabet saja
#     # isalnum: apakah sebuah string mengandung alpha-numerical
#     # isnumeric: apakah sebuah string mengandung numerical saja

# else:
#     berat = int(berat)
#     tinggi = int(tinggi)
#     if berat < 40 or tinggi < 40:
#         print('Apakah Anda baik baik saja?')
#     else:
#         imt = ((berat / tinggi)/tinggi)*10000
#         print(f'Indeks massa tubuh anda adalah {imt}')
#         if imt < 18.5:
#             print('BB Anda kurang')
#         elif 18.5 < imt <= 24.9:
#             print('BB Anda ideal')
#         elif 24.9 < imt <= 29.9:
#             print('BB Anda berlebih')
#         elif 29.9 < imt <= 39.9:
#             print('BB Anda sangat berlebih')
#         else: print('Anda Obesitas')

'''
EXERCISES (not quiz)

1. Anda adalah penjual pisang. Yang mana pisang anda berharga 3000.
Buatlah sebuah program if-else yg memiliki kondisi, jika seseorang berbelanja di Anda lebih dari 100,000
maka akan diberikan diskon 10%. Kalau lebih dari 50,000 namun kurang dari 100,000 maka akan diberi diskon 5%.
Kalau kurang dari 50,000 maka tidak diberi diskon sama sekali.

contoh:
in: berapa pisang yg ingin anda beli? 30
out: total belanja Anda adalah IDR 85,500 (90,000 di diskon 5%)

2. Anda adalah seorang pemilik perusahaan dan Anda berniat untuk memberi bonus kepada pegawai Anda.
Buatlah program if-else yg memiliki kondisi, jika Year of Service seorang pegawai lebih dari 10 tahun,
maka gajinya akan diberi bonus sebesar 10%.

contoh:
in: berapa gaji anda? 10000000
in: year of service? 15

out: Selamat Anda mendapat bonus! Total gaji anda IDR 11000000

3. Ambil 3 input umur dari 3 user lalu tentukan siapa yang lebih tua.

contoh:
in: umur user_1 = 50
in: umur user_2 = 40
in: umur user_3 = 25

out: user 1 adalah yang paling tua

contoh lain:
in: umur user_1 = 40
in: umur user_2 = 40
in: umur user_3 = 40

out: tidak ada yang lebih tua

'''
# user_1 = int(input('Input umur user 1: '))
# user_2 = int(input('Input umur user 2: '))
# user_3 = int(input('Input umur user 3: '))

# #  True                    True    True
# if user_1 >= user_2 and user_1 >= user_3:
#     print('user 1 adalah yang paling tua')
# #  False                    True    False
# elif user_2 >= user_1 and user_2 >= user_3:
#     print('user 2 adalah yang paling tua')
# #  False                    False   False
# elif user_3 >= user_1 and user_3 >= user_2:
#     print('user 3 adalah yang paling tua')
# else:
#     print('tidak ada yang lebih tua')

'''
4. Buatlah program sederhana untuk menentukan apakah seorang siswa boleh mengikuti
ujian atau tidak berdasarkan presentase absennya. Minimal absensi adalah 75%.

contoh:
in: total kelas yang diadakan: 100
in: total attendances: 50

out: Total kehadiran Anda 50%. Maaf Anda tidak diperbolehkan mengikuti ujian.


'''




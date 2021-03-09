import math
#NO 1
# x=4
# y=3
# z=2
# w=((x+(y*z))/(x*y))**2
# print(w)

# #NO 2

# angka = int(input('Silakan masukkan angka berapapun : '))
# hasil = (angka**2)
# print('Kuadrat dari',angka,'=',hasil)

#NO 3

# total_hari = int(input('Masukkan jumlah hari : '))
# tahun = (math.floor(total_hari/360))
# bulan = (math.floor((total_hari-360)/30))
# minggu = (math.floor((total_hari-360)%30/7))
# hari = (math.floor((total_hari-360)%(30)%7))
# print(total_hari,'hari =',tahun,'tahun,',bulan,'bulan,',minggu,'minggu dan',hari,'hari.')

#NO 4

# Total_Usia = int(input("Masukkan total usia : "))
# Rasio = float(input("Masukkan Rasio usia : "))
# Usia_Budi = int(Total_Usia/(Rasio+1))
# Usia_Andi = Total_Usia-Usia_Budi
# print('Usia Budi 2 tahun lagi = ',int(Usia_Budi + 2))
# print('Usia Andi 2 tahun lagi = ',int(Usia_Andi + 2))

#NO 5
# Kata = input('Masukkan Kata :')
# Karakter = input('Masukkan Karakter yang ingin dicari :')
# print(Kata.count(Karakter))

#atau

# b = 'Halo Duniaa'
# count = 0
# for i in b:
#     if i == 'a':
#         count += 1
# print(count)

#NO 6
Jarak = int(input('Masukkan Jarak dalam Km:'))
Speed_A = int(input('Kecepatan A dalam Km/hr :'))
Speed_B = int(input('Kecepatan B dalam Km/hr :'))
Jam = int(input('Jam Awal : '))
Menit = int(input('Menit Awal : '))
Jam_akhir = math.floor((Jarak/(Speed_A + Speed_B) + (Jam + (Menit/60))))
print(Jam_akhir)
Menit_akhir = ((Jam+(Menit/60)+(Jarak/(Speed_A+Speed_B))-Jam_akhir)*60)
print(Menit_akhir)
print('A & B akan bertabrakan pada jam',Jam_akhir,'lewat',Menit_akhir,'menit')

















#No 6

# Jarak = int(input("Masukkan jarak dalam Km = "))
# Speed_A = int(input("Masukkan kecepatan A  dalam Km/hr= "))
# Speed_B = int(input("Masukkan kecepatan B dalam Km/hr = "))
# Jam_Awal= int(input("Jam Awal = "))
# Menit_Awal = int(input("Menit Awal = "))

# Jam = Jam_Awal + (Menit_Awal/60)

# Jam_bertabrakan = Jarak/(Speed_A + Speed_B) + Jam

# Jam_akhir = math.floor(Jam_bertabrakan)
# Menit_akhir = math.ceil((Jam_bertabrakan - Jam_akhir)*60)

# Jam_akhir1 = str(Jam_akhir);
# Menit_akhir1 = str(Menit_akhir)
# print("A & B akan bertabrakan pada jam " ,Jam_akhir1, " lewat " ,Menit_akhir1, " Menit")
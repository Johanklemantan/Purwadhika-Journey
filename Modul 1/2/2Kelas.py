# IF ELSE
x = 5
y = '5'
z = 6

print(x==float(y)) # sama dengan
print(x==z)
print(x!=z) #tidak sama dengan
print(x>z) #lebih besar
print(x<z) #lebih kecil
print(x>=int(y)) #lebih besar sama dengan
print(x<=z) #lebih kecil sama dengan


# and atau or

     #False and #True
print(x==z and x<z)
    # False or True
print(x==z or x<z)


# rules AND
# True and True --> True
# True and False --> False
# False and True --> False
# False and False --> False

# rules OR
# True or True --> True
# True or False --> True
# False or True --> True
# False or False --> False

nilai = int(input('Masukkan nilai siswa :'))
# nilai 60>=80 = False
if nilai >= 80:
    print('Murid lulus')
else :
    print('Murid harus remidi')

if nilai >=80 and nilai <=100:
    print('A')
elif nilai >=70 and nilai <80:
    print('B')
else :
    print('C')

x = 5;
y = '5';
z = 6;
print(x==int(y) and int(y)<z);
print(x==int(y) or int(y)<z);
print(not(x==int(y) or int(y)<z));

# Take class quiz 1
 
Angka = int(input('Masukkan angka :'))
if Angka % 2 == 0:
    print('Angka',Angka,'termasuk bilangan Genap')
else :
    print('Angka',Angka,'termasuk bilangan Ganjil')

# Take Class Quiz 2
Massa = int(input('Masukkan berat badan dalam kg : '))
Tinggi = int(input('Masukkan tinggi badan dalam cm : '))
IMT = ((Massa/Tinggi)/Tinggi)*10000
print('Berat badan ente adalah',Massa,'kg dan tinggi kamu adalah',float(Tinggi/100),'m. IMT kamu adalah',IMT)
if IMT < 18.5 :
    print('berat badan anda kurang')
elif IMT >=18.5 and IMT <=25.0:
    print('berat badan anda ideal')
elif IMT >=25.0 and IMT <=30.0:
    print('berat badan anda berlebih')
elif IMT >=30.0 and IMT <=40.0:
    print('berat badan anda sangat berlebih')
else :
    print('Anda obesitas')

# Atau
Massa = input('Masukkan berat badan dalam kg : ')
Tinggi = input('Masukkan tinggi badan dalam cm : ')

if Massa.isnumeric()== False or Tinggi.isnumeric()== False:
    #ada macam2
    #Isalpha : apakah sebuah string mengandung alphabet saja
    #Isnalnum : apakah sebuah string mengandung alpha-numerical
    #Isnumeric : apakah sebuah string mengandung numerical saja
    print('Input only numerical')
else :
    Massa=int(Massa)
    Tinggi=int(Tinggi)
    if Massa<40 or Tinggi<40:
        print('Are u okay ?')
    else :
        IMT = ((Massa/Tinggi)/Tinggi)*10000
        print('Berat badan ente adalah',Massa,'kg dan tinggi kamu adalah',(float(Tinggi/100)),'m. IMT kamu adalah',IMT)
        if IMT < 18.5 :
            print('berat badan anda kurang')
        elif IMT >=18.5 and IMT <=25.0:
            print('berat badan anda ideal')
        elif IMT >=25.0 and IMT <=30.0:
            print('berat badan anda berlebih')
        elif IMT >=30.0 and IMT <=40.0:
            print('berat badan anda sangat berlebih')
        else :
            print('Anda obesitas')


# AFTER CLASS (RESPONSI)

#xercise 1
jumlah_pisang = int(input('Berapa pisang yang ingin anda beli ?'))
harga_total = jumlah_pisang*3000
if harga_total > 100000:
    harga_total = int(harga_total*0.9)
elif harga_total>50000 and harga_total<100000:
    harga_total = int(harga_total*0.95)
else:
    harga_total = harga_total
print('Harga total belanja anda adalah IDR',('{:,}'.format(harga_total)))

# Exercise 2
gaji = int(input('Masukkan Gaji Anda :'))
year = int(input('Masukkan Year of Service :'))
if year>10:
    gaji *= 1.1
    print('Selamat Anda mendapat bonus!. Total Gaji anda IDR',('{:,}'.format(int(gaji))))
else:
    gaji==gaji
    print('Kerjanya kurang lama pak. Total gaji anda IDR',('{:,}'.format(int(gaji))))

# Exercise 3
Umur_1 = int(input('Masukkan umur 1 :'))
Umur_2 = int(input('Masukkan umur 2 :'))
Umur_3 = int(input('Masukkan umur 3 :'))
if Umur_1>Umur_2 and Umur_1>Umur_3 :
    print('User 1 adalah yang paling tua')
elif Umur_2>Umur_1 and Umur_2>Umur_3 :
    print('User 2 adalah yang paling tua')
elif Umur_3>Umur_1 and Umur_3>Umur_2 :
    print('User 3 adalah yang paling tua')
else:
    print('Tidak ada yang lebih tuaa')

# Exercise 4
kelas = int(input('Masukkan total kelas yang diadakan :'))
hadir = int(input('Masukkan total attendances :'))
if hadir/kelas >= 0.75:
    print('Total kehadiran Anda',(round((hadir/kelas)*100)),'%. Anda bisa ikut ujian')
else :
    print('Total kehadiran Anda',(round((hadir/kelas)*100)),'%. Maaf anda tidak diperbolehkan mengikuti ujian.')

x = 'python123'
print(x.isdigit())
print(x.isalpha())
print(x.isalnum())
print(x.isnumeric())
print(x.isascii())

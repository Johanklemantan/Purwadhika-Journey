# class uraiRajutKata():
#     def urai(self, kata):
#         self.kata = kata
#         stringPenampungUrai = ''
#         for i in range(len(self.kata)):
#             for j in range(i+1):
#                 stringPenampungUrai += self.kata[j]
#         return stringPenampungUrai
#     def rajut(self, kata):
#         self.kata = kata
#         stringPenampungRajut = ''
#         index = 0
#         for i in range(len(self.kata)):
#             for j in range(i):
#                 index += 1
#             if i+index <= len(self.kata):
#                 stringPenampungRajut += self.kata[i+index]
#         return stringPenampungRajut

# x = uraiRajutKata()
# print(x.urai('Code'))
# print(x.urai('Python'))
# print(x.urai('Purwadhika'))

# print(x.rajut('CCoCodCode'))
# print(x.rajut('PPyPytPythPythoPython'))
# print(x.rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))

# # perfecto numero uno
# class uraiRajutKata:
#     def urai(self, kata):
#         str_tampung = ''
#         b = len(kata)
#         for i in range(b):
#             a=0 
#             for a in range(i+1): 
#                 str_tampung = str_tampung + kata[a]
#         return str_tampung

#     def rajut(self, kata_uraian):
#         str_tampung = '' 
#         panjangKata = len(kata_uraian)
#         angkaTotal = 0
#         pengulangan = 0
#         penambah = 1
#         while angkaTotal <= len(kata_uraian): 
#             if angkaTotal != len(kata_uraian): 
#                 pengulangan += 1 
#                 angkaTotal = angkaTotal + penambah 
#                 penambah += 1
#             else:
#                 angkaTotal = angkaTotal + penambah

#         for i in range(panjangKata-1, panjangKata-pengulangan-1, -1): 
#             str_tampung = kata_uraian[i] + str_tampung
#         return str_tampung



# x = uraiRajutKata() 

# print(x.urai('Code'))
# print(x.urai('Python'))
# print(x.urai('Purwadhika'))

# print(x.rajut('CCoCodCode'))
# print(x.rajut('PPyPytPythPythoPython'))
# print(x.rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))

# import xlrd
# import xlsxwriter
# import xlwt 
# from xlwt import Workbook 


# book = xlsxwriter.Workbook("segitigaexcel.xlsx")
# sheet = book.add_worksheet("sheet1")

# def segitigakata(y):
#     z = ''
#     x = 0
#     kata = y.replace(' ', '')
#     # Pola Segitiga
#     pola = list(map(lambda row: row * (row + 1)/2, range(len(kata))))
#     pola = list(map(int, pola))

#     # Bentuk segitiga kata
#     if len(kata) not in pola:
#         print('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola')
#     else:
#         for i in range(pola.index(len(kata))):
#             for j in range(pola[i], pola[i + 1]):
#                 z += f"{kata[j]} "
#                 x += 1
#             z += '\n'
#         x = 0
    

#     return z

# row = 0
# sheet.write(1,0,segitigakata("purwadhika"))
# book.close()

# import requests 
# import json

# url = "http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json" 
# data = requests.get(url) 
# daftarProvinsi = data.json() 

# url = "http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json" 
# data = requests.get(url) 
# dataProvinsi = data.json() 

# provinsiDilan = "BANTEN"
# provinsiMilea = "JAWA BARAT" 

# keysProvinsi = list(daftarProvinsi.keys())
# valuesProvinsi = list(daftarProvinsi.values()) 

# for i in valuesProvinsi: 
#     if i == provinsiDilan: 
#         kodeProvinsiDilan = keysProvinsi[valuesProvinsi.index(i)] 
#         break

# for i in valuesProvinsi: 
#     if i == provinsiMilea: 
#         kodeProvinsiMilea = keysProvinsi[valuesProvinsi.index(i)] 
#         break

# for i in dataProvinsi[str(kodeProvinsiDilan)]: 
#     if i["urban"] == "SAMPORA" : 
#         if i["sub_district"] == "CISAUK": 
#             if i["city"] == "TANGERANG": 
#                 kodePosDilan = i["postal_code"]
#                 break

# for i in dataProvinsi[str(kodeProvinsiMilea)]: 
#     if i["urban"] == "CITARUM" : 
#         if i["sub_district"] == "BANDUNG WETAN": 
#             if i["city"] == "BANDUNG": 
#                 kodePosMilea = i["postal_code"]
#                 break
# apikey = "AkaypVfrop7FofpXt7tATDTwPKmBM3Lx7NaBXlDnUyBAvgLrop78L2s0kkQvu4OJ" 
# url = f"https://www.zipcodeapi.com/rest/{apikey}/distance.json/{kodePosDilan}/{kodePosMilea}/km " 

# data = requests.get(url)
# jarakJson = data.json() 
# jarak = jarakJson["distance"] 

# print(f"Kode Pos lokasi Dilan adalah {kodePosDilan}")
# print(f"Kode Pos lokasi Milea adalah {kodePosMilea}")
# print(f"Jarak Dilan & Milea adalah {jarak} km")

# import requests

# # Data Dilan
# dilan = {
#     'kelurahan':'SAMPORA',
#     'kecamatan':'CISAUK',
#     'kabupaten':'TANGERANG',
#     'provinsi':'BANTEN'
# }

# # Data Milea
# milea = {
#     'kelurahan':'CITARUM',
#     'kecamatan':'BANDUNG WETAN',
#     'kabupaten':'BANDUNG',
#     'provinsi':'JAWA BARAT'
# }

# # Mencari kode provinsi BANTEN dan JAWA BARAT
# url_kodeprov = 'https://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json'
# data_kodeprov = requests.get(url_kodeprov)

# kodeprov = data_kodeprov.json()
# kodeprov_keys = kodeprov.keys()
# kodeprov_values = kodeprov.values()
# kodeprov_dict = dict(zip(kodeprov_values, kodeprov_keys))

# kodeprov_dilan = kodeprov_dict[dilan['provinsi']]
# kodeprov_milea = kodeprov_dict[milea['provinsi']]

# # Mencari kode pos Dilan dan Milea
# url_kodepos = 'http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json'
# data_kodepos = requests.get(url_kodepos)

# kodepos = data_kodepos.json()
# # kodepos_dilan = kodepos[kodeprov_dilan]
# # kodepos_milea = kodepos[kodeprov_milea]

# for i in kodepos[kodeprov_dilan] :
#     if i['urban'] == dilan['kelurahan'] and i["sub_district"] == dilan['kecamatan'] and i["city"] == dilan['kabupaten'] :
#         kodepos_dilan = i["postal_code"]

# for i in kodepos[kodeprov_milea] :
#     if i['urban'] == milea['kelurahan'] and i["sub_district"] == milea['kecamatan'] and i["city"] == milea['kabupaten'] :
#         kodepos_milea = i["postal_code"]

# # Menentukan jarak Dilan dan Milea
# apikey ='9mkHDVaN6FSy48k6Govz8DU619IdmJloCCUpISJ6ZbZZMiHbAG7uH9LhAad9ROqC'
# url_jarak = f'http://www.zipcodeapi.com/rest/{apikey}/distance.json/{kodepos_dilan}/{kodepos_milea}/km'
# data_jarak =  requests.get(url_jarak)
# jarak = data_jarak.json()

# print(f"Kode Pos lokasi Dilan adalah {kodepos_dilan}")
# print(f"Kode Pos lokasi Milea adalah {kodepos_milea}")
# print(f"Jarak Dilan & Milea adalah {jarak['distance']} km") 

A={2,4,6,8,10,12,14,16,18,20} #bilangan genap antara 1 dan 20
B={1,3,5,7,9,11,13,15,17,19} #bilangan ganjil antara 1 dan 20
C={-9,-8,-7,-6,-5,-4,-3,-2,-1} #bilangan negatif lebih dari -10
D={2,3,5,7,11,13,17,19} #bilangan prima antara 1 dan 20
E={4,6,8,9,10,12,14,15,16,18,20} #bilangan komposit antara 1 dan 20

# print(type(A))
#soal A
print(A | B | C | D | E )

#soal B
print(((A & B) | (D & E)))

#soal C
print((A | B) & (D | E))

#soal D
print((A | B) - (D | E))

#soal E
print((A | B | C) - (A & E))

  
# A = himpunan (set) bilangan genap antara 1 dan 20.
# B = himpunan (set) bilangan ganjil antara 1 dan 20.
# C = himpunan (set) bilangan negatif lebih dari -10.
# D = himpunan (set) bilangan prima antara 1 dan 20.
# E = himpunan (set) bilangan komposit antara 1 dan 20.
# a. A ∪ B ∪ C ∪ D ∪ E
# b. (A ∩ B) ∪ (D ∩ E)
# c. (A ∪ B) ∩ (D ∪ E)
# d. (A ∪ B) - (D ∪ E)
# e. (A ∪ B ∪ C) - (A ∩ E)


A = []; B = []; C = []; D = []; E = []; F = [] 
prime = False
for i in range (1, 20):
    if i % 2 ==0:
        A.append(i)
    elif i % 2 != 0:
        B.append(i)
    if i >= 2:
        prime = True 
        if i > 2:
            for j in range (2,i):
                if i % j == 0:
                    prime = False
                    break
        if prime == True:
            D.append(i)
    if prime == False:
        E.append (i)   
    if i > 0 and i < 10:
        C.append (-i)

A = set(A)
B = set(B) 
C = set(C) 
D = set(D)
E = set(E)

print ('Selamat datang di operasi Himpunan! \nPilihan operasi: ')
print ('a. A ∪ B ∪ C ∪ D ∪ E\nb. (A ∩ B) ∪ (D ∩ E)\nc. (A ∪ B) ∩ (D ∪ E)\nd. (A ∪ B) - (D ∪ E)\ne. (A ∪ B ∪ C) - (A ∩ E)')
operasi = (input ('Masukan operasi pilihan anda (a/b/c/d/e): ')).lower()

if operasi == 'a': 
    hasil = A | B | C | D | E
elif operasi =='b':
    hasil  = (A & B) | ( D & E) 
elif operasi == 'c':
    hasil = (A | B) & (D | E)
elif operasi == 'd':
    hasil = (A | B) - (D | E)
elif operasi == 'e':
    hasil = (A | B | C) - (A & E)
else:
    print ('Pilihan yang anda masukan tidak tersedia')

print (f'Hasil operasi {operasi} adalah {hasil}')

# def segitigaKata(x):
#     new_x=x.replace(" ","")
#     counter=1
#     panjang=len(new_x)
#     valid= False
#     while panjang != 0:
#         if panjang - counter == 0:
#             valid=True
#             break
#         elif panjang - counter > 0:
#             panjang=panjang-counter
#             counter+=1
#         else:
#             valid=False
#             break

#     if valid == True:
#         new_kata1=x.replace(" ", '')
#         new_kata2=x.replace(" ", '')
#         i=0
#         while len(new_kata1) != 0:
#             kata=''
#             i+=1
#             for j in range(i):
#                 kata+=new_kata1[j] + ' '
#             new_kata1=new_kata1[i:]
#             print(kata)
#         while len(new_kata2) != 0:
#             kata=''
#             for k in range(i):
#                 kata+=new_kata2[k] +' '
#             print(kata)
#             new_kata2=new_kata2[i:]
#             i-=1
#     else:
#         print("Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.")


# print("# segitigaKata('Purwadhika')")           
# segitigaKata('Purwadhika')
# print("")

# print("# segitigaKata('Purwadhika Startup and Coding School @BSD')")           
# segitigaKata('Purwadhika Startup and Coding School @BSD')
# print("")

# print("# segitigaKata('kode')")           
# segitigaKata('kode')
# print("")

# print("# segitigaKata('kode python')")           
# segitigaKata('kode python')
# print("")

# print("# segitigaKata('lintang')")           
# segitigaKata('lintang')
# print("") 

# def segitigaKata (letters):
#     a = letters.replace(" ","")
#     l = list (a)
#     if len(l) == 10:
#         n = 4
#         def maju(n):   
#             num = 0
#             for i in range(0, n): 
#                 for j in range(0, i+1): 
#                     print(l[num], end=" ")  
#                     num = num + 1
#                 print("\r") 
#         maju(n)
#         def mundur(n):   
#                 num = 0
#                 for i in range(n, 0, -1): 
#                     for j in range(1, i+1): 
#                         print(l[num], end=" ")  
#                         num = num + 1
#                     print("\r") 
#         mundur(n)
#     elif len (l) == 36:
#         n = 8
#         def maju(n):   
#             num = 0
#             for i in range(0, n): 
#                 for j in range(0, i+1): 
#                     print(l[num], end=" ")  
#                     num = num + 1
#                 print("\r") 
#         maju(n)
#         def mundur(n):   
#             num = 0
#             for i in range(n, 0, -1): 
#                 for j in range(1, i+1): 
#                     print(l[num], end=" ")  
#                     num = num + 1
#                 print("\r") 
#         mundur(n)
#     else:
#         print ("Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.")

# segitigaKata("purwadhika")
# segitigaKata("Purwadhika Startup and Coding School @BSD")
# segitigaKata("kode python")
# segitigaKata("kode")
# segitigaKata("lintang")

# tahun = int(input("Masukan Tahun yang Ingin Di-cek : "))

# if (tahun % 4) == 0:
#     print('Tahun Kabisat')
# else:
#     print('Bukan Tahun Kabisat')

# def Kabisat():
#     tahun = int(input('ketikkan tahun : '))
#     if tahun%400 == 0:
#         chek = 'termasuk TAHUN KABISAT'
#     else:
#         if tahun%100 == 0:
#             chek = 'BUKAN termasuk TAHUN KABISAT'
#         else:
#             if tahun%4 == 0:
#                 chek = 'termasuk TAHUN KABISAT'
#             else:
#                 chek = 'BUKAN termasuk TAHUN KABISAT'
#     print(f'Hasil : {chek}')
#     return chek

# Kabisat()

# email = input('Masukan Email yang Ingin Di-cek : ')

# emailll = email.split('@')
# # print(email)
# asd = emailll[1].split('.')
# # print(asd)
# emailll.append(asd)
# print(emailll)

# alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# angka = [1,2,3,4,5,6,7,8,9]

# def cek_email(email):
#     email = email.replace('@', ' ')
#     email = email.replace('.', ' ')
#     split = email.split(' ')

#     if len(split) != 3: 
#         return 'tidak valid_1'
#     else:
#         x = emailll[0]
#         y = emailll[2][0]
#         z = emailll[2][1]
#         if z.isalpha() == False or len(z) > 5:
#             return 'tidak valid_2'    
#         else:
#             if y.isalnum():
#                 if x.isalnum() == True or '-' in x or '_' in x:
#                     return 'valid_1'
#                 else:
#                     return 'valid_2'
#             else:
#                 return 'tidak valid_3'

# # Angka di sebelah valid / tidak valid untuk cek error dan jalan dimana

# print(cek_email(email))

# a = input('Input email: ')
# def coba(a):
#     a = a.replace('@', ' ')
#     a = a.replace('.', ' ')
#     a_split = a.split(' ')

#     if len(a_split) != 3: 
#         return 'Email tidak valid'
#     else:
#         nU = a_split[0]
#         nH = a_split[1]
#         tambahan = a_split[2]
#         if tambahan.isalpha() == False or len(tambahan) > 5:
#             return 'Email tidak valid'    
#         else:
#             if nH.isalnum() == True:
#                 if nU.isalnum() == True or '_' in nU or '-' in nU:
#                     return 'Email valid'
#                 else:
#                     return 'Email tidak valid'
#             else:
#                 return 'Email tidak valid'
# print(coba(a)) 

# def cekNPWP(x):
#     hrf = '0123456789-.'
#     status = True
#     syarat1 = ['01','02','03','04','06','05','07','08','09']

#     for i in x:
#         if i not in hrf:
#             status = False

#     if '-' not in x and '.' not in x:
#         status = False

#     if x.split('.')[0] not in syarat1:
#         status = False

#     if status:
#         print('Output: Kode seri NPWP valid!')

#         if x.split('.')[0] in syarat1[:3]:
#             print('Identitas Wajib Pajak:', x.split('.')[0], 'Wajib Pajak Badan')
#         elif x.split('.')[0] in syarat1[3:5]:
#             print('Identitas Wajib Pajak:', x.split('.')[0], 'Wajib Pajak Pengusaha')
#         elif x.split('.')[0] in syarat1[5]:
#             print('Identitas Wajib Pajak:', x.split('.')[0], 'Wajib Pajak Karyawan')
#         elif x.split('.')[0] in syarat1[6:9]:
#             print('Identitas Wajib Pajak:', x.split('.')[0], 'Wajib Pajak Orang Pribadi')

#         print('Nomor Registrasi: ', x.split('.')[1] + '.' + x.split('.')[2])            
#         print('Alat pengaman: ', x.split('.')[3].split('-')[0])
#         print('Kode KPP: ', x.split('.')[3].split('-')[-1])      
#         print('Status Wajib Pajak: ', x.split('.')[-1])      
#     else:
#         print('Output: Kode seri NPWP tidak valid!')

# cekNPWP('091234560123123')
# cekNPWP('99.999.999.9-999.999')
# cekNPWP('09.123.456.A-123.123')
# cekNPWP('07.123.456.0-212.191')

# # membuat function pangkat => rekursif
# def pangkat(a,b):
#     kali = int(a)
#     # print(kali)
#     a = int(a)
#     # print(a)
#     kali = a
#     i = 1
#     while i < int(b):
#         kali = kali * a
#         i += 1
#     return kali
    
# print(pangkat(2,2))
# print(pangkat(3,3))
# print(pangkat(10,5))

# # # just in case menggunakan input untuk parameter a & b
# # # print(pangkat(input('Masukkan angka pertama: '), input('Masukkan angka kedua: '))) 
# print(pangkat(input('Masukkan angka pertama: '), input('Masukkan angka kedua: ')))

# def pangkat(x, y):
#     if (y == 0):
#         return 1
#     elif (int(y % 2) == 0):
#         return (pangkat(x, int(y/2)) * pangkat(x, int(y/2)))
#     else:
#         return (x * pangkat(x, int(y / 2)) * pangkat(x, int(y / 2))) 

# print(pangkat(2,2))
# print(pangkat(3,3))
# print(pangkat(10,5))
# print(pangkat(input('Masukkan angka pertama: '), input('Masukkan angka kedua: ')))

# def balikPosisi(a):
#     list_balik = []
#     for i in range(1, len(a)+1):
#         list_balik.append(a[-i])
#     return list_balik


# print(balikPosisi([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(balikPosisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
# print(balikPosisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))

# def fpb(a,b):
#     if a<b:
#         smaller=a
#     else:
#         smaller=b
#     for i in range (1,smaller+1):
#         if a%i==0 and b%i==0:
#             fpb=i
#         # else:
#         #     continue
#     return fpb
# def kpk(a,b):
#     kpk=int(a*b/fpb(a,b))
#     return kpk
# a=int(input('Masukkan angka pertama :'))
# b=int(input('Masukkan angka kedua   :'))
# print('FPB dari ',a,' dan ',b,' adalah ',fpb(a,b))
# print('KPK dari ',a,' dan ',b,' adalah ',kpk(a,b))

# bil1 = int(input('Ketik angka pertama   :'))
# bil2 = int(input('Ketik angka kedua     :'))

# def fpb(bil1,bil2):
#     while 1:
#         sisa = bil1 % bil2
#         if sisa == 0:
#             break
#         bil1, bil2 = bil2, sisa
#     return bil2
# print('FPB dari', bil1, 'dan', bil2, 'adalah =', fpb(bil1,bil2))

# def kpk(bil1,bil2):
#     perkali1 = 1
#     perkali2 = 1
#     p = bil1 * perkali1
#     q = bil2 * perkali2
#     while p != q:
#         while p > q:
#             perkali2 += 1
#             q = bil2 * perkali2
#         while p < q:
#             perkali1 += 1
#             p = bil1 * perkali1
#     if p == q:
#         return p
# print('KPK dari', bil1, 'dan', bil2, 'adalah =', kpk(bil1,bil2)) 

# def kpk(x, y):
#    if x > y:
#        faktor = x
#    else:
#        faktor = y

#    while True:
#        if((faktor % x == 0) and (faktor % y == 0)):
#         #    kpk = faktor
#            break
#        faktor+= 1
#    return faktor

# a = int(input("Ketik angka pertama: "))
# b = int(input("Ketik angka kedua: "))

# print("kpk dari", a,"and", b,"is", kpk(a, b))

# def FPB(x, y): 

#     if x > y: 
#         nilai = y 
#     else: 
#         nilai = x 
#     for i in range(1,nilai+1): 
#         if((x % i == 0) and (y % i == 0)): 
#             FPB = i 

#     return FPB 

# d = int(input("Ketik angka pertama: "))
# e = int(input("Ketik angka kedua: "))


# print("FPB dari", d,"and", e,"is", FPB(d, e)) 

# x = int(input('Ketik angka: '))

# def factor(a):
#     factor=[]
#     for i in range(1,a+1):
#         if a%i == 0:
#             factor.append(i)
#     return factor

# def categorize(x):
#     list1 = []
#     if isinstance(x, int) :
#         list1.append('bulat')
#     if x >= 0:
#         list1.append('cacah')
#     if x<0:
#         list1.append('negatif')
#     if x == 0:
#         list1.append('nol')
#     if x>0:
#         list1.append('asli')
#     if x%2 !=0:
#         list1.append('ganjil')
#     if x%2 == 0:
#         list1.append('genap')
#     if x != 1 and sum(factor(x))==x+1:
#         list1.append('prima')
#     if x >0 and sum(factor(x))!=x+1:
#         list1.append('komposit')

#     return list1
# print(categorize(x)) 

# words = input('Input words: ').replace(' ', '')

# def word_triangle(sentences):  
#     sen_list = list(sentences)
#     rules = []
#     for a in range(len(sen_list)):
#         x = int((a*(a+1))/2)
#         rules.append(x)

#     n=0
#     if len(sen_list) not in rules:
#         print ('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.')
#     else:
#         n= rules.index(len(sen_list)) 
#     y = 0
#     for i in range(0, n): 
#         for j in range(0, i+1): 
#             print(sen_list[y], end=" ")  
#             y += 1
#         print("\r")   
#     z = 0
#     for i in range(n, 0, -1): 
#         for j in range(1, i+1): 
#             print(sen_list[z], end=" ")  
#             z += 1
#         print("\r") 

# word_triangle(words)

# def Hastag(string) :
#     if string == '' :
#         return False
#     elif len(string.replace(' ','')) > 139 : # 139 karena sudah ada hastag(#) jadi 140 = '#' + 139
#         return False
#     else :
#         kata = '#'
#         string = list(string.split())
#         for a in range(0,len(string)) :
#             string[a] = string[a].capitalize()
#             kata += string[a]
#         return kata

# print(Hastag(' Hello there how are you doing'))
# print(Hastag("  Hello  World  "))
# print(Hastag(""))

# def create_phone_number(number) :
#     angka = 0
#     x = 0
#     for a in number :
#         if type(a) == int :
#             angka += 1
#         if a > 9 or a < 0  :
#             x += 1


#     if angka != len(number) :
#         return 'Just input the number'
#     elif x != 0 :
#         return 'Just input number in range 0-9'
#     elif len(number) == 10 :
#         no = '('
#         for a in range(0,3) :
#             no += str(number[a])
#         no += ') '
#         for a in range(3,6) :
#             no += str(number[a])
#         no += '-'
#         for a in range(6,len(number)) :
#             no += str(number[a])        
#         return no
#     else :
#         return 'Input 10 digits of number!'

# print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))

# def sort_odd_even(num) :

#     odd = []
#     even = []
#     for a in range(0,len(num)) :
#         if num[a]%2 == 0 :
#             even.append(a)
#         else :
#             odd.append(a)
#     for a in range(0,len(odd)-1) :
#         for b in range(a,len(odd)) :
#             if num[odd[a]] > num[odd[b]] :
#                 num[odd[a]], num[odd[b]] = num[odd[b]], num[odd[a]]

#     for a in range(0,len(even)-1) :
#         for b in range(a,len(even)) :
#             if num[even[a]] < num[even[b]] :
#                 num[even[a]], num[even[b]] = num[even[b]], num[even[a]]

#     return num

# print(sort_odd_even([5,3,2,8,1,4]))
# print(sort_odd_even([5,7,2,8,1,4,3,6,9])) 

# def hollowTriangel(angka) :

#     if type(angka) != int :
#         return 'Just input number'
#     else :
#         bintang = ''
#         for a in range(0,angka) :
#             if a == angka-1 :
#                 bintang += '#'*(angka*2-1)
#             elif a == 0 :
#                 bintang += '_'*(angka-a-1) + '#' + '_'*(angka-a-1) + '\n'
#             else :
#                 bintang += '_'*(angka-a-1) + '#' + '_'*(a*2-1) + '#' + '_'*(angka-a-1) + '\n'

#         return bintang

# print(hollowTriangel(6))



# # Function Initialization
# # def counterClockwise(List): #buat fungsi 
# def counterClockwise(List): #buat fungsi ada parameterny dinamakan List
#     putarbalik = [] #buat tempat penyimpanan yg nanti akan di append
#     # print(putarbalik)
#     for i in range(len(List[0]), 0, -1): #buat fungsi i dg jarak dr length parameter list,0 dan step -1 (jadi i 3 2 1 karna turun)
#         putarbalik.append(list(map(lambda x: x[i-1], List))) #menggunakan append dan fungsi lambda. map digunakan karna iterasi. list harus ditulis kalo tidak nanti jd call objekny saja 
#         #bkin vriable x yg fungsiny membaca index i-1 dr list. List adalah dia baca dr parameter fungsi counterClock
#         #nanti dia akan mengambil setiap angka terakhir dr list jd 3,6,9 dulu 
#     return putarbalik #kembali ke putarbalik pengganti print
# List_awal = [[1,2,3]
#             ,[4,5,6]
#             ,[7,8,9]]
# # Use the Function
# print(counterClockwise(List_awal)) #cetak fungsi counterclock dengan parameter List_awal yg sudah di tentukan 
# print(counterClockwise(List_awal)) #cetak fungsi counterclock dengan parameter List_awal yg sudah di tentukan

'''
ujian no 2

def moveZeros(array):
    ListBaru=[]
    ListIsiNol = []
    for i in array:
        # False == 0 will evaluate to True (but False should stay in place), ignore boolean types
        # not isinstance(i, bool) means anything other than True or False
        # True and False (like everything else) are objects in python
        if not isinstance(i, bool):
            # at this point, we can use ==, which will only evaluate to True if an int or float is zero
            if i == 0:
                # add the zero, but maintain the type (int or float)
                ListIsiNol.append(i)
                # go to the next iteration
                continue
        # if the continue statement wasn't executed, everything else will be added here
        ListBaru.append(i)
    # append the zero list (with the same types) to the non-zero list
    return ListBaru + ListIsiNol

print(moveZeros([False,1,0,1,2,0,1,3,"a"]))
print(moveZeros([0,0,0,"test",0,3,"a",True,False]))
print(moveZeros([0,True,True,False,"a","b",1,1,1]))
'''

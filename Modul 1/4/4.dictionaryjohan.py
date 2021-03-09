#dictionary = 'key1' : 'value1',
                # 'key2' : 'value 2'

# employee = {
#     #key  : value
#     'nama' : 'Andy',
#     'usia' : 20,
#     'married' : True,
#     'jabatan' : 'IT Engineer',
#     'kendaraan' : ['mobil','motor'],
#     'address' : {
#         'street' : 'Jalan Mawar',
#         'RT' : 5,
#         'RW' : 2,
#         'zipcode' : 12345,
#         'geo' : {
#             'lat' : 12345.621271,
#             'long': 1232131.12313
#         }
#     }

# }
# # print(employee)
# # print("value di dalam key'nama' adalah", employee['nama'])
# # print("value di dalam key'kendaraan' adalah",employee['kendaraan'])
# # print("value di dalam key'kendaraan' di index pertama adalah",employee['kendaraan'][0])
# # print("value di dalam key 'address' adalah",employee['address'])
# # print("value di dalam key 'address' nama jalan saja adalah",employee['address']['street'])

# # print(list(employee.keys()))
# # print(list(employee.values()))
# # print(list(employee['address'].keys()))

# # #GET = MANggil values. Gabisa buat manggil keys
# # print(employee.get('nama','Key not Found'))
# # print(employee.get('Nama','Key not Found'))
# # print(employee.get('Nama'))
# # print(employee.get('Andy','Salah'))

# # #ASSIGN = memasukkan value baru ke key yang juga baru di posisi terakhir
# # employee['gaji'] = 2000000
# # print(employee)

# #Update value di key yang sudah ada
# employee['gaji'] = 3000000
# employee['kendaraan'].append('scooter') # PAKE Kurung biasa
# print(employee)

# # #.update (pake dot) langsung update beberapa keys
# # employee.update({'NIK' : 3493492, 'BPJS' : 881349})
# # print(employee)

# #.ITEMS = untuk melihat pasangan
# print(list(employee.items()))
# print(list(employee['address'].items()))
# print(list(employee['address']['geo'].items()))

# #NGECEK Apakah value ada di dalam dict ?
# print('Cari value 3.000.000 ada di values apa engga ?',3000000 in employee.values())

# #cari value terkecil atau tertinggi di dalam dict

# nilai_ujian = {
#     'Fisika' : 82,
#     'Matematika' : 65,
#     'Sejarah' : 75
# }
# print('Mata pelajaran yang nilainya paling kecil adalah', min(nilai_ujian,key=nilai_ujian.get ))
# print('Mata pelajaran yang nilainya paling tinggi adalah', max(nilai_ujian,key=nilai_ujian.get ))


# #MENGGANTI NAMA KEY
# employee['alamat'] = employee.pop('address')
# print(employee)

#MENGGANTI 2 DICTIONARY
# dict1 = {'Ten' : 10, 'Twenty' : 20, 'Thirty' : 30}
# dict2 = {'Forty' : 40, 'Fifty' : 50, 'Sixty' : 60}
# dict5 = {70 : 'Seventy', 80 : 'Eighty'}

# dict3 = dict1.copy()
# dict3.update(dict2)
# print(dict3)

# # atau menggabungkan 2 dict atau lebih
# dict4 = {**dict1, **dict5, **dict2}
# print(dict4)


# #membuat dictionary dari 2 bulah list
# key = ['Ten','Twenty','Thirty']
# value = [10,20,30]

# # ZIP = MENGGABUNGKAN LIST ATAU SET ATAU TUPLE JADI 1
# sample_dict = dict(zip(value,key))
# sample_dict2 = dict(zip(key,value))

# sample_tuples = tuple(zip(key,value))
# print(sample_dict)
# print(sample_dict2)
# print(sample_tuples)

#initialize dictinonary with default values

karyawan = ['Doni', 'Fiki','Akbar']
defaults = {'designation' : 'Application Developer', 'Salary' : 5000000}

res_dict = dict.fromkeys(karyawan,defaults)
print(res_dict)

print(res_dict['Doni'])
print(res_dict['Fiki'])
print(res_dict['Akbar'])


'''
Quiz : day translator

No. 1
Masukkan hari : Senin
Output : bahasa inggris dari Senin adalah Monday

No. 2
Masukkan hari (INA/ENG) : Senin
Output : bahasa inggris dari senin adalah Monday

Masukkan hari (INA/ENG) : Monday
Output : bahasa Indonesia dari Monday adalah Senin
'''

# kamus = {
#     "senin" : "monday",
#     "selasa" : "tuesday",
#     "rabu" : "wednesday",
#     "kamis" : "thursday",
#     "jumat" : "friday",
#     "sabtu" : "saturday",
#     "minggu" : "sunday"
# }

# # NO 1
# Hari = input('Masukkan hari : ').lower()
# print(f'Bahasa Inggris dari',Hari.capitalize(),'adalah',kamus[Hari].capitalize())


#NO 2
# print(kamus.values())
# print(kamus.keys())
# Day = input('Masukkan hari (INA/ENG) :').lower()
# ina = list(kamus.keys()) #[senin, selasa, rabu, kamis, jumat, sabtu, minggu]
# eng = list(kamus.values()) #[monday, tuesday, wednesday, thursday, friday, saturday, sunday]
# if Day in ina :
#     print(f'Bahasa Inggris dari',Day.capitalize(),'adalah',kamus[Day].capitalize())
# elif Day in eng:
#     print(f'Bahasa Indonesia dari',Day.capitalize(),'adalah',ina[eng.index(Day)].capitalize())
# else :
#     print('Salah masukin kata')
# print(ina)
# print(ina[4])
# print(eng.index('saturday'))



# dictionary = 'key', 'value'

employee = {
    # key :  value
    'nama': 'Andy',
    'usia': 20,
    'married': True,
    'jabatan': 'IT Engineer',
    'kendaraan': ['mobil', 'motor'],
    'address': {
        'street': 'Jalan Mawar',
        'RT': 5,
        'RW': 2,
        'zipcode': 12345,
        'geo': {
            'lat': 12345.621271,
            'long': 1232131.12313
        }
    }
}

print(employee)
# print("Value di dalam key 'nama' adalah:", employee['nama'])
# print("Value di dalam key 'kendaraan' adalah:", employee['kendaraan'])
# print("Value di dalam key 'kendaraan' di index pertama:", employee['kendaraan'][0])
# #                                                         ['mobil', 'motor][0] = 'mobil'
# print("Value di dalam key 'address' adalah:", employee['address'])
# print("Value di dalam key 'address' nama jalan saja:", employee['address']['street'])
# #                                                       ['mobil', 'motor][0] = 'mobil'

# print(list(employee.keys()))
# print(list(employee.values()))

# # GET
# print(employee.get('nama'))
# print(employee.get('gaji'))
# # print(employee['gaji']) error
# print(employee.get('gaji', 'Key Not Found'))

# # Assign Value Baru ke Key yg juga baru
# employee['gaji'] = 2000000
# print(employee)

# # Update value di key yang sudah ada
# employee['gaji'] = 3000000
# print(employee)
# employee['kendaraan'].append('scooter')
# print(employee)

# # .update untuk mengupdate key dan value
# employee.update({'NIK': 92131231, 'BPJS': 10000002121})
# print(employee)

# # .items
# print(list(employee.items()))
# print(list(employee['address'].items()))
# print(list(employee['address']['geo'].items()))

# print(employee.get('gaji'))
# print(employee.items())

# # cari value apakah ada di dictionary atau tidak
# print('Cari value 3,000,000 ada atau ngga?: ', 3000000 in employee.values())

# # cari value terkecil atau tertinggi di dalam dictionary
# nilai_ujian = {
#     'Matematika': 82,
#     'Fisika': 82,
#     'Sejarah': 75
# }

# print('Mata pelajaran yang nilainya paling kecil: ', min(nilai_ujian, key=nilai_ujian.get))
# print('Mata pelajaran yang nilainya paling tinggi: ', max(nilai_ujian, key=nilai_ujian.get))

# # mengganti nama key
# employee['alamat'] = employee.pop('address')
# print(employee)

# # menggabungkan 2 dictionary
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Forty': 40, 'Fifty': 50, 'Sixty': 60}

# # .update
# dict3 = dict1.copy()
# dict3.update(dict2)
# print(dict3)

# # cara ke-2
# dict1_dict2 = {**dict1, **dict2}
# print(dict1_dict2)

# # membuat dictionary dari 2 buah list
# key = ('Ten', 'Twenty', 'Thirty', 'Thirty') # itterable
# value = (10, 20, 30, 40) # itterable

# sample_dict = dict(zip(key, value))
# sample_dict_reversed = dict(zip(value, key))
# print(sample_dict)
# print(sample_dict_reversed)

# sample_list = list(zip(key, value))
# print('ini sample list', sample_list)

# sample_tuple = tuple(zip(key, value))
# print('ini sample tuple', sample_tuple)

# sample_dict_test = {*key, *value}
# print(sample_dict_test)

# # Initialize dictionary with default values
# karyawan = ['Doni', 'Fiki', 'Akbar']
# defaults = {'designation': 'Application Developer', 'salary': 5000000}

# res_dict = dict.fromkeys(karyawan, defaults)
# print(res_dict)

# print(res_dict['Doni'])

# '''
# No. 1
# Masukkan hari: Senin 
# output: bahasa inggris dari Senin adalah Monday

'''

# hari_dict = {
#     'senin': 'monday',
#     'selasa': 'tuesday',
#     'rabu': 'wednesday',
#     'kamis': 'thursday',
#     'jumat': 'friday',
#     'sabtu': 'saturday',
#     'minggu': 'sunday'
# }

# hari = input('Masukkan hari: ').lower()

# if hari in list(hari_dict.keys()):
#     print(f"Bahasa Inggris dari hari {hari.upper()} adalah {hari_dict[hari].upper()}")
# else:
#     print('Invalid Input')

'''

# No. 2
# Masukkan hari (INA/ENG): senin
# output: bahasa inggris dari senin adalah Monday

# Masukkan hari (INA/ENG): monday
# output: bahasa indonesia dari monday adalah Senin
# '''
# hari_list = list(hari_dict.keys())
# day_list = list(hari_dict.values())

# user_input = input("Masukkan hari (INA/ENG): ").lower()

# if user_input in hari_list:
#     day = day_list[hari_list.index(user_input)]
#     print(f"Bahasa Inggris dari {user_input.upper()} adalah {day.upper()}")
# elif user_input in day_list:
#     hari = hari_list[day_list.index(user_input)]
#     print(f"Bahasa Indonesia dari {user_input.upper()} adalah {hari.upper()}")
# else:
#     print(f"Hari {user_input} tidak ditemukan.")

# print(isinstance(['a', 'b', 'c'], list)) # True

# print(employee.get('nama', 'Not Found'))

# import itertools

# print(dict(itertools.islice(employee.items(), 4)))
# print(employee['gaji'])
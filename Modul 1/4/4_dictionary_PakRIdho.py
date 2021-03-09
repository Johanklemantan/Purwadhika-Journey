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
print("Value di dalam key 'nama' adalah:", employee['nama'])
print("Value di dalam key 'kendaraan' adalah:", employee['kendaraan'])
print("Value di dalam key 'kendaraan' di index pertama:", employee['kendaraan'][0])
#                                                         ['mobil', 'motor][0] = 'mobil'
print("Value di dalam key 'address' adalah:", employee['address'])
print("Value di dalam key 'address' nama jalan saja:", employee['address']['street'])
#                                                       ['mobil', 'motor][0] = 'mobil'

print(list(employee.keys()))
print(list(employee.values()))

'''
No. 1
Masukkan hari: Senin 
output: bahasa inggris dari Senin adalah Monday

No. 2
Masukkan hari (INA/ENG): senin
output: bahasa inggris dari senin adalah Monday

Masukkan hari (INA/ENG): monday
output: bahasa indonesia dari monday adalah Senin
'''
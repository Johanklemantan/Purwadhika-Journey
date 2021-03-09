mobil = ['Toyota', 'Honda', 'Mercedes']

print(type(mobil))
print(mobil)

# indexing
print(mobil[0])
print(mobil[1])
# print(mobil[5])

# slicing
print(mobil[0:2])
print(mobil[:3])
print(mobil[2:7])
print(mobil[::-1])

# append = menambahkan element di posisi paling belakang
mobil.append('BMW')
print(mobil)
mobil.append('Mercedes')
print(mobil)

# pop = meremove element yang ada di posisi paling belakang
hasil_pop = mobil.pop()
print(mobil)
print(hasil_pop)

# index = mengetahui index dari sebuah element tertentu
print('Index dari mobil Toyota:', mobil.index('Toyota'))
print('Index dari mobil Mercedes:', mobil.index('Mercedes'))

print(mobil[0].index('y'))
print(mobil[mobil.index('Mercedes')].index('s'))
#     mobil[0].index('y')
#     'Toyota'.index('y')

# copy = membuat copy dari list
mobil_copy = mobil.copy()
print(mobil)
print(mobil_copy)

mobil_copy.pop()
print(mobil) # tidak akan terdampak oleh pop dari mobil_copy
print(mobil_copy)

mobil2 = mobil
print(mobil)
print(mobil2)

mobil2.pop()
print(mobil)
print(mobil2)
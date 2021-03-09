#           0           1       2
# mobil = ['Toyota', 'Honda', 'Mercedes']
# campur = [1, 'Surabaya', 2, 'Adidas', True, False, [4,5,6]]

# print(type(campur))

# print(type(mobil))
# print(mobil)

# # indexing
# print(mobil[0])
# print(mobil[1])
# # print(mobil[5])

# # slicing
# print(mobil[0:2]) # ['Toyota', 'Honda']
# print(mobil[:3]) # ['Toyota', 'Honda', 'Mercedes']
# print(mobil[2:7]) # ['Mercedes']
# print(mobil[::-1]) # ['Mercedes', 'Honda', 'Toyota']
# print('coba coba', mobil[3:]) # []

# # append = menambahkan element di posisi paling belakang
# mobil.append('BMW')
# print(mobil) # ['Toyota', 'Honda', 'Mercedes', 'BMW']
# mobil.append('Mercedes')
# print(mobil) # ['Toyota', 'Honda', 'Mercedes', 'BMW', 'Mercedes']

# # pop = meremove element yang ada di posisi paling belakang
# hasil_pop = mobil.pop()
# print(mobil) # ['Toyota', 'Honda', 'Mercedes', 'BMW']
# print(hasil_pop) # 'Mercedes'
# mobil.pop(1)
# print(mobil)

# # index = mengetahui index dari sebuah element tertentu
# print('Index dari mobil Toyota:', mobil.index('Toyota'))
# print('Index dari mobil Mercedes:', mobil.index('Mercedes'))

# print(mobil[0].index('y'))
# print(mobil[mobil.index('Mercedes')].index('s'))
# #     mobil[0].index('y')
# #     'Toyota'.index('y')

# # copy = membuat copy dari list
# mobil_copy = mobil.copy()
# print(mobil)
# print(mobil_copy)

# mobil_copy.pop()
# print(mobil) # tidak akan terdampak oleh pop dari mobil_copy
# print(mobil_copy)

# mobil2 = mobil
# print(mobil)
# print(mobil2)

# mobil2.pop()
# print(mobil)
# print(mobil2)

# # insert = memasukkan element di index tertentu
# mobil.insert(0, 'Hummer')
# print(mobil)
# mobil.insert(10, 'Citroen')
# print(mobil)
# mobil.insert(2, 'Jaguar')
# print(mobil)
# # mobil.insert(3, ['BMW', 'Porsche'])
# # print('tes masukin list', mobil)

# # sort = mengurutkan (reverse = True/False)
# mobil.sort(reverse=False)
# print(mobil)
# print(mobil.index('Citroen'))

# # reverse = membalik urutan dari list
# mobil.reverse()
# print(mobil)

# a = [4,3,2,5,6,7]
# print(a[::-1]) # [7,6,]
# a.sort(reverse=False)
# print(a)

# b = ['Python', 'Java', 'C', 'Javascript']
# b.reverse()
# print(b)

# # count = menghitung ada berapa element tertentu dalam sebuah list
# print(mobil.count('Toyota'))
# mobil.append('Toyota')
# print(mobil.count('Toyota'))

# # extend = memasukkan beberapa element sekaligus
# # mobil.append('Ferrari', 'Honda', 'Toyota')
# mobil.append(['Ford', 'Honda', 'Toyota'])
# #                   0           1          2        3          4          5                     6
# print(mobil) # ['Toyota', 'Mercedes', 'Jaguar', 'Hummer', 'Citroen', 'Toyota', ['Ferrari', 'Honda', 'Toyota']]
# print(mobil[6])
# mobil.extend(['Honda', 'Toyota', 'Ferrari'])
# #                   0           1          2        3          4          5                     6                   7         8         9  
# print(mobil) # ['Toyota', 'Mercedes', 'Jaguar', 'Hummer', 'Citroen', 'Toyota', ['Ford', 'Honda', 'Toyota'], 'Ferrari', 'Honda', 'Toyota']
# # mobil.extend('Ferrari')
# # print(mobil)
# print(mobil[6][0])
# #     ['Ford', 'Honda', 'Toyota'][0]
# #     Ford

# # cara mengganti element pada index tertentu
# # mobil[6] = 'Ford'
# mobil[6][1] = 'Porsche'
# # mobil[6][1][3] = 'z'
# print(mobil)

# # broadcasting
# mobil[0:3] = 'Porsche', 'Ford', 'Toyota'
# print(mobil)
# mobil[3], mobil[6], mobil[8] = 'Ford', 'Toyota', 'BMW'
# print(mobil)
# mobil[0:3] = ['Mercedes'] # bisa, tapi mengurangi panjang dari list kita
# print(mobil)

# # in = untuk mengecek apakah element tertentu ada di dalam sebuah list
# print('Toyota' in mobil)
# print('Porsche' in mobil)
# print(mobil[4] in mobil)
# #     'Toyota' in mobil

# TUPLE
# angka = (1,2,3,4,5,6,7,2,2)

# print(type(angka))

# # count = menghitung element tertentu
# print(angka.count(2))

# # angka.append(9) #error
# # angka.pop() #error
# # angka.extend([1]) #error
# # angka.reverse() #error
# print(angka[3])

# kartu_kredit = [(121213123123123, 606), (1421433333333312, 412)]
# huruf = ('a', 'b', 'c', 'c', 'd')
# print(huruf.count('c'))
# kata = 'python forever'
# print(kata.count('o'))

# angka_list = list(angka)
# print(angka_list)
# back_to_tuple = tuple(angka_list)
# print(back_to_tuple)

# SET

z = {1,2,3,1,2,3,4,4,4,4,4}
print(type(z))
z2 = {}
print(type(z2))

print(z)
z_list = list(z)
print(z_list)

# add = menambah element baru
z.add(5)
print(z)
z.add('Budi')
print(z)

# update = menambah beberapa element sekaligus
# harus memasukkan datanya dalam bentuk itterable (list, tuple, set, string(kalau string akan dipecah))
z.update([5,6,7,8])
z.update(('Andy', 'Caca'))
print(z)

# print(z[1:])

z.update('Andy')
print(z)

# discard = menghapus 1 element tertentu
z.discard('Budi')
print(z)
# z.discard(['A', 'n', 'd', 'y']) # error
# print(z)

# pop = meremove 1 element tertentu
# pop random
z.pop()
print('pop pertama', z)
z.pop()
print('pop kedua', z)
z.pop()
print('pop ketiga', z)
z.pop()
print('pop keempat', z)

# clear = menghapus semua element di dalam set
z.clear()
print(z)

rand_tuple = (1,3,5,6,7,8,9)
print(rand_tuple)
rand_list = list(rand_tuple) # (1,3,5,6,7,8,9) => [1,3,5,6,7,8,9] 
print(rand_list)
rand_list.append(10)
print(rand_list)
back_tuple = tuple(rand_list) # [1,3,5,6,7,8,9,10] => (1,3,5,6,7,8,9,10)
print(back_tuple) 
rand_set = set(back_tuple)
print(rand_set)

a = list('abcdeaaaaaaa')
b = list('bcfga')

c = ['Halo', 'Apa', 'Kabar']
d = '-'.join(c)
print(d)

print(a,b)

a_set = set(a)
b_set = set(b)

print(a_set, b_set)

print('irisan atau intersection dari set_a dan set_b: ', a_set.intersection(b_set))
print('irisan atau intersection dari set_a dan set_b (&): ', a_set&b_set)

print('selisih atau diference dari set_a dan set_b: ', a_set.difference(b_set))
print('selisih atau diference dari set_b dan set_a: ', b_set.difference(a_set))
print('selisih atau diference dari set_b dan set_a (-): ', b_set-a_set)

print('gabungan atau union dari set_a dan set_b: ', a_set.union(b_set))
print('gabungan atau union dari set_a dan set_b (|): ', a_set|b_set)

print('beda setangkup atau symmetric difference dari set_a dan set_b: ', a_set.symmetric_difference(b_set))

'''
Buat lah set:
p = 1,2,4,7,9,19
q = 5,12,16,17,7,9,19,6
r = 19,6,3,8

1. tentukan gabungan P dengan Q
2. tentukan gabungan P dengan R
3. tentukan gabungan Q dengan R
4. tentukan irisan dari gabungan P dengan Q dan gabungan Q dengan R
5. tentukan symmetric difference dari gabungan Q dengan R dan gabungan P dengan Q

'''

p = {1,2,4,7,9,19}
q = {5,12,16,17,7,9,19,6}
r = {19,6,3,8}

p_q = p|q
p_r = p|r
q_r = q|r

print(p_q)
print(p_r)
print(q_r)
print(p_q&q_r)
print(q_r.symmetric_difference(p_q))
mobil = ['Toyota', 'Honda', 'Mercedes']

print(type(mobil))
print(mobil)

# #indexing
print(mobil[0])
print(mobil[2])

# #SLICING
# print(mobil[0:2]) # hasil ['Toyota','Honda']
# print(mobil[1:6]) # hasil ['Honda','Mercedes']
# print(mobil[::-1]) # hasil ['Mercedes','Honda','Toyota']
# print('coba2',mobil[3:]) #hasilnya [] karena 3 gak ada. cuman 0 1 2

# # #APPEND -> menambah 1 element di posisi paling belakang
# mobil.append('BMW')
# print(mobil) #hasilnya ['Mercedes','Honda','Toyota','BMW']
# mobil.append('Mercedes') # bisa dobel gapapa.
# print(mobil)#hasilnya ['Mercedes','Honda','Toyota','BMW','Mercedes']

# # POP --> memindahkan 1 elemen di posisi paling belakang ke value hasil pop.
# # cuman bisa 1 kali aja. Kalau di pop lagi, yang pertama di pop bakal ilang.
# Hasil_pop = mobil.pop()
# Hasil_pop = mobil.pop()
# print(mobil)
# print(Hasil_pop)

# #INDEX = mengetahui index dari sebuah element
# print('Index dari mobil Toyota:',mobil.index('Toyota'))
# print('Index dari mobil Merecedes :',mobil.index('Mercedes'))

# #index dari huruf 'y' di toyota.
# print('Index dari angka y di Toyota',mobil[0].index('y'))
# #atau
# print(mobil[mobil.index('Mercedes')].index('c'))

#COPY = membuat copy dari list
# mobil_copy = mobil.copy()
# print(mobil)
# print(mobil_copy)

# # #copy : antara parents dan children sudah tidak ada hubungan. Kalau di pop tidak ke pop yang lainnya.
# mobil_copy.pop()
# print(mobil)
# print(mobil_copy)

# #kalau = : antara parents dan children masih berhubungan. Kalau di pop ke pop 22nya
# mobil2 = mobil
# print(mobil)
# print(mobil2)

# mobil2.pop()
# print(mobil)
# print(mobil2)
        #   0  1        2
# listTest = [1,'hi',['Hello',1,{2}]]
# print(listTest)
# print(listTest[2:3]) #cumanyang terakhir
# print(listTest[0]) #1
# print(listTest[1]) # hi
# print(listTest[2]) # yang panjang
# print(listTest.index('hi')) #1
# print(listTest.index(1)) #0

# x = [0, 1.5, 243, 1341,4,43, 34, 1,343,1049]
# print(x)
# x.sort()
# print(x)

# campur = [1, 'Surabaya', 2, 'Adidas',True, False, [4,5,6]]
# # print(campur)
# # print(type(campur))

# #INSERT = memasukkan element di index tertentu
mobil.insert(0,'Hammer')
print(mobil)

mobil.insert(10,'Citroen')
print(mobil)

mobil.insert(2,'Jaguar')
print(mobil)

# #SORT = mengurutkan (reverse = True / False)

mobil.sort(reverse=True) #descending
print(mobil) 

mobil.sort(reverse=False) #ascending
print(mobil)

# #REVERSE = membalik urutan dari listn

mobil.reverse()
print(mobil)

a = [4,3,2,5,6,7]
a.reverse()
print( a )

# COUNT = menghitung ada berapa element tertentu dalam sebuah list
print(mobil.count('Toyota'))
mobil.append('Toyota')
print(mobil.count('Toyota'))

# EXTEND = memasukka beberapa element sekaligus
mobil.append(['Ferrari','Honda','Toyota'])
print(f'append{mobil}')
mobil.extend(['Ferrari','Honda','Toyota'])
print(mobil)
# mobil.extend('Ferrari')
# print(mobil)
# mobil.pop()
# print(mobil)

# #mau ngambil o dari HOnda yang di dalam list
print(mobil[4][1]) # [elemen1][elemen2][elemen3]
print(mobil[4][1][1])

# mobil[4] = 'Ferrari, Honda'
# print(mobil)

mobil[4][2] = 'Porsche'
print(mobil)
mobil[4][2] = 'Porzche'
print(mobil)

# #BROADCASTING
mobil[0:3] = 'Porsche','Ford','Toyota'
print(mobil)

mobil[0], mobil[3],mobil[4]='Ford','Totota','BMW'
print(mobil)

mobil[0:3] = ['Mercedes']
print(mobil)

#IN = untuk mengecek apakah elemen tertentu ada di dalam sebuah list

print('Toyota' in mobil)
print('Ford' in mobil)

#TUPLE = mirip seperti list, tapi immutable

angka = (1,2,6,4,5,6,7,2,2)
print(type(angka))

# #COUNT = menghitung element tertentu
print(angka.count(2))

angka.append(9) #error karena tuple itu immutable
angka.pop #error karena tuple itu immutable
angka.extend([1]) #error
angka.reverse() #error
print(angka)
print(angka[3])
angka_list = list(angka) # bisa dibikin list, diedit, baru kalo dah fix dibikin tuple lagi.
print(angka_list)

kartu_kredit = ([234343934, 959]), (['aa3434311', 343])
print(kartu_kredit)
print(kartu_kredit[1][0].count('a'))

#SET 

z = {1,2,3,1,2,3,4,4,4,4,4} # yang di print hanya unique element
print(type(z))

z2 = {}
print(type(z2))

# print(z)

z_list = list(z)
print(z_list)

# #ADD = menambah elemen baru
z.add(5)
z.add('Andy')
print(z)

# #UPDATE = menambah beberapa element sekaligus
#harus memasukkan data dalam bentuk iterable (list, tuple,set)
z.update([5,6,7,8])
z.update('Andy') #SET Tidak peduli urutan jik amenggunakan update
print(z)

#DISCARD = menghapus 1 elemen tertentu
z.discard('Andy')
print(z)
#z.discard('A','n','d','y') error. harus 1 1
#print(z)

# #POP = meremove 1 element tertentu lagi
z.pop()
print('pop pertama',z)
z.pop()
print('pop kedua',z)
z.pop()
print('pop ketiga',z)
z.pop()
print('pop keempat',z)

#CLEAR = menghapus semua elemen di dalam list
z.clear()
print(z)


#LATIHAN DIAGRAM VENN

a = list('abcdeaaaaaaa')
b = list('bcfga')
print(a,b)

a_set = set(a)
b_set = set(b)

print(a_set,b_set)
#IRISAN(&)
print('irisan atau intersection dari set_a dan set_b :',a_set.intersection(b_set))
#atau
print('irisan atau intersection dari set_a dan set_b :',a_set&b_set)

#SELISIH(-)
print('selisih atau difference dari set_a dan set_b :',a_set.difference(b_set))
print('selisih atau difference dari set_b dan set_a :',b_set.difference(a_set))
#atau
print('selisih atau difference dari set_b dan set_a :',b_set-a_set)

#UNION (|)
print('gabungan atau union dari set_a dan set_b :', a_set.union(b_set))
#atau
print('gabungan atau union dari set_a dan set_b :', a_set|b_set)

#SYMMETRIC DIFFERENCE (tidak ada symbol)
print('beda setangkup atau symmetric difference dari set_a dan set_b :', a_set.symmetric_difference(b_set))
# JOIN
# c = ['Halo', 'Apa','Kabar']
# d = ' '.join(c)
# print(d)


'''
EXERCISE
Buatlah set :
p = 1,2,4,7,9,19
q = 5,12,16,17,7,9,19,6
r = 19,6,3,8

1. tentukan gabungan P dengan Q
2. tentukan gabungan P dengan R
3. tentukan gabungan Q dengan R
4. tentukan irisan dari gabungan P dengan q dan gabungan Q dengan R
5. tentukan symmetric difference dari gabungan Q dengan R dan gabungan P dengan Q
'''

p = {1,2,4,7,9,19}
q = {5,12,16,17,7,9,19,6}
r = {19,6,3,8}

print('1. Gabungan P dengan Q adalah ', p|q)
print('2. Gabungan P dengan R adalah ', p|r)
print('3. Gabungan Q dengan R adalah ', q|r)
print('4. Irisan dari gabungan P dengan Q dan gabungan dari Q dengan R adalah',(p|q)&(q|r))
print('5. Symmetric difference dari gabungan Q dengan R dan gabungan dari P dan Q adalah',(q|r).symmetric_difference(p|q))
## LAMBDA ##

def perkalian(a, b):
    print(a*b)

perkalian(2,3)

x = lambda a, b: a*b
print(x(2,3))

y = lambda a,b,c: (a/b)*c
print(y(1,2,3))

z = lambda a: 'Genap' if a%2==0 else 'Ganjil'
print(z(4))
print(z(3))

def penjumlahan(a, b):
    y = lambda a, b: a+b
    return y(a,b)

print(penjumlahan(1,2))

## MAP ##
name_list = 'Andi Budi Caca'.split()

def function(a):
    return f'halo {a}'

len_list = list(map(function, name_list))
print(len_list)

len_list2 = list(map(lambda a: len(a), name_list))
print(len_list2)

list_1 = 'cokelat melon nangka'.split()
list_2 = [10000, 5000, 20000]
couple_list = list(map(lambda a, b: a + str(b), list_1, list_2))
print(couple_list)

## FILTER ##
h = range(11) # [0,1,2,3,4,5,6,7,8,9,10]
def kurang_lima(x):
    if x < 5:
        return True
    else:
        return False

j = list(filter(kurang_lima, h))

print(j)
print(list(h))

k = [1,2,3,4,5]
l = [1,2,6,7,8]

m = list(filter(lambda a: a in k, l))
print(m)

## EXERCISE ##
'''
Pakai map dan lambda
input = [2,4,6,8]
output = [4,16,36,64]
'''

'''
quiz poin 1
words_list = ['merdeka', 'hello', 'sohib', 'kari ayam', 'pesawat', 'mobil', 'loker', 'kamar', 'saya', 'motor', 'pertamax', 'merah']
what do you want to search: 'me'
output = ['merdeka', 'merah']
what do you want to search: 'ri'
output = ['kari ayam']
what do you want to search: 'tw'
output = []
'''

## REDUCE ##
from functools import reduce

numbers = [6,2,3,4,5]
numbers_sum = reduce(lambda a,b: a*b, numbers)
print(numbers_sum)

kata = ['ini', 'ibu', 'budi']
o = reduce(lambda a,b: a+b, kata)
print(o)

'''
Quiz
input = [1-100]

output = 5100

[1,2,3,4]
[2,4]
[4,8]
12
rules = bilangannya genap semua, dikalikan 2, baru dijumlah semua.
clue = pakai reduce, filter dan map.
challenge = kalo bisa cuman 1 line. # poin 3
kalo lebih dari 1 line, poinnya 2 
'''






# word=['merdeka', 'hello', 'sohib', 'kari ayam', 'pesawat', 'mobil', 'loker', 'kamar', 'saya', 'motor', 'pertamax', 'merah']

# cari=str(input('Masukan huruf Anda: '))
# hasil = filter(lambda a: cari in a, word)
# print(list(hasil))

word = ['merdeka', 'hello', 'sohib', 'kari ayam', 'pesawat', 'mobil', 'loker', 'kamar', 'saya', 'motor', 'pertamax', 'merah']
cari = str(input('what do you want to search :'))
hasil = filter(lambda a: cari in a,word)
print(list(hasil))
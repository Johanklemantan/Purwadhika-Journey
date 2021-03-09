#f(x) = 2x + 3
#f(3) = 2(3) + 3
#f(3) = 9

#function hello world
# def hello():
#     print("Hello World!")

# hello()

# # function pangkat 2
# def power():
#     print(3**2)

# power()

# #cara 1
# def power2(x):
#     print(x**2)

# power2(5)

# #pake return
# def power2(x):
#     print('Print dari dalam function',(x**5))
#     return x**3
# hasil = power2(5)
# print('Hasil Print dari luar function', hasil)

# #FUNCTION 2 PARAMETER
# def power3(angka, pangkat):
#     return angka ** pangkat

# hasil_power3 = power3(5,5)
# print('hasil pangkat adalah',hasil_power3)


#QUIZ

#INI YANG MASIH ERROR
# def kalkulator(par1,par2,par3):
#     if par2 == '+':
#         print('Hasil pertambahan dari',par1,'dan',par3,'adalah',par1+par3)
#         return par1+par3
#     elif par2 == '-':
#         print('Hasil pengurangan dari',par1,'dan',par3,'adalah',par1-par3)
#         return par1-par3
#     elif par2 == 'x':
#         print('Hasil perkalian dari',par1,'dan',par3,'adalah',par1*par3)
#         return par1*par3
#     elif par2 =='/':
#         print('Hasil pembagian dari',par1,'dan',par3,'adalah',par1/par3)
#         return f'halo saya dari return {par1/par3}'
#     elif par2 == '**':
#         print('Hasil pangkat dari',par1,'dan',par3,'adalah',par1**par3)
#         return par1**par3
#     else :
#         print('Operator not Found')
    
# hasil_kalkulator = kalkulator(6,'/',85)

# print(hasil_kalkulator)

# JAWABAN
# def calculator(x1,op,x2):
#     if (x1.isnumeric()==True) and (op.isascii()==True) and (x2.isnumeric()==True):
#     # x1 = 3 #inside input
#     # op = 'x'
#     # x2 = 4
#         if op == '+':
#             print(f'Hasil penjumlahan dari {x1} {op} {x2} adalah {x1 + x2}')
#         elif op == '-':
#             print(f'Hasil pengurangan dari {x1} {op} {x2} adalah {x1 - x2}')
#         elif op == 'x':
#             print(f'Hasil perkalian dari {x1} {op} {x2} adalah {x1 * x2}')
#         elif op == '/':
#             print(f'Hasil pembagian dari {x1} {op} {x2} adalah {x1 / x2}')
#         elif op == '**':
#             print(f'Hasil pemangkatan dari {x1} {op} {x2} adalah {x1 ** x2}')
#         else:
#             print(f'Operator {op} tidak ditemukan')
#     else :
#         print('Salah input')
# calculator((int(input('Masukkan angka 1 :'))),(input('Masukkan operator matematika :')),int(input('Masukkan angka 2 :')))

#FUNGSI RETURN = untuk pake variabelnya dibawah nanti

# def all_in_calculator(angka1, angka2):
#     penjumlahan = angka1+angka2
#     pengurangan = angka1-angka2
#     perkalian = angka1*angka2
#     pembagian = angka1/angka2
#     pangkat = angka1**angka2

#     print(f'penjumlahan {penjumlahan}, pengurangan {pengurangan},perkalian {perkalian},pembagian {pembagian},pangkat {pangkat}')
#     return penjumlahan, pengurangan, perkalian, pembagian, pangkat

# hasil_tambah, hasil_kurang, hasil_kali, hasil_bagi, hasil_pangkat = all_in_calculator(2,3)

# print(hasil_tambah)
# print(hasil_kurang)
# print(hasil_kali)
# print(hasil_bagi)
# print(hasil_pangkat)


#LATIHAN ISENG2
# def calc (a,b,c):
#     #              5, int True == True
#     if (isinstance(a, int)==True) and (isinstance(b, str)==True) and (isinstance(c, int)==True):
#         a=int(a)
#         c=int(c)
#         if b == '+':
#             print('Hasil pertambahan dari',a,'dan ',c,'adalah :', a+c)
#         elif b == '-':
#             print('Hasil pengurangan dari',a,'dan ',c,'adalah :', a-c)
#         elif b == 'x':
#             print('Hasil perkalian dari',a,'dan ',c,'adalah :', a*c)
#         elif b == '/':
#             print('Hasil pembagian dari',a,'dan ',c,'adalah :', a/c)
#         elif b == '^':
#             print('Hasil pemangkatan dari',a,'dan ',c,'adalah :', a**c)
#         else:
#             print(f'Operator {b} bukan termasuk operasi matematika')
#     else :
#         print('Invalid input')

# calc(5,'+',3)
# #ISINSTANCE
# print(isinstance(4, list))
    

# a = input('angka pertama :') #angka pertama

# b = input('operasi amtematika :') #metode operasi

# c = input('angka kedua :') #angka kedua

# def calc (a,b,c):
#     if (a.isnumeric()==True) and (b.isascii()==True) and (c.isnumeric()==True):
#         a=int(a)
#         c=int(c)
#         if b == '+':
#             print('Hasil pertambahan dari',a,'dan ',c,'adalah :', a+c)
#         elif b == '-':
#             print('Hasil pengurangan dari',a,'dan ',c,'adalah :', a-c)
#         elif b == 'x':
#             print('Hasil perkalian dari',a,'dan ',c,'adalah :', a*c)
#         elif b == '/':
#             print('Hasil pembagian dari',a,'dan ',c,'adalah :', a/c)
#         elif b == '^':
#             print('Hasil pemangkatan dari',a,'dan ',c,'adalah :', a**c)
#         else:
#             print(f'Operator{b} bukan termasuk operasi matematika')
#     else :
#         print('Invalid input')

# calc(a,b,c)
# print('12a'.isalnum())


#PR Pak Ridho

#ada fungsi2 diatasnya yang kalo di run hasilnya hello

# def beta ():
#     return 'h e l l o'.split()
# beta = {
#     '' : 'hello'
# }

# #test=[1, 'c']

# print(beta)
# beta()['hello'][2]()()[1][2]['test']()


# def beta(x):
#     print('hello')
# x = "())['hello'][2]()()[1][2]['test']()"
# beta()['hello'][2]()()[1][2]['test']()

# def a(x):
#     print(f'Hasil {x} dikali 10 adalah {x*10} ')
#     return  x*10

# a(2)

#GAGAL

# def beta(x):
#     x = "())['hello'][2]()()[1][2]['test']()"
#     print('hello')
#     return  'Hello'

# beta("()['hello'][2]()()[1][2]['test']()")

# def apapun():
#     return 1

# a_list = [apapun, 'a', 'c']
# print(a_list[0]())
# 
def a():
    print('hello')
def b():
    return[1,[1,3,{'test' : a}]]
def c():
    return b
def beta():
    return{'hello':[1,1,c]}
beta()['hello'][2]()()[1][2]['test']()

# beta()['hello'][2]()()[1][2]['test']()

# print(a)
# print(type(a))
# print(b)
# print(type(b))
# print(c)
# print(type(c))
# print(beta)



#ORAK DONG
# b = input('Masukkan :')

# def process_1(b):
#     c = b.split("beta()")[1]
#     print(c)

#     def process_2(c):
#         d = c.split("[")[1]
#         print(d)

#         def process_3(d):
#             e = d.split("]"[0])
#             print(e)

#             def process_4(e):
#                 f = e.replace("'","")
#                 print(f)

#             process_4(e)
#         process_3(d)
#     process_2(c)
# process_1(b)
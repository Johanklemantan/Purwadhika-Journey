# While Loops & For Loops
# Hanya akan menjalankan code ketika kondisinya True

# print(1*2)
# print(2*2)
# print(3*2)
# print(4*2)
# print(5*2)
# print(6*2)
# print(7*2)
# print(8*2)
# print(9*2)
# print(10*2)


# While Loops
# i = 1 
# while i <=10:  
#     print(i*2)
#     i += 1
    
i = 1 
while i <10: # 10<=10 True
    i += 1 # 2 => 11
    if i <= 5: # 6<=5 False
        print(i*2)
    else:
        print(i*3)

# i = 1 
# while i <=10:
#     i += 1
#     if i <= 5: 
#         print(i*2)
#     else:# 6 
#         continue

''' 
Menggunakan while loop buatlah program sederhana,
ketika bertemu dengan angka ganjil, maka print angkanya.
ketika bertemu dengan angka genap, maka print "GENAP"
1-20
'''

# i = 1
# while i <= 20:
#     if i%2 == 0:
#         print('Genap')
#     else:
#         print(i)
#     i += 1

'''
Quiz Password Attempt Poin 2

No. 1
password = '12345'

case 1:
input = 23452
'Password Incorrect'
input = 23423
'Password Incorrect'
input = 23423
'Password Incorrect'
input = 23423
'Try again later'

case 2:
input 12345
'Password Correct'

case 3:
input = 23452
'Password Incorrect'
input = 23423
'Password Incorrect'
input = 12345
'Password Correct'
'''

# password = '12345'
# attempt = 1
# while attempt <= 4: # 5 => False
#     input_password = input('Masukkan Password: ')
#     if input_password == password:
#         print('Password Correct')
#         break
#     else:
#         if attempt == 4:
#             print('Try Again Later!')
#             break
#         else:
#             if attempt == 3:
#                 print(f'Password Incorrect! You have {4-attempt} attempt left!')
#             else:
#                 print(f'Password Incorrect! You have {4-attempt} attempts left!')
#             attempt +=1

'''
No. 2 poin 1
function untuk mengganti semua huruf vokal, dengan huruf "o"
input = ridho apa kabar
output = rodho opo kobor
replace_o
'''
# def replace_o(kalimat):
#     kalimat = kalimat.replace('a', 'o')
#     kalimat = kalimat.replace('i', 'o')
#     kalimat = kalimat.replace('u', 'o')
#     kalimat = kalimat.replace('e', 'o')
#     return kalimat

# print(replace_o('halo apa kabar kamu di sana'))

'''
No. 3
Factorial
input = 5
return 120
input = 10
return 3,628,800
input = 1
return 1
input = 0
return 1
input < 0
return 'must be positive digit'
# '''
# def factorial(n): # n = 5
#     if n == 0: # 5 == 0 False
#         return 1
#     elif n == 1: # 5 == 1 False
#         return 1
#     elif n < 0: # 5 < 0 False
#         return 'must be positive digit'
#     else:
#         result = 1 # 5 // 20 // 60 // 120
#         i = n # 5 // 4 // 3 // 2 // 1
#         while i != 1: # 5 != 1 True // 4 != 1 True // 3 != 1 True // 2 != 1 True // i != 1 False
#             result *= i # 1*5=5 // 5*4=20 // 20*3=60 // 60*2=120
#             i -= 1 #5-1=4 // 4-1=3 // 3-1=2 // 2-1=1
#         return result

# d = 5
# # print(factorial(d))

# def zzz(n): # n = 5 // n = 4 // n = 3 // n = 2 // n = 1
#     if n == 0: # 5 == 0 False // 4 == 0 False // 3 == 0 False // 2 == 0 False // 1 == 0 False 
#         return 1
#     elif n == 1: # 5 == 1 False // 4 == 1 False // 3 == 1 False // 2 == 1 False // 1 == 1 True
#         return 1
#     elif n < 0: # 5 < 0 False // 4 < 0 False // 3 < 0 False // 2 < 0 False
#         return 'must be positive digit'
#     else:
#         return n*zzz(n-1) # 5 * 24 = 120
# print(zzz(d))

## FOR Loops ##
# i = 1
# while i <= 10:
#     print(i*2)
#     i+=1

# for i in range(1,11):
#     print(i*2)

# for i in range(1,11):
#     if i == 5:
#         break
#     else:
#         print(i*2)

# for i in range(1,11):
#     if i == 5:
#         continue
#     else:
#         print(i*2)

# for i in range(6): # 0,1,2,3,4,5
#     print('*')

# for i in list(range(1,5)):
#     print(i)

# a_list = ['Budi', 'Andi', 'Candi', 'Dedi', 'Edi']
# for i in a_list:
#     print(f'Halo nama saya {i}!')

# a_list = ['Budi', 'Andi', 'Candi', 'Dedi', 'Edi']
# b_list = ['Kapiten', 'Data Scientist', 'Tour Guide', 'Montir', 'Reparasi AC']
# for i in range(len(a_list)): # range(5) => 0,1,2,3,4
#     print(f'Halo nama saya {a_list[i]}! Pekerjaan Saya adalah {b_list[i]}')

# a_list = ['Budi', 'Andi', 'Candi', 'Dedi', 'Edi']
# b_list = ['Kapiten', 'Data Scientist', 'Tour Guide', 'Montir', 'Reparasi AC']


# for i, j in zip(b_list, a_list): #[('Budi', 'Kapiten'), ('Andi', 'Data Scientist'), ('Candi', 'Tour Guide')]
#     print(f'Halo nama saya {i}! Pekerjaan Saya adalah {j}')
# while loops & foor loops
# hanya akan menjalankan code ketika kondisinya True.

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

#WHILE LOOPS

# i = 1
# while i <=10:
#     print (i*2)
#     i += 1

# i = 1
# while i <=10:
#     i += 1
#     if i <=5 :
#         print(i*2)
#     else :
#         print(i*3)

#BREAK AND CONTInue
# i = 1
# while i <=10:
#     i += 1
#     if i <=5 :
#         print(i*2)
#     else :
#         break
#EXERCISE

# angka = 1
# while angka <= 20:
#     if angka%2 == 0:
#         print ('GENAP')
#     else:
#         print (angka)
#     angka += 1

'''QUIZ
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
# i = 1
# while i <= 4:
#     enter = int(input('Enter the password:'))
#     if enter != password and i<=3:
#         print ('Password Incorrect')
#     elif enter != password and i == 4:
#         print('Try again later')
#     elif enter == password :
#         print('password correct')
#         break
#     i += 1

#PAK RIDHO
# password = '12345'
# attempt = 1
# while attempt <=4:
#     input_password = input('Masukkan password :')
#     if input_password == password:
#         print('Password Bener')
#         break
#     else:
#         if attempt == 4:
#             print('Try again later')
#             break
#         else:
#             if attempt ==3 :
#                 print(f'Password Incorrect! Yoh have {4-attempt} attempt left!')
#             else :
#                 print(f'Password Incorrect! Yoh have {4-attempt} attempts left!')
#             attempt+=1








#CARA PAK RIDHO
# def a(kata):
#     kata = kata.replace('a','o')
#     kata = kata.replace('e','o')
#     kata = kata.replace('i','o')   
#     kata = kata.replace('u','o')
#     return  kata
# print(a('kok tidak bisa ya'))

#CARA AZKA
# vokal = ['a', 'i', 'u', 'e', 'o']
# kalimat = input('Masukkan kalimat: ')
# kalimat2 = ''
# for i in kalimat:
#     if i in vokal:
#         huruf = 'o'
#     else: huruf = i
#     kalimat2 += huruf
# print(kalimat2)





#yosi
# def factorial(n):
#     result = 1

#     if n < 0 :
#         return 'Must be positive int'
#     else:
#         i = 1
#         while i <= n:
#             result *= i
#             i += 1
#     return result

# n = int(input('Masukkan n : '))
# print(factorial(n))


# n = int(input('Masukkan angka :'))
# def factorial(n):

#     result = 1
#     if n<0:
#         return 'Must be positive'
#     else:
#         i =1
#         while i<=n:
#             result *=1
#     return result 



#ben
# def factorial(n):
#     if n < 0:
#         print('must be positive digit')
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
# user_input = int(input('Masukkan angka'))
# print(factorial(user_input)



#PAK RIDHO
# def factorial(n):
#     if n == 0 :
#         return 1
#     elif n == 1:
#         return 1
#     elif n<0:
#         return 'must be positive digit'
#     else:
#         result = 1
#         i = n
#         while i!=1:
#             result *= i
#             i -=1
#         return result

# print(factorial(10))

#RECURSIVE
# d = 5
# # print(factorial(d))

# def rec_factorial(n):
#     if n == 0 :
#         return 1
#     elif n == 1:
#         return 1
#     elif n<0:
#         return 'must be positive digit'
#     else:
#         return n*rec_factorial(n-1)

# print(rec_factorial(d))


#FOR LOOPS
# i = 1
# while i<=10:
#     print(i*2)
#     i+=1

# for i in range (1,11): #5*2 nya di skip
#     if i == 5:
#         continue
#     else:
#         print(i*2)


# for i in range(6):
#     print('*')

# for i in list(range(1,5)):
#     print(i)

# a_list = ['Budi','Andi','Candi','Dedi','Edi']
# b_list = ['Kapiten','Data Scientist','Tour Guide','Montir','Reparasi AC']


# for i,j in zip(a_list, b_list):

#     print(f'Halo nama saya {i}! Pekerjaan saya adalah {j}.')

#game fizz buzz
#SOAL 1
'''
case 1
buat sebuah function untu game fizz buzz!
function ini menerima 1 parameter.
ketika bertemu angka yang habis dibagi 3 maka dia akan print fizz [3,6,9,12]
ketika bertemu angka yang habis dibagi 5 maka dia akan print buzz [5,10,15,20,25]
ketika bertemu angka yang habis dibagi 3 dan 5 maka dia akan print fizz buzz [15, 30, 45]

contoh:
input : fizzbuzz(15)
output :
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
'''
# def fizzbuzz(i):
#     for i in range(1,i+1):
#         if i%15==0:
#             print('fizzbuzz')
#         elif i % 3 == 0:
#             print ('fizz')
#         elif i%5 ==0 :
#             print('buzz')
#         else:
#             print (i)
           
# fizzbuzz(15)
#SOAL 2
'''
case 2
tanpa membuat function, buatlah sebuah program untuk reversing namun menggunakan for loop
input = [1,2,3,4,5,6,7]

output = [7,6,5,4,3,2,1]

'''
#CARA 1
# a = [1,2,3,4,5,6,7]
# b = a[::-1]
# print(b)

#CARA 2
# def reverse(list1):
#     reverse_list =''
#     for i in list1:
#         reverse_list = i+reverse_list
#     print('reversed list is',reverse_list)
# list1=(list(input('enter a list :')))
# reverse(list1)

#CARA 3
# a = [1,2,3,4,5,6,7]
# b = []
# i = 0
# for i in range(len(a)):
#     k = -(i+1)
#     b.append(a[k])
# print(b)



    
'''
case 3
PALINDROME
tanpa membuat function, buatlah sebuah program untuk mengecek apakah suatu kata palindrom atau bukan.
Palindrome: kondisi ketika suatu kata akan dieja sama baik dieja dari depan maupun belakang.
contoh: "malam", dibalik juga "malam"
contoh: "kodok", dibalik juga "kodok"
contoh bukan palindrome: "kotak", dibalik jadi "katok"

input = malam
output = Is word malam a palindrome = True

input = malab
output = Is word malab a palindrome = False

input = kodok
output = Is word kodok a palindrome = True
'''
#jawaban azka
# def cekkata():
#     kata = input('Masukkan kata: ').lower()
#     list2 = '' #l
#     # k = 0
#     for i in range(len(kata)): # 0
#         # k -= 1 # k = -2; k = -
#         #             -(1+1)
#         list2 += kata[-(i+1)] # list2 = lib --> libom
#     if list2 == kata:
#         print(f'{kata} is a palindrome')
#     else: print(f'{kata} is not a palindrome')

# cekkata()

# def cekkata():
#     kata = input('masukkan kata :').lower()
#     kata2 = ''
#     for i in range(len(kata)):
#         kata2+=kata[-(i+1)]
#     if kata2==kata:
#         print(f'kata {kata} merupakan polindrome')
#     else:
#         print(f'kata {kata} bukan merupakan polindrome')
# cekkata()


# kata = input('masukkan kata :').lower()
# kata_balik = kata[::-1]
# if kata == kata_balik:
#     print(f'is word {kata} merupakan polindrome == True' )
# else:
#     print(f'is word {kata} merupakan polindrome == False' )

'''
case 4:
segitiga siku(5)

case 5:
segitiga siku(7)
'''
# a =''
# n = int(input('masukkan jumlah baris: '))
# for i in range(0,n):
#     for j in range(0,i+1):
#         a += ' * '
#     a += '\n'
# print(a)

#atau cara BEN
# def segitiga_siku():
#     soal_4 = ""
#     count = 1
#     s4 = int(input('masukkan jumlah baris: '))
#     for i in range(s4):
#         soal_4 += (' * ' * count)
#         soal_4 += '\n'
#         count += 1
#     print(soal_4)
# segitiga_siku()

'''
case 6 
segitiga kebalik
'''

a = ''
n = int(input('masukkan jumlah baris : '))
for i in range(0,n):
    for j in range(0,n-i):
        a+=' * '
    a += '\n'
print(a)

#CARA RAISSA
# def b(a):
#     for i in reversed(range(0,a)):
#         for k in range(i):
#             print(' * ', end='')
#         print(' * ')
# b(10)

# def b(a):
#     for i in range(0,a):
#         for k in range(0,a-i):
#             print(' * ', end=f'{k}')
#         print(' ')
# b(9)

#CARA CEPAT GG
# def b(a):
#     for i in reversed(range(0,a)):
#         print(' * ' * (i+1))
# b(9)
# def b(a):
#     for i in (range(0,a)):
#         print(' * ' * (i+1))
# b(9)
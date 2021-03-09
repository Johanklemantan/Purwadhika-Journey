'''
a = 1
b = 2
'''
'''
# c = a
# a = b
# b = c
'''
'''
b,a = a,b # swap teknik
'''
# print (a,b)
# print(isinstance(a,int)) # validasi apakah a adalah int atau tidak
# print(issubclass) # apakah kelas tertentu inheritance dari kelas parent tertentu
'''
# int ke str ga bisa, ga ada angkanya
'''
# update nilai
# cara import
# indexing hanya me return index pertama yang di temui
# cari_huruf(x,"h") # kata, huruf
# [0,15]
# def cari_huruf(word,alphabet):
#     # index_list = []
#     alpha_lower = alphabet.lower()
#     word_lower = word.lower()
#     index_list = []
#     for i in enumerate(word_lower): ((0,"a"),(1,"b"),(2,"c"))
#         if alpha_lower == i[1]:
#             index_list.append(i[0])
#     return index_list
# print(cari_huruf(input("kata: "), input(" huruf: ")))

# x = input("kata: ")
# a = input("huruf: ")
# def cari_huruf(text, huruf):
#     list_index = []
#     for i,j in enumerate(text):
#         if j == huruf:
#             list_index.append(i)
#     return list_index
# print(cari_huruf(x,a))

# cars = ['kia', 'audi', 'bmw']
# listOfCars = []
# n = 0
# for car in cars:
#     listOfCars.append((n, car))
#     n += 1
# print(listOfCars)

# def greet(name):
#     gr = "Hello" + " " + name
#     return gr
# a = greet("Harry")
# print(a)    

# def greet(name = "stranger"):
#     gr = "Hello" + " " + name
#     return gr
# # a = greet("Harry")
# a = greet()
# print(a)    

# def factorial (n):
#     if n == 0 or n == 1:
#         return 1 
#     else:   
#         return n * factorial(n-1)
# print(factorial(4))

# square = lambda x : x*x
# print(square(6))
# sum = lambda a,b,c : a+b+c
# print(sum(1,2,3))

# l = ["apple", "mango", "banana"]
# print(" ".join(l))

# # format method => format the value inside the string into a desired output
# print ("{} is a good {}".format("Harry","boy")) # Harry is a good boy
# print ("{1} is a good {0}".format("Harry","boy")) # boy is a good Harry


'''
if else, tergantung conditional statement, kalo true bisa masuk
= assignment == apakah sama dengan
!= tidak sama dengan
rules jangan lupa antara true dengan false
'''
'''
# detik = 7259
# hour = detik // 3600
# print(hour)
# minute = detik % 3600 // 60
# if hour < 10:
#     hour = (f"0{hour}")
# if minute < 10:
#     minute = (f"0{minute}")
# print(f"{hour}:{minute}")
'''
'''
list tuple set
'''
# # print(list(range(0,10)))
# mobil = ["Toyota","Honda","Mercedes"]
# mobil1, mobil2, mobil3 = mobil[0:3]
# mobil1, mobil2, mobil3 = mobil
# # print(mobil1) # Toyota
# mobil.sort(reverse=False)
# # print(mobil)
# # mobil.extend(mobil[mobil.index(["Toyota","Honda","Mercedes"])])

# a = [1,2,3,4,5]
# print(*[1,2,3,4,5]) # 1 2 3 4 5
# print(*a) # 1 2 3 4 5
# for i in a:
#     b += " " + str(i) + " "
# print(b)
# yang bikin tuple itu karena komanya bukan karena kurungnya

# stars = ''
# for i in range(5) :
#     stars += '*'
#     stars += '\n'
# print (stars)

# stars = ''
# row = 7

# # menentukan banyaknya baris
# for i in range(row) :
#     # menentukan banyak bintang per baris
#     for j in range(row) :
#         stars += ' + '
#     stars+='\n'
# print(stars)

# # membuat segi empat
# row = 5
# x = ''
# for h in range (row) :
#     for g in range (row) :
#         x += ' * '
#     x += '\n'
# print(x)

# # segitiga terbalik
# z= ''
# # solve 1
# # for yang awal menentukan banyaknya baris
# for item in range(5) :
#         # for kedua mementukan banyaknya bintang di baris
#         for item1 in range(5-item) :
#                 z += ' * '
#         z += '\n'
# print(z)
# print('selanjutnya solve 2 \n \n solve 2')

# y = ''
# for items in range(5) :
#         for item2 in range(5-items) :
#                 y += '* '
#         y += '\n'
# print(y)

# for items in range(1,5) :
#         for item2 in range (0,items+1) :
#                 y += '* '
#         y += '\n'
# print(y)

# print('selanjutnya solve 2 cara lain \n')

# w = ''
# for items in range(9) :
#         for item2 in range(-1, abs(4-items)) :
#                 w += '* '
#         w += '\n'
# print(w)

# print('\n solve 3 \n')


# solv3 = ''
# for solve3 in range(10) :
#         for solves3 in range(9-solve3):
#                 solv3+= '  '
#         for bintang in range((2*solve3)+1):
#                 solv3+= '* '
#         solv3 += "\n"
# print(solv3)

# print('\n solve 4 \n')


# solv4 = ''
# for solve4 in range(10) :
#         for solves4 in range(solve4):
#                 solv4+= '  '
#         for bintang in range(19-(2*solve4)):
#                 solv4+= '* '
#         solv4 += "\n"
# print(solv4)

# print('\n solve 5 \n')

# solv3 = ''
# for solve3 in range(5) :
#         for solves3 in range(4-solve3):
#                 solv3+= '  '
#         for bintang in range((2*solve3)+1):
#                 solv3+= '* '
#         solv3 += "\n"
#         enter = 4- solve3
#         if enter>0 :
#                  solv3 +='\n'
# print(solv3)

# solv4 = ''
# for solve4 in range(5) :
#         for solves4 in range(solve4):
#                 solv4+= '  '
#         for bintang in range(9-(2*solve4)):
#                 solv4+= '* '
#         solv4 += "\n"
#         enter = 9-solve4
#         if enter>0 :
#                 solv4 += '\n'
# print(solv4)

# print (list(range(5, 0, -1)))
# print (list(range(5, 1, -1)))
# print (list(range(5, 2, -1)))
# print (list(range(5, 3, -1)))
# print (list(range(5, 4, -1)))

# stars = ''
# # banyaknya baris
# # 0, 1, 2 ,3 ,4
# for i in range(5):
#     # banyaknya bintang per baris
#     # [5, 4, 3, 2, 1 ]
#     for j in range (5, i, -1):
#         stars += ' * '
#     stars += '\n'
# print(stars)

# Ganjil = 1
# while Ganjil <= 10 :
#     print(f'Ganjil : {Ganjil}')
#     Ganjil +=2
# Genap = 0
# while Genap <= 10 :
#     print(f'Genap : {Genap}')
#     Genap +=2


# k = 1 
# for k in range (0, 9 ,2) :
#     print (f'genap :{k}') 
# for k in range (1, 10, 2):
#     print (f'ganjil : {k}')
# # genap = list(range(0,11,2))
# # print(genap)
# # for ganjil in range(1,11,2):
# #     print(ganjil)

# word = input('masukkan kata : ') # william => illiamway
# vokal = ['a', 'i', 'u', 'e', 'o']

# def changeWord(text) :
#     if text[0] in vokal:
#         text = text +'ay'
#     else :
#         text = text[1:] + text[0] + 'ay'
#     return text

# res = changeWord(word)
# print(res)

'''
dalam function, return simpan ke dalam variabel tertentu
'''

# sente = input ('kalimat yang ingin di reverse : ')
# def sentRev (word) :
#     wSplit = word.split(' ')
#     wRev = reversed(wSplit)
#     word = ' '.join(wRev)
#     return word


# print(sentRev(sente))

# # has 99

# # cara sulit 
# def has99(lis):
#     idx = lis.index(9)
#     if lis[idx + 1] == 9:
#         return True
#     else :
#         return False
# # cara mudah
# def has99(lis):
#     idx = lis.index(9)
#     return lis[idx + 1] == 9

# print(has99([1, 9, 9]))
# print(has99([5, 9, 2, 9]))
# print(has99([9, 3, 9]))
# print(has99([7, 9, 9, 6]))

# # misahin mengenai genap dan ganjil
# def angka() :
#     listInput = [1,2,3,4,5,6,7]
#     newlist=[[],[]]
#     for num in listInput:
#         numCtrl=num%2
#         if numCtrl==0:
#             newlist[0].append(num) #genap
#         else:
#             newlist[1].append(num) #ganjil
#     print(newlist)
# angka()

# print(3*'7') # print string sebanyak 3 kali
'''
# fruits = ['Apel', 'Anggur', 'Jeruk']
# stock = [5, 7, 8]
# price = [1000, 15000, 20000]
# qty = [0 , 0, 0]

# # # input dari user diubah ke integer
# # mainOpt = int(input(
# #     'Menu Utama \n' +
# #     '1. Menampilkan list\n' +
# #     '2. Menambahkan buah\n' +
# #     '3. Belanja\n' +
# #     'Menu pilihan :' 
# # ))

# # if mainOpt == 1:
# #     print('CreateList')
# # elif mainOpt == 2 :
# #     print('Add Fruit')
# # elif mainOpt == 3 :
# #     print('Shopping')

# # Akan loop sebanyak data buah
# #     for i in range(len(fruits)):
# #         askAgain = True
# #         while askAgain:
# #             # User akan menginput jumlah qty buah yg diinginkan
# #             qty[i] =  int(input(f'\nMasukkan jumlah {fruits[i]} : '))
# #             # Jika permintaan user melebihi stock
# #             if qty[i] > stock[i]:
# #                 print(f'Kesalahan input, stock Apel : {stock[i]}')
# #             else :
# #                 askAgain = False

# # Hitung total harga setiap buah
# totalApple = qtyApple * priceApple
# totalGrape = qtyGrape * priceGrape
# totalOrange = qtyOrange * priceOrange

# # Hitung total belanja keseluruhan
# totalPrice = totalApple + totalGrape + totalOrange

# print(
#         '\n# # # # # # # # # # # # # # # # # #\n' +
#         'Detail Belanja \n\n' +
#         f'Apel : {qtyApple} x {priceApple} = {totalApple}\n' +
#         f'Anggur : {qtyGrape} x {priceGrape} = {totalGrape}\n' +
#         f'Jeruk : {qtyOrange} x {priceOrange} = {totalOrange}\n\n' +
#         f'Total : {totalPrice}' +
#         '\n# # # # # # # # # # # # # # # # # # '
#     )

# moneyAgain = True

# while moneyAgain:
#         # User akan input uang
#         userMoney = int(input('\nMasukkan jumlah uang : '))
#         # Cari selisih uang user dengan total belanja
#         margin = userMoney - totalPrice
#         # Jika uang yang user masukkan kurang
#         if userMoney < totalPrice:
#             print(f'Uang yang Anda masukkan kurang Rp.{margin}')
#         else :
#             print(f'Terimakasih, uang kembalian Anda Rp. {margin}')
#             moneyAgain = False


# Upgrade :
# Memiliki menu utama :
# 1. Melihat list buah (name | stock | price)
# 2. Menambahkan list buah
# 3. Belanja buah
#
# Hanya boleh ada satu while dalam input qty semua buah
# Setiap selesai menambahkan buah, tampilkan list buah terbaru
'''
# # badan bintang tengahnya kosong
# # misal input = 7
# tri = int(input("tall: "))
# for i in range (tri-1,0,-1):
#         if i == 0:
#                 print( " * ")
#         # elif i == 1:
#         #         print (" *  * ")
#                 # 7     len([0,1,2,3,4,5,6]) = 7
#         # elif i+1 == len(list(range())):
#         elif i+1 == tri:
#                 print (" * "*(i+1))
#         else:
#                 print(" * "+("   "*(i-1))+" * ")
# for i in range (tri):
#         if i == 0:
#                 print( " * ")
#         # elif i == 1:
#         #         print (" *  * ")
#                 # 7     len([0,1,2,3,4,5,6]) = 7
#         # elif i+1 == len(list(range())):
#         elif i+1 == tri:
#                 print (" * "*(i+1))
#         else:
#                 print(" * "+("   "*(i-1))+" * ")

# # HOMEWORK
# # Buat duplicate function untuk map dan filter
# # def myMap(fun, lis):
# #     # do something
'''
# numList = [1, 2, 3, 4, 5]
# def times2(num) :
#     return num*2
# # Map' menerima dua argumen : function, list
# def myMap(fun, lis):
#     # List kosong untuk menyimpan hasil map
#     mapList = []
#     # Loop sebanyak data di list
#     for i in lis:
#         # Hasil return function disimpan di res
#         res = fun(i)
#         # res di input ke list
#         mapList.append(res)
    
#     # myMap akan mengeluarkan list baru 'mapList'
#     return mapList

# myMapRes = myMap(times2, numList)
# print (numList)
# print(myMapRes)

# # def myFilter(fun, lis):
# numList = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
# def even(num) :
#     return num %2 == 0

# # myFilter menerima dua argumen function dan list
# def myFilter(fun, lis):
#      # List kosong untuk menyimpan hasil filter
#      filterList = []
#      # Loop sebanyak data di list
#      for i in lis:
#          # Setiap loop akan return True / False, disimpan di 'res'
#          res = fun(i)
#          # jika 'res' berisi True, maka nilai 'i' akan dimasukkan ke 'filterList'
#          if res == True:
#              filterList.append(i)
#      # list yang berisi hasil filter, dikeluarkan dari 'myFilter'
#      return filterList
# myFilterRes = myFilter(even, numList)
# print(numList)
# print(myFilterRes)
'''
# wordList = ['Merdeka', 'Hello', 'Hellos', 'sohib', 'kari ayam']
# print(f'list = {wordList}')
# inputFilter = input('search : ')
# def srch (x) :
#     return inputFilter.lower() in x.lower()
# kaList = list(filter(srch, wordList))
# print(kaList)
'''
'''
# wordList = ['Merdeka', 'Hello', 'Hellos', 'sohib', 'kari ayam', 'Andika']
# final = []
# inputFilter = input(f'{wordList} \n search : ')

# for i in wordList :
#     #  'a' in 'merdeka'
#     # res : true / false
#     res = inputFilter.lower() in i.lower()

#     if res == True:
#         final.append(i)

# print(final)

# # KEDUA
# # Sebuah function yang dapat memisahkan nilai genap dan ganjil
# # [11, 22, 34, 41, 52, 63, 71, 86,]
# # [[22, 34, 52, 86], [11, 41, 63 ,71]]

# startList = [11, 22, 34, 41, 52, 63, 71, 86,]

# def oddEven(listNumber):
#     oddList = []
#     evenList = []
#     finalList = []

#     for i in listNumber:
#         if i % 2 == 0:
#             # input ke array genap
#             evenList.append(i)
#         else:
#             # input ke array ganjil
#             oddList.append(i)
#     # Memasukkan list genap ke dalam list penampung (index 0)
#     finalList.append(evenList)
#     # Memasukkan list ganjil ke dalam list penampung (index 1)
#     finalList.append(oddList)

#     return finalList

# result = oddEven( startList )
# print(result)

# # def digital_root(n):
# #     while n >= 10:
# #         n = sum(int(i) for i in str(n))
# #     return n

# def digital_root(n):
#     return n if n < 10 else digital_root(sum(map(int,str(n))))
# print(digital_root(399))
# print(digital_root(942))
# print(digital_root(132189))
# print(digital_root(493193))

# def friend(x):
#     ans = []
#     for i in x:
#         if len(i) == 4:
#             ans.append(i)
#     return ans

# print(friend(["Ryan", "Kieran", "Mark", ]))

# # bikin option
# while True:
#    print("Options:")
#    print("Enter 'add' to add two numbers")
#    print("Enter 'subtract' to subtract two numbers")
#    print("Enter 'multiply' to multiply two numbers")
#    print("Enter 'divide' to divide two numbers")
#    print("Enter 'quit' to end the program")
#    user_input = input(": ")

#    if user_input == "quit":
#       break
#    elif user_input == "add":
#       ...
#    elif user_input == "subtract":
#       ...
#    elif user_input == "multiply":
#       ...
#    elif user_input == "divide":
#       ...
#    else:
#       print("Unknown input")

# # menghitung bit
# def countBits(n):
#     return str(bin(n)).count('1')

# print(countBits(1234))

'''
#######################
#       No. 1         #
#######################


# def pnumber(x) :
#     res = len(x)
#     if res >9 :
#         phoneList = []
#         for num in x:
#             phoneList.append("". join(str(num)))
#         phStr = phoneList
#         print(phoneList)
#         ac = "".join(phStr[0:3])
#         prefix = "".join(phStr[3:6])
#         suffix = "".join(phStr[6:10]) 
#         print("({}) {}-{}".format(ac, prefix, suffix))
#     else :
#         print("False")
    
# pnumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# pnumber([1, 2, 3, 4, 5, 6, 7, 8, 9])



#######################
#       No. 2         #
#######################
# def kata(text) :
#     res = len(text)
#     if 1 <= res <= 20 :
#         textUpper = text.title()
#         textSplit = textUpper.split(" ")
#         textJoin = "".join(textSplit)
#         print(f"#{textJoin}")
#     else :
#         print("False")

# kata("Hello there how are you doing")
# kata("    Hello   world")
# kata("")

#######################
#       No. 3         #
#######################

def fix(a):
    list1 = []
    for item in a:
        if len(list1) == 0:
            list1.append(item)

        elif len(list1) > 0:
            if list1[-1] != item:
                list1.append(item)
    print(list1)
uniq = 'KKKKLLLMMNKKKKLLLL'
uniq1 = 'KLLMmKN'
uniq2 = [1,2,2,3,3]
fix(uniq)
fix(uniq1)
fix(uniq2)

#######################
#       No. 4         #
#######################
# number1 = int(input('Number1: '))
# if number1 < 1 or number1 > 9:
#     print("Invalid integer. The number must be in the range of 1-9.")
# number2 = int(input('Number2: '))
# if number2 < 1 or number2 > 9:
#     print("Invalid integer. The number must be in the range of 1-9.")
# number3 = int(input('Number3: '))
# if number3 < 1 or number3 > 9:
#     print("Invalid integer. The number must be in the range of 1-9.")
# number4 = int(input('Number4: '))
# if number4 < 1 or number4 > 9:
#     print("Invalid integer. The number must be in the range of 1-9.")
# number5 = int(input('Number5: '))
# if number5 < 1 or number5 > 9:
#     print("Invalid integer. The number must be in the range of 1-9.")
# number6 = int(input('Number6: '))
# if number6 < 1 or number6 > 9:
#     print("Invalid integer. The number must be in the range of 1-9.")
# number7 = int(input('Number7: '))
# if number7 < 1 or number7 > 9:
#     print("Invalid integer. The number must be in the range of 1-9.")

# allnumber = [number1, number2, number3, number4, number5, number6, number7]

# allnumbers= []
# for i in allnumber:
#     if 1 <= i <= 9 :
#         allnumbers.append(i)
# print(f"1. Angka yang diinput : {allnumbers}")
# def ascending(num):
#     num.sort()
#     print(f"2. Sort ascending : {num}")
# ascending(allnumbers)
# def descending (angk)
#     angk.sort(reverse =True)
#     print(f"3. Sort descending :{angk}")
# descending(angk)

# def genap(x):
#     newlist1=[]
#     newlist2=[]
#     for num in listInput:
#         numCtrl=num%2
#         if numCtrl==0:
#             newlist1.append(num) #genap
#         else:
#             newlist2.append(num) #ganjil
#     print(newlist1,newlist2)    

# #  no 4
# listInput = []
# listTrash = []
# listGenap = []
# listGanjil = []

# y = 1
# print('Input sampai 7 angka (kombinasi ganjil dan genap)')
# while len(listInput) <= 6:
#     ele = int(input(f'Masukkkan Element ke-{y} : '))
#     if ele <= 9:
#         listInput.append(ele)
#         y += 1
#     if ele >= 9:
#         listTrash.append(ele)

# for i in listInput:
#     if i % 2 == 0:
#         listGenap.append(i)    
#     else:
#         listGanjil.append(i)

# def average(z):
#     return sum(z)/len(z)

# avRes = average(listGanjil)

# print(f'Angka yang terinput : {listInput}')
# listInput.sort()
# print(f'Sort ascending : {listInput}')
# listInput.sort(reverse=True)
# print(f'Sort descending : {listInput}')
# print(f'Hasil jumlah angka genap : ', sum(listGenap))
# print(f'Hasil rata rata angka ganjil : {avRes}')


# Number Two
# def sum01
# Buat function yang menerima list of number
# Jumlahkan semua angka, kecuali angka yang ada diantara angka 0 - 1

# [2, 4, 0, 1, 11] -- > 17 (0, 1 tidak masuk hitungan)
# [7, 0, 3, 1, 7, 9] --> 23 (0, 3, 1 tidak masuk hitungan)
# [5, 0, 3, 2, 1] --> 5 (0, 3, 2, 1 tidak masuk hitungan)

# a = [2, 4, 0, 1, 11]
# b = [7, 0, 3, 1, 7, 9]
# c = [5, 0, 3, 2, 1]
# def sum01(lis) :
#     # temukan index angka 0 dan 1
#     # untuk index angka 1 dijumlahkan dengan angka 1 
#     zero = lis.index(0)
#     one = lis.index(1)+1
    
#     # delete data dari index angka 0 hingga index angka 1
#     del lis[zero:one]

#     result = sum(lis)

#     # print hasil jumlah dari daa lis
#     print(result)

# sum01(a)
# sum01(b)
# sum01(c)
'''

# f(x) = 2x + 3
# f(3) = 2(3) + 3
# # f(3) = 9

# # function hello world
# def hello():
#     print("Hello World!")

# hello()

# # function pangkat 2
# def power():
#     print(3**2)

# power()

# # function 1 parameter
# def power2(x):
#     # print('print dari dalam function', x**2)
#     return x**2

# print(power2(4)) # 1
# # hasil_power = power2(4)
# print('print dari luar function', power2(4))
# power2(4)

# # function 2 parameter
# def power3(angka, pangkat):
#     return angka**pangkat

# hasil_power3 = power3(3, 4)
# print(power3(3, 4))
# print('di print dari variable hasil_power3:', hasil_power3)

'''
buat sebuah kalkulator sederhana yang menerima 3 paramater / argument
par1 = angka di sebelah kiri
par2 = +, -, x, /, ^
par3 = angka di sebelah kanan

input = calculator(2, 'x', 3)
output = hasil pengalian dari 2 x 3 adalah 6

input = calculator(2, '+', 3)
output = hasil penjumlahan dari 2 + 3 adalah 5

input = calculator(2, ',' , 3)
output = 'Operator Not Found!"
CLUE: if - else
'''

# angka1 = input('angka pertama: ')
# oper = input('Operator(+,-,x,/,^): ')
# angka2 = input('angka kedua: ')

# print(angka1.isnumeric())
# print(oper.isascii())
# print(angka2.isnumeric())

def calculator(x1, op, x2):
    if (x1.isnumeric() == True) and (op.isascii() == True) and (x2.isnumeric() == True):
        x1 = int(x1)
        x2 = int(x2)
        if op == '+':
            print(f'Hasil penjumlahan dari {x1} {op} {x2} adalah {x1+x2}')
        elif op == '-':
            print(f'Hasil pengurangan dari {x1} {op} {x2} adalah {x1-x2}')
        elif op == 'x':
            print(f'Hasil pengalian dari {x1} {op} {x2} adalah {x1*x2}')
        elif op == '/':
            print(f'Hasil pembagian dari {x1} {op} {x2} adalah {x1/x2}')
        elif op == '^':
            print(f'Hasil pemangkatan dari {x1} {op} {x2} adalah {x1**x2}')
        else:
            print(f'Operator {op} tidak ditemukan')
    else:
        print('Invalid Input')

calculator('5',"x",'5')

# def all_in_calculator(angka1, angka2):
#     penjumlahan = angka1 + angka2
#     pengurangan = angka1 - angka2
#     pengalian = angka1 * angka2
#     pembagian = angka1 / angka2
#     pangkat = angka1 ** angka2
    
#     print(f'penjumlahan {penjumlahan}, pengurangan {pengurangan}, pengalian {pengalian}, pembagian {pembagian}, pangkat {pangkat}')

#     return penjumlahan, pengurangan, pengalian, pembagian, pangkat

# hasil_jumlah, hasil_kurang, hasil_kali, hasil_bagi, hasil_pangkat = all_in_calculator(4, 2)
# print('print kedua', all_in_calculator(4,2))
# print(hasil_jumlah)
# print(hasil_kurang)
# print(hasil_kali)
# print(hasil_bagi)
# print(hasil_pangkat)

# print(hasil_jumlah + 10)

# application = ['ABC for Kids١', 'asdsabdasd', 'asdas١assad', 'sada']
# english_app = []
# #   i = 'B'
# for app in application:
#     true_sum = 0 # 1 => 2 => 3 => 4 => 5 => 12
#     for i in app: # 'ABC for Kids'
#         #   (97 <= ord('A') <= 122) or (65 <= ord('A') <= 90) or (i == ' ')
#         #   (97 <= ord('B') <= 122) or (65 <= ord('B') <= 90) or (i == ' ')
#         #   (97 <= ord('C') <= 122) or (65 <= ord('C') <= 90) or (i == ' ')
#         #   (97 <= ord(' ') <= 122) or (65 <= ord(' ') <= 90) or (i == ' ')
#         #   (97 <= ord('f') <= 122) or (65 <= ord('f') <= 90) or (i == ' ')
#         #       False or False or True = True
#         if (ord('a') <= ord(i) <= ord('z')) or (ord('A') <= ord(i) <= ord('Z')) or (i==' '):
#             true_sum += 1

#     print('true_sum:', true_sum)
#     print('len apps:', len(app))
#     if true_sum == len(app):
#         english_app.append(app)

# print(english_app)


# print(ord('A'))


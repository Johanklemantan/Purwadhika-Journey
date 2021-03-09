# def encryption():
#     kata = print(str(input('Masukkan Kata :')))
#     pisah = kata.split('')
#     output = pisah[index]


a = str(input('Masukkan Kata :'))
# print(a)
# # def b(a):
#    print( [i for i in a])
# b(a)
# print()
# print(b(a))
# print(chr(25))
# ord('f')
    # for i in b:
#     c = b[i+2]
#     print(c)
# c = index[b]
# print(c)

numbers = []
letter = []
for i in a:
    if i == 'y' or i == 'z':
        number = ord(i)-120
    else:
        number = ord(i)-94
        numbers.append(number)
print('numbers:',numbers)

for j in numbers:
    if j == 28 or j == 27:
        letters = chr(j+69)
    else:
        letters = chr(j+96)
    letter.append(letters)
print(letter)
z = ''.join(letter).upper()
print('encryption:', z)

# abjad = list('abcdefgh')
# print(abjad)
'''
import random
question answer pake list
nested while
gambar pake list
'''

import random

print('***** HANGMAN *****')
q = ['Makanan pokok?','Cotton?','Sapi minum?']
a = ['nasi','kapas','air']
g = ['_____','|   |','|   o','|  /|\\','|  / \\','|____']

def indexCheck(kata,car): #cek nomor index
    indexno = []
    for i in range(len(kata)):
        a = kata[i]
        if a == car:
            indexno.append(i)
    return indexno

def updateMultiple(noIndex, kata, char): #update multiple value
    a = list(kata)
    for i in noIndex:
        a[i] = char 
    return a

def stopWhenTrue(a, jwb): #stop saat jawaban sudah benar
    if a == jwb:
        stopper = True
    else:
        stopper = False
    return stopper

def berhasilGagal(salah, stopper, nyawa): #message safe atau dead
    if stopper == True:
        print('YOU ARE SAFE')
    elif salah == nyawa and stopper == False:
        print('YOU ARE DEAD') 

def gambar(salah, gambar): #print gambar saat salah
    for i in range(salah):
        print(gambar[i])

def validasiChar(jawab, stopper, salah): #validasi hanya satu character
    if len(jawab) != 1:
        print('Please input one character only')
        salah -= 1
        # stopper = True
    return salah

# def wrongCounter(loc, salah):
#     if loc == []:
#         salah += 1
#     return salah

again = 'y'
while again == 'y':
    r = random.randint(0,len(q)-1)
    attempt = 1
    salah = 0
    stopper = False
    nyawa = 6
    print(f'{len(a[r])} huruf! {q[r]}')
    jwbBenar = ('_'*len(a[r]))
    print(f'random = {r}') #value checker
    while salah < nyawa and stopper == False:
        jwb = input(f'Attempt(s) {attempt}: ').lower()
        loc = indexCheck(a[r],jwb) #no index yang akan di-append dengan jwb
        print(f'loc = {loc}') #value checker
        if loc == []:   #trigger counter salah
            salah += 1
        jwbBenar = updateMultiple(loc, jwbBenar, jwb) #update jwbbenar dengan value jwb
        print(' '.join(jwbBenar))
        salah = validasiChar(jwb,stopper, salah) #validasi hanya satu character untuk jwb
        gambar(salah,g) #print gambar
        stopper = stopWhenTrue(a[r],''.join(jwbBenar)) #while loop berhenti ketika jawaban sudah benar
        berhasilGagal(salah, stopper, nyawa) #message safe atau dead 
        print(f'salah = {salah}') #value checker
        attempt += 1
    again = input('Do you want to play again? (y/n): ').lower()
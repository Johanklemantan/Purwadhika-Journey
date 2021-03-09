# angka = 1
# while angka<=10:
#     print(angka)
#     angka +=1

# listItem = list(range(1,11,2))
# print(listItem)

# for item in range(1,11,2):
#     print(item)

#Solve It 1
# angka = 1
# y = 'Nomor urut'
# while angka<=10:
#     print(y,angka)
#     angka+=1

# y = 'Nomor urut'
# for i in range (1,11):
#     print(y,i)

#Solve It 2
# y = 'Nomor urut'
# for i in range (0,21,2):
#     print(y,i)

#Solve It 3
# y = 'Nomor urut'
# for i in range (1,21,2):
#     print(y,i)

z = ''
for i in range(0,5):
    z += ' * '
print(z)

z = ''
for i in range(0,5):
    z += ' * \n'
print(z)

#Solve It 4
# z = ''
# for i in range (1,26):
#     if i%5==0:
#         z+=' *  \n'
#     else:
#         z+=' * '
# print(z)

#atau

# z='';
# for ii in range(5):
#     for j in range(0,5):
#         z += ' * '
#     z += '\n'
# print(z);

# z='';
# for i in range(0,5):
#     for j in range(0,i+1):
#         z += ' * '
#     z += '\n'
# print(z);
#SOlve it 1
z='';
for i in range(0,5):
    for j in range(0,5-i):
        z += ' * '
    z += '\n'
print(z);


#SOlve it 2 bener
z=""
for i in range(1,10):
    print(i)
    if i != 5:
        for j in range(1,7-i):#(1,6). (1,5). (1,4). (1,3). (1,2)
        # z+=" * "
            print(' * ', end=f"{j} ")
        for j in range(7,i+3): #(10,6)
            print(' * ',end = f'{j} ')
        print('')
    else:
        print(' * ')

#Solveit2 irin
# a=''

# j=5
# for i in range (0,j): #(0,1,2,3,4)
#     a += '\n'
#     for item in range(0,j):#(0,1,2,3,4)
#         a+=' * '
#     j-=1
# print(a)

# b=' * '

# for x in range(0,4): #(0,1,2,3)
#     b += ' * '
#     print(b)

# #Solve it! 3 ngaco
# z = ''
# for i in range (0,10):
#     z += ' * '
#     print(z,f'{i}')
    
    # solveit3 irin
 
 
# baris=int(input("Masukan jumlah baris segitiga:"))
# kolom=(baris-1)*2+1
   
# for relement in range(0,baris+1):
#     for celement in range(0,kolom):
#         if celement>=baris-relement and celement<baris+relement:
#             a+=' * '
#         else:
#             a+='   '
#     a+=''
# print(a)

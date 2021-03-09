# def pyramid(a):
#     for i in range(0,a): #0,1,2,3,4,5,6,7,8
#         if i <=a//2:
#             print(' ')
#         for j in reversed(range(a)):
#             if j == a//2:
                
#     pyramid(9)

#SETELAH REVISI DAN IKUT PAK RIDHO (dah bisa pake ganjil)
a = int(input('masukkan nomer : '))
b = 1
if a % 2!=0:
    a = a+1
else:
    a = a
for i in range (a-1,0,-2): #[9,7,5,3,1]
    print(' '*(a-i),' *'*(i))
for j in range(b+2,a,2):#[3,5,7,9]
    print(' '*(a-j),' *'*(j))
        




#PAK RIDHO PUNYA (genap doang)


# b = int(input('How tall?:')) #20
# a = 1
# for i in range(b-1,0,-2): # [19, 17, 15, 13, 11, 9, 7, 5, 3, 1] 
#     print('-'*(b-i), ' *'*(i)) #
# for ii in range(a+2,b,2): # [3, 5, 7, 9, 11, 13, 15, 17, 19] 
#     print('-'*(b-ii), ' *'*(ii))

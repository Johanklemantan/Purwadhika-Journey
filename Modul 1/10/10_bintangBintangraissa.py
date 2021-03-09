bintang_bint =int(input("Masukkan angka tersera bro : "))

if bintang_bint%2 ==0 :
    bintang = bintang_bint//2
else:
    bintang = bintang_bint//2+1

for i in reversed(range(0,bintang)):#(4,3,2,1,0)
    for k in range(0,bintang-i):
        print("  ",end="")
    for j in range(0,i*2):
        print(" *",end="")
    print(" - ")

    
# for i in range(0,bintang):
#     if i == 0 :
#         continue
#     else :
#         for k in range(0,bintang-i):
#             print("  ",end="")
#         for j in range(0,i*2):
#             print(" *",end="")
#         print(" * ")


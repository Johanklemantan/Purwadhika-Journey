
# def tickets(peopleInLine):
#     x = 0
#     for i in peopleInLine:
#         if x >=0 :  
#             if i == 25:
#                 x += 1
#             elif i ==50:
#                 x-=1
                
#             elif i ==100:
#                 x-=3
#         else:
#             print('NO')
#             break
#     # print(x)
#     if x >= 0 :
#         print('YES')
#     else:
#         print('NO')
# tickets([25,25,50,100])


def tickets(peopleInLine):
    x = 0 #jumlah uang 25
    y = 0 #jumlah uang 50
    z = 0 #jumlah uang 100
    for i in peopleInLine:
        if x <0 :  
            print('NO')
        else:
            if i == 25:
                x += 1
                print('YES')
                
            elif i ==50:
                if x>=1:
                    x-=1
                    y +=1
                    print('YES')
                else:
                    print('NO')
                    break
            elif i ==100: 
                if x>=3 and y<1:
                    x-=3
                    z +=1
                    print('YES')
                elif x >=1 and y >=1:
                    x-=1
                    y -=1
                    z +=1
                    print('YES')
                else:
                    print('NO')
                    break

                    
    # print(x)
    # print(f'sisa uang adalah {x*25}')
    print(f'pecahan 25 ada {x} lembar')
    print(f'pecahan 50 ada {y} lembar')
    print(f'pecahan 100 ada {z} lembar')
tickets([25,25,50,100,100])





#Raissa



# hrg_tiket = 25
# duit_di_kasir = {   25 : 0,
#                     50 : 0,
#                     100 : 0,
#                 }
# jml_tiket = 10
# pelanggan = 0

# def bioskop_buka():   
#     global pelanggan
#     global jml_tiket
#     while jml_tiket > 0 :
#         pelanggan += 1
#         print(f'Hello, anda pelanggan ke :{pelanggan}, harga tiket 25 USD, berapa uang yang ingin anda bayarkan?')
#         bayar_pake_duit()

# def bayar_pake_duit ():
#     duit = int(input(f'hanya menerima 25 USD, 50 USD dan 100 USD'))
#     check_total(duit)
    
# def check_total (duit):
#     global jml_tiket
#     if duit == 25:
#         duit_di_kasir[duit] += 1
#         kasir = sum(k*v for k,v in duit_di_kasir.items())
#         print('Selamat, anda mendapat tiket! Happy watching! ')
#         print('Jumlah duid Vasya sekarangg',kasir)
#         print(duit_di_kasir)
#         jml_tiket -= 1
#         print("sisa tiket yang ada",jml_tiket)
#         bioskop_buka()
#     elif duit == 50 :
#         if duit_di_kasir[25] > 0 :
#           duit_di_kasir[duit] += 1
#           duit_di_kasir[25] -= 1
#           kasir = sum(k*v for k,v in duit_di_kasir.items())
#           print('Selamat, anda mendapat tiket! Happy watching! ')
#           print('Jumlah duid Vasya sekarangg',kasir)
#           print(duit_di_kasir)
#           jml_tiket -= 1
#           bioskop_buka()
#         else :
#           print('Tidak ada kembalian, next customer please')
#     else :
#         if duit_di_kasir[25] > 0 and duit_di_kasir[50] > 0 :
#             duit_di_kasir[duit] += 1
#             duit_di_kasir[25] -= 1
#             duit_di_kasir[50] -= 1
#             kasir = sum(k*v for k,v in duit_di_kasir.items())
#             print('Selamat, anda mendapat tiket! Happy watching! ')
#             print('Jumlah duid Vasya sekarangg',kasir)
#             print(duit_di_kasir)
#             jml_tiket -= 1
#             bioskop_buka()
#         elif duit_di_kasir[25] > 2 :
#             duit_di_kasir[duit] += 1
#             duit_di_kasir[25] -= 3
#             kasir = sum(k*v for k,v in duit_di_kasir.items())
#             print('Selamat, anda mendapat tiket! Happy watching! ')
#             print('Jumlah duid Vasya sekarangg',kasir)
#             print(duit_di_kasir)
#             jml_tiket -= 1
#             bioskop_buka()
#         else :
#             print('Tidak ada kembalian, next customer please')
            
# bioskop_buka()
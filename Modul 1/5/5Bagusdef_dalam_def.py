# def hello():
#     print("hello world")

# hello()

# def power(x):
#     print(x**2)

# power(5)

#func 1 parameter
# def power2(x):
#     z = print(x**2)
#     return z

# power_5 = power2(5)

#func 2 parameter
# def power3(angka, pangkat):
#     return angka**pangkat

# tiga_pangkat_4 = power3(3,4)
# print(tiga_pangkat_4)

#kuis kalkulator

# par1 = int(input('angka pertama:'))
# par2 = input('operator (+,-,*,/,^):')
# par3 = int(input('angka kedua:'))
# y = int(input('angka pangkat:'))

def kalkulator(par1, par2, par3):
    if par2 == '+':
        print('hasil penambahan dari', par1, par2, par3, 'adalah', par1 + par3)
        return par1 + par3
    elif par2 == '-':
        print('hasil pengurangan dari', par1, par2, par3, 'adalah', par1 - par3)
        return par1 + par3
    elif par2 == 'x':
        print('hasil perkalian dari', par1, par2, par3, 'adalah', par1 * par3)
        return par1 * par3
    elif par2 == '/':
        print('hasil pembagian dari', par1, par2, par3, 'adalah', par1 / par3)
        return par1 / par3
    elif par2 == '^':
        print('hasil pemangkatan dari', par1, par2, par3, 'adalah', par1 ** par3)
        return par1**par3
    else:
        print('invalid input')

def perhitungan_kuadrat(hasil, y):
    print('pangkat dari', f'{hasil:,}', 'adalah', f'{hasil ** y:,}')
    return (hasil ** y)

# print(f'{(perhitungan_kuadrat(kalkulator(par1,par2,par3))):,}')
print(kalkulator(perhitungan_kuadrat(2, 2), '+', perhitungan_kuadrat(3, 2)))

# perhitungan = kalkulator(2, '^', 4)
# perhitungan = kalkulator(int(input('angka pertama:')), input('operator (+,-,*,/,^):'), int(input('angka kedua:')))
# print('kuadrat dari', f'{(int(perhitungan)):,}', 'adalah', f'{(int(perhitungan ** 2)):,}')








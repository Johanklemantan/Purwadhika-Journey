# nomor 1
# dicthari = {
#     'senin': 'Monday',
#     'selasa': 'Tuesday',
#     'rabu': 'Wednesday',
#     'kamis': 'Thursday',
#     'jumat': 'Friday',
#     'sabtu': 'Saturday',
#     'minggu': 'Sunday'
#     }
# hari = input('Masukkan hari: ').lower()
# print(f'Bahasa Inggris dari {hari.capitalize()} adalah {dicthari[hari]}')



# nomor 2
dicthari = {
    'senin': 'monday',
    'selasa': 'tuesday',
    'rabu': 'wednesday',
    'kamis': 'thursday',
    'jumat': 'friday',
    'sabtu': 'saturday',
    'minggu': 'sunday'
    }
hari = input('Masukkan hari (ENG/INA): ').lower()
ina = list(dicthari.keys()) # [senin, selasa, rabu, kamis, jumat, sabtu, minggu]
eng = list(dicthari.values()) # [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
if hari in ina:
    print(f'Bahasa Inggris dari {hari.capitalize()} adalah {dicthari[hari].capitalize()}')
elif hari in eng:
#                                                                 ina[4].capitalize()
    print(f'Bahasa Indonesia dari {hari.capitalize()} adalah {ina[eng.index(hari)].capitalize()}')
else: print(f'Kata yang Anda masukkan bukan nama hari.')

print(dicthari.items())

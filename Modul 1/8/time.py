# import datetime as dt

# string_date = '2020/02/18'
# tanggal = dt.datetime.strptime(string_date, '%Y/%m/%d')
# print(tanggal.date())

# print(tanggal.year)
# print(tanggal.month)
# print(tanggal.day)

# now = dt.datetime.now()
# print(now)
# print(now.day)
# print(now.month)
# print(now.strftime('%d')) #%d itu tanggal format 2 angka
# print(now.strftime('%m')) #%m itu bulan format 2 angka
# print(now.strftime('%y')) #%y itu tahun format 2 angka
# print(now.strftime('%Y')) #%Y itu tahun format 4 angka
# print(now.strftime('%A')) #%A itu nama hari
# print(now.strftime('%B')) #%B itu nama bulan
# print(now.strftime('%H')) #%H format 24 jam
# print(now.strftime('%I')) #%I format 12 jam
# print(now.strftime('%p')) #%p format AM/PM
# print(now.strftime('%M')) #%M menit
# print(now.strftime('%S')) #%S second

# import sekarang.py

# from module_sekarang import Waktu as saiki

# print(saiki.hari)
# print(saiki.tanggal)
# print(saiki.bulan)
# print(saiki.tahun)
# print(saiki.jam)
# print(saiki.menit)
# print(saiki.detik)

import datetime as dt
class Skarang:
    # def __init__(self):
    #     pass
    now = dt.datetime.now()
    def hari():
        print(now.strftime('%A'))
    def tanggal():
        print(now.strftime('%d'))
    def bulan():
        print(now.strftime('%B'))
    def tahun():
        print(now.strftime('%Y'))
    def jam():
        print(now.strftime('%H'))
    def menit():
        print(now.strftime('%M'))
    def detik():
        print(now.strftime('%S'))

saiki = Skarang()
print(saiki.hari())
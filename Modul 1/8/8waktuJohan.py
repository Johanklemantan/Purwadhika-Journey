import datetime as dt
# class Sekarang:
#     def time(self):
#         now = dt.datetime.now()
#         print(now)
#     time(self=())

#     def tahun(self):
#         now = dt.datetime.now()
#         print(now.strftime('%Y'))
#     tahun(self=())
       
#     def bulan(self):
#         now = dt.datetime.now()
#         bulan = now.strftime('%B')
#         if bulan == 'January':
#             bulan ='Januari'
#         elif bulan == 'February':
#             bulan = 'Febuari'
#         elif bulan == 'March':
#             bulan = 'Maret'
#         elif bulan == 'May':
#             bulan = 'Mei'
#         elif bulan == 'June':
#             bulan = 'Juni'
#         elif bulan == 'July':
#             bulan = 'Juli'
#         elif bulan == 'August':
#             bulan = 'Agustus'
#         elif bulan == 'October':
#             bulan = 'Oktober'
#         elif bulan == 'November':
#             bulan = 'Nopember'
#         elif bulan == 'December':
#             bulan = 'Desember'
#         print(bulan)
#     bulan(self=())
        
#     def hari(self):
#         now = dt.datetime.now()
#         hari = now.strftime('%A')
#         if hari == 'Monday':
#             hari ='Senin'
#         elif hari == 'Tuesday':
#             hari ='Selasa'
#         elif hari == 'Wednesday':
#             hari ='Rabu'
#         elif hari == 'Thursday':
#             hari ='Kamis'
#         elif hari == 'Friday':
#             hari ='Jumat'
#         elif hari == 'Saturday':
#             hari ='Sabtu'
#         elif hari == 'Sunday':
#             hari ='Minggu'
#         print(hari)
#     hari(self=())
       
#     def jam(self):
#         now = dt.datetime.now()
#         jam = now.strftime('%H')
#         print(jam)
#     jam(self=())

#     def menit(self):
#         now = dt.datetime.now()
#         menit = now.strftime('%M')
#         print(menit)
#     menit(self=())

#     def detik(self):
#         now = dt.datetime.now()
#         detik = now.strftime('%S')
#         print(detik)
#     detik(self=())
        
   
class Sekarang:
    def time(self):
        now = dt.datetime.now()
        print(now)
    time(self=())

    def tahun(self):
        now = dt.datetime.now()
        print(now.strftime('%Y'))
    tahun(self=())
       
    def bulan(self):
        now = dt.datetime.now()
        bulan = now.strftime('%B')
        if bulan == 'January':
            bulan ='Januari'
        elif bulan == 'February':
            bulan = 'Febuari'
        elif bulan == 'March':
            bulan = 'Maret'
        elif bulan == 'May':
            bulan = 'Mei'
        elif bulan == 'June':
            bulan = 'Juni'
        elif bulan == 'July':
            bulan = 'Juli'
        elif bulan == 'August':
            bulan = 'Agustus'
        elif bulan == 'October':
            bulan = 'Oktober'
        elif bulan == 'November':
            bulan = 'Nopember'
        elif bulan == 'December':
            bulan = 'Desember'
        print(bulan)
    bulan(self=())
        
    def hari(self):
        now = dt.datetime.now()
        hari = now.strftime('%A')
        if hari == 'Monday':
            hari ='Senin'
        elif hari == 'Tuesday':
            hari ='Selasa'
        elif hari == 'Wednesday':
            hari ='Rabu'
        elif hari == 'Thursday':
            hari ='Kamis'
        elif hari == 'Friday':
            hari ='Jumat'
        elif hari == 'Saturday':
            hari ='Sabtu'
        elif hari == 'Sunday':
            hari ='Minggu'
        print(hari)
    hari(self=())
       
    def jam(self):
        now = dt.datetime.now()
        jam = now.strftime('%H')
        print(jam)
    jam(self=())

    def menit(self):
        now = dt.datetime.now()
        menit = now.strftime('%M')
        print(menit)
    menit(self=())

    def detik(self):
        now = dt.datetime.now()
        detik = now.strftime('%S')
        print(detik)
    detik(self=())
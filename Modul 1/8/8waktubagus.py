import datetime as dt

class Sekarang:
    # def __init__(self, time, tahun, bulan, hari, jam, menit, detik):
    #      now = dt.datetime.now()
    #      self.time = now
    #      self.tahun = now.strftime('%Y')
    #      self.bulan = now.strftime('%B')
    #      hari_time = now.strftime('%A')
    #      if hari_time == 'Tuesday':
    #         self.hari = hari_time.replace('Tuesday', 'Selasa')
    #      elif hari_time == 'Monday':
    #         self.hari = hari_time.replace('Monday', 'Senin')
    #      elif hari_time == 'Wednesday':
    #         self.hari = hari_time.replace('Wednesday', 'Rabu')
    #      elif hari_time == 'Thursday':
    #         self.hari = hari_time.replace('Thursday', 'Kamis')
    #      elif hari_time == 'Friday':
    #         self.hari = hari_time.replace('Friday', 'Jumat')
    #      elif hari_time == 'Saturday':
    #         self.hari = hari_time.replace('Saturday', 'Sabtu')
    #      elif hari_time == 'Sunday':
    #         self.hari = hari_time.replace('Sunday', 'Minggu')
    #      self.jam = now.strftime('%H')
    #      self.menit = now.strftime('%M')
    #      self.detik = now.strftime('%S')
    #      print(self.time)
    #      print(self.tahun)
    #      print(self.bulan)
    #      print(self.hari)
    #      print(self.jam)
    #      print(self.menit)
    #      print(self.detik)
    def time(self):
        now = dt.datetime.now()       
        self.time = now
        # print(self.time)
    def tahun(self):
        now = dt.datetime.now()
        self.tahun = now.strftime('%Y')
        # print(self.tahun)
    def bulan(self):
        now = dt.datetime.now()  
        self.bulan = now.strftime('%B')
        # print(self.bulan)
    def hari(self):
        now = dt.datetime.now()
        hari_time = now.strftime('%A')
        if hari_time == 'Tuesday':
            self.hari = hari_time.replace('Tuesday', 'Selasa')
        elif hari_time == 'Monday':
            self.hari = hari_time.replace('Monday', 'Senin')
        elif hari_time == 'Wednesday':
            self.hari = hari_time.replace('Wednesday', 'Rabu')
        elif hari_time == 'Thursday':
            self.hari = hari_time.replace('Thursday', 'Kamis')
        elif hari_time == 'Friday':
            self.hari = hari_time.replace('Friday', 'Jumat')
        elif hari_time == 'Saturday':
            self.hari = hari_time.replace('Saturday', 'Sabtu')
        elif hari_time == 'Sunday':
            self.hari = hari_time.replace('Sunday', 'Minggu')
        # print(self.hari)
    def jam(self):
        now = dt.datetime.now()
        self.jam = now.strftime('%H')
        # print(self.jam)
    def menit(self):
        now = dt.datetime.now()
        self.menit = now.strftime('%M')
        # print(self.menit)
    def detik(self):
        now = dt.datetime.now()
        self.detik = now.strftime('%S')
        # print(self.detik)
Sekarang = Sekarang()
Sekarang.time() 
Sekarang.tahun()
Sekarang.bulan()
Sekarang.hari()
Sekarang.jam()
Sekarang.menit()
Sekarang.detik()
# print(Sekarang.time)
class Employee:
    '''
    Employee Class adalah Class untuk membuat object pegawai.
    '''

    # class variable
    raise_amount = 1
    employee_id = 10000 # 10001 => 10002

    def __init__(self, first, last, pay):
        self.firstname = first
        self.lastname = last
        self.payment = pay

        self.email = f'{self.firstname.lower()}.{self.lastname.lower()}@company.com'
        Employee.employee_id += 1
        self.id = Employee.employee_id
    
    # regular method
    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split()
        self.firstname = first
        self.lastname = last

    @fullname.deleter
    def fullname(self):
        print('Name Deleted!')
        self.firstname = None
        self.lastname = None



# PROPERTY DECORATOR, SETTER, DELETER

emp_1 = Employee('John', 'Smith', 1000000)

# Property Decorator
# emp_1.firstname = 'Jim'

print(emp_1.firstname)
print(emp_1.email)
print(emp_1.fullname)

# Setter
emp_1.fullname = 'Budi Prakoso'

print(emp_1.firstname)
print(emp_1.email)
print(emp_1.fullname)

# Deleter
del emp_1.fullname

print(emp_1.firstname)
print(emp_1.email)
print(emp_1.fullname)

# INHERITANCE
# dev_1 = Developer('Andi', 'Budiman', 9000000, 'Python')
# print(dev_1.firstname)
# print(dev_1.fullname())
# print(dev_1.email)
# print(dev_1.working_on)
# dev_2 = Developer('Joni', 'Suherman', 8000000, 'HTML')
# print(dev_2.firstname)
# print(dev_2.fullname())
# print(dev_2.email)
# print(dev_2.working_on)
# dev_3 = Developer('Tejo', 'Sukejo', 8000000, 'HTML', 'Web Mainan')

# print(Developer.working_timeline)

# print()

# dev_1.make_apps('hangman')
# print(dev_1.working_on)
# print(dev_2.working_on)
# print(dev_3.working_on)
# dev_2.make_apps('snake')
# print(dev_1.working_on)
# print(dev_2.working_on)
# dev_1.make_apps('sudoku')

# print(Developer.working_timeline)

# dev_1.done_apps('hangman')
# dev_2.done_apps('sudoku')

# print(Developer.working_timeline)

# mgr_1 = Manager('Sue', 'Smith', 15000000)
# print(mgr_1.firstname)
# print(mgr_1.email)
# mgr_1.add_emp(dev_1)
# mgr_1.add_emp(dev_1)
# mgr_1.print_emps()
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# print(dev_1.raise_amount)
# print(mgr_1.raise_amount)
# mgr_1.set_raise_amt(dev_1, 1.50)
# print('raise amount dev_1:', dev_1.raise_amount)
# print('raise amount dev_2:', dev_2.raise_amount)
# print(mgr_1.raise_amount)

# print()

# emp_1 = Employee(first='Ridho', pay=1000000, last='Pratama')
# emp_2 = Employee('Terawan', 'Menkes', 20000000)

# print(emp_1.firstname)
# print(emp_1.lastname)
# print(emp_2.firstname)
# print(Employee.employee_id)

# # df = pandas.read_csv('file.csv')
# # df.describe()

# # print(emp_1.firstname)
# # print('ID Karyawan saya', emp_1.id)
# # nama_ridho = emp_1.firstname
# # print('gaji sebelum dinaikin', emp_1.payment)
# # print(emp_1.email)
# # print(emp_1.fullname())
# # print('Rate kenaikan gaji saya', emp_1.raise_amount)
# # emp_1.apply_raise()
# # print('gaji setelah dinaikin', emp_1.payment)
# # print(emp_1.__dict__)

# # print()
# # print(emp_2.firstname)
# # print('ID Karyawan Pak Terawan', emp_2.id)
# # print('Gaji Pak Terawan kemarin', emp_2.payment)
# # print('Rate kenaikan gaji Pak Terawan', emp_2.raise_amount)
# # emp_2.raise_amount = 1.2
# # print('Rate kenaikan gaji Pak Terawan', emp_2.raise_amount)
# # emp_2.apply_raise()
# # print('Gaji Pak Terawan sekarang', emp_2.payment)
# # print(emp_2.__dict__)
# # print()
# # print(Employee.__doc__)

# # print(emp_2.id)

# # print('Raise Amount:', Employee.raise_amount)
# # print('Raise Amount Saya:', emp_1.raise_amount)
# # print('Raise Amount Pak Terawan:', emp_2.raise_amount)
# # Employee.set_raise_amt(1.10)
# # print('Raise Amount:', Employee.raise_amount)
# # print('Raise Amount Saya:', emp_1.raise_amount)
# # print('Raise Amount Pak Terawan:', emp_2.raise_amount)
# # emp_1.raise_amount = 1.2
# # print('Raise Amount:', Employee.raise_amount)
# # print('Raise Amount Saya:', emp_1.raise_amount)
# # print('Raise Amount Pak Terawan:', emp_2.raise_amount)

# emp_3 = Employee.from_string('Joko-Saurus-1000000')
# print(emp_3.firstname)
# print(emp_3.email)

# # import datetime
# # my_date = datetime.date(2020, 11, 3)
# # print(Employee.is_workday(my_date))
# # print(emp_1.is_workday(my_date))

# class Karnivora:
#     def __init__(self):
#         self.makan_daging = True

# class Herbivora:
#     def __init__(self):
#         self.makan_tumbuhan = True

# class Omnivora():
#     def __init__(self):
#         Karnivora.__init__(self)
#         Herbivora.__init__(self)

# harimau = Karnivora()
# kelinci = Herbivora()
# beruang = Omnivora()

# print(harimau.makan_daging)
# print(kelinci.makan_tumbuhan)
# print(beruang.makan_tumbuhan)
# print(beruang.makan_daging)

# import datetime as dt

# string_date = '2020/02/18'
# tanggal = dt.datetime.strptime(string_date, '%Y/%m/%d')
# # print(tanggal.date())

# # print(tanggal.year)
# # print(tanggal.month)
# # print(tanggal.day)

# now = dt.datetime.now()
# # print(now)
# print(now.day)
# print(now.month)
# print(now.strftime('%d')) # tanggal format dua angka
# print(now.strftime('%m')) # bulan format dua angka
# print(now.strftime('%y')) # tahun format dua angka
# print(now.strftime('%A')) # nama hari
# print(now.strftime('%Y')) # tahun format empat angka
# print(now.strftime('%B')) # nama bulan
# print()
# print(now.strftime('%H')) # format 24 jam
# print(now.strftime('%I')) # format 12 jam
# print(now.strftime('%p')) # format AM/PM
# print(now.strftime('%M')) # menit
# print(now.strftime('%S')) # second / detik

# https://docs.python.org/2/library/datetime.html

# from waktu import Sekarang as skr

# print(skr.time)
# print(skr.tahun)
# print(skr.bulan)
# print(skr.hari)
# print(now.strftime('%A')) # nama hari
# print(skr.jam)
# print(skr.menit)
# print(skr.detik)
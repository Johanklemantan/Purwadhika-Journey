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
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
    # regular method
    def apply_raise(self):
        self.payment = int(self.payment * self.raise_amount)


emp_2 = Employee('Terawan', 'Menkes', 20000000)

# print(emp_1.firstname)
# print(emp_1.lastname)
print(emp_2.fullname())
# print(Employee.employee_id)

# df = pandas.read_csv('file.csv')
# df.describe()

# print(emp_1.firstname)
# print('ID Karyawan saya', emp_1.id)
# nama_ridho = emp_1.firstname
# print('gaji sebelum dinaikin', emp_1.payment)
# print(emp_1.email)
# print(emp_1.fullname())
# print('Rate kenaikan gaji saya', emp_1.raise_amount)
# emp_1.apply_raise()
# print('gaji setelah dinaikin', emp_1.payment)
# print(emp_1.__dict__)

# print()
# print(emp_2.firstname)
# print('ID Karyawan Pak Terawan', emp_2.id)
# print('Gaji Pak Terawan kemarin', emp_2.payment)
# print('Rate kenaikan gaji Pak Terawan', emp_2.raise_amount)
# emp_2.raise_amount = 1.2
# print('Rate kenaikan gaji Pak Terawan', emp_2.raise_amount)
# emp_2.apply_raise()
# print('Gaji Pak Terawan sekarang', emp_2.payment)
# print(emp_2.__dict__)
# print()
# print(Employee.__doc__)

# print(emp_2.id)

# print('Raise Amount:', Employee.raise_amount)
# print('Raise Amount Saya:', emp_1.raise_amount)
# print('Raise Amount Pak Terawan:', emp_2.raise_amount)
# Employee.set_raise_amt(1.10)
# print('Raise Amount:', Employee.raise_amount)
# print('Raise Amount Saya:', emp_1.raise_amount)
# print('Raise Amount Pak Terawan:', emp_2.raise_amount)
# emp_1.raise_amount = 1.2
# print('Raise Amount:', Employee.raise_amount)
# print('Raise Amount Saya:', emp_1.raise_amount)
# print('Raise Amount Pak Terawan:', emp_2.raise_amount)

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

# # harimau = Karnivora()
# # kelinci = Herbivora()
# # beruang = Omnivora()

# # print(harimau.makan_daging)
# # print(kelinci.makan_tumbuhan)
# # print(beruang.makan_tumbuhan)
# # print(beruang.makan_daging)
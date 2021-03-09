class Employee:
    '''
    Employee Class adalah Class untuk membuat object pegawai.
    '''

    # class variable
    raise_amount = 1
    employee_id = 10000 # 10001 => 10002

    def __init__(self, first, last, pay): #first, last, dan pay itu positional argument
        self.firstname = first              #Self, itu object
        self.lastname = last
        self.payment = pay

        # self.email = f'{self.firstname.lower()}.{self.lastname.lower()}@company.com'
        Employee.employee_id += 1
        self.id = Employee.employee_id
    
    #regular method
    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
    
  
    @property
    def email(self):
        if self.fullname == None and self.lastname == None:
            print('This employee is no longer in this office.')
        else:
            return f'{self.firstname.lower()}.{self.lastname.lower()}@company.com'
    #regular method

    @fullname.setter
    def fullname(self, name):
        first, last = name.split() #default spasi
        self.firstname = first
        self.lastname = last

    @fullname.deleter
    def fullname(self):
        print('Full Name Deleted')
        self.firstname = None
        self.lastname = None
    

    def apply_raise(self):
        self.payment = int(self.payment * self.raise_amount)

    # @classmethod
    # def set_raise_amt(cls, ammount):
    #     cls.raise_amount = ammount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    #INHERITANCE CODE
class Developer(Employee):

    working_timeline = dict()

    def __init__(self, first, last, pay, prog_lang, projects=None):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        if projects == None:
            self.working_on = []
        else:
            self.projects = [projects]
        Developer.working_timeline[self.fullname] = self.working_on

    def make_apps(self, apps):
        if apps not in self.working_on:
            self.working_on.append(apps)
            Developer.working_timeline[self.fullname]=self.working_on
            print(f'{self.fullname} is adding {apps} to on going projects')
    
    def done_apps(self,apps):
        if apps in self.working_on:
            self.working_on.remove(apps)
            Developer.working_timeline[self.fullname]=self.working_on
            print(f'{self.fullname} done making the app {apps}')
        else:
            print(f'{self.fullname} is not making the app {apps}. Maybe the other dev.')

    #INHERITANCE PRINT
dev_1 = Developer('Andi','Budiman',9000000,'Python')
# print(dev_1.firstname)
# print(dev_1.fullname())
# print(dev_1.email)
# print(dev_1.working_on)
# print('')
dev_2 = Developer('Joni','Suherman',8000000,'HTML')
# print(dev_2.firstname)
# print(dev_2.fullname())
# print(dev_2.email)
# print(dev_2.working_on)
# print('')
# dev_1.make_apps('hangman')
# dev_1.make_apps('Sudoku')
# print(dev_1.working_on)
# print(dev_2.working_on)
# # dev_2.make_apps('snake')
# # print(dev_1.working_on)
# # print(dev_2.working_on)
dev_3 = Developer('Joko','Widodo',81000000,'HTML')
# dev_3.make_apps('Web Mainan')
# print(Developer.working_timeline)
# dev_2.make_apps('ular')
# print(dev_1.working_on)
# print(dev_2.working_on)



#MGR

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees == None:
            self.employees_list = []
        else:
            self.employees_list = [employees]

    def add_emp(self, emp):
        if emp not in self.employees_list:
            self.employees_list.append(emp)
            print(f'{emp.fullname()} successfully added to your list.')
        else:
            print(f'{emp.fullname()} already in your list.')

    def remove_emp(self,emp):
        if emp in self.employees_list:
            self.employees_list.remove(emp)
            print(f'{emp.fullname()} successfully removed from your list.')
        else:
            print(f'{emp.fullname()} not in your list.')

    def print_emps(self):
        for emp in self.employees_list:
            print(f'--> {emp.fullname()}')
    
    def set_raise_amt(self, emp,ammount):
        emp.raise_amount = ammount

#MGR PRINT
mgr_1 = Manager('Sue', 'Smith',1500000)
# print(mgr_1.firstname)
# print(mgr_1.email)
# mgr_1.add_emp(dev_1)
# mgr_1.add_emp(dev_1)
# mgr_1.print_emps()
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()
# emp_1 = Employee(first='Ridho', last='Pratama',pay= 1000000)
# emp_2 = Employee('Terawan','Menkes',20000000)
# emp_3 = Employee.from_string('Joko-Saurus-1500000')
# print(emp_3.firstname)
# print(emp_3.email)
# # emp_2.raise_amount = 1.2

# print(emp_1.firstname)
# print(emp_2.firstname)

# print(emp_1.firstname)
# print('ID Karyawan saya', emp_1.id)
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
# emp_2.apply_raise()
# print('Gaji Pak Terawan sekarang', emp_2.payment)
# print(emp_2.__dict__)
# print()
# print(Employee.__doc__)

# print(emp_2.id)

# print('Raise Ammount:',Employee.raise_amount)
# print('Raise Ammouns Saya:', emp_1.raise_amount)
# print('Raise Ammouns Pak Terawan:', emp_2.raise_amount)
# Employee.set_raise_amt(1.10)
# print('Raise Ammouns Saya:', emp_1.raise_amount)
# print('Raise Ammouns Pak Terawan:', emp_2.raise_amount)
# emp_1.raise_amount = 1.2
# print('Raise Ammouns Saya:', emp_1.raise_amount)
# print('Raise Ammouns Pak Terawan:', emp_2.raise_amount)

# print(dev_1.raise_amount)
# print(mgr_1.raise_amount)
# mgr_1.set_raise_amt(dev_1, 1.5)
# print('raise ammount dev 1', dev_1.raise_amount)
# print('raise ammount dev 2', dev_2.raise_amount)
# print(mgr_1.raise_amount)


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

# print(dt.datetime.fromisocalendar(2019,7,4))

#https://docs/python.org/2/library/datetime.html



#PROPERTY DECORATOR, SETTER, DELETER

emp_1 = Employee('John','Smith',1000000)
emp_1.firstname = 'Jim'

print(emp_1.firstname)
print(emp_1.email)
print(emp_1.fullname)

#SETTER
emp_1.fullname = 'Budi Prakoso'

print(emp_1.firstname)
print(emp_1.email)
print(emp_1.fullname)

#DELETER
del emp_1.fullname
print(emp_1.firstname)
print(emp_1.email)
print(emp_1.fullname)
class Employee:#parent lass
    num_of_emps = 0
    def __init__(self,name,lastname,pay):
        self.name = name
        self.lastname = lastname
        self.pay = pay
        self.email = name + '.' + lastname + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.name, self.lastname)

class Developer(Employee):#sublass the concept of inheritance
    def __init__(self, name, lastname, pay,pro_lang):
        super().__init__(name,lastname,pay) #by this we an inherit all the funtions of the parent class
        self.pro_lang = pro_lang


emp1 = Employee("Hana", "Kassie",50000)
emp2 = Employee("Atnatewos", "Seyum", 60000)
emp3 = Developer("Bina", "Yeremed", 70000, "Javascript")

print(emp1.name)
print(emp2.email)
print(emp1.fullname())
print(Employee.num_of_emps)

print(emp3.name)
print(emp3.pro_lang)

class Employee():
    def __init__(self, First_Name, Last_Name, Age, Address, Country, Phone_Number, Email):
        self.first_name = First_Name
        self.last_name = Last_Name
        self.age = Age
        self.address = Address
        self.country = Country
        self.phone_number = Phone_Number
        self.email = Email
        self.mail = First_Name + "." + Last_Name + "@class.gmail.com"

    def fullname(self):
        return "{} {} {} {} {} {} {}" .format(self.first_name, self.last_name, self.age, 
                                              self.address, self.country, self.phone_number, self.email)

emp_1 = Employee("Joy", "Simon", 23, "Lisbon off coast dolphin", "Lisbon", +90435647774, "joy.winner@gmail.com")
emp_2 = Employee("Frank", "Tuldin", 37, "westerner pusher 0034", "England", +198745300, "tryertuldin@gmail.com")
emp_3 = Employee("Akira", "kosh", 18, "Vilgan cosma", "North Korea", +112-64538, "kirah@gmail.com")
emp_4 = Employee("Mosh", "Hanedashi", 39, "Delhi", "India", +34266667721, "th@.@gmail.com")
emp_5 = Employee("Ruth", "vukveda", 23, "Town hall", "Poland", +6541099, "vukveda@gmail.com")
emp_6 = Employee("Mark", "Moon", 31, "Upper layer", "Peru", +00-4365733, "mm.10@gmail.com")
emp_7 = Employee("Hadiza", "Suleiman", 27, "Dutsen", "Nigeria", +2347056473653, "hadizbaby@gmail.com")
emp_8 = Employee("Chioma", "Peter", 25, "Orji Owerri", "Nigeria", +2348135657373, "chipeter@gmail.com")
emp_9 = Employee("Kate", "Abraham", 25, "Ruder close werner", "America", +341-44556382, "kateabraham@gmail.com")
emp_10 = Employee("John", "Sky", 28, "Hasbunner oosp", "Russia", +146576000, "opener@gmail.com")

print(emp_1.fullname())
print(emp_2.fullname())
print(emp_3.fullname())
print(emp_4.fullname())
print(emp_5.fullname())
print(emp_6.fullname())
print(emp_7.fullname())
print(emp_8.fullname())
print(emp_9.fullname())
print(emp_10.fullname())

print(emp_1.mail)
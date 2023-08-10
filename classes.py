class Patient():
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.email = first_name + "." + last_name + "@gmail.com"

    def fullname(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.age)
pid = Patient("John", "Joy", 20)
pid1 = Patient("Frank", "Mark", 16)


print(pid.age)
print(pid1.email)

print(pid.fullname())
print(pid1.fullname())

# Classes: Building functions into them
class Patient():
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
    def say_if_minor(self):
        if self.age < 21:
            print("Patient is a minor")
pid2 = Patient("Joel", "Kate", 20)
pid2.say_if_minor()



# 1. Construct a class
class Student:
    def __init__(self, code, name):
        self.code = code
        self.fullname = name

    def display(self):
        print('Code:', self.code, '- Name:', self.fullname)

st1 = Student('SE170000', 'Nguyen Thanh Thuy')
st2 = Student('SE170030', 'Tran Thi Thuy')

st1.display()
st2.display()

# 2. Inheritance:
class Animal:
    def speak(self):
        print('Animal speaking')

class Dog(Animal):
    def bark(self):
        print("Roof roof")

d = Dog()
d.bark()
d.speak()

# 3. Polymorphism:
class Cucumber:
    def type(self):
        print('Vegetable')

    def color(self):
        print('Green')

class Apple:
    def type(self):
        print('Fruit')

    def color(self):
        print('Red')

def func(obj):  # Cách 1: Cách này ngắn gọn, recommended
    obj.type()
    obj.color()

objCucumber = Cucumber()
objApple = Apple()
func(objCucumber)
func(objApple)

# 4. Polymorphism:
class India:
    def capital(self):
        print('New Delhi')

    def language(self):
        print('Hindi and English')

class USA:
    def capital(self):
        print('Washington D.C')

    def language(self):
        print('English')

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):  # Cách 2: dùng vòng lặp thôi vì def func, nhưng cách này dài dòng
    country.capital()
    country.language()

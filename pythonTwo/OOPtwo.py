class Cat():

    # CLASS OBJECT ATTRIBUTES
    species = 'mammal'
    def __init__(self,input_breed, name):
        self.breed = input_breed
        self.name = name

x = Cat('TortoiseShell', 'Moonbeam')
new_cat = Cat('persian','Sammy')
print(new_cat.breed)

class Circle():

    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * self.pi

    def circumference(self):
        return 2 * self.pi * self.radius
mycircle = Circle(10)
print(mycircle.radius)
print(mycircle.area())
print(mycircle.circumference())

class Animal():

    def __init__(self,fur):
        self.fur = fur

    def report(self):
        print('Animal')

    def eat(self):
        print('Eating!')

a = Animal('long and dark')
a.eat()
a.report()

class Dog(Animal):

    def __init__(self,fur):
        Animal.__init__(self,fur)
        print('Dog Created!')

    def report(self):
        print('I am overwriting Animal by writing this in the Dog class')

d = Dog('fuzzy')
d.eat()
d.report()
e = Animal('hairy')
Animal('blonde').report()

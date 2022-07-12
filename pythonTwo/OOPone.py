mylist = [1,2,3]
mylist.append(4)
print(type(mylist))
print(type(12))
print(type(23.53))
print('-----CREATING SAMPLE() CLASS--------')
class Sample():
    pass

# Creating an instance of the class
x = Sample()

print(type(x))

class Dog():
    def __init__(self,breed):
        self.breed = breed

x = Dog('lab')
print(type(x))
print(type(x.breed))
print(x.breed)

class Cat():

    # CLASS OBJECT ATTRIBUTES
    species = 'mammal'
    def __init__(self,input_breed, name):
        self.breed = input_breed
        self.name = name

x = Cat('TortoiseShell', 'Moonbeam')
print(x.breed)
print(x.name)
print(x.species)

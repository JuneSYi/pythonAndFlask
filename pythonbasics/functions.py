def report_person():
    for x in [1,2,3,4,5]:
        print("reporting this person")
report_person()
def reporting(name):
    print("reporting " +name)
reporting("John")
def can(name='EMPTY'):
    print("reporting " +name)
can()
def add_num(num1, num2):
    print(num1+num2)
add_num(2,4)
def num(car):
    return car
print(num(3))
print("-----------functions part two-----------")
print(max([1,3,55,23,145]))
print(min(1,100))
for letter in ['a','b','c']:
    print(letter)
mylist = ['a','b','c']
index = 0
for letter in mylist:
    print(letter)
    print('is at index: {}'.format(index))
    index = index+1
    print('')
for item in enumerate(mylist):
    print(item)

for index,item in enumerate(mylist):
    print(item)
    print(f"is at index {index}")
    print('')

newlist = ['a','b','c','d']
print(''.join(newlist))
print('--'.join(newlist))

def secret_check(mystring):
    if 'secret' in mystring:
        return True
    else:
        return False
print(secret_check('the secreste should be in this string'))

def secret_check(mystring):
    return 'secret' in mystring
print(secret_check('this is a secret'))

def secret_check(mystring):
    return 'secret' in mystring.lower()
print(secret_check('this is a Secret'))

def code_maker(mystring):
    output = list(mystring)
    for index,letter in enumerate(mystring):
        for vowel in 'aeiou':
            if letter.lower()==vowel:
                output[index] = 'x'
                print(letter)
    output = ''.join(output)
    return output
print(code_maker('Sammy'))
print(code_maker('Adam'))

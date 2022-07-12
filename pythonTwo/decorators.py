# decorators allow you to tack on extra functionality to an already existing function
# uses the @ operator and are then placed o top of the original function
def hello(name='Jose'):
    print('The hello() func has been run')

    def greet():
        return '    This is inside the greet() which is insdie hello()'

    def welcome():
        return '     this is inside welcome()'

    if name == 'Jose':
        return greet
    else:
        return welcome

x = hello()
print(x())
print(x)
x=hello(name='Sammy')
print(x())
print('-------hello to jelllo-----------')
def jello():
    return 'Hi Jose'

def other(func):
    print('Some other code')
    # assume that func passed in is a function!!!
    print(func())

other(jello)
print('-----------------')
def new_decorator(func):

    def wrap_func():
        print('some code before executing func')

        func()

        print('Code here, after executing func()')

    return wrap_func

def func_needs_decorator():
    print('please decorate me!!')

func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()

print('--------ANOTHER WAY WITH DECORATOR---------')

def new_decorator(func):

    def wrap_func():
        print('some code before executing func')

        func()

        print('Code here, after executing func()')

    return wrap_func

@new_decorator
def func_needs_decorator():
    print('please decorate me!!')

func_needs_decorator()

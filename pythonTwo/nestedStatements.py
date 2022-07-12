x = 'outside'

def report():
    x = 'inside'
    return x

print(x)
report()
print(x)
print(report())
print(x)

def report():
    # local assignment
    x = 'local'
    print(x)
report()
print(x)

x = 'THIS IS GLOBAL LEVEL'

print(x)
def enclosing():
    x = 'Enclosing level'
    def inside():
        print(x)
    inside()
print(x)
enclosing()
print(x)

def globally():
    # HEY GRAB THE GLOBAL LEVEL X VARIABLE
    global x
    # REASSIGN GLOBAL x
    x = 'reassigning global x inside the fcn()'
    return x
print(x)
globally()
print(x)
print(globally())

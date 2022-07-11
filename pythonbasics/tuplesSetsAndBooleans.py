# TUPLES
t = (1,2,3, 'a', 2.3)
print(t)
print(t[0])
mylist = [1,2,3]
u = (1,2,3)
print(mylist)
mylist[0] = 'NEW'
print(mylist)
# can't change u because it's a tuple. it's immutable
print('-------SETS---------')
x = set()
print(x)
x.add(1)
print(x)
x.add(2)
x.add(3)
print(x)
x.add(3)
x.add(2)
print(x)
mylist = [1,2,121,1,1,2,3,4,5,5,5,4,3,2,2,12]
print(set(mylist))
print(mylist)
print('----BOOLEANS----')
a = True
print(a)
b = False
c = None
print(1 > 2)
print(1<2)

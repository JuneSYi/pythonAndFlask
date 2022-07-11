seq = [1,2,3,4,5]
for item in seq:
    print(item)
salaries = {'John':10, 'Sally':20,'Lisa':30}
for employee in salaries:
    print(employee)
    print(salaries[employee])

print("-----TYPLE UNPACKING-----")
mypairs = [('a',1),('b',2),('c',3)]
for (item1,item2) in mypairs:
    print(item1)
    print(item2)
for item1 in mypairs:
    print(item1)
for letter,num in mypairs:
    print(letter)
print("-------WHILE LOOPS-----------")
i = 1
while i <5:
    print(f"i is currently: {i}")
    i = i+1
for x in range(0,5):
    print(x)
result = list(range(0,11,2))
print(result)
print('s' in 'whgiseogjoei;sgjiodfvjdfiov;jaewjoejfioawfjeio')
print('p' in 'whgiseogjoei;sgjiodfvjdfiov;jaewjoejfioawfjeio')
print(1 in [1,2,3])
print(9 in [1,2,3])

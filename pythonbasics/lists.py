mylist = [1,2,3]
print(mylist)
print(len(mylist))
newlist = [1,2,3,1,1,2,3]
print(len(newlist))
mixlist = [1,2,44.3,'hello']
print(mixlist)
print(len(mixlist))
newlist.append(4)
print(newlist)
newlist.insert(3,224)
print(newlist)
poppeditem = newlist.pop(0)
print(poppeditem)
print(newlist)
mylist1 = [0,1,2]
mylist2 = [3,4,5]
mylist3 = [6,77,88]
megalist = [mylist1, mylist3]
print(megalist)
print(len(megalist))
print("--------------------")
print(megalist[1][2])

'''a=[1,2,2,"python"]
print("a=",a)
print("a =",a[0])
print(len(a))'''

list1=['abc',60,78,45,'manu']
list2=[124,245]
print(list1)
list1.append(25)
print(list1)
print(list1.count(45))
list1.remove(60)
print(list1)
print(list1.index(78))
list1.extend(list2)
print(list1)
list1.reverse()
print(list1)

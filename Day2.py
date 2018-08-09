#type casting
a=42
print(a)
print(str(a))
b = str(a)
print(type(b))

#list
lisT = [1,2,3]
print(lisT)
empty = []
print(empty)
letter = ['a','b','c','d']
print(letter)
# List can contain elements of different types
mixed = ['a',1,'b',2,3,"ali"]
print(mixed)

#---------Modify-------
#Append elements to the end of a List
letter.append('e')
print(letter)
lisT.append(4)
print(lisT)

#Acess elements at a particular index

print(lisT[3])

#You can also slice lists

print(lisT[:3])
print(lisT[1:-1])

#-------------Nested List--------------
#Lists really can contain anything - even other list

list1 = [1,3,4,5]
list2 = [2,6,7]
Nestedlist3 = [list1,list2]
print(Nestedlist3)
print(Nestedlist3[0])
print(Nestedlist3[1])


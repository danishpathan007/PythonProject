# Variables

x = 2 #No Semicolon
y = x * 7
print(y)

x = "Hello , I'am "
z= x + "python"
print(z)

String_way1 = 'hello World'
print(String_way1)
String_way2 = "Hello world"
print(String_way2)
String_way3 = ''' Hello World  '''
print(String_way3)

'''
type(1)
type('h')
type("HEllo")

'''
x = 1
print(x==1)
name = 'Danish'+''+'khan'
print(name)

s = "DANISH"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])
#print(s[6]) IndexError: string Index out of range

#Negative Index
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
#Slicing
print(s[0:2])
print(s[0:4])
print(s[:4]) #by defaut it's start from index[0]
print(s[1:]) #its run upto last index
print(s[1:5:2]) # 1st is starting index , 2nd is last index and the 3rd one is step size and last index is also excluded

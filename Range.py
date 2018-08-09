data = []
if data:
    process(data)
else:
    print("There is no data")
#------------range()-------------#
print(range(3))
#=> range(0, 3)
print(range(5,10))
#=> range(5, 10)
print(range(5,12,3))

for i in range(10):
    print(i)

for i in range(10,20):
    print(i)

for i in range(2,20,4):
    print(i)


#----------Break and Continue----------#


for n in range(10):
    if n == 6:
        break
    print(n, end=',')
       

#=> 0,1,2,3,4,5,


for n in range(10):
    if n % 2 ==0:
        print("Even",n)
        continue
    print("ODd",n)
#-------output-------
'''
ODd 1
Even 2
ODd 3
Even 4
ODd 5
Even 6
ODd 7
Even 8
ODd 9
'''

#------------------FUNCTIONS--------------------#



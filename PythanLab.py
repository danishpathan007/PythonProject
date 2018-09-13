#----------------Multiply all the no of list------------
def mult(list1):
    i,x = 0,1
    while(i<5):
        x*=list1[i]  
        i+=1
    return x     #x return the value of sum of all number in the list

#-------------------Prime Number----------------

def prime1(x):
    i=2
    flag=0
    while(i<x):   #loop will run until condition is false. value i=2 ,x is upto user
        if x%i==0: 
            flag=1
            break  
        i+=1
    if flag==0:   
        print("prime number")
    else:
        print("Not prime number")
    
#list1 = [2,4,5,6,7]            
z=mult([2,4,5,6,7])
print("sum of elements is ",z)
x=int(input("Enter value"))
prime1(x)   


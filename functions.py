#-----------------Functions()-----------

#---No arguments no return type---
def square():
    value = 4**2
    print(value)
square()

#---arguments with no return type---

def square(x):
    value = x**2
    print(value)

square(10)

#---arguments with return type---

def square(x):
    value = x**2
    ''' return value of square'''
    return value

new_value=square(10)
print(new_value)

#------Sum_of_two_var()----------
def add(x,y):
    z = x + y
    ''' return sum  of  x and y '''
    return z

addition=add(22,44)
print(addition)


#-------cal-------

def cal(x,y):
    s = x+y
    m = x*y
    sub = x-y

    return s,m,sub
add,mul,subt=cal(20,10)
print("x+y=",add,"\n","x*y=",mul,"\n","x-y=",subt)


#------ nested function()----------


def mod2plus(x1,x2,x3):
    def inner(x):
        return x % 2+5
    return (inner(x1),inner(x2),inner(x3))
print(mod2plus(1,2,3))


print("\n")

def raise_val(n):
    """ return the inner function """
    def inner(x):
        """Raise x to the power"""
        raised = x ** n
        return raised
    return inner
square=raise_val(2)
cube=raise_val(3)
print(square(2),cube(4))

#-------- Default par------------------

def power(number, pow=1):
    new_value = number**2
    return new_value
print(power(9,2))
print(power(9,1))
print(power(9))


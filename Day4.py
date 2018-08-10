print('spam eggs')
print('doesn\'t')   #use \' toescape the single Quote
print('"yes","he said."')

print('I\'am in Kolkata but I don\'t know that "you are also here".I\'ll see you in Howrah!. But I\'ll request \' you \' to bring "Rasogulla "for me.')

#-------------In Python Everthing is an Object----------------------#

print(isinstance(4, object))
#=> True

print(isinstance("Hello",object))
#=> True

print(isinstance(None,object))
#=> True

print(isinstance([1,2,3],object))
#=> True

#--------------Object have Identity---------------------------#

print(id(object)) #Gives object "identity"
#=>4489377056
#-----------------NOTE--------------#
# "identity " is unique and Fixed during an object's lifetime
# Object contain pointers to their data blob
#object are tagged  with their type at runtime

#This means even small things take up a lot of space.

print((23).__sizeof__())
#=>28

#------------------Variables------------------------#

''' variable are reference to object
    Little more than a object   '''

#------------------FUNCTION--------------------------#

def com(a,b,c):
	return(a+b)*c
print(com(1,2,3))
print(com([1],[2,3],2))  #my first 2 arg is listType and the last one is scaler 
print(com('l', 'olo' ,4))
#=>9
#=>[1, 2, 3, 1, 2, 3]
#lolololololololo


#---------------is vs == ----------------#

print(1 == 1.0)
#=>True
print(type(1) != type(1.0))
#=>True
print(type(1) == type(1.0))
#=>False

''' 1. This 'Is' operator check identity instead of equality
    Use == when comparing values       (Almost always used!)
    use 'is' when comparing identities  (Almost never used!)
'''
#--------------String Methods()------------#
greeting = "Hello world!"

print(greeting.find('lo')) #=>3
print(greeting.replace('llo','y')) #=> Hey world
print(greeting.startswith('Hell')) #=> True
print(greeting.isalpha()) #=> False (due to spacial char or space)
print(greeting.lower()) #=> hello world
print(greeting.title()) #=> Hello World
print(greeting.strip()) #=> Hello world!
print(greeting.strip('!')) #=> Hello world" (no '!')

#--------------split()--------------#

print("Ram and shyam  Both are God".split()) # usind split() String will be convetr into List
#=> ['Ram', 'and', 'shyam', 'Both', 'are', 'God']

print("03-30-2016".split(sep='-'))
#=> ['03', '30', '2016']

# 'join' create a String from a list

print(' ,Ali,'.join(['MAnoj','Tafsir']))
#=> MAnoj ,Ali,Tafsir


#--------------------String Formatting------------------#
print('{} {} '.format('monty','python'))
#=> monty python


#------Provide values by position or by placeholder------
print("{0} can be {1} {0}s".format("strings","formatted")) 
#=>  strings can be formatted stringss

print("{name} loves {food}".format(name="Danish",food="plums"))
#=>Danish loves plums





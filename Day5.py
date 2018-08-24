#-----------------------List---------------------------#

# Finite , Orderded , mutable and sequence of Elements

'''

list.remove(12)
list.clear()
list.count()


'''


#---------------------Dictonary------------------------#
#Mutable map from hashable values to arbitrary object

'''

myself.get("key")

del myself['keyname']
> myself.keys()
> myself.values()
> myself.items()

'''

#-----------Tuples---------#

'''
>>> 
>>> t= 12345, 54321,'hello'
>>> t
(12345, 54321, 'hello')
>>> type(t)
<class 'tuple'>
>>> x , y , z = t
>>> t
(12345, 54321, 'hello')
>>> x
12345
>>> y
54321
>>> z
'hello'
'''


#-----------Swapping values--------------#
'''
>>> x = 15
>>> y = 10
>>> x = x ^ y
>>> y = x ^ y
>>> x = x ^ y
>>> print(x,y)
10 15

x,y = y,x  [as simple as that]   //Tuple packing

'''



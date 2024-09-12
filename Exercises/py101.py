# if 5<2:
#     print("5<2")
# elif 2<3:
#     print("2<3")
# else:
#     print("NULL")

# for i in range(2,10):
#     if i%2==0:
#         print("even ",i)
#     else:
#         print("odd ",i)

# print(float("inf"))   # positive infinity
# print(float("-inf"))  # negative infinity

##Lists

# arr = [2,3,4]
# print(len(arr))

# arr.append(5)
# print(arr)
# arr.pop()
# print(arr)

# s = 'chandan'
# s = ['chandan','champy']
# for ch in s:
#     print(ch, end = ' ')

# tup = (1,2,3)
# print(sum(tup))

# find_sum = lambda s: sum(int(ch) for ch in str(s))
# print(find_sum(101))
# print((lambda s: sum(int(ch) for ch in str(s)))(101)) # function name can be replaced by the lambda function itself

# lambda_func = lambda n,m: (n**3 - m) if n % 2 == 0 and m % 2 ==0 else n**3
# print(lambda_func(2,2))


l = ["1", "2", "9", "0", "-1", "-2"]
# # added 10 to each item after type
# # casting to int, then convert items to string again
# print("Operation on each item using lambda and map()", list(map(lambda x: str(int(x) + 10), l)))
# print("Operation on each item using lambda and map()", map(lambda x: str(int(x) + 10),l))

#yield 
# def sum(a,b):
#     yield a+b
#     yield a-b

# sum_func = sum(3,4)
# print(next(sum_func))
# print(next(sum_func))

# Control statements
# lis = list()
# if len(lis) == 0:
#      lis.append('cas')
# else: pass
# for l in lis:       
#     print(l)

# pass does nothing and is used as a placeholder.
# break terminates the current loop prematurely.
# continue skips the remaining code for the current iteration and moves to the next iteration in the loop.

# Iterating over dictionary
# print("Dictionary Iteration")

# d = dict()

# d['xyz'] = 123
# d['abc'] = 345
# for i in d:
# 	print("% s % d" % (i, d[i]))

# for k,v in d.items():
#       print(k,v)

# rangoli program lol
# num = 5
# num2 = num
# for i in range(1,num+1):
#     for j in range(num2,0,-1):
#         print("*",end='')
#     num2-=1
#     print()
# for i in range(1,num+1):
#     for j in range(i,0,-1):
#         print("*",end='')
#     print()

# # zip function to iterate over two lists simultaneously 
# fruits = ["apple", "banana", "cherry"]
# colors = ["red", "yellow", "green",'sdf']
# for fruit, color in zip(fruits, colors):
# 	print(fruit, "is", color)

# non-equal lists result will be only for common indices

# sum = 0
# for i in range(1,11):
# 	sum+=i
# print("Sum of first 10 integers: ",sum)

#for/while else statements
# The else block just after for/while is executed only when the loop is NOT terminated by a break statement.
# count = 0
# while (count < 1):	
# 	count = count+1
# 	print(count)
# 	break
# else:
# 	print("No Break")


# Prints all letters except 'e' and 's'
# i = 0
# a = 'geeksforgeeks'
# print(''.join([x for x in a if x != 'e' and x!= 's']))
# print([x if x!='e' and x!='s' else '-1' for x in a])
# for ch in a:
#       if ch == 'e' or ch == 's':
#             continue
#       else:
#             print(ch)

# while i < len(a):
# 	if a[i] == 'e' or a[i] == 's':
# 		i += 1
# 		continue
		
# 	print('Current Letter :', a[i])
# 	i += 1

# STRINGS
s = 'chandan likes nivedita'
# #string[start:stop:step] - string slicing
# print("prints entire string: ",s[:]) #prints entire string
# print("prints from third character to second last character (not including): ",s[3:-2]) #prints from third character to second last character (not including)
'''string reversal - 1'''
# print("reverses the string: ",s[::-1]) #reverses the string
# print("writes the string as it is: ",end='') #usage of end in print
# print(s[::1]) #writes the string as it is

'''string reversal - 2'''
# def reverse_func(str):
#     s = ''
#     for i in str:
#         s = i + s
#     return s

# print("Reversed string : ",reverse_func(s))

#python reversed function
# print(tuple(reversed(range(1,5))))

'''string reversal - 3'''
#reversing a string using built-in join and reversed function
# s = ['45','65']
# def reverse(str):
#     return ','.join(reversed(str))

# print(reverse(s))

'''string reversal - 4'''
#using list comprehension

# def reverse_str(str):
#     s = [str[i] for i in range(len(str)-1,-1,-1)]
#     # print(s) #prints the string as list in reverse
#     return ''.join(s) #''.join(list) can be used to convert list to string

# print(reverse_str(s))

# t = (2,3,4)
# print(sum(t))
# t = [2,3,4]
# print(sum(t))

#String functions
# my_string = "geEks 4 GeeKS & Geeks For Geeks"
# print("counts number of occurrences of a given substring: ",my_string.count('e'),my_string.lower().count("geeks")) 
# print("Convert to lower case: ",my_string.lower())
# print("Convert to upper case: ",my_string.upper())
# print("Convert to capitalize: ",my_string.capitalize())
# #Python f-strings
# title_str = my_string.title()
# print(f"Convert to title: {title_str} ")
#evaluating expressions in f-strings
# a = 5
# b = 10
# print(f"He said his age is {2 * (a + b)}.")
# #Lambda Expressions using F-strings
# num = 16
# print(f"Square of {num} if the number is even, is: {(lambda num: num**2 if num%2==0 else 0)(num)}")

#code to remove i-th element from a string

# s = 'chandan'
# l = list(s)
# i = 4
# del l[4]
# print(l)
# l[4] = 'g'
# print(''.join(l))
# l.insert(4,'d')
# l[5] = 'a'
# print(''.join(l))


#FUNCTIONS

# #python function to add two numbers
# def add(num1: int, num2: int) -> int:
# 	"""Add two numbers"""
# 	num3 = num1 + num2
# 	return num3

# # Driver code
# num1, num2 = 5, 15
# ans = add(num1, num2)
# print(f"The addition of {num1} and {num2} results {ans}")

# Python map() Function

# Syntax:
# map(fun, iter)
# Parameters:
# fun: It is a function to which map passes each element of given iterable.
# iter: It is iterable which is to be mapped.

# Note: You can pass one or more iterable to the map() function.

# Returns:
# Returns a list of the results after applying the given function  
# to each item of a given iterable (list, tuple etc.) 

#example - 1
# def addition(n):
#     return n+n

# numbers = list(range(1,6))
# result =  map(addition,numbers)
# print(result)
# print(list(result)) #prints a list
# print(tuple(result)) #in an attempt to print a tuple, it gives null cz, I've already consumed the iterator into the list. The others get an empty iterator.
# print(tuple(map(addition,numbers))) #prints a tuple
# print(set(map(addition,numbers))) #prints a set

# #example - 2
# #using lambda expressions
# numbers2 = list(range(11,16))
# result_lambda = map(lambda x: x*x, numbers2)
# print(tuple(result_lambda))

# # example - 3
# # Add two lists using map and lambda
# list_1 = list(range(1,6))
# list_2 = list(range(11,14))

# print(f"List 1: {list_1}\nList 2: {list_2}")
# result = map(lambda x,y: x+y, list_1, list_2)
# print(f"Result list: {list(result)}")


# Python filter() 
# Syntax: filter(function, sequence)

# Parameters:
# function: function that tests if each element of a sequence is true or not.
# sequence: sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.
# Returns: an iterator that is already filtered.

#example - 1

# Define a function to check
# if a number is divisible by 3

# def divisible_by_3(num):
#     temp_list = list(str(num))
#     result = lambda temp_list : sum(int(t) for t in temp_list)
#     return result(temp_list)%3 == 0

# numbers = [1,2,3,33,77,102,104,78]
# result_filter = filter(lambda x: divisible_by_3(x),numbers)
# print(list(result_filter))

#example - 2

# # a list contains both even and odd numbers.
# seq = [0, 1, 2, 3, 5, 8, 13]

# # result contains odd numbers of the list
# result = filter(lambda x: x % 2 != 0, seq)
# print(list(result))

# # result contains even numbers of the list
# result = filter(lambda x: x % 2 == 0, seq)
# print(list(result))

# LISTS and list functions

# List = [1,2,3,4,4,67]
# #append always inserts value at the end of the list
# List.append(10)
# List.append(('chandan','nivu')) #append tuple
# List.append({'string','string','append'}) #set append, we see only one occurrence of string. And the order might not be exact. Why??
# #to insert value at a particular position, use insert(position,value)
# List.insert(0,'Geek')
# List.insert(4,'For')
# #since append takes only 1 argument, we use extent method which appends more than one value at the end of list
# List.extend([('end','of','list'),[45],55])
# print(f"Actual list: {List}")
# #list reversal
# List.reverse()
# print(f"Reversed list using reverse function : {List}")
# new_list = list(reversed(List))
# print(f"Reversed list using reversed function: {new_list}, OG list : {List}")
# #Removing Elements from the List
# #remove removes first occurrence of the element in the list. throws error if not found in the list
# #to remove multiple elements using remove, an iterator is used
# new_list.remove(4)
# # pop() function can also be used to remove and return an element from the list, but by default it removes only the last element of the list, to remove an element from a specific position of the List, the index of the element is passed as an argument to the pop() method.
# new_list.pop()
# new_list.pop(-2)
# print(new_list)

#LIST SLICING
# Python program to demonstrate
# Removal of elements in a List

# # Creating a List
# List = ['G', 'E', 'E', 'K', 'S', 'F',
# 		'O', 'R', 'G', 'E', 'E', 'K', 'S']
# print("Initial List: ")
# print(List)

# # Print elements of a range
# # using Slice operation
# Sliced_List = List[3:8]
# print("\nSlicing elements in a range 3-8: ")
# print(Sliced_List)

# # Print elements from a
# # pre-defined point to end
# Sliced_List = List[5:]
# print("\nElements sliced from 5th "
# 	"element till the end: ")
# print(Sliced_List)

# # Printing elements from
# # beginning till end
# Sliced_List = List[:]
# print("\nPrinting all elements using slice operation: ")
# print(Sliced_List)

# # Negative index List slicing

# # Creating a List
# List = ['G', 'E', 'E', 'K', 'S', 'F',
# 		'O', 'R', 'G', 'E', 'E', 'K', 'S']
# print("\n---------------------\nInitial List: ")
# print(List)

# # Print elements from beginning
# # to a pre-defined point using Slice
# Sliced_List = List[:-6]
# print("\nElements sliced till 6th element from last: ")
# print(Sliced_List)

# # Print elements of a range
# # using negative index List slicing
# Sliced_List = List[-6:-1]
# print("\nElements sliced from index -6 to -1")
# print(Sliced_List)

# # Printing elements in reverse
# # using Slice operation
# Sliced_List = List[::-1]
# print("\nPrinting List in reverse: ")
# print(Sliced_List)

# DICTIONARY

# # Creating an empty Dictionary
# Dict = {}
# print("Empty Dictionary: ")
# print(Dict)

# # Creating a Dictionary
# # with dict() method
# Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
# print("\nDictionary with the use of dict(): ")
# print(Dict)

# # Creating a Dictionary
# # with each item as a Pair
# Dict = dict([(1, 'Geeks'), (2, 'For')])
# print("\nDictionary with each item as a pair: ")
# print(Dict)

# # Creating a Nested Dictionary
# # as shown in the below image
# Dict = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
# print(Dict)

# Adding elements to a Dictionary
# dict = {}
# print(f'Empty dict {dict}\n')
# dict[1] = 'my'
# dict[2] = 'name'
# dict[3] = 'is'
# dict['khan'] = 'chandan'
# print(f'Original dict {dict}\n')
# dict[3] = 'iz'
# print(f'After updating value for key 3, the dict is {dict}\n')
# #Adding nested key-value pair to the dict
# dict[6] = {7:'python is interesting','excited':'i like python'}
# print(f'Nested dict {dict}\n')
# #Updating value using update() function
# dict.update({1:'iam'})
# print(f'Updating dictionary using update() function {dict}\n')
# #Merging two dictionaries using update() function
# mydict2 = {1:'my',7:'it\'s my birthday'}
# dict.update(mydict2)
# print(f'OG dict post merge {dict}. Value of key 1 is overwritten with the value of the same key from second dictionary\n')
# #Accessing nested dictionaries
# print(dict[6]['excited'])
# print(dict[1])
# #delete elements from dict
# del dict['khan']
# print(f'Post deleting the element from dict {dict}\n')

# Dictionary functions

# mydict2 = {1:'is',2:'my name is khan',7:'it\'s my birthday',10:'july 7th'}
# # print(dict[0]) # throws error as there's no key = 0
# #instead we use get function to fetch value of a key
# print(f'\nValue in the dict of key=0 is: {mydict2.get(0, None)}\n')
# print(f'Value in the dict of key=7 is: {mydict2.get(7, None)}\n')
# print(f'Actual dict is {mydict2}\n')

# #copy function - Returns a copy of the dictionary
# new_dict = mydict2.copy()
# print(f'\nPost copy {new_dict}')

# # clear function - Remove all the elements from the dictionary
# new_dict.clear()
# print(f'\nPost clear {new_dict}')

# keys_only_dict = {'key1': None, 'key2': None, 'key3': None}
# print(keys_only_dict)

# print(f'\nReturns a list containing a tuple for each key value pair - {mydict2.items()}')
# print(f'\nReturns a list of keys in the dictionary - {mydict2.keys()}')
# print(f'\nReturns a list of values in the dictionary - {mydict2.values()}')
# Remove the element with specified key
# print(f'\nRemove the element with specified key and returns value: {mydict2.pop(1)}')
# print(f'\nPost removal of key = 1, the dict is - {mydict2}')
# print(f'\nIf no key is found, default argument is used - {mydict2.pop(1,"No such key found in mydict2")}')
# print(f'\nUpdated dictionary - {mydict2}')
# print(f'\npopitem() function removes last inserted kv pair - {mydict2.popitem()}')
# print(f'\nUpdated dictionary - {mydict2}')
# print(f'\nIs key = 7 present in mydict2? {7 in mydict2}') #has_key() function has been removed in python 3.x instead use key in dict

# REMEMBER -
# dict.get(key,default) and dict.pop(key,default)
# ex:
# print(f'{mydict2.get(0, None)}')
# print(f'{mydict2.pop(1,"No such key found in mydict2")}')

# setdefault() is a dictionary method used to retrieve a value from a dictionary. If the specified key is present in the dictionary, it returns the corresponding value; otherwise, it inserts the key with a specified default value and returns that value.

# # Define a dictionary
# my_dict = {'a': 1, 'b': 2, 'c': 3}

# # Retrieve value for an existing key
# value1 = my_dict.setdefault('a', 0)
# print("Value for 'a':", value1)  # Output: Value for 'a': 1

# # Retrieve value for a non-existing key
# value2 = my_dict.setdefault('d', 4)
# print("Value for 'd':", value2)  # Output: Value for 'd': 4

# print("Updated Dictionary:", my_dict)
# # Output: Updated Dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}



# dict = {'1':'chandu',2:'pushpakka',3:'swaroop'}
# val = list(dict.values())
# print(val)
# keys = list(dict.keys())
# print(keys)
# print(val.append('swaroopini'))     #prints None, as append returns None
# print(val)
# print(f"Actual dictionary {dict}\n")
# if 'swaroop' in dict.values():
#       print("Swaroop found in the dictionary values")
# else:
#       print("Swaroop not found in the dictionary values")

# # if 'swaroop' in dict.keys(): or
# if 'swaroop' in dict:
#       print("Swaroop found in the keys")
# else:
#       print("Swaroop not found in the keys")



# tup = ('chandan',)*3
# print(tup)

# # Sorting a list in ascending order with sorted()
# my_tuples = [(1, "one"), (3, "three"), (2, "two"), (4, "four")]
# sorted_tuples = sorted(my_tuples, key=lambda x: x[1], reverse=True)
# print(sorted_tuples)

# # Sorting a List of Dictionaries by a Specific Key using Sorted()
# students = [
#     {'name': 'John', 'age': 20},
#     {'name': 'Alice', 'age': 18},
#     {'name': 'Bob', 'age': 22}
# ]
# sorted_students = sorted(students,key=lambda x: x['age'])
# print(sorted_students)

# # LIST Sorting
# l = [23,12,63]
# l.sort() #tim_sort
# print(l)

# # Sorting a List by a Specific Key using Sorted()
# l = ['chanda','chandan','cha']
# new_l = sorted(l,key = lambda x: len(x))
# print(new_l)

# Extended iterable unpacking
# numbers = [1, 2, 3, 4, 5]
# first, second, Three, *rest = numbers

# print("First:", first)  # Output: First: 1
# print(f"Second: {second}")
# print("Rest:", rest)    # Output: Rest: [3, 4, 5]
# print(f"Third element: {Three}")

# args and kwargs in python

# *args:

# The *args syntax in a function definition allows you to pass a variable number of positional arguments to the function.
# When you use *args, you can pass any number of arguments to the function, and they will be wrapped into a tuple.
# The name args is a convention, but you can use any valid variable name preceded by * to collect positional arguments.

# Example of *args:

# def my_function(*args):
#     for arg in args:
#         print(arg)

# my_function(1, 2, 3)

# **kwargs:

# The **kwargs syntax in a function definition allows you to pass a variable number of keyword arguments (key-value pairs) to the function.
# When you use **kwargs, you can pass any number of keyword arguments to the function, and they will be wrapped into a dictionary.
# The name kwargs is a convention, but you can use any valid variable name preceded by ** to collect keyword arguments.

# Example of *kwargs:

# def my_function(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# my_function(name="Alice", age=30, city="New York")


# *args collects positional arguments into a tuple.
# **kwargs collects keyword arguments into a dictionary.

# You can use both *args and **kwargs together in a function definition if you want to accept both positional and keyword arguments of variable length:

# def my_function(*dargs, **dkwargs):
#     for arg in dargs:
#         print(arg)
#     for key, value in dkwargs.items():
#         print(f"{key}: {value}")

# my_function(1, 2, name="Alice", age=30)

# dict_a = {'a': 1, 'b': 2}
# print(set(dict_a))

# dict_a = {'a': 1, 'b': 2}
# dict_b = {'b': 3, 'c': 4}
 
# result = {key: dict_a.get(key, 0) + dict_b.get(key, 0) for key in set(dict_a) | set(dict_b)}
# result2 = {key: dict_a.get(key, 0) + dict_b.get(key, 0) for key in set(dict_a) & set(dict_b)}
# result3 = [dict_a.get(key, 0) + dict_b.get(key, 0) for key in set(dict_a) | set(dict_b)]

# print(result)
# print(result2)
# print(result3)

# print([2,3,1]+['chandan'])
# s = [2,3,1],['chandan']
# print(s)
# print([2,3,1],['chandan'])


# split() function splits a sentence into a list of words
# split()[::-1] reverses this list that was created
# list(string_s) creates a list of characters the string contains. the string might be a sentence too!

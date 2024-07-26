# Python3 code to demonstrate working of 
# Filter dictionary values in heterogeneous dictionary
# Using type() + dictionary comprehension
 
# initializing dictionary
test_dict = {'Gfg' : 4, 'is' : 2, 'best' : 3, 'for' : 'geeks'}
 
# printing original dictionary
print("The original dictionary : " + str(test_dict))
 
# initializing K 
K = 3
res_dict = {key: val for key, val in test_dict.items()
            if type(val) != int or (type(val) == int and val > K)}

res_dict_2 = {key: val for key, val in test_dict.items()
            if not isinstance(val,int) or (type(val) == int and val > K)}

print(f"Result dictionary where values are greater than 3 or not integer")
print(res_dict)
print(res_dict_2)
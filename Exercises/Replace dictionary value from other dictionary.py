# Replace dictionary value from other dictionary

# initializing dictionary
test_dict = {"Gfg" : 5, "is" : 8, "Best" : 10, "for" : 8, "Geeks" : 9}
 
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
 
# initializing updict
updict = {"Gfg"  : 10, "Best" : 17}

#method-1
test_dict.update(updict)
print(f"Updated dictionary {test_dict}")

# method-2
res_dict = {key: updict.get(key,val) for key, val in test_dict.items()}
res_dict2 = {key: updict.get(key,test_dict[key]) for key in test_dict.keys()}
print(f"Updated dictionary {res_dict}")
print(f"Updated dictionary {res_dict2}")
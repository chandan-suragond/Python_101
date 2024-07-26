# Code to sort dictionary based on key

dict = {'ravi': '10', 'rajnish': '9',
        'sanjeev': '15', 'yash': '2', 'suraj': '32'}

print(f"Initial dictionary {dict}")
keys = list(dict.keys())

keys.sort()
# print(sorted(keys,reverse=True))

# sorted_dict = {}
# for k in keys:
#       sorted_dict[k] = dict[k]
sorted_dict = {key: dict[key] for key in keys}
print(f"Sorted dictionary based on key {sorted_dict}")

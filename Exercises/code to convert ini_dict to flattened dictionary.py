# code to convert ini_dict to flattened dictionary

# di = {'a': 1,
# 'c': {'a': 2,
# 'b': {'x': 5,
# 'y' : 10}},
# 'd': [1, 2, 3]}

def flatten_dict(dd, separator='_', prefix=''):
	res = {}
	for key, value in dd.items():
		if isinstance(value, dict):
			res.update(flatten_dict(value, separator, prefix + key + separator))
		else:
			res[prefix + key] = value
	return res

# initialising_dictionary
ini_dict = {'geeks': {'Geeks': {'for': 7}},
			'for': {'geeks': {'Geeks': 3}},
			'Geeks': {'for': {'for': 1, 'geeks': 4}}}

# printing initial dictionary
print("initial dictionary", str(ini_dict))

# flattening the dictionary
res = flatten_dict(ini_dict)

# printing final dictionary
print("final dictionary", str(res))
#This code is contributed by Vinay Pinjala.

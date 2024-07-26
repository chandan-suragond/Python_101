# Convert flattened dictionary into nested dictionary

def add_to_nested_dict(nested_dict, keys, value):
	"""Add a value to a nested dictionary at the specified keys."""
	temp = nested_dict
	for key in keys[:-1]:
		temp = temp.setdefault(key, {})
	temp[keys[-1]] = value
	return nested_dict

# initialising_dictionary
ini_dict = {'Geeks_for_for':1,'Geeks_for_geeks':4,
			'for_geeks_Geeks':3,'geeks_Geeks_for':7}

# printing initial dictionary
print ("initial_dictionary", str(ini_dict))

# create empty nested dictionary
d = {}

# iterating_over_dict
for k, v in ini_dict.items():
	# splitting keys
	keys = k.split('_')
	# add value to nested dictionary
	add_to_nested_dict(d, keys, v)

# printing final dictionary
print ("final_dictionary", str(d))

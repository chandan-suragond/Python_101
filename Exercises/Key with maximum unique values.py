# Key with maximum unique values

test_dict = {"Gfg" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]} 

# def find_max_key (test_dict):
#       new_dict = {}
#       max_val = 0
#       for k,v in test_dict.items():
#             new_dict[k] = len(set(v))
#             if len(set(v)) > max_val:
#                   max_key = k
#       # print(f"New dictionary where values are length of set: {new_dict}")
#       # print(f"Max length key is '{max_key}'")
#       return max_key


# print(f'Max key - {find_max_key(test_dict)}')
# # Sorting to reverse sort dictionary
print(sorted(test_dict, key = lambda ele: len(set(test_dict[ele])), reverse = True)[0])
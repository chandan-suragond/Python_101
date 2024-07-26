# Sort String list by K character frequency

# Input : test_list = ['geekforgeekss', 'is', 'bessst', 'for', 'geeks'], K = 's' 
# Output : ['bessst', 'geekforgeekss', 'geeks', 'is', 'for'] 
# Explanation : bessst has 3 occurrence, geeksforgeekss has 3, and so on.

# Input : test_list = ['geekforgeekss', 'is', 'bessst'], K = 'e' 
# Output : ['geekforgeekss', 'bessst', 'is'] 
# Explanation : Ordered decreasing order of 'e' count. 

test_list = ['geekforgeekss', 'is', 'bessst', 'for', 'geeks']
k = 's'

print(f"Original string list : {test_list}")
print(f"Sorted function used to sort the list : {sorted(test_list)}")
print(f"Sorted function used to sort the list in reverse : {sorted(test_list, reverse=True)}")
print(f"Sorted function used to sort the list in reverse basis string length : {sorted(test_list, key=len, reverse=True)}")
print(f"Actual needed output : {sorted(test_list, key= lambda x: x.count(k), reverse=True)}")
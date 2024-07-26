# Group Similar items to Dictionary Values List

from collections import Counter

test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8] 

s = dict(Counter(test_list))
print(s)

new_dict = {}
for k,v in s.items():
      new_dict[k] = [k]*v

print(new_dict)
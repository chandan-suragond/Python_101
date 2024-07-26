# Find all duplicate characters in string

# Input : geeksforgeeeks
# Output : e g k s
from collections import Counter

s = 'geeksforgeeks'

def using_Counter(s):
      new_dict = dict(Counter(s))
      print(new_dict)
      new_list = []
      for k,v in new_dict.items():
                  if v > 1:
                        new_list.append(k)
      return new_list

def find_duplicate_chars(s):
      chars_dict = {}

      for x in s:
            if x not in chars_dict:
                  chars_dict[x] = 1
            else:
                  chars_dict[x] += 1

      new_list = []
      for k,v in chars_dict.items():
            if v > 1:
                  new_list.append(k)
      return new_list

def using_count(s)->list:
      new_list = []
      for i in s: 
            if i not in new_list and s.count(i)>1:
                  new_list.append(i)
      return new_list

print(find_duplicate_chars(s))
print(using_count(s))
print(using_Counter(s))
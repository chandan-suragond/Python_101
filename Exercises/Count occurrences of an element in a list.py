# Count occurrences of an element in a list

from collections import Counter

lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
key = 10

#Solution - 3
def using_counter(lst):
      new_dict = Counter(lst)
      print(dict(new_dict))
      return new_dict[key]

# solution - 1
def count_occ(li):
      counter = 0
      for x in li:
            if x == key:
                  counter+=1
      return counter

# solution - 2
def count_func(li):
      return li.count(key) #list method

print(f"Number of times the element {key} occurs in the list is {count_occ(lst)}")
print(f"Number of times the element {key} occurs in the list is {count_func(lst)}")
print(f"Number of times the element {key} occurs in the list is {using_counter(lst)}")
# Python Program to print all Possible Combinations from the three Digits

from itertools import permutations

count = 0
comb = permutations(range(1,4),3)
for i in comb:
      print(i)
      count+=1
print(count)

# print(list(permutations('chn',3)))
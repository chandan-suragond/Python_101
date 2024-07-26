# Reverse Row sort in Lists of List
lst = [[4, 1, 6], [7, 8], [4, 10, 8]]

# solution - 1
reverse_row_sort1 = list(map(lambda x: sorted(x,reverse=True),lst))

# solution - 2
reverse_row_sort2 = [sorted(x,reverse=True) for x in lst]

# solution - 3
def reverse_row_sort_func(lst):
      for ele in lst:
            ele.sort(reverse = True)
      return lst

print(f'Actual list {lst}')
print(f'Reverse row sorted list {reverse_row_sort1}')
print(f'Reverse row sorted list {reverse_row_sort2}')
print(f'Reverse row sorted list {reverse_row_sort_func(lst)}')
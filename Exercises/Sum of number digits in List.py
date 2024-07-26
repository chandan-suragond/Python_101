# Sum of number digits in List
lst = [12, 67, 98, 34]

# solution - 1
result_list = []
def find_sum(li):
      for l in li:
            result_list.append(sum_num_int(list(str(l))))
      return result_list

sum_num_int = lambda x: sum(int(i) for i in x)

# solution - 2
result_lst = list(map(lambda x: sum(int(i) for i in str(x)),lst))

print(f"Actual list: {lst}")
print(f"Summation list: {find_sum(lst)}")
print(f"Summation list: {result_lst}")
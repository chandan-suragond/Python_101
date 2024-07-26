
# Python program to find the Strongest Neighbour

arr1 = [1,2,2,3,4,5]
# arr1 = [5,5]

def strongest_neighbour(lst):
      len_var = len(lst)
      result_lst = []
      for i in range(0,len_var-1):
            # if lst[i] >= lst[i+1]:
            #       result_lst.append(lst[i])
            # else:
            #       result_lst.append(lst[i+1])
            result_lst.append(max(lst[i],lst[i+1]))
      return result_lst

print(f'Actual list {arr1}')            
print(f'Strongest neighbour list {strongest_neighbour(arr1)}')
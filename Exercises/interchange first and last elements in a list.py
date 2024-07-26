# Python program to interchange first and last elements in a list
list = [21,32,56,78,99]

def swapList(list_l):
      first = list_l.pop(0)
      last = list_l.pop()
      list_l.insert(0,last)
      list_l.append(first)
      return list_l

def swapList_2(l):
      l[0],l[-1] = l[-1],l[0]
      return l

def swapList_3(l):
      # store values in a tuple var get
      get = l[-1],l[0]
      # unpack tuple var
      l[0],l[-1] = get
      return l

print(f"Actual list: {list}")
print(f"Swapped list: {swapList(list)}")
print(f"Swapped list: {swapList_2(list)}")
print(f"Swapped list: {swapList_3(list)}")
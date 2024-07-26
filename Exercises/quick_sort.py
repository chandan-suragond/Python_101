def quick_sort(arr):
      if len(arr) <= 1:
            return arr
      length = len(arr)
      pivot = arr[0]
      less_than_pivot = [arr[x] for x in range(1,length) if arr[x] <= pivot]
      greater_than_pivot = [arr[x] for x in range(1,length) if arr[x] > pivot]
      return quick_sort(less_than_pivot)+[pivot]+quick_sort(greater_than_pivot)


a = [2, 8, 5, 3, 9, 4, 1]
print(quick_sort(a))

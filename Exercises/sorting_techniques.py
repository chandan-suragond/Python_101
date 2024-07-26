def bubble_sort(arr):
      if len(arr) <= 1:
            return arr
      n = len(arr)
      for i in range(n):
            for j in range(0, n - i - 1):
                  if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
      return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged


a = [2, 8, 5, 3, 9, 4, 1]
print(bubble_sort(a))
print(quick_sort(a))
print(merge_sort(a))  # Output: [1, 2, 3, 4, 5, 8, 9]







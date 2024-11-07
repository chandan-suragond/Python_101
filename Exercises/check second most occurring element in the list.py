li = [1,2,3,4,5,2,2,3]

#Solution-1 (my solution)
def char_freq(li):
    di = dict()
    for i in li:
        if i in di.keys():
            pass
        else:
            di[i] = li.count(i)
    print(di)
    val_li = list(set(di.values()))
    val_li.sort(reverse = True)
    for k,v in di.items():
        if v == val_li[1]:
            print(k)
            

char_freq(li)

# #Solution-2
# # Original dictionary
# di = {1: 3, 2: 3, 3: 3, 4: 2, 5: 1}

# # Sort the dictionary by values in descending order
# sorted_di = dict(sorted(di.items(), key=lambda item: item[1], reverse=True)) #di.items() populates (key,value) pairs, item refers to each key,value pair, of which item[1] refers to the value part of the pair.

# print(sorted_di)

#Solution-3
# def char_freq(li):
#     di = dict()
#     for i in li:
#         if i in di.keys():
#             pass
#         else:
#             di[i] = li.count(i)
#     print(di)
#     print(sorted(di, key = lambda item: di[item], reverse=True)[1]) #by default sorted function over a dictionary always returns a list of keys. Here, di populates dictionary, item picks up each key and di[item] pulls out value of each key and [1] pull out second element of the resultant list



#LIGHT READING
# The reason sorted_di ends up as a dictionary in this code:
# ```python
# sorted_di = dict(sorted(di.items(), key=lambda item: item[1], reverse=True))
# ```

# is because of the `dict()` constructor. Here’s a breakdown of how it works:

# 1. **`sorted(di.items(), key=lambda item: item[1], reverse=True)`**: This sorts `di.items()` (a list of key-value pairs) by the values, in descending order. The result is a **list of tuples**, where each tuple is a `(key, value)` pair from the dictionary.

#    For example, if `di` was `{1: 3, 2: 3, 3: 3, 4: 2, 5: 1}`, then:
#    ```python
#    sorted(di.items(), key=lambda item: item[1], reverse=True)
#    ```
#    would return:
#    ```python
#    [(1, 3), (2, 3), (3, 3), (4, 2), (5, 1)]
#    ```

# 2. **`dict(...)`**: Wrapping this sorted list of tuples with `dict()` converts it back into a dictionary. The `dict()` constructor takes an iterable of key-value pairs and creates a dictionary from it.

# So, the sorted result is a list of tuples, which is then converted back to a dictionary by `dict()`.

# ### Why `sorted(di)` Alone Returns Only Keys
# When you use `sorted(di)`, it sorts just the **keys** by default, because `di` itself represents an iterable of keys. 

# But when you use `sorted(di.items(), key=lambda item: item[1])`, you’re explicitly sorting the key-value pairs, allowing `dict()` to construct a new dictionary from the sorted tuples.

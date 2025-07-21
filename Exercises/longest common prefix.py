def longest_common_prefix():
    # str_list = ["fire", "firefly", "five"]
    str_list = ["dog", "racecar", "car"]

    index = 1
    flag = True
    common_prefix = []
    
    while(flag):
        common_prefix.append(str_list[0][:index])
        for word in str_list:
            if word[:index] == ''.join(common_prefix):
                continue
            else:
                flag = False
                break
        common_prefix.clear()
        index += 1
    common_prefix.append(str_list[0][:index-2])
    return ''.join(common_prefix)

print(longest_common_prefix())

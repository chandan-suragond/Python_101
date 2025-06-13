# code to check for common elements between two lists with exception handling for 3 tries

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
output_list = []
counter = 1

try:
    while(counter<=3):
        print(f"Check {counter}")
        for i in list_a:
            if i in list_b and i not in output_list:
                output_list.append(i)
        if output_list:
            break
        else:
            counter += 1
    if not output_list:
        raise Exception
except:
    print('No common elements')
finally:
    print(f"Output list: {output_list}")

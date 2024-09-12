def beautifulDays(i, j, k):
    beautdays = 0
    days = range(i, j+1)
    beautdays = list(filter(lambda x: abs(x - int(''.join(reversed(str(x)))))%k == 0, days))
    return len(beautdays)
    
print(beautifulDays(13, 45, 3))

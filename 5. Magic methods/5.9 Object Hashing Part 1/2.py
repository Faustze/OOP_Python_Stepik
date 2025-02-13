def hash_function(obj):
    s = str(obj)
    length = len(s)
    
    temp1 = 0
    for i in range((length + 1) // 2):
        if i == length - i - 1:  
            temp1 += ord(s[i])
        else:
            temp1 += ord(s[i]) * ord(s[length - i - 1])
    
    temp2 = 0
    for i in range(length):
        if i % 2 == 0:
            temp2 += ord(s[i]) * (i + 1)
        else:
            temp2 -= ord(s[i]) * (i + 1)
    
    return (temp1 * temp2) % 123456791
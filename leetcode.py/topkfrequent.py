def topkfrequent(nums, k):
    dictionary = {}
    output =[]
        
    for i in nums:
        if i in dictionary:
            dictionary[i] +=1
        else:
            dictionary[i] = 1
    
    for _ in range(k):
        maximum = 0
        for i in dictionary:
            if dictionary[i] > maximum:
                value = i
                maximum = dictionary[i]
        output.append(value)
        del dictionary[value]
    return output
print(topkfrequent([1,1,1,2,2,3],2))
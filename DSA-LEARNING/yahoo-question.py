def yahoo(array, target, sum, cur_array, output):
    for i in array:
        sum+=i
        if sum == target:
            cur_array.append(i)
            output.append(cur_array.copy())
        elif sum > target:
            cur_array.append(i)
        else:
            cur_array.append(i)
            yahoo(array, target, sum, cur_array,output)
        sum-=cur_array[-1]
        cur_array.pop()
    return output
output = yahoo([1],8,0,[],[])
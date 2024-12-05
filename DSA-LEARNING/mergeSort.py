def mergeSort(array):
    if len(array) == 1:
        return array
    
    l,r = 0, len(array)-1
    mid = (l+r)//2

    left = mergeSort(array[l:mid+1])

    right = mergeSort(array[mid+1:])
    
    return merge(left, right)


def merge(left, right):
    output = []
    l,r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            output.append(left[l])
            l += 1
        else:
            output.append(right[r])
            r += 1
    if l < len(left):
        output += left[l:]
    if r < len(right):
        output += right[r:]
    return output


array = [9,8,7,6,5,4,3,2,1]
print(mergeSort(array))
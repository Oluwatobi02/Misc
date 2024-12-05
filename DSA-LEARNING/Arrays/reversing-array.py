# Reversing an Array
lst = [1,2,3]
def reverse_array_by_swapping(array):
    i = 0
    length = len(array)-1
    while i < len(array)//2:
        array[i], array[length-i] = array[length-i], array[i]
        i +=1
    return array

print(reverse_array_by_swapping(lst))

def reverse_array_by_two_pointer(array):
    l,r = 0, len(array)-1
    while l < r:
        array[l], array[r] = array[r], array[l]
        l, r = l+1, r-1
    return array

print(reverse_array_by_two_pointer(lst))
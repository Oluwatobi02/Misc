#Rotating an Array
lst = [1,2,3,4,5,6,7,8]
print(lst)
d = 1
def rotate(array, d):
    temp_array = [i for i in array[d:]]
    for i in array[:d]:
        temp_array.append(i)
    i = 0
    while i < len(array):
        array[i] = temp_array[i]
        i+=1
    return array
def rot(array, t):
    for _ in range(t):
        rotate(array, 1)
    return array

print(rot(lst, 3))

def rotate_by_swapping_one(array, d):
    for _ in range(d):
        for i in range(len(array)-1):
            array[i], array[i+1] = array[i+1], array[i]
    return array
print(rotate_by_swapping_one(lst, 3))
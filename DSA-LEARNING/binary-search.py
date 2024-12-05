def binarySearch(arr, target):
    l, r = 0, len(arr)-1
    while l < r:
        mid = (l+r)//2
        if arr[mid] == target:
            return [mid, arr[mid]]
        elif arr[mid] < target:
            l = mid+1
        else:
            r = mid
print(binarySearch([2,6,8,9,11,15,18],8))
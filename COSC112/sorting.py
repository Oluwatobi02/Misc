arrays = [1, 4, 2, 5, 18, 3, 2, 7, 6, 10]

def selection_sort(array):
  for i in range(len(array)-1):
    min = i
    for j in range(i+1, len(array)):
      if array[j] < array[min]:
        min = j
    if min != i:
      array[min], array[i] = array[i], array[min]

  return array
# print(selection_sort(arrays))


def bubble_sort(array):
  for i in range(len(array)-1):
    for j in range(0, len(array)-1-i):
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]
  return array
# print(bubble_sort(arrays))



def insertion_sort(array):
  for i in range(1, len(array)):
    curNum = array[i]
    for j in range(i-1, -1 , -1):
      if array[j] > curNum:
        array[j+1] = array[j]
      else:
          array[j+1] = curNum
          break
  return array

print(insertion_sort(arrays))





def merge_sort(array, left, right):
  if left >= right:
    return
  
  mid = (left + right) //2

  merge_sort(array, left, mid)
  merge_sort(array, mid+1, right)

  merge(array, left, mid, right)

def merge(lst, left, mid, right):
  l,r = 0, 0

  sorted_counter= left
  left_cpy = lst[left:mid+1]
  right_cpy = lst[mid+1:right+1]

  while l < len(left_cpy) and r < len(right_cpy):
    if left_cpy[l] < right_cpy[r]:
      lst[sorted_counter] = left_cpy[l]
      l+=1
    else:
      lst[sorted_counter] = right_cpy[r]
      r+=1
    sorted_counter+=1

  while l < len(left_cpy):
    lst[sorted_counter] = left_cpy[l]
    l+=1
    sorted_counter+=1

  while r < len(right_cpy):
    lst[sorted_counter] = right_cpy[r]
    r+=1 
    sorted_counter+=1


# print(merge(arrays, 0, (0+(len(arrays)-1)//2),len(arrays)-1))
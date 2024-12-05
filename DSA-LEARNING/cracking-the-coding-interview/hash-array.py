ARRAY_SIZE = 5



class Node:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def is_empty(self):
        return self.head == None
        

    def add_new_node(self, key, value):
        if self.is_empty():
            self.head = Node(key, value)
            return True
        else:
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = Node(key, value)
            return True
        
    def find_node(self, key):
        if self.is_empty(): return None
        else:
            cur_node = self.head
            while cur_node != None:
                if cur_node.key == key:
                    return cur_node.value
                cur_node = cur_node.next
        return False
    
    def __str__(self):
        print("this is a dictionary")
    def __repr__(self) -> str:
        print("this is a linked list")
    
array = [LinkedList() for _ in range(ARRAY_SIZE)]

def hash_function(lst):
    for i in lst:
        key, value = i
        hashed_key = hash(key)
        index = hashed_key % ARRAY_SIZE
        arr_index = array[index]
        print(arr_index)
        arr_index.add_new_node(key, value)

def find_key(key):
    hashed_key = hash(key)
    index = hashed_key % ARRAY_SIZE
    arr_index = array[index]
    return arr_index.find_node(key)


lt = [('first', 1), ('second', 2), ('third', 3), ('fourth', 4), ('fifth', 5), ('sixth', 6), ('seventh', 7), ('eighth', 8), ()] 


hash_function(lt)
print(find_key('second'))

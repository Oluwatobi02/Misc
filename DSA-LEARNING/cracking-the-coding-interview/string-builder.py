# word = ['l', 'i', 'f', 'e', ' ', 'i', 's', ' ', 'g', 'o', 'o', 'd']
# n**2 complexity
def joinwords(string):
    sentence = ""
    for i in string:
        sentence += i
    return sentence

#more efficient and O(n) complexity
def joinwords(string):
    sentence = []
    for i in string:
        sentence.append(i)
    return ''.join(sentence)
# print(joinwords(word))

def isUnique(word):
    word_store = "" 
    for i in word:
        if i in word_store:
            return False
        else:
            word_store += i
    return True
44,117,132
# print(isUnique('wordr'))


def check_perm(first, second):
    if len(first) > len(second):
        max_words = first
        min_words = second
    else:
        max_words = second
        min_words = first
    for i in min_words:
        if i not in max_words:
            return False 
    return True
# print(check_perm('tobie', 'oluwatobi'))

def urlify(word):
    pass

# print(urlify("Mr John Smith"))
x, y,z,n = 1,1,1,3
output = []
# for i in range(x+1):
#     print(i)
#     for j in range(y+1):
#         print(j)
#         for k in range(z+1):
#             print(k)
#             if i+j+k != n:
#                 output.append([i, j, k])
# print(output)
# print([[i for i in range(x+1)] + [j for j in range(y+1)] + [k for k in range(z+1)]])
print([i for i in range(x+1)] [j for j in range(y+1)] [k for k in range(z+1)])

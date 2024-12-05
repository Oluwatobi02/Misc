def string_looping():
    counter = 0
    string = input('Enter a string: ')
    for i in string:
        if i in 'aeiou':
            counter+=1
    return f'you have {counter} vowels in your string'

def string_index():
    string = input('Enter your full name: ')
    last_name = ''
    for i in range(len(string)):
        if string[i] == ' ':
            last_name = string[i+1:]
            break
    return f'your last name is {last_name}'

def string_concat():
    first_name = input('Enter your first name: ')
    last_name = input('enter your last name: ')
    return f'your full name is {first_name +' ' + last_name}'

def string_slicing():
    string = input('Enter a string: ')
    length = len(string)
    mid = (length-1)//2
    return f'the first half of the string is {string[:mid+1]}  and the last part of the string is {string[mid+1:]}'

print(string_looping())
print(string_index())
print(string_concat())
print(string_slicing())
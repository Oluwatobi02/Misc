import random

textfile = open('numbers3.txt', 'w')

for i in range(101):
    textfile.writelines(f'{random.randint(1, 100)}\n')
textfile.close()


def main():
    file = open('numbers3.txt', 'r')
    i = 0
    while i < 100:
        number = file.readline()
        print(checker(number))
        i+=1
    file.close()

def checker(number):
    number = int(number)
    if number <= 20:
        return f'{number} : ineligible'
    elif number < 40:
        return f'{number} : Bronze Class'
    elif number < 64:
        return f'{number} : Silver Class'
    else:
        return f'{number} : Gold Class'


main()
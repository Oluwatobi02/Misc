def play():
    number = int(input('Enter a number: '))
    result = tripleNumber(number)
    print(result)
    

def tripleNumber(n):
    return n*3

play()
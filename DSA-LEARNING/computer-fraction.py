def computer_fraction(string):
    split_array = string.split(' ')
    num1, den1 = split_array[0].split('/')
    num2, den2 = split_array[-1].split('/')
    numerator = ((int(num2)*int(den1)) +(int( num1) * int(den2))) 
    denominator = (int(den1)*int(den2))
    return reduce(numerator, denominator)


def reduce(num, den):
    minimum = min(num,den)
    if den == 1:
        return num
    if num == 1:
        return f'{num}/{den}'
    for i in range(2, minimum+1):
        if num%i == 0 and den%i == 0:
            return reduce(int(num/i), int(den/i))
    return f'{num}/{den}'

print(computer_fraction('1/1 + 1/1'))

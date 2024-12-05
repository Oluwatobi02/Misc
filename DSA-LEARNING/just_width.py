def ddm(n, m):
    middle = (n//2) + 1
    straight = ".|."
    count = 1
    for i in range(1,n+1):
        if i < middle:
            print((straight* count).center(m-i, '-'))
            count +=2
            continue
        elif i == middle:
            print('WELCOME'.center(m, '-'))
            count -=2
        else:
            print((straight*count).center((m-i), '-'))
            count-=2

if __name__ == '__main__':
    n,m = input().split()
    print(n,m)
    ddm(int(n),int(m))
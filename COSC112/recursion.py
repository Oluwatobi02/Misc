def main():
    def recursive_call(i):
        if type(i) == int:
            output.append(i)
        else:
            for j in i:
                recursive_call(j)

    output = []
    array = [1,2,3,[9,4,7],[0, 2, 4, 6], 10, 33, 5]

    for i in array:
        recursive_call(i)
    print(output)


main()
def valid(sentences, keyword):
    output = []
    for i in sentences:
        value = True
        for j in keyword:
            if j not in i:
                value = False
        if value == True:
            output.append(i)

    return output


# print(valid(["The dog is out at night", "The dog barks at night", "Why does it bark at night, I hate this dog", "Test sentence"], ['dog', "night", "bark"]))

def lastStoneWeight(stones):
        if len(stones) == 1:
            return stones[0]
        stones.sort()
        y = stones[-1]
        x = stones[-2]
        if x == y:
            x, y == 0, 0
            stones.pop()
            stones.pop()
        elif x != y:
            y = y-x
            stones[-1] = y
            stones.pop(-2)
        return lastStoneWeight(stones)

# print(lastStoneWeight([1]))


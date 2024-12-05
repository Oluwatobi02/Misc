# Enter your code here. Read input from STDIN. Print output to STDOUT
def camelCase4(sample):
    op, second_op, word = sample.split(';')
    if word[-2:] == '()':
        word = word[:-2]
    if op == 'S':
        new_word = ""
        for index in range(len(word)):
            if word[index].upper() == word[index] and index != 0:
                new_word+= " "
            new_word += word[index].lower()
        return new_word
    else:
        new_word = ""
        i = 0
        while i < len(word):
            if word[i] == " ":
                i += 1
                new_word += word[i].upper()
            
            elif second_op == 'C' and i == 0:
                new_word+=word[i].upper()
            else:
                new_word+=word[i]
            i+=1
        if second_op == 'M':
            new_word+="()"
        return new_word
                
# 
# C;M;mouse pad
# C;C;code swarm
# S;C;OrangeHighlighter
                
                
        
print("supposed: plastic cup",camelCase4("S;M;plasticCup()"))
print(f"correct: mobilePhone",camelCase4("C;V;mobile phone"))
print("correct: CoffeeMachine",camelCase4("C;C;coffee machine"))
print("correct: large software book", camelCase4("S;C;LargeSoftwareBook"))
print("corret: whiteSheetOfPaper()", camelCase4("C;M;white sheet of paper"))
print(camelCase4("S;V;pictureFrame"))
print(camelCase4("S;V;iPad"))
print(camelCase4("C;M;mouse pad"))
print(camelCase4("C;C;code swarm"))
print(camelCase4("S;C;OrangeHighlighter"))

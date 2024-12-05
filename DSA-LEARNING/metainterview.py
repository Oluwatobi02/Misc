
def dict_checker(string, dictionary):

    if not string:
        return ""

    for i in range(1, len(string) + 1):
        if string[:i] in dictionary:
            rest_of_string = dict_checker(string[i:], dictionary)
            if rest_of_string is not None:
                if rest_of_string:
                    return string[:i] + " " + rest_of_string
                else:
                    return string[:i]
    
    return None
result = dict_checker('vwhatisfacebook', {'what','is', 'facebook', 'meta'})
print(result)
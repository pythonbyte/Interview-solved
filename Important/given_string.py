# Given a string find out whether there are the same number of letters inside of it.

def balanced(string):
    dict_word = {}

    for i in string:
        if i in dict_word:
            dict_word[i] += 1
        else:
            dict_word[i] = 1

    len_dict = len(dict_word.values())
    sum_dict = sum(dict_word.values())

    values = list(dict_word.values())

    for v in values:
        if values[0] == v:
            continue
        else:
            return False
    return True

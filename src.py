def stringReverse(string_input):
    str_list = []
    string = string_input.split()
    for word in reversed(string):
        str_list.append(word)
    return " ".join(str_list)

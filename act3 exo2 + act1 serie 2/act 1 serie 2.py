def flatten_word(w_tuple):
    result = ""
    for char, count in w_tuple:
        result += char * count
    return result

print(flatten_word([("a",2),("b",4),("a",2),("b",6),("c",1)]))


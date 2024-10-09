def duplicate_encode(word):
    # return ''.join(['(' if word.lower().count(i) >= 2 else ')' for i in word])

    res = ''
    for i in word:
        if word.lower().count(i) >= 2:
            res += '('
        else:
            res += ')'
    return res


print(duplicate_encode("din")) # "(((")
print(duplicate_encode("Success")) # ")())())"
def get_word_indices(strings: list[str]) -> dict:
    d={}
    for i in range(len(strings)):
        for j in strings[i].lower().split():
            if j not in d:
                d[j] = [i]
            else:
                d[j].append(i)
    return d



assert get_word_indices(['This is a string',
                         'test String',
                         'test',
                         'string']) == {'this': [0], 'is': [0], 'a': [0],
                                        'string': [0, 1, 3], 'test': [1, 2]}
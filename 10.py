def longest_word_in_file(file_name: str) -> str:
    file = open(file_name, mode='r', encoding='utf-8')
    from string import punctuation
    max=''
    for line in file:
        words=line.split()
        for word in words:
            s=word.strip(punctuation)
            if len(s)>=len(max):
                max=s
    return max
print(longest_word_in_file('range_4.txt'))
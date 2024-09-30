import json
with open('Abracadabra__1_.txt', encoding='utf-8') as abra, open('Alphabet.json', encoding='utf-8') as alph:
    data = json.load(alph)
    text = abra.read()
    for i in text:
        print(data.setdefault(i, i), end='')
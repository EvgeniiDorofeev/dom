def make_header(text:str, num:int=1):
    s = '<h' + str(num)+'>'+str(text)+'</h' + str(num)+'>'
    #print(s)
    return s

make_header('Нет') == '<h1>Нет</h1>'
make_header('Bella Ciao', 4) == '<h4>Bella Ciao</h4>'
make_header('Go little rock star', 6) == '<h6>Go little rock star</h6>'
make_header('Девальвации не будет. Твердо и четко') == '<h1>Девальвации не будет. Твердо и четко</h1>'
# объявление функции
def replace(text: str, old: str, new: str = ''):

    text=text.replace(old, new)
    return text

replace('Нет', 'т') == 'Не'
replace('Bella Ciao', 'a') == 'Bell Cio'
replace('nobody; i myself farewell analysis', 'l', 'z') == 'nobody; i mysezf farewezz anazysis'
replace('commend me to my kind lord meaning', 'M', 'w') == 'commend me to my kind lord meaning'
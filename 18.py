import json
with open('manager_sales.json','r') as file:
    data=json.load(file)
    print(data)
s=0
for i in data:
    summa=0
    for j in i['cars']:
        summa=j['price']+summa
    k=summa
    if k>s:
        s=k
        first_name=i['manager']['first_name']
        last_name=i['manager']['last_name']

print(first_name, last_name, s)

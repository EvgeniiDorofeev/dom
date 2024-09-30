import json
with open('group_people.json','r') as file:
    data=json.load(file)
    print(data)
k=0
for i in data:
    s=0
    #print(i['people'])
    for j in i['people']:
        print(j)
        if j['gender']=='Female' and j['year']>1977:
            s= s+1
    print(s)
    if s>k:
        k=s
        t=i['id_group']
print(t, k)

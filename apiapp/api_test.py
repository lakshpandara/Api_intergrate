import requests

name_list = []
home_list = []
resp = requests.get('https://api.covid19api.com/countries')
data = resp.json()
dataa = resp.json()
#print(data[1]['league'])


for i in range(248):
    x = data[i]['Country']
    y = dataa[i]['Slug']
    name_list.append(x)
    home_list.append(y)
    print(x,end=' ')
    print(y)
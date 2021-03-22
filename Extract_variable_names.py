import json

with open('annotations.json') as json_file:
    data = json.load(json_file)

list_color = []
for i in range(100000):
    if data[i]['type'] == ('vbar_categorical' or 'hbar_categorical'):
        for j in range(len(data[i]['models'][0]['labels'])):
            if data[i]['models'][0]['labels'][j] not in list_color:
                list_color.append(data[i]['models'][0]['labels'][j])
                print(data[i]['models'][0]['labels'][j])

    if data[i]['type'] == ('line' or 'dot_line'):
        for j in range(len(data[i]['models'])):
            if data[i]['models'][j]['name'] not in list_color:
                list_color.append(data[i]['models'][j]['name'])
                print(data[i]['models'][j]['name'])

    if data[i]['type'] == 'pie':
        for j in range(len(data[i]['models'])):
            if data[i]['models'][j]['name'] not in list_color:
                list_color.append(data[i]['models'][j]['name'])
                print(data[i]['models'][j]['name'])

with open('variable_names.txt', 'w') as outfile:
    json.dump(list_color, outfile, indent=4)
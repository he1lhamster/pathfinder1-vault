import csv

r_file = open('conditions.csv', newline="", encoding='utf-8-sig')
reader = csv.DictReader(r_file, delimiter=';')

conditions = []

for i in reader: 
    if i:
        j = i['name']
        conditions.append({'name': j.split(': ')[0], 'text':  j.split(': ')[1]})


for c in conditions:
    output = ''
    name = c['name']
    text = c['text'].replace('\n','\n  ')
    output = f"---\nname: {name}\ntext:\n  \"{text}\"\n---\n\n"
    output += f"# {name}\n{text}"

    with open(f'conditions/{name}.md', 'w', encoding='utf-8-sig') as f:
        f.write(output)


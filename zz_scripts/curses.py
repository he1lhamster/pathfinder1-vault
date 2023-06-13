import csv

r_file = open('curses.csv', newline="", encoding='utf-8-sig')
reader = csv.DictReader(r_file, delimiter=';')

curses = []

for i in reader: 
    if i:
        name = i['Name']
        type = i['Type']
        save = i['Save']
        onset = i['Onset']
        frequency = i['Frequency']
        effect = i['Effect'].replace('\n','\n  ')
        cure = i['Cure']

    output = f"---\nname: {name}\ntype: {type}\nsave: {save}\nonset: {onset}\nfrequency: {frequency}\neffect:\n  \"{effect}\"\ncure: {cure}\n---\n"

    output += f"\n# {name}\n *Type:* {type}\n*Save: * {save} "
    if onset: output += f"* Onset:* {onset}; "
    if frequency: output += f" *Frequency*: {frequency}; "
    if cure: output += f" *Cure:* {cure}; "

    output += f'\n*Effect: * {effect}'


    with open(f'curses/{name}.md', 'w', encoding='utf-8-sig') as f:
        f.write(output)



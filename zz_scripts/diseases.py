import csv

r_file = open('diseases.csv', newline="", encoding='utf-8-sig')
reader = csv.DictReader(r_file, delimiter=';')

diseases = []

for i in reader: 
    if i:
        name = i['Name']
        type = i['Type']
        fortitude = i['Fortitude']
        onset = i['Onset']
        frequency = i['Frequency']
        effect = i['Effect'].replace('\n','\n  ')
        cure = i['Cure']

    output = f"---\nname: {name}\ntype: {type}\nfortitude: {fortitude}\nonset: {onset}\nfrequency: {frequency}\neffect:\n  \"{effect}\"\ncure: {cure}\n---\n"

    output += f"\n# {name}\n *Type:* {type}\n*Fortitude: * {fortitude} "
    if onset: output += f"*Onset:* {onset}; "
    if frequency: output += f"*Frequency*: {frequency}; "
    if cure: output += f"*Cure:* {cure};"

    output += f'\n*Effect: * {effect}'


    with open(f'diseases/{name}.md', 'w', encoding='utf-8-sig') as f:
        f.write(output)



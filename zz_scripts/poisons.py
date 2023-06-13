import csv

r_file = open('poisons.csv', newline="", encoding='utf-8-sig')
reader = csv.DictReader(r_file, delimiter=';')

poisons = []

for i in reader: 
    if i:
        name = i['Poison']
        type = i['Type']
        fortitude = i['Fort DC']
        onset = i['Onset']
        frequency = i['Frequency']
        effect = i['Effect'].replace('\n','\n  ')
        cure = i['Cure']
        price = i['Price']

    output = f"---\nname: {name}\ntype: {type}\nfortitude: {fortitude}\nonset: {onset}\nfrequency: {frequency}\neffect:\n  \"{effect}\"\ncure: {cure}\nprice: {price}\n---\n"

    output += f"\n# {name}\n *Type:* {type}\n*Fortitude: * {fortitude} "
    if onset: output += f"* Onset:* {onset}; "
    if frequency: output += f" *Frequency*: {frequency}; "
    if cure: output += f" *Cure:* {cure}; "

    output += f'\n*Effect: * {effect}'
    output += f'\n*Price: * {price}'


    with open(f'poisons/{name}.md', 'w', encoding='utf-8-sig') as f:
        f.write(output)

#         poisons.append({'name': name,
#                        'type': type,
#                        'fortitude': save,
#                        'onset': onset,
#                        'frequency': frequency,
#                        'effect': effect,
#                        'cure': cure,
#                       }
#                      )


# for c in poisons:
   


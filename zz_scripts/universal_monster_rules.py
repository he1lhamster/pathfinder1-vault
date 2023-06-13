import csv

# r_file = open('monsters.csv', newline="", encoding='utf-8-sig')
# reader = csv.DictReader(r_file, delimiter=';')
reader = open('m_rules.txt', 'r', encoding='utf-8-sig')

monsters = []
signs = ['Su)', 'Ex)', 'Sp)']
rule = {
    'header': '',
    'type': '',
    'text': '',
    'format': '',
}

head = 0
formats = 0
t_count = 0
header = ''
text = ''

for count, i in enumerate(reader):
    i = i.replace(u'\xa0', u' ').replace('[MA]','_MA_').strip()

    if not i:
        continue

    for s in signs: # search for header
        if i.endswith(s):
            header, type_abil = i.split(' (')
            type_abil = '(' + type_abil
            break
    else:
        if '_Format:_' in i:
            format_abil = i
            text = text.replace('\n','\n  ')
            format_abil = format_abil.replace('\n','\n  ')
            output = f"---\nname: {header}\ntype: {type}\ntext:\n  \"{text}\"\nformat:\n  \"{format_abil}\"\n---\n "
            output += f'\n# {header} {type_abil}'\
                        f'\n{text}\n\n{format_abil}'
            with open(f'universal monster rules/{header}.md','w') as f:
                f.write(output)

            text = ''
            header = ''
            type_abil = ''
            format_abil = ''
        else:
            text += i

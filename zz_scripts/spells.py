import csv
import re
from functools import reduce
from html5lib_to_markdown import transform
import add_links

rating_colors = {
    '5' : 'purple', # 800080
    '4' : 'blue', # 0000FF
    '3' : 'green', #008000
    '2' : 'orange', # FFA500
    '1' : 'red', # FF0000
    '0' : 'black' # 000000
}


def template_spell(d:dict) -> str:
    out = f"# <font style='color:{rating_colors[d['spell_rating']]}'>{d['name']}</font> \n**School:** {d['school']} "
    if d['subschool']: out += f"({d['subschool']}) "
    if d['descriptor']: out += f"[{d['descriptor']}] "
    out += '\n'

    for cl in ['arcanist', 'wizard', 'sorcerer', 'witch', 'magus', 'bard', 'skald', 'summoner', 'unsummoner', 'bloodrager', 'shaman', 'druid', 'hunter', 'ranger', 'cleric', 'oracle', 'warpriest', 'inquisitor', 'antipaladin', 'paladin', 'alchemist', 'investigator', 'psychic', 'mesmerist', 'occultist', 'spiritualist', 'medium',] :
        if d[cl]:
            out += f"_{cl}_ {d[cl]}, "

    out += f"\n#### Casting\n**Casting Time:** {d['cast_time']}\n **Components:** {d['components']} "
    if d['material_components']: out += f"{d['material_components']}"

    out += f"\n #### Effects\n"
    if d['targets']: out += f"**Targets:** {d['targets']}\n"
    if d['area']: out += f"**Area:** {d['area']}\n"
    if d['range']: out += f"**Range:** {d['range']}\n"
    if d['duration']: out += f"**Duration:** {d['duration']}\n"
    if d['effect']: out += f"**Effect:** {d['effect']}\n"
    if d['saving_throw']: out += f"**Saving Throw:** {d['saving_throw']}; "
    if d['spell_resistance']: out += f"**Spell Resistance:** {d['spell_resistance']}; "

    text_with_links = add_links.replace_in_text(d['text'])
    out += f"\n #### Description\n{text_with_links}\n"
    # out += f"\n #### Description\n{d['text']}\n"

    out += f"\n #### Other\n**Source:** {d['source']}\n**Rating:** {d['spell_rating']}\n"

    if d['permanency']: out += f"**Permanency:** Yes\n"
    if d['potion'] != '0': out += f"**Potion:** Yes\n"
    if d['cleric_domain']: out += f"**Domain:** {d['cleric_domain']}; "
    if d['bloodline']: out += f"**Bloodline:** {d['bloodline']}; "
    if d['patron']: out += f"**Patron:** {d['patron']}; "

    return out


def write_file(d:dict) -> None:
    output = '---\n'
    for k, v in d.items():
        if k == 'text':
            output += f'{k}: |\n  "{v}"\n'
        else:
            output += f'{k}: "{v}"\n'
    output += f"rated_name: <font style='color:{rating_colors[d['spell_rating']]}'>{d['name']}</font>\n"
    output += '---\n\n'
    if '/' in d['name']: d['name'] = d['name'].replace('/','-')

    with open(f"spells/{d['name']}.md", 'w') as f:
        print(d['name'])
        f.write(output)
        f.write(template_spell(d))


spells_csv = open('spells.csv', newline="", encoding='utf-8-sig')
reader = csv.DictReader(spells_csv, delimiter=';')
full_spell = {sp['name'].lower() : sp for sp in reader}

only_spells = [
               "corpse hammer",
               "grand curse",
               "mage's evasion",
               "cone of slime",
               "chant",
              ]

r_codex = open('pf1codex.csv', newline="", encoding='utf-8-sig')
reader_2 = csv.DictReader(r_codex, delimiter=';')
codex_spell = {sp['name'].lower() : sp for sp in reader_2}
only_codex = []
with open('only_codex.txt', 'r') as f_codex:
    for i in f_codex:
        only_codex.append(i[:-1])


for i in full_spell:
    d = {
    'name' : '',
    'spell_rating' : '',
    'school' : '',
    'subschool' : '',
    'descriptor' : '',
    'cast_time' : '',
    'components' : '',
    'material_components' : '',
    'range' : '',
    'area' : '',
    'effect' : '',
    'targets' : '',
    'duration' : '',
    'saving_throw' : '',
    'spell_resistance' : '',
    'short_text' : '',
    'text' : '',
    'source' : '',
    'permanency' : '',
    'potion' : '',
    'race' : '',
    'deity' : '',
    'cleric_domain' : '',
    'druid_domain' : '',
    'bloodline' : '',
    'patron' : '',
    'arcanist' : '',
    'wizard' : '',
    'sorcerer' : '',
    'witch' : '',
    'magus' : '',
    'bard' : '',
    'skald' : '',
    'summoner' : '',
    'unsummoner' : '',
    'bloodrager' : '',
    'shaman' : '',
    'druid' : '',
    'hunter' : '',
    'ranger' : '',
    'cleric' : '',
    'oracle' : '',
    'warpriest' : '',
    'inquisitor' : '',
    'antipaladin' : '',
    'paladin' : '',
    'alchemist' : '',
    'investigator' : '',
    'psychic' : '',
    'mesmerist' : '',
    'occultist' : '',
    'spiritualist' : '',
    'medium' : '',
        }

    if i in only_spells:
        continue

    d['name'] = full_spell[i]['name']
    d['spell_rating'] = codex_spell[i]['rating']
    d['school'] = full_spell[i]['school']
    d['subschool'] = full_spell[i]['subschool']
    d['descriptor'] = full_spell[i]['descriptor']
    d['cast_time'] = full_spell[i]['casting_time']
    d['components'] = full_spell[i]['components']
    d['material_components'] = ''

    b = re.findall(r'\([A-Za-z0-9, +-]*\)', full_spell[i]['components'])
    if b:
        d['material_components'] = reduce(lambda x,y: x+y, b).replace('(','{').replace(')','}')
    else: d['material_components'] = ''

    d['range'] = full_spell[i]['range']
    d['area'] = full_spell[i]['area']
    if full_spell[i]['shapeable'] == '1' and '(S)' not in d['area']:
        d['area'] += ' (S)'

    d['effect'] = full_spell[i]['effect']
    d['targets'] = full_spell[i]['targets']
    d['duration'] = full_spell[i]['duration']
    if full_spell[i]['dismissible'] == '1' and '(D)' not in d['duration']:
        d['duration'] += ' (D)'

    d['saving_throw'] = full_spell[i]['saving_throw']
    d['spell_resistance'] = full_spell[i]['spell_resistance']
    d['text'] = full_spell[i]['description_formatted']
    d['text'] = d['text'].replace('</p><p>', '\n  ').replace('<p>', '').replace('</p>', '')
    d['text'] = transform(d['text']).replace('\n', '\n  ').replace('__', '_')
    d['short_text'] = full_spell[i]['short_description'] if full_spell[i]['short_description'] else d['text'][:80]
    d['source'] = full_spell[i]['source']
    d['permanency'] = codex_spell[i]['permanency']

    d['potion'] = codex_spell[i]['potion']
    d['race'] = codex_spell[i]['race']
    d['deity'] = codex_spell[i]['deity']
    d['cleric_domain'] = codex_spell[i]['cleric_domain']
    d['druid_domain'] = codex_spell[i]['druid_domain']
    d['bloodline'] = codex_spell[i]['bloodline']
    d['patron'] = codex_spell[i]['patron']

    d['arcanist'] = codex_spell[i]['arcanist']
    d['wizard'] = codex_spell[i]['wizard']
    d['sorcerer'] = codex_spell[i]['sorcerer']
    d['witch'] = codex_spell[i]['witch']
    d['magus'] = codex_spell[i]['magus']
    d['bard'] = codex_spell[i]['bard']
    d['skald'] = codex_spell[i]['skald']
    d['summoner'] = codex_spell[i]['summoner']
    d['unsummoner'] = codex_spell[i]['unsummoner']
    d['bloodrager'] = codex_spell[i]['bloodrager']
    d['shaman'] = codex_spell[i]['shaman']
    d['druid'] = codex_spell[i]['druid']
    d['hunter'] = codex_spell[i]['hunter']
    d['ranger'] = codex_spell[i]['ranger']
    d['cleric'] = codex_spell[i]['cleric']
    d['oracle'] = codex_spell[i]['oracle']
    d['warpriest'] = codex_spell[i]['warpriest']
    d['inquisitor'] = codex_spell[i]['inquisitor']
    d['antipaladin'] = codex_spell[i]['antipaladin']
    d['paladin'] = codex_spell[i]['paladin']
    d['alchemist'] = codex_spell[i]['alchemist']
    d['investigator'] = codex_spell[i]['investigator']
    d['psychic'] = codex_spell[i]['psychic']
    d['mesmerist'] = codex_spell[i]['mesmerist']
    d['occultist'] = codex_spell[i]['occultist']
    d['spiritualist'] = codex_spell[i]['spiritualist']
    d['medium'] = codex_spell[i]['medium']
    write_file(d)


for i in only_spells:
    d = {
    'name' : '',
    'spell_rating' : '',
    'school' : '',
    'subschool' : '',
    'descriptor' : '',
    'cast_time' : '',
    'components' : '',
    'material_components' : '',
    'range' : '',
    'area' : '',
    'effect' : '',
    'targets' : '',
    'duration' : '',
    'saving_throw' : '',
    'spell_resistance' : '',
    'text' : '',
    'permanency' : '',
    'potion' : '',
    'race' : '',
    'deity' : '',
    'cleric_domain' : '',
    'druid_domain' : '',
    'bloodline' : '',
    'patron' : '',
    'arcanist' : '',
    'wizard' : '',
    'sorcerer' : '',
    'witch' : '',
    'magus' : '',
    'bard' : '',
    'skald' : '',
    'summoner' : '',
    'unsummoner' : '',
    'bloodrager' : '',
    'shaman' : '',
    'druid' : '',
    'hunter' : '',
    'ranger' : '',
    'cleric' : '',
    'oracle' : '',
    'warpriest' : '',
    'inquisitor' : '',
    'antipaladin' : '',
    'paladin' : '',
    'alchemist' : '',
    'investigator' : '',
    'psychic' : '',
    'mesmerist' : '',
    'occultist' : '',
    'spiritualist' : '',
    'medium' : '',
        }

    d['name'] = full_spell[i]['name']
    d['spell_rating'] = '0'
    d['school'] = full_spell[i]['school']
    d['subschool'] = full_spell[i]['subschool']
    d['descriptor'] = full_spell[i]['descriptor']
    d['cast_time'] = full_spell[i]['casting_time']
    d['components'] = full_spell[i]['components']
    d['material_components'] = ''

    b = re.findall(r'\([A-Za-z0-9, +-]*\)', full_spell[i]['components'])
    if b:
        d['material_components'] = reduce(lambda x,y: x+y, b).replace('(','{').replace(')','}')
    else: d['material_components'] = ''

    d['range'] = full_spell[i]['range']
    d['area'] = full_spell[i]['area']
    if full_spell[i]['shapeable'] == '1' and '(S)' not in d['area']:
        d['area'] += ' (S)'

    d['effect'] = full_spell[i]['effect']
    d['targets'] = full_spell[i]['targets']
    d['duration'] = full_spell[i]['duration']
    if full_spell[i]['dismissible'] == '1' and '(D)' not in d['duration']:
        d['duration'] += ' (D)'

    d['saving_throw'] = full_spell[i]['saving_throw']
    d['spell_resistance'] = full_spell[i]['spell_resistance']
    d['text'] = full_spell[i]['description_formatted']
    d['text'] = d['text'].replace('</p><p>', '\n  ').replace('<p>', '').replace('</p>', '')
    d['text'] = transform(d['text']).replace('\n', '\n  ').replace('__', '_')
    d['short_text'] = full_spell[i]['short_description'] if full_spell[i]['short_description'] else d['text'][:80]

    d['source'] = full_spell[i]['source']

    d['cleric_domain'] = full_spell[i]['domain']
    d['druid_domain'] = full_spell[i]['domain']
    d['bloodline'] = full_spell[i]['bloodline']
    d['patron'] = full_spell[i]['patron']

    d['arcanist'] = full_spell[i]['wiz']
    d['wizard'] = full_spell[i]['wiz']
    d['sorcerer'] = full_spell[i]['sor']
    d['witch'] = full_spell[i]['witch']
    d['magus'] = full_spell[i]['magus']
    d['bard'] = full_spell[i]['bard']
    d['skald'] = full_spell[i]['skald']
    d['summoner'] = full_spell[i]['summoner']
    d['unsummoner'] = full_spell[i]['summoner_unchained']
    d['bloodrager'] = full_spell[i]['bloodrager']
    d['shaman'] = full_spell[i]['shaman']
    d['druid'] = full_spell[i]['druid']
    d['hunter'] = full_spell[i]['hunter']
    d['ranger'] = full_spell[i]['ranger']
    d['cleric'] = full_spell[i]['cleric']
    d['oracle'] = full_spell[i]['cleric']
    try:
        if int(d['cleric']) <= 6:
            d['warpriest'] = full_spell[i]['cleric']
    except: pass
    d['inquisitor'] = full_spell[i]['inquisitor']
    d['antipaladin'] = full_spell[i]['antipaladin']
    d['paladin'] = full_spell[i]['paladin']
    d['alchemist'] = full_spell[i]['alchemist']
    d['investigator'] = full_spell[i]['investigator']
    d['psychic'] = full_spell[i]['psychic']
    d['mesmerist'] = full_spell[i]['mesmerist']
    d['occultist'] = full_spell[i]['occultist']
    d['spiritualist'] = full_spell[i]['spiritualist']
    d['medium'] = full_spell[i]['medium']

    write_file(d)


for i in only_codex:
    d = {
    'name' : '',
    'spell_rating' : '',
    'school' : '',
    'subschool' : '',
    'descriptor' : '',
    'cast_time' : '',
    'components' : '',
    'material_components' : '',
    'range' : '',
    'area' : '',
    'effect' : '',
    'targets' : '',
    'duration' : '',
    'saving_throw' : '',
    'spell_resistance' : '',
    'text' : '',
    'permanency' : '',
    'potion' : '',
    'race' : '',
    'deity' : '',
    'cleric_domain' : '',
    'druid_domain' : '',
    'bloodline' : '',
    'patron' : '',
    'arcanist' : '',
    'wizard' : '',
    'sorcerer' : '',
    'witch' : '',
    'magus' : '',
    'bard' : '',
    'skald' : '',
    'summoner' : '',
    'unsummoner' : '',
    'bloodrager' : '',
    'shaman' : '',
    'druid' : '',
    'hunter' : '',
    'ranger' : '',
    'cleric' : '',
    'oracle' : '',
    'warpriest' : '',
    'inquisitor' : '',
    'antipaladin' : '',
    'paladin' : '',
    'alchemist' : '',
    'investigator' : '',
    'psychic' : '',
    'mesmerist' : '',
    'occultist' : '',
    'spiritualist' : '',
    'medium' : '',
        }

    d['name'] = codex_spell[i]['name']
    d['spell_rating'] = codex_spell[i]['rating']
    d['school'] = codex_spell[i]['school']
    d['subschool'] = codex_spell[i]['subschool']
    d['descriptor'] = ''
    d['cast_time'] = codex_spell[i]['casting_time']

    if codex_spell[i]['verbal']: d['components'] += 'V, '
    if codex_spell[i]['somatic']: d['components'] += 'S, '
    if codex_spell[i]['material_components']: d['components'] += 'M, '
    if codex_spell[i]['focus']: d['components'] += 'F, '
    if codex_spell[i]['divine_focus']: d['components'] += 'DF'
    if d['components'].endswith(', '): d['components'] = d['components'][:-2]

    d['material_components'] = codex_spell[i]['component_costs']

    d['range'] = codex_spell[i]['range']
    d['area'] = codex_spell[i]['area']
    if codex_spell[i]['shapeable'] == '1' and '(S)' not in d['area']:
        d['area'] += ' (S)'

    d['effect'] = codex_spell[i]['effect']
    d['targets'] = codex_spell[i]['targets']
    d['duration'] = codex_spell[i]['duration']
    if codex_spell[i]['dismissible'] == '1' and '(D)' not in d['duration']:
        d['duration'] += ' (D)'

    d['saving_throw'] = codex_spell[i]['saving_throw']
    d['spell_resistance'] = codex_spell[i]['spell_resistance']
    d['text'] = codex_spell[i]['description']
    d['short_text'] = codex_spell[i]['description'][:80]
    d['source'] = codex_spell[i]['source']

    d['permanency'] = codex_spell[i]['permanency']
    d['potion'] = codex_spell[i]['potion']
    d['race'] = codex_spell[i]['race']
    d['deity'] = codex_spell[i]['deity']
    d['cleric_domain'] = codex_spell[i]['cleric_domain']
    d['druid_domain'] = codex_spell[i]['druid_domain']
    d['bloodline'] = codex_spell[i]['bloodline']
    d['patron'] = codex_spell[i]['patron']
    d['arcanist'] = codex_spell[i]['arcanist']
    d['wizard'] = codex_spell[i]['wizard']
    d['sorcerer'] = codex_spell[i]['sorcerer']
    d['witch'] = codex_spell[i]['witch']
    d['magus'] = codex_spell[i]['magus']
    d['bard'] = codex_spell[i]['bard']
    d['skald'] = codex_spell[i]['skald']
    d['summoner'] = codex_spell[i]['summoner']
    d['unsummoner'] = codex_spell[i]['unsummoner']
    d['bloodrager'] = codex_spell[i]['bloodrager']
    d['shaman'] = codex_spell[i]['shaman']
    d['druid'] = codex_spell[i]['druid']
    d['hunter'] = codex_spell[i]['hunter']
    d['ranger'] = codex_spell[i]['ranger']
    d['cleric'] = codex_spell[i]['cleric']
    d['oracle'] = codex_spell[i]['oracle']
    d['warpriest'] = codex_spell[i]['warpriest']
    d['inquisitor'] = codex_spell[i]['inquisitor']
    d['antipaladin'] = codex_spell[i]['antipaladin']
    d['paladin'] = codex_spell[i]['paladin']
    d['alchemist'] = codex_spell[i]['alchemist']
    d['investigator'] = codex_spell[i]['investigator']
    d['psychic'] = codex_spell[i]['psychic']
    d['mesmerist'] = codex_spell[i]['mesmerist']
    d['occultist'] = codex_spell[i]['occultist']
    d['spiritualist'] = codex_spell[i]['spiritualist']
    d['medium'] = codex_spell[i]['medium']
    write_file(d)


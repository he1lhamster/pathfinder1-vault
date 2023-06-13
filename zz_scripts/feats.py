import csv
from bs4 import BeautifulSoup
from html5lib_to_markdown import transform
import os
from functools import reduce
from tqdm import tqdm
# from replace_with_links import replace_links
import add_links


tags = ['teamwork', 'critical', 'grit', 'style', 'performance', 'racial', 'companion_familiar', 'panache', 'betrayal', 'targeting', 'esoteric', 'stare', 'weapon_mastery', 'item_mastery', 'armor_mastery', 'shield_master', 'blood_hex', 'trick', ]
tags_value = ['type', 'race_name'] # need to split(',') and replace(' ', '_')


r_file = open('feats.csv', newline="", encoding='utf-8-sig')
reader = csv.DictReader(r_file, delimiter=';')
headers = reader.fieldnames

for i in tqdm(reader):
    output = ''
    feat_name = i['name']

    listdir = os.listdir('feats/')
    if f'{feat_name}.md' in listdir:
        continue

    if "Mythic" in i['type']:
        feat_name += ' Mythic'
    print(feat_name)
    
    feat_desc = BeautifulSoup(i['fulltext'], 'html.parser')
    feat_desc.link.extract()
    header = feat_desc.new_tag('h1')
    header.string = feat_desc.find('p').text
    feat_desc.find('p').replace_with(header)

    new_feat_desc = transform(str(feat_desc)).replace('##### ', '').replace(' **', '** ')
    name = new_feat_desc[:new_feat_desc.find('\n')] # exclude first line with feat name
    new_feat_desc = add_links.replace_in_text(new_feat_desc[new_feat_desc.find('\n'):])
    new_feat_desc = name + new_feat_desc

    tags_panel = ''
    for j in tags_value:
        try:
            add_tags = ['#feat/'+tag.replace(' ', '_') for tag in i[j].split(',').strip() if tag]
            tags_panel += reduce(lambda a, b: a + ', ' + b + ', ', add_tags)
        except:
            pass

    for j in tags:
        try:
            if i[j] != '0':
                new_t = j.replace(' ','_')
                tags_panel += f'#feat/{new_t}' + ', '
        except:
            pass

    source = '\n\n**Source** ' + i['source']
    
    if tags_panel:
        tags_panel = '\n>[!tags_panel]- Tags\n> ' + tags_panel

    new_feat_desc = f"---\ncssclass: [feats]\n\n---\n" + new_feat_desc
    output_file_name = f'feats/mythic/{feat_name}.md' if "Mythic" in feat_name else f'feats/{feat_name}.md'

    with open(output_file_name, 'w', encoding='utf-8-sig') as f:
        f.write(new_feat_desc)
        f.write(source)
        f.write(tags_panel)
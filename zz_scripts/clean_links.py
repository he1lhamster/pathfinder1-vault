import os
import re
from tqdm import tqdm


folder_name = 'monsters'
items = os.listdir(f'{folder_name}/')
banned = [
    'medium',
    'dodge',
    'slave',
    'deflection',

    ]

for i in tqdm(items):
    print(i)
    with open(f'{folder_name}/{i}', 'r', encoding='utf-8-sig') as file:
        text = file.read()
        old_links = re.findall(r'_\[\[.*?\]\]_', text)        
        for l in old_links:
            clean_l = l.split('|')[-1].replace(']]','').replace('_', '')
            if clean_l.lower() in banned:
                text = text.replace(l, clean_l)
                print(clean_l)
                break

    with open(f'{folder_name}/{i}', 'w', encoding='utf-8-sig') as file:
        file.write(text)

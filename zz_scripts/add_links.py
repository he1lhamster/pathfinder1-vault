'''
find patterns in text, replace it this way:
word - _[[path_to_word/Word|word]]_
'''

import json
import re

with open('all_json.json', 'r', encoding='utf-8-sig') as all_json:
    # open('banned.txt', 'r', encoding='utf-8-sig') as banned:
    all_files = json.loads(all_json.read())
    print('JSON loaded')
    # for ban in banned:
    #     if ban in all_files:
    #         print(all_files.pop(ban))

def replace_in_text(text:str) -> str:
    def clean_text(text:str) ->str:
        old_links = re.findall(r'_\[\[.*?\]\]_', text)
        for l in old_links:
            clean_l = l.split('|')[-1].replace(']]','').replace('_', '')
            text = text.replace(l, clean_l)
        text = text.replace('_', '')
        return text

    def replace_func(match):
        return f"_[[{link}|{match.group(0)}]]_"

    def replace_func_second(match): # first occurrence - link, all other just italic
        return f"_{match.group(0)}_"
    # replaced_text = text.replace('[[', '').replace(']]', '').replace('_', '')
    replaced_text = clean_text(text)

    for item in all_files:
        link = f'{all_files[item]}/{item}' # npcs/Accomplished Angler      
        regex_pattern = r'(?<![|\\\/\[\]_-])\b' + re.escape(item) + r'\b(?![|\\\/\[\]_-])'
        replaced_text = re.sub(regex_pattern, replace_func, replaced_text, count=1, flags=re.IGNORECASE)
        replaced_text = re.sub(regex_pattern, replace_func_second, replaced_text, flags=re.IGNORECASE)

    return replaced_text

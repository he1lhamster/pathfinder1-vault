import os
import json
import re

def get_files_to_dict(folder: str):
    # print('Iteration - ', folder)
    files = os.listdir(folder + '/')
    for file in files:
        if '.md' in file: # add it to all dict
            file = file.replace('.md', '')
            all_dict[file] = folder
        else: # folder case
            get_files_to_dict(f'{folder}/{file}')

def get_links_to_json():
    for fold in folders:
        get_files_to_dict(fold)

    with open('banned.txt', 'r') as banned:
        for ban in banned.read().splitlines():
            if ban in all_dict:
                print(all_dict.pop(ban))

    with open(f'all_json.json', 'w', encoding='utf-8-sig') as all_json:
        all_sorted = {k: all_dict[k] for k in sorted(all_dict.keys(), key=lambda x: len(x), reverse=True)}
        # sort dict - longest keys first
        json.dump(all_sorted, all_json)


if __name__ == '__main__':
    all_dict = {} # main dict with all links

    # manually set folders for solving same name items problem, lower - high priority
    folders = ['npcs',
               'monsters',
               'classes',
               'poisons',
               'diseases',
               'curses',
               'feats',
               'items',
               'spells',
               'conditions',
               'universal monster rules',
               ]

    get_links_to_json()
    # set_links_in_files()

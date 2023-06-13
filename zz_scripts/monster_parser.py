from bs4 import BeautifulSoup
from html5lib_to_markdown import transform
import re
from tqdm import tqdm
import add_links


#3084 NPC = 486
monster_type = 'npcs'
range_count = 486 if monster_type == 'npcs' else 3084


for i in tqdm(range(0, range_count)):
    with open(f'data_{monster_type}/{i}.html', 'r', encoding='utf-8-sig') as f:
        monster_name = str(i)
        f = re.sub(r'<sup>\w*</sup>','', f.read())

        try:
            soup = BeautifulSoup(f, "html.parser")
            table = soup.find('td').find('span')

            monster_name = table.find('h1').text.replace('/', '-').replace('"','-').replace(':','-')

            # choose all between two first h1
            for c in list(table.contents):
                if c is table.h1 or c.find_previous('h1') is table.h1:
                    continue
                c.extract()
            for h1 in table.select('h1'):
                h1.extract()

            with open('fix.txt', 'a') as fix_f:

                for spa in ['Quicken', 'Empower', 'Bouncing', 'Disruptive', 'Fearsome', 'Intensified', 'Lingering', 'Reach', 'Sickening', 'Scarring', 'Traumatic', ]:
                    for j in soup.find_all(text = re.compile(f'{spa} Spell-Like Ability')):
                        fixed = j.replace(f'{spa} Spell-Like Ability', f'_{spa} Spell-Like Ability_')
                        j.replace_with(fixed)

                for a_tag in table.find_all('a'):
                    # print(a_tag)

                    if a_tag.string:
                        if a_tag.string[-1] == ' ':
                            a_tag.string = '<i>' + str(a_tag.string).strip() + '<i> '
                        else:
                            a_tag.string = '<i>' + str(a_tag.string) + '<i>'

                    elif not 'Spell-Like Ability' in a_tag.text:                        
                        print(f"ERROR = {i} {monster_name} ---------------")
                        fix_f.write(f"{i} {monster_name}\n")                    
                    a_tag.unwrap()

            table.find('h2').decompose()

            replace_with_items = []
            treas = table.find('b', text='Treasure')           
            gear = table.find('b', text='Other Gear')
            combat_gear = table.find('b', text='Combat Gear')
  
            try:
                replace_with_items.append(treas.next_sibling)
            except: pass
            try:
                replace_with_items.append(gear.next_sibling)
            except: pass
            try:
                replace_with_items.append(combat_gear.next_sibling)
            except: pass
            # print('REPL = ', replace_with_items)

            # -------TRANSFORM from HTML to MD----------
            mid_txt = str(table)
            if '<br/>' in mid_txt:
                mid_txt = mid_txt.replace('<br/><br/>','\n\n')

            new_txt = transform(mid_txt).replace('<table>','').replace('</table>','').replace('<tbody>','').replace('</tbody>','').replace('<tr>','').replace('</tr>','').replace('<td>','').replace('</td>','').replace('&lt;i&gt;', '_').replace('\n_,', '_,').replace('вЂ™','\'').replace('<i>','_').replace('</i>','_').strip()

            new_txt = new_txt.replace('### Offense\n', '##### Offense\n').replace('### Defense\n', '##### Defense\n').replace('### Statistics\n', '##### Statistics\n').replace('### Ecology\n', '##### Ecology\n').replace('### Description\n', '##### Description\n')

            # new_txt = replace_links(new_txt)

            alignments = ['LG','NG','CG','N','NE','CN','LE','CE,','LN']
            new_txt = new_txt.replace('**Source', '\n**Source').replace('\n\n**S', '\n**S')
            
            for k in alignments:
                new_txt = new_txt.replace(f'\n{k} ', f'\n\n{k} ')

            output_yaml = '---\ncssclass: [monsters]\n'
            new_txt = add_links.replace_in_text(new_txt)

            try:
                with open(f'yaml_monsters/{monster_name}.yaml', 'r', encoding='utf-8') as yaml_monster:
                    current_monster = yaml_monster.read()
                    output_yaml += current_monster
            except: pass

            output_yaml += '\n---\n\n'
            new_txt = output_yaml + f"# {monster_name}\n" + new_txt

            with open(f'{monster_type}/{monster_name}.md', 'w', encoding='utf-8-sig') as x_file:
                    x_file.write(new_txt)
                    print('+:', monster_name, i)

        except Exception as e:
            print(f"!!{monster_name} {i} : {e}")
            break

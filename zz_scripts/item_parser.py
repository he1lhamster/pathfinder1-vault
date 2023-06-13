from bs4 import BeautifulSoup
import os
from tqdm import tqdm
import json
from html5lib_to_markdown import transform
import add_links

'''
script for converting html to MD file 
'''

#6184
for num, i in enumerate(tqdm(range(6184))):
    with open(os.path.join('items/items_parse', str(i) + ".html"), encoding='utf-8-sig') as file:

        soup = BeautifulSoup(file, "html.parser")
        result = {}
        yaml_result = {}

        current_h2_key = None
        current_h3_key = None
        current_h3_value = None

        title = soup.find('h1').get_text().strip().strip(':').replace('/','-')
        result['Title'] = title
        yaml_result['Title'] = title

        try:
            for tag in soup.find_all(['h2', 'h3', 'strong', 'p']):
                if tag.name == 'h2':
                    current_h2_key = tag.get_text().strip().strip(':')

                    if current_h2_key == 'Sources':
                        ul_tag = tag.find_next_sibling('ul')
                        result[current_h2_key] = [li.get_text().strip().strip(':') for li in ul_tag.find_all('li')]
                        yaml_result[current_h2_key] = [li.get_text().strip().strip(':') for li in ul_tag.find_all('li')]

                    elif current_h2_key in ['Description', 'Destruction']:
                        result[current_h2_key] = ''
                        yaml_result[current_h2_key] = ''
                    else:
                        result[current_h2_key] = {}
                    current_h3_key = None

                elif current_h2_key == 'Description' and tag.name != 'strong':
                    result['Description'] += str(tag)
                    yaml_result['Description'] += str(tag)

                elif current_h2_key == 'Destruction':
                    result['Destruction'] +=  str(tag)
                    yaml_result['Destruction'] += str(tag)

                elif tag.name == 'h3':
                    current_h3_key = tag.get_text().strip().strip(':')
                    result[current_h2_key][current_h3_key] = {}

                elif tag.name == 'strong' and current_h2_key != 'Description' and current_h2_key != 'Destruction':
                    if tag.get_text() == 'Cursed':
                        current_h3_value = 'True'
                    else:
                        current_h3_value = tag.next_sibling.strip().strip(':')
                    
                    current_strong_key = tag.get_text().strip().strip(':')

                    if current_h3_key:
                        result[current_h2_key][current_h3_key][current_strong_key] = current_h3_value   
                    else:
                        result[current_h2_key][current_strong_key] = current_h3_value

                    if current_strong_key == 'Type' and current_h3_key:
                        yaml_result[current_h3_key + ' Type'] = current_h3_value
                    else:
                        yaml_result[current_strong_key] = current_h3_value

            blank_keys = []
            for k, v in result.items():
                if not v: blank_keys.append(k)
            for k in blank_keys:
                result.pop(k)
 
            with open(f'items/json_items/{title}.json', 'w', encoding='UTF-8-sig') as fjs:
                fjs.write(json.dumps(result, indent=4))
           
            # ----------- write MD to file
            # yaml_result = yaml.dump(yaml_result, indent=2)

            yaml_output = '---\n'
            for k, v in yaml_result.items():
                if k == 'Description' or k == 'Destruction':
                    v = v.replace('<p>', '\n').replace('</p>', '\n')
                    yaml_output += f'{k}: |\n  "{v.strip()}"\n'
                else:
                    yaml_output += f'{k}: "{v}"\n'
                
                if k == 'Type':
                    item_type = v

            yaml_output += '---'
            yaml_output = transform(yaml_output)
            yaml_output = yaml_output.replace('Description: |\n', 'Description: |\n  ')\
                                                .replace('Destruction: |\n', 'Destruction: |\n  ')\
                                                .replace('\n\n', '\n  ')

            tag = soup.find('h1')
            content = str(tag)

            while tag.name != 'ul':
                tag = tag.next_sibling
                if tag == None:
                    break
                elif tag.name == 'em' and tag.find_next('h2').get_text() == 'See also':
                    tag = tag.find_next('h2').find_next('h2')
                    content += str(tag)
                else:
                    content += str(tag)

            content = content.replace('<strong>', ' <strong>').replace(': </strong>', ':</strong> ')
            content = transform(content).replace('\n### ','\n##### ').replace('\n## ','\n### ')
            content = content.split('### See also')[0]
            # ---------- add links here
            name = content[:content.find('\n')] # exclude first line with item name
            content = add_links.replace_in_text(content[content.find('\n'):])
            content = name + content
            # ---------- end add links
            output_md = yaml_output + '\n\n' + content

            with open(f'items/{item_type}/{title}.md', 'w', encoding='utf-8-sig') as item_out_file:
                item_out_file.write(output_md)

        except Exception as e:
            with open('items_fix.txt', 'w') as fix:
                error = f"{i} {title}: {e}"
                print(error)
                fix.write(error)
                continue

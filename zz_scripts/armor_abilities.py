from bs4 import BeautifulSoup
import requests
from html5lib_to_markdown import transform
from tqdm import tqdm


shields = []
with open ('shield_abilities.txt', 'r', encoding='utf-8-sig') as shield_abilities:
	for i in shield_abilities:
		shields.append(i.strip())

armors = []
with open ('armor_abilities.txt', 'r', encoding='utf-8-sig') as armor_abilities:
	for i in armor_abilities:
		armors.append(i.strip())

abilities = set(armors + shields)


for num, i in enumerate(tqdm(abilities)):
	try:
		i = i.strip()
		print(i)
		url = f'https://aonprd.com/MagicArmorDisplay.aspx?ItemName={i}'
		html = requests.get(url).text
		soup = BeautifulSoup(html, "html.parser")
		abil = soup.find(id="ctl00_MainContent_DataListTypes_ctl00_LabelName")

		try:
			[a.unwrap() for a in abil.find_all('a')]
			[img.unwrap() for img in abil.find_all('img')]
		except: pass

		price_b = str(abil.find('b', string='Price').next_sibling)
		price_b = price_b.strip().strip(';')


		try:
			meta_desc = soup.find('meta', {'name':'description'})

			description = transform(meta_desc['content'].replace(' </i>', '</i> ')).strip()
			description = description.replace('\n\n','\n').replace('\n','\n  ')
		except:
			description = ''

		armor_type = []
		if i in armors: armor_type.append('armor_quality')
		if i in shields: armor_type.append('shield_quality')

		output = f'---\nname: "{i}"\ntype: {armor_type}\nprice: "{price_b}"\ndescription: |\n  "{description}"\n---\n\n'
		output += transform(str(abil))

		with open(f'armor_magic_abilities/{i}.md', 'w', encoding='utf-8-sig') as w_file:
			w_file.write(output)

	except Exception as e:
		print(e)
		continue
	

	
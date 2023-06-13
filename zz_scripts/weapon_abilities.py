from bs4 import BeautifulSoup
import requests
from html5lib_to_markdown import transform
from tqdm import tqdm


with open ('weapon_abilities.txt', 'r', encoding='utf-8-sig') as abilities:

	for num, i in enumerate(tqdm(abilities)):

		try:
			i = i.strip()
			url = f'https://aonprd.com/MagicWeaponsDisplay.aspx?ItemName={i}'
			html = requests.get(url).text
			soup = BeautifulSoup(html, "html.parser")
			abil = soup.find(id="ctl00_MainContent_DataListTypes_ctl00_LabelName")

			try:
				[a.unwrap() for a in abil.find_all('a')]
				[img.unwrap() for img in abil.find_all('img')]
			except: pass

			price_b = str(abil.find('b', string='Price').next_sibling)
			price_b = price_b.strip().strip(';')

			meta_desc = soup.find('meta', {'name':'description'})
			description = transform(meta_desc['content']).strip()
			description = description.replace('\n\n','\n  ')

			output = f'---\nname: "{i}"\ntype: "weapon_quality"\nprice: "{price_b}"\ndescription: |\n  "{description}"\n---\n\n'
			output += transform(str(abil))

			with open(f'weapon_magic_abilities/{i}.md', 'w', encoding='utf-8-sig') as w_file:
				w_file.write(output)
				# print(i)

		except Exception as e:
			print(e)
			continue
		

		
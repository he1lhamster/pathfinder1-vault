---
cssclass: [monsters]
title1: River Cleric
desc_short: This holy woman wears a large pendant of a winged, two-headed cobra around
  her neck and wields a mace of similar make.
title2: River Cleric
CR: 3
sources:
- name: Osirion, Legacy of the Pharaohs
  page: 62
  link: http://paizo.com/products/btpy93n8?Pathfinder-Campaign-Setting-Osirion-Legacy-of-Pharaohs
XP: 800
race: Human
classes:
- cleric of Wadjet 4
alignment: LG
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 2
AC:
  AC: 15
  touch: 12
  flat_footed: 13
  components:
    armor: 3
    dex: 2
HP:
  HP: 25
  long: 4d8+4
saves:
  fort: 5
  ref: 4
  will: 7
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk light mace +6 (1d6+2)
      entries:
      - - damage: 1d6+2
      attack: mwk light mace
      bonus:
      - 6
  ranged:
  - - text: mwk javelin +6 (1d6+2)
      entries:
      - - damage: 1d6+2
      attack: mwk javelin
      bonus:
      - 6
  special:
  - channel positive energy 2/day (DC 11, 2d6)
spell_like_abilities:
  entries:
  - name: icicle
    source: default
    freq: 5/day
    other: 1d6+2 cold damage
  - name: resistant touch
    source: default
    freq: 5/day
  sources:
  - name: default
    CL: 4
    concentration: 6
spells:
  entries:
  - name: aid
    source: Cleric
    level: 2
  - name: calm emotions
    source: Cleric
    level: 2
    DC: 14
  - superscripts:
    - UC
    name: communal endure elements
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: fog cloud
    source: Cleric
    level: 2
  - name: bless
    source: Cleric
    level: 1
  - name: remove fear
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: sanctuary
    source: Cleric
    level: 1
    DC: 13
  - name: shield of faith
    source: Cleric
    level: 1
  - name: summon monster I
    source: Cleric
    level: 1
  - name: guidance
    source: Cleric
    level: 0
  - name: know direction
    source: Cleric
    level: 0
  - name: purify food and drink
    source: Cleric
    level: 0
  - name: stabilize
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 4
    concentration: 6
    slots:
      0: at-will
    domains:
    - protection
    - water
ability_scores:
  STR: 14
  DEX: 14
  CON: 10
  INT: 14
  WIS: 15
  CHA: 8
BAB: 3
CMB: 5
CMD: 17
feats:
- name: Alertness
- name: Skill Focus (Survival)
- name: Toughness
skills:
  Knowledge (local): 5
  Knowledge (religion): 6
  Perception: 6
  Profession (sailor): 9
  Sense Motive: 9
  Survival: 9
  Swim: 4
languages:
- Aquan
- Common
- Osiriani
ecology:
  environment: any (Osirion)
  organization: solitary or with fellow travelers
  treasure_type: NPC Gear
  treasure:
  - +1 leather armor
  - mwk javelin
  - mwk light mace
  - swan boat feather token
  - antitoxin
  - backpack
  - bedroll
  - fishing net
  - flint and steel
  - healer's kit
  - holy water [2]
  - silk rope [50 ft.]
  - tent
  - torches [3]
  - wooden holy symbol
  - 5 gp
desc_long: |-
  River clerics are dedicated to the pharaoh and the goddess Wadjet, the latter of whom they believe dwells within the papyrus marshes of the River Sphinx. These holy men and women consider it their sacred duty to offer services to river-goers in Osirion, whether by acting as guides for unexperienced travelers or by ferrying individuals across rivers. While accompanying travelers on their river journeys, river clerics make sure to educate the uninitiated on Wadjet and their ancient goddess's divine doctrine.

  While attending to an Osirian river in accordance with Wadjet's tenets, river clerics expect to be paid for their services just as any other guide or ferryman. Unlike others who perform similar functions, however, clerics of Wadjet use nearly all of their income to fund their deity's church. A river cleric never turns down a job unless she feels it clearly violates her deity's code of conduct (such as obstructing or defiling the river or acting against the interests of the pharaoh and his loyal subjects). Even when not ferrying clients, a river cleric can be found traveling along the river, offering her goddess's insight and blessings to the loyal subjects of the reigning pharaoh.

  For more information on Wadjet and the other gods of Ancient Osirion, see Pathfinder Adventure Path #80: Empty Graves.

---

# River Cleric
This holy woman wears a large pendant of a winged, two-headed cobra around her neck and wields a mace of similar make.
**Source** Osirion, Legacy of the Pharaohs pg. 62
**XP** 800
Human _[[classes/Cleric|cleric]]_ of Wadjet 4

LG Medium humanoid (human)
**Init** +2; **Senses** Perception +6

##### Defense

**AC** 15, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+3 armor, +2 Dex)
**hp** 25 (4d8+4)
**Fort** +5, **Ref** +4, **Will** +7

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Light mace|light mace]]_ +6 (1d6+2)
**Ranged** mwk _[[items/Weapon/Javelin|javelin]]_ +6 (1d6+2)
**Special Attacks** channel positive energy 2/day (DC 11, 2d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +6)
5/day—icicle (1d6+2 cold damage), resistant touch
**_Cleric_ Spells Prepared **(CL 4th; concentration +6)
2nd—aid, _[[spells/Calm Emotions|calm emotions]]_ (DC 14), communal _[[spells/Endure Elements|endure elements]]_, _[[spells/Fog Cloud|fog cloud]]_
1st—_[[spells/Bless|bless]]_, _[[spells/Remove Fear|remove fear]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 13), _[[spells/Shield Of Faith|shield of faith]]_, _[[spells/Summon Monster I|summon monster I]]_
0 (at will)—_[[spells/Guidance|guidance]]_, _[[spells/Know Direction|know direction]]_, _[[spells/Purify Food and Drink|purify food and drink]]_, stabilize
**D **Domain spell; **Domains **Protection, Water

##### Statistics
**Str** 14, **Dex** 14, **Con** 10, **Int** 14, **Wis** 15, **Cha** 8
**Base Atk** +3; **CMB** +5; **CMD** 17
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Skill Focus|Skill Focus]]_ (Survival), _[[feats/Toughness|Toughness]]_
**Skills** Knowledge (local) +5, Knowledge (religion) +6, Perception +6, Profession (sailor) +9, Sense Motive +9, Survival +9, Swim +4
**Languages** Aquan, Common, Osiriani

##### Ecology

**Environment** any (Osirion)
**Organization** solitary or with fellow travelers
**Treasure** NPC gear (+1 _[[items/Armor/Leather armor|leather armor]]_, mwk _javelin_, mwk _light mace_, swan boat feather token, _[[items/Mundane/Antitoxin|antitoxin]]_, backpack, _[[items/Mundane/Bedroll|bedroll]]_, _[[items/Mundane/Fishing net|fishing net]]_, _[[items/Mundane/Flint and steel|flint and steel]]_, _[[npcs/Healer|healer]]_’s kit, _[[items/Mundane/Holy water|holy water]]_ [2], _[[items/Mundane/Silk rope|silk rope]]_ [50 ft.], _[[items/Mundane/Tent|tent]]_, torches [3], wooden holy symbol, 5 gp)

River clerics are dedicated to the pharaoh and the goddess Wadjet, the latter of whom they believe dwells within the papyrus marshes of the River Sphinx. These holy men and women consider it their _[[items/Weapon Magic Abilities/Sacred|sacred]]_ duty to offer services to river-goers in Osirion, whether by acting as guides for unexperienced travelers or by ferrying individuals across rivers. While accompanying travelers on their river journeys, river clerics make sure to educate the uninitiated on Wadjet and their ancient goddess’s divine doctrine.

While attending to an Osirian river in accordance with Wadjet’s tenets, river clerics expect to be paid for their services just as any other guide or ferryman. Unlike others who perform similar functions, however, clerics of Wadjet use nearly all of their income to fund their deity’s church. A _[[npcs/River Cleric|river cleric]]_ never turns down a job unless she feels it clearly violates her deity’s code of conduct (such as obstructing or defiling the river or acting against the interests of the pharaoh and his loyal subjects). Even when not ferrying clients, a _river cleric_ can be found traveling along the river, offering her goddess’s insight and blessings to the loyal subjects of the reigning pharaoh.

For more information on Wadjet and the other gods of Ancient Osirion, see Pathfinder Adventure Path #80: Empty Graves.
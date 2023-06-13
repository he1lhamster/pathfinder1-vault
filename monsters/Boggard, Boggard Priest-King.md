---
cssclass: [monsters]
title1: Boggard, Boggard Priest-King
title2: Boggard Priest-King
CR: 11
sources:
- name: Monster Codex
  page: 15
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 12800
race: Boggard
classes:
- cleric 10
alignment: CE
size: Medium
type: humanoid
subtypes:
- boggard
initiative:
  bonus: 3
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 20
  touch: 9
  flat_footed: 20
  components:
    armor: 6
    dex: -1
    natural: 4
    shield: 1
HP:
  HP: 120
  long: 13d8+62
saves:
  fort: 14
  ref: 6
  will: 14
resistances:
  cold: 10
speeds:
  base: 15
  swim: 30
attacks:
  melee:
  - - text: +1 morningstar +15/+10 (1d8+5)
      entries:
      - - damage: 1d8+5
      attack: +1 morningstar
      bonus:
      - 15
      - 10
    - text: tongue +8 touch (sticky tongue)
      entries:
      - - effect: sticky tongue
      attack: tongue
      bonus:
      - 8
      touch: true
  special:
  - channel negative energy 5/day (DC 17, 5d6)
  - scythe of evil (5 rounds, 1/day)
  - terrifying croak (DC 15)
spell_like_abilities:
  entries:
  - name: fog cloud
    source: default
    freq: 1/day
  - name: jump
    source: default
    freq: 1/day
  - name: summon swarm
    source: default
    freq: 1/day
  - name: icicle
    source: domain
    freq: 8/day
    other: 1d6+5 cold
  - name: touch of evil
    source: domain
    freq: 8/day
    other: 5 rounds
  sources:
  - name: default
    CL: 13
    concentration: 15
  - name: domain
    CL: 10
    concentration: 15
spells:
  entries:
  - is_domain_spell: true
    name: dispel good
    source: Cleric
    level: 5
    DC: 20
  - name: insect plague
    source: Cleric
    level: 5
  - name: righteous might
    source: Cleric
    level: 5
  - name: slay living
    source: Cleric
    level: 5
    DC: 20
  - is_domain_spell: true
    name: control water
    source: Cleric
    level: 4
  - name: cure critical wounds
    source: Cleric
    level: 4
  - name: divine power
    source: Cleric
    level: 4
  - name: freedom of movement
    source: Cleric
    level: 4
  - name: unholy blight
    source: Cleric
    level: 4
    DC: 19
  - name: bestow curse
    source: Cleric
    level: 3
    DC: 18
  - name: dispel magic
    source: Cleric
    level: 3
  - name: invisibility purge
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: magic circle against good
    source: Cleric
    level: 3
  - name: magic vestment
    source: Cleric
    level: 3
  - name: bear's endurance
    source: Cleric
    level: 2
  - name: death knell
    source: Cleric
    level: 2
    DC: 17
  - name: enthrall
    source: Cleric
    level: 2
    DC: 17
  - is_domain_spell: true
    name: fog cloud
    source: Cleric
    level: 2
  - name: resist energy
    source: Cleric
    level: 2
  - name: sound burst
    source: Cleric
    level: 2
    DC: 17
  - name: bane
    source: Cleric
    level: 1
    DC: 16
  - name: bless
    source: Cleric
    level: 1
  - name: cure light wounds
    source: Cleric
    level: 1
  - name: divine favor
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: protection from good
    source: Cleric
    level: 1
  - name: sanctuary
    source: Cleric
    level: 1
    DC: 16
  - name: shield of faith
    source: Cleric
    level: 1
  - name: create water
    source: Cleric
    level: 0
  - name: detect poison
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: purify food and water
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 10
    concentration: 15
    slots:
      0: at-will
    domains:
    - evil
    - water
tactics:
  During Combat: The priest-king sits back with lazy arrogance, casting the occasional
    spell and allowing his minions to protect him until he is forced to intervene
    personally.
ability_scores:
  STR: 18
  DEX: 9
  CON: 16
  INT: 10
  WIS: 20
  CHA: 14
BAB: 9
CMB: 13
CMD: 22
feats:
- name: Brew Potion
- name: Combat Casting
- name: Craft Wand
- name: Improved Initiative
- name: Lightning Reflexes
- name: Toughness
- name: Weapon Focus (morningstar)
skills:
  Acrobatics: 0
    when jumping: 16
  Diplomacy: 8
  Knowledge (planes): 8
  Knowledge (religion): 8
  Perception: 9
  Sense Motive: 13
  Spellcraft: 8
  Stealth: 0
    in swamps: 8
  Swim: 10
languages:
- Boggard
special_qualities:
- hold breath
- priest-king
- swamp stride
gear:
  combat:
  - wand of cure light wounds (35 charges)
  - wand of owl's wisdom (25 charges)
  - wand of prayer (13 charges)
  other:
  - +2 hide armor
  - mwk light wooden shield
  - +1 morningstar
  - amulet of natural armor +1
  - cloak of resistance +1
  - spell component pouch
  - 24 gp
ecology:
  environment: temperate marshes
desc_long: Boggard priest-kings are the undisputed lords of their tribes, interpreting
  the wills of their dark patron deities (wills that are often suspiciously similar
  to what the priest-kings themselves desire). Grotesquely large, a boggard priest-king
  is usually the tribe's most capable combatant, and acts as a champion when needed.

---

# Boggard, Boggard Priest-King

**Source** Monster Codex pg. 15
**XP** 12,800
_[[monsters/Boggard|Boggard]]_ _[[classes/Cleric|cleric]]_ 10
CE Medium humanoid (_boggard_)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +9

##### Defense

**AC** 20, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+6 armor, –1 Dex, +4 natural, +1 _[[spells/Shield|shield]]_)
**hp** 120 (13d8+62)
**Fort** +14, **Ref** +6, **Will** +14
**Resist** cold 10

##### Offense
**Speed** 15 ft., swim 30 ft.
**Melee** +1 _[[items/Weapon/Morningstar|morningstar]]_ +15/+10 (1d8+5), tongue +8 touch (_[[items/Weapon Magic Abilities/Sticky|sticky]]_ tongue)
**Special Attacks** channel negative energy 5/day (DC 17, 5d6), _[[items/Weapon/Scythe|scythe]]_ of evil (5 rounds, 1/day), terrifying croak (DC 15)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +15)
1/day—_[[spells/Fog Cloud|fog cloud]]_, _[[spells/Jump|jump]]_, _[[spells/Summon Swarm|summon swarm]]_
**Domain _Spell-Like Abilities_ **(CL 10th; concentration +15)
8/day—icicle (1d6+5 cold), _[[feats/Touch Of Evil|touch of evil]]_ (5 rounds)
**_Cleric_ Spells Prepared **(CL 10th; concentration +15)
5th—_[[spells/Dispel Good|dispel good]]_ (DC 20), _[[spells/Insect Plague|insect plague]]_, _[[spells/Righteous Might|righteous might]]_, _[[spells/Slay Living|slay living]]_ (DC 20)
4th—_[[spells/Control Water|control water]]_, _[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Divine Power|divine power]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 19)
3rd—_[[spells/Bestow Curse|bestow curse]]_ (DC 18), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Magic Circle against Good|magic circle against good]]_, _[[spells/Magic Vestment|magic vestment]]_
2nd—bear’s _[[feats/Endurance|endurance]]_, _[[spells/Death Knell|death knell]]_ (DC 17), _[[spells/Enthrall|enthrall]]_ (DC 17), _fog cloud_, _[[spells/Resist Energy|resist energy]]_, _[[spells/Sound Burst|sound burst]]_ (DC 17)
1st—_[[spells/Bane|bane]]_ (DC 16), _[[spells/Bless|bless]]_, _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Protection From Good|protection from good]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 16), _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, purify food and water
**D** domain spell; **Domains** Evil, Water

### Tactics

**During Combat** The priest-king sits back with lazy arrogance, casting the occasional spell and allowing his minions to protect him until he is forced to intervene personally.

##### Statistics
**Str** 18, **Dex** 9, **Con** 16, **Int** 10, **Wis** 20, **Cha** 14
**Base Atk** +9; **CMB** +13; **CMD** 22
**Feats** _[[feats/Brew Potion|Brew Potion]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Craft Wand|Craft Wand]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_morningstar_)
**Skills** Acrobatics +0 (+16 when jumping), Diplomacy +8, Knowledge (planes) +8, Knowledge (religion) +8, Perception +9, Sense Motive +13, Spellcraft +8, Stealth +0 (+8 in swamps), Swim +10
**Languages** _Boggard_
**SQ** _[[universal monster rules/Hold Breath|hold breath]]_, priest-king, swamp stride
**Combat Gear** wand of _cure light wounds_ (35 charges), wand of owl’s wisdom (25 charges), wand of _[[spells/Prayer|prayer]]_ (13 charges); **Other Gear** +2 _[[items/Armor/Hide armor|hide armor]]_, mwk _[[items/Shield/Light wooden shield|light wooden shield]]_, +1 _morningstar_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 24 gp

##### Ecology

**Environment** temperate marshes

##### Description

_Boggard_ priest-kings are the undisputed lords of their tribes, interpreting the wills of their dark patron deities (wills that are often suspiciously similar to what the priest-kings themselves desire). Grotesquely large, a _boggard_ priest-king is usually the tribe’s most capable combatant, and acts as a _[[items/Armor Magic Abilities/Champion|champion]]_ when needed.
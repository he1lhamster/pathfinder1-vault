---
cssclass: [monsters]
title1: Serpentfolk, Serpentfolk High Priest
title2: Serpentfolk High Priest
CR: 14
sources:
- name: Monster Codex
  page: 207
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 38400
race: Advanced
classes:
- serpentfolk cleric 10
alignment: CE
size: Medium
type: monstrous humanoid
initiative:
  bonus: 10
senses:
  darkvision: 60
  scent: true
AC:
  AC: 28
  touch: 13
  flat_footed: 25
  components:
    armor: 8
    dex: 3
    natural: 4
    shield: 3
HP:
  HP: 182
  long: 5d10+10d8+110
  HD: 15
saves:
  fort: 15
  ref: 13
  will: 17
immunities:
- mind-affecting effects
- paralysis
- poison
SR: 25
speeds:
  base: 20
attacks:
  melee:
  - - text: +3 unholy light mace +24/+19/+14/+9 (1d6+6)
      entries:
      - - damage: 1d6+6
      attack: +3 unholy light mace
      bonus:
      - 24
      - 19
      - 14
      - 9
    - text: bite +16 (1d6+3 plus poison)
      entries:
      - - damage: 1d6+3
        - effect: poison
      attack: bite
      bonus:
      - 16
  ranged:
  - - text: mwk light crossbow +22 (1d8+3/19-20)
      entries:
      - - damage: 1d8+3
          crit_range: 19-20
      attack: mwk light crossbow
      bonus:
      - 22
  special:
  - channel negative energy 10/day (DC 22, 5d6)
  - scythe of evil (5 rounds, 1/day)
  - weapon master (10 rounds/day)
spell_like_abilities:
  entries:
  - name: disguise self
    source: default
    freq: At will
    DC: 16
    other: humanoid form only
  - name: ventriloquism
    source: default
    freq: At will
    DC: 16
  - name: blur
    source: default
    freq: 1/day
  - name: dominate person
    source: default
    freq: 1/day
    DC: 20
  - name: major image
    source: default
    freq: 1/day
    DC: 18
  - name: mass suggestion
    source: default
    freq: 1/day
    DC: 21
  - name: mirror image
    source: default
    freq: 1/day
  - name: suggestion
    source: default
    freq: 1/day
    DC: 18
  - name: teleport
    source: default
    freq: 1/day
  - name: battle rage
    source: domain
    freq: 9/day
    other: '+5'
  - name: touch of evil
    source: domain
    freq: 9/day
    other: 5 rounds
  sources:
  - name: default
    CL: 4
    concentration: 9
  - name: domain
    CL: 10
    concentration: 16
spells:
  entries:
  - is_domain_spell: true
    name: flame strike
    source: Cleric
    level: 5
    count: 2
    DC: 21
  - name: righteous might
    source: Cleric
    level: 5
  - name: slay living
    source: Cleric
    level: 5
    DC: 21
  - name: cure critical wounds
    source: Cleric
    level: 4
  - name: divine power
    source: Cleric
    level: 4
  - name: freedom of movement
    source: Cleric
    level: 4
  - superscripts:
    - UM
    name: spit venom
    source: Cleric
    level: 4
    DC: 20
  - is_domain_spell: true
    name: unholy blight
    source: Cleric
    level: 4
    DC: 20
  - name: cure serious wounds
    source: Cleric
    level: 3
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
  - name: protection from energy
    source: Cleric
    level: 3
  - name: bear's endurance
    source: Cleric
    level: 2
  - name: calm emotions
    source: Cleric
    level: 2
    DC: 18
  - name: darkness
    source: Cleric
    level: 2
  - superscripts:
    - UM
    name: dread bolt
    source: Cleric
    level: 2
    DC: 18
  - name: hold person
    source: Cleric
    level: 2
    count: 2
    DC: 18
  - is_domain_spell: true
    name: spiritual weapon
    source: Cleric
    level: 2
  - name: bane
    source: Cleric
    level: 1
    DC: 17
  - superscripts:
    - UM
    name: forbid action
    source: Cleric
    level: 1
    DC: 17
  - superscripts:
    - UM
    name: murderous command
    source: Cleric
    level: 1
    count: 2
    DC: 17
  - is_domain_spell: true
    name: protection from good
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
    count: 2
  - name: bleed
    source: Cleric
    level: 0
    DC: 16
  - name: detect magic
    source: Cleric
    level: 0
  - name: resistance
    source: Cleric
    level: 0
  - name: stabilize
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 10
    concentration: 16
    slots:
      0: at-will
    domains:
    - evil
    - war
tactics:
  Before Combat: A high priest prepares for battle by casting divine power and freedom
    of movement, then uses its scythe of evil ability to enhance its weapon.
ability_scores:
  STR: 10
  DEX: 23
  CON: 20
  INT: 16
  WIS: 22
  CHA: 20
BAB: 12
CMB: 12
CMD: 28
feats:
- name: Combat Casting
- name: Extra Channel
- name: Great Fortitude
- name: Improved Channel
- name: Improved Initiative
- name: Selective Channeling
- name: Toughness
- name: Weapon Finesse
skills:
  Acrobatics: 7
    when jumping: 3
  Diplomacy: 15
  Disguise: 10
  Escape Artist: 15
  Intimidate: 10
  Knowledge (arcana): 9
  Knowledge (nobility): 9
  Knowledge (planes): 9
  Knowledge (history): 10
  Knowledge (religion): 15
  Perception: 21
  Sense Motive: 15
  Spellcraft: 15
  Stealth: 11
  Use Magic Device: 15
languages:
- Aklo
- Common
- Draconic
- Undercommon
- telepathy 100 ft.
gear:
  combat:
  - potion of aid
  - wand of cure moderate wounds (10 charges)
  other:
  - +2 breastplate
  - +1 heavy steel shield
  - +3 unholy light mace
  - mwk light crossbow with 10 bolts
  - amulet of natural armor +1
  - belt of incredible dexterity +2
  - headband of inspired wisdom +2
  - pearl of power (1st)
  - phylactery of faithfulness
  - silver unholy symbol
  - spell component pouch
  - 1,434 gp
ecology:
  environment: any land (usually jungles or underground)
special_abilities:
  Poison (Ex): Bite-injury; save Fort DC 17; frequency 1/round for 6 rounds; effect
    1d2 Str; cure 2 saves. The save DC is Constitution-based.
desc_long: Serpentfolk high priests are the leaders of their people.

---

# Serpentfolk, Serpentfolk High Priest

**Source** Monster Codex pg. 207
**XP** 38,400
Advanced _[[monsters/Serpentfolk|serpentfolk]]_ _[[classes/Cleric|cleric]]_ 10
CE Medium monstrous humanoid
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +21

##### Defense

**AC** 28, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+8 armor, +3 Dex, +4 natural, +3 _[[spells/Shield|shield]]_)
**hp** 182 (15 HD; 5d10+10d8+110)
**Fort** +15, **Ref** +13, **Will** +17
**Immune** mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, poison; **SR** 25

##### Offense
**Speed** 20 ft.
**Melee** +3 _[[items/Weapon Magic Abilities/Unholy|unholy]]_ _[[items/Weapon/Light mace|light mace]]_ +24/+19/+14/+9 (1d6+6), bite +16 (1d6+3 plus poison)
**Ranged** mwk _[[items/Weapon/Light crossbow|light crossbow]]_ +22 (1d8+3/19–20)
**Special Attacks** channel negative energy 10/day (DC 22, 5d6), _[[items/Weapon/Scythe|scythe]]_ of evil (5 rounds, 1/day), weapon master (10 rounds/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +9)
At will—_[[spells/Disguise Self|disguise self]]_ (DC 16, humanoid form only), _[[spells/Ventriloquism|ventriloquism]]_ (DC 16)
1/day—_[[spells/Blur|blur]]_, _[[spells/Dominate Person|dominate person]]_ (DC 20), _[[spells/Major Image|major image]]_ (DC 18), mass _[[spells/Suggestion|suggestion]]_ (DC 21), _[[spells/Mirror Image|mirror image]]_, _suggestion_ (DC 18), teleport
**Domain _Spell-Like Abilities_** (CL 10th; concentration +16)
9/day— battle _[[spells/Rage|rage]]_ (+5), _[[feats/Touch Of Evil|touch of evil]]_ (5 rounds)
**_Cleric_ Spells Prepared **(CL 10th; concentration +16)
5th—_[[spells/Flame Strike|flame strike]]_ (2, DC 21), _[[spells/Righteous Might|righteous might]]_, _[[spells/Slay Living|slay living]]_ (DC 21)
4th—_[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Divine Power|divine power]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Spit Venom|spit venom]]_ (DC 20), _[[spells/Unholy Blight|unholy blight]]_ (DC 20)
3rd—_[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Magic Circle against Good|magic circle against good]]_, _[[spells/Protection from Energy|protection from energy]]_
2nd—bear’s _[[feats/Endurance|endurance]]_, _[[spells/Calm Emotions|calm emotions]]_ (DC 18), _[[spells/Darkness|darkness]]_, _[[spells/Dread Bolt|dread bolt]]_ (DC 18), _[[spells/Hold Person|hold person]]_ (2, DC 18), _[[spells/Spiritual Weapon|spiritual weapon]]_
1st—_[[spells/Bane|bane]]_ (DC 17), _[[spells/Forbid Action|forbid action]]_ (DC 17), _[[spells/Murderous Command|murderous command]]_ (2, DC 17), _[[spells/Protection From Good|protection from good]]_, _[[spells/Shield Of Faith|shield of faith]]_ (2)
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 16), _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/Resistance|resistance]]_, stabilize
**D** domain spell; **Domains** Evil, War

### Tactics

**Before Combat** A high priest prepares for battle by casting _divine power_ and _freedom of movement_, then uses its _scythe_ of evil ability to enhance its weapon.

##### Statistics
**Str** 10, **Dex** 23, **Con** 20, **Int** 16, **Wis** 22, **Cha** 20
**Base Atk** +12; **CMB** +12; **CMD** 28
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Channel|Improved Channel]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Selective Channeling|Selective Channeling]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +7 (+3 when jumping), Diplomacy +15, Disguise +10, Escape Artist +15, Intimidate +10, Knowledge (arcana, nobility, planes) +9, Knowledge (history) +10, Knowledge (religion) +15, Perception +21, Sense Motive +15, Spellcraft +15, Stealth +11, Use Magic Device +15
**Languages** Aklo, Common, Draconic, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**Combat Gear** potion of aid, wand of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (10 charges); **Other Gear** +2 _[[items/Armor/Breastplate|breastplate]]_, +1 _[[items/Shield/Heavy steel shield|heavy steel shield]]_, +3 _unholy_ _light mace_, mwk _light crossbow_ with 10 bolts, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, pearl of power (1st), _[[items/Wondrous Item/Phylactery of Faithfulness|phylactery of faithfulness]]_, silver _unholy_ symbol, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 1,434 gp

##### Ecology

**Environment** any land (usually jungles or underground)

### Special Abilities

**Poison (Ex)** Bite—injury; save Fort DC 17; frequency 1/round for 6 rounds; effect 1d2 Str; cure 2 saves. The save DC is Constitution-based.

##### Description

_Serpentfolk_ high priests are the leaders of their people.
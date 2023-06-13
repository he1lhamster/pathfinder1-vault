---
cssclass: [monsters]
title1: Sahuagin, Sahuagin High Priestess
title2: Sahuagin High Priestess
CR: 9
sources:
- name: Monster Codex
  page: 193
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 6400
race: Giant
classes:
- sahuagin cleric 7 (Pathfinder RPG Bestiary 295)
alignment: LE
size: Large
type: monstrous humanoid
subtypes:
- aquatic
initiative:
  bonus: -1
senses:
  blindsense: 30
  darkvision: 60
AC:
  AC: 23
  touch: 8
  flat_footed: 23
  components:
    armor: 7
    dex: -1
    natural: 8
    size: -1
HP:
  HP: 121
  long: 2d10+7d8+79
  HD: 9
saves:
  fort: 13
  ref: 6
  will: 13
weaknesses:
- light blindness
speeds:
  base: 30
  swim: 60
attacks:
  melee:
  - - text: +1 spear +13/+8 (2d6+8/×3)
      entries:
      - - damage: 2d6+8
          crit_multiplier: 3
      attack: +1 spear
      bonus:
      - 13
      - 8
    - text: bite +6 (1d8+5)
      entries:
      - - damage: 1d8+5
      attack: bite
      bonus:
      - 6
  ranged:
  - - text: mwk underwater heavy crossbow +6 (2d8/19-20)
      entries:
      - - damage: 2d8
          crit_range: 19-20
      attack: mwk underwater heavy crossbow
      bonus:
      - 6
  special:
  - blood frenzy
  - channel negative energy 5/day (DC 13, 4d6)
  - destructive smite (+3, 8/day)
spells:
  entries:
  - is_domain_spell: true
    name: dimension door
    source: Cleric
    level: 4
  - name: gift of the deep
    source: Cleric
    level: 4
  - name: unholy blight
    source: Cleric
    level: 4
    DC: 19
  - name: air breathing
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: fly
    source: Cleric
    level: 3
  - name: prayer
    source: Cleric
    level: 3
  - name: summon monster III
    source: Cleric
    level: 3
  - name: bear's endurance
    source: Cleric
    level: 2
  - name: cure moderate wounds
    source: Cleric
    level: 2
  - superscripts:
    - UM
    name: dread bolt
    source: Cleric
    level: 2
    DC: 17
  - name: hold person
    source: Cleric
    level: 2
    DC: 17
  - is_domain_spell: true
    name: shatter
    source: Cleric
    level: 2
    DC: 17
  - name: command
    source: Cleric
    level: 1
    DC: 16
  - name: cure light wounds
    source: Cleric
    level: 1
    count: 2
  - name: divine favor
    source: Cleric
    level: 1
  - superscripts:
    - UM
    name: murderous command
    source: Cleric
    level: 1
    DC: 16
  - name: sanctuary
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: true strike
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 15
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 7
    concentration: 12
    slots:
      0: at-will
    domains:
    - destruction
    - travel
ability_scores:
  STR: 20
  DEX: 9
  CON: 26
  INT: 14
  WIS: 20
  CHA: 11
BAB: 7
CMB: 13
CMD: 22
feats:
- name: Combat Casting
- name: Extra Channel
- name: Improved Natural Attack (bite)
- name: Lightning Reflexes
- name: Weapon Focus (spear)
skills:
  Intimidate: 12
  Knowledge (religion): 14
  Perception: 12
  Sense Motive: 17
  Spellcraft: 14
  Swim: 10
languages:
- Aquan
- Common
- Elven
- Infernal
- speak with sharks
special_qualities:
- agile feet (8/day)
gear:
  combat:
  - scroll of cure critical wounds
  other:
  - +1 breastplate
  - +1 spear
  - mwk underwater heavy crossbow with 20 bolts
  - headband of inspired wisdom +2
  - gold unholy symbol (worth 250 gp)
  - 796 gp
ecology:
  environment: temperate or warm ocean
desc_long: Priestesses lead ceremonies and support military actions.

---

# Sahuagin, Sahuagin High Priestess

**Source** Monster Codex pg. 193
**XP** 6,400
Giant _[[monsters/Sahuagin|sahuagin]]_ _[[classes/Cleric|cleric]]_ 7 (Pathfinder RPG Bestiary 295)

LE Large monstrous humanoid (aquatic)
**Init** –1; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 30 ft., _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +12

##### Defense

**AC** 23, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+7 armor, –1 Dex, +8 natural, –1 size)
**hp** 121 (9 HD; 2d10+7d8+79)
**Fort** +13, **Ref** +6, **Will** +13
**Weaknesses** _[[universal monster rules/Light Blindness|light blindness]]_

##### Offense
**Speed** 30 ft., swim 60 ft.
**Melee** +1 _[[items/Weapon/Spear|spear]]_ +13/+8 (2d6+8/×3), bite +6 (1d8+5)
**Ranged** mwk _[[items/Weapon/Underwater heavy crossbow|underwater heavy crossbow]]_ +6 (2d8/19–20)
**Special Attacks** blood frenzy, channel negative energy 5/day (DC 13, 4d6), destructive smite (+3, 8/day)
**_Cleric_ Spells Prepared** (CL 7th; concentration +12)
4th—_[[spells/Dimension Door|dimension door]]_, _[[spells/Gift Of The Deep|gift of the deep]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 19)
 3rd—_[[spells/Air Breathing|air breathing]]_, fly, _[[spells/Prayer|prayer]]_, _[[spells/Summon Monster III|summon monster III]]_
 2nd—bear’s _[[feats/Endurance|endurance]]_, _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Dread Bolt|dread bolt]]_ (DC 17), _[[spells/Hold Person|hold person]]_ (DC 17), _[[spells/Shatter|shatter]]_ (DC 17)
 1st—_[[spells/Command|command]]_ (DC 16), _[[spells/Cure Light Wounds|cure light wounds]]_ (2), _[[spells/Divine Favor|divine favor]]_, _[[spells/Murderous Command|murderous command]]_ (DC 16), _[[spells/Sanctuary|sanctuary]]_, _[[spells/True Strike|true strike]]_
 0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Read Magic|read magic]]_
 **D** domain spell; **Domains** _[[spells/Destruction|Destruction]]_, Travel

##### Statistics
**Str** 20, **Dex** 9, **Con** 26, **Int** 14, **Wis** 20, **Cha** 11
**Base Atk** +7; **CMB** +13; **CMD** 22
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Improved Natural Attack|Improved Natural Attack]]_ (bite), _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_spear_)
**Skills** Intimidate +12, Knowledge (religion) +14, Perception +12, Sense Motive +17, Spellcraft +14, Swim +10
**Languages** Aquan, Common, Elven, Infernal; speak with sharks
**SQ** _[[items/Weapon Magic Abilities/Agile|agile]]_ feet (8/day)
**Combat Gear** scroll of _[[spells/Cure Critical Wounds|cure critical wounds]]_; **Other Gear** +1 _[[items/Armor/Breastplate|breastplate]]_, +1 _spear_, mwk _underwater heavy crossbow_ with 20 bolts, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, gold _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol (worth 250 gp), 796 gp

##### Ecology

**Environment** temperate or warm ocean

##### Description

Priestesses lead ceremonies and support military actions.
---
cssclass: [monsters]
title1: Ratfolk, Ratfolk Elder
title2: Ratfolk Elder
CR: 8
sources:
- name: Monster Codex
  page: 183
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 4800
race: Ratfolk
classes:
- cleric of Abadar 9
alignment: N
size: Small
type: humanoid
subtypes:
- ratfolk
initiative:
  bonus: 4
senses:
  darkvision: 60
AC:
  AC: 19
  touch: 11
  flat_footed: 19
  components:
    armor: 7
    shield: 1
    size: 1
HP:
  HP: 80
  long: 9d8+36
saves:
  fort: 12
  ref: 5
  will: 12
speeds:
  base: 40
attacks:
  melee:
  - - text: mwk light mace +8/+3 (1d4)
      entries:
      - - damage: 1d4
      attack: mwk light mace
      bonus:
      - 8
      - 3
  ranged:
  - - text: light crossbow +7 (1d6/19-20)
      entries:
      - - damage: 1d6
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 7
  special:
  - channel positive energy 7/day (DC 16, 5d6)
  - swarming
spell_like_abilities:
  entries:
  - name: resistant touch +2
    source: default
    freq: 7/day
  - name: dimensional hop
    source: default
    freq: At will
    other: 90 feet/day
  sources:
  - name: default
    CL: 9
    concentration: 13
spells:
  entries:
  - is_domain_spell: true
    name: teleport
    source: Cleric
    level: 5
  - name: wall of stone
    source: Cleric
    level: 5
    DC: 19
  - is_domain_spell: true
    name: dimension door
    source: Cleric
    level: 4
  - name: dismissal
    source: Cleric
    level: 4
    DC: 18
  - name: freedom of movement
    source: Cleric
    level: 4
  - name: summon monster IV
    source: Cleric
    level: 4
  - name: dispel magic
    source: Cleric
    level: 3
  - name: magic vestment
    source: Cleric
    level: 3
  - name: meld into stone
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: protection from energy
    source: Cleric
    level: 3
  - name: stone shape
    source: Cleric
    level: 3
  - name: bull's strength
    source: Cleric
    level: 2
  - name: calm emotions
    source: Cleric
    level: 2
    DC: 16
  - name: darkness
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: shield other
    source: Cleric
    level: 2
  - name: sound burst
    source: Cleric
    level: 2
    DC: 16
  - name: zone of truth
    source: Cleric
    level: 2
    DC: 16
  - name: bless
    source: Cleric
    level: 1
  - name: command
    source: Cleric
    level: 1
    DC: 15
  - name: endure elements
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: longstrider
    source: Cleric
    level: 1
  - name: sanctuary
    source: Cleric
    level: 1
    DC: 15
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
  - name: mending
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 9
    concentration: 13
    slots:
      0: at-will
    domains:
    - protection
    - travel
tactics:
  Before Combat: The elder casts longstrider on herself, and bear's endurance, bull's
    strength, and magic vestment and on allies who will enter combat. She chooses
    one vulnerable ally to protect with shield other.
  During Combat: The elder focuses on healing her allies and counteracting her enemies'
    spells while staying out of harm's way. If the group needs to escape, she assists
    the evacuation by casting teleport (if a small number of allies are with her)
    or wall of stone (if a large number of ratfolk are with her).
  Base Statistics: Without longstrider, the elder's statistics are Speed 30 ft.
ability_scores:
  STR: 10
  DEX: 10
  CON: 14
  INT: 12
  WIS: 18
  CHA: 14
BAB: 6
CMB: 5
CMD: 15
feats:
- name: Extra Channel
- name: Great Fortitude
- name: Improved Initiative
- name: Selective Channeling
- name: Toughness
skills:
  Appraise: 5
  Craft (alchemy): 3
  Diplomacy: 14
  Heal: 12
  Knowledge (religion): 9
  Perception: 6
  Sense Motive: 14
  Use Magic Device: 4
  _racial_mods:
    Craft (alchemy):
      _: 2
    Perception:
      _: 2
    Use Magic Device:
      _: 2
languages:
- Celestial
- Common
special_qualities:
- agile feet (7/day)
- aura of protection (+1 deflection, energy resistance 5, 9 rounds/day)
- +10 base speed from Travel domain
gear:
  combat:
  - scroll of bear's endurance
  - scroll of invisibility purge
  - scroll of sending
  - wand of cure moderate wounds (15 charges)
  other:
  - +1 chainmail
  - light steel shield
  - light crossbow with 10 bolts
  - mwk light mace
  - cloak of resistance +1
  - headband of inspired wisdom +2
  - silver holy symbol
  - spell component pouch
  - sunrod
  - pair of platinum rings (worth 50 gp total)
  - 768 gp
ecology:
  environment: warm deserts or urban
desc_long: Since ratfolk have short lifespans, they heed the wisdom of those who attain
  old age. Many ratfolk aspire to become elders from a very young age, and try to
  get their hands on books and histories when they go into trade, intending to later
  study them. Often, aspiring leaders pursue the healing arts to keep the rest of
  the warren healthy-and to ensure they live long enough to pass on their knowledge.

---

# Ratfolk, Ratfolk Elder

**Source** Monster Codex pg. 183
**XP** 4,800
_[[monsters/Ratfolk|Ratfolk]]_ _[[classes/Cleric|cleric]]_ of Abadar 9

N Small humanoid (_ratfolk_)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +6

##### Defense

**AC** 19, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+7 armor, +1 _[[spells/Shield|shield]]_, +1 size)
**hp** 80 (9d8+36)
**Fort** +12, **Ref** +5, **Will** +12

##### Offense
**Speed** 40 ft.
**Melee** mwk _[[items/Weapon/Light mace|light mace]]_ +8/+3 (1d4)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +7 (1d6/19–20)
**Special Attacks** channel positive energy 7/day (DC 16, 5d6), swarming
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +13)
7/day—resistant touch +2
At will—dimensional hop (90 feet/day)
**_Cleric_ Spells Prepared **(CL 9th; concentration +13)
5th—teleport, _[[spells/Wall Of Stone|wall of stone]]_ (DC 19)
4th—_[[spells/Dimension Door|dimension door]]_, _[[spells/Dismissal|dismissal]]_ (DC 18), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Summon Monster IV|summon monster IV]]_
3rd—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Magic Vestment|magic vestment]]_, _[[spells/Meld into Stone|meld into stone]]_, _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Stone Shape|stone shape]]_
2nd—bull’s strength, _[[spells/Calm Emotions|calm emotions]]_ (DC 16), _[[spells/Darkness|darkness]]_, _[[spells/Shield Other|shield other]]_, _[[spells/Sound Burst|sound burst]]_ (DC 16), _[[spells/Zone of Truth|zone of truth]]_ (DC 16)
1st—_[[spells/Bless|bless]]_, _[[spells/Command|command]]_ (DC 15), _[[spells/Endure Elements|endure elements]]_, _[[spells/Longstrider|longstrider]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 15), _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, _[[spells/Mending|mending]]_
**D** domain spell; **Domains** Protection, Travel

### Tactics

**Before Combat** The elder casts _longstrider_ on herself, and bear’s _[[feats/Endurance|endurance]]_, bull’s strength, and _magic vestment_ and on allies who will enter combat. She chooses one vulnerable ally to protect with _shield other_.
 **During Combat** The elder focuses on healing her allies and counteracting her enemies’ spells while staying out of _[[spells/Harm|harm]]_’s way. If the group needs to escape, she assists the evacuation by casting teleport (if a small number of allies are with her) or _wall of stone_ (if a large number of _ratfolk_ are with her).
 **Base Statistics** Without _longstrider_, the elder’s statistics are **Speed **30 ft.

##### Statistics
**Str** 10, **Dex** 10, **Con** 14, **Int** 12, **Wis** 18, **Cha** 14
**Base Atk** +6; **CMB** +5; **CMD** 15
**Feats** _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Selective Channeling|Selective Channeling]]_, _[[feats/Toughness|Toughness]]_
**Skills** Appraise +5, Craft (alchemy) +3, Diplomacy +14, _[[spells/Heal|Heal]]_ +12, Knowledge (religion) +9, Perception +6, Sense Motive +14, Use Magic Device +4; **Racial Modifiers** +2 Craft (alchemy), +2 Perception, +2 Use Magic Device
**Languages** Celestial, Common
**SQ** _[[items/Weapon Magic Abilities/Agile|agile]]_ feet (7/day), aura of protection (+1 deflection, _[[items/Armor Magic Abilities/Energy Resistance|energy resistance]]_ 5, 9 rounds/day), +10 base speed from Travel domain
**Combat Gear** scroll of bear’s _endurance_, scroll of _[[spells/Invisibility Purge|invisibility purge]]_, scroll of _[[spells/Sending|sending]]_, wand of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (15 charges); **Other Gear** +1 _[[items/Armor/Chainmail|chainmail]]_, _[[items/Shield/Light steel shield|light steel shield]]_, _light crossbow_ with 10 bolts, mwk _light mace_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, silver holy symbol, _[[items/Mundane/Spell component pouch|spell component pouch]]_, _[[items/Mundane/Sunrod|sunrod]]_, pair of platinum rings (worth 50 gp total), 768 gp

##### Ecology

**Environment** warm deserts or urban

##### Description

Since _ratfolk_ have short lifespans, they heed the wisdom of those who attain old age. Many _ratfolk_ aspire to become elders from a very young age, and try to get their hands on books and histories when they go into trade, intending to later study them. Often, aspiring leaders pursue the healing arts to keep the rest of the warren healthy—and to ensure they live long enough to pass on their knowledge.
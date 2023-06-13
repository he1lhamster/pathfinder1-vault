---
cssclass: [monsters]
title1: Girtablilu, Divine Chieftain
desc_short: This authoritative, scorpion-bodied woman is bedecked with amulets and
  other regalia.
title2: Divine Chieftain
CR: 14
sources:
- name: Inner Sea Monster Codex
  page: 39
  link: http://paizo.com/products/btpy9elc?Pathfinder-Campaign-Setting-Inner-Sea-Monster-Codex
XP: 38400
race: Girtablilu
classes:
- druid (desert druid) 10 (Pathfinder RPG Bestiary 3 130, Pathfinder RPG Advanced
  Player's Guide 99)
alignment: N
size: Large
type: monstrous humanoid
initiative:
  bonus: 11
senses:
  darkvision: 60
  tremorsense: 30
AC:
  AC: 30
  touch: 12
  flat_footed: 27
  components:
    armor: 8
    dex: 2
    dodge: 1
    natural: 10
    size: -1
HP:
  HP: 240
  long: 10d8+10d10+140
  HD: 20
saves:
  fort: 19
  ref: 14
  will: 21
  other: +2 vs. gaze attacks and figment and pattern illusions
immunities:
- blinding and dazzling effects
speeds:
  base: 35
attacks:
  melee:
  - - text: +1 spear +23/+18/+13/+8 (2d6+10/×3)
      entries:
      - - damage: 2d6+10
          crit_multiplier: 3
      attack: +1 spear
      bonus:
      - 23
      - 18
      - 13
      - 8
    - text: 2 claws +21 (1d6+3 plus grab)
      entries:
      - - damage: 1d6+3
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 21
    - text: sting +21 (1d6+3 plus poison)
      entries:
      - - damage: 1d6+3
        - effect: poison
      attack: sting
      bonus:
      - 21
  ranged:
  - - text: mwk sling +19/+14/+9/+4 (1d4+6)
      entries:
      - - damage: 1d4+6
      attack: mwk sling
      bonus:
      - 19
      - 14
      - 9
      - 4
  - - text: +1 spear +19 (2d6+10/×3)
      entries:
      - - damage: 2d6+10
          crit_multiplier: 3
      attack: +1 spear
      bonus:
      - 19
  special:
  - constrict (1d6+5)
  - poison (DC 27)
  - wild shape 4/day
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: summon nature's ally V
    source: default
    freq: 1/day
    other: 1d3 giant scorpions
  sources:
  - name: default
    CL: 10
    concentration: 13
spells:
  entries:
  - name: baleful polymorph
    source: Druid
    level: 5
    DC: 20
  - is_domain_spell: true
    name: commune with nature
    source: Druid
    level: 5
  - name: cure critical wounds
    source: Druid
    level: 5
  - name: stoneskin
    source: Druid
    level: 5
  - name: dispel magic
    source: Druid
    level: 4
  - name: freedom of movement
    source: Druid
    level: 4
  - name: giant vermin
    source: Druid
    level: 4
  - is_domain_spell: true
    name: rusting grasp
    source: Druid
    level: 4
  - name: scrying
    source: Druid
    level: 4
    DC: 19
  - name: cure moderate wounds
    source: Druid
    level: 3
  - name: greater magic fang
    source: Druid
    level: 3
  - is_domain_spell: true
    name: meld into stone
    source: Druid
    level: 3
  - name: protection from energy
    source: Druid
    level: 3
  - name: stone shape
    source: Druid
    level: 3
  - name: barkskin
    source: Druid
    level: 2
  - name: bear's strength
    source: Druid
    level: 2
  - name: lesser restoration
    source: Druid
    level: 2
  - name: owl's wisdom
    source: Druid
    level: 2
  - name: spider climb
    source: Druid
    level: 2
  - superscripts:
    - APG
    is_domain_spell: true
    name: stone call
    source: Druid
    level: 2
  - name: cure light wounds
    source: Druid
    level: 1
  - superscripts:
    - APG
    name: expeditious excavation
    source: Druid
    level: 1
  - name: longstrider
    source: Druid
    level: 1
  - name: magic fang
    source: Druid
    level: 1
  - is_domain_spell: true
    name: magic stone
    source: Druid
    level: 1
  - name: pass without trace
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
  - name: create water
    source: Druid
    level: 0
  - name: guidance
    source: Druid
    level: 0
  - name: mending
    source: Druid
    level: 0
  - name: read magic
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 10
    concentration: 15
    slots:
      0: at-will
    domains:
    - ruins
ability_scores:
  STR: 22
  DEX: 14
  CON: 25
  INT: 12
  WIS: 20
  CHA: 16
BAB: 17
CMB: 24
CMB_other: +28 grapple
CMD: 38
CMD_other: 50 vs. trip
feats:
- name: Dazzling Display
- name: Deadly Stroke
- name: Dodge
- name: Improved Initiative
- name: Improved Natural Armor
- name: Multiattack
- name: Persuasive
- name: Shatter Defenses
- name: Weapon Focus (claw)
- name: Weapon Focus (sting)
skills:
  Climb: 12
  Diplomacy: 23
  Intimidate: 23
  Knowledge (dungeoneering): 11
  Knowledge (engineering): 11
  Knowledge (geography): 11
  Knowledge (history): 11
  Knowledge (nature): 11
  Knowledge (religion): 11
  Perception: 17
  Sense Motive: 23
  Stealth: 17
  Survival: 20
  _racial_mods:
    Climb:
      _: 4
    Perception:
      _: 4
    Stealth:
      _: 4
languages:
- Common
- Druidic
- Girtablilu
- Kelish
special_qualities:
- desert endurance
- desert native +5
- nature bond (Ruins domain)
- nature sense
- sandwalker
- scorpion empathy +20
- shaded vision
- undersized weapons
- wild empathy +13
gear:
  combat:
  - oils of make whole (3)
  - wand of call lightning (13 charges)
  other:
  - +2 scorpion-hide breastplate (worth 5,350 gp)
  - +1 spear
  - mwk sling
  - amulet of natural armor +1
  - belt of giant strength +2
  - cloak of resistance +2
  - headband of mental prowess +2 (Wis, Cha)
  - ring of protection +1
  - granite and diamond dust (1,000 gp)
ecology:
  environment: warm deserts
desc_long: 'A divine chieftain wields absolute authority over her tribe. She embodies
  the girtablilus' dedication to their selfappointed sacred duties: studied in history,
  an expert on lost ruins, a compassionate diplomat, and a fearsome warrior.'

---

# Girtablilu, Divine Chieftain
This authoritative, scorpion-bodied woman is bedecked with amulets and other regalia.
**Source** Inner Sea Monster Codex pg. 39
**XP** 38,400
_[[monsters/Girtablilu|Girtablilu]]_ _[[classes/Druid|druid]]_ (desert _druid_) 10 (Pathfinder RPG Bestiary 3 130, Pathfinder RPG Advanced Player’s Guide 99)

N Large monstrous humanoid
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Tremorsense|tremorsense]]_ 30 ft.; Perception +17

##### Defense

**AC** 30, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+8 armor, +2 Dex, +1 dodge, +10 natural, –1 size)
**hp** 240 (20 HD; 10d8+10d10+140)
**Fort** +19, **Ref** +14, **Will** +21; +2 vs. _[[universal monster rules/Gaze|gaze]]_ attacks and figment and pattern illusions
**Immune** _[[items/Armor Magic Abilities/Blinding|blinding]]_ and dazzling effects

##### Offense
**Speed** 35 ft.
**Melee** +1 _[[items/Weapon/Spear|spear]]_ +23/+18/+13/+8 (2d6+10/×3), 2 claws +21 (1d6+3 plus _[[universal monster rules/Grab|grab]]_), sting +21 (1d6+3 plus poison)
**Ranged** mwk _[[items/Weapon/Sling|sling]]_ +19/+14/+9/+4 (1d4+6) or +1 _spear_ +19 (2d6+10/×3)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (1d6+5), poison (DC 27), wild shape 4/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +13)
1/day—_[[universal monster rules/Summon|summon]]_ nature’s ally V (1d3 giant scorpions)
**_Druid_ Spells Prepared **(CL 10th; concentration +15)
5th—_[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 20), _[[spells/Commune with Nature|commune with nature]]_, _[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Stoneskin|stoneskin]]_
4th—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Giant Vermin|giant vermin]]_, _[[spells/Rusting Grasp|rusting grasp]]_, _[[spells/Scrying|scrying]]_ (DC 19)
3rd—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_, greater _[[spells/Magic Fang|magic fang]]_, _[[spells/Meld into Stone|meld into stone]]_, _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Stone Shape|stone shape]]_
2nd—_[[spells/Barkskin|barkskin]]_, bear’s strength, lesser _[[spells/Restoration|restoration]]_, owl’s wisdom, _[[spells/Spider Climb|spider climb]]_, stone callD, APG
1st—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Expeditious Excavation|expeditious excavation]]_, _[[spells/Longstrider|longstrider]]_, _magic fang_, _[[spells/Magic Stone|magic stone]]_, _[[spells/Pass without Trace|pass without trace]]_, _[[spells/Speak with Animals|speak with animals]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Guidance|guidance]]_, _[[spells/Mending|mending]]_, _[[spells/Read Magic|read magic]]_
**D** Domain spell; **Domain** Ruins

##### Statistics
**Str** 22, **Dex** 14, **Con** 25, **Int** 12, **Wis** 20, **Cha** 16
**Base Atk** +17; **CMB** +24 (+28 grapple); **CMD** 38 (50 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Dazzling Display|Dazzling Display]]_, _[[feats/Deadly Stroke|Deadly Stroke]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Natural Armor|Improved Natural Armor]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Persuasive|Persuasive]]_, _[[feats/Shatter Defenses|Shatter Defenses]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw, sting)
**Skills** _[[universal monster rules/Climb|Climb]]_ +12, Diplomacy +23, Intimidate +23, Knowledge (dungeoneering, engineering, geography, history, nature, religion) +11, Perception +22, Sense Motive +23, Stealth +17, Survival +20; **Racial Modifiers** +4 _Climb_, +4 Perception, +4 Stealth
**Languages** Common, Druidic, _Girtablilu_, Kelish
**SQ** desert _[[feats/Endurance|endurance]]_, desert native +5, nature bond (Ruins domain), nature sense, sandwalker, scorpion _[[feats/Empathy|empathy]]_ +20, shaded _[[spells/Vision|vision]]_, _[[universal monster rules/Undersized Weapons|undersized weapons]]_, wild _empathy_ +13
**Combat Gear** oils of _[[spells/Make Whole|make whole]]_ (3), wand of _[[spells/Call Lightning|call lightning]]_ (13 charges); **Other Gear** +2 scorpion-hide _[[items/Armor/Breastplate|breastplate]]_ (worth 5,350 gp), +1 _spear_, mwk _sling_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Headband of Mental Prowess +2|headband of mental prowess +2]]_ (Wis, Cha), _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, granite and diamond dust (1,000 gp)

##### Ecology

**Environment** warm deserts

##### Description

A divine chieftain wields absolute authority over her tribe. She embodies the girtablilus’ dedication to their selfappointed _[[items/Weapon Magic Abilities/Sacred|sacred]]_ duties: studied in history, an expert on lost ruins, a _[[items/Weapon Magic Abilities/Compassionate|compassionate]]_ _[[npcs/Diplomat|diplomat]]_, and a fearsome warrior.
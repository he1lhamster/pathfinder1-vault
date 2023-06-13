---
cssclass: [monsters]
title1: Dragon (Primal, Brine), Young Brine Dragon
desc_short: 'A blue-green neck frill sweeps back from the head of this dragon, leading
  to a body of shiny scales and fin-like crests. '
title2: Young Brine Dragon
CR: 7
sources:
- name: Bestiary 2
  page: 94
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 3200
alignment: LN
size: Medium
type: dragon
subtypes:
- extraplanar
- water
initiative:
  bonus: 5
senses:
  dragon senses: true
AC:
  AC: 20
  touch: 11
  flat_footed: 19
  components:
    dex: 1
    natural: 9
HP:
  HP: 68
  long: 8d12+16
saves:
  fort: 8
  ref: 7
  will: 7
immunities:
- acid
- paralysis
- sleep
speeds:
  base: 60
  fly: 150
  fly_maneuverability: average
  swim: 60
attacks:
  melee:
  - - text: bite +15 (1d8+10)
      entries:
      - - damage: 1d8+10
      attack: bite
      bonus:
      - 15
    - text: 2 claws +15 (1d6+7)
      entries:
      - - damage: 1d6+7
      count: 2
      attack: claws
      bonus:
      - 15
    - text: 2 wings +10 (1d4+3)
      entries:
      - - damage: 1d4+3
      count: 2
      attack: wings
      bonus:
      - 10
  special:
  - breath weapon (60-ft. line, 6d6 acid, DC 16)
spell_like_abilities:
  entries:
  - name: obscuring mist
    source: default
    freq: At will
  - name: speak with animals
    source: default
    freq: At will
    other: fish only
  sources:
  - name: default
    CL: 8
    concentration: 9
spells:
  entries:
  - name: color spray
    source: '?'
    level: 1
    DC: 12
  - name: touch of the sea
    source: '?'
    level: 1
  - name: detect magic
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: open/close
    source: '?'
    level: 0
  - name: prestidigitation
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 1
    concentration: 2
    slots:
      1: 4
      0: at-will
ability_scores:
  STR: 24
  DEX: 13
  CON: 15
  INT: 15
  WIS: 12
  CHA: 13
BAB: 8
CMB: 15
CMD: 26
CMD_other: 30 vs. trip
feats:
- name: Hover
- name: Improved Initiative
- name: Power Attack
- name: Skill Focus (swim)
skills:
  Diplomacy: 12
  Fly: 12
  Heal: 12
  Knowledge (nature): 13
  Perception: 12
  Sense Motive: 12
  Survival: 12
  Swim: 29
languages:
- Aquan
- Common
- Draconic
special_qualities:
- water breathing
ecology:
  environment: any aquatic (Plane of Water)
  organization: solitary
  treasure_type: triple
desc_long: Although not inherently evil, brine dragons have little patience for kindness
  and philanthropy. As they age, they grow more and more opinionated and obsessed
  with power-by adult age, a brine dragon counts itself a failure if it doesn't rule
  over a collection of “lesser beings” such as humans, merfolk, locathah, or even
  sahuagin.

---

# Dragon (Primal, Brine), Young Brine Dragon
A blue-green neck frill sweeps back from the head of this dragon, leading to a body of shiny scales and fin-like crests.

**Source** Bestiary 2 pg. 94
**XP** 3,200

LN Medium dragon (extraplanar, water)
**Init** +5; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +12

##### Defense

**AC** 20, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+1 Dex, +9 natural)
**hp** 68 (8d12+16)
**Fort** +8, **Ref** +7, **Will** +7
**Immune** acid, _[[universal monster rules/Paralysis|paralysis]]_, sleep

##### Offense
**Speed** 60 ft., fly 150 ft. (average), swim 60 ft.
**Melee** bite +15 (1d8+10), 2 claws +15 (1d6+7), 2 wings +10 (1d4+3)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. line, 6d6 acid, DC 16)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +9)
At will—_[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Speak with Animals|speak with animals]]_ (fish only)
**Spells Known **(CL 1st; concentration +2)
1st (4/day)—_[[spells/Color Spray|color spray]]_ (DC 12), _[[spells/Touch of the Sea|touch of the sea]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_, open/close, _[[spells/Prestidigitation|prestidigitation]]_

##### Statistics
**Str** 24, **Dex** 13, **Con** 15, **Int** 15, **Wis** 12, **Cha** 13
**Base Atk** +8; **CMB** +15; **CMD** 26 (30 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Hover|Hover]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (swim)
**Skills** Diplomacy +12, Fly +12, _[[spells/Heal|Heal]]_ +12, Knowledge (nature) +13, Perception +12, Sense Motive +12, Survival +12, Swim +29
**Languages** Aquan, Common, Draconic
**SQ** _[[universal monster rules/Water Breathing|water breathing]]_

##### Ecology

**Environment** any aquatic (Plane of Water)
**Organization** solitary
**Treasure** triple

##### Description

Although not inherently evil, brine dragons have little patience for kindness and philanthropy. As they age, they grow more and more opinionated and obsessed with power—by adult age, a brine dragon counts itself a failure if it doesn't rule over a collection of “lesser beings” such as humans, _[[monsters/Merfolk|merfolk]]_, _[[monsters/Locathah|locathah]]_, or even _[[monsters/Sahuagin|sahuagin]]_.
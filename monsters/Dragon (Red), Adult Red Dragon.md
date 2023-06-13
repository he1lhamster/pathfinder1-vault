---
cssclass: [monsters]
title1: Dragon (Red), Adult Red Dragon
title2: Adult Red Dragon
CR: 14
sources:
- name: Pathfinder RPG Bestiary
  page: 98
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 38400
alignment: CE
size: Huge
type: dragon
subtypes:
- fire
initiative:
  bonus: 4
senses:
  dragon senses: true
  smoke vision: true
auras:
- name: fire
  radius: 5
  other:
  - 1d6 fire
- name: frightful presence
  radius: 180
  DC: 21
AC:
  AC: 29
  touch: 8
  flat_footed: 29
  components:
    natural: 21
    size: -2
HP:
  HP: 212
  long: 17d12+102
saves:
  fort: 16
  ref: 10
  will: 15
DR:
- amount: 5
  weakness: magic
immunities:
- fire
- paralysis
- sleep
SR: 25
weaknesses:
- vulnerability to cold
speeds:
  base: 40
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +25 (2d8+15)
      entries:
      - - damage: 2d8+15
      attack: bite
      bonus:
      - 25
    - text: 2 claws +25 (2d6+10)
      entries:
      - - damage: 2d6+10
      count: 2
      attack: claws
      bonus:
      - 25
    - text: 2 wings +23 (1d8+5)
      entries:
      - - damage: 1d8+5
      count: 2
      attack: wings
      bonus:
      - 23
    - text: tail slap +23 (2d6+15)
      entries:
      - - damage: 2d6+15
      attack: tail slap
      bonus:
      - 23
  special:
  - breath weapon (50-ft. cone, DC 24, 12d10 fire)
  - crush
space: 15
reach: 10
reach_other: 15 ft. with bite
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: At will
  - name: pyrotechnics
    source: default
    freq: At will
    DC: 15
  - name: suggestion
    source: default
    freq: At will
    DC: 16
  sources:
  - name: default
    CL: 17
spells:
  entries:
  - name: dispel magic
    source: '?'
    level: 3
  - name: haste
    source: '?'
    level: 3
  - name: invisibility
    source: '?'
    level: 2
  - name: resist energy
    source: '?'
    level: 2
  - name: see invisibility
    source: '?'
    level: 2
  - name: alarm
    source: '?'
    level: 1
  - name: grease
    source: '?'
    level: 1
    DC: 14
  - name: magic missile
    source: '?'
    level: 1
  - name: shield
    source: '?'
    level: 1
  - name: true strike
    source: '?'
    level: 1
  - name: arcane mark
    source: '?'
    level: 0
  - name: light
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: mending
    source: '?'
    level: 0
  - name: message
    source: '?'
    level: 0
  - name: prestidigitation
    source: '?'
    level: 0
  - name: read magic
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 7
    slots:
      3: 5
      2: 7
      1: 7
      0: at-will
ability_scores:
  STR: 31
  DEX: 10
  CON: 23
  INT: 16
  WIS: 17
  CHA: 16
BAB: 17
CMB: 29
CMD: 39
CMD_other: 43 vs. trip
feats:
- name: Cleave
- name: Greater Vital Strike
- name: Improved Initiative
- name: Improved Iron Will
- name: Improved Vital Strike
- name: Iron Will
- name: Multiattack
- name: Power Attack
- name: Vital Strike
skills:
  Appraise: 23
  Bluff: 23
  Fly: 12
  Intimidate: 23
  Knowl. (arcana): 23
  Perception: 23
  Sense Motive: 23
  Spellcraft: 23
  Stealth: 12
languages:
- Common
- Draconic
- Dwarven
- Orc
ecology:
  environment: warm mountains
desc_long: Few creatures are more cruel and fearsome than the mighty red dragon. King
  of the chromatics, this terrible beast brings ruin and death to the lands that fall
  under its shadow.

---

# Dragon (Red), Adult Red Dragon

**Source** Pathfinder RPG Bestiary pg. 98
**XP** 38,400
CE Huge dragon (fire)
**Init** +4; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, smoke _[[spells/Vision|vision]]_; Perception +23
**Aura** fire (5 ft., 1d6 fire), _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 21)

##### Defense

**AC** 29, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 29 (+21 natural, –2 size)
**hp** 212 (17d12+102)
**Fort** +16, **Ref** +10, **Will** +15
**DR** 5/magic; **Immune** fire, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 25
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to cold

##### Offense
**Speed** 40 ft., fly 200 ft. (poor)
**Melee** bite +25 (2d8+15), 2 claws +25 (2d6+10), 2 wings +23 (1d8+5), tail slap +23 (2d6+15)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (50-ft. cone, DC 24, 12d10 fire), crush
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th)
At will—_[[spells/Detect Magic|detect magic]]_, _[[spells/Pyrotechnics|pyrotechnics]]_ (DC 15), _[[spells/Suggestion|suggestion]]_ (DC 16)
**Spells Known **(CL 7th)
3rd (5/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Haste|haste]]_
2nd (7/day)—_[[spells/Invisibility|invisibility]]_, _[[spells/Resist Energy|resist energy]]_, _[[spells/See Invisibility|see invisibility]]_
1st (7/day)—_[[spells/Alarm|alarm]]_, _[[spells/Grease|grease]]_ (DC 14), _[[spells/Magic Missile|magic missile]]_, _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 31, **Dex** 10, **Con** 23, **Int** 16, **Wis** 17, **Cha** 16
**Base Atk** +17; **CMB** +29; **CMD** 39 (43 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Appraise +23, Bluff +23, Fly +12, Intimidate +23, Knowl. (arcana) +23, Perception +23, Sense Motive +23, Spellcraft +23, Stealth +12
**Languages** Common, Draconic, Dwarven, _[[monsters/Orc|Orc]]_

##### Ecology

**Environment** warm mountains

Few creatures are more _[[items/Weapon Magic Abilities/Cruel|cruel]]_ and fearsome than the mighty red dragon. _[[npcs/King|King]]_ of the chromatics, this terrible beast brings ruin and death to the lands that fall under its _[[items/Armor Magic Abilities/Shadow|shadow]]_.
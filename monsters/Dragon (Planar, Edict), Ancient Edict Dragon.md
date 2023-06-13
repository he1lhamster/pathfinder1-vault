---
cssclass: [monsters]
title1: Dragon (Planar, Edict), Ancient Edict Dragon
title2: Ancient Edict Dragon
CR: 21
sources:
- name: "Pathfinder #131: The Reaper's Right Hand"
  page: 89
  link: http://paizo.com/products/btpy9x04?Pathfinder-Adventure-Path-The-Reaper-s-Right-Hand
XP: 409600
alignment: LN
size: Gargantuan
type: dragon
subtypes:
- extraplanar
- lawful
initiative:
  bonus: 2
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 300
  DC: 31
AC:
  AC: 41
  touch: 4
  flat_footed: 41
  components:
    dex: -2
    natural: 35
    shield: 2
    size: -4
HP:
  HP: 434
  long: 28d12+252
saves:
  fort: 25
  ref: 16
  will: 25
defensive_abilities:
- parapet wings
DR:
- amount: 15
  weakness: chaotic
immunities:
- disease
- fear
- paralysis
- poison
- sleep
SR: 34
speeds:
  60 ft. fly: 250
  60 ft. fly_other: clumsy
attacks:
  melee:
  - - text: bite +38 (4d6+14/19-20)
      entries:
      - - damage: 4d6+14
          crit_range: 19-20
      attack: bite
      bonus:
      - 38
    - text: 2 claws +38 (2d8+14)
      entries:
      - - damage: 2d8+14
      count: 2
      attack: claws
      bonus:
      - 38
    - text: tail slap +33 (sweeping scrawl)
      entries:
      - - effect: sweeping scrawl
      attack: tail slap
      bonus:
      - 33
    - text: 2 wings +39 (2d6+7)
      entries:
      - - damage: 2d6+7
      count: 2
      attack: wings
      bonus:
      - 39
  special:
  - breath weapon (120-foot line, 20d10 slashing damage, Reflex DC 33 half)
  - crush
  - hindering shards
  - master scrivener
  - powerful wings
  - scrivener
  - sweeping scrawl
  - tail sweep
space: 20
reach: 15
reach_other: 20 ft. with bite
spells:
  entries:
  - name: dictum
    source: Oracle
    level: 7
    DC: 24
  - name: repulsion
    source: Oracle
    level: 7
    DC: 24
  - name: geas/quest
    source: Oracle
    level: 6
  - name: heal
    source: Oracle
    level: 6
  - name: symbol of fear
    source: Oracle
    level: 6
    DC: 23
  - name: dispel chaos
    source: Oracle
    level: 5
  - name: mark of justice
    source: Oracle
    level: 5
  - name: symbol of pain
    source: Oracle
    level: 5
    DC: 22
  - name: true seeing
    source: Oracle
    level: 5
  - name: dimensional anchor
    source: Oracle
    level: 4
  - name: dismissal
    source: Oracle
    level: 4
    DC: 21
  - name: order's wrath
    source: Oracle
    level: 4
    DC: 21
  - name: sending
    source: Oracle
    level: 4
  - name: bestow curse
    source: Oracle
    level: 3
    DC: 20
  - name: dispel magic
    source: Oracle
    level: 3
  - name: glyph of warding
    source: Oracle
    level: 3
    DC: 20
  - name: stone shape
    source: Oracle
    level: 3
  - name: calm emotions
    source: Oracle
    level: 2
    DC: 19
  - name: cure moderate wounds
    source: Oracle
    level: 2
  - name: make whole
    source: Oracle
    level: 2
  - name: resist energy
    source: Oracle
    level: 2
  - name: silence
    source: Oracle
    level: 2
    DC: 19
  - name: command
    source: Oracle
    level: 1
    DC: 18
  - name: comprehend languages
    source: Oracle
    level: 1
  - name: detect chaos
    source: Oracle
    level: 1
  - name: remove fear
    source: Oracle
    level: 1
  - name: shield of faith
    source: Oracle
    level: 1
  - name: create water
    source: Oracle
    level: 0
  - name: detect magic
    source: Oracle
    level: 0
  - name: detect poison
    source: Oracle
    level: 0
  - name: guidance
    source: Oracle
    level: 0
  - name: light
    source: Oracle
    level: 0
  - name: mending
    source: Oracle
    level: 0
  - name: purify food and drink
    source: Oracle
    level: 0
  - name: read magic
    source: Oracle
    level: 0
  - name: stabilize
    source: Oracle
    level: 0
  sources:
  - name: Oracle
    type: known
    CL: 15
    concentration: 22
    slots:
      7: 5
      6: 7
      5: 7
      4: 7
      3: 8
      2: 8
      1: 8
      0: at-will
ability_scores:
  STR: 39
  DEX: 6
  CON: 29
  INT: 24
  WIS: 29
  CHA: 24
BAB: 28
CMB: 46
CMB_other: +50 reposition
CMD: 58
CMD_other: 60 vs. reposition, 62 vs. trip
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Crippling Critical
- name: Critical Focus
- name: Greater Reposition
- name: Hover
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Reposition
- name: Lightning Reflexes
- name: Quicken Spell
- name: Repositioning Strike
- name: Stand Still
- name: Weapon Focus (wing)
skills:
  Diplomacy: 38
  Fly: 15
  Intimidate: 38
  Knowledge (engineering): 38
  Knowledge (history): 38
  Knowledge (local): 38
  Knowledge (nobility): 38
  Knowledge (planes): 38
  Linguistics: 38
  Perception: 40
  Sense Motive: 40
  Spellcraft: 38
  Survival: 40
languages:
- Common
- Draconic
- plus any 28 others
- truespeech
special_qualities:
- planar infusion (300 ft.)
desc_long: These planar dragons establish bastions of order and transform lawless
  towns into shining examples of urban grandeur.

---

# Dragon (Planar, Edict), Ancient Edict Dragon

**Source** Pathfinder #131: The Reaper's Right Hand pg. 89
**XP** 409,600

LN Gargantuan dragon (extraplanar, lawful)
**Init** +2; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +40
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 31)

##### Defense

**AC** 41, touch 4, _[[conditions/Flat-Footed|flat-footed]]_ 41 (–2 Dex, +35 natural, +2 _[[spells/Shield|shield]]_, –4 size)
**hp** 434 (28d12+252)
**Fort** +25, **Ref** +16, **Will** +25
**Defensive Abilities** parapet wings; **DR** 15/chaotic; **Immune** disease, _[[universal monster rules/Fear|fear]]_, _[[universal monster rules/Paralysis|paralysis]]_, poison, sleep; **SR** 34

##### Offense
**Speed** 60 ft. fly 250 ft. (clumsy)
**Melee** bite +38 (4d6+14/19–20), 2 claws +38 (2d8+14), tail slap +33 (sweeping scrawl), 2 wings +39 (2d6+7)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (120-foot line, 20d10 slashing damage, Reflex DC 33 half), crush, hindering shards, master scrivener, _[[feats/Powerful Wings|powerful wings]]_, scrivener, sweeping scrawl, tail sweep
**_[[classes/Oracle|Oracle]]_ Spells Known** (CL 15th; concentration +22)
7th (5/day)—_[[spells/Dictum|dictum]]_ (DC 24), _[[spells/Repulsion|repulsion]]_ (DC 24) 
6th (7/day)—geas/quest, _[[spells/Heal|heal]]_, _[[spells/Symbol of Fear|symbol of fear]]_ (DC 23) 
5th (7/day)—_[[spells/Dispel Chaos|dispel chaos]]_, _[[spells/Mark of Justice|mark of justice]]_, _[[spells/Symbol of Pain|symbol of pain]]_ (DC 22), _[[spells/True Seeing|true seeing]]_ 
4th (7/day)—_[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Dismissal|dismissal]]_ (DC 21), order’s wrath (DC 21), _[[spells/Sending|sending]]_ 
3rd (8/day)—_[[spells/Bestow Curse|bestow curse]]_ (DC 20), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Glyph Of Warding|glyph of warding]]_ (DC 20), _[[spells/Stone Shape|stone shape]]_ 
2nd (8/day)—_[[spells/Calm Emotions|calm emotions]]_ (DC 19), _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Make Whole|make whole]]_, _[[spells/Resist Energy|resist energy]]_, _[[spells/Silence|silence]]_ (DC 19) 
1st (8/day)—_[[spells/Command|command]]_ (DC 18), _[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Detect Chaos|detect chaos]]_, _[[spells/Remove Fear|remove fear]]_, _[[spells/Shield Of Faith|shield of faith]]_ 
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, light, _[[spells/Mending|mending]]_, _[[spells/Purify Food and Drink|purify food and drink]]_, _[[spells/Read Magic|read magic]]_, stabilize

##### Statistics
**Str** 39, **Dex** 6, **Con** 29, **Int** 24, **Wis** 29, **Cha** 24
**Base Atk** +28; **CMB** +46 (+50 reposition); **CMD** 58 (60 vs. reposition, 62 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Crippling Critical|Crippling Critical]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Reposition|Greater Reposition]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Reposition|Improved Reposition]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Repositioning Strike|Repositioning Strike]]_, _[[feats/Stand Still|Stand Still]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (wing)
**Skills** Diplomacy +38, Fly +15, Intimidate +38, Knowledge (engineering, history, local, nobility, planes) +38, Linguistics +38, Perception +40, Sense Motive +40, Spellcraft +38, Survival +40
**Languages** Common, Draconic, plus any 28 others; truespeech
**SQ** _[[feats/Planar Infusion|planar infusion]]_ (300 ft.)

##### Description

These _[[items/Weapon Magic Abilities/Planar|planar]]_ dragons establish bastions of order and transform lawless towns into shining examples of urban grandeur.
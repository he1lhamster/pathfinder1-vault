---
cssclass: [monsters]
title1: Dragon (Planar, Edict), Adult Edict Dragon
title2: Adult Edict Dragon
CR: 16
sources:
- name: "Pathfinder #131: The Reaper's Right Hand"
  page: 88
  link: http://paizo.com/products/btpy9x04?Pathfinder-Adventure-Path-The-Reaper-s-Right-Hand
XP: 76800
alignment: LN
size: Huge
type: dragon
subtypes:
- extraplanar
- lawful
initiative:
  bonus: 3
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 180
  DC: 25
AC:
  AC: 32
  touch: 7
  flat_footed: 32
  components:
    dex: -1
    natural: 23
    shield: 2
    size: -2
HP:
  HP: 270
  long: 20d10+140
saves:
  fort: 19
  ref: 13
  will: 19
defensive_abilities:
- parapet wings
DR:
- amount: 5
  weakness: chaotic
immunities:
- disease
- fear
- paralysis
- poison
- sleep
SR: 29
speeds:
  base: 60
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +28 (2d8+15/19-20)
      entries:
      - - damage: 2d8+15
          crit_range: 19-20
      attack: bite
      bonus:
      - 28
    - text: 2 claws +28 (2d6+10)
      entries:
      - - damage: 2d6+10
      count: 2
      attack: claws
      bonus:
      - 28
    - text: tail slap +23 (scrivener)
      entries:
      - - effect: scrivener
      attack: tail slap
      bonus:
      - 23
    - text: 2 wings +29 (1d8+10)
      entries:
      - - damage: 1d8+10
      count: 2
      attack: wings
      bonus:
      - 29
  special:
  - breath weapon (100-foot line, 12d10 slashing damage, Reflex DC 27 half)
  - crush
  - hindering shards
  - powerful wings
  - scrivener
  - tail sweep
space: 15
reach: 10
reach_other: 15 ft. with bite
spells:
  entries:
  - name: bestow curse
    source: Oracle
    level: 3
    DC: 18
  - name: dispel magic
    source: Oracle
    level: 3
  - name: calm emotions
    source: Oracle
    level: 2
    DC: 17
  - name: cure moderate wounds
    source: Oracle
    level: 2
  - name: resist energy
    source: Oracle
    level: 2
  - name: command
    source: Oracle
    level: 1
    DC: 16
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
  - name: detect magic
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
    CL: 7
    concentration: 12
    slots:
      3: 5
      2: 7
      1: 8
      0: at-will
ability_scores:
  STR: 31
  DEX: 8
  CON: 25
  INT: 20
  WIS: 25
  CHA: 20
BAB: 20
CMB: 32
CMB_other: +34 reposition
CMD: 45
CMD_other: 47 vs. reposition, 49 vs. trip
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Hover
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Reposition
- name: Lightning Reflexes
- name: Repositioning Strike
- name: Stand Still
- name: Weapon Focus (wing)
skills:
  Diplomacy: 28
  Fly: 14
  Knowledge (engineering): 28
  Knowledge (history): 28
  Knowledge (local): 28
  Knowledge (nobility): 28
  Knowledge (planes): 28
  Linguistics: 28
  Perception: 30
  Sense Motive: 30
  Spellcraft: 28
languages:
- Common
- Draconic
- plus any 20 others
- truespeech
special_qualities:
- planar infusion (180 ft.)
desc_long: These planar dragons establish bastions of order and transform lawless
  towns into shining examples of urban grandeur.

---

# Dragon (Planar, Edict), Adult Edict Dragon

**Source** Pathfinder #131: The Reaper's Right Hand pg. 88
**XP** 76,800

LN Huge dragon (extraplanar, lawful)
**Init** +3; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +30
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 25)

##### Defense

**AC** 32, touch 7, _[[conditions/Flat-Footed|flat-footed]]_ 32 (–1 Dex, +23 natural, +2 _[[spells/Shield|shield]]_, –2 size)
**hp** 270 (20d10+140)
**Fort** +19, **Ref** +13, **Will** +19
**Defensive Abilities** parapet wings; **DR** 5/chaotic; **Immune** disease, _[[universal monster rules/Fear|fear]]_, _[[universal monster rules/Paralysis|paralysis]]_, poison, sleep; **SR** 29

##### Offense
**Speed** 60 ft., fly 200 ft. (poor)
**Melee** bite +28 (2d8+15/19–20), 2 claws +28 (2d6+10), tail slap +23 (scrivener), 2 wings +29 (1d8+10)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (100-foot line, 12d10 slashing damage, Reflex DC 27 half), crush, hindering shards, _[[feats/Powerful Wings|powerful wings]]_, scrivener, tail sweep
**_[[classes/Oracle|Oracle]]_ Spells Known** (CL 7th; concentration +12)
3rd (5/day)—_[[spells/Bestow Curse|bestow curse]]_ (DC 18), _[[spells/Dispel Magic|dispel magic]]_ 
2nd (7/day)—_[[spells/Calm Emotions|calm emotions]]_ (DC 17), _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Resist Energy|resist energy]]_ 
1st (8/day)—_[[spells/Command|command]]_ (DC 16), _[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Detect Chaos|detect chaos]]_, _[[spells/Remove Fear|remove fear]]_, _[[spells/Shield Of Faith|shield of faith]]_ 
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, light, _[[spells/Mending|mending]]_, _[[spells/Purify Food and Drink|purify food and drink]]_, _[[spells/Read Magic|read magic]]_, stabilize

##### Statistics
**Str** 31, **Dex** 8, **Con** 25, **Int** 20, **Wis** 25, **Cha** 20
**Base Atk** +20; **CMB** +32 (+34 reposition); **CMD** 45 (47 vs. reposition, 49 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Reposition|Improved Reposition]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Repositioning Strike|Repositioning Strike]]_, _[[feats/Stand Still|Stand Still]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (wing)
**Skills** Diplomacy +28, Fly +14, Knowledge (engineering, history, local, nobility, planes) +28, Linguistics +28, Perception +30, Sense Motive +30, Spellcraft +28
**Languages** Common, Draconic, plus any 20 others; truespeech
**SQ** _[[feats/Planar Infusion|planar infusion]]_ (180 ft.)

##### Description

These _[[items/Weapon Magic Abilities/Planar|planar]]_ dragons establish bastions of order and transform lawless towns into shining examples of urban grandeur.
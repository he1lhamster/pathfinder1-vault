---
cssclass: [monsters]
title1: Dragon (Planar, Bliss), Young Bliss Dragon
desc_short: This serene dragon's feathered form emits a comforting warmth.
title2: Young Bliss Dragon
CR: 12
sources:
- name: 'Pathfinder #137: The City Outside of Time'
  page: 90
  link: https://paizo.com/products/btq01vak
XP: 19200
alignment: NG
size: Large
type: dragon
subtypes:
- extraplanar
- good
initiative:
  bonus: 5
senses:
  dragon sense: true
AC:
  AC: 25
  touch: 10
  flat_footed: 24
  components:
    dex: 1
    natural: 15
    size: -1
HP:
  HP: 161
  long: 14d12+70
saves:
  fort: 14
  ref: 10
  will: 12
immunities:
- ability damage
- ability drain
- electricity
- paralysis
- petrification
- sleep
speeds:
  base: 60
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +19 (2d6+9)
      entries:
      - - damage: 2d6+9
      attack: bite
      bonus:
      - 19
    - text: 2 claws +20 (1d8+6/19-20)
      entries:
      - - damage: 1d8+6
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 20
    - text: tail slap +14 (1d8+9)
      entries:
      - - damage: 1d8+9
      attack: tail slap
      bonus:
      - 14
    - text: 2 wings +14 (1d6+3)
      entries:
      - - damage: 1d6+3
      count: 2
      attack: wings
      bonus:
      - 14
  special:
  - breath weapon (80-ft. line, 6d10 electricity, DC 22)
  - subduing strikes
space: 10
reach: 5
reach_other: 10 ft. with bite
spells:
  entries:
  - name: remove fear
    source: Oracle
    level: 1
  - name: sanctuary
    source: Oracle
    level: 1
    DC: 16
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
  sources:
  - name: Oracle
    type: known
    CL: 1
    concentration: 6
    slots:
      1: 5
      0: at-will
ability_scores:
  STR: 23
  DEX: 12
  CON: 21
  INT: 16
  WIS: 17
  CHA: 20
BAB: 14
CMB: 21
CMB_other: +23 disarm
CMD: 32
CMD_other: 34 vs. disarm, 36 vs. trip
feats:
- name: Alertness
- name: Combat Expertise
- name: Imp. Critical (claw)
- name: Imp. Disarm
- name: Imp. Initiative
- name: Self-Sufficient
- name: Weapon Focus (claw)
skills:
  Diplomacy: 22
  Fly: 12
  Heal: 24
  Knowledge (nature): 20
  Knowledge (planes): 20
  Perception: 24
  Sense Motive: 24
  Spellcraft: 20
  Survival: 24
languages:
- Celestial
- Common
- Draconic
special_qualities:
- change shape
- lay on hands (7d6, 12/day)
desc_long: Bliss dragons are self-appointed wardens of wildlife and wilderness, sometimes
  even displacing fey and magical beasts whose ethics fall short of the dragons' high
  standards. Bliss dragons often sequester refugees in their extraplanar glades, granting
  sanctuary and healing to those in need.

---

# Dragon (Planar, Bliss), Young Bliss Dragon
This serene dragon’s feathered form emits a comforting warmth.
**Source** Pathfinder #137: The City Outside of Time pg. 90
**XP** 19,200

NG Large dragon (extraplanar, good)
**Init** +5; **Senses** dragon sense; Perception +24

##### Defense

**AC** 25, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+1 Dex, +15 natural, –1 size)
**hp** 161 (14d12+70)
**Fort** +14, **Ref** +10, **Will** +12
**Immune** ability damage, ability drain, electricity, _[[universal monster rules/Paralysis|paralysis]]_, petrification, sleep

##### Offense
**Speed** 60 ft., fly 200 ft. (poor)
**Melee** bite +19 (2d6+9), 2 claws +20 (1d8+6/19–20), tail slap +14 (1d8+9), 2 wings +14 (1d6+3)
**Space** 10 ft., **Reach** 5 ft. (10 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (80-ft. line, 6d10 electricity, DC 22), subduing strikes
**_[[classes/Oracle|Oracle]]_ Spells Known** (CL 1st; concentration +6)
1st (5/day)—_[[spells/Remove Fear|remove fear]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 16) 
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, light

##### Statistics
**Str** 23, **Dex** 12, **Con** 21, **Int** 16, **Wis** 17, **Cha** 20
**Base Atk** +14; **CMB** +21 (+23 disarm); **CMD** 32 (34 vs. disarm, 36 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Expertise|Combat Expertise]]_, Imp. Critical (claw), Imp. Disarm, Imp. Initiative, _[[feats/Self-Sufficient|Self-Sufficient]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Diplomacy +22, Fly +12, _[[spells/Heal|Heal]]_ +24, Knowledge (nature, planes) +20, Perception +24, Sense Motive +24, Spellcraft +20, Survival +24
**Languages** Celestial, Common, Draconic
**SQ** _[[universal monster rules/Change Shape|change shape]]_, lay on hands (7d6, 12/day)

##### Description

Bliss dragons are self-appointed wardens of wildlife and wilderness, sometimes even displacing fey and magical beasts whose ethics fall short of the dragons’ high standards. Bliss dragons often _[[spells/Sequester|sequester]]_ refugees in their extraplanar glades, granting _sanctuary_ and healing to those in need.
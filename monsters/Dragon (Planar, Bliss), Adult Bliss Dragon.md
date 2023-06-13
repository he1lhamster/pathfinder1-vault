---
cssclass: [monsters]
title1: Dragon (Planar, Bliss), Adult Bliss Dragon
desc_short: This serene dragon's feathered form emits a comforting warmth.
title2: Adult Bliss Dragon
CR: 16
sources:
- name: 'Pathfinder #137: The City Outside of Time'
  page: 90
  link: https://paizo.com/products/btq01vak
XP: 76800
alignment: NG
size: Huge
type: dragon
subtypes:
- extraplanar
- good
initiative:
  bonus: 4
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 180
  DC: 27
AC:
  AC: 32
  touch: 8
  flat_footed: 32
  components:
    natural: 24
    size: -2
HP:
  HP: 270
  long: 20d12+140
saves:
  fort: 19
  ref: 12
  will: 17
DR:
- amount: 5
  weakness: evil
immunities:
- ability damage
- ability drain
- electricity
- paralysis
- petrification
- sleep
SR: 27
speeds:
  base: 60
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +27 (2d8+13)
      entries:
      - - damage: 2d8+13
      attack: bite
      bonus:
      - 27
    - text: 2 claws +28 (2d6+9/19-20)
      entries:
      - - damage: 2d6+9
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 28
    - text: tail slap +22 (2d6+13)
      entries:
      - - damage: 2d6+13
      attack: tail slap
      bonus:
      - 22
    - text: 2 wings +22 (1d8+4)
      entries:
      - - damage: 1d8+4
      count: 2
      attack: wings
      bonus:
      - 22
  special:
  - breath weapon (100-ft. line, 12d10 electricity, DC 27)
  - crush
  - peacemaker
  - subduing strikes
space: 15
reach: 10
reach_other: 15 ft. with bite
spells:
  entries:
  - name: dispel magic
    source: Oracle
    level: 3
  - name: wind wall
    source: Oracle
    level: 3
  - name: bull's strength
    source: Oracle
    level: 2
  - name: calm emotions
    source: Oracle
    level: 2
    DC: 19
  - name: status
    source: Oracle
    level: 2
  - name: deathwatch
    source: Oracle
    level: 1
  - name: divine favor
    source: Oracle
    level: 1
  - name: remove fear
    source: Oracle
    level: 1
  - name: sanctuary
    source: Oracle
    level: 1
    DC: 18
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
  - name: stabilizestabilize
    source: Oracle
    level: 0
  sources:
  - name: Oracle
    type: known
    CL: 7
    concentration: 14
    slots:
      3: 6
      2: 8
      1: 8
      0: at-will
ability_scores:
  STR: 29
  DEX: 10
  CON: 25
  INT: 20
  WIS: 21
  CHA: 24
BAB: 20
CMB: 31
CMB_other: +35 disarm
CMD: 41
CMD_other: 43 vs. disarm, 45 vs. trip
feats:
- name: Alertness
- name: Combat Expertise
- name: Critical Focus
- name: Greater Disarm
- name: Improved Critical (claw)
- name: Improved Disarm
- name: Improved Initiative
- name: Self-Sufficient
- name: Sickening Critical
- name: Weapon Focus (claw)
skills:
  Diplomacy: 30
  Fly: 15
  Heal: 32
  Knowledge (geography): 28
  Knowledge (nature): 28
  Knowledge (planes): 28
  Perception: 32
  Sense Motive: 32
  Spellcraft: 28
  Stealth: 15
  Survival: 32
languages:
- Celestial
- Common
- Draconic
special_qualities:
- change shape
- lay on hands (10d6, 17/day)
- planar infusion (180 ft.)
desc_long: Bliss dragons are self-appointed wardens of wildlife and wilderness, sometimes
  even displacing fey and magical beasts whose ethics fall short of the dragons' high
  standards. Bliss dragons often sequester refugees in their extraplanar glades, granting
  sanctuary and healing to those in need.

---

# Dragon (Planar, Bliss), Adult Bliss Dragon
This serene dragon’s feathered form emits a comforting warmth.
**Source** Pathfinder #137: The City Outside of Time pg. 90
**XP** 76,800

NG Huge dragon (extraplanar, good)
**Init** +4; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +32
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 27)

##### Defense

**AC** 32, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 32 (+24 natural, –2 size)
**hp** 270 (20d12+140)
**Fort** +19, **Ref** +12, **Will** +17
**DR** 5/evil; **Immune** ability damage, ability drain, electricity, _[[universal monster rules/Paralysis|paralysis]]_, petrification, sleep; **SR** 27

##### Offense
**Speed** 60 ft., fly 200 ft. (poor)
**Melee** bite +27 (2d8+13), 2 claws +28 (2d6+9/19–20), tail slap +22 (2d6+13), 2 wings +22 (1d8+4)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (100-ft. line, 12d10 electricity, DC 27), crush, _[[feats/Peacemaker|peacemaker]]_, subduing strikes
**_[[classes/Oracle|Oracle]]_ Spells Known** (CL 7th; concentration +14)
3rd (6/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Wind Wall|wind wall]]_ 
2nd (8/day)—bull’s strength, _[[spells/Calm Emotions|calm emotions]]_ (DC 19), _[[spells/Status|status]]_ 
1st (8/day)—_[[spells/Deathwatch|deathwatch]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Remove Fear|remove fear]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 18), _[[spells/Shield Of Faith|shield of faith]]_ 
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, light, _[[spells/Mending|mending]]_, stabilizestabilize

##### Statistics
**Str** 29, **Dex** 10, **Con** 25, **Int** 20, **Wis** 21, **Cha** 24
**Base Atk** +20; **CMB** +31 (+35 disarm); **CMD** 41 (43 vs. disarm, 45 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Disarm|Greater Disarm]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Self-Sufficient|Self-Sufficient]]_, _[[feats/Sickening Critical|Sickening Critical]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Diplomacy +30, Fly +15, _[[spells/Heal|Heal]]_ +32, Knowledge (geography, nature, planes) +28, Perception +32, Sense Motive +32, Spellcraft +28, Stealth +15, Survival +32
**Languages** Celestial, Common, Draconic
**SQ** _[[universal monster rules/Change Shape|change shape]]_, lay on hands (10d6, 17/day), _[[feats/Planar Infusion|planar infusion]]_ (180 ft.)

##### Description

Bliss dragons are self-appointed wardens of wildlife and wilderness, sometimes even displacing fey and magical beasts whose ethics fall short of the dragons’ high standards. Bliss dragons often _[[spells/Sequester|sequester]]_ refugees in their extraplanar glades, granting _sanctuary_ and healing to those in need.
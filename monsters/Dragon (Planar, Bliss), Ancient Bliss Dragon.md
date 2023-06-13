---
cssclass: [monsters]
title1: Dragon (Planar, Bliss), Ancient Bliss Dragon
desc_short: This serene dragon's feathered form emits a comforting warmth.
title2: Ancient Bliss Dragon
CR: 21
sources:
- name: 'Pathfinder #137: The City Outside of Time'
  page: 91
  link: https://paizo.com/products/btq01vak
XP: 409600
alignment: NG
size: Gargantuan
type: dragon
subtypes:
- extraplanar
- good
initiative:
  bonus: 3
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 300
  DC: 33
AC:
  AC: 41
  touch: 5
  flat_footed: 41
  components:
    dex: -1
    natural: 36
    size: -4
HP:
  HP: 434
  long: 28d12+252
saves:
  fort: 25
  ref: 17
  will: 23
DR:
- amount: 15
  weakness: evil
immunities:
- ability damage
- ability drain
- electricity
- paralysis
- petrification
- sleep
SR: 32
speeds:
  base: 60
  fly: 250
  fly_maneuverability: clumsy
attacks:
  melee:
  - - text: bite +37 (4d6+19)
      entries:
      - - damage: 4d6+19
      attack: bite
      bonus:
      - 37
    - text: 2 claws +38 (2d8+13/19-20)
      entries:
      - - damage: 2d8+13
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 38
    - text: tail slap +32 (2d8+19)
      entries:
      - - damage: 2d8+19
      attack: tail slap
      bonus:
      - 32
    - text: 2 wings +32 (2d6+6)
      entries:
      - - damage: 2d6+6
      count: 2
      attack: wings
      bonus:
      - 32
  special:
  - breath weapon (120-ft. line, 20d10 electricity, DC 33)
  - crush
  - peacemaker
  - sedating sparks
  - subduing strikes
  - tail sweep
space: 20
reach: 15
reach_other: 20 ft. with bith
spells:
  entries:
  - name: holy word
    source: Oracle
    level: 7
    DC: 26
  - name: waves of ecstasy
    source: Oracle
    level: 7
    DC: 28
  - name: find the path
    source: Oracle
    level: 6
  - name: heal
    source: Oracle
    level: 6
  - name: heroes' feast
    source: Oracle
    level: 6
  - name: dispel evil
    source: Oracle
    level: 5
  - name: life bubble
    source: Oracle
    level: 5
    DC: 24
  - name: serenity
    source: Oracle
    level: 5
    DC: 26
  - name: true seeing
    source: Oracle
    level: 5
  - name: dismissal
    source: Oracle
    level: 4
    DC: 23
  - name: freedom of movement
    source: Oracle
    level: 4
  - name: holy smite
    source: Oracle
    level: 4
    DC: 23
  - name: ride the waves
    source: Oracle
    level: 4
    DC: 23
  - name: cure serious wounds
    source: Oracle
    level: 3
  - name: dispel magic
    source: Oracle
    level: 3
  - name: searing light
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
    DC: 23
  - name: grace
    source: Oracle
    level: 2
  - name: resist energy
    source: Oracle
    level: 2
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
    DC: 20
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
  - name: resistance
    source: Oracle
    level: 0
  - name: stabilize
    source: Oracle
    level: 0
  sources:
  - name: Oracle
    type: known
    CL: 15
    concentration: 24
    slots:
      7: 5
      6: 7
      5: 8
      4: 8
      3: 8
      2: 8
      1: 9
      0: at-will
ability_scores:
  STR: 37
  DEX: 8
  CON: 29
  INT: 24
  WIS: 25
  CHA: 28
BAB: 28
CMB: 45
CMB_other: +49 disarm
CMD: 54
CMD_other: 56 vs. disarm, 58 vs. trip
feats:
- name: Alertness
- name: Combat Expertise
- name: Critical Focus
- name: Disarming Strike
- name: Greater Disarm
- name: Greater Spell Focus (enchantment)
- name: Improved Critical (claw)
- name: Improved Disarm
- name: Improved Initiative
- name: Lightning Reflexes
- name: Self-Sufficient
- name: Sickening Critical
- name: Spell Focus (enchantment)
- name: Weapon Focus (claw)
skills:
  Diplomacy: 40
  Fly: 16
  Heal: 42
  Intimidate: 40
  Knowledge (geography): 38
  Knowledge (nature): 38
  Knowledge (planes): 38
  Knowledge (religion): 38
  Perception: 42
  Sense Motive: 42
  Spellcraft: 38
  Stealth: 18
  Survival: 42
languages:
- Celestial
- Common
- Draconic
special_qualities:
- change shape
- lay on hands (14d6, 23/day)
- merciful
- planar infusion (300 ft.)
desc_long: Bliss dragons are self-appointed wardens of wildlife and wilderness, sometimes
  even displacing fey and magical beasts whose ethics fall short of the dragons' high
  standards. Bliss dragons often sequester refugees in their extraplanar glades, granting
  sanctuary and healing to those in need.

---

# Dragon (Planar, Bliss), Ancient Bliss Dragon
This serene dragon’s feathered form emits a comforting warmth.
**Source** Pathfinder #137: The City Outside of Time pg. 91
**XP** 409,600

NG Gargantuan dragon (extraplanar, good)
**Init** +3; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +42
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 33)

##### Defense

**AC** 41, touch 5, _[[conditions/Flat-Footed|flat-footed]]_ 41 (–1 Dex, +36 natural, –4 size)
**hp** 434 (28d12+252)
**Fort** +25, **Ref** +17, **Will** +23
**DR** 15/evil; **Immune** ability damage, ability drain, electricity, _[[universal monster rules/Paralysis|paralysis]]_, petrification, sleep; **SR** 32

##### Offense
**Speed** 60 ft., fly 250 ft. (clumsy)
**Melee** bite +37 (4d6+19), 2 claws +38 (2d8+13/19–20), tail slap +32 (2d8+19), 2 wings +32 (2d6+6)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bith)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (120-ft. line, 20d10 electricity, DC 33), crush, _[[feats/Peacemaker|peacemaker]]_, sedating sparks, subduing strikes, tail sweep
**_[[classes/Oracle|Oracle]]_ Spells Known** (CL 15th; concentration +24)
7th (5/day)—_[[spells/Holy Word|holy word]]_ (DC 26), _[[spells/Waves of Ecstasy|waves of ecstasy]]_ (DC 28) 
6th (7/day)—_[[spells/Find the Path|find the path]]_, _[[spells/Heal|heal]]_, heroes’ feast 
5th (8/day)—_[[spells/Dispel Evil|dispel evil]]_, _[[spells/Life Bubble|life bubble]]_ (DC 24), _[[spells/Serenity|serenity]]_ (DC 26), _[[spells/True Seeing|true seeing]]_ 
4th (8/day)—_[[spells/Dismissal|dismissal]]_ (DC 23), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Holy Smite|holy smite]]_ (DC 23), _[[spells/Ride The Waves|ride the waves]]_ (DC 23) 
3rd (8/day)—_[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Searing Light|searing light]]_, _[[spells/Wind Wall|wind wall]]_ 
2nd (8/day)—bull’s strength, _[[spells/Calm Emotions|calm emotions]]_ (DC 23), _[[spells/Grace|grace]]_, _[[spells/Resist Energy|resist energy]]_, _[[spells/Status|status]]_ 
1st (9/day)—_[[spells/Deathwatch|deathwatch]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Remove Fear|remove fear]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 20), _[[spells/Shield Of Faith|shield of faith]]_ 
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, light, _[[spells/Mending|mending]]_, _[[universal monster rules/Resistance|resistance]]_, stabilize

##### Statistics
**Str** 37, **Dex** 8, **Con** 29, **Int** 24, **Wis** 25, **Cha** 28
**Base Atk** +28; **CMB** +45 (+49 disarm); **CMD** 54 (56 vs. disarm, 58 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Disarming Strike|Disarming Strike]]_, _[[feats/Greater Disarm|Greater Disarm]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (enchantment), _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Self-Sufficient|Self-Sufficient]]_, _[[feats/Sickening Critical|Sickening Critical]]_, _[[feats/Spell Focus|Spell Focus]]_ (enchantment), _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Diplomacy +40, Fly +16, _Heal_ +42, Intimidate +40, Knowledge (geography, nature, planes, religion) +38, Perception +42, Sense Motive +42, Spellcraft +38, Stealth +18, Survival +42
**Languages** Celestial, Common, Draconic
**SQ** _[[universal monster rules/Change Shape|change shape]]_, lay on hands (14d6, 23/day), _[[items/Weapon Magic Abilities/Merciful|merciful]]_, _[[feats/Planar Infusion|planar infusion]]_ (300 ft.)

##### Description

Bliss dragons are self-appointed wardens of wildlife and wilderness, sometimes even displacing fey and magical beasts whose ethics fall short of the dragons’ high standards. Bliss dragons often _[[spells/Sequester|sequester]]_ refugees in their extraplanar glades, granting _sanctuary_ and healing to those in need.
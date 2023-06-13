---
cssclass: [monsters]
title1: Dragon (Planar, Tumult), Ancient Tumult Dragon
desc_short: This dragon seems to be made of parts from different creatures.
title2: Ancient Tumult Dragon
CR: 21
sources:
- name: 'Pathfinder #138: Rise of New Thassilon'
  page: 91
  link: https://paizo.com/products/btq01w1w
XP: 409600
alignment: CN
size: Gargantuan
type: dragon
subtypes:
- chaotic
- extraplanar
initiative:
  bonus: 3
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 300
  DC: 31
AC:
  AC: 40
  touch: 5
  flat_footed: 40
  components:
    dex: -1
    natural: 35
    size: -4
HP:
  HP: 462
  long: 28d12+280
saves:
  fort: 26
  ref: 17
  will: 23
defensive_abilities:
- adaptive form
DR:
- amount: 15
  weakness: lawful
immunities:
- paralysis
- sleep
- warpproof
SR: 32
speeds:
  base: 60
  climb: 60
  fly: 250
  fly_maneuverability: clumsy
  swim: 60
attacks:
  melee:
  - - text: bite +39 (4d6+21)
      entries:
      - - damage: 4d6+21
      attack: bite
      bonus:
      - 39
    - text: 2 claws +39 (2d8+14)
      entries:
      - - damage: 2d8+14
      count: 2
      attack: claws
      bonus:
      - 39
    - text: tail slap +36 (2d8+21)
      entries:
      - - damage: 2d8+21
      attack: tail slap
      bonus:
      - 36
    - text: 2 wings +37 (2d6+7)
      entries:
      - - damage: 2d6+7
      count: 2
      attack: wings
      bonus:
      - 37
  special:
  - breath weapon (60-ft. cone, 20d8, DC 34)
  - crush
  - entropic breath
  - flexible breath
  - tail sweep
  - transforming breath
  - vexing wings
space: 20
reach: 15
reach_other: 20 ft. with bite
spells:
  entries:
  - name: destruction
    source: Oracle
    level: 7
    DC: 24
  - name: word of chaos
    source: Oracle
    level: 7
  - name: animate objects
    source: Oracle
    level: 6
  - name: harm
    source: Oracle
    level: 6
    DC: 23
  - name: heal
    source: Oracle
    level: 6
  - name: dispel law
    source: Oracle
    level: 5
  - name: insect plague
    source: Oracle
    level: 5
  - name: plane shift
    source: Oracle
    level: 5
    DC: 22
  - name: wall of stone
    source: Oracle
    level: 5
  - name: chaos hammer
    source: Oracle
    level: 4
    DC: 21
  - name: dismissal
    source: Oracle
    level: 4
    DC: 21
  - name: freedom of movement
    source: Oracle
    level: 4
  - name: tongues
    source: Oracle
    level: 4
  - name: daylight
    source: Oracle
    level: 3
  - name: dispel magic
    source: Oracle
    level: 3
  - name: sands of time
    source: Oracle
    level: 3
  - name: stone shape
    source: Oracle
    level: 3
  - name: eagle's splendor
    source: Oracle
    level: 2
  - name: enthrall
    source: Oracle
    level: 2
    DC: 19
  - name: grace
    source: Oracle
    level: 2
  - name: lesser restoration
    source: Oracle
    level: 2
  - name: shatter
    source: Oracle
    level: 2
    DC: 19
  - name: bless
    source: Oracle
    level: 1
  - name: entropic shield
    source: Oracle
    level: 1
  - name: obscuring mist
    source: Oracle
    level: 1
  - name: ray of sickening
    source: Oracle
    level: 1
    DC: 18
  - name: shield of faith
    source: Oracle
    level: 1
  - name: bleed
    source: Oracle
    level: 0
    DC: 17
  - name: create water
    source: Oracle
    level: 0
  - name: detect magic
    source: Oracle
    level: 0
  - name: guidance
    source: Oracle
    level: 0
  - name: light
    source: Oracle
    level: 0
  - name: read magic
    source: Oracle
    level: 0
  - name: resistance
    source: Oracle
    level: 0
  - name: spark
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
  DEX: 8
  CON: 31
  INT: 22
  WIS: 25
  CHA: 24
BAB: 28
CMB: 46
CMB_other: +50 dirty trick
CMD: 55
CMD_other: 57 vs. dirty trick, 59 vs. trip
feats:
- name: Blind-Fight
- name: Combat Expertise
- name: Critical Focus
- name: Greater Dirty Trick
- name: Hover
- name: Improved Dirty Trick
- name: Improved Initiative
- name: Lightning Reflexes
- name: Multiattack
- name: Power Attack
- name: Sickening Critical
- name: Weapon Focus (bite)
- name: Weapon Focus (claw)
- name: Weapon Focus (wing)
skills:
  Acrobatics: 27
  Bluff: 38
  Climb: 22
  Fly: 20
  Knowledge (arcana): 37
  Knowledge (local): 37
  Knowledge (nature): 37
  Knowledge (planes): 37
  Perception: 38
  Perform (act): 35
  Perform (dance): 35
  Spellcraft: 37
  Swim: 22
  Use Magic Device: 38
languages:
- Common
- Draconic
- Protean
special_qualities:
- eccentric infusion
- planar infusion (300 ft.)
desc_long: These planar dragons seek out dynamic and changing places, imposing their
  own whimsical will when those sites no longer intrigue them.

---

# Dragon (Planar, Tumult), Ancient Tumult Dragon
This dragon seems to be made of parts from different creatures.
**Source** Pathfinder #138: Rise of New Thassilon pg. 91
**XP** 409,600

CN Gargantuan dragon (chaotic, extraplanar)
**Init** +3; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +38
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 31)

##### Defense

**AC** 40, touch 5, _[[conditions/Flat-Footed|flat-footed]]_ 40 (–1 Dex, +35 natural, –4 size)
**hp** 462 (28d12+280)
**Fort** +26, **Ref** +17, **Will** +23
**Defensive Abilities** adaptive form; **DR** 15/lawful; **Immune** _[[universal monster rules/Paralysis|paralysis]]_, sleep, warpproof; **SR** 32

##### Offense
**Speed** 60 ft., _[[universal monster rules/Climb|climb]]_ 60 ft., fly 250 ft. (clumsy), swim 60 ft.
**Melee** bite +39 (4d6+21), 2 claws +39 (2d8+14), tail slap +36 (2d8+21), 2 wings +37 (2d6+7)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, 20d8, DC 34), crush, entropic breath, flexible breath, tail sweep, transforming breath, vexing wings
**_[[classes/Oracle|Oracle]]_ Spells Known** (CL 15th; concentration +22)
7th (5/day)—_[[spells/Destruction|destruction]]_ (DC 24), _[[spells/Word Of Chaos|word of chaos]]_ 
6th (7/day)—_[[spells/Animate Objects|animate objects]]_, _[[spells/Harm|harm]]_ (DC 23), _[[spells/Heal|heal]]_ 
5th (7/day)—_[[spells/Dispel Law|dispel law]]_, _[[spells/Insect Plague|insect plague]]_, _[[spells/Plane Shift|plane shift]]_ (DC 22), _[[spells/Wall Of Stone|wall of stone]]_ 
4th (7/day)—_[[spells/Chaos Hammer|chaos hammer]]_ (DC 21), _[[spells/Dismissal|dismissal]]_ (DC 21), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Tongues|tongues]]_ 
3rd (8/day)—_[[spells/Daylight|daylight]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Sands of Time|sands of time]]_, _[[spells/Stone Shape|stone shape]]_ 
2nd (8/day)—_[[monsters/Eagle|eagle]]_’s splendor, _[[spells/Enthrall|enthrall]]_ (DC 19), _[[spells/Grace|grace]]_, lesser _[[spells/Restoration|restoration]]_, _[[spells/Shatter|shatter]]_ (DC 19) 
1st (8/day)—_[[spells/Bless|bless]]_, _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Ray of Sickening|ray of sickening]]_ (DC 18), _[[spells/Shield Of Faith|shield of faith]]_ 
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 17), _[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, light, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Spark|spark]]_

##### Statistics
**Str** 39, **Dex** 8, **Con** 31, **Int** 22, **Wis** 25, **Cha** 24
**Base Atk** +28; **CMB** +46 (+50 dirty trick); **CMD** 55 (57 vs. dirty trick, 59 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Dirty Trick|Greater Dirty Trick]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Dirty Trick|Improved Dirty Trick]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Sickening Critical|Sickening Critical]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite, claw, wing)
**Skills** Acrobatics +27, Bluff +38, _Climb_ +22, Fly +20, Knowledge (arcana, local, nature, planes) +37, Percept. +38, Perform (act, dance) +35, Spellcraft +37, Swim +22, Use Magic Device +38
**Languages** Common, Draconic, Protean
**SQ** eccentric infusion, _[[feats/Planar Infusion|planar infusion]]_ (300 ft.)

##### Description

These _[[items/Weapon Magic Abilities/Planar|planar]]_ dragons seek out dynamic and changing places, imposing their own whimsical will when those sites no longer intrigue them.
---
cssclass: [monsters]
title1: Dragon (Planar, Apocalypse), Adult Apocalypse Dragon
desc_short: Gangrenous wounds mar this dragon's twisted body.
title2: Adult Apocalypse Dragon
CR: 16
sources:
- name: 'Pathfinder #137: The City Outside of Time'
  page: 88
  link: https://paizo.com/products/btq01vak
XP: 76800
alignment: NE
size: Huge
type: dragon
subtypes:
- evil
- extraplanar
initiative:
  bonus: 4
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 180
  DC: 25
AC:
  AC: 31
  touch: 8
  flat_footed: 31
  components:
    natural: 23
    size: -2
HP:
  HP: 250
  long: 20d12+120
saves:
  fort: 18
  ref: 14
  will: 19
DR:
- amount: 5
  weakness: good
immunities:
- cold
- death effects
- disease
- paralysis
- poison
- sleep
SR: 27
speeds:
  base: 60
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +30 (2d8+18 plus grab)
      entries:
      - - damage: 2d8+18
        - effect: grab
      attack: bite
      bonus:
      - 30
    - text: 2 claws +30 (2d6+12)
      entries:
      - - damage: 2d6+12
      count: 2
      attack: claws
      bonus:
      - 30
    - text: tail slap +28 (2d6+18/19-20)
      entries:
      - - damage: 2d6+18
          crit_range: 19-20
      attack: tail slap
      bonus:
      - 28
  special:
  - blight coils
  - breath weapon (50-ft. cone, 12d6 cold plus disease, DC 25)
  - constrict (2d8+18)
  - crush
  - virulence
space: 15
reach: 10
reach_other: 15 ft. with bite
spells:
  entries:
  - name: bestow curse
    source: Oracle
    level: 3
    DC: 18
  - name: contagion
    source: Oracle
    level: 3
    DC: 18
  - name: aid
    source: Oracle
    level: 2
  - name: darkness
    source: Oracle
    level: 2
  - name: disfiguring touch
    source: Oracle
    level: 2
    DC: 17
  - name: doom
    source: Oracle
    level: 1
    DC: 16
  - name: endure elements
    source: Oracle
    level: 1
  - name: obscuring mist
    source: Oracle
    level: 1
  - name: protection from good
    source: Oracle
    level: 1
  - name: ray of sickening
    source: Oracle
    level: 1
    DC: 16
  - name: bleed
    source: Oracle
    level: 0
    DC: 15
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
  - name: read magic
    source: Oracle
    level: 0
  - name: spark
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
  STR: 35
  DEX: 10
  CON: 23
  INT: 20
  WIS: 21
  CHA: 20
BAB: 20
CMB: 24
CMD: 44
CMD_other: 48 vs. trip
feats:
- name: Cleave
- name: Critical Focus
- name: Improved Critical (tail slap)
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Lunge
- name: Multiattack
- name: Power Attack
- name: Tiring Critical
skills:
  Bluff: 28
  Fly: 15
  Intimidate: 28
  Knowledge (planes): 28
  Knowledge (religion): 28
  Perception: 28
  Sense Motive: 28
  Spellcraft: 28
  Stealth: 15
  Survival: 28
  Use Magic Device: 28
languages:
- Abyssal
- Common
- Draconic
- Infernal
special_qualities:
- planar infusion (180 ft.)
desc_long: These planar dragons ravage places of growth, life, and fecundity.

---

# Dragon (Planar, Apocalypse), Adult Apocalypse Dragon
Gangrenous wounds mar this dragon’s twisted body.
**Source** Pathfinder #137: The City Outside of Time pg. 88
**XP** 76,800

NE Huge dragon (evil, extraplanar)
**Init** +4; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +28
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 25)

##### Defense

**AC** 31, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 31 (+23 natural, –2 size)
**hp** 250 (20d12+120)
**Fort** +18, **Ref** +14, **Will** +19
**DR** 5/good; **Immune** cold, death effects, disease, _[[universal monster rules/Paralysis|paralysis]]_, poison, sleep; **SR** 27

##### Offense
**Speed** 60 ft., fly 200 ft. (poor)
**Melee** bite +30 (2d8+18 plus _[[universal monster rules/Grab|grab]]_), 2 claws +30 (2d6+12), tail slap +28 (2d6+18/19–20)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** _[[spells/Blight|blight]]_ coils, _[[universal monster rules/Breath Weapon|breath weapon]]_ (50-ft. cone, 12d6 cold plus disease, DC 25), _[[universal monster rules/Constrict|constrict]]_ (2d8+18), crush, _[[spells/Virulence|virulence]]_
**_[[classes/Oracle|Oracle]]_ Spells Known** (CL 7th; concentration +12)
3rd (5/day)—_[[spells/Bestow Curse|bestow curse]]_ (DC 18), _[[spells/Contagion|contagion]]_ (DC 18) 
2nd (7/day)—aid, _[[spells/Darkness|darkness]]_, _[[spells/Disfiguring Touch|disfiguring touch]]_ (DC 17) 
1st (8/day)—_[[spells/Doom|doom]]_ (DC 16), _[[spells/Endure Elements|endure elements]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Protection From Good|protection from good]]_, _[[spells/Ray of Sickening|ray of sickening]]_ (DC 16) 
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, light, _[[spells/Read Magic|read magic]]_, _[[spells/Spark|spark]]_

##### Statistics
**Str** 35, **Dex** 10, **Con** 23, **Int** 20, **Wis** 21, **Cha** 20
**Base Atk** +20; **CMB** +24; **CMD** 44 (48 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (tail slap), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Tiring Critical|Tiring Critical]]_
**Skills** Bluff +28, Fly +15, Intimidate +28, Knowledge (planes, religion) +28, Perception +28, Sense Motive +28, Spellcraft +28, Stealth +15, Survival +28, Use Magic Device +28
**Languages** Abyssal, Common, Draconic, Infernal
**SQ** _[[feats/Planar Infusion|planar infusion]]_ (180 ft.)

##### Description

These _[[items/Weapon Magic Abilities/Planar|planar]]_ dragons ravage places of growth, life, and fecundity.
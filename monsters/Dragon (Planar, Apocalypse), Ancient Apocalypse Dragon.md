---
cssclass: [monsters]
title1: Dragon (Planar, Apocalypse), Ancient Apocalypse Dragon
desc_short: Gangrenous wounds mar this dragon's twisted body.
title2: Ancient Apocalypse Dragon
CR: 21
sources:
- name: 'Pathfinder #137: The City Outside of Time'
  page: 89
  link: https://paizo.com/products/btq01vak
XP: 409600
alignment: NE
size: Gargantuan
type: dragon
subtypes:
- evil
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
  HP: 406
  long: 28d12+224
saves:
  fort: 24
  ref: 17
  will: 25
DR:
- amount: 15
  weakness: good
immunities:
- cold
- death effects
- disease
- paralysis
- poison
- sleep
SR: 32
speeds:
  base: 60
  fly: 250
  fly_maneuverability: clumsy
attacks:
  melee:
  - - text: bite +40 (4d6+24/19-20 plus grab)
      entries:
      - - damage: 4d6+24
          crit_range: 19-20
        - effect: grab
      attack: bite
      bonus:
      - 40
    - text: 2 claws +40 (2d8+16)
      entries:
      - - damage: 2d8+16
      count: 2
      attack: claws
      bonus:
      - 40
    - text: tail slap +38 (2d8+24/19-20)
      entries:
      - - damage: 2d8+24
          crit_range: 19-20
      attack: tail slap
      bonus:
      - 38
  special:
  - blight coils
  - breath weapon (60-ft. cone, 20d6 cold plus disease, DC 31)
  - constrict (4d6+24)
  - crush
  - soul reaver
  - tail sweep
  - virulence
space: 20
reach: 15
reach_other: 20 ft. with bite
spells:
  entries:
  - name: blasphemy
    source: Oracle
    level: 7
    DC: 24
  - name: control weather
    source: Oracle
    level: 7
  - name: heal
    source: Oracle
    level: 6
  - name: plague storm
    source: Oracle
    level: 6
    DC: 23
  - name: word of recall
    source: Oracle
    level: 6
  - name: cleanse
    source: Oracle
    level: 5
  - name: dispel good
    source: Oracle
    level: 5
  - name: flame strike
    source: Oracle
    level: 5
    DC: 22
  - name: plane shift
    source: Oracle
    level: 5
    DC: 22
  - name: dimensional anchor
    source: Oracle
    level: 4
  - name: dismissal
    source: Oracle
    level: 4
    DC: 21
  - name: giant vermin
    source: Oracle
    level: 4
  - name: unholy blight
    source: Oracle
    level: 4
    DC: 21
  - name: bestow curse
    source: Oracle
    level: 3
    DC: 20
  - name: blindness/deafness
    source: Oracle
    level: 3
    DC: 20
  - name: contagion
    source: Oracle
    level: 3
    DC: 20
  - name: dispel magic
    source: Oracle
    level: 3
  - name: aid
    source: Oracle
    level: 2
  - name: darkness
    source: Oracle
    level: 2
  - name: death knell
    source: Oracle
    level: 2
    DC: 19
  - name: disfiguring touch
    source: Oracle
    level: 2
    DC: 19
  - name: silence
    source: Oracle
    level: 2
    DC: 19
  - name: doom
    source: Oracle
    level: 1
    DC: 18
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
    DC: 18
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
  STR: 43
  DEX: 8
  CON: 27
  INT: 24
  WIS: 25
  CHA: 24
BAB: 28
CMB: 48
CMD: 57
CMD_other: 61 vs. trip
feats:
- name: Cleave
- name: Critical Focus
- name: Exhausting Critical
- name: Improved Critical (bite)
- name: Improved Critical (tail slap)
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Lunge
- name: Multiattack
- name: Power Attack
- name: Snatch
- name: Tiring Critical
- name: Wingover
skills:
  Bluff: 38
  Fly: 16
  Intimidate: 38
  Knowledge (arcana): 38
  Knowledge (history): 38
  Knowledge (planes): 38
  Knowledge (religion): 38
  Perception: 38
  Sense Motive: 38
  Spellcraft: 38
  Stealth: 18
  Survival: 38
  Use Magic Device: 38
languages:
- Abyssal
- Common
- Draconic
- Infernal
special_qualities:
- planar infusion (300 ft.)
desc_long: These planar dragons ravage places of growth, life, and fecundity.

---

# Dragon (Planar, Apocalypse), Ancient Apocalypse Dragon
Gangrenous wounds mar this dragon’s twisted body.
**Source** Pathfinder #137: The City Outside of Time pg. 89
**XP** 409,600

NE Gargantuan dragon (evil, extraplanar)
**Init** +3; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +38
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 31)

##### Defense

**AC** 40, touch 5, _[[conditions/Flat-Footed|flat-footed]]_ 40 (–1 Dex, +35 natural, –4 size)
**hp** 406 (28d12+224)
**Fort** +24, **Ref** +17, **Will** +25
**DR** 15/good; **Immune** cold, death effects, disease, _[[universal monster rules/Paralysis|paralysis]]_, poison, sleep; **SR** 32

##### Offense
**Speed** 60 ft., fly 250 ft. (clumsy)
**Melee** bite +40 (4d6+24/19–20 plus _[[universal monster rules/Grab|grab]]_), 2 claws +40 (2d8+16), tail slap +38 (2d8+24/19–20)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite)
**Special Attacks** _[[spells/Blight|blight]]_ coils, _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, 20d6 cold plus disease, DC 31), _[[universal monster rules/Constrict|constrict]]_ (4d6+24), crush, soul reaver, tail sweep, _[[spells/Virulence|virulence]]_
**_[[classes/Oracle|Oracle]]_ Spells Known** (CL 15th; concentration +22)
7th (5/day)—_[[spells/Blasphemy|blasphemy]]_ (DC 24), _[[spells/Control Weather|control weather]]_ 
6th (7/day)—_[[spells/Heal|heal]]_, _[[spells/Plague Storm|plague storm]]_ (DC 23), _[[spells/Word of Recall|word of recall]]_ 
5th (7/day)—_[[spells/Cleanse|cleanse]]_, _[[spells/Dispel Good|dispel good]]_, _[[spells/Flame Strike|flame strike]]_ (DC 22), _[[spells/Plane Shift|plane shift]]_ (DC 22) 
4th (7/day)—_[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Dismissal|dismissal]]_ (DC 21), _[[spells/Giant Vermin|giant vermin]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 21) 
3rd (8/day)—_[[spells/Bestow Curse|bestow curse]]_ (DC 20), blindness/deafness (DC 20), _[[spells/Contagion|contagion]]_ (DC 20), _[[spells/Dispel Magic|dispel magic]]_ 
2nd (8/day)—aid, _[[spells/Darkness|darkness]]_, _[[spells/Death Knell|death knell]]_ (DC 19), _[[spells/Disfiguring Touch|disfiguring touch]]_ (DC 19), _[[spells/Silence|silence]]_ (DC 19) 
1st (8/day)—_[[spells/Doom|doom]]_ (DC 18), _[[spells/Endure Elements|endure elements]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Protection From Good|protection from good]]_, _[[spells/Ray of Sickening|ray of sickening]]_ (DC 18) 
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 17), _[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, light, _[[spells/Read Magic|read magic]]_, _[[spells/Spark|spark]]_

##### Statistics
**Str** 43, **Dex** 8, **Con** 27, **Int** 24, **Wis** 25, **Cha** 24
**Base Atk** +28; **CMB** +48; **CMD** 57 (61 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Exhausting Critical|Exhausting Critical]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite, tail slap), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Snatch|Snatch]]_, _[[feats/Tiring Critical|Tiring Critical]]_, _[[feats/Wingover|Wingover]]_
**Skills** Bluff +38, Fly +16, Intimidate +38, Knowledge (arcana, history, planes, religion) +38, Perception +38, Sense Motive +38, Spellcraft +38, Stealth +18, Survival +38, Use Magic Device +38
**Languages** Abyssal, Common, Draconic, Infernal
**SQ** _[[feats/Planar Infusion|planar infusion]]_ (300 ft.)

##### Description

These _[[items/Weapon Magic Abilities/Planar|planar]]_ dragons ravage places of growth, life, and fecundity.
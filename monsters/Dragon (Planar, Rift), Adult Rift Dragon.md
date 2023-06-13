---
cssclass: [monsters]
title1: Dragon (Planar, Rift), Adult Rift Dragon
desc_short: This dark-scaled dragon has massive claws, and foul-smellingacid drips
  from its saber teeth.
title2: Adult Rift Dragon
CR: 16
sources:
- name: Bestiary 6
  page: 106
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 76800
alignment: CE
size: Huge
type: dragon
subtypes:
- chaotic
- evil
- extraplanar
initiative:
  bonus: 4
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 180
  DC: 26
AC:
  AC: 31
  touch: 8
  flat_footed: 31
  components:
    natural: 23
    size: -2
HP:
  HP: 270
  long: 20d12+140
saves:
  fort: 19
  ref: 14
  will: 17
DR:
- amount: 5
  weakness: good
immunities:
- acid
- disease
- nausea
- paralysis
- poison,sleep
- stun
SR: 27
speeds:
  base: 60
  burrow: 30
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +30 (2d8+16/19-20 plus bleed)
      entries:
      - - damage: 2d8+16
          crit_range: 19-20
        - effect: bleed
      attack: bite
      bonus:
      - 30
    - text: 2 claws +29 (2d6+11plus bleed)
      entries:
      - - damage: 2d6+11
          type: plus bleed
      count: 2
      attack: claws
      bonus:
      - 29
    - text: tail slap +27 (2d6+16/19-20)
      entries:
      - - damage: 2d6+16
          crit_range: 19-20
      attack: tail slap
      bonus:
      - 27
    - text: 2 wings +27 (1d8+5)
      entries:
      - - damage: 1d8+5
      count: 2
      attack: wings
      bonus:
      - 27
  special:
  - abyssal juggernaut
  - bleed 6
  - breath weapon(50-ft. cone, 12d10 acid, Reflex DC 27 half)
  - corrosion
  - crush,foul acid
  - trample (2d8+16 plus bleed, DC 31)
space: 15
reach: 10
reach_other: 15 ft. with bite
spells:
  entries:
  - name: contagion
    source: Oracle
    level: 3
    DC: 19
  - name: deeper darkness
    source: Oracle
    level: 3
  - name: death knell
    source: Oracle
    level: 2
    DC: 18
  - name: hold person
    source: Oracle
    level: 2
    DC: 18
  - name: shatter
    source: Oracle
    level: 2
    DC: 18
  - name: bane
    source: Oracle
    level: 1
    DC: 17
  - name: cure light wounds
    source: Oracle
    level: 1
  - name: murderous command
    source: Oracle
    level: 1
    DC: 17
  - name: obscuring mist
    source: Oracle
    level: 1
  - name: shield of faith
    source: Oracle
    level: 1
  - name: bleed
    source: Oracle
    level: 0
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
  - name: read magic
    source: Oracle
    level: 0
  - name: resistance
    source: Oracle
    level: 0
  - name: spark
    source: Oracle
    level: 0
    DC: 16
  sources:
  - name: Oracle
    type: known
    CL: 7
    concentration: 13
    slots:
      3: 5
      2: 8
      1: 8
      0: at-will
ability_scores:
  STR: 33
  DEX: 10
  CON: 25
  INT: 18
  WIS: 21
  CHA: 22
BAB: 20
CMB: 33
CMD: 43
CMD_other: 47 vs. trip
feats:
- name: Critical Focus
- name: Improved Critical (bite)
- name: Improved Critical (tail slap)
- name: ImprovedInitiative
- name: Intimidating Prowess
- name: Lightning Reflexes
- name: Multiattack
- name: Power Attack
- name: Staggering Critical
- name: Weapon Focus (bite)
skills:
  Bluff: 29
  Fly: 15
  Intimidate: 40
  Knowledge (arcana,planes): 27
  Perception: 28
  Sense Motive: 28
  Spellcraft: 27
  Stealth: 15
  Use Magic Device: 29
languages:
- Abyssal
- Common
- Draconic
special_qualities:
- planar infusion (180 ft.)
desc_long: Wherever they go, rift dragons leave behind shattered ruins.These scaled
  terrors often intimidate local humanoid groupsinto worshiping them as demigods of
  destruction.

---

# Dragon (Planar, Rift), Adult Rift Dragon
This dark-scaled dragon has massive claws, and foul-smelling

acid drips from its saber teeth.
**Source** Bestiary 6 pg. 106
**XP** 76,800
CE Huge dragon (chaotic, evil, extraplanar)
**Init** +4; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +28
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 26)

##### Defense

**AC** 31, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 31 (+23 natural, –2 size)
**hp** 270 (20d12+140)
**Fort** +19, **Ref** +14, **Will** +17
**DR** 5/good; **Immune** acid, disease, nausea, _[[universal monster rules/Paralysis|paralysis]]_, poison,

sleep, stun; **SR** 27

##### Offense
**Speed** 60 ft., _[[universal monster rules/Burrow|burrow]]_ 30 ft., fly 200 ft. (poor)
**Melee** bite +30 (2d8+16/19–20 plus _[[universal monster rules/Bleed|bleed]]_), 2 claws +29 (2d6+11

plus _bleed_), tail slap +27 (2d6+16/19–20), 2 wings +27 (1d8+5)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** abyssal _[[monsters/Juggernaut|juggernaut]]_, _bleed_ 6, _[[universal monster rules/Breath Weapon|breath weapon]]_

(50-ft. cone, 12d10 acid, Reflex DC 27 half), corrosion, crush,

foul acid, _[[universal monster rules/Trample|trample]]_ (2d8+16 plus _bleed_, DC 31)
**_[[classes/Oracle|Oracle]]_ Spells Known** (CL 7th; concentration +13)
3rd (5)—_[[spells/Contagion|contagion]]_ (DC 19), _[[spells/Deeper Darkness|deeper darkness]]_ 
2nd (8)—_[[spells/Death Knell|death knell]]_ (DC 18), _[[spells/Hold Person|hold person]]_ (DC 18), _[[spells/Shatter|shatter]]_ (DC 18) 
1st (8)—_[[spells/Bane|bane]]_ (DC 17), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Murderous Command|murderous command]]_ (DC 17), _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shield Of Faith|shield of faith]]_ 
0 (at will)—_bleed_ (DC 16), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Spark|spark]]_ (DC 16)

##### Statistics
**Str** 33, **Dex** 10, **Con** 25, **Int** 18, **Wis** 21, **Cha** 22
**Base Atk** +20; **CMB** +33; **CMD** 43 (47 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite, tail slap), Improved

Initiative, _[[feats/Intimidating Prowess|Intimidating Prowess]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Bluff +29, Fly +15, Intimidate +40, Knowledge (arcana,

planes) +27, Perception +28, Sense Motive +28, Spellcraft +27,

Stealth +15, Use Magic Device +29
**Languages** Abyssal, Common, Draconic
**SQ** _[[feats/Planar Infusion|planar infusion]]_ (180 ft.)

##### Description

Wherever they go, rift dragons leave behind shattered ruins.

These scaled terrors often intimidate local humanoid groups

into worshiping them as demigods of _[[spells/Destruction|destruction]]_.
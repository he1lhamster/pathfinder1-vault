---
cssclass: [monsters]
title1: Daemon, Piscodaemon
desc_short: 'This hideous cross between a lobster, an octopus, and a human threatens
  enemies with powerful claws and writhing tentacles. '
title2: Piscodaemon
CR: 10
sources:
- name: Bestiary 2
  page: 72
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 9600
alignment: NE
size: Medium
type: outsider
subtypes:
- aquatic
- daemon
- evil
- extraplanar
initiative:
  bonus: 8
senses:
  darkvision: 60
  detect good: true
  detect magic: true
  see invisibility: true
AC:
  AC: 24
  touch: 14
  flat_footed: 20
  components:
    dex: 4
    natural: 10
HP:
  HP: 137
  long: 11d10+77
saves:
  fort: 14
  ref: 7
  will: 9
DR:
- amount: 10
  weakness: good
immunities:
- acid
- death effects
- disease
- poison
resistances:
  cold: 10
  electricity: 10
  fire: 10
SR: 21
speeds:
  base: 30
  swim: 50
attacks:
  melee:
  - - text: 2 claws +18 (2d6+7/18-20/×3 plus grab and 1d6 bleed)
      entries:
      - - damage: 2d6+7
          crit_range: 18-20
          crit_multiplier: 3
        - effect: grab
        - damage: 1d6
          type: bleed
      count: 2
      attack: claws
      bonus:
      - 18
    - text: tentacles +16 (1d10+3 plus poison)
      entries:
      - - damage: 1d10+3
        - effect: poison
      attack: tentacles
      bonus:
      - 16
  special:
  - constrict (2d6+10)
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: fly
    source: default
    freq: 3/day
  - name: stinking cloud
    source: default
    freq: 3/day
    DC: 16
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: hydrodaemons
      amount: 1d3
      chance: 35%
  sources:
  - name: default
    CL: 11
    concentration: 14
ability_scores:
  STR: 25
  DEX: 18
  CON: 24
  INT: 14
  WIS: 15
  CHA: 17
BAB: 11
CMB: 18
CMB_other: +22 grapple
CMD: 32
feats:
- name: Critical Focus
- name: Improved Initiative
- name: Multiattack
- name: Power Attack
- name: Sickening Critical
- name: Vital Strike
skills:
  Escape Artist: 18
  Intimidate: 17
  Knowledge (planes): 16
  Perception: 16
  Sense Motive: 16
  Stealth: 18
  Survival: 16
  Swim: 29
languages:
- Abyssal
- Draconic
- Infernal
- telepathy 100 ft.
special_qualities:
- amphibious
- augmented critical
ecology:
  environment: any (Abaddon)
  organization: solitary, pair, or knot (3-5)
  treasure_type: standard
special_abilities:
  Augmented Critical (Ex): A piscodaemon's claws threaten a critical hit on an 18-20
    and inflict ×3 damage on a successful critical hit.
  Poison (Ex): Tentacles-injury; save Fort DC 22; frequency 1/round for 6 rounds;
    effect 1d2 Con plus staggered for 1 round; cure 2 consecutive saves.
desc_long: |-
  These aquatic daemons roam the lower planes sowing misery and blight. They delight in drawn-out deaths, poisoning creatures or dismembering victims to watch them slowly bleed out. On their home plane of Abaddon, piscodaemons gravitate toward the same aquatic regions inhabited by hydrodaemons, and often the stronger among their ranks end up leading armies of hydrodaemons against their enemies. These creatures serve as sergeants in the hierarchy of Abaddon, and run their units with an excess of cruelty and violence. 

  Instead of preying on the weak, piscodaemons enjoy targeting strong, well-armored warriors, knowing the pain of their weakening poison rests poorly on shoulders accustomed to bearing heavy weights and delivering devastating blows. 

  Piscodaemons are 7 feet tall and weigh 400 pounds.

---

# Daemon, Piscodaemon
This hideous cross between a lobster, an _[[monsters/Octopus|octopus]]_, and a human threatens enemies with powerful claws and writhing tentacles.

**Source** Bestiary 2 pg. 72
**XP** 9,600

NE Medium outsider (aquatic, daemon, evil, extraplanar)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +16

##### Defense

**AC** 24, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+4 Dex, +10 natural)
**hp** 137 (11d10+77)
**Fort** +14, **Ref** +7, **Will** +9
**DR** 10/good; **Immune** acid, death effects, disease, poison; **Resist** cold 10, electricity 10, fire 10; **SR** 21

##### Offense
**Speed** 30 ft., swim 50 ft.
**Melee** 2 claws +18 (2d6+7/18-20/×3 plus _[[universal monster rules/Grab|grab]]_ and 1d6 _[[universal monster rules/Bleed|bleed]]_), tentacles +16 (1d10+3 plus poison)
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (2d6+10)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +14)
Constant—_detect good_, _detect magic_, _see invisibility_
At will—_[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport (self plus 50 lbs. of objects only)
3/day—fly, _[[spells/Stinking Cloud|stinking cloud]]_ (DC 16)
1/day—_[[universal monster rules/Summon|summon]]_ (level 4, 1d3 hydrodaemons 35%)

##### Statistics
**Str** 25, **Dex** 18, **Con** 24, **Int** 14, **Wis** 15, **Cha** 17
**Base Atk** +11; **CMB** +18 (+22 grapple); **CMD** 32
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Sickening Critical|Sickening Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Escape Artist +18, Intimidate +17, Knowledge (planes) +16, Perception +16, Sense Motive +16, Stealth +18, Survival +16, Swim +29
**Languages** Abyssal, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Amphibious|amphibious]]_, augmented critical

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary, pair, or knot (3–5)
**Treasure** standard

### Special Abilities

**Augmented Critical (Ex)** A piscodaemon’s claws threaten a critical hit on an 18–20 and inflict ×3 damage on a successful critical hit.

**Poison (Ex)** Tentacles—injury; save Fort DC 22; frequency 1/round for 6 rounds; effect 1d2 Con plus _[[conditions/Staggered|staggered]]_ for 1 round; cure 2 consecutive saves.

##### Description

These aquatic daemons roam the lower planes sowing misery and _[[spells/Blight|blight]]_. They delight in drawn-out deaths, _[[items/Armor Magic Abilities/Poisoning|poisoning]]_ creatures or dismembering victims to watch them slowly _bleed_ out. On their home plane of Abaddon, piscodaemons gravitate toward the same aquatic regions inhabited by hydrodaemons, and often the stronger among their ranks end up leading armies of hydrodaemons against their enemies. These creatures serve as sergeants in the hierarchy of Abaddon, and run their units with an excess of _[[feats/Cruelty|cruelty]]_ and violence.

Instead of preying on the weak, piscodaemons enjoy targeting strong, well-armored warriors, knowing the pain of their weakening poison rests poorly on shoulders accustomed to bearing heavy weights and delivering devastating blows.

Piscodaemons are 7 feet tall and weigh 400 pounds.
---
cssclass: [monsters]
title1: Agathion, Cervinal
desc_short: Beneath a crown of antlers, this centaurlike creature blends the upper
  body of a humanoid with the lower body of a majestic elk.
title2: Cervinal
CR: 17
sources:
- name: Bestiary 5
  page: 12
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
- name: Chronicle of the Righteous
  page: 58
  link: http://paizo.com/products/btpy8xe9?Pathfinder-Campaign-Setting-Chronicle-of-the-Righteous
XP: 102400
alignment: NG
size: Large
type: outsider
subtypes:
- agathion
- extraplanar
- good
initiative:
  bonus: 5
senses:
  darkvision: 60
  detect scrying: true
  low-light vision: true
  see invisibility: true
AC:
  AC: 32
  touch: 15
  flat_footed: 26
  components:
    dex: 5
    dodge: 1
    natural: 17
    size: -1
HP:
  HP: 283
  long: 21d10+168
saves:
  fort: 20
  ref: 14
  will: 19
  other: +4 vs. poison
DR:
- amount: 10
  weakness: evil and silver
immunities:
- electricity
- petrification
resistances:
  cold: 10
  sonic: 10
SR: 28
speeds:
  base: 50
  other_semicolon: gallop
attacks:
  melee:
  - - text: 2 slams +30 (1d6+10)
      entries:
      - - damage: 1d6+10
      count: 2
      attack: slams
      bonus:
      - 30
    - text: 2 hooves +25 (2d6+5)
      entries:
      - - damage: 2d6+5
      count: 2
      attack: hooves
      bonus:
      - 25
  ranged:
  - - text: +3 composite longbow +29/+24/+19/+14 (1d8+13/×3)
      entries:
      - - damage: 1d8+13
          crit_multiplier: 3
      attack: +3 composite longbow
      bonus:
      - 29
      - 24
      - 19
      - 14
  special:
  - powerful charge (gore, 2d8+15 plus stagger)
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: detect scrying
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: speak with animals
    source: default
    freq: Constant
  - name: discern lies
    source: default
    freq: At will
  - name: freedom of movement
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: invisibility purge
    source: default
    freq: At will
  - name: light
    source: default
    freq: At will
  - name: message
    source: default
    freq: At will
  - name: clairaudience/clairvoyance
    source: default
    freq: 5/day
  - name: cure critical wounds
    source: default
    freq: 5/day
  - name: dismissal
    source: default
    freq: 5/day
    DC: 18
  - name: dispel magic
    source: default
    freq: 5/day
  - name: breath of life
    source: default
    freq: 3/day
  - name: mass bull's strength
    source: default
    freq: 3/day
  - name: plane shift
    source: default
    freq: 3/day
    DC: 19
  - name: discern location
    source: default
    freq: 1/day
  - name: greater scrying
    source: default
    freq: 1/day
    DC: 21
  sources:
  - name: default
    CL: 20
    concentration: 24
ability_scores:
  STR: 31
  DEX: 20
  CON: 26
  INT: 19
  WIS: 24
  CHA: 19
BAB: 21
CMB: 32
CMD: 48
CMD_other: 52 vs. trip
feats:
- name: Combat Casting
- name: Combat Reflexes
- name: Deadly Aim
- name: Dodge
- name: Lightning Reflexes
- name: Manyshot
- name: Mobility
- name: Point-Blank Shot
- name: Precise Shot
- name: Rapid Shot
- name: Weapon Focus (composite longbow)
skills:
  Acrobatics: 29
  Climb: 31
  Diplomacy: 28
  Intimidate: 25
  Knowledge (arcana): 28
  Knowledge (nature): 28
  Knowledge (planes): 28
  Perception: 31
  Stealth: 25
  Survival: 28
languages:
- Celestial
- Draconic
- Infernal
- speak with animals
- truespeech
special_qualities:
- lay on hands (10d6, 14/day, as a 20th-level paladin)
- undersized weapons
ecology:
  environment: any land (Nirvana)
  organization: solitary, collective (2-3), or herd (4-6)
  treasure_type: double
  treasure:
  - +3 composite longbow [+10 Str]
  - other treasure
special_abilities:
  Gallop (Ex): When a cervinal uses a full-round action to run, it can move up to
    six times its speed.
  Stagger (Ex): Any creature that takes damage from a cervinal's powerful charge attack
    must succeed at a DC 28 Fortitude save or be staggered for 1 round. The save DC
    is Constitution-based.
desc_long: Cervinals stand proud and regal at the head of Nirvana's agathion forces.
  Sometimes termed the "knights" of the agathions, cervinals have gained a reputation
  for their battle prowess, noble natures, and admirable wisdom, as well as their
  fearlessness and willingness to lead from the front. They stand almost 11 feet tall,
  though part of that height is their magnificent racks of antlers, which can measure
  up to 4 feet across. These antlers gleam as if forged from beaten bronze, and a
  fine fuzz of downy gold covers their entire bodies, particularly along the shoulders
  and neck. Cervinals from the more frigid regions of Nirvana sport an entire coat
  of chestnut fur up their chests and shoulders.

---

# Agathion, Cervinal
Beneath a crown of antlers, this centaurlike creature blends the upper body of a humanoid with the lower body of a majestic elk.
**Source** Bestiary 5 pg. 12, _[[items/Wondrous Item/Chronicle of the Righteous|Chronicle of the Righteous]]_ pg. 58
**XP** 102,400

NG Large outsider (agathion, extraplanar, good)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Scrying|detect scrying]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +31

##### Defense

**AC** 32, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+5 Dex, +1 dodge, +17 natural, -1 size)
**hp** 283 (21d10+168)
**Fort** +20, **Ref** +14, **Will** +19; +4 vs. poison
**DR** 10/evil and silver; **Immune** electricity, petrification; **Resist** cold 10, sonic 10; **SR** 28

##### Offense
**Speed** 50 ft.; gallop
**Melee** 2 slams +30 (1d6+10), 2 hooves +25 (2d6+5)
**Ranged** +3 _[[items/Weapon/Composite longbow|composite longbow]]_ +29/+24/+19/+14 (1d8+13/×3)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** _[[universal monster rules/Powerful Charge|powerful charge]]_ (gore, 2d8+15 plus stagger)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +24)
Constant—_detect scrying_, _see invisibility_, _[[spells/Speak with Animals|speak with animals]]_
At will—_[[spells/Discern Lies|discern lies]]_, _[[spells/Freedom of Movement|freedom of movement]]_, greater teleport (self plus 50 lbs. of objects only), _[[spells/Invisibility Purge|invisibility purge]]_, light, _[[spells/Message|message]]_
5/day—clairaudience/clairvoyance, _[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Dismissal|dismissal]]_ (DC 18), _[[spells/Dispel Magic|dispel magic]]_
3/day—_[[spells/Breath Of Life|breath of life]]_, mass bull’s strength, _[[spells/Plane Shift|plane shift]]_ (DC 19)
1/day—_[[spells/Discern Location|discern location]]_, greater _[[spells/Scrying|scrying]]_ (DC 21)

##### Statistics
**Str** 31, **Dex** 20, **Con** 26, **Int** 19, **Wis** 24, **Cha** 19
**Base Atk** +21; **CMB** +32; **CMD** 48 (52 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _Dodge_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Manyshot|Manyshot]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_composite longbow_)
**Skills** Acrobatics +29, _[[universal monster rules/Climb|Climb]]_ +31, Diplomacy +28, Intimidate +25, Knowledge (arcana, nature, planes) +28, Perception +31, Stealth +25, Survival +28
**Languages** Celestial, Draconic, Infernal; _speak with animals_; truespeech
**SQ** lay on hands (10d6, 14/day, as a 20th-level _[[classes/Paladin|paladin]]_), _[[universal monster rules/Undersized Weapons|undersized weapons]]_

##### Ecology

**Environment** any land (Nirvana)
**Organization** solitary, collective (2-3), or herd (4-6)
**Treasure** double (+3 _composite longbow_ [+10 Str], other treasure)

### Special Abilities

**Gallop (Ex) **When a cervinal uses a full-round action to run, it can move up to six times its speed.
**Stagger (Ex)** Any creature that takes damage from a cervinal’s _powerful charge_ attack must succeed at a DC 28 Fortitude save or be _[[conditions/Staggered|staggered]]_ for 1 round. The save DC is Constitution-based.

##### Description

Cervinals stand proud and regal at the head of Nirvana’s agathion forces. Sometimes termed the "knights" of the agathions, cervinals have gained a reputation for their battle prowess, noble natures, and admirable wisdom, as well as their fearlessness and willingness to lead from the front. They stand almost 11 feet tall, though part of that height is their magnificent racks of antlers, which can measure up to 4 feet across. These antlers gleam as if forged from beaten bronze, and a fine fuzz of downy gold covers their entire bodies, particularly along the shoulders and neck. Cervinals from the more frigid regions of Nirvana sport an entire coat of chestnut fur up their chests and shoulders.
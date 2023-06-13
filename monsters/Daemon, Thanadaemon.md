---
cssclass: [monsters]
title1: Daemon, Thanadaemon
desc_short: 'Rattling with each stride, this looming, horned, skeletal figure clutches
  a wicked staff. A seething glow burns in its eye sockets. '
title2: Thanadaemon
CR: 13
sources:
- name: Bestiary 2
  page: 74
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 25600
alignment: NE
size: Medium
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 7
senses:
  darkvision: 60
  true seeing: true
AC:
  AC: 27
  touch: 14
  flat_footed: 23
  components:
    dex: 3
    dodge: 1
    natural: 13
HP:
  HP: 172
  long: 15d10+90
saves:
  fort: 11
  ref: 12
  will: 14
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
SR: 24
speeds:
  base: 30
attacks:
  melee:
  - - text: +2 quarterstaff +22/+17/+12 (1d6+9 plus energy drain)
      entries:
      - - damage: 1d6+9
        - effect: energy drain
      attack: +2 quarterstaff
      bonus:
      - 22
      - 17
      - 12
  - - text: 2 claws +20 (1d4+5 plus energy drain)
      entries:
      - - damage: 1d4+5
        - effect: energy drain
      count: 2
      attack: claws
      bonus:
      - 20
  special:
  - draining weapon
  - energy drain (1 level, DC 21)
  - fear gaze
  - soul crush
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: greater teleport
    source: default
    freq: At will
    other: self plus skiff and passengers only
  - name: plane shift
    source: default
    freq: At will
    paren_text: self plus skiff and passengers only, Astral, Ethereal, and evil-aligned
      planes only
  - name: animate dead
    source: default
    freq: 3/day
  - name: desecrate
    source: default
    freq: 3/day
  - name: enervation
    source: default
    freq: 3/day
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: hydrodaemons
      amount: 1d4
      chance: 80%
    - name: thanadaemon
      amount: 1
      chance: 35%
  sources:
  - name: default
    CL: 15
    concentration: 19
ability_scores:
  STR: 21
  DEX: 16
  CON: 23
  INT: 17
  WIS: 17
  CHA: 18
BAB: 15
CMB: 20
CMD: 34
feats:
- name: Alertness
- name: Blind-Fight
- name: Dodge
- name: Improved Initiative
- name: Iron Will
- name: Lunge
- name: Mobility
- name: Power Attack
skills:
  Acrobatics: 21
  Bluff: 22
  Diplomacy: 22
  Intimidate: 22
  Knowledge (planes): 21
  Knowledge (religion): 21
  Perception: 25
  Sense Motive: 25
  Stealth: 14
  Survival: 10
languages:
- Abyssal
- Draconic
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Abaddon)
  organization: solitary, pair, or council (3-11)
  treasure_type: standard
  treasure:
  - +2 quarterstaff
  - other treasure
special_abilities:
  Draining Weapon (Su): A thanadaemon's energy drain attack functions through any
    melee weapon it wields.
  Fear Gaze (Su): Cower in fear for 1d6 rounds, 30 feet, Will DC 21 negates. This
    is a mind-affecting fear effect. The save DC is Charisma-based.
  Soul Crush (Su): A thanadaemon can crush a soul gem (see cacodaemon) as a standard
    action to gain fast healing 15 for 15 rounds (this is a standard action). This
    action condemns the crushed soul to Abaddon-resurrecting this victim requires
    a DC 28 caster level check.
desc_long: While all daemons represent death in some fashion, thanadaemons, the Deacons
  of Death, represent the inevitable death through old age. Thanadaemons effortlessly
  work eerie skiffs along every pus- and bile-choked river in Abaddon, including the
  legendary River Styx. For the right price (typically 50 pp or 2 gems worth at least
  300 gp each), a thanadaemon will even carry passengers on its skiff, yet those who
  travel with these fiends should beware-they frequently renegotiate the terms once
  they've got their passengers in dangerous realms.

---

# Daemon, Thanadaemon
Rattling with each stride, this looming, horned, skeletal figure clutches a wicked staff. A seething glow burns in its eye sockets.

**Source** Bestiary 2 pg. 74
**XP** 25,600

NE Medium outsider (daemon, evil, extraplanar)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +25

##### Defense

**AC** 27, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+3 Dex, +1 _[[feats/Dodge|dodge]]_, +13 natural)
**hp** 172 (15d10+90)
**Fort** +11, **Ref** +12, **Will** +14
**DR** 10/good; **Immune** acid, death effects, disease, poison; **Resist** cold 10, electricity 10, fire 10; **SR** 24

##### Offense
**Speed** 30 ft.
**Melee** +2 _[[items/Weapon/Quarterstaff|quarterstaff]]_ +22/+17/+12 (1d6+9 plus _[[universal monster rules/Energy Drain|energy drain]]_) or
 2 claws +20 (1d4+5 plus _energy drain_)
**Special Attacks** draining weapon, _energy drain_ (1 level, DC 21), _[[universal monster rules/Fear|fear]]_ _[[universal monster rules/Gaze|gaze]]_, soul crush
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +19)
Constant—_[[spells/Air Walk|air walk]]_, _true seeing_
At will—greater teleport (self plus skiff and passengers only), _[[spells/Plane Shift|plane shift]]_ (self plus skiff and passengers only, Astral, Ethereal, and evil-aligned planes only)
3/day—_[[spells/Animate Dead|animate dead]]_, _[[spells/Desecrate|desecrate]]_, _[[spells/Enervation|enervation]]_
1/day—_[[universal monster rules/Summon|summon]]_ (level 4, 1d4 hydrodaemons 80% or 1 thanadaemon 35%)

##### Statistics
**Str** 21, **Dex** 16, **Con** 23, **Int** 17, **Wis** 17, **Cha** 18
**Base Atk** +15; **CMB** +20; **CMD** 34
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Blind-Fight|Blind-Fight]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Acrobatics +21, Bluff +22, Diplomacy +22, Intimidate +22, Knowledge (planes) +21, Knowledge (religion) +21, Perception +25, Sense Motive +25, Stealth +14, Survival +10
**Languages** Abyssal, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary, pair, or council (3–11)
**Treasure** standard (+2 _quarterstaff_, other treasure)

### Special Abilities

**Draining Weapon (Su)** A thanadaemon’s _energy drain_ attack functions through any melee weapon it wields.

**_Fear_ _Gaze_ (Su)** Cower in _fear_ for 1d6 rounds, 30 feet, Will DC 21 negates. This is a mind-affecting _fear_ effect. The save DC is Charisma-based.
**Soul Crush (Su)** A thanadaemon can crush a soul gem (see cacodaemon) as a standard action to gain _[[universal monster rules/Fast Healing|fast healing]]_ 15 for 15 rounds (this is a standard action). This action condemns the crushed soul to Abaddon—resurrecting this victim requires a DC 28 caster level check.

##### Description

While all daemons represent death in some fashion, thanadaemons, the Deacons of Death, represent the inevitable death through old age. Thanadaemons effortlessly work eerie skiffs along every pus- and bile-choked river in Abaddon, including the legendary River Styx. For the right price (typically 50 pp or 2 gems worth at least 300 gp each), a thanadaemon will even carry passengers on its skiff, yet those who travel with these fiends should beware—they frequently renegotiate the terms once they’ve got their passengers in dangerous realms.
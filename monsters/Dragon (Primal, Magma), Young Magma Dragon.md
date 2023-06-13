---
cssclass: [monsters]
title1: Dragon (Primal, Magma), Young Magma Dragon
desc_short: 'Between this dragon's jet-black scales run glowing rivulets of lava,
  and veins aglow with heat shine in the membranes of its wings. '
title2: Young Magma Dragon
CR: 8
sources:
- name: Bestiary 2
  page: 100
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 4800
alignment: CN
size: Medium
type: dragon
subtypes:
- extraplanar
- fire
initiative:
  bonus: 6
senses:
  dragon senses: true
AC:
  AC: 22
  touch: 12
  flat_footed: 20
  components:
    dex: 2
    natural: 10
HP:
  HP: 85
  long: 9d12+27
saves:
  fort: 11
  ref: 8
  will: 10
immunities:
- fire
- paralysis
- sleep
weaknesses:
- vulnerable to cold
speeds:
  base: 40
  fly: 150
  fly_maneuverability: average
attacks:
  melee:
  - - text: bite +17 (1d8+12 plus 3 fire)
      entries:
      - - damage: 1d8+12
        - damage: '3'
          type: fire
      attack: bite
      bonus:
      - 17
    - text: 2 claws +17 (1d6+8)
      entries:
      - - damage: 1d6+8
      count: 2
      attack: claws
      bonus:
      - 17
    - text: 2 wings +12 (1d4+4)
      entries:
      - - damage: 1d4+4
      count: 2
      attack: wings
      bonus:
      - 12
  special:
  - breath weapon (30-ft. cone, 6d6 fire, DC 17)
spell_like_abilities:
  entries:
  - name: burning hands
    source: default
    freq: At will
    DC: 12
  sources:
  - name: default
    CL: 9
    concentration: 10
spells:
  entries:
  - name: flare burst
    source: '?'
    level: 1
    DC: 12
  - name: grease
    source: '?'
    level: 1
    DC: 12
  - name: bleed
    source: '?'
    level: 0
    DC: 11
  - name: detect magic
    source: '?'
    level: 0
  - name: open/close
    source: '?'
    level: 0
  - name: spark
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 1
    concentration: 2
    slots:
      1: 4
      0: at-will
ability_scores:
  STR: 21
  DEX: 14
  CON: 17
  INT: 14
  WIS: 14
  CHA: 13
BAB: 9
CMB: 14
CMD: 26
CMD_other: 30 vs. trip
feats:
- name: Great Fortitude
- name: Improved Initiative
- name: Iron Will
- name: Power Attack
- name: Vital Strike
skills:
  Acrobatics: 11
    jump: 15
  Climb: 17
  Fly: 14
  Intimidate: 13
  Perception: 14
  Sense Motive: 14
  Stealth: 14
  Swim: 17
languages:
- Common
- Draconic
- Ignan
special_qualities:
- superheated
ecology:
  environment: any mountains or underground (Plane of Fire)
  organization: solitary
  treasure_type: triple
desc_long: Temperamental and prone to violent outbursts, magma dragons are regarded
  by most other dragons as dangerously insane-an assumption that, more often than
  not, proves correct. One can rarely predict a magma dragon's state of mind until
  it either attacks or attempts to engage in conversation. For their part, magma dragons
  can justify all of their actions-they just rarely feel the need to do so.

---

# Dragon (Primal, Magma), Young Magma Dragon
Between this dragon’s jet-black scales run glowing rivulets of lava, and veins aglow with _[[universal monster rules/Heat|heat]]_ shine in the membranes of its wings.

**Source** Bestiary 2 pg. 100
**XP** 4,800

CN Medium dragon (extraplanar, fire)
**Init** +6; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +14

##### Defense

**AC** 22, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+2 Dex, +10 natural)
**hp** 85 (9d12+27)
**Fort** +11, **Ref** +8, **Will** +10
**Immune** fire, _[[universal monster rules/Paralysis|paralysis]]_, sleep
**Weaknesses** vulnerable to cold

##### Offense
**Speed** 40 ft., fly 150 ft. (average)
**Melee** bite +17 (1d8+12 plus 3 fire), 2 claws +17 (1d6+8), 2 wings +12 (1d4+4)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (30-ft. cone, 6d6 fire, DC 17)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +10)
At will—_[[spells/Burning Hands|burning hands]]_ (DC 12)
**Spells Known **(CL 1st; concentration +2)
1st (4/day)—_[[spells/Flare Burst|flare burst]]_ (DC 12), _[[spells/Grease|grease]]_ (DC 12)
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 11), _[[spells/Detect Magic|detect magic]]_, open/close, _[[spells/Spark|spark]]_

##### Statistics
**Str** 21, **Dex** 14, **Con** 17, **Int** 14, **Wis** 14, **Cha** 13
**Base Atk** +9; **CMB** +14; **CMD** 26 (30 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +11 (+15 _[[spells/Jump|jump]]_), _[[universal monster rules/Climb|Climb]]_ +17, Fly +14, Intimidate +13, Perception +14, Sense Motive +14, Stealth +14, Swim +17
**Languages** Common, Draconic, Ignan
**SQ** superheated

##### Ecology

**Environment** any mountains or underground (Plane of Fire)
**Organization** solitary
**Treasure** triple

##### Description

Temperamental and _[[conditions/Prone|prone]]_ to violent outbursts, magma dragons are regarded by most other dragons as dangerously insane—an assumption that, more often than not, proves correct. One can rarely predict a magma dragon’s state of mind until it either attacks or attempts to engage in conversation. For their part, magma dragons can justify all of their actions—they just rarely feel the need to do so.
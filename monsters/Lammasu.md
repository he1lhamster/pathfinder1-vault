---
cssclass: [monsters]
title1: Lammasu
desc_short: This majestic creature has the body of a lion, the wings of an eagle,
  and the face of a wise human man.
title2: Lammasu
CR: 8
sources:
- name: Bestiary 3
  page: 175
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
- name: Bonus Bestiary
  page: 13
  link: http://paizo.com/pathfinderRPG/v5748btpy88x4
XP: 4800
alignment: LG
size: Large
type: magical beast
initiative:
  bonus: 5
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: magic circle against evil
  radius: 20
AC:
  AC: 21
  touch: 10
  flat_footed: 20
  components:
    dex: 1
    natural: 11
    size: -1
HP:
  HP: 94
  long: 9d10+45
saves:
  fort: 11
  ref: 9
  will: 8
speeds:
  base: 30
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: 2 claws +14 (1d8+6)
      entries:
      - - damage: 1d8+6
      count: 2
      attack: claws
      bonus:
      - 14
    - text: 2 wings +9 (1d6+3)
      entries:
      - - damage: 1d6+3
      count: 2
      attack: wings
      bonus:
      - 9
  special:
  - pounce
  - rake (2 claws +14; 1d8+6)
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: greater invisibility
    source: default
    freq: 3/day
  - name: dimension door
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 9
    concentration: 11
spells:
  entries:
  - name: cure serious wounds
    source: '?'
    level: 3
  - name: searing light
    source: '?'
    level: 3
  - name: cure moderate wounds
    source: '?'
    level: 2
  - name: lesser restoration
    source: '?'
    level: 2
  - name: resist energy
    source: '?'
    level: 2
  - name: bless
    source: '?'
    level: 1
  - name: command
    source: '?'
    level: 1
    DC: 13
  - name: cure light wounds
    source: '?'
    level: 1
  - name: detect evil
    source: '?'
    level: 1
  - name: divine favor
    source: '?'
    level: 1
  - name: detect magic
    source: '?'
    level: 0
  - name: detect poison
    source: '?'
    level: 0
  - name: guidance
    source: '?'
    level: 0
  - name: mending
    source: '?'
    level: 0
  - name: purify food and drink
    source: '?'
    level: 0
  - name: resistance
    source: '?'
    level: 0
  - name: stabilize
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 7
    concentration: 9
    slots:
      3: 4
      2: 7
      1: 7
      0: at-will
ability_scores:
  STR: 23
  DEX: 12
  CON: 21
  INT: 16
  WIS: 17
  CHA: 14
BAB: 9
CMB: 16
CMD: 27
CMD_other: 31 vs. trip
feats:
- name: Blind-Fight
- is_bonus: true
  name: Eschew Materials
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
skills:
  Diplomacy: 11
  Fly: 11
  Knowledge (arcana): 12
  Perception: 15
  Sense Motive: 12
languages:
- Celestial
- Common
ecology:
  environment: temperate deserts
  organization: solitary
  treasure_type: standard
special_abilities:
  Spells: A lammasu casts spells as a 7th-level oracle, but does not gain any other
    class abilities possessed by an oracle. It ignores all divine focus material components
    for spells it casts.
desc_long: |-
  Lammasus are protectors of the weak and ever-vigilant champions against evil. These noble creatures dwell in crumbling desert ruins or other remote areas, where they tirelessly fight against the forces of darkness, hoping to defend those they consider lesser races from the evils that often lurk in such places.

  Although most of these winged sentinels prove wise and knowledgeable about those who would seek to do evil in their lands, many races find lammasus arrogant, dismissive, and patronizing, taking umbrage at their superior attitudes and affectations. Such reactions confuse and sometimes insult these highly honorable creatures, who seek only to do good and aid those weaker than themselves. Lammasus who witness members of other races actively combating evil typically prove more sensitive and address such allies as equals. Should good-aligned creatures prove their skill and overcome any differences of attitude they might have with one of these majestic beings, they find a true and noble ally and an invaluable resource for those hoping to defeat evil.

  Lammasus are quite parental toward those who join their cause, bringing a lifetime of experience to any struggle. This often makes them stern, but those who know lammasus find them to be extremely caring about those they protect. A lammasu eagerly lays down its own life to protect those in peril if such a sacrifice might win the day. Most lammasus are 8 feet in length and weigh approximately 900 pounds.

---

# Lammasu
This majestic creature has the body of a _[[monsters/Lion|lion]]_, the wings of an _[[monsters/Eagle|eagle]]_, and the face of a wise human man.
**Source** Bestiary 3 pg. 175, Bonus Bestiary pg. 13
**XP** 4,800

LG Large magical beast
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +15
**Aura** _[[spells/Magic Circle against Evil|magic circle against evil]]_ (20 ft.)

##### Defense

**AC** 21, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+1 Dex, +11 natural, –1 size)
**hp** 94 (9d10+45)
**Fort** +11, **Ref** +9, **Will** +8

##### Offense
**Speed** 30 ft., fly 60 ft. (average)
**Melee** 2 claws +14 (1d8+6), 2 wings +9 (1d6+3)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** _[[universal monster rules/Pounce|pounce]]_, _[[universal monster rules/Rake|rake]]_ (2 claws +14; 1d8+6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +11)
3/day—greater _[[spells/Invisibility|invisibility]]_
1/day—_[[spells/Dimension Door|dimension door]]_
**Spells Known **(CL 7th; concentration +9)
3rd (4/day)—_[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Searing Light|searing light]]_
2nd (7/day)—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_, lesser _[[spells/Restoration|restoration]]_, _[[spells/Resist Energy|resist energy]]_
1st (7/day)—_[[spells/Bless|bless]]_, _[[spells/Command|command]]_ (DC 13), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Detect Evil|detect evil]]_, _[[spells/Divine Favor|divine favor]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, _[[spells/Mending|mending]]_, _[[spells/Purify Food and Drink|purify food and drink]]_, _[[universal monster rules/Resistance|resistance]]_, stabilize

##### Statistics
**Str** 23, **Dex** 12, **Con** 21, **Int** 16, **Wis** 17, **Cha** 14
**Base Atk** +9; **CMB** +16; **CMD** 27 (31 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Diplomacy +11, Fly +11, Knowledge (arcana) +12, Perception +15, Sense Motive +12
**Languages** Celestial, Common

##### Ecology

**Environment** temperate deserts
**Organization** solitary
**Treasure** standard

### Special Abilities
**Spells **A _[[monsters/Lammasu|lammasu]]_ casts spells as a 7th-level _[[classes/Oracle|oracle]]_, but does not gain any other class abilities possessed by an _oracle_. It ignores all divine focus material components for spells it casts.

##### Description

Lammasus are protectors of the weak and ever-vigilant champions against evil. These noble creatures dwell in crumbling desert ruins or other remote areas, where they tirelessly fight against the forces of _[[spells/Darkness|darkness]]_, hoping to defend those they consider lesser races from the evils that often lurk in such places.

Although most of these winged sentinels prove wise and knowledgeable about those who would seek to do evil in their lands, many races find lammasus arrogant, dismissive, and patronizing, taking umbrage at their superior attitudes and affectations. Such reactions confuse and sometimes insult these highly honorable creatures, who seek only to do good and aid those weaker than themselves. Lammasus who _[[spells/Witness|witness]]_ members of other races actively combating evil typically prove more sensitive and address such allies as equals. Should good-aligned creatures prove their skill and overcome any differences of attitude they might have with one of these majestic beings, they find a true and noble ally and an invaluable resource for those hoping to defeat evil.

Lammasus are quite parental toward those who join their cause, bringing a lifetime of experience to any struggle. This often makes them stern, but those who know lammasus find them to be extremely caring about those they protect. A _lammasu_ eagerly lays down its own life to protect those in peril if such a _[[spells/Sacrifice|sacrifice]]_ might win the day. Most lammasus are 8 feet in length and weigh approximately 900 pounds.
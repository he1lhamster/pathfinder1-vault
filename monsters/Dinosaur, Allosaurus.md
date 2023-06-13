---
cssclass: [monsters]
title1: Dinosaur, Allosaurus
desc_short: 'This bipedal dinosaur has a mouth filled with sharp teeth and short,
  powerful arms that end in sharp claws. '
title2: Allosaurus
CR: 7
sources:
- name: Bestiary 2
  page: 90
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 3200
alignment: N
size: Huge
type: animal
initiative:
  bonus: 5
senses:
  low-light vision: true
  scent: true
AC:
  AC: 19
  touch: 9
  flat_footed: 18
  components:
    dex: 1
    natural: 10
    size: -2
HP:
  HP: 93
  long: 11d8+44
saves:
  fort: 11
  ref: 8
  will: 7
speeds:
  base: 50
attacks:
  melee:
  - - text: bite +14 (2d6+8/19-20 plus grab)
      entries:
      - - damage: 2d6+8
          crit_range: 19-20
        - effect: grab
      attack: bite
      bonus:
      - 14
    - text: 2 claws +14 (1d8+8)
      entries:
      - - damage: 1d8+8
      count: 2
      attack: claws
      bonus:
      - 14
  special:
  - pounce
  - rake (2 talons +14, 1d8+8)
space: 15
reach: 15
ability_scores:
  STR: 26
  DEX: 13
  CON: 19
  INT: 2
  WIS: 15
  CHA: 10
BAB: 8
CMB: 18
CMD: 29
feats:
- name: Alertness
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Iron Will
- name: Nimble Moves
- name: Run
skills:
  Perception: 28
  _racial_mods:
    Perception:
      _: 8
ecology:
  environment: temperate or warm forests or plains
  organization: solitary, pair, or pack (3-6)
  treasure_type: none
desc_long: A huge, swift hunter, the allosaurus measures 30 feet in length and weighs
  10,000 pounds.

---

# Dinosaur, Allosaurus
This bipedal dinosaur has a mouth filled with sharp teeth and short, powerful arms that end in sharp claws.

**Source** Bestiary 2 pg. 90
**XP** 3,200

N Huge animal
**Init** +5; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +28

##### Defense

**AC** 19, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+1 Dex, +10 natural, –2 size)
**hp** 93 (11d8+44)
**Fort** +11, **Ref** +8, **Will** +7

##### Offense
**Speed** 50 ft.
**Melee** bite +14 (2d6+8/19–20 plus _[[universal monster rules/Grab|grab]]_), 2 claws +14 (1d8+8)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _[[universal monster rules/Pounce|pounce]]_, _[[universal monster rules/Rake|rake]]_ (2 talons +14, 1d8+8)

##### Statistics
**Str** 26, **Dex** 13, **Con** 19, **Int** 2, **Wis** 15, **Cha** 10
**Base Atk** +8; **CMB** +18; **CMD** 29
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Nimble Moves|Nimble Moves]]_, Run
**Skills** Perception +28; **Racial Modifiers** +8 Perception

##### Ecology

**Environment** temperate or warm forests or plains
**Organization** solitary, pair, or pack (3–6)
**Treasure** None

##### Description

A huge, swift _[[classes/Hunter|hunter]]_, the allosaurus measures 30 feet in length and weighs 10,000 pounds.
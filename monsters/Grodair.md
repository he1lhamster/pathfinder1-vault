---
cssclass: [monsters]
title1: Grodair
desc_short: Several water-dripping tentacles sprout from this four-eyed fish's belly,
  while long fins protrude from its back.
title2: Grodair
CR: 5
sources:
- name: Bestiary 3
  page: 143
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
- name: 'Pathfinder #36: Sound of a Thousand Screams'
  page: 84
  link: http://paizo.com/pathfinder/adventurePath/kingmaker/v5748btpy8b7x
XP: 1600
alignment: CN
size: Medium
type: magical beast
subtypes:
- aquatic
- extraplanar
initiative:
  bonus: -1
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 16
  touch: 9
  flat_footed: 16
  components:
    dex: -1
    natural: 7
HP:
  HP: 66
  long: 7d10+28
saves:
  fort: 11
  ref: 4
  will: 5
speeds:
  base: 30
  swim: 60
attacks:
  melee:
  - - text: bite +11 (1d8+4)
      entries:
      - - damage: 1d8+4
      attack: bite
      bonus:
      - 11
    - text: 2 tentacles +6 (1d4+2 plus trip)
      entries:
      - - damage: 1d4+2
        - effect: trip
      count: 2
      attack: tentacles
      bonus:
      - 6
  ranged:
  - - text: water blast +7 touch (1d8 plus push)
      entries:
      - - damage: 1d8
        - effect: push
      attack: water blast
      bonus:
      - 7
      touch: true
  special:
  - death flood
  - push (water blast, 5 ft.)
spell_like_abilities:
  entries:
  - name: control water
    source: default
    freq: At will
  sources:
  - name: default
    CL: 7
    concentration: 9
ability_scores:
  STR: 18
  DEX: 8
  CON: 19
  INT: 12
  WIS: 13
  CHA: 15
BAB: 7
CMB: 11
CMD: 20
CMD_other: 24 vs. trip
feats:
- name: Combat Reflexes
- name: Great Fortitude
- name: Iron Will
- name: Weapon Focus (water blast)
skills:
  Knowledge (nature): 8
  Survival: 8
  Swim: 22
  Perception: 1
languages:
- Aquan
- Sylvan
special_qualities:
- amphibious
- muddy field
ecology:
  environment: any water or coastlines
  organization: solitary
  treasure_type: standard
special_abilities:
  Death Flood (Su): When a grodair is killed, it immediately explodes in a 15-foot-radius
    burst of highly pressurized water that deals 5d6 points of bludgeoning damage
    (DC 17 Reflex for half). After the explosion, a successful DC 25 Survival check
    allows a creature to recover a cluster of strange organs from the remains. This
    cluster functions as a decanter of endless water for 2d6 hours, but can only produce
    a “stream” or “fountain” effect. Failing this Survival check by 5 or more causes
    the cluster to burst, dealing an additional 2d6 points of damage to that creature
    (no save) and destroying the organs entirely. The save DC is Constitution-based.
  Muddy Field (Su): As a standard action when on sand, soil, or other types of loose
    earth, a grodair can gush standing water into the area surrounding it. Upon doing
    so, the land within 15 feet of the grodair is treated as a shallow bog. This water
    remains as long as the grodair is within 15 feet and wishes to maintain the water.
    The bog instantly disperses as soon as the grodair is killed or moves out of the
    area.
  Water Blast (Ex): The grodair's ranged attack is a pressurized blast of water. This
    attack has a range of 60 feet with no range increment.
desc_long: |-
  A grodair is a bloated aquatic creature from the primal world of the fey. The bulbous sac on its spine is an extradimensional space that can contain thousands of gallons of water. The creature drains water (including small bits of debris and even very small creatures) from one place and releases it in another, typically creating boggy areas as it moves so it can travel more quickly than its tentacles can carry it. A grodair can rise up to 6 feet on its tentacles, measures 7 feet long, and weighs about 400 pounds.

  A grodair is intelligent, but extremely absentminded and careless. Its memory is poor, and it has difficulty remembering things it was told even 5 minutes prior-though it can recall some events of the distant past with perfect (and often frustrating) clarity.

---

# Grodair
Several water-dripping tentacles sprout from this four-eyed fish’s belly, while long fins protrude from its back.
**Source** Bestiary 3 pg. 143, Pathfinder #36: Sound of a Thousand Screams pg. 84
**XP** 1,600

CN Medium magical beast (aquatic, extraplanar)
**Init** –1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +1

##### Defense

**AC** 16, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 16 (–1 Dex, +7 natural)
**hp** 66 (7d10+28)
**Fort** +11, **Ref** +4, **Will** +5

##### Offense
**Speed** 30 ft., swim 60 ft.
**Melee** bite +11 (1d8+4), 2 tentacles +6 (1d4+2 plus _[[universal monster rules/Trip|trip]]_)
**Ranged** water blast +7 touch (1d8 plus push)
**Special Attacks** death flood, push (water blast, 5 ft.)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +9)
At will—_[[spells/Control Water|control water]]_

##### Statistics
**Str** 18, **Dex** 8, **Con** 19, **Int** 12, **Wis** 13, **Cha** 15
**Base Atk** +7; **CMB** +11; **CMD** 20 (24 vs. _trip_)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (water blast)
**Skills** Knowledge (nature) +8, Survival +8, Swim +22
**Languages** Aquan, Sylvan
**SQ** _[[universal monster rules/Amphibious|amphibious]]_, muddy field

##### Ecology

**Environment** any water or coastlines
**Organization** solitary
**Treasure** standard

### Special Abilities

**Death Flood (Su)** When a _[[monsters/Grodair|grodair]]_ is killed, it immediately explodes in a 15-foot-radius burst of highly pressurized water that deals 5d6 points of bludgeoning damage (DC 17 Reflex for half). After the explosion, a successful DC 25 Survival check allows a creature to recover a cluster of strange organs from the remains. This cluster functions as a _[[items/Wondrous Item/Decanter of Endless Water|decanter of endless water]]_ for 2d6 hours, but can only produce a “stream” or “fountain” effect. Failing this Survival check by 5 or more causes the cluster to burst, dealing an additional 2d6 points of damage to that creature (no save) and destroying the organs entirely. The save DC is Constitution-based.

**Muddy Field (Su)** As a standard action when on sand, soil, or other types of loose earth, a _grodair_ can gush standing water into the area surrounding it. Upon doing so, the land within 15 feet of the _grodair_ is treated as a shallow bog. This water remains as long as the _grodair_ is within 15 feet and wishes to maintain the water. The bog instantly disperses as soon as the _grodair_ is killed or moves out of the area.

**Water Blast (Ex)** The _grodair_’s ranged attack is a pressurized blast of water. This attack has a range of 60 feet with no range increment.

##### Description

A _grodair_ is a bloated aquatic creature from the primal world of the fey. The bulbous sac on its spine is an extradimensional space that can contain thousands of gallons of water. The creature drains water (including small bits of debris and even very small creatures) from one place and releases it in another, typically creating boggy areas as it moves so it can travel more quickly than its tentacles can carry it. A _grodair_ can rise up to 6 feet on its tentacles, measures 7 feet long, and weighs about 400 pounds.

A _grodair_ is intelligent, but extremely absentminded and careless. Its memory is poor, and it has difficulty remembering things it was told even 5 minutes prior—though it can recall some events of the distant past with perfect (and often frustrating) _[[items/Weapon/Clarity|clarity]]_.
---
cssclass: [monsters]
title1: Nuckelavee
desc_short: This skinless creature resembles a horse and its humanoid rider, fused
  into a single hideous being of rage and sickness.
title2: Nuckelavee
CR: 9
sources:
- name: Bestiary 3
  page: 203
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
- name: 'Pathfinder #34: Blood for Blood'
  page: 88
  link: http://paizo.com/pathfinder/adventurePath/kingmaker/v5748btpy8b7w
XP: 6400
alignment: NE
size: Large
type: fey
subtypes:
- aquatic
initiative:
  bonus: 7
senses:
  low-light vision: true
auras:
- name: frightful presence
  radius: 30
  DC: 20
AC:
  AC: 23
  touch: 17
  flat_footed: 15
  components:
    dex: 7
    dodge: 1
    natural: 6
    size: -1
HP:
  HP: 104
  long: 11d6+66
saves:
  fort: 9
  ref: 16
  will: 10
DR:
- amount: 10
  weakness: cold iron
immunities:
- disease
- poison
speeds:
  base: 50
  swim: 50
attacks:
  melee:
  - - text: mwk longsword +11 (1d8+9/19-20)
      entries:
      - - damage: 1d8+9
          crit_range: 19-20
      attack: mwk longsword
      bonus:
      - 11
    - text: bite +10 (1d8+6 plus disease)
      entries:
      - - damage: 1d8+6
        - effect: disease
      attack: bite
      bonus:
      - 10
    - text: 2 hooves +5 (1d6+3 plus disease)
      entries:
      - - damage: 1d6+3
        - effect: disease
      count: 2
      attack: hooves
      bonus:
      - 5
  special:
  - breath weapon (30-ft. cone, 10d6 damage plus disease, Reflex DC 21 for half, usable
    every 1d4 rounds)
  - trample (1d6+9, DC 21)
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: control water
    source: default
    freq: 3/day
  - name: diminish plants
    source: default
    freq: 3/day
  - name: obscuring mist
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 9
    concentration: 14
ability_scores:
  STR: 22
  DEX: 24
  CON: 22
  INT: 13
  WIS: 17
  CHA: 21
BAB: 5
CMB: 12
CMD: 30
CMD_other: 34 vs. trip
feats:
- name: Dodge
- name: Lightning Reflexes
- name: Lightning Stance
- name: Mobility
- name: Spring Attack
- name: Wind Stance
skills:
  Acrobatics: 21
    when jumping: 29
  Escape Artist: 21
  Intimidate: 16
  Knowledge (nature): 15
  Perception: 17
  Stealth: 17
  Swim: 28
languages:
- Aklo
- Common
- Sylvan
special_qualities:
- amphibious
- undersized weapons
ecology:
  environment: cold swamps or coastlines
  organization: solitary
  treasure_type: standard
  treasure:
  - masterwork longsword
  - other treasure
special_abilities:
  Breath Weapon (Su): A nuckelavee's breath weapon is a cone of withering foulness
    that causes painful welts, cramps, and bleeding, and only harms living creatures-this
    damage bypasses all energy resistance and damage reduction. Non-creature plants
    in the area are affected as if by a blight spell. Any creature that fails its
    Reflex save against the breath weapon must make a DC 21 Fortitude save or contract
    mortasheen (see below). The save DC is Constitution-based.
  Disease (Su): 'Mortasheen: Contact; save Fort DC 21; onset immediate; frequency
    1/day; effect 1d4 Con and target is fatigued; cure 2 consecutive saves. Animals
    take a -2 penalty on their saves against this disease. The save DC is Constitution-based.'
desc_long: |-
  The dreaded nuckelavee is a manifestation of pollution and filth, be it the natural decay of a red tide or the intrusive pollution of sewage and other urban waste. A nuckelavee is a living irony-a carrier of disease and a spreader of corruption that unleashes its wrath against other sources that bring corruption into the world. The corruption spread by nuckelavees only serves to further their own sense of self-loathing and overall rage. While nuckelavees might, incidentally, carry out vengeance for the victims of such pollution, defending the denizens of their rivers, swamps, and bogs is not their primary drive, for they revel in inflicting the very corruption they hate and enjoy little more than watching their enemies sicken and die.

  Folktales tell of talismans to carry-fetishes of seaweed garlands, horsehair soaked in brine, or vials of sanctified seawater-or of prayers to recite to ward away nuckelavees or convince them the bearer is innocent. In truth, however, these old solutions offer no protection from the vile plague-bearers.

  A nuckelavee is the same size as a horse.

---

# Nuckelavee
This skinless creature resembles a _[[monsters/Horse|horse]]_ and its humanoid rider, fused into a single hideous being of _[[spells/Rage|rage]]_ and sickness.
**Source** Bestiary 3 pg. 203, Pathfinder #34: Blood for Blood pg. 88
**XP** 6,400

NE Large fey (aquatic)
**Init** +7; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +17
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (30 ft., DC 20)

##### Defense

**AC** 23, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+7 Dex, +1 dodge, +6 natural, –1 size)
**hp** 104 (11d6+66)
**Fort** +9, **Ref** +16, **Will** +10
**DR** 10/cold iron; **Immune** disease, poison

##### Offense
**Speed** 50 ft., swim 50 ft.
**Melee** mwk _[[items/Weapon/Longsword|longsword]]_ +11 (1d8+9/19–20), bite +10 (1d8+6 plus disease), 2 hooves +5 (1d6+3 plus disease)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (30-ft. cone, 10d6 damage plus disease, Reflex DC 21 for half, usable every 1d4 rounds), _[[universal monster rules/Trample|trample]]_ (1d6+9, DC 21)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +14)
3/day—_[[spells/Control Water|control water]]_, _[[spells/Diminish Plants|diminish plants]]_, _[[spells/Obscuring Mist|obscuring mist]]_

##### Statistics
**Str** 22, **Dex** 24, **Con** 22, **Int** 13, **Wis** 17, **Cha** 21
**Base Atk** +5; **CMB** +12; **CMD** 30 (34 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _Dodge_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Lightning Stance|Lightning Stance]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Wind Stance|Wind Stance]]_
**Skills** Acrobatics +21 (+29 when jumping), Escape Artist +21, Intimidate +16, Knowledge (nature) +15, Perception +17, Stealth +17, Swim +28
**Languages** Aklo, Common, Sylvan
**SQ** _[[universal monster rules/Amphibious|amphibious]]_, _[[universal monster rules/Undersized Weapons|undersized weapons]]_

##### Ecology

**Environment** cold swamps or coastlines
**Organization** solitary
**Treasure** standard (masterwork _longsword_, other treasure)

### Special Abilities

**_Breath Weapon_ (Su)** A _[[monsters/Nuckelavee|nuckelavee]]_’s _breath weapon_ is a cone of withering foulness that causes painful welts, cramps, and bleeding, and only harms living creatures—this damage bypasses all _[[items/Armor Magic Abilities/Energy Resistance|energy resistance]]_ and _[[universal monster rules/Damage Reduction|damage reduction]]_. Non-creature plants in the area are affected as if by a _[[spells/Blight|blight]]_ spell. Any creature that fails its Reflex save against the _breath weapon_ must make a DC 21 Fortitude save or contract mortasheen (see below). The save DC is Constitution-based.

**Disease (Su)** Mortasheen: Contact; save Fort DC 21; onset immediate; frequency 1/day; effect 1d4 Con and target is _[[conditions/Fatigued|fatigued]]_; cure 2 consecutive saves. Animals take a –2 penalty on their saves against this disease. The save DC is Constitution-based.

##### Description

The dreaded _nuckelavee_ is a manifestation of pollution and filth, be it the natural decay of a red tide or the intrusive pollution of sewage and other urban waste. A _nuckelavee_ is a living irony—a carrier of disease and a spreader of corruption that unleashes its wrath against other sources that bring corruption into the world. The corruption spread by nuckelavees only serves to further their own sense of self-loathing and overall _rage_. While nuckelavees might, incidentally, carry out _[[feats/Vengeance|vengeance]]_ for the victims of such pollution, _[[items/Weapon Magic Abilities/Defending|defending]]_ the denizens of their rivers, swamps, and bogs is not their primary drive, for they revel in inflicting the very corruption they hate and enjoy little more than watching their enemies sicken and die.

Folktales tell of talismans to carry—fetishes of seaweed garlands, horsehair soaked in brine, or vials of sanctified seawater—or of prayers to recite to ward away nuckelavees or convince them the bearer is innocent. In truth, however, these old solutions offer no protection from the vile plague-bearers.

A _nuckelavee_ is the same size as a _horse_.
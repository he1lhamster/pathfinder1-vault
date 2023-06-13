---
cssclass: [monsters]
title1: Sturzstromer
desc_short: Stones jump and roll as if moved by an earthquake that affects nothing
  else around it. A wave of disturbed earth and rock follows behind them.
title2: Sturzstromer
CR: 19
sources:
- name: 'Pathfinder #138: Rise of New Thassilon'
  page: 92
  link: https://paizo.com/products/btq01w1w
XP: 204800
alignment: CN
size: Tiny
type: outsider
subtypes:
- earth
- elemental
- extraplanar
- swarm
initiative:
  bonus: 1
senses:
  darkvision: 60
  tremorsense: 120
AC:
  AC: 34
  touch: 14
  flat_footed: 32
  components:
    dex: 1
    dodge: 1
    natural: 20
    size: 2
HP:
  HP: 324
  long: 24d10+192
saves:
  fort: 22
  ref: 17
  will: 16
DR:
- amount: 10
  weakness: '-'
immunities:
- electricity
- elemental traits
- swarm traits
resistances:
  cold: 30
  fire: 30
SR: 30
speeds:
  base: 50
attacks:
  melee:
  - - text: swarm (6d6+6 plus distraction)
      entries:
      - - damage: 6d6+6
        - effect: distraction
      attack: swarm
  ranged:
  - - text: rock +29/+24/+19/+14 (6d6+6)
      entries:
      - - damage: 6d6+6
      attack: rock
      bonus:
      - 29
      - 24
      - 19
      - 14
  special:
  - distraction (DC 30)
  - landslide
  - powerful swarm
  - rock throwing (120 ft.)
  - rumble
  - trample (6d6+6, DC 26)
space: 10
reach: 0
spell_like_abilities:
  entries:
  - name: stone tell
    source: default
    freq: Constant
  sources:
  - name: default
    CL: 19
    concentration: 21
ability_scores:
  STR: 18
  DEX: 13
  CON: 27
  INT: 10
  WIS: 22
  CHA: 15
BAB: 24
CMB:
CMD:
feats:
- name: Blind-Fight
- name: Dodge
- name: Greater Blind-Fight
- name: Improved Blind-Fight
- name: Improved Iron Will
- name: Improved Lightning Reflexes
- name: Iron Will
- name: Lightning Reflexes
- name: Mobility
- name: Quick Draw
- name: Run
- name: Weapon Focus (rock)
skills:
  Appraise: 27
  Climb: 31
  Knowledge (geography): 27
  Knowledge (planes): 27
  Perception: 33
  Stealth: 36
languages:
- Terran
- stone tell
special_qualities:
- mountaineer
ecology:
  environment: any mountains (Plane of Earth)
  organization: solitary
  treasure_type: incidental
special_abilities:
  Landslide (Ex): When a sturzstromer runs, it can create an avalanche 1d6×100 feet
    wide along the path which it moves as a free action. The sturzstromer must be
    in an area of natural rock, soil, or sand and moving downhill, though even gentle
    slopes are sufficient, and it can use this ability only if it took sonic damage
    within the past round or if it used its landslide or rumble abilities in the previous
    round. Each creature caught in the avalanche can attempt a DC 26 Reflex save to
    halve damage in the bury zone or negate damage in the slide zone. The sturzstromer
    is unaffected by its own avalanche. The save DC is Strength based.
  Mountaineer (Ex): A sturzstromer takes no penalty to speed or on Acrobatics or Stealth
    checks when moving across steep slopes, rubble, or scree. In addition, a sturzstromer
    can hide in rocky terrain, even if that terrain provides no cover or concealment.
  Powerful Swarm (Ex): A sturzstromer adds 1-1/2 times its Strength modifier on swarm
    damage rolls, and it is treated as a Large creature for the purposes of its rock
    throwing and trample abilities.
  Rumble (Ex): As a full-round action, a sturzstromer can create a rumble that shakes
    the ground and air in a 120-ft. radius centered on the sturzstromer (the sturzstromer
    still makes a swarm attack at the end of this round). A creature that starts its
    turn in the affected area must succeed at a DC 26 Reflex save or be unable to
    move. A creature that fails this save by 5 or more is knocked prone; a flying
    creature falls instead. Casting a spell in this area requires a successful concentration
    check (DC = 15 + the level of the spell being cast). All other concentration checks
    in the area have their DCs increased by 5. The DC of Perception checks is likewise
    increased by 5. The effects of this ability last until the start of the sturzstromer's
    next turn. The save DCs are Strength-based.
desc_long: |-
  Sturzstromers, also known as living landslides, are the elemental incarnations of earth in motion, from crushing rockfalls to landscape-altering avalanches. A sturzstromer consists of hundreds of stones, each moving of its own volition. When at rest, the stones lie atop one another; when the sturzstromer moves, the stones roll and churn, drawing smaller pebbles and dirt into their mass. Some observers are able to discern faces in the textures and colors of these rocks.

   The individual rocks that compose a sturzstromer are roughly a foot in diameter, though often irregularly shaped, and weigh approximately 80 pounds each. Altogether, a sturzstromer weighs around 12 tons, and when formed into a pile, the peak reaches 5 feet high.

---

# Sturzstromer
Stones _[[spells/Jump|jump]]_ and roll as if moved by an _[[spells/Earthquake|earthquake]]_ that affects nothing else around it. A wave of disturbed earth and rock follows behind them.
**Source** Pathfinder #138: Rise of New Thassilon pg. 92
**XP** 204,800

CN Tiny outsider (earth, elemental, extraplanar, swarm)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Tremorsense|tremorsense]]_ 120 ft.; Perception +33

##### Defense

**AC** 34, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 32 (+1 Dex, +1 dodge, +20 natural, +2 size)
**hp** 324 (24d10+192)
**Fort** +22, **Ref** +17, **Will** +16
**DR** 10/—; **Immune** electricity, elemental traits, swarm traits; **Resist** cold 30, fire 30; **SR** 30

##### Offense
**Speed** 50 ft.
**Melee** swarm (6d6+6 plus _[[universal monster rules/Distraction|distraction]]_)
**Ranged** rock +29/+24/+19/+14 (6d6+6)
**Space** 10 ft., **Reach** 0 ft.
**Special Attacks** _distraction_ (DC 30), landslide, powerful swarm, _[[universal monster rules/Rock Throwing|rock throwing]]_ (120 ft.), rumble, _[[universal monster rules/Trample|trample]]_ (6d6+6, DC 26)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 19th; concentration +21)
Constant—_[[spells/Stone Tell|stone tell]]_

##### Statistics
**Str** 18, **Dex** 13, **Con** 27, **Int** 10, **Wis** 22, **Cha** 15
**Base Atk** +24; **CMB** —; **CMD** —
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _Dodge_, _[[feats/Greater Blind-Fight|Greater Blind-Fight]]_, _[[feats/Improved Blind-Fight|Improved Blind-Fight]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Lightning Reflexes|Improved Lightning Reflexes]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quick Draw|Quick Draw]]_, Run, _[[feats/Weapon Focus|Weapon Focus]]_ (rock)
**Skills** Appraise +27, _[[universal monster rules/Climb|Climb]]_ +31, Knowledge (geography) +27, Knowledge (planes) +27, Perception +33, Stealth +36
**Languages** Terran; _stone tell_
**SQ** _[[npcs/Mountaineer|mountaineer]]_

##### Ecology

**Environment** any mountains (Plane of Earth)
**Organization** solitary
**Treasure** incidental

### Special Abilities

**Landslide (Ex)** When a _[[monsters/Sturzstromer|sturzstromer]]_ runs, it can create an avalanche 1d6×100 feet wide along the path which it moves as a free action. The _sturzstromer_ must be in an area of natural rock, soil, or sand and moving downhill, though even gentle slopes are sufficient, and it can use this ability only if it took sonic damage within the past round or if it used its landslide or rumble abilities in the previous round. Each creature caught in the avalanche can attempt a DC 26 Reflex save to halve damage in the bury zone or negate damage in the slide zone. The _sturzstromer_ is unaffected by its own avalanche. The save DC is Strength based.

**_Mountaineer_ (Ex)** A _sturzstromer_ takes no penalty to speed or on Acrobatics or Stealth checks when moving across steep slopes, rubble, or scree. In addition, a _sturzstromer_ can hide in rocky terrain, even if that terrain provides no cover or concealment.

**Powerful Swarm (Ex)** A _sturzstromer_ adds 1-1/2 times its Strength modifier on swarm damage rolls, and it is treated as a Large creature for the purposes of its _rock throwing_ and _trample_ abilities.

**Rumble (Ex)** As a full-round action, a _sturzstromer_ can create a rumble that _[[diseases/Shakes|shakes]]_ the ground and air in a 120-ft. radius centered on the _sturzstromer_ (the _sturzstromer_ still makes a swarm attack at the end of this round). A creature that starts its turn in the affected area must succeed at a DC 26 Reflex save or be unable to move. A creature that fails this save by 5 or more is knocked _[[conditions/Prone|prone]]_; a flying creature falls instead. Casting a spell in this area requires a successful concentration check (DC = 15 + the level of the spell being cast). All other concentration checks in the area have their DCs increased by 5. The DC of Perception checks is likewise increased by 5. The effects of this ability last until the start of the _sturzstromer_’s next turn. The save DCs are Strength-based.

##### Description

Sturzstromers, also known as living landslides, are the elemental incarnations of earth in motion, from crushing rockfalls to landscape-altering avalanches. A _sturzstromer_ consists of hundreds of stones, each moving of its own volition. When at rest, the stones lie atop one another; when the _sturzstromer_ moves, the stones roll and churn, drawing smaller pebbles and dirt into their mass. Some observers are able to discern faces in the textures and colors of these rocks.

The individual rocks that compose a _sturzstromer_ are roughly a foot in diameter, though often irregularly shaped, and weigh approximately 80 pounds each. Altogether, a _sturzstromer_ weighs around 12 tons, and when formed into a pile, the peak reaches 5 feet high.
---
cssclass: [monsters]
title1: Demon, Shemhazian
desc_short: 'This enormous, bestial demon combines the worst aspects of a bear, a
  mantis, a wolf, and a reptilian humanoid. '
title2: Shemhazian
CR: 16
sources:
- name: Bestiary 2
  page: 80
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
- name: 'Pathfinder #5: Sins of the Saviors'
  page: 86
  link: http://paizo.com/pathfinder/adventurePath/riseOfTheRunelords/v5748btpy815o
XP: 76800
alignment: CE
size: Gargantuan
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 4
senses:
  darkvision: 60
  detect good: true
  scent: true
  true seeing: true
AC:
  AC: 31
  touch: 11
  flat_footed: 26
  components:
    dex: 4
    dodge: 1
    natural: 20
    size: -4
HP:
  HP: 246
  long: 17d10+153
saves:
  fort: 19
  ref: 11
  will: 18
DR:
- amount: 10
  weakness: cold iron and good
immunities:
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 27
speeds:
  base: 40
  climb: 20
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +25 (2d6+12 plus 2d4 Strength drain)
      entries:
      - - damage: 2d6+12
        - damage: 2d4
          type: Strength drain
      attack: bite
      bonus:
      - 25
    - text: 2 claws +25 (2d6+12)
      entries:
      - - damage: 2d6+12
      count: 2
      attack: claws
      bonus:
      - 25
    - text: 2 pincers +23 (1d12+6)
      entries:
      - - damage: 1d12+6
      count: 2
      attack: pincers
      bonus:
      - 23
    - text: tail slap +23 (2d6+6)
      entries:
      - - damage: 2d6+6
      attack: tail slap
      bonus:
      - 23
  special:
  - paralyzing gaze
  - rend (2 claws, 2d6+18)
space: 20
reach: 20
reach_other: 30 ft. with tail slap
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: fly
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: invisibility
    source: default
    freq: At will
  - name: telekinesis
    source: default
    freq: At will
    DC: 18
  - name: clairaudience/clairvoyance
    source: default
    freq: 3/day
  - name: mass inflict serious wounds
    source: default
    freq: 3/day
    DC: 20
  - name: prying eyes
    source: default
    freq: 3/day
  - name: blasphemy
    source: default
    freq: 1/day
    DC: 20
  - name: summon
    source: default
    freq: 1/day
    level: 5
    summons:
    - name: shemhazian
      amount: 1
      chance: 30%
    - name: vrocks
      amount: 1d4
      chance: 60%
  sources:
  - name: default
    CL: 15
    concentration: 18
ability_scores:
  STR: 35
  DEX: 19
  CON: 29
  INT: 10
  WIS: 26
  CHA: 16
BAB: 17
CMB: 33
CMD: 48
feats:
- name: Awesome Blow
- name: Combat Reflexes
- name: Dodge
- name: Improved Bull Rush
- name: Improved Vital Strike
- name: Lightning Reflexes
- name: Multiattack
- name: Power Attack
- name: Vital Strike
skills:
  Bluff: 23
  Climb: 20
  Fly: 2
  Heal: 28
  Intimidate: 23
  Knowledge (religion): 20
  Perception: 36
  Sense Motive: 28
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
ecology:
  environment: any (the Abyss)
  organization: solitary
  treasure_type: standard
special_abilities:
  Paralyzing Gaze (Su): Paralysis for 1 round, 30 feet, Fortitude DC 21 negates. Evil
    creatures are immune to this effect. The save DC is Charisma-based.
  Strength Drain (Su): A shemhazian demon deals 2d4 points of Strength drain with
    each successful bite. A DC 27 Fortitude save reduces this amount to 1d4 points
    of Strength damage. The save DC is Constitution-based.
desc_long: |-
  Although nearly all the horrors of the Abyss prey upon one another in an endless, eternal bloodbath, shemhazians are predators among predators. They are more intimidating and physically powerful than most demons, combining the features of numerous insectile and bestial hunters into one massive, deadly form. Although they don't require sustenance, shemhazians take perverse delight in mutilating and eating their victims. 

  A shemhazian stands 35 feet tall and weighs 12,000 pounds. They form from the sinful souls of torturers and those who enjoyed mutilating living victims to death.

---

# Demon, Shemhazian
This enormous, bestial demon combines the worst aspects of a bear, a mantis, a _[[monsters/Wolf|wolf]]_, and a reptilian humanoid.

**Source** Bestiary 2 pg. 80, Pathfinder #5: Sins of the Saviors pg. 86
**XP** 76,800
CE Gargantuan outsider (chaotic, demon, evil, extraplanar)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[universal monster rules/Scent|scent]]_, _[[spells/True Seeing|true seeing]]_; Perception +36

##### Defense

**AC** 31, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+4 Dex, +1 dodge, +20 natural, –4 size)
**hp** 246 (17d10+153)
**Fort** +19, **Ref** +11, **Will** +18
**DR** 10/cold iron and good; **Immune** electricity, poison; **Resist** acid 10, cold 10, fire 10; **SR** 27

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 20 ft., fly 60 ft. (good)
**Melee** bite +25 (2d6+12 plus 2d4 Strength drain), 2 claws +25 (2d6+12), 2 pincers +23 (1d12+6), tail slap +23 (2d6+6)
**Space** 20 ft., **Reach** 20 ft. (30 ft. with tail slap)
**Special Attacks** paralyzing _[[universal monster rules/Gaze|gaze]]_, _[[universal monster rules/Rend|rend]]_ (2 claws, 2d6+18)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +18)
Constant—_detect good_, fly, _true seeing_
At will—greater teleport (self plus 50 lbs. of objects only), _[[spells/Invisibility|invisibility]]_, _[[spells/Telekinesis|telekinesis]]_ (DC 18)
3/day—clairaudience/clairvoyance, mass _[[spells/Inflict Serious Wounds|inflict serious wounds]]_ (DC 20), _[[spells/Prying Eyes|prying eyes]]_
1/day—_[[spells/Blasphemy|blasphemy]]_ (DC 20), _[[universal monster rules/Summon|summon]]_ (level 5, 1 shemhazian 30% or 1d4 vrocks 60%)

##### Statistics
**Str** 35, **Dex** 19, **Con** 29, **Int** 10, **Wis** 26, **Cha** 16
**Base Atk** +17; **CMB** +33; **CMD** 48
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Bluff +23, _Climb_ +20, Fly +2, _[[spells/Heal|Heal]]_ +28, Intimidate +23, Knowledge (religion) +20, Perception +36, Sense Motive +28; **Racial Modifiers** +8 Perception
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (the Abyss)
**Organization** solitary
**Treasure** standard

### Special Abilities

**Paralyzing _Gaze_ (Su)** _[[universal monster rules/Paralysis|Paralysis]]_ for 1 round, 30 feet, Fortitude DC 21 negates. Evil creatures are immune to this effect. The save DC is Charisma-based.
**Strength Drain (Su)** A shemhazian demon deals 2d4 points of Strength drain with each successful bite. A DC 27 Fortitude save reduces this amount to 1d4 points of Strength damage. The save DC is Constitution-based.

##### Description

Although nearly all the horrors of the Abyss prey upon one another in an endless, eternal _[[spells/Bloodbath|bloodbath]]_, shemhazians are predators among predators. They are more intimidating and physically powerful than most demons, combining the features of numerous insectile and bestial hunters into one massive, _[[items/Weapon Magic Abilities/Deadly|deadly]]_ form. Although they don’t require sustenance, shemhazians take perverse delight in mutilating and eating their victims.

A shemhazian stands 35 feet tall and weighs 12,000 pounds. They form from the sinful souls of torturers and those who enjoyed mutilating living victims to death.
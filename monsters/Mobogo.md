---
cssclass: [monsters]
title1: Mobogo
desc_short: This grotesque creature looks like a gigantic toad with leathery wings,
  fangs, horns, and three bulbous eyes.
title2: Mobogo
CR: 10
sources:
- name: Bestiary 3
  page: 194
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
- name: 'Pathfinder #12: Crown of Fangs'
  page: 88
  link: http://paizo.com/pathfinder/adventurePath/curseOfTheCrimsonThrone/v5748btpy84el
XP: 9600
alignment: CE
size: Huge
type: magical beast
subtypes:
- aquatic
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 24
  touch: 10
  flat_footed: 22
  components:
    dex: 2
    natural: 14
    size: -2
HP:
  HP: 136
  long: 13d10+65
  regeneration: 5
  regeneration_weakness: acid, cold, or fire
saves:
  fort: 13
  ref: 10
  will: 8
speeds:
  base: 30
  fly: 30
  fly_maneuverability: poor
  swim: 40
attacks:
  melee:
  - - text: bite +20 (2d6+9)
      entries:
      - - damage: 2d6+9
      attack: bite
      bonus:
      - 20
    - text: 2 slams +20 (1d8+9)
      entries:
      - - damage: 1d8+9
      count: 2
      attack: slams
      bonus:
      - 20
  - - text: tongue +20 (1d6+9 plus grab and pull)
      entries:
      - - damage: 1d6+9
        - effect: grab
        - effect: pull
      attack: tongue
      bonus:
      - 20
  special:
  - crush (DC 21, 2d8+13, see page 92)
  - pull (tongue, 5 ft.)
  - swallow whole (2d6+13 bludgeoning damage, AC 17, 13 hp)
  - vile croak
space: 15
reach: 15
reach_other: 45 ft. with tongue
spell_like_abilities:
  entries:
  - name: pass without trace
    source: default
    freq: Constant
  - name: speak with animals
    source: default
    freq: Constant
  - name: charm animal
    source: default
    freq: At will
    DC: 14
  - name: create water
    source: default
    freq: At will
  - name: sound burst
    source: default
    freq: At will
    DC: 15
  - name: control water
    source: default
    freq: 3/day
  - name: fog cloud
    source: default
    freq: 3/day
  - name: gust of wind
    source: default
    freq: 3/day
    DC: 15
  - name: plant growth
    source: default
    freq: 3/day
  - name: quench
    source: default
    freq: 3/day
    DC: 16
  - name: soften earth and stone
    source: default
    freq: 3/day
    DC: 15
  sources:
  - name: default
    CL: 8
    concentration: 11
ability_scores:
  STR: 28
  DEX: 15
  CON: 21
  INT: 6
  WIS: 15
  CHA: 16
BAB: 13
CMB: 24
CMB_other: +28 grapple
CMD: 36
CMD_other: 40 vs. trip
feats:
- name: Awesome Blow
- name: Cleave
- name: Combat Reflexes
- name: Improved Bull Rush
- name: Improved Overrun
- name: Iron Will
- name: Power Attack
skills:
  Acrobatics: 9
    when jumping: 17
  Fly: -6
  Perception: 19
  Stealth: 0
    in swamps: 8
  Swim: 17
  _racial_mods:
    Acrobatics:
      when jumping: 8
    Perception:
      _: 8
    Stealth:
      in swamps: 8
languages:
- Boggard
- speak with animals
special_qualities:
- amphibious
- swamp stride
ecology:
  environment: temperate swamps
  organization: solitary or gang (2-4)
  treasure_type: standard
special_abilities:
  Swamp Stride (Ex): A mobogo can move through any sort of natural difficult terrain
    at its normal speed while within a swamp. Magically altered terrain affects it
    normally.
  Tongue (Ex): A mobogo's tongue is a primary attack with reach equal to three times
    the mobogo's normal reach (45 feet for a typical mobogo). A mobogo does not gain
    the grappled condition when using its tongue to grapple a foe.
  Vile Croak (Su): As a standard action once every 1d4 rounds, a mobogo can unleash
    a thunderous croak. Any non-boggard or non-mobogo within 50 feet of the mobogo
    must make a DC 19 Will save or become staggered for 1d4 rounds. Once a creature
    makes its saving throw against a particular mobogo's vile croak, it is immune
    to that mobogo's croak for 24 hours. Any boggards or mobogos within the area of
    a mobogo's vile croak gains a +2 morale bonus on attack rolls and saving throws
    against fear effects for 1 round. The save DC is Charisma-based.
desc_long: |-
  Huge and hungry, mobogos merge the features of gigantic toads and swampy dragons, and lair in the deepest, oldest swamps. Here, whole tribes of boggards serve the beasts' fickle, capricious whims.

  Mobogos reside in the most primal swamps of the world, grotesque eldritch wildernesses unchanged for centuries. Boggards believe that in ancient times, after their fecund demon goddess deposited her frogspawn in the muddy morass of the world's still-forming continents, mobogos were among the first creatures to emerge. Ever since, the mobogos have slept and fed, preying upon the beasts of their fetid meres, growing huge and lethargic, and dreaming inscrutable amphibious dreams of their godly mother's return. Nearly all mobogos are attended by tribes of boggards. Mobogos care little for matters of origins and philosophies-they care only for the endless sacrifices of food, victims, and pleasing swamp art brought to them by their obedient tribes.

  A mobogo is 18 feet tall and weighs 12,000 pounds.

---

# Mobogo
This grotesque creature looks like a gigantic toad with leathery wings, fangs, horns, and three bulbous eyes.
**Source** Bestiary 3 pg. 194, Pathfinder #12: _[[items/Wondrous Item/Crown of Fangs|Crown of Fangs]]_ pg. 88
**XP** 9,600
CE Huge magical beast (aquatic)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +19

##### Defense

**AC** 24, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+2 Dex, +14 natural, –2 size)
**hp** 136 (13d10+65); _[[universal monster rules/Regeneration|regeneration]]_ 5 (acid, cold, or fire)
**Fort** +13, **Ref** +10, **Will** +8

##### Offense
**Speed** 30 ft., fly 30 ft. (poor), swim 40 ft.
**Melee** bite +20 (2d6+9), 2 slams +20 (1d8+9) or tongue +20 (1d6+9 plus _[[universal monster rules/Grab|grab]]_ and _[[universal monster rules/Pull|pull]]_)
**Space** 15 ft., **Reach** 15 ft. (45 ft. with tongue)
**Special Attacks** crush (DC 21, 2d8+13, see page 92), _pull_ (tongue, 5 ft.), _[[universal monster rules/Swallow Whole|swallow whole]]_ (2d6+13 bludgeoning damage, AC 17, 13 hp), vile croak
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +11)
Constant—_[[spells/Pass without Trace|pass without trace]]_, _[[spells/Speak with Animals|speak with animals]]_
At will—_[[spells/Charm Animal|charm animal]]_ (DC 14), _[[spells/Create Water|create water]]_, _[[spells/Sound Burst|sound burst]]_ (DC 15)
3/day—_[[spells/Control Water|control water]]_, _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Gust Of Wind|gust of wind]]_ (DC 15), _[[spells/Plant Growth|plant growth]]_, _[[spells/Quench|quench]]_ (DC 16), _[[spells/Soften Earth and Stone|soften earth and stone]]_ (DC 15)

##### Statistics
**Str** 28, **Dex** 15, **Con** 21, **Int** 6, **Wis** 15, **Cha** 16
**Base Atk** +13; **CMB** +24 (+28 grapple); **CMD** 36 (40 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Overrun|Improved Overrun]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Acrobatics +9 (+17 when jumping), Fly –6, Perception +19, Stealth +0 (+8 in swamps), Swim +17; **Racial Modifiers** +8 Acrobatics when jumping, +8 Perception, +8 Stealth in swamps
**Languages** _[[monsters/Boggard|Boggard]]_; _speak with animals_
**SQ** _[[universal monster rules/Amphibious|amphibious]]_, swamp stride

##### Ecology

**Environment** temperate swamps
**Organization** solitary or gang (2–4)
**Treasure** standard

### Special Abilities
**Swamp Stride (Ex) **A _[[monsters/Mobogo|mobogo]]_ can move through any sort of natural difficult terrain at its normal speed while within a swamp. Magically altered terrain affects it normally.

**Tongue (Ex)** A _mobogo_’s tongue is a primary attack with reach equal to three times the _mobogo_’s normal reach (45 feet for a typical _mobogo_). A _mobogo_ does not gain the _[[conditions/Grappled|grappled]]_ condition when using its tongue to grapple a foe.

**Vile Croak (Su)** As a standard action once every 1d4 rounds, a _mobogo_ can unleash a thunderous croak. Any non-boggard or non-mobogo within 50 feet of the _mobogo_ must make a DC 19 Will save or become _[[conditions/Staggered|staggered]]_ for 1d4 rounds. Once a creature makes its saving throw against a particular _mobogo_’s vile croak, it is immune to that _mobogo_’s croak for 24 hours. Any boggards or mobogos within the area of a _mobogo_’s vile croak gains a +2 morale bonus on attack rolls and saving throws against _[[universal monster rules/Fear|fear]]_ effects for 1 round. The save DC is Charisma-based.

##### Description

Huge and hungry, mobogos merge the features of gigantic toads and swampy dragons, and lair in the deepest, oldest swamps. Here, whole tribes of boggards serve the beasts’ fickle, capricious whims.

Mobogos reside in the most primal swamps of the world, grotesque eldritch wildernesses unchanged for centuries. Boggards believe that in ancient times, after their fecund demon goddess deposited her frogspawn in the muddy morass of the world’s still-forming continents, mobogos were among the first creatures to emerge. Ever since, the mobogos have slept and fed, preying upon the beasts of their fetid meres, _[[items/Weapon Magic Abilities/Growing|growing]]_ huge and lethargic, and dreaming inscrutable _amphibious_ dreams of their godly mother’s return. Nearly all mobogos are attended by tribes of boggards. Mobogos care little for matters of origins and philosophies—they care only for the endless sacrifices of food, victims, and pleasing swamp art brought to them by their obedient tribes.

A _mobogo_ is 18 feet tall and weighs 12,000 pounds.
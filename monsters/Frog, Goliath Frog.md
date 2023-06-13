---
cssclass: [monsters]
title1: Frog, Goliath Frog
desc_short: This massive, mottled amphibian glistens with slime, and its tongue drips
  with saliva.
title2: Goliath Frog
CR: 3
sources:
- name: Bestiary 5
  page: 117
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 800
alignment: N
size: Large
type: animal
initiative:
  bonus: 1
senses:
  low-light vision: true
  scent: true
AC:
  AC: 15
  touch: 10
  flat_footed: 14
  components:
    dex: 1
    natural: 5
    size: -1
HP:
  HP: 34
  long: 4d8+16
saves:
  fort: 8
  ref: 7
  will: 1
speeds:
  base: 30
  climb: 20
  swim: 30
attacks:
  melee:
  - - text: bite +6 (2d6+6 plus grab)
      entries:
      - - damage: 2d6+6
        - effect: grab
      attack: bite
      bonus:
      - 6
  - - text: tongue +6 (grab)
      entries:
      - - effect: grab
      attack: tongue
      bonus:
      - 6
  special:
  - fast swallow
  - pull (tongue, 5 ft.)
  - swallow whole (1d6 bludgeoning damage, AC 12, 3 hp)
  - tongue
space: 10
reach: 5
reach_other: 15 ft. with tongue
ability_scores:
  STR: 19
  DEX: 13
  CON: 18
  INT: 1
  WIS: 10
  CHA: 6
BAB: 3
CMB: 8
CMB_other: +12 grapple
CMD: 19
CMD_other: 23 vs. trip
feats:
- name: Lightning Reflexes
- name: Skill Focus (Acrobatics)
skills:
  Acrobatics: 12
    when jumping: 20
  Climb: 16
  Perception: 8
  Stealth: 5
  Swim: 12
  _racial_mods:
    Acrobatics:
      _: 4
      when jumping: 12
    Perception:
      _: 4
    Stealth:
      _: 4
ecology:
  environment: warm marshes or water
  organization: solitary, pair, or army (3-6)
  treasure_type: none
special_abilities:
  Tongue (Ex): A goliath frog's tongue is a primary attack with three times the reach
    of its bite. Its tongue deals no damage but can be used to grab. The frog does
    not gain the grappled condition when grappling with its tongue.
desc_long: These hulking frogs haunt warm marshlands and river shallows where thick
  undergrowth can conceal them. They are dangerous, aggressive predators that gorge
  themselves on smaller creatures or team up to bring down larger prey. They often
  climb to the low branches of ancient, mossy trees, picking off prey from the wetland's
  floor before their existence is even suspected.

---

# Frog, Goliath Frog
This massive, mottled amphibian glistens with slime, and its tongue drips with saliva.
**Source** Bestiary 5 pg. 117
**XP** 800

N Large animal
**Init** +1; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +8

##### Defense

**AC** 15, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+1 Dex, +5 natural, –1 size)
**hp** 34 (4d8+16)
**Fort** +8, **Ref** +7, **Will** +1

##### Offense
**Speed** 30 ft., _[[universal monster rules/Climb|climb]]_ 20 ft., swim 30 ft.
**Melee** bite +6 (2d6+6 plus _[[universal monster rules/Grab|grab]]_) or tongue +6 (_grab_)
**Space** 10 ft., **Reach** 5 ft. (15 ft. with tongue)
**Special Attacks** _[[universal monster rules/Fast Swallow|fast swallow]]_, _[[universal monster rules/Pull|pull]]_ (tongue, 5 ft.), _[[universal monster rules/Swallow Whole|swallow whole]]_ (1d6 bludgeoning damage, AC 12, 3 hp) , tongue

##### Statistics
**Str** 19, **Dex** 13, **Con** 18, **Int** 1, **Wis** 10, **Cha** 6
**Base Atk** +3; **CMB** +8 (+12 grapple); **CMD** 19 (23 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Skill Focus|Skill Focus]]_ (Acrobatics)
**Skills** Acrobatics +12 (+20 when jumping), _Climb_ +16, Perception +8, Stealth +5, Swim +12; **Racial Modifiers** +4 Acrobatics (+12 when jumping), +4 Perception, +4 Stealth

##### Ecology

**Environment** warm marshes or water
**Organization** solitary, pair, or army (3–6)
**Treasure** none

### Special Abilities

**Tongue (Ex)** A goliath frog’s tongue is a primary attack with three times the reach of its bite. Its tongue deals no damage but can be used to _grab_. The frog does not gain the _[[conditions/Grappled|grappled]]_ condition when grappling with its tongue.

##### Description

These hulking frogs haunt warm marshlands and river shallows where thick undergrowth can conceal them. They are dangerous, aggressive predators that gorge themselves on smaller creatures or _[[feats/Team Up|team up]]_ to bring down larger prey. They often _climb_ to the low branches of ancient, mossy trees, picking off prey from the wetland’s floor before their existence is even suspected.
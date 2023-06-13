---
cssclass: [monsters]
title1: Frog, Giant Frog
desc_short: This creature looks like a normal frog, with moist, mottled, blackish-green
  skin, but grown to truly monstrous size.
title2: Giant Frog
CR: 1
sources:
- name: Pathfinder RPG Bestiary
  page: 135
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 400
alignment: N
size: Medium
type: animal
initiative:
  bonus: 1
senses:
  low-light vision: true
  scent: true
AC:
  AC: 12
  touch: 11
  flat_footed: 11
  components:
    dex: 1
    natural: 1
HP:
  HP: 15
  long: 2d8+6
saves:
  fort: 6
  ref: 6
  will: -1
speeds:
  base: 30
  swim: 30
attacks:
  melee:
  - - text: bite +3 (1d6+2 plus grab)
      entries:
      - - damage: 1d6+2
        - effect: grab
      attack: bite
      bonus:
      - 3
  - - text: tongue +3 touch (grab)
      entries:
      - - effect: grab
      attack: tongue
      bonus:
      - 3
      touch: true
  special:
  - pull (tongue, 5 feet)
  - swallow whole (1d4 bludgeoning damage, AC 10, 1 hp)
  - tongue
space: 5
reach: 5
reach_other: 15 ft. with tongue
ability_scores:
  STR: 15
  DEX: 13
  CON: 16
  INT: 1
  WIS: 8
  CHA: 6
BAB: 1
CMB: 3
CMB_other: +7 grapple
CMD: 14
CMD_other: 18 vs. trip
feats:
- name: Lightning Reflexes
skills:
  Acrobatics: 9
    jumping: 13
  Perception: 3
  Stealth: 5
  Swim: 10
  _racial_mods:
    Acrobatics:
      _: 4
      jumping: 8
    Stealth:
      _: 4
ecology:
  environment: temperate or warm marshes and aquatic
  organization: solitary, pair, or army (3-8)
  treasure_type: none
special_abilities:
  Tongue (Ex): A giant frog's tongue is a primary attack with reach equal to three
    times the frog's normal reach (15 feet for a Medium giant frog). A giant frog's
    tongue deals no damage on a hit, but can be used to grab. A giant frog does not
    gain the grappled condition while using its tongue in this manner.
desc_long: Giant frogs have razor-sharp teeth lining their mouths. They are 6 feet
  long and weigh 200 pounds.

---

# Frog, Giant Frog
This creature looks like a normal frog, with moist, mottled, blackish-green skin, but grown to truly monstrous size.
**Source** Pathfinder RPG Bestiary pg. 135
**XP** 400

N Medium animal
**Init** +1; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +3

##### Defense

**AC** 12, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 11 (+1 Dex, +1 natural)
**hp** 15 (2d8+6)
**Fort** +6, **Ref** +6, **Will** –1

##### Offense
**Speed** 30 ft., swim 30 ft.
**Melee** bite +3 (1d6+2 plus _[[universal monster rules/Grab|grab]]_) or tongue +3 touch (_grab_)
**Space** 5 ft., **Reach** 5 ft. (15 ft. with tongue)
**Special Attacks** _[[universal monster rules/Pull|pull]]_ (tongue, 5 feet), _[[universal monster rules/Swallow Whole|swallow whole]]_ (1d4 bludgeoning damage, AC 10, 1 hp), tongue

##### Statistics
**Str** 15, **Dex** 13, **Con** 16, **Int** 1, **Wis** 8, **Cha** 6
**Base Atk** +1; **CMB** +3 (+7 grapple); **CMD** 14 (18 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Acrobatics +9 (+13 jumping), Perception +3, Stealth +5, Swim +10; **Racial Modifiers** +4 Acrobatics (+8 jumping), +4 Stealth

##### Ecology

**Environment** temperate or warm marshes and aquatic
**Organization** solitary, pair, or army (3–8)
**Treasure** none

### Special Abilities

**Tongue (Ex)** A giant frog’s tongue is a primary attack with reach equal to three times the frog’s normal reach (15 feet for a _Medium_ giant frog). A giant frog’s tongue deals no damage on a hit, but can be used to _grab_. A giant frog does not gain the _[[conditions/Grappled|grappled]]_ condition while using its tongue in this manner.

##### Description

Giant frogs have razor-sharp teeth lining their mouths. They are 6 feet long and weigh 200 pounds.
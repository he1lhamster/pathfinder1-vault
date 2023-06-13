---
cssclass: [monsters]
title1: Frog, Frog Father
desc_short: This elephantine amphibian has a grotesquely long tongue and beady eyes.
title2: Frog Father
CR: 5
sources:
- name: Bestiary 5
  page: 117
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 1600
alignment: N
size: Huge
type: animal
initiative:
  bonus: 1
senses:
  low-light vision: true
  scent: true
AC:
  AC: 18
  touch: 9
  flat_footed: 17
  components:
    dex: 1
    natural: 9
    size: -2
HP:
  HP: 57
  long: 6d8+30
saves:
  fort: 10
  ref: 8
  will: 4
speeds:
  base: 30
  swim: 30
attacks:
  melee:
  - - text: bite +8 (3d6+9 plus grab)
      entries:
      - - damage: 3d6+9
        - effect: grab
      attack: bite
      bonus:
      - 8
    - text: tongue +8 (grab)
      entries:
      - - effect: grab
      attack: tongue
      bonus:
      - 8
  special:
  - fast swallow
  - pull (tongue, 10 ft.)
  - swallow whole (2d6 bludgeoning damage, AC 14, 5 hp)
  - tongue
space: 15
reach: 10
reach_other: 30 ft. with tongue
ability_scores:
  STR: 23
  DEX: 13
  CON: 20
  INT: 1
  WIS: 10
  CHA: 6
BAB: 4
CMB: 12
CMD: 23
CMD_other: 27 vs. trip
feats:
- name: Iron Will
- name: Lightning Reflexes
- name: Skill Focus (Acrobatics)
skills:
  Acrobatics: 12
    jumping: 20
  Perception: 10
  Stealth: 2
  Swim: 14
  _racial_mods:
    Acrobatics:
      _: 4
      jumping: 12
    Perception:
      _: 4
    Stealth:
      _: 4
ecology:
  environment: warm marshes or water
  organization: solitary or pair
  treasure_type: none
special_abilities:
  Tongue (Ex): A frog father's tongue is a primary attack with three times the reach
    of its bite. Its tongue deals no damage but can be used to grab. The frog does
    not gain the grappled condition when grappling with its tongue.
desc_long: Frog fathers devour entire hives of monstrous vermin and any livestock
  that stray too close to their marshes, but happily gulp down any prey that crosses
  their paths. Their long, sticky tongues allow them to capture and restrain prey
  while they determine whether they want to consume it. A frog father's chosen prey
  has little chance of escaping, as the frog's powerful throat muscles allow it to
  swallow even large creatures rapidly.

---

# Frog, Frog Father
This elephantine amphibian has a grotesquely long tongue and beady eyes.
**Source** Bestiary 5 pg. 117
**XP** 1,600

N Huge animal
**Init** +1; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +10

##### Defense

**AC** 18, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+1 Dex, +9 natural, –2 size)
**hp** 57 (6d8+30)
**Fort** +10, **Ref** +8, **Will** +4

##### Offense
**Speed** 30 ft., swim 30 ft.
**Melee** bite +8 (3d6+9 plus _[[universal monster rules/Grab|grab]]_), tongue +8 (_grab_)
**Space** 15 ft., **Reach** 10 ft. (30 ft. with tongue)
**Special Attacks** _[[universal monster rules/Fast Swallow|fast swallow]]_, _[[universal monster rules/Pull|pull]]_ (tongue, 10 ft.), _[[universal monster rules/Swallow Whole|swallow whole]]_ (2d6 bludgeoning damage, AC 14, 5 hp), tongue

##### Statistics
**Str** 23, **Dex** 13, **Con** 20, **Int** 1, **Wis** 10, **Cha** 6
**Base Atk** +4; **CMB** +12; **CMD** 23 (27 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Skill Focus|Skill Focus]]_ (Acrobatics)
**Skills** Acrobatics +12 (+20 jumping), Perception +10, Stealth +2, Swim +14; **Racial Modifiers** +4 Acrobatics (+12 jumping), +4 Perception, +4 Stealth

##### Ecology

**Environment** warm marshes or water
**Organization** solitary or pair
**Treasure** none

### Special Abilities

**Tongue (Ex)** A frog father’s tongue is a primary attack with three times the reach of its bite. Its tongue deals no damage but can be used to _grab_. The frog does not gain the _[[conditions/Grappled|grappled]]_ condition when grappling with its tongue.

##### Description

Frog fathers devour entire hives of monstrous vermin and any livestock that stray too close to their marshes, but happily gulp down any prey that crosses their paths. Their long, _[[items/Weapon Magic Abilities/Sticky|sticky]]_ _[[spells/Tongues|tongues]]_ allow them to capture and restrain prey while they determine whether they want to consume it. A frog father’s chosen prey has little chance of escaping, as the frog’s powerful throat muscles allow it to swallow even large creatures rapidly.
---
cssclass: [monsters]
title1: Eel, Electric Eel
desc_short: This six-foot-long, snake-like fish moves slowly. A strange popping and
  snapping sound occasionally emits from the creature's body.
title2: Electric Eel
CR: 2
sources:
- name: Pathfinder RPG Bestiary
  page: 119
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 600
alignment: N
size: Small
type: animal
initiative:
  bonus: 6
senses:
  low-light vision: true
AC:
  AC: 15
  touch: 13
  flat_footed: 13
  components:
    dex: 2
    natural: 2
    size: 1
HP:
  HP: 17
  long: 2d8+8
saves:
  fort: 7
  ref: 5
  will: 0
resistances:
  electricity: 10
speeds:
  base: 5
  swim: 30
attacks:
  melee:
  - - text: bite +3 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: bite
      bonus:
      - 3
    - text: tail -2 touch (1d6 electricity)
      entries:
      - - damage: 1d6
          type: electricity
      attack: tail
      bonus:
      - -2
      touch: true
ability_scores:
  STR: 13
  DEX: 14
  CON: 19
  INT: 1
  WIS: 10
  CHA: 6
BAB: 1
CMB: 1
CMD: 13
CMD_other: can't be tripped
feats:
- name: Improved Initiative
skills:
  Escape Artist: 10
  Perception: 4
  Stealth: 10
  Swim: 9
  _racial_mods:
    Escape Artist:
      _: 8
ecology:
  environment: warm fresh water
  organization: solitary
  treasure_type: none
special_abilities:
  Electricity (Ex): An electric eel can produce a powerful jolt of electricity from
    its tail, delivering the jolt with a successful touch attack. On a critical hit,
    the creature struck must make a DC 15 Fortitude save or be stunned for 1d4 rounds.
    The save DC is Constitution-based.
desc_long: The electric eel is a curious fish that breathes air instead of water,
  yet certainly its most unusual characteristic is its ability to generate powerful
  jolts of electricity. An electric eel is 6 feet long and weighs 45 pounds.

---

# Eel, Electric Eel
This six-foot-long, snake-like fish moves slowly. A strange popping and snapping sound occasionally emits from the creature’s body.
**Source** Pathfinder RPG Bestiary pg. 119
**XP** 600

N Small animal
**Init** +6; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +4

##### Defense

**AC** 15, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+2 Dex, +2 natural, +1 size)
**hp** 17 (2d8+8)
**Fort** +7, **Ref** +5, **Will** +0
**Resist** electricity 10

##### Offense
**Speed** 5 ft., swim 30 ft.
**Melee** bite +3 (1d6+1) and tail –2 touch (1d6 electricity)

##### Statistics
**Str** 13, **Dex** 14, **Con** 19, **Int** 1, **Wis** 10, **Cha** 6
**Base Atk** +1; **CMB** +1; **CMD** 13 (can’t be tripped)
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_
**Skills** Escape Artist +10, Perception +4, Stealth +10, Swim +9; **Racial Modifiers** +8 Escape Artist

##### Ecology

**Environment** warm fresh water
**Organization** solitary
**Treasure** none

### Special Abilities

**Electricity (Ex)** An electric eel can produce a powerful _[[spells/Jolt|jolt]]_ of electricity from its tail, delivering the _jolt_ with a successful touch attack. On a critical hit, the creature struck must make a DC 15 Fortitude save or be _[[conditions/Stunned|stunned]]_ for 1d4 rounds. The save DC is Constitution-based.

##### Description

The electric eel is a curious fish that breathes air instead of water, yet certainly its most unusual characteristic is its ability to generate powerful jolts of electricity. An electric eel is 6 feet long and weighs 45 pounds.
---
cssclass: [monsters]
title1: Boreal Creature, Boreal Manticore
desc_short: This white-furred creature has a vaguely humanoid head, the body of a
  lion, and the wings of a dragon. Its tail ends in long, sharp spikes encrusted with
  ice.
title2: Boreal Manticore
CR: 6
sources:
- name: Irrisen - Land of Eternal Winter
  page: 56
  link: http://paizo.com/products/btpy8w7f?Pathfinder-Campaign-Setting-Irrisen-Land-of-Eternal-Winter
XP: 2400
alignment: LE
size: Large
type: magical beast
subtypes:
- cold
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 17
  touch: 11
  flat_footed: 15
  components:
    dex: 2
    natural: 6
    size: -1
HP:
  HP: 63
  long: 6d10+30
saves:
  fort: 10
  ref: 7
  will: 3
immunities:
- cold
weaknesses:
- vulnerable to fire
speeds:
  base: 30
  fly: 50
  fly_maneuverability: clumsy
attacks:
  melee:
  - - text: bite +11 (1d8+6 plus 1d6 cold)
      entries:
      - - damage: 1d8+6
        - damage: 1d6
          type: cold
      attack: bite
      bonus:
      - 11
    - text: 2 claws +11 (2d4+6 plus 1d6 cold)
      entries:
      - - damage: 2d4+6
        - damage: 1d6
          type: cold
      count: 2
      attack: claws
      bonus:
      - 11
  ranged:
  - - text: 4 spikes +8 (1d6+5 plus 1d6 cold)
      entries:
      - - damage: 1d6+5
        - damage: 1d6
          type: cold
      count: 4
      attack: spikes
      bonus:
      - 8
space: 10
reach: 5
ability_scores:
  STR: 22
  DEX: 15
  CON: 20
  INT: 7
  WIS: 12
  CHA: 9
BAB: 6
CMB: 13
CMD: 23
CMD_other: 27 vs. trip
feats:
- name: Flyby Attack
- name: Hover
- name: Weapon Focus (spikes)
skills:
  Fly: -3
  Perception: 9
  Stealth: -2
    in snow: 2
  Survival: 4
    in snow or when tracking: 8
  _racial_mods:
    Perception:
      _: 4
    Stealth:
      in snow: 4
    Survival:
      in snow or when tracking: 4
languages:
- Common
special_qualities:
- trackless step
ecology:
  environment: cold forests
  organization: solitary, pair, or pride (3-12)
  treasure_type: standard
special_abilities:
  Spikes (Ex): With a snap of its tail, a manticore can loose a volley of four spikes
    as a standard action (make an attack roll for each spike). This attack has a range
    of 180 feet with no range increment. All targets must be within 30 feet of each
    other. The creature can launch only 24 spikes in any 24-hour period.
  Trackless Step (Ex): |-
    A boreal manticore does not leave a trail in snow and cannot be tracked. It can choose to leave a trail if it so desires.

    Though boreal creatures mostly resemble their temperate kin, the effects of sorcerous winter have bolstered them, making them stronger and much more dangerous. In basic shape and form they appear similar to their ancestors, but other characteristics reveal the creatures' altered nature. Their fur and skin are much paler, often shades of blue, gray, or simply white, and it is not uncommon for parts of these creatures to be cloaked in frost, especially their jagged claws and shaggy hair.
desc_long: ''

---

# Boreal Creature, Boreal Manticore
This white-furred creature has a vaguely humanoid head, the body of a _[[monsters/Lion|lion]]_, and the wings of a dragon. Its tail ends in long, sharp spikes encrusted with ice.
**Source** Irrisen - Land of Eternal Winter pg. 56
**XP** 2,400

LE Large magical beast (cold)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +9

##### Defense

**AC** 17, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+2 Dex, +6 natural, –1 size)
**hp** 63 (6d10+30)
**Fort** +10, **Ref** +7, **Will** +3
**Immune** cold
**Weaknesses** vulnerable to fire

##### Offense
**Speed** 30 ft., fly 50 ft. (clumsy)
**Melee** bite +11 (1d8+6 plus 1d6 cold), 2 claws +11 (2d4+6 plus 1d6 cold)
**Ranged** 4 spikes +8 (1d6+5 plus 1d6 cold)
**Space** 10 ft., **Reach** 5 ft.

##### Statistics
**Str** 22, **Dex** 15, **Con** 20, **Int** 7, **Wis** 12, **Cha** 9
**Base Atk** +6; **CMB** +13; **CMD** 23 (27 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (spikes)
**Skills** Fly –3, Perception +9, Stealth –2 (+2 in snow), Survival +4 (+8 in snow or when tracking); **Racial Modifiers** +4 Perception, +4 Stealth (in snow), +4 Survival (in snow or when tracking)
**Languages** Common
**SQ** _[[items/Armor Magic Abilities/Trackless|trackless]]_ step

##### Ecology

**Environment** cold forests
**Organization** solitary, pair, or pride (3–12)
**Treasure** standard

### Special Abilities
**Spikes (Ex) **With a snap of its tail, a _[[monsters/Manticore|manticore]]_ can loose a volley of four spikes as a standard action (make an attack roll for each spike). This attack has a range of 180 feet with no range increment. All targets must be within 30 feet of each other. The creature can launch only 24 spikes in any 24-hour period.

**_Trackless_ Step (Ex)** A boreal _manticore_ does not leave a trail in snow and cannot be tracked. It can choose to leave a trail if it so desires.

Though boreal creatures mostly resemble their temperate kin, the effects of sorcerous winter have bolstered them, making them stronger and much more dangerous. In basic shape and form they appear similar to their ancestors, but other characteristics reveal the creatures’ altered nature. Their fur and skin are much paler, often _[[spells/Shades|shades]]_ of blue, _[[monsters/Gray|gray]]_, or simply white, and it is not uncommon for parts of these creatures to be cloaked in frost, especially their jagged claws and shaggy hair.
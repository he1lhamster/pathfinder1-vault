﻿---
cssclass: [monsters]
title1: Thessalhydra
desc_short: This four-legged reptile has eight serpentine heads arrayed arounda central
  maw. Its long, thrashing tail ends in a crab-like pincer.
title2: Thessalhydra
CR: 18
sources:
- name: Bestiary 6
  page: 263
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 153600
alignment: N
size: Gargantuan
type: aberration
initiative:
  bonus: 15
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 33
  touch: 21
  flat_footed: 18
  components:
    dex: 15
    natural: 12
    size: -4
HP:
  HP: 310
  long: 20d8+220
  fast_healing: 15
saves:
  fort: 17
  ref: 21
  will: 19
defensive_abilities:
- all-around vision
immunities:
- acid
speeds:
  base: 40
  swim: 20
attacks:
  melee:
  - - text: bite +27 (3d6+10/19-20 plus 2d6 acid)
      entries:
      - - damage: 3d6+10
          crit_range: 19-20
        - damage: 2d6
          type: acid
      attack: bite
      bonus:
      - 27
    - text: 8 snake bites +25(1d8+5/19-20 plus 1d6 acid)
      entries:
      - - damage: 1d8+5
          crit_range: 19-20
        - damage: 1d6
          type: acid
      count: 8
      attack: snake bites
      bonus:
      - 25
    - text: pincer +24 (2d8+5 plus grab)
      entries:
      - - damage: 2d8+5
        - effect: grab
      attack: pincer
      bonus:
      - 24
  ranged:
  - - text: 8 acid spits +26 touch (2d6 acid)
      entries:
      - - damage: 2d6
          type: acid
      count: 8
      attack: acid spits
      bonus:
      - 26
      touch: true
  special:
  - breath weapon (160-ft. line, 20d6 acid damage,Reflex DC 31 half, usable every
    1d4rounds)
  - constrict (2d6+10)
  - pounce
space: 20
reach: 20
reach_other: 30 ft. with snake bites, 40 ft. with pincer
ability_scores:
  STR: 31
  DEX: 40
  CON: 32
  INT: 2
  WIS: 24
  CHA: 9
BAB: 15
CMB: 29
CMD: 54
CMD_other: 58 vs. trip
feats:
- name: Bleeding Critical
- name: Combat Reflexes
- name: CriticalFocus
- name: Improved Critical (bite)
- name: Improved Critical (snake bites)
- name: Multiattack
- name: Skill Focus (Perception)
- name: Weapon Finesse
- name: Weapon Focus (bite)
- name: Weapon Focus (snake bites)
skills:
  Perception: 31
  Swim: 26
ecology:
  environment: temperate swamps
  organization: solitary
  treasure_type: incidental
special_abilities:
  Acid Spit (Su): As a standard action, a thessalhydra can spit acid from its eight
    snake mouths, making eight ranged touch attacks at any number of targets within
    a range of 120 feet. On a hit, an acid spit deals 2d6 points of acid damage. A
    creature hit by multiple acid spits from a single thessalhydra in 1 round takes
    the damage as if from one source for the purposes of applying acid resistance.
    For example, a creature hit by eight acid spits would take 16d6 points of acid
    damage, not 2d6 points of acid damage eight times. A creature critically hit by
    acid spit must succeed at a DC 31 Reflex save to avoid being blinded for 1 round
    by the acid. The save DC is Constitution-based.
  Snake Bite (Ex): A thessalhydra's serpent heads strike as secondary attacks that
    deal piercing and slashing damage plus an additional 1d6 points of acid damage.
desc_long: |-
  The dreaded thessalhydra is a fearsome predator that has an unexpected agility. Despite its lumbering shape and looming size, the monster's nimbleness makes it almost beautiful as it attacks. Thessalhydras are relatively rare, though their notorious speed and savagery have featured in countless legends. They are often whispered of in fear and awe by willful children in rural areas, whose exasperated parents have warned them to “be good, or the thessalhydra will pluck you out of your bed through the window when you sleep!” 

  A thessalhydra is 40 feet long, with its pincer-tipped tail adding another 30 feet to its overall length.

---

# Thessalhydra
This four-legged reptile has eight serpentine heads arrayed around

a central maw. Its long, thrashing tail ends in a crab-like pincer.
**Source** Bestiary 6 pg. 263
**XP** 153,600

N Gargantuan aberration
**Init** +15; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_;

Perception +31

##### Defense

**AC** 33, touch 21, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+15 Dex, +12 natural, –4 size)
**hp** 310 (20d8+220); _[[universal monster rules/Fast Healing|fast healing]]_ 15
**Fort** +17, **Ref** +21, **Will** +19
**Defensive Abilities** _[[universal monster rules/All-Around Vision|all-around vision]]_; **Immune** acid

##### Offense
**Speed** 40 ft., swim 20 ft.
**Melee** bite +27 (3d6+10/19–20 plus 2d6 acid), 8 snake bites +25

(1d8+5/19–20 plus 1d6 acid), pincer +24 (2d8+5 plus _[[universal monster rules/Grab|grab]]_)
**Ranged** 8 acid spits +26 touch (2d6 acid)
**Space** 20 ft., **Reach** 20 ft. (30 ft. with snake bites, 40 ft. with pincer)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (160-ft. line, 20d6 acid damage,

Reflex DC 31 half, usable every 1d4

rounds), _[[universal monster rules/Constrict|constrict]]_ (2d6+10), _[[universal monster rules/Pounce|pounce]]_

##### Statistics
**Str** 31, **Dex** 40, **Con** 32, **Int** 2, **Wis** 24, **Cha** 9
**Base Atk** +15; **CMB** +29; **CMD** 54 (58 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, Critical

Focus, _[[feats/Improved Critical|Improved Critical]]_ (bite, snake bites), _[[feats/Multiattack|Multiattack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite), _Weapon Focus_ (snake bites)
**Skills** Perception +31, Swim +26

##### Ecology

**Environment** temperate swamps
**Organization** solitary
**Treasure** incidental

### Special Abilities

**Acid Spit (Su)** As a standard action, a _[[monsters/Thessalhydra|thessalhydra]]_ can spit acid from its eight snake mouths, making eight ranged touch attacks at any number of targets within a range of 120 feet. On a hit, an acid spit deals 2d6 points of acid damage. A creature hit by multiple acid spits from a single _thessalhydra_ in 1 round takes the damage as if from one source for the purposes of applying acid _[[universal monster rules/Resistance|resistance]]_. For example, a creature hit by eight acid spits would take 16d6 points of acid damage, not 2d6 points of acid damage eight times. A creature critically hit by acid spit must succeed at a DC 31 Reflex save to avoid being _[[conditions/Blinded|blinded]]_ for 1 round by the acid. The save DC is Constitution-based.
**Snake Bite (Ex)** A _thessalhydra_’s serpent heads strike as secondary attacks that deal piercing and slashing damage plus an additional 1d6 points of acid damage.

##### Description

The dreaded _thessalhydra_ is a fearsome predator that has an unexpected agility. Despite its lumbering shape and looming size, the monster’s nimbleness makes it almost beautiful as it attacks. Thessalhydras are relatively rare, though their notorious speed and savagery have featured in countless legends. They are often whispered of in _[[universal monster rules/Fear|fear]]_ and awe by willful children in rural areas, whose exasperated parents have warned them to “be good, or the _thessalhydra_ will pluck you out of your bed through the window when you sleep!”

A _thessalhydra_ is 40 feet long, with its pincer-tipped tail adding another 30 feet to its overall length.
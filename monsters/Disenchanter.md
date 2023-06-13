---
cssclass: [monsters]
title1: Disenchanter
desc_short: This blue-furred creature sports a short trunk and a camel-like body.
  The air around it seems to shimmer with magical energy.
title2: Disenchanter
CR: 3
sources:
- name: Bestiary 3
  page: 81
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
- name: Misfit Monsters Redeemed
  page: 27
  link: http://paizo.com/store/downloads/pathfinder/pathfinderChronicles/pathfinderRPG/v5748btpy8gnj
XP: 800
alignment: N
size: Large
type: magical beast
initiative:
  bonus: 3
senses:
  darkvision: 60
  detect magic: true
  low-light vision: true
AC:
  AC: 15
  touch: 12
  flat_footed: 12
  components:
    dex: 3
    natural: 3
    size: -1
HP:
  HP: 30
  long: 4d10+8
saves:
  fort: 6
  ref: 7
  will: 4
DR:
- amount: 5
  weakness: magic
weaknesses:
- vulnerable to dispel magic
speeds:
  base: 50
attacks:
  melee:
  - - text: trunk +7 touch (disenchant)
      entries:
      - - effect: disenchant
      attack: trunk
      bonus:
      - 7
      touch: true
    - text: 2 hooves +2 (1d6+2)
      entries:
      - - damage: 1d6+2
      count: 2
      attack: hooves
      bonus:
      - 2
  special:
  - power spray
space: 10
reach: 5
reach_other: 10 ft. with trunk
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: magic weapon
    source: default
    freq: 3/day
  - name: dimension door
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 4
    concentration: 3
ability_scores:
  STR: 19
  DEX: 17
  CON: 14
  INT: 5
  WIS: 12
  CHA: 8
BAB: 4
CMB: 9
CMD: 22
CMD_other: 26 vs. trip
feats:
- name: Iron Will
- name: Skill Focus (Perception)
skills:
  Escape Artist: 5
  Perception: 9
languages:
- none
ecology:
  environment: warm land
  organization: solitary, pair, or family (2 adults and 1-2 calves with the young
    creature template)
  treasure_type: none
special_abilities:
  Disenchant (Ex): A disenchanter can use its trunk to make a melee touch attack against
    a target's worn, held, or carried magic item in an attempt to drink the item's
    magic. The disenchanter makes a caster level check (+4) opposed by the target's
    Fortitude save. If the check succeeds, the disenchanter drains the item's magic,
    rendering it nonmagical. To determine which of a target's magic items is affected,
    use Table 9-2 on page 216 of the Core Rulebook (though a disenchanter never uses
    this ability on a headband or similar head-slot item unless it has first tried
    to wear the item). Disenchanters may instead target specific visible items, in
    which case they generally target the most obvious items. Artifacts are immune
    to this ability. Disenchant only works against objects that a disenchanter can
    touch, and even a thin layer of cloth effectively protects items from it.
  Power Spray (Su): Once per day, a disenchanter can release a 20-foot cone-shaped
    burst of raw magical energy through its trunk. Creatures in the cone take 4d6
    points of damage (DC 14 Reflex save for half). Creatures immune to magic effects
    that allow spell resistance (such as golems) are immune to this ability. The save
    DC is Constitution-based.
  Vulnerable to Dispel Magic (Ex): A disenchanter targeted by dispel magic takes 1d6
    points of damage per caster level (maximum 10d6, Fortitude save for half). Greater
    dispel magic functions similarly (maximum 20d6 damage, Fortitude save for half).
desc_long: A disenchanter is a blue-furred creature that resembles a single-humped
  camel with a prehensile trunk. The creatures can sense magic, which they consume
  for sustenance, draining the power of magic items and storing their magical energy
  in their humps. Disenchanters are social creatures, and often seek the companionship
  of other intelligent beings, making excellent mounts and trackers for treasure hunters.
  A typical disenchanter is 8 feet long and weighs 1,600 pounds.

---

# Disenchanter
This blue-furred creature sports a short trunk and a camel-like body. The air around it seems to shimmer with magical energy.
**Source** Bestiary 3 pg. 81, Misfit Monsters _[[items/Weapon Magic Abilities/Redeemed|Redeemed]]_ pg. 27
**XP** 800

N Large magical beast
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +9

##### Defense

**AC** 15, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+3 Dex, +3 natural, –1 size)
**hp** 30 (4d10+8)
**Fort** +6, **Ref** +7, **Will** +4
**DR** 5/magic
**Weaknesses** vulnerable to _[[spells/Dispel Magic|dispel magic]]_

##### Offense
**Speed** 50 ft.
**Melee** trunk +7 touch (disenchant), 2 hooves +2 (1d6+2)
**Space** 10 ft., **Reach** 5 ft. (10 ft. with trunk)
**Special Attacks** power spray
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +3)
Constant—_detect magic_
3/day—_[[spells/Magic Weapon|magic weapon]]_
1/day—_[[spells/Dimension Door|dimension door]]_

##### Statistics
**Str** 19, **Dex** 17, **Con** 14, **Int** 5, **Wis** 12, **Cha** 8
**Base Atk** +4; **CMB** +9; **CMD** 22 (26 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Iron Will|Iron Will]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** Escape Artist +5, Perception +9
**Languages** none

##### Ecology

**Environment** warm land
**Organization** solitary, pair, or family (2 adults and 1–2 calves with the young creature template)
**Treasure** none

### Special Abilities

**Disenchant (Ex)** A _[[monsters/Disenchanter|disenchanter]]_ can use its trunk to make a melee touch attack against a target’s worn, held, or carried magic item in an attempt to drink the item’s magic. The _disenchanter_ makes a caster level check (+4) opposed by the target’s Fortitude save. If the check succeeds, the _disenchanter_ drains the item’s magic, rendering it nonmagical. To determine which of a target’s magic items is affected, use Table 9–2 on page 216 of the Core Rulebook (though a _disenchanter_ never uses this ability on a headband or similar head-slot item unless it has first tried to wear the item). Disenchanters may instead target specific visible items, in which case they generally target the most obvious items. Artifacts are immune to this ability. Disenchant only works against objects that a _disenchanter_ can touch, and even a thin layer of cloth effectively protects items from it.

**Power Spray (Su)** Once per day, a _disenchanter_ can release a 20-foot cone-shaped burst of raw magical energy through its trunk. Creatures in the cone take 4d6 points of damage (DC 14 Reflex save for half). Creatures immune to magic effects that allow _[[universal monster rules/Spell Resistance|spell resistance]]_ (such as golems) are immune to this ability. The save DC is Constitution-based.

**Vulnerable to _Dispel Magic_ (Ex)** A _disenchanter_ targeted by _dispel magic_ takes 1d6 points of damage per caster level (maximum 10d6, Fortitude save for half). Greater _dispel magic_ functions similarly (maximum 20d6 damage, Fortitude save for half).

##### Description

A _disenchanter_ is a blue-furred creature that resembles a single-humped camel with a _[[items/Weapon Magic Abilities/Prehensile|prehensile]]_ trunk. The creatures can sense magic, which they consume for sustenance, draining the power of magic items and storing their magical energy in their humps. Disenchanters are social creatures, and often seek the companionship of other intelligent beings, making excellent mounts and trackers for treasure hunters. A typical _disenchanter_ is 8 feet long and weighs 1,600 pounds.
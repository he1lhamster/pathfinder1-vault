---
cssclass: [monsters]
title1: Frostfallen Creature, Frostfallen Mammoth
desc_short: This frozen mammoth erupts into movement, its bones armored with plates
  of ice and eyes burning with cold flames.
title2: Frostfallen Mammoth
CR: 10
sources:
- name: 'Pathfinder #51: The Hungry Storm'
  page: 84
  link: http://paizo.com/pathfinder/v5748btpy8kgv
XP: 9600
alignment: NE
size: Huge
type: undead
subtypes:
- cold
initiative:
  bonus: 1
senses:
  darkvision: 60
  lifesense: true
AC:
  AC: 25
  touch: 9
  flat_footed: 26
  components:
    dex: 1
    natural: 16
    size: -2
HP:
  HP: 91
  long: 14d8+28
saves:
  fort: 5
  ref: 5
  will: 9
DR:
- amount: 10
  weakness: bludgeoning
immunities:
- cold
- undead traits
weaknesses:
- vulnerable to fire
speeds:
  base: 40
attacks:
  melee:
  - - text: gore +21 (2d8+13 plus 3d6 cold)
      entries:
      - - damage: 2d8+13
        - damage: 3d6
          type: cold
      attack: gore
      bonus:
      - 21
    - text: slam +21 (2d6+13 plus 3d6 cold)
      entries:
      - - damage: 2d6+13
        - damage: 3d6
          type: cold
      attack: slam
      bonus:
      - 21
  special:
  - cold
space: 15
reach: 15
ability_scores:
  STR: 36
  DEX: 12
  CON:
  INT:
  WIS: 10
  CHA: 12
BAB: 10
CMB: 25
CMD: 36
CMD_other: 40 vs. trip
feats:
- is_bonus: true
  name: Toughness
skills: {}
special_qualities:
- lifesense
ecology:
  environment: any cold land
  organization: solitary, pair, or drove (3-12)
  treasure_type: none
desc_long: Frostfallen creatures are mindless undead infused with icy cold and animated
  by a hatred for all living things. Their bodies radiate a devastating chill that
  cloaks them in patches of ice that act as armor. Frostfallen creatures appear otherwise
  as they did at the time of their reanimation, except for a cold gleam in the eyes.

---

# Frostfallen Creature, Frostfallen Mammoth
This frozen mammoth erupts into movement, its bones armored with plates of ice and eyes _[[items/Weapon Magic Abilities/Burning|burning]]_ with cold flames.
**Source** Pathfinder #51: The Hungry Storm pg. 84
**XP** 9,600

NE Huge undead (cold)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Lifesense|lifesense]]_; Perception +0

##### Defense

**AC** 25, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+1 Dex, +16 natural, –2 size)
**hp** 91 (14d8+28)
**Fort** +5, **Ref** +5, **Will** +9
**DR** 10/bludgeoning; **Immune** cold, _[[universal monster rules/Undead Traits|undead traits]]_
**Weaknesses** vulnerable to fire

##### Offense
**Speed** 40 ft.
**Melee** gore +21 (2d8+13 plus 3d6 cold), slam +21 (2d6+13 plus 3d6 cold)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** cold

##### Statistics
**Str** 36, **Dex** 12, **Con** —, **Int** —, **Wis** 10, **Cha** 12
**Base Atk** +10; **CMB** +25; **CMD** 36 (40 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Toughness|Toughness]]_
**SQ** _lifesense_

##### Ecology

**Environment** any cold land
**Organization** solitary, pair, or drove (3–12)
**Treasure** none

##### Description

Frostfallen creatures are mindless undead infused with icy cold and _[[items/Armor Magic Abilities/Animated|animated]]_ by a hatred for all living things. Their bodies radiate a devastating chill that cloaks them in patches of ice that act as armor. Frostfallen creatures appear otherwise as they did at the time of their reanimation, except for a cold gleam in the eyes.
---
cssclass: [monsters]
title1: Aballonian
desc_short: This insectile construct skitters around on metallic legs, its manipulators
  clacking and glowing eyes searching.
title2: Aballonian
CR: 7
sources:
- name: Distant Worlds
  page: 58
  link: http://paizo.com/products/btpy8qib?Pathfinder-Campaign-Setting-Distant-Worlds
XP: 3200
alignment: N
size: Medium
type: construct
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 20
  touch: 12
  flat_footed: 18
  components:
    dex: 2
    natural: 8
HP:
  HP: 75
  long: 10d10+20
saves:
  fort: 3
  ref: 7
  will: 5
DR:
- amount: 5
  weakness: adamantine
immunities:
- construct traits
weaknesses:
- sunlight dependency
speeds:
  base: 40
  climb: 20
attacks:
  melee:
  - - text: 2 claws +15 (1d8+4/19-20 plus grab)
      entries:
      - - damage: 1d8+4
          crit_range: 19-20
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 15
  ranged:
  - - text: spark +12 touch (2d6 electricity)
      entries:
      - - damage: 2d6
          type: electricity
      attack: spark
      bonus:
      - 12
      touch: true
ability_scores:
  STR: 19
  DEX: 14
  CON:
  INT: 17
  WIS: 10
  CHA: 11
BAB: 10
CMB: 14
CMB_other: +18 grapple
CMD: 26
feats:
- name: Improved Critical (claw)
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
- name: Weapon Focus (claw)
skills:
  Acrobatics: 12
    when jumping: 16
  Climb: 22
  Knowledge (engineering): 13
  Perception: 10
  Stealth: 12
languages:
- Common
- shortwave 100 ft.
special_qualities:
- rebuild
ecology:
  environment: Aballon
  organization: solitary, pair, or network (3-6)
  treasure_type: standard
special_abilities:
  Rebuild (Ex): 'Aballonian machines are capable of improving and adapting their designs.
    Each Aballonian starts out with one of the abilities listed below. For every two
    additional abilities it possesses, its CR increases by +1. Aballonians may also
    add the customizable abilities of animated objects (Pathfinder RPG Bestiary 14,
    Pathfinder Adventure Path #43 80), increasing their CRs by +1 for every 2 Construction
    Points spent in this way. (They are already considered metal.) Aballonians may
    adapt of their own volition, but it takes 1 day to add each additional ability
    beyond the first, and they must also possess the rare materials necessary to make
    such improvements. An ability can only be gained once unless stated otherwise.
    Gain a plasma cutter that deals 1d6 points of fire damage on a melee touch attack.Gain
    advanced treads that increase base speed to 60 feet.Modify chassis to gain a burrow,
    climb, or swim speed of 60 feet. This ability may be taken multiple times. Its
    effects do not stack. Each time it is taken, it applies to a new movement type.Add
    a radar dish that grants blindsight 120 feet.Gain an additional claw or slam melee
    attack (1d6 damage).Lengthen arms to extend reach by 5 feet.Gain the rend special
    attack (2 claws, 1d8+6).Add armor plating to gain a +4 natural armor bonus to
    AC.Harden systems to gain resistance 10 against a single energy type (acid, cold,
    electricity, or fire). This ability may be taken multiple times. Its effects do
    not stack. Each time it is taken, it applies to a new energy type.'
  Shortwave (Ex): An Aballonian can communicate with nearby Aballonians via invisible
    waves. This functions as telepathy 100 ft., but only with other Aballonians. In
    combat, if any allied Aballonians within range can act in a surprise round, all
    of them can.
  Spark (Ex): As a standard action, an Aballonian can launch an arc of electricity
    at a nearby creature. This attack has a range of 20 feet with no range increment.
    In addition, whenever an Aballonian makes a check to maintain a grapple, it can
    use its spark attack against the creature it is grappling as a free action.
  Sunlight Dependency (Ex): Aballonians gain their energy from light. In areas of
    darkness, they gain the sickened condition.
desc_long: Aballonians are intelligent, self-modifying constructs. The stat block
  presented here represents only the most basic type found on Aballon, with much larger
  or smaller variants taking the form of gargantuan excavators, gliding solar-powered
  flyers, ribbonlike serpent creatures, disembodied processor intelligences, or stranger
  designs.

---

# Aballonian
This insectile construct skitters around on metallic legs, its manipulators clacking and glowing eyes searching.
**Source** Distant Worlds pg. 58
**XP** 3,200

N Medium construct
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +10

##### Defense

**AC** 20, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+2 Dex, +8 natural)
**hp** 75 (10d10+20)
**Fort** +3, **Ref** +7, **Will** +5
**DR** 5/adamantine; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_
**Weaknesses** sunlight dependency

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** 2 claws +15 (1d8+4/19–20 plus _[[universal monster rules/Grab|grab]]_)
**Ranged** _[[spells/Spark|spark]]_ +12 touch (2d6 electricity)

##### Statistics
**Str** 19, **Dex** 14, **Con** —, **Int** 17, **Wis** 10, **Cha** 11
**Base Atk** +10; **CMB** +14 (+18 grapple); **CMD** 26
**Feats** _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Acrobatics +12 (+16 when jumping), _Climb_ +22, Knowledge (engineering) +13, Perception +10, Stealth +12
**Languages** Common; shortwave 100 ft.
**SQ** rebuild

##### Ecology

**Environment** Aballon
**Organization** solitary, pair, or network (3–6)
**Treasure** standard

### Special Abilities

**Rebuild (Ex) **_[[monsters/Aballonian|Aballonian]]_ machines are capable of improving and adapting their designs. Each _Aballonian_ starts out with one of the abilities listed below. For every two additional abilities it possesses, its CR increases by +1. Aballonians may also add the customizable abilities of _[[items/Armor Magic Abilities/Animated|animated]]_ objects (Pathfinder RPG Bestiary 14, Pathfinder Adventure Path #43 80), increasing their CRs by +1 for every 2 Construction Points spent in this way. (They are already considered metal.) Aballonians may adapt of their own volition, but it takes 1 day to add each additional ability beyond the first, and they must also possess the rare materials necessary to make such improvements. An ability can only be gained once unless stated otherwise.

* Gain a plasma cutter that deals 1d6 points of fire damage on a melee touch attack.
* Gain advanced treads that increase base speed to 60 feet.
* Modify chassis to gain a _[[universal monster rules/Burrow|burrow]]_, _climb_, or swim speed of 60 feet. This ability may be taken multiple times. Its effects do not stack. Each time it is taken, it applies to a new movement type.
* Add a radar dish that grants _[[universal monster rules/Blindsight|blindsight]]_ 120 feet.
* Gain an additional claw or slam melee attack (1d6 damage).
* Lengthen arms to extend reach by 5 feet.
* Gain the _[[universal monster rules/Rend|rend]]_ special attack (2 claws, 1d8+6).
* Add armor plating to gain a +4 natural armor bonus to AC.
* Harden systems to gain _[[universal monster rules/Resistance|resistance]]_ 10 against a single energy type (acid, cold, electricity, or fire). This ability may be taken multiple times. Its effects do not stack. Each time it is taken, it applies to a new energy type.
**Shortwave (Ex) **An _Aballonian_ can communicate with nearby Aballonians via _[[conditions/Invisible|invisible]]_ waves. This functions as _[[universal monster rules/Telepathy|telepathy]]_ 100 ft., but only with other Aballonians. In combat, if any allied Aballonians within range can act in a surprise round, all of them can.
**_Spark_ (Ex)** As a standard action, an _Aballonian_ can launch an arc of electricity at a nearby creature. This attack has a range of 20 feet with no range increment. In addition, whenever an _Aballonian_ makes a check to maintain a grapple, it can use its _spark_ attack against the creature it is grappling as a free action.
**Sunlight Dependency (Ex)** Aballonians gain their energy from light. In areas of _[[spells/Darkness|darkness]]_, they gain the _[[conditions/Sickened|sickened]]_ condition.

##### Description

Aballonians are intelligent, self-modifying constructs. The stat block presented here represents only the most basic type found on Aballon, with much larger or smaller variants taking the form of gargantuan excavators, gliding solar-powered flyers, ribbonlike serpent creatures, disembodied processor intelligences, or stranger designs.
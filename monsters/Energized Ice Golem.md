---
cssclass: [monsters]
title1: Energized Ice Golem
desc_short: This construct is covered in rime, with razor-sharp shards of ice protruding
  from its limbs and caustic green fumes emanating from the surface of its frigid
  body.
title2: Energized Ice Golem
CR: 7
sources:
- name: Construct Handbook
  page: 38
  link: https://paizo.com/products/btq01vam
XP: 3200
alignment: N
size: Medium
type: construct
subtypes:
- cold
initiative:
  bonus: 0
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: caustic mist
  radius: 5
  other:
  - 1d6 acid plus poison
  DC: 13
AC:
  AC: 21
  touch: 10
  flat_footed: 21
  components:
    natural: 11
HP:
  HP: 73
  long: 6d10+40
saves:
  fort: 2
  ref: 2
  will: 2
DR:
- amount: 5
  weakness: adamantine
immunities:
- cold
- construct traits
- magic
weaknesses:
- vulnerable to fire
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 slams +11 (1d6+5 plus 1d6 acid plus 1d6 cold)
      entries:
      - - damage: 1d6+5
        - damage: 1d6
          type: acid
        - damage: 1d6
          type: cold
      count: 2
      attack: slams
      bonus:
      - 11
  ranged:
  - - text: breath weapon (20-ft. cone, 3d6 cold damage, Reflex DC 13 half, usable
        every 1d4 rounds)
      entries:
      - - damage: '20'
          type: -ft. cone
        - damage: 3d6
          type: cold damage
        - effect: Reflex DC 13 half
        - effect: usable every 1d4 rounds
      attack: breath weapon
    - text: energy discharge (20-ft. burst, 3d8 acid)
      entries:
      - - damage: '20'
          type: -ft. burst
        - damage: 3d8
          type: acid
      attack: energy discharge
ability_scores:
  STR: 20
  DEX: 11
  CON:
  INT:
  WIS: 11
  CHA: 1
BAB: 6
CMB: 11
CMD: 21
skills: {}
special_qualities:
- elemental overcharge
ecology:
  environment: any
  organization: solitary or gang (2-4)
  treasure_type: none
desc_long: |-
  Most golems are animated by an elemental spirit bound within a constructed body, but some creators build their golems with a greater purpose in mind. An energized golem is infused with the raw elemental energy of the elemental spirit used to animate it, granting it increased strength and agility and a host of supernatural powers.

   The sample energized golem presented here is built using an ice golem as the base creature. See that entry for full descriptions of its base abilities.

---

# Energized Ice Golem
This construct is covered in rime, with razor-sharp shards of ice protruding from its limbs and caustic green fumes emanating from the surface of its frigid body.
**Source** Construct Handbook pg. 38
**XP** 3,200

N Medium construct (cold)
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +0
**Aura** caustic mist (5 ft., 1d6 acid plus poison, DC 13)

##### Defense

**AC** 21, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+11 natural)
**hp** 73 (6d10+40)
**Fort** +2, **Ref** +2, **Will** +2
**DR** 5/adamantine; **Immune** cold, _[[universal monster rules/Construct Traits|construct traits]]_, magic
**Weaknesses** vulnerable to fire

##### Offense
**Speed** 30 ft.
**Melee** 2 slams +11 (1d6+5 plus 1d6 acid plus 1d6 cold)
**Ranged** _[[universal monster rules/Breath Weapon|breath weapon]]_ (20-ft. cone, 3d6 cold damage, Reflex DC 13 half, usable every 1d4 rounds), energy _[[spells/Discharge|discharge]]_ (20-ft. burst, 3d8 acid)

##### Statistics
**Str** 20, **Dex** 11, **Con** —, **Int** —, **Wis** 11, **Cha** 1
**Base Atk** +6; **CMB** +11; **CMD** 21
**SQ** elemental overcharge

##### Ecology

**Environment** any
**Organization** solitary or gang (2-4)
**Treasure** none

##### Description

Most golems are _[[items/Armor Magic Abilities/Animated|animated]]_ by an elemental spirit bound within a constructed body, but some creators build their golems with a greater purpose in mind. An energized golem is infused with the raw elemental energy of the elemental spirit used to animate it, granting it increased strength and agility and a host of supernatural powers.

The sample energized golem presented here is built using an ice golem as the base creature. See that entry for full descriptions of its base abilities.
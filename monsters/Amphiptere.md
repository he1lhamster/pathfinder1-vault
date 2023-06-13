---
cssclass: [monsters]
title1: Amphiptere
desc_short: This snake-bodied dragon has a sinuous tail with a spiked tip. Flared
  wings attach to its forelimbs, and it lacks rear legs.
title2: Amphiptere
CR: 4
sources:
- name: Bestiary 5
  page: 18
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 1200
alignment: N
size: Large
type: dragon
initiative:
  bonus: 4
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 16
  touch: 9
  flat_footed: 16
  components:
    natural: 7
    size: -1
HP:
  HP: 42
  long: 5d12+10
saves:
  fort: 6
  ref: 4
  will: 5
immunities:
- paralysis
- sleep
speeds:
  base: 10
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: tail +9 (1d8+4)
      entries:
      - - damage: 1d8+4
      attack: tail
      bonus:
      - 9
    - text: bite +8 (1d10+4 plus grab)
      entries:
      - - damage: 1d10+4
        - effect: grab
      attack: bite
      bonus:
      - 8
    - text: 2 wings +3 (1d4+2)
      entries:
      - - damage: 1d4+2
      count: 2
      attack: wings
      bonus:
      - 3
  special:
  - constrict (1d10+4)
  - impale
space: 10
reach: 5
reach_other: 10 ft. with tail
ability_scores:
  STR: 18
  DEX: 11
  CON: 14
  INT: 7
  WIS: 12
  CHA: 9
BAB: 5
CMB: 10
CMD: 20
CMD_other: can't be tripped
feats:
- name: Flyby Attack
- name: Improved Initiative
- name: Weapon Focus (tail)
skills:
  Fly: 10
  Perception: 13
  Sense Motive: 9
  Stealth: 4
  _racial_mods:
    Fly:
      _: 4
    Perception:
      _: 4
languages:
- Draconic
special_qualities:
- limited flight
ecology:
  environment: temperate or warm deserts, hills, or mountains
  organization: solitary, pair, or flight (3-18)
  treasure_type: standard
special_abilities:
  Impale (Ex): If an amphiptere confirms a critical hit with its tail attack against
    a creature smaller than itself, the spike-tipped tail impales the target creature.
    An impaled creature gains the pinned condition (though the amphiptere doesn't
    gain the grappled condition), takes 1d6 points of bleed damage, and automatically
    takes damage from the amphiptere's tail each round it remains pinned. An amphiptere
    can't constrict a creature it has impaled, nor can it use its tail attack while
    it is impaling a creature, but it doesn't need to succeed at a grapple combat
    maneuver check to maintain the grapple. An amphiptere can release an impaled creature
    as a free action.
  Limited Flight (Ex): Though amphipteres have wings, they can't truly fly. Amphipteres
    usually move by lifting themselves a few feet off the ground with their great
    batlike wings and pulling themselves along the ground with their claws. This tactic
    provides an amphiptere a fly speed of 60 feet and average maneuverability, though
    they can't lift themselves higher than 10 feet off the ground and can't use their
    wings to hover. Additionally, amphipteres can attempt a DC 15 Fly check to fall
    safely from any height without taking falling damage, as if under the effects
    of feather fall. When falling safely, an amphiptere can attempt an additional
    DC 15 Fly check to glide, allowing it to move 5 feet laterally for every 10 feet
    it falls.
desc_long: |-
  Distantly related to wyverns, amphipteres are equally cruel and prone to violence. Like wyverns, they have serpentine bodies and bat-like wings. Unlike wyverns, however, amphipteres must use the long claws on the tips of their wings to propel their bodies along as they awkwardly leap and soar a few feet off the ground. They're also longer and much leaner than wyverns, and instead of a wyvern's poisonous stinger, an amphiptere has a broad, arrow-shaped spur at the end of its long tail. Capable of piercing armor and shattering bone, an amphiptere's tail skewers prey much like a fisher might spear a fish.

  Amphipteres average 18 feet in length, though most of this length is the tail, and they weigh around 1,600 pounds.

---

# Amphiptere
This snake-bodied dragon has a sinuous tail with a spiked tip. Flared wings _[[universal monster rules/Attach|attach]]_ to its forelimbs, and it lacks rear legs.
**Source** Bestiary 5 pg. 18
**XP** 1,200

N Large dragon
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +13

##### Defense

**AC** 16, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+7 natural, -1 size)
**hp** 42 (5d12+10)
**Fort** +6, **Ref** +4, **Will** +5
**Immune** _[[universal monster rules/Paralysis|paralysis]]_, sleep

##### Offense
**Speed** 10 ft., fly 60 ft. (average)
**Melee** tail +9 (1d8+4), bite +8 (1d10+4 plus _[[universal monster rules/Grab|grab]]_), 2 wings +3 (1d4+2)
**Space** 10 ft., **Reach** 5 ft. (10 ft. with tail)
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (1d10+4), impale

##### Statistics
**Str** 18, **Dex** 11, **Con** 14, **Int** 7, **Wis** 12, **Cha** 9
**Base Atk** +5; **CMB** +10; **CMD** 20 (can’t be tripped)
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (tail)
**Skills** Fly +10, Perception +13, Sense Motive +9, Stealth +4; **Racial Modifiers** +4 Fly, +4 Perception
**Languages** Draconic
**SQ** limited _[[universal monster rules/Flight|flight]]_

##### Ecology

**Environment** temperate or warm deserts, hills, or mountains
**Organization** solitary, pair, or _flight_ (3-18)
**Treasure** standard

### Special Abilities

**Impale (Ex)** If an _[[monsters/Amphiptere|amphiptere]]_ confirms a critical hit with its tail attack against a creature smaller than itself, the spike-tipped tail impales the target creature. An impaled creature gains the _[[conditions/Pinned|pinned]]_ condition (though the _amphiptere_ doesn’t gain the _[[conditions/Grappled|grappled]]_ condition), takes 1d6 points of _[[universal monster rules/Bleed|bleed]]_ damage, and automatically takes damage from the _amphiptere_’s tail each round it remains _pinned_. An _amphiptere_ can’t _constrict_ a creature it has impaled, nor can it use its tail attack while it is impaling a creature, but it doesn’t need to succeed at a grapple combat maneuver check to maintain the grapple. An _amphiptere_ can release an impaled creature as a free action.

**Limited _Flight_ (Ex)** Though amphipteres have wings, they can’t truly fly. Amphipteres usually move by lifting themselves a few feet off the ground with their great batlike wings and pulling themselves along the ground with their claws. This tactic provides an _amphiptere_ a fly speed of 60 feet and average maneuverability, though they can’t lift themselves higher than 10 feet off the ground and can’t use their wings to _[[feats/Hover|hover]]_. Additionally, amphipteres can attempt a DC 15 Fly check to fall safely from any height without taking falling damage, as if under the effects of _[[spells/Feather Fall|feather fall]]_. When falling safely, an _amphiptere_ can attempt an additional DC 15 Fly check to _[[spells/Glide|glide]]_, allowing it to move 5 feet laterally for every 10 feet it falls.

##### Description

Distantly related to wyverns, amphipteres are equally _[[items/Weapon Magic Abilities/Cruel|cruel]]_ and _[[conditions/Prone|prone]]_ to violence. Like wyverns, they have serpentine bodies and bat-like wings. Unlike wyverns, however, amphipteres must use the long claws on the tips of their wings to propel their bodies along as they awkwardly leap and soar a few feet off the ground. They’re also longer and much leaner than wyverns, and instead of a _[[monsters/Wyvern|wyvern]]_’s poisonous stinger, an _amphiptere_ has a broad, arrow-shaped spur at the end of its long tail. Capable of piercing armor and _[[items/Weapon Magic Abilities/Shattering|shattering]]_ bone, an _amphiptere_’s tail skewers prey much like a fisher might _[[items/Weapon/Spear|spear]]_ a fish.

Amphipteres average 18 feet in length, though most of this length is the tail, and they weigh around 1,600 pounds.
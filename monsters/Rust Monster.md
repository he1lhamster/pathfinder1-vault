---
cssclass: [monsters]
title1: Rust Monster
desc_short: This insectile monster has four legs, a strange propeller-shaped protrusion
  at the end of its tail, and two long, feathery antennae.
title2: Rust Monster
CR: 3
sources:
- name: Pathfinder RPG Bestiary
  page: 238
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 800
alignment: N
size: Medium
type: aberration
initiative:
  bonus: 3
senses:
  darkvision: 60
  scent metals: 90
AC:
  AC: 18
  touch: 13
  flat_footed: 15
  components:
    dex: 3
    natural: 5
HP:
  HP: 27
  long: 5d8+5
saves:
  fort: 2
  ref: 4
  will: 5
speeds:
  base: 40
  climb: 10
attacks:
  melee:
  - - text: bite +6 (1d3)
      entries:
      - - damage: 1d3
      attack: bite
      bonus:
      - 6
    - text: antennae +6 touch (rust)
      entries:
      - - effect: rust
      attack: antennae
      bonus:
      - 6
      touch: true
ability_scores:
  STR: 10
  DEX: 17
  CON: 13
  INT: 2
  WIS: 13
  CHA: 8
BAB: 3
CMB: 3
CMD: 16
CMD_other: 20 vs. trip
feats:
- name: Ability Focus (rust)
- name: Skill Focus (Perception)
- name: Weapon Finesse
skills:
  Climb: 8
  Perception: 12
ecology:
  environment: any underground
  organization: solitary, pair, or nest (3-10)
  treasure_type: incidental
  treasure:
  - no metal treasure
special_abilities:
  Rust (Su): A rust monster's antennae are a primary touch attack that causes any
    metal object they touch to swiftly rust and corrode. The object touched takes
    half its maximum hp in damage and gains the broken condition-a second hit destroys
    the item. A rust monster never provokes attacks of opportunity by attempting to
    strike a weapon with its antennae. Against creatures made of metal, a rust monster's
    antennae deal 3d6+5 points of damage. An attended object, any magic object, or
    a metal creature can attempt a DC 15 Reflex save to negate this effect. The save
    DC is Constitution-based.
  Scent Metals (Ex): This ability functions much the same as the scent ability, except
    that the range is 90 feet and the rust monster can only use it to sense metal
    objects (including creatures wearing or carrying metal objects).
desc_long: |-
  Of all the terrifying beasts an explorer might encounter underground, only the rust monster targets that which the average adventurer values most: his treasure.

  Typically 5 feet long and weighing almost 200 pounds, the lobster-like rust monster would be frightening enough even without the alien feeding process that gives it its name. Rust monsters consume metal objects, preferring iron and ferrous alloys like steel but devouring even mithral, adamantine, and enchanted metals with equal ease. Any metal touched by the rust monster's delicate antennae or armored hide corrodes and falls to dust within seconds, making the beast a major threat to subterranean adventurers and those dwarven miners who must defend their forges and compete for ore.

  Though rust monsters have no innate tendency toward violence, their insatiable hunger leads them to charge anything they come across that bears even trace amounts of metal, and any resistance is met with unthinking savagery. It's not unheard of for rust monsters in metal-poor areas to track escaped victims for days using their scent metal ability, provided the victims retain intact metal objects. Fortunately, it's often possible to escape a rust monster's attentions by throwing it a dense metal object like a shield and running in the opposite direction. Those who frequent areas infested with rust monsters quickly learn to keep a few stone or wooden weapons close at hand.

---

# Rust Monster
This insectile monster has four legs, a strange propeller-shaped protrusion at the end of its tail, and two long, feathery antennae.
**Source** Pathfinder RPG Bestiary pg. 238
**XP** 800

N Medium aberration
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_ metals 90 ft.; Perception +12

##### Defense

**AC** 18, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+3 Dex, +5 natural)
**hp** 27 (5d8+5)
**Fort** +2, **Ref** +4, **Will** +5

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 10 ft.
**Melee** bite +6 (1d3), antennae +6 touch (rust)

##### Statistics
**Str** 10, **Dex** 17, **Con** 13, **Int** 2, **Wis** 13, **Cha** 8
**Base Atk** +3; **CMB** +3; **CMD** 16 (20 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (rust), _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** _Climb_ +8, Perception +12

##### Ecology

**Environment** any underground
**Organization** solitary, pair, or nest (3–10)
**Treasure** incidental (no metal treasure)

### Special Abilities

**Rust (Su)** A _[[monsters/Rust Monster|rust monster]]_’s antennae are a primary touch attack that causes any metal object they touch to swiftly rust and corrode. The object touched takes half its maximum hp in damage and gains the _[[conditions/Broken|broken]]_ condition—a second hit destroys the item. A _rust monster_ never provokes attacks of opportunity by attempting to strike a weapon with its antennae. Against creatures made of metal, a _rust monster_’s antennae deal 3d6+5 points of damage. An attended object, any magic object, or a metal creature can attempt a DC 15 Reflex save to negate this effect. The save DC is Constitution-based.
**_Scent_ Metals (Ex)** This ability functions much the same as the _scent_ ability, except that the range is 90 feet and the _rust monster_ can only use it to sense metal objects (including creatures wearing or carrying metal objects).

##### Description

Of all the terrifying beasts an _[[feats/Explorer|explorer]]_ might encounter underground, only the _rust monster_ targets that which the average adventurer values most: his treasure.

Typically 5 feet long and weighing almost 200 pounds, the lobster-like _rust monster_ would be frightening enough even without the alien feeding process that gives it its name. Rust monsters consume metal objects, preferring iron and ferrous alloys like steel but devouring even mithral, adamantine, and enchanted metals with equal ease. Any metal touched by the _rust monster_’s delicate antennae or armored hide corrodes and falls to dust within seconds, making the beast a major threat to subterranean adventurers and those dwarven miners who must defend their forges and compete for ore.

Though rust monsters have no innate tendency toward violence, their insatiable hunger leads them to charge anything they come across that bears even trace amounts of metal, and any _[[universal monster rules/Resistance|resistance]]_ is met with unthinking savagery. It’s not unheard of for rust monsters in metal-poor areas to track escaped victims for days using their _scent_ metal ability, provided the victims retain intact metal objects. Fortunately, it’s often possible to escape a _rust monster_’s attentions by _[[items/Weapon Magic Abilities/Throwing|throwing]]_ it a dense metal object like a _[[spells/Shield|shield]]_ and running in the opposite direction. Those who frequent areas infested with rust monsters quickly learn to keep a few stone or wooden weapons close at hand.
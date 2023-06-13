---
cssclass: [monsters]
title1: Lizard, Giant Chameleon
desc_short: Nearly invisible in its surroundings, this scaly lizard's eyes dart about
  independently of each other.
title2: Giant Chameleon
CR: 3
sources:
- name: Bestiary 3
  page: 186
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 800
alignment: N
size: Large
type: animal
initiative:
  bonus: 6
senses:
  low-light vision: true
AC:
  AC: 14
  touch: 11
  flat_footed: 12
  components:
    dex: 2
    natural: 3
    size: -1
HP:
  HP: 34
  long: 4d8+16
saves:
  fort: 8
  ref: 6
  will: 1
speeds:
  base: 40
  climb: 40
attacks:
  melee:
  - - text: bite +5 (2d6+4)
      entries:
      - - damage: 2d6+4
      attack: bite
      bonus:
      - 5
  - - text: tongue +5 touch (grab)
      entries:
      - - effect: grab
      attack: tongue
      bonus:
      - 5
      touch: true
  special:
  - tongue
  - pull (tongue, 5 ft.)
space: 10
reach: 10
reach_other: 15 ft. with tongue
ability_scores:
  STR: 16
  DEX: 15
  CON: 18
  INT: 2
  WIS: 11
  CHA: 7
BAB: 3
CMB: 7
CMB_other: +11 grapple
CMD: 19
CMD_other: 23 vs. trip
feats:
- name: Improved Initiative
- name: Skill Focus (Stealth)
skills:
  Climb: 15
  Perception: 4
  Stealth: 18
    when still: 28
  _racial_mods:
    Stealth:
      _: 12
      when still: 22
ecology:
  environment: warm forests and mountains
  organization: solitary, pair, or blend (3-6)
  treasure_type: none
special_abilities:
  Tongue (Ex): A giant chameleon can grab a foe with its tongue and draw the victim
    to its mouth. This tongue attack has a reach of 15 feet. The attack does no damage,
    but allows the creature to grab. A giant chameleon does not gain the grappled
    condition while using its tongue in this manner.
desc_long: These large lizards have the ability to shift the pigments in their skin
  to match their surroundings. A giant chameleon is typically 11 feet long and weighs
  160 pounds.

---

# Lizard, Giant Chameleon
Nearly _[[conditions/Invisible|invisible]]_ in its surroundings, this scaly lizard’s eyes _[[items/Weapon/Dart|dart]]_ about independently of each other.
**Source** Bestiary 3 pg. 186
**XP** 800

N Large animal
**Init** +6; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +4

##### Defense

**AC** 14, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+2 Dex, +3 natural, –1 size)
**hp** 34 (4d8+16)
**Fort** +8, **Ref** +6, **Will** +1

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 40 ft.
**Melee** bite +5 (2d6+4) or tongue +5 touch (_[[universal monster rules/Grab|grab]]_)
**Space** 10 ft., **Reach** 10 ft. (15 ft. with tongue)
**Special Attacks** tongue, _[[universal monster rules/Pull|pull]]_ (tongue, 5 ft.)

##### Statistics
**Str** 16, **Dex** 15, **Con** 18, **Int** 2, **Wis** 11, **Cha** 7
**Base Atk** +3; **CMB** +7 (+11 grapple); **CMD** 19 (23 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth)
**Skills** _Climb_ +15, Perception +4, Stealth +18 (+28 when still); **Racial Modifiers** +12 Stealth (+22 when still)

##### Ecology

**Environment** warm forests and mountains
**Organization** solitary, pair, or _[[spells/Blend|blend]]_ (3–6)
**Treasure** none

### Special Abilities

**Tongue (Ex)** A giant _[[npcs/Chameleon|chameleon]]_ can _grab_ a foe with its tongue and draw the victim to its mouth. This tongue attack has a reach of 15 feet. The attack does no damage, but allows the creature to _grab_. A giant _chameleon_ does not gain the _[[conditions/Grappled|grappled]]_ condition while using its tongue in this manner.

##### Description

These large lizards have the ability to shift the pigments in their skin to match their surroundings. A giant _chameleon_ is typically 11 feet long and weighs 160 pounds.
---
cssclass: [monsters]
title1: Bog Strider
desc_short: A narrow, beetle-like creature glides across the water's dark surface
  on four brown, spindly legs. It stands just over five feet tall, holding its head
  and thorax upright while clutching an intricately carved hunting spear in two clawed
  forelimbs. Powerful mandibles click in rhythm with the reed-thin antennae waving
  upon its head as if testing the air for the scent of prey.
title2: Bog Strider
CR: 2
sources:
- name: 'Pathfinder #34: Blood for Blood'
  page: 82
  link: http://paizo.com/pathfinder/adventurePath/kingmaker/v5748btpy8b7w
XP: 600
alignment: N
size: Medium
type: monstrous humanoid
initiative:
  bonus: 2
senses:
  darkvision: 60
  tremorsense: 120
  tremorsense_other: in water
AC:
  AC: 16
  touch: 13
  flat_footed: 13
  components:
    dex: 2
    dodge: 1
    natural: 3
HP:
  HP: 15
  long: 2d10+4
saves:
  fort: 2
  ref: 5
  will: 4
speeds:
  base: 30
  water stride: 50
attacks:
  melee:
  - - text: spear +4 (1d8+3/x3)
      entries:
      - - damage: 1d8+3
          crit_multiplier: 3
      attack: spear
      bonus:
      - 4
    - text: bite -1 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: bite
      bonus:
      - -1
  - - text: 2 claws +4 (1d4-2)
      entries:
      - - damage: 1d4-2
      count: 2
      attack: claws
      bonus:
      - 4
    - text: bite +4 (1d6+2)
      entries:
      - - damage: 1d6+2
      attack: bite
      bonus:
      - 4
  ranged:
  - - text: spear +4 (1d8+2/x3)
      entries:
      - - damage: 1d8+2
          crit_multiplier: 3
      attack: spear
      bonus:
      - 4
  - - text: mwk net +5 ranged touch (entangle)
      entries:
      - - effect: entangle
      attack: mwk net
      bonus:
      - 5
      touch: true
ability_scores:
  STR: 14
  DEX: 14
  CON: 14
  INT: 11
  WIS: 13
  CHA: 9
BAB: 2
CMB: 4
CMD: 17
CMD_other: 21 vs. trip
feats:
- name: Dodge
skills:
  Perception: 6
  Stealth: 7
  Survival: 6
  Swim: 11
  _racial_mods:
    Swim:
      _: 4
languages:
- Aquan
- tremor tap 120 ft.
special_qualities:
- hold breath
- water sprint
ecology:
  environment: temperate or warm swamps
  organization: solitary, pair, band (3-12), or tribe (13-60)
  treasure_type: NPC Gear
  treasure:
  - masterwork net
  - spear
  - other treasure
special_abilities:
  Hold Breath (Ex): A bog strider can hold its breath for a number of rounds equal
    to 4 times its Constitution score before it risks drowning.
  Tremor Tap (Ex): Bog striders can send and receive messages by creating and sensing
    silent vibrations on the surface of any body of water they currently tread. The
    range of communication extends outward 120 feet to all other bog striders within
    line of effect on or under the water. Because the ripples created on the water
    prove omni-directional, bog striders can communicate with multiple targets at
    the same time. Only bog striders can understand this form of communication. This
    ability also grants bog striders tremorsense in water at a range of 120 feet.
  Water Sprint (Ex): Once per hour, a bog strider can move up to 5 times its normal
    speed (250 feet) on water when making a charge or retreating from an enemy. Once
    it decides to increase its movement in this fashion, the effect lasts for up to
    4 rounds, after which a bog strider becomes fatigued for as many rounds as it
    chose to move at a higher speed.
  Water Stride (Su): A bog strider can tread upon rivers, lakes, and flooded swamplands
    or marshes as if under the effects of the water walk spell. It also gains an increased
    movement rate by using the surface tension and its multiple legs to propel itself
    across the water.
desc_long: |-
  Bog striders call themselves Ses'h in Aquan, but the first explorers to encounter them named the reclusive bug-men after their ability to stride on water like solid ground. Individual bog striders resemble upright beetles with four legs, two arms, and powerful mandibles. They depend on their waterborne speed to quickly chase down prey and flee from predators. Otherwise, they care little for civilizations other than their own, rarely venturing from the swampy rivers and lakes they call home.

  The long, spindly legs of bog striders give the impression of a greater size then their relatively fragile frames actually account for. Although their limbs are in most cases more than double, even triple, the length of other humanoids, their inflexible joints grant them little more mobility, range of motion, and capability to reach than others. Regardless of gender, nearly all bog striders stand 5 feet tall and weigh approximately 150 pounds.

---

# Bog Strider
A narrow, beetle-like creature glides across the water’s dark surface on four brown, spindly legs. It stands just over five feet tall, holding its head and thorax upright while clutching an intricately carved hunting _[[items/Weapon/Spear|spear]]_ in two clawed forelimbs. Powerful mandibles click in rhythm with the reed-thin antennae waving upon its head as if testing the air for the _[[universal monster rules/Scent|scent]]_ of prey.
**Source** Pathfinder #34: Blood for Blood pg. 82
**XP** 600

N Medium monstrous humanoid
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Tremorsense|tremorsense]]_ 120 ft. (in water); Perception +6

##### Defense

**AC** 16, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+2 Dex, +1 _[[feats/Dodge|dodge]]_, +3 natural)
**hp** 15 (2d10+4)
**Fort** +2, **Ref** +5, **Will** +4

##### Offense
**Speed** 30 ft., water stride 50 ft.
**Melee** _spear_ +4 (1d8+3/x3), bite -1 (1d6+1) or 2 claws +4 (1d4-2), bite +4 (1d6+2)
**Ranged** _spear_ +4 (1d8+2/x3) or mwk _[[items/Mundane/Net|net]]_ +5 ranged touch (_[[spells/Entangle|entangle]]_)

##### Statistics
**Str** 14, **Dex** 14, **Con** 14, **Int** 11, **Wis** 13, **Cha** 9
**Base Atk** +2; **CMB** +4; **CMD** 17 (21 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _Dodge_
**Skills** Perception +6, Stealth +7, Survival +6, Swim +11; **Racial Modifiers** +4 Swim
**Languages** Aquan; tremor tap 120 ft.
**SQ** _[[universal monster rules/Hold Breath|hold breath]]_, water sprint

##### Ecology

**Environment** temperate or warm swamps
**Organization** solitary, pair, band (3-12), or tribe (13-60)
**Treasure** NPC gear (masterwork _net_, _spear_, other treasure)

### Special Abilities

**_Hold Breath_ (Ex)** A _[[monsters/Bog Strider|bog strider]]_ can hold its breath for a number of rounds equal to 4 times its Constitution score before it risks drowning.

**Tremor Tap (Ex)** Bog striders can send and receive messages by creating and _[[items/Armor Magic Abilities/Sensing|sensing]]_ silent vibrations on the surface of any body of water they currently tread. The range of communication extends outward 120 feet to all other bog striders within line of effect on or under the water. Because the ripples created on the water prove omni-directional, bog striders can communicate with multiple targets at the same time. Only bog striders can understand this form of communication. This ability also grants bog striders _tremorsense_ in water at a range of 120 feet.

**Water Sprint (Ex)** Once per hour, a _bog strider_ can move up to 5 times its normal speed (250 feet) on water when making a charge or retreating from an enemy. Once it decides to increase its movement in this fashion, the effect lasts for up to 4 rounds, after which a _bog strider_ becomes _[[conditions/Fatigued|fatigued]]_ for as many rounds as it chose to move at a higher speed.

**Water Stride (Su)** A _bog strider_ can tread upon rivers, lakes, and flooded swamplands or marshes as if under the effects of the _[[spells/Water Walk|water walk]]_ spell. It also gains an increased movement rate by using the surface tension and its multiple legs to propel itself across the water.

##### Description

Bog striders call themselves Ses’h in Aquan, but the first explorers to encounter them named the reclusive bug-men after their ability to stride on water like solid ground. Individual bog striders resemble upright beetles with four legs, two arms, and powerful mandibles. They depend on their waterborne speed to quickly chase down prey and flee from predators. Otherwise, they care little for civilizations other than their own, rarely venturing from the swampy rivers and lakes they call home.

The long, spindly legs of bog striders give the impression of a greater size then their relatively fragile frames actually account for. Although their limbs are in most cases more than double, even triple, the length of other humanoids, their inflexible joints grant them little more _[[feats/Mobility|mobility]]_, range of motion, and capability to reach than others. Regardless of gender, nearly all bog striders stand 5 feet tall and weigh approximately 150 pounds.
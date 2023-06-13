---
cssclass: [monsters]
title1: Thassilonian Sentinel, Ivory Sentinel
desc_short: Sculpted from ivory in the form of a large skull, this construct perches
  on six segmented legs of whitened bone.
title2: Ivory Sentinel
CR: 7
sources:
- name: 'Pathfinder #134: It Came from Hollow Mountain'
  page: 90
  link: http://paizo.com/products/btpy9z14?Pathfinder-Adventure-Path-134-It-Came-from-Hollow-Mountain
XP: 3200
alignment: N
size: Small
type: construct
initiative:
  bonus: 10
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 21
  touch: 17
  flat_footed: 15
  components:
    dex: 6
    natural: 4
    size: 1
HP:
  HP: 75
  long: 10d10+20
saves:
  fort: 3
  ref: 9
  will: 3
immunities:
- construct traits
- electricity
- magic
speeds:
  base: 40
  climb: 20
  fly: 40
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 claws +17 (1d6+5 plus poison)
      entries:
      - - damage: 1d6+5
        - effect: poison
      count: 2
      attack: claws
      bonus:
      - 17
    - text: 2 wings +11 (1d3+2)
      entries:
      - - damage: 1d3+2
      count: 2
      attack: wings
      bonus:
      - 11
  special:
  - disorienting screech
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  sources:
  - name: default
    CL: 2
    concentration: -1
ability_scores:
  STR: 21
  DEX: 23
  CON:
  INT: 1
  WIS: 11
  CHA: 5
BAB: 10
CMB: 14
CMD: 30
CMD_other: 38 vs. trip
feats:
- name: Flyby Attack
- name: Improved Initiative
- name: Skill Focus (Perception)
- name: Toughness
- name: Weapon Focus (claws)
skills:
  Acrobatics: 8
  Climb: 15
  Fly: 17
  Perception: 5
  Stealth: 12
languages:
- Thassilonian (can't speak)
special_qualities:
- alert
- freeze
ecology:
  environment: any
  organization: solitary, pair, or troop (3-7)
  treasure_type: none
special_abilities:
  Alert (Su): An ivory sentinel can take simple orders and identify intruders. This
    functions as the iron sentinel's alert ability).
  Disorienting Screech (Su): Three times per day, an ivory sentinel can emit a disorienting
    screech as a standard action. All living creatures within a 30-foot spread must
    succeed at a DC 15 Will save or become confused (as per the spell confusion) for
    1d4+1 rounds. A creature that succeeds at this saving throw is immune to further
    disorienting screeches from that ivory sentinel for 24 hours. This is a sonic,
    mind-affecting effect. The save is Constitution-based.
  Immunity to Magic (Ex): An ivory sentinel is immune to spells or spell-like abilities
    that allow spell resistance, except for spells with the sonic descriptor.
  Poison (Ex): Claws-injury; save Fort DC 15; frequency 1/round for 6 rounds; effect
    1d3 Con damage; cure 2 consecutive saves. The save DC is Constitution-based.
desc_long: |-
  Ivory sentinels were most often employed by the upper echelons of Thassilonian aristocracy, especially across Bakrakhan and Shalast. These nobles competed with one another in decking out the approaches to their palaces with outlandish and lethal guardians, and the avian ivory sentinels served this purpose well. Often employed to terrorize peasants and foreign dignitaries, most of these constructs were destroyed during Earthfall when those extravagant palaces came tumbling down.

   When an ivory sentinel takes flight, delicate wings carved to resemble those of a bird unfurl from the sides of its skull-like head.

---

# Thassilonian Sentinel, Ivory Sentinel
Sculpted from ivory in the form of a large skull, this construct perches on six segmented legs of whitened bone.
**Source** Pathfinder #134: It Came from Hollow Mountain pg. 90
**XP** 3,200

N Small construct
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +5

##### Defense

**AC** 21, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+6 Dex, +4 natural, +1 size)
**hp** 75 (10d10+20)
**Fort** +3, **Ref** +9, **Will** +3
**Immune** _[[universal monster rules/Construct Traits|construct traits]]_, electricity, magic

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 20 ft., fly 40 ft. (good)
**Melee** 2 claws +17 (1d6+5 plus poison), 2 wings +11 (1d3+2)
**Special Attacks** disorienting _[[spells/Screech|screech]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 2nd; concentration -1)
Constant—_[[spells/Detect Magic|detect magic]]_

##### Statistics
**Str** 21, **Dex** 23, **Con** —, **Int** 1, **Wis** 11, **Cha** 5
**Base Atk** +10; **CMB** +14; **CMD** 30 (38 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claws)
**Skills** Acrobatics +8, _Climb_ +15, Fly +17, Perception +5, Stealth +12
**Languages** Thassilonian (can’t speak)
**SQ** alert, _[[universal monster rules/Freeze|freeze]]_

##### Ecology

**Environment** any
**Organization** solitary, pair, or troop (3-7)
**Treasure** none

### Special Abilities

**Alert (Su)** An ivory sentinel can take simple orders and _[[spells/Identify|identify]]_ intruders. This functions as the iron sentinel’s alert ability).

**Disorienting _Screech_ (Su)** Three times per day, an ivory sentinel can emit a disorienting _screech_ as a standard action. All living creatures within a 30-foot spread must succeed at a DC 15 Will save or become _[[conditions/Confused|confused]]_ (as per the spell _[[spells/Confusion|confusion]]_) for 1d4+1 rounds. A creature that succeeds at this saving throw is immune to further disorienting screeches from that ivory sentinel for 24 hours. This is a sonic, mind-affecting effect. The save is Constitution-based.

**_[[universal monster rules/Immunity|Immunity]]_ to Magic (Ex)** An ivory sentinel is immune to spells or _spell-like abilities_ that allow _[[universal monster rules/Spell Resistance|spell resistance]]_, except for spells with the sonic descriptor.

**Poison (Ex)** Claws—injury; save Fort DC 15; frequency 1/round for 6 rounds; effect 1d3 Con damage; cure 2 consecutive saves. The save DC is Constitution-based.

##### Description

Ivory sentinels were most often employed by the upper echelons of Thassilonian aristocracy, especially across Bakrakhan and Shalast. These nobles competed with one another in decking out the approaches to their palaces with outlandish and lethal guardians, and the avian ivory sentinels served this purpose well. Often employed to terrorize peasants and foreign dignitaries, most of these constructs were destroyed during Earthfall when those extravagant palaces came tumbling down.

When an ivory sentinel takes _[[universal monster rules/Flight|flight]]_, delicate wings carved to resemble those of a bird unfurl from the sides of its skull-like head.
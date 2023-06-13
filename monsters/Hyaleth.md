---
cssclass: [monsters]
title1: Hyaleth
desc_short: This giant translucent leech has three squirming tentacles around an orifice
  on one end and a stinger on the other.
title2: Hyaleth
CR: 10
sources:
- name: "Pathfinder #130: City in the Lion's Eye"
  page: 84
  link: http://paizo.com/products/btpy9wmy?Pathfinder-Adventure-Path-City-in-the-Lions-Eye
XP: 9600
alignment: N
size: Large
type: aberration
subtypes:
- aquatic
initiative:
  bonus: 6
senses:
  darkvision: 60
  thoughtsense: 60
AC:
  AC: 23
  touch: 12
  flat_footed: 20
  components:
    dex: 2
    dodge: 1
    natural: 11
    size: -1
HP:
  HP: 127
  long: 15d8+60
saves:
  fort: 11
  ref: 7
  will: 11
DR:
- amount: 10
  weakness: slashing
immunities:
- acid
resistances:
  cold: 10
speeds:
  base: 20
  other_semicolon: aquiferous glide
  burrow: 20
  burrow_other: wet earth or saturated stone only
  swim: 30
attacks:
  melee:
  - - text: sting +16 (1d8+5 plus poison and probe intellect)
      entries:
      - - damage: 1d8+5
        - effect: poison
        - effect: probe intellect
      attack: sting
      bonus:
      - 16
    - text: 3 tentacles +14 (1d6+2 plus grab)
      entries:
      - - damage: 1d6+2
        - effect: grab
      count: 3
      attack: tentacles
      bonus:
      - 14
  special:
  - adaptive digestion
  - engulf (DC 22)
  - poison
space: 10
reach: 10
ability_scores:
  STR: 21
  DEX: 15
  CON: 18
  INT: 12
  WIS: 14
  CHA: 11
BAB: 11
CMB: 17
CMB_other: +21 grapple
CMD: 30
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Dodge
- name: Great Fortitude
- name: Improved Initiative
- name: Multiattack
- name: Skill Focus (Stealth)
- name: Weapon Focus (sting)
- name: Weapon Focus (tentacle)
skills:
  Escape Artist: 20
  Perception: 20
  Stealth: 22
    when swimming: 26
  Survival: 20
  Swim: 31
  _racial_mods:
    Stealth:
      when swimming: 4
languages:
- Aklo
- Common
- telepathy 100 ft.
special_qualities:
- compression
ecology:
  environment: temperate fresh water or underground
  organization: solitary, squad (2-9), or colony (10-200 and 1 hyaleth queen)
  treasure_type: incidental
special_abilities:
  Adaptive Digestion (Ex): |-
    A hyaleth can alter the makeup of its digestive secretions to suit one of two different purposes. It can switch between secretions as a swift action, and each secretion has a different effect on creatures the hyaleth has engulfed with its engulf extraordinary ability. The hyaleth can choose one of the following effects, and it must apply the same effect to all creatures it has engulfed. A hyaleth can affect engulfed creatures with only one of the following effects per round. 

    Digest Body: Engulfed creatures take 2d6 points of acid damage and must succeed at a DC 21 Fortitude save or take 1d2 points of Constitution damage. A creature reduced to negative hit points by this effect is dissolved entirely. 

    Digest Thoughtsf: Engulfed creatures that are awake must succeed at a DC 21 Will save or take 1d2 points of Intelligence damage and fall asleep for 1 hour. Each time a creature fails its save against this effect, as a free action the hyaleth can retrieve one answer to a specific question as though sifting through the creature's surface thoughts with detect thoughts. Alternatively, the hyaleth can attempt one Knowledge check in a skill in which the engulfed creature has at least 1 rank, using the creature's current total skill modifier. This is a mind-affecting effect. The secretions used to digest thoughts are foamy and oxygenated, allowing engulfed creatures to breathe normally while it is in effect. The save DCs are Constitution-based.
  Aquiferous Glide (Su): A hyaleth can travel through aquifers and sodden earth with
    ease, even while it has creatures engulfed within its body. This functions like
    the earth glide universal monster rule, except the hyaleth can move through only
    earth and stone saturated with water. While a hyaleth travels in this manner,
    creatures it has engulfed that are unable to burrow cannot escape except through
    magical means.
  Engulf (Ex): A hyaleth can engulf Medium or smaller creatures, but it loses its
    compression special quality and its racial bonus on Stealth checks when it has
    a creature engulfed. Engulfed creatures are subject to the hyaleth's adaptive
    digestion.
  Poison (Ex): Sting-injury; save Fort DC 21; frequency 1/round for 2 rounds; effect
    paralysis for 1d3 rounds (the duration of the paralysis is cumulative with each
    failed save); cure 1 save. The save DC is Constitution-based. When a creature
    fails its initial saving throw against the poison delivered by a hyaleth's sting
    attack, the hyaleth learns the creature's Intelligence score.
desc_long: |-
  Hyaleths are translucent, tubular aberrations hailing from deep underground waters. They occasionally travel to the surface, usually during heavy downpours, emerging into lakes, streams, swamps, and sometimes wells. Inquisitive and aggressive, hyaleths come to the surface to explore and to hunt sentient humanoids. Despite their large size, hyaleth can swim and hide in surprisingly shallow waters, allowing them to remain undetected while approaching their prey. Once it closes in on a target, a hyaleth uses its stinger to deliver a paralyzing neurotoxin before engulfing its victim within its elastic body. Though hyaleths cannot breathe air, they can leave the water and slither along the ground for short periods of time.

   An average hyaleth is 16 feet long and weighs about 1,300 pounds.

---

# Hyaleth
This giant translucent leech has three squirming tentacles around an orifice on one end and a stinger on the other.
**Source** Pathfinder #130: City in the _[[monsters/Lion|Lion]]_'s Eye pg. 84
**XP** 9,600

N Large aberration (aquatic)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Thoughtsense|thoughtsense]]_ 60 ft.; Perception +20

##### Defense

**AC** 23, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+2 Dex, +1 dodge, +11 natural, –1 size)
**hp** 127 (15d8+60)
**Fort** +11, **Ref** +7, **Will** +11
**DR** 10/slashing; **Immune** acid; **Resist** cold 10

##### Offense
**Speed** 20 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft. (wet earth or saturated stone only), swim 30 ft.; aquiferous _[[spells/Glide|glide]]_
**Melee** sting +16 (1d8+5 plus poison and probe intellect), 3 tentacles +14 (1d6+2 plus _[[universal monster rules/Grab|grab]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** adaptive digestion, _[[universal monster rules/Engulf|engulf]]_ (DC 22), poison

##### Statistics
**Str** 21, **Dex** 15, **Con** 18, **Int** 12, **Wis** 14, **Cha** 11
**Base Atk** +11; **CMB** +17 (+21 grapple); **CMD** 30 (can't be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth), _[[feats/Weapon Focus|Weapon Focus]]_ (sting, tentacle)
**Skills** Escape Artist +20, Perception +20, Stealth +22 (+26 when swimming), Survival +20, Swim +31; **Racial Modifiers** +4 Stealth when swimming
**Languages** Aklo, Common; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Compression|compression]]_

##### Ecology

**Environment** temperate fresh water or underground
**Organization** solitary, squad (2–9), or colony (10–200 and 1 _[[monsters/Hyaleth|hyaleth]]_ queen)
**Treasure** incidental

### Special Abilities

**Adaptive Digestion (Ex)** A _hyaleth_ can alter the makeup of its digestive secretions to suit one of two different purposes. It can switch between secretions as a swift action, and each secretion has a different effect on creatures the _hyaleth_ has engulfed with its _engulf_ extraordinary ability. The _hyaleth_ can choose one of the following effects, and it must apply the same effect to all creatures it has engulfed. A _hyaleth_ can affect engulfed creatures with only one of the following effects per round.

Digest Body: Engulfed creatures take 2d6 points of acid damage and must succeed at a DC 21 Fortitude save or take 1d2 points of Constitution damage. A creature reduced to negative hit points by this effect is dissolved entirely.

Digest Thoughtsf: Engulfed creatures that are awake must succeed at a DC 21 Will save or take 1d2 points of Intelligence damage and fall asleep for 1 hour. Each time a creature fails its save against this effect, as a free action the _hyaleth_ can retrieve one answer to a specific question as though sifting through the creature’s surface thoughts with _[[spells/Detect Thoughts|detect thoughts]]_. Alternatively, the _hyaleth_ can attempt one Knowledge check in a skill in which the engulfed creature has at least 1 rank, using the creature’s current total skill modifier. This is a mind-affecting effect. The secretions used to digest thoughts are foamy and oxygenated, allowing engulfed creatures to breathe normally while it is in effect. The save DCs are Constitution-based.

**Aquiferous _Glide_ (Su)** A _hyaleth_ can travel through aquifers and sodden earth with ease, even while it has creatures engulfed within its body. This functions like the _[[universal monster rules/Earth Glide|earth glide]]_ universal monster rule, except the _hyaleth_ can move through only earth and stone saturated with water. While a _hyaleth_ travels in this manner, creatures it has engulfed that are unable to _burrow_ cannot escape except through magical means.

**_Engulf_ (Ex)** A _hyaleth_ can _engulf_ _[[classes/Medium|Medium]]_ or smaller creatures, but it loses its _compression_ special quality and its racial bonus on Stealth checks when it has a creature engulfed. Engulfed creatures are subject to the _hyaleth_’s adaptive digestion.

**Poison (Ex)** Sting—injury; save Fort DC 21; frequency 1/round for 2 rounds; effect _[[universal monster rules/Paralysis|paralysis]]_ for 1d3 rounds (the duration of the _paralysis_ is cumulative with each failed save); cure 1 save. The save DC is Constitution-based. When a creature fails its initial saving throw against the poison delivered by a _hyaleth_’s sting attack, the _hyaleth_ learns the creature’s Intelligence score.

##### Description

Hyaleths are translucent, tubular aberrations hailing from deep underground waters. They occasionally travel to the surface, usually during heavy downpours, emerging into lakes, streams, swamps, and sometimes wells. Inquisitive and aggressive, hyaleths come to the surface to explore and to hunt sentient humanoids. Despite their large size, _hyaleth_ can swim and hide in surprisingly shallow waters, allowing them to remain undetected while approaching their prey. Once it closes in on a target, a _hyaleth_ uses its stinger to deliver a paralyzing neurotoxin before engulfing its victim within its elastic body. Though hyaleths cannot breathe air, they can leave the water and slither along the ground for short periods of time.

An average _hyaleth_ is 16 feet long and weighs about 1,300 pounds.
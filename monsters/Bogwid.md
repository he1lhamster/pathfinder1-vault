---
cssclass: [monsters]
title1: Bogwid
desc_short: This nightmare shambles along the ground on eight muscular tentacles that
  leave behind a clear viscous residue stinking of putrefaction. Its amphibian skin
  is moist, green-black, and covered in warts and protuberances. On its back, dozens
  of fistsized pustules shift and pulsate with nauseating vitality, like sentient
  oily bubbles threatening to burst.
title2: Bogwid
CR: 5
sources:
- name: "Pathfinder #62: Curse of the Lady's Light"
  page: 84
  link: http://paizo.com/products/btpy8run?Pathfinder-Adventure-Path-62-Curse-of-the-Ladys-Light
XP: 1600
alignment: CN
size: Medium
type: aberration
initiative:
  bonus: 8
senses:
  darkvision: 60
auras:
- name: revolting aura
  radius: 10
  DC: 13
  DC_type: Fort
AC:
  AC: 19
  touch: 14
  flat_footed: 15
  components:
    dex: 4
    natural: 5
HP:
  HP: 47
  long: 5d8+25
saves:
  fort: 5
  ref: 5
  will: 1
resistances:
  acid: 5
  cold: 5
speeds:
  base: 30
  climb: 20
  swim: 20
attacks:
  melee:
  - - text: 2 slams +7 (1d6+4 plus nauseating touch)
      entries:
      - - damage: 1d6+4
        - effect: nauseating touch
      count: 2
      attack: slams
      bonus:
      - 7
  ranged:
  - - text: offspring +7 ranged touch (1d2 bleed plus disease)
      entries:
      - - damage: 1d2
          type: bleed
        - effect: disease
      attack: offspring
      bonus:
      - 7
      touch: true
ability_scores:
  STR: 19
  DEX: 18
  CON: 18
  INT: 3
  WIS: 4
  CHA: 13
BAB: 3
CMB: 7
CMD: 21
CMD_other: 33 vs. trip
feats:
- name: Improved Initiative
- name: Stealthy
- name: Toughness
skills:
  Climb: 16
  Escape Artist: 6
  Perception: 2
  Stealth: 11
    in swamps: 19
  Swim: 12
  _racial_mods:
    Stealth:
      in swamps: 8
special_qualities:
- amphibious
ecology:
  environment: any swamps or underground
  organization: solitary or clutch (1 adult plus 2-8 adolescents)
  treasure_type: none
special_abilities:
  Disease (Ex): 'Bogwid Fever: Bite-injury; save Fort DC 16, onset 1 day, frequency
    1/day, effect 1d2 Str damage and shaken, cure 2 consecutive saves. The DC save
    is Constitution-based.'
  Nauseating Touch (Ex): The bogwid's touch is disgusting. Creatures hit by its slam
    attack must succeed at a DC 16 Fortitude save or be nauseated for 1 round. The
    save DC is Constitution-based.
  Ravenous Young (Ex): Each round, a bogwid can launch one of the offspring clinging
    to its back at a target within 10 feet as a ranged touch attack. On a successful
    hit, the offspring attaches itself to the target and begins draining blood, automatically
    dealing 1d2 points of bleed damage each round (and possibly infecting the target
    with bogwid fever). As a full-round action, a creature can attempt to remove one
    of these offspring, either by bludgeoning it with a fist or pulling it off. Either
    way, removing an offspring kills the larval creature. Someone other than the target
    the offspring is attached to can also perform this action. Anyone using a weapon
    to kill or remove an attached offspring deals half of the damage to the creature
    to which the offspring is attached. A bogwid can launch up to 10 offspring per
    day before it must rest and gestate more larval young.
  Revolting Aura (Ex): The bogwid is both visually and odoriferously revolting. Any
    creature within 10 feet of a bogwid must succeed at a DC 16 Fortitude save or
    be sickened. This effect persists as long as the creature is within the aura and
    for 2 rounds thereafter. A creature that successfully saves is not subject to
    the same bogwid's revolting aura for 24 hours. The save DC is Constitution-based.
desc_long: Aberrant beasts of ancient origin, bogwids are loathsome, skulking predators
  that inhabit the gloomy swamps and damp subterranean places of the world. Looking
  like a bloated, eight-limbed, greenish-black mix of frog and tentacled beast, this
  asexual creature is most notorious for the larvae it carries on its back.

---

# Bogwid
This _[[spells/Nightmare|nightmare]]_ shambles along the ground on eight muscular tentacles that leave behind a clear viscous residue stinking of putrefaction. Its amphibian skin is moist, green-black, and covered in warts and protuberances. On its back, dozens of fistsized pustules shift and pulsate with nauseating vitality, like sentient oily bubbles threatening to burst.
**Source** Pathfinder #62: Curse of the Lady's Light pg. 84
**XP** 1,600

CN Medium aberration
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +2
**Aura** revolting aura (10 ft., DC 13 Fort)

##### Defense

**AC** 19, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 Dex, +5 natural)
**hp** 47 (5d8+25)
**Fort** +5, **Ref** +5, **Will** +1
**Resist** acid 5, cold 5

##### Offense
**Speed** 30 ft., _[[universal monster rules/Climb|climb]]_ 20 ft., swim 20 ft.
**Melee** 2 slams +7 (1d6+4 plus nauseating touch)
**Ranged** offspring +7 ranged touch (1d2 _[[universal monster rules/Bleed|bleed]]_ plus disease)

##### Statistics
**Str** 19, **Dex** 18, **Con** 18, **Int** 3, **Wis** 4, **Cha** 13
**Base Atk** +3; **CMB** +7; **CMD** 21 (33 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Stealthy|Stealthy]]_, _[[feats/Toughness|Toughness]]_
**Skills** _Climb_ +16, Escape Artist +6, Perception +2, Stealth +11 (+19 in swamps), Swim +12; **Racial Modifiers** +8 Stealth in swamps
**SQ** _[[universal monster rules/Amphibious|amphibious]]_

##### Ecology

**Environment** any swamps or underground
**Organization** solitary or clutch (1 adult plus 2–8 adolescents)
**Treasure** none

### Special Abilities

**Disease (Ex) **_[[monsters/Bogwid|Bogwid]]_ Fever: Bite—injury; save Fort DC 16, onset 1 day, frequency 1/day, effect 1d2 Str damage and _[[conditions/Shaken|shaken]]_, cure 2 consecutive saves. The DC save is Constitution-based.

**Nauseating Touch (Ex)** The _bogwid_’s touch is disgusting. Creatures hit by its slam attack must succeed at a DC 16 Fortitude save or be _[[conditions/Nauseated|nauseated]]_ for 1 round. The save DC is Constitution-based.

**_[[curses/Ravenous|Ravenous]]_ Young (Ex) **Each round, a _bogwid_ can launch one of the offspring clinging to its back at a target within 10 feet as a ranged touch attack. On a successful hit, the offspring attaches itself to the target and begins draining blood, automatically dealing 1d2 points of _bleed_ damage each round (and possibly infecting the target with _bogwid_ fever). As a full-round action, a creature can attempt to remove one of these offspring, either by bludgeoning it with a fist or pulling it off. Either way, removing an offspring kills the larval creature. Someone other than the target the offspring is attached to can also perform this action. Anyone using a weapon to kill or remove an attached offspring deals half of the damage to the creature to which the offspring is attached. A _bogwid_ can launch up to 10 offspring per day before it must rest and gestate more larval young.

**Revolting Aura (Ex) **The _bogwid_ is both visually and odoriferously revolting. Any creature within 10 feet of a _bogwid_ must succeed at a DC 16 Fortitude save or be _[[conditions/Sickened|sickened]]_. This effect persists as long as the creature is within the aura and for 2 rounds thereafter. A creature that successfully saves is not subject to the same _bogwid_’s revolting aura for 24 hours. The save DC is Constitution-based.

##### Description

Aberrant beasts of ancient origin, bogwids are loathsome, skulking predators that inhabit the gloomy swamps and damp subterranean places of the world. Looking like a bloated, eight-limbed, greenish-black mix of frog and tentacled beast, this asexual creature is most notorious for the larvae it carries on its back.
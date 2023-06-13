---
cssclass: [monsters]
title1: Prismatic Orrery
desc_short: A series of metal rings rotates around a giant prismatic sphere.
title2: Prismatic Orrery
CR: 13
sources:
- name: Tombs of Golarion
  page: 53
  link: http://paizo.com/products/btpy98yu?Pathfinder-Campaign-Setting-Tombs-of-Golarion
XP: 25600
alignment: N
size: Gargantuan
type: construct
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
  true seeing: true
AC:
  AC: 24
  touch: 8
  flat_footed: 22
  components:
    dex: 2
    natural: 16
    size: -4
HP:
  HP: 159
  long: 18d10+60
saves:
  fort: 6
  ref: 8
  will: 6
defensive_abilities:
- all-around vision
- dispel resistance
- hardness 10
immunities:
- construct traits
speeds:
  base: 0
  base_other: cannot move
attacks:
  melee:
  - - text: slam +21 (6d6+10 plus grab)
      entries:
      - - damage: 6d6+10
        - effect: grab
      attack: slam
      bonus:
      - 21
  special:
  - blinding pulse
  - constrict (6d6+10)
  - prismatic refraction (+17 ranged touch, DC 21, every 1d4 rounds)
space: 20
reach: 15
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  sources:
  - name: default
    CL: 13
    concentration: 8
ability_scores:
  STR: 25
  DEX: 14
  CON:
  INT:
  WIS: 10
  CHA: 1
BAB: 18
CMB: 29
CMB_other: +33 grapple
CMD: 41
skills:
  Perception: 12
  _racial_mods:
    Perception:
      _: 12
special_abilities:
  Blinding Pulse (Ex): As a move action, the prismatic orrery can set its lenses to
    refract the light of the prismatic sphere at its center, granting it a gaze attack
    that causes blindness in all targets that fail a DC 19 Fortitude saving throw.
    This gaze attack can be disabled as a move action, and is automatically disabled
    if the orrery uses its prismatic refraction ability or if the prismatic sphere
    is temporarily dispelled. The save DC is Constitution-based.
  Dispel Resistance (Su): The prismatic sphere at the center of the orrery (CL 20th)
    can be dispelled with a targeted dispel magic spell, but only temporarily. As
    the sphere is fueled by the elemental energies within the Prismatic Lantern's
    demiplane, it reappears after 1d3 rounds. While the prismatic sphere is inactive,
    the prismatic orrery cannot use its blinding pulse and prismatic refraction abilities.
  Prismatic Refraction (Ex): As a standard action, the prismatic orrery can position
    its many rings and lenses such that the magical energy of the prismatic sphere
    at its center is aimed in a series of beams at all targets within 60 feet. These
    beams take the form of a prismatic spray spell (CL 13th); determine the color
    of each ray randomly with a roll of 1d8 as indicated in the spell. A prismatic
    refraction ray is a ranged touch attack with a +17 bonus to hit and a save DC
    of 21. It takes the prismatic orrery 1d4 rounds to recalibrate its lenses to recharge
    this ability. The save DC is Dexterity-based.
desc_long: The automated orrery atop the Prismatic Lantern takes no defensive actions
  against intruders except when attacked or if commanded to do so by the wielder of
  a crystal control rod.

---

# Prismatic Orrery
A series of metal rings rotates around a giant _[[spells/Prismatic Sphere|prismatic sphere]]_.
**Source** Tombs of Golarion pg. 53
**XP** 25,600

N Gargantuan construct
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/True Seeing|true seeing]]_; Perception +12

##### Defense

**AC** 24, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+2 Dex, +16 natural, –4 size)
**hp** 159 (18d10+60)
**Fort** +6, **Ref** +8, **Will** +6
**Defensive Abilities** _[[universal monster rules/All-Around Vision|all-around vision]]_, dispel _[[universal monster rules/Resistance|resistance]]_, hardness 10; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_

##### Offense
**Speed** 0 ft. (cannot move)
**Melee** slam +21 (6d6+10 plus _[[universal monster rules/Grab|grab]]_)
**Space** 20 ft., **Reach** 15 ft.
**Special Attacks** _[[items/Armor Magic Abilities/Blinding|blinding]]_ pulse, _[[universal monster rules/Constrict|constrict]]_ (6d6+10), prismatic refraction (+17 ranged touch, DC 21, every 1d4 rounds)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +8)
Constant—_true seeing_

##### Statistics
**Str** 25, **Dex** 14, **Con** —, **Int** —, **Wis** 10, **Cha** 1
**Base Atk** +18; **CMB** +29 (+33 grapple); **CMD** 41
**Skills** Perception +12; **Racial Modifiers** +12 Perception

### Special Abilities

**_Blinding_ Pulse (Ex)** As a move action, the _[[monsters/Prismatic Orrery|prismatic orrery]]_ can set its lenses to refract the light of the _prismatic sphere_ at its center, granting it a _[[universal monster rules/Gaze|gaze]]_ attack that causes blindness in all targets that fail a DC 19 Fortitude saving throw. This _gaze_ attack can be _[[conditions/Disabled|disabled]]_ as a move action, and is automatically _disabled_ if the orrery uses its prismatic refraction ability or if the _prismatic sphere_ is temporarily dispelled. The save DC is Constitution-based.

**Dispel _Resistance_ (Su)** The _prismatic sphere_ at the center of the orrery (CL 20th) can be dispelled with a targeted _[[spells/Dispel Magic|dispel magic]]_ spell, but only temporarily. As the sphere is fueled by the elemental energies within the Prismatic Lantern’s demiplane, it reappears after 1d3 rounds. While the _prismatic sphere_ is inactive, the _prismatic orrery_ cannot use its _blinding_ pulse and prismatic refraction abilities.

**Prismatic Refraction (Ex)** As a standard action, the _prismatic orrery_ can position its many rings and lenses such that the magical energy of the _prismatic sphere_ at its center is aimed in a series of beams at all targets within 60 feet. These beams take the form of a _[[spells/Prismatic Spray|prismatic spray]]_ spell (CL 13th); determine the color of each ray randomly with a roll of 1d8 as indicated in the spell. A prismatic refraction ray is a ranged touch attack with a +17 bonus to hit and a save DC of 21. It takes the _prismatic orrery_ 1d4 rounds to recalibrate its lenses to _[[spells/Recharge|recharge]]_ this ability. The save DC is Dexterity-based.

##### Description

The automated orrery atop the Prismatic Lantern takes no defensive actions against intruders except when attacked or if commanded to do so by the wielder of a _[[items/Rod/Crystal Control Rod|crystal control rod]]_.
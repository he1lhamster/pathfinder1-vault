---
cssclass: [monsters]
title1: Gravitic Globe
desc_short: This large, adamantine sphere is carved to resemble the surface of Golarion,
  and burns with magical flame.
title2: Gravitic Globe
CR: 10
sources:
- name: Tombs of Golarion
  page: 52
  link: http://paizo.com/products/btpy98yu?Pathfinder-Campaign-Setting-Tombs-of-Golarion
XP: 9600
alignment: N
size: Large
type: construct
initiative:
  bonus: -1
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: magnetism
  radius: 30
  DC: 20
AC:
  AC: 18
  touch: 8
  flat_footed: 18
  components:
    dex: -1
    natural: 10
    size: -1
HP:
  HP: 140
  long: 20d10+30
saves:
  fort: 6
  ref: 5
  will: 1
defensive_abilities:
- hardness 20
- magnetism
immunities:
- construct traits
speeds:
  base: 30
attacks:
  melee:
  - - text: slam +29 (3d6+15 plus burn)
      entries:
      - - damage: 3d6+15
        - effect: burn
      attack: slam
      bonus:
      - 29
  special:
  - burn (2d6 fire, DC 20)
  - trample (3d6+15 plus burn, DC 30)
space: 10
reach: 5
ability_scores:
  STR: 30
  DEX: 8
  CON:
  INT:
  WIS: 1
  CHA: 1
BAB: 20
CMB: 31
CMD: 40
CMD_other: can't be tripped
skills: {}
special_abilities:
  Magnetism (Ex): The gravitic globe is surrounded by an aura of magnetism that allows
    it to attract metal objects and creatures. A metal creature or creature wearing
    metal armor that begins its turn within the globe's aura must succeed at a DC
    20 Reflex saving throw or fall prone; standing up from prone within the aura is
    a standard action for such creatures. Such a creature that enters the globe's
    aura must succeed at a DC 20 Reflex save or be pushed back 5 feet, ending its
    movement. On its turn, the gravitic globe can attempt a bull rush, pull, or trip
    combat maneuver against a single metal or metal-wearing creature within its aura
    as a swift action that does not provoke attacks of opportunity. Alternatively,
    it can attempt a disarm or steal combat maneuver targeting a metal weapon or item
    within its aura as a swift action that does not provoke attacks of opportunity.
    The erratic magnetic field surrounding the globe grants it a 20% miss chance against
    attacks made with metallic weapons (including ammunition), as the invisible forces
    make targeting unpredictable. The save DC is Constitution-based.
desc_long: Having seen a similar construct made of stone in an arcane library in the
  Five Kings Mountains, Alzika Karr was determined to improve upon the design. Wishing
  to make the construct as realistic as possible so as to fall in line with her experiences
  in the Darklands researching magnetic ores and magma, the Arclord procured a rare
  sample of a plasma ooze (Pathfinder RPG Bestiary 3 220) from a colleague in Oenopion
  and infused it into the core of her gravitic globe. The effects on the newly forged
  construct were remarkable- not only did it draw metallic objects toward it as the
  ooze did, but it occasionally repelled them as well.

---

# Gravitic Globe
This large, adamantine sphere is carved to resemble the surface of Golarion, and burns with magical flame.
**Source** Tombs of Golarion pg. 52
**XP** 9,600

N Large construct
**Init** –1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception –5
**Aura** magnetism (30 ft., DC 20)

##### Defense

**AC** 18, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 18 (–1 Dex, +10 natural, –1 size)
**hp** 140 (20d10+30)
**Fort** +6, **Ref** +5, **Will** +1
**Defensive Abilities** hardness 20, magnetism; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_

##### Offense
**Speed** 30 ft.
**Melee** slam +29 (3d6+15 plus _[[universal monster rules/Burn|burn]]_)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** _burn_ (2d6 fire, DC 20), _[[universal monster rules/Trample|trample]]_ (3d6+15 plus _burn_, DC 30)

##### Statistics
**Str** 30, **Dex** 8, **Con** —, **Int** —, **Wis** 1, **Cha** 1
**Base Atk** +20; **CMB** +31; **CMD** 40 (can’t be tripped)

### Special Abilities

**Magnetism (Ex)** The _[[monsters/Gravitic Globe|gravitic globe]]_ is surrounded by an aura of magnetism that allows it to attract metal objects and creatures. A metal creature or creature wearing metal armor that begins its turn within the globe’s aura must succeed at a DC 20 Reflex saving throw or fall _[[conditions/Prone|prone]]_; standing up from _prone_ within the aura is a standard action for such creatures. Such a creature that enters the globe’s aura must succeed at a DC 20 Reflex save or be pushed back 5 feet, ending its movement. On its turn, the _gravitic globe_ can attempt a bull rush, _[[universal monster rules/Pull|pull]]_, or _[[universal monster rules/Trip|trip]]_ combat maneuver against a single metal or metal-wearing creature within its aura as a swift action that does not provoke attacks of opportunity. Alternatively, it can attempt a disarm or steal combat maneuver targeting a metal weapon or item within its aura as a swift action that does not provoke attacks of opportunity. The erratic _[[spells/Magnetic Field|magnetic field]]_ surrounding the globe grants it a 20% miss chance against attacks made with metallic weapons (including ammunition), as the _[[conditions/Invisible|invisible]]_ forces make targeting unpredictable. The save DC is Constitution-based.

##### Description

Having seen a similar construct made of stone in an arcane library in the Five Kings Mountains, Alzika Karr was determined to improve upon the design. Wishing to make the construct as realistic as possible so as to fall in line with her experiences in the Darklands researching magnetic ores and magma, the Arclord procured a rare sample of a _[[monsters/Plasma Ooze|plasma ooze]]_ (Pathfinder RPG Bestiary 3 220) from a colleague in Oenopion and infused it into the core of her _gravitic globe_. The effects on the newly forged construct were remarkable— not only did it draw metallic objects toward it as the ooze did, but it occasionally repelled them as well.
---
cssclass: [monsters]
title1: Gunpowder Ooze
desc_short: This lurching mass of slime and gunpowder leaves a trail of shiny black
  residue in its wake, and shudders with concussive energy.
title2: Gunpowder Ooze
CR: 14
sources:
- name: Bestiary 5
  page: 139
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
- name: Wardens of the Reborn Forge
  page: 63
  link: http://paizo.com/products/btpy92lr?Pathfinder-Module-Wardens-of-the-Reborn-Forge
XP: 38400
alignment: N
size: Large
type: ooze
initiative:
  bonus: 0
AC:
  AC: 9
  touch: 9
  flat_footed: 9
  components:
    size: -1
HP:
  HP: 230
  long: 20d8+140
saves:
  fort: 13
  ref: 6
  will: 1
defensive_abilities:
- split (slashing or fire, 46 hp)
immunities:
- cold
- ooze traits
weaknesses:
- vulnerable to fire
speeds:
  base: 20
  climb: 20
attacks:
  melee:
  - - text: slam +23 (2d6+13 plus grab and gunpowder residue)
      entries:
      - - damage: 2d6+13
        - effect: grab
        - effect: gunpowder residue
      attack: slam
      bonus:
      - 23
  ranged:
  - - text: blast +14 touch (4d6+7 plus gunpowder residue)
      entries:
      - - damage: 4d6+7
        - effect: gunpowder residue
      attack: blast
      bonus:
      - 14
      touch: true
  special:
  - blast
  - combust
  - constrict (2d6+13)
  - gunpowder residue
space: 10
reach: 10
ability_scores:
  STR: 28
  DEX: 11
  CON: 24
  INT:
  WIS: 1
  CHA: 1
BAB: 15
CMB: 25
CMB_other: +29 grapple
CMD: 35
CMD_other: can't be tripped
skills:
  Climb: 17
  Perception: -5
ecology:
  environment: any land
  organization: solitary
  treasure_type: none
special_abilities:
  Blast (Ex): Once every 1d4 rounds as a swift action, a gunpowder ooze can fire a
    blast of gunpowder from its body as a ranged touch attack, dealing an amount of
    damage equal to 4d6 + the ooze's Constitution modifier (+7 for most gunpowder
    oozes). Any creature struck by this blast is coated in the ooze's gunpowder residue
    (Reflex DC 27 negates). This attack has a range of 180 feet with no range increment.
    The save DC is Constitution-based.
  Combust (Ex): Because of its volatile nature, a gunpowder ooze may explode around
    open flames or sparks. Anytime a gunpowder ooze takes fire damage or damage from
    a ranged firearm attack, it spontaneously explodes, dealing 10d6 points of fire
    damage to all creatures and objects in a 30-foot cone facing the damage source
    that ignited the ooze (Reflex DC 27 half). If there is no method of determining
    the damage source's direction (such as a burst or spread centered on the ooze),
    the ooze instead combusts in a 15-foot-radius burst. A gunpowder ooze that combusts
    splits automatically. The save DC is Constitution-based.
  Gunpowder Residue (Ex): Whenever a gunpowder ooze successfully strikes a creature
    with its blast or slam attack, the target must succeed at a DC 27 Reflex save
    or be coated in sticky gunpowder residue. Though the residue is not harmful in
    itself, if a creature covered in the residue uses a firearm, wields any weapon
    capable of dealing fire damage, takes fire damage from any source, or is exposed
    to a suitable spark, the residue immediately ignites and explodes, dealing 5d6
    points of fire damage to the creature. Creatures adjacent to the exploding creature
    take half damage (which can be halved again with a successful DC 27 Reflex save).
    Gunpowder residue remains flammable for 24 hours, until it is ignited, or until
    it is scrubbed away (which requires soap, water, and at least 1 hour of bathing
    and washing). A creature can be covered in only up to one layer of gunpowder residue
    at a time. The save DC is Constitution-based.
desc_long: Common where wild magic and gunpowder are prevalent, gunpowder oozes are
  the combination of these two dangerous and unpredictable elements.

---

# Gunpowder Ooze
This lurching mass of slime and gunpowder leaves a trail of shiny black residue in its wake, and shudders with concussive energy.
**Source** Bestiary 5 pg. 139, Wardens of the Reborn Forge pg. 63
**XP** 38,400

N Large ooze
**Init** +0; **Senses** Perception –5

##### Defense

**AC** 9, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 9 (–1 size)
**hp** 230 (20d8+140)
**Fort** +13, **Ref** +6, **Will** +1
**Defensive Abilities** _[[universal monster rules/Split|split]]_ (slashing or fire, 46 hp); **Immune** cold, ooze traits
**Weaknesses** vulnerable to fire

##### Offense
**Speed** 20 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** slam +23 (2d6+13 plus _[[universal monster rules/Grab|grab]]_ and gunpowder residue)
**Ranged** blast +14 touch (4d6+7 plus gunpowder residue)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** blast, combust, _[[universal monster rules/Constrict|constrict]]_ (2d6+13), gunpowder residue

##### Statistics
**Str** 28, **Dex** 11, **Con** 24, **Int** —, **Wis** 1, **Cha** 1
**Base Atk** +15; **CMB** +25 (+29 grapple); **CMD** 35 (can’t be tripped)
**Skills** _Climb_ +17

##### Ecology

**Environment** any land
**Organization** solitary
**Treasure** none

### Special Abilities

**Blast (Ex)** Once every 1d4 rounds as a swift action, a _[[monsters/Gunpowder Ooze|gunpowder ooze]]_ can fire a blast of gunpowder from its body as a ranged touch attack, dealing an amount of damage equal to 4d6 + the ooze’s Constitution modifier (+7 for most gunpowder oozes). Any creature struck by this blast is coated in the ooze’s gunpowder residue (Reflex DC 27 negates). This attack has a range of 180 feet with no range increment. The save DC is Constitution-based.
 **Combust (Ex)** Because of its volatile nature, a _gunpowder ooze_ may explode around open flames or sparks. Anytime a _gunpowder ooze_ takes fire damage or damage from a ranged firearm attack, it spontaneously explodes, dealing 10d6 points of fire damage to all creatures and objects in a 30-foot cone facing the damage source that ignited the ooze (Reflex DC 27 half). If there is no method of determining the damage source’s direction (such as a burst or spread centered on the ooze), the ooze instead combusts in a 15-foot-radius burst. A _gunpowder ooze_ that combusts splits automatically. The save DC is Constitution-based.
 **Gunpowder Residue (Ex)** Whenever a _gunpowder ooze_ successfully strikes a creature with its blast or slam attack, the target must succeed at a DC 27 Reflex save or be coated in _[[items/Weapon Magic Abilities/Sticky|sticky]]_ gunpowder residue. Though the residue is not harmful in itself, if a creature covered in the residue uses a firearm, wields any weapon capable of dealing fire damage, takes fire damage from any source, or is exposed to a suitable _[[spells/Spark|spark]]_, the residue immediately ignites and explodes, dealing 5d6 points of fire damage to the creature. Creatures adjacent to the exploding creature take half damage (which can be halved again with a successful DC 27 Reflex save). Gunpowder residue remains flammable for 24 hours, until it is ignited, or until it is scrubbed away (which requires _[[items/Mundane/Soap|soap]]_, water, and at least 1 hour of bathing and washing). A creature can be covered in only up to one layer of gunpowder residue at a time. The save DC is Constitution-based.

##### Description

Common where wild magic and gunpowder are prevalent, gunpowder oozes are the combination of these two dangerous and unpredictable elements.
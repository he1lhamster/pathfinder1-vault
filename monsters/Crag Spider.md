---
cssclass: [monsters]
title1: Crag Spider
is_3.5: true
desc_short: This gigantic spider-thing is covered in jagged red-and-black chitin.
  Many-legged and alien, the creature's waving tendrils and serrated pedipalps twitch
  hungrily beneath a cluster of unblinking black eyes. Hooked claws at the ends of
  its many-jointed legs pierce the earth with every step.
title2: Crag Spider
CR: 8
sources:
- name: 'Pathfinder #6: Spires of Xin-Shalast'
  page: 77
  link: http://paizo.com/pathfinder/adventurePath/riseOfTheRunelords/v5748btpy817c
alignment: Always N
size: Huge
type: vermin
initiative:
  bonus: 4
senses:
  darkvision: 60
  tremorsense: 60
AC:
  AC: 19
  touch: 12
  flat_footed: 15
  components:
    dex: 4
    natural: 7
    size: -2
HP:
  HP: 104
  long: 16d8+32
saves:
  fort: 12
  ref: 9
  will: 5
immunities:
- mind-affecting effects
speeds:
  base: 40
  climb: 30
attacks:
  melee:
  - - text: bite +15 (2d6+7 plus poison)
      entries:
      - - damage: 2d6+7
        - effect: poison
      attack: bite
      bonus:
      - 15
  ranged:
  - - text: web +14 touch (entangle)
      entries:
      - - effect: entangle
      attack: web
      bonus:
      - 14
      touch: true
  special:
  - web
space: 15
reach: 10
ability_scores:
  STR: 20
  DEX: 18
  CON: 14
  INT:
  WIS: 10
  CHA: 2
BAB: 12
grapple_3.5: 25
feats:
- is_bonus: true
  name: Altitude Affinity
skills:
  Climb: 21
  Hide: 0
  Jump: 15
  Spot: 8
  Listen: 0
  _racial_mods:
    Jump:
      _: 4
special_qualities:
- tether
ecology:
  environment: cold mountains
  organization: solitary or colony (2-5)
  treasure:
  - 1/10 coins; 50% goods; 50% items
  advancement_3.5:
  - type: size
    HD_min: 17
    size: Huge
    HD_max: 32
  - type: size
    HD_min: 33
    size: Gargantuan
    HD_max: 48
special_abilities:
  Poison (Ex): Injury, Fortitude DC 20, 1d8 Str/1d8 Str. The save DC is Constitution-based.
  Tether (Ex): |-
    As a move action, a crag spider can anchor itself to a surface within its reach by a tether of webbing. This web is identical in characteristics to its normal webbing. A tethered crag spider gains a +10 competence bonus on Climb and Jump checks and can arrest any fall as a free action, taking no damage. The maximum distance a crag spider can jump or climb while tethered is 200 feet. It can release its tether as a free action and start another normally if it needs to move its anchor point.

    A crag spider cannot use any of its other web abilities while anchored to a tether. Creating a tether counts as one of the eight times a crag spider can throw its web per day.
  Web (Ex): Crag spiders can use the web ability as other monstrous spiders (see page
    288 of the MM). An entangled creature can escape with a successful DC 20 Escape
    Artist check or burst the web with a DC 24 Strength check. Each 5-foot section
    has 16 hit points.
desc_long: The original crag spiders were magically engineered from a species of common
  spider that resides atop the mountain and were created to serve as steeds for the
  personal guards of the Runelords of Greed. They are still primarily used for that
  purpose, but escapees from captivity over the years have begun to breed in the wild
  and migrate to other mountaintops.

---

# Crag Spider
This gigantic spider-thing is covered in jagged red-and-black chitin. Many-legged and alien, the creature’s waving tendrils and serrated pedipalps twitch hungrily beneath a cluster of unblinking black eyes. Hooked claws at the ends of its many-jointed legs pierce the earth with every step.
**Source** Pathfinder #6: Spires of Xin-Shalast pg. 77
Always N Huge vermin
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Tremorsense|tremorsense]]_ 60 ft.; Listen +0, Spot +8

##### Defense

**AC** 19, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 Dex, +7 natural, -2 size)
**hp** 104 (16d8+32)
**Fort** +12, **Ref** +9, **Will** +5
**Immune** mind-affecting effects

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 30 ft.
**Melee** bite +15 (2d6+7 plus poison)
**Ranged** web +14 touch (_[[spells/Entangle|entangle]]_)
**Space** 15 ft., **Reach** 10 ft.
**Special Attacks** web

##### Statistics
**Str** 20, **Dex** 18, **Con** 14, **Int** —, **Wis** 10, **Cha** 2
**Base Atk** +12; **Grapple** +25
**Feats** _[[feats/Altitude Affinity|Altitude Affinity]]_
**Skills** _Climb_ +21, Hide +0, _[[spells/Jump|Jump]]_ +15, Spot +8; **Racial Modifiers** +4 _Jump_
**SQ** tether

##### Ecology

**Environment** cold mountains
**Organization** solitary or colony (2-5)
**Treasure** 1/10 coins; 50% goods; 50% items
**Advancement** 17-32 HD (Huge), 33-48 HD (Gargantuan)

### Special Abilities

**Poison (Ex)** Injury, Fortitude DC 20, 1d8 Str/1d8 Str. The save DC is Constitution-based.

**Tether (Ex)** As a move action, a _[[monsters/Crag Spider|crag spider]]_ can anchor itself to a surface within its reach by a tether of webbing. This web is identical in characteristics to its normal webbing. A tethered _crag spider_ gains a +10 competence bonus on _Climb_ and _Jump_ checks and can arrest any fall as a free action, taking no damage. The maximum distance a _crag spider_ can _jump_ or _climb_ while tethered is 200 feet. It can release its tether as a free action and start another normally if it needs to move its anchor point.

A _crag spider_ cannot use any of its other web abilities while anchored to a tether. Creating a tether counts as one of the eight times a _crag spider_ can throw its web per day.

**Web (Ex)** Crag spiders can use the web ability as other monstrous spiders (see page 288 of the MM). An _[[conditions/Entangled|entangled]]_ creature can escape with a successful DC 20 Escape Artist check or burst the web with a DC 24 Strength check. Each 5-foot section has 16 hit points.

##### Description

The original crag spiders were magically engineered from a species of common spider that resides atop the mountain and were created to serve as steeds for the personal guards of the Runelords of Greed. They are still primarily used for that purpose, but escapees from captivity over the years have begun to breed in the wild and migrate to other mountaintops.
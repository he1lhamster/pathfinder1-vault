---
cssclass: [monsters]
title1: Juggernaut
desc_short: This oppressive construct rumbles forth on deadly rollers, crushing everything
  in its path.
title2: Juggernaut
CR: 11
sources:
- name: Bestiary 4
  page: 162
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 12800
alignment: N
size: Gargantuan
type: construct
initiative:
  bonus: 0
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 26
  touch: 6
  flat_footed: 26
  components:
    natural: 20
    size: -4
HP:
  HP: 142
  long: 15d10+60
  fast_healing: 5
saves:
  fort: 5
  ref: 5
  will: 9
DR:
- amount: 10
  weakness: adamantine
immunities:
- construct traits
SR: 22
weaknesses:
- faith-bound
speeds:
  base: 30
attacks:
  melee:
  - - text: slam +24 (4d6+19 plus wounding)
      entries:
      - - damage: 4d6+19
        - effect: wounding
      attack: slam
      bonus:
      - 24
  special:
  - soul-powered
  - vicious trample (8d6+38 plus wounding, DC 30)
space: 20
reach: 5
spell_like_abilities:
  entries:
  - name: enervation
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 15
    concentration: 10
ability_scores:
  STR: 36
  DEX: 11
  CON:
  INT:
  WIS: 18
  CHA: 1
BAB: 15
CMB: 32
CMD: 42
CMD_other: can't be tripped
skills: {}
special_qualities:
- keyed domains (Death, War)
- shrine
ecology:
  environment: any
  organization: solitary
  treasure_type: none
special_abilities:
  Faith-Bound (Su): A juggernaut cannot attack any creature that openly wears or displays
    the holy symbol or unholy symbol of the deity to which the juggernaut is dedicated
    unless that creature first attacks the juggernaut.
  Shrine (Ex): A juggernaut counts as a movable shrine for the deity or religion it
    is dedicated to.
  Soul-Powered (Su): When a juggernaut kills a creature with at least 5 Hit Dice and
    an alignment two or more steps away from the juggernaut's alignment, it gains
    a kill point. Add its current total kill points as a bonus on its attack rolls,
    combat maneuver checks, caster level checks, and skill checks. Add half its current
    total kill points as a bonus to its natural armor and spell resistance. The juggernaut
    loses 1 kill point every 24 hours.
  Vicious Trample (Ex): A juggernaut's massive rollers deal 8d6+38 points of damage
    on a successful trample attack.
desc_long: Juggernauts protect locations dedicated to a particular faith, their massive
  forms infused with divine energy that animates them and infuses them with their
  deity's power. Some faiths use a juggernaut as a mobile shrine, anointing it with
  sacred materials and offering prayers to the divine.

---

# Juggernaut
This oppressive construct rumbles forth on _[[items/Weapon Magic Abilities/Deadly|deadly]]_ rollers, crushing everything in its path.
**Source** Bestiary 4 pg. 162
**XP** 12,800

N Gargantuan construct
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +4

##### Defense

**AC** 26, touch 6, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+20 natural, –4 size)
**hp** 142 (15d10+60); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +5, **Ref** +5, **Will** +9
**DR** 10/adamantine; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_; **SR** 22
**Weaknesses** faith-bound

##### Offense
**Speed** 30 ft.
**Melee** slam +24 (4d6+19 plus _[[items/Weapon Magic Abilities/Wounding|wounding]]_)
**Space** 20 ft., **Reach** 5 ft.
**Special Attacks** soul-powered, _[[items/Weapon Magic Abilities/Vicious|vicious]]_ _[[universal monster rules/Trample|trample]]_ (8d6+38 plus _wounding_, DC 30)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +10)
3/day—_[[spells/Enervation|enervation]]_

##### Statistics
**Str** 36, **Dex** 11, **Con** —, **Int** —, **Wis** 18, **Cha** 1
**Base Atk** +15; **CMB** +32; **CMD** 42 (can’t be tripped)
**SQ** keyed domains (Death, War), shrine

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** none

### Special Abilities

**Faith-Bound (Su)** A _[[monsters/Juggernaut|juggernaut]]_ cannot attack any creature that openly wears or displays the holy symbol or _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol of the deity to which the _juggernaut_ is dedicated unless that creature first attacks the _juggernaut_.
**Shrine (Ex)** A _juggernaut_ counts as a movable shrine for the deity or religion it is dedicated to.
**Soul-Powered (Su)** When a _juggernaut_ kills a creature with at least 5 Hit Dice and an alignment two or more steps away from the _juggernaut_’s alignment, it gains a kill point. Add its current total kill points as a bonus on its attack rolls, combat maneuver checks, caster level checks, and skill checks. Add half its current total kill points as a bonus to its natural armor and _[[universal monster rules/Spell Resistance|spell resistance]]_. The _juggernaut_ loses 1 kill point every 24 hours.

**_Vicious_ _Trample_ (Ex)** A _juggernaut_’s massive rollers deal 8d6+38 points of damage on a successful _trample_ attack.

##### Description

Juggernauts protect locations dedicated to a particular faith, their massive forms infused with divine energy that animates them and infuses them with their deity’s power. Some faiths use a _juggernaut_ as a mobile shrine, anointing it with _[[items/Weapon Magic Abilities/Sacred|sacred]]_ materials and offering prayers to the divine.
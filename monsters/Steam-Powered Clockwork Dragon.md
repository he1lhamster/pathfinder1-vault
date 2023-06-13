---
cssclass: [monsters]
title1: Steam-Powered Clockwork Dragon
desc_short: Puffs of steam, quiet hissing, and a whirring of gears accompany this
  massive metal dragon.
title2: Steam-Powered Clockwork Dragon
CR: 18
sources:
- name: Construct Handbook
  page: 62
  link: https://paizo.com/products/btq01vam
XP: 153600
alignment: N
size: Huge
type: construct
subtypes:
- clockwork
initiative:
  bonus: 10
senses:
  darkvision: 60
  low-light vision: true
  see invisibility: true
AC:
  AC: 36
  touch: 16
  flat_footed: 28
  components:
    dex: 6
    dodge: 2
    natural: 20
    size: -2
HP:
  HP: 217
  long: 25d10+80
saves:
  fort: 8
  ref: 16
  will: 8
defensive_abilities:
- fortification 75%
DR:
- amount: 15
  weakness: adamantine
immunities:
- construct traits
resistances:
  fire: 30
SR: 27
weaknesses:
- vulnerable to electricity
speeds:
  base: 70
  fly: 110
  fly_maneuverability: average
  swim: 70
attacks:
  melee:
  - - text: bite +37 (4d6+14 plus 1d6 fire)
      entries:
      - - damage: 4d6+14
        - damage: 1d6
          type: fire
      attack: bite
      bonus:
      - 37
    - text: 2 claws +37 (2d8+14 plus 1d6 fire)
      entries:
      - - damage: 2d8+14
        - damage: 1d6
          type: fire
      count: 2
      attack: claws
      bonus:
      - 37
    - text: tail slap +32 (2d6+7 plus 1d6 fire)
      entries:
      - - damage: 2d6+7
        - damage: 1d6
          type: fire
      attack: tail slap
      bonus:
      - 32
    - text: 2 wings +32 (2d6+7 plus 1d6 fire)
      entries:
      - - damage: 2d6+7
        - damage: 1d6
          type: fire
      count: 2
      attack: wings
      bonus:
      - 32
  special:
  - adamantine weapons
  - breath weapon (100-ft. line, 14d6 fire damage, Reflex DC 22 half, usable every
    1d4 rounds)
  - self-destruction
  - storm blast
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: see invisibility
    source: default
    freq: Constant
  sources:
  - name: default
    CL: 25
    concentration: 20
ability_scores:
  STR: 38
  DEX: 23
  CON:
  INT:
  WIS: 11
  CHA: 1
BAB: 25
CMB: 41
CMD: 59
CMD_other: 63 vs. trip
feats:
- is_bonus: true
  name: Improved Initiative
- is_bonus: true
  name: Lightning Reflexes
- is_bonus: true
  name: Run
skills:
  Fly: 10
  Perception: 8
  Swim: 22
  _racial_mods:
    Fly:
      _: 8
    Perception:
      _: 8
special_qualities:
- heat management
- increased locomotion
- steam engine
- swift reactions
ecology:
  environment: any
  organization: solitary
  treasure_type: none
desc_long: |-
  Though some scholars may argue about who exactly created the first steam-powered clockwork, the secret of their manufacture is now out. Savvy engineers have started to create faster and more powerful clockwork contraptions in the form of marvels blending arcane heat sources with large boilers to create pressured steam that powers the complex constructs.

   The steam-powered clockwork dragon presented here is built using the clockwork dragon. See that entry for full descriptions of its base abilities.

---

# Steam-Powered Clockwork Dragon
Puffs of steam, quiet hissing, and a whirring of gears accompany this massive metal dragon.
**Source** Construct Handbook pg. 62
**XP** 153,600

N Huge construct (clockwork)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +8

##### Defense

**AC** 36, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+6 Dex, +2 dodge, +20 natural, -2 size)
**hp** 217 (25d10+80)
**Fort** +8, **Ref** +16, **Will** +8
**Defensive Abilities** _[[universal monster rules/Fortification|fortification]]_ 75%; **DR** 15/adamantine; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_; **Resist** fire 30; **SR** 27
**Weaknesses** vulnerable to electricity

##### Offense
**Speed** 70 ft., fly 110 ft. (average), swim 70 ft.
**Melee** bite +37 (4d6+14 plus 1d6 fire), 2 claws +37 (2d8+14 plus 1d6 fire), tail slap +32 (2d6+7 plus 1d6 fire), 2 wings +32 (2d6+7 plus 1d6 fire)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** adamantine weapons, _[[universal monster rules/Breath Weapon|breath weapon]]_ (100-ft. line, 14d6 fire damage, Reflex DC 22 half, usable every 1d4 rounds), self-destruction, storm blast
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 25th; concentration +20)
Constant—_see invisibility_

##### Statistics
**Str** 38, **Dex** 23, **Con** —, **Int** —, **Wis** 11, **Cha** 1
**Base Atk** +25; **CMB** +41; **CMD** 59 (63 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, Run
**Skills** Fly +10, Perception +8, Swim +22; **Racial Modifiers** +8 Fly, +8 Perception
**SQ** _[[universal monster rules/Heat|heat]]_ management, increased locomotion, steam engine, swift reactions

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** none

##### Description

Though some scholars may argue about who exactly created the first steam-powered clockwork, the secret of their manufacture is now out. Savvy engineers have started to create faster and more powerful clockwork contraptions in the form of marvels blending arcane _heat_ sources with large boilers to create pressured steam that powers the complex constructs.

The _[[monsters/Steam-Powered Clockwork Dragon|steam-powered clockwork dragon]]_ presented here is built using the clockwork dragon. See that entry for full descriptions of its base abilities.
---
cssclass: [monsters]
title1: Thassilonian Sentinel, Iron Sentinel
desc_short: An apelike head with demonic features cast in black iron sits on six segmented
  mechanical legs.
title2: Iron Sentinel
CR: 5
sources:
- name: 'Pathfinder #134: It Came from Hollow Mountain'
  page: 90
  link: http://paizo.com/products/btpy9z14?Pathfinder-Adventure-Path-134-It-Came-from-Hollow-Mountain
XP: 1600
alignment: N
size: Small
type: construct
initiative:
  bonus: 9
senses:
  darkvision: 60
  detect magic: true
  low-light vision: true
AC:
  AC: 19
  touch: 15
  flat_footed: 15
  components:
    dex: 4
    natural: 4
    size: 1
HP:
  HP: 54
  long: 8d10+10
saves:
  fort: 2
  ref: 8
  will: 2
immunities:
- cold
- construct traits
- magic
speeds:
  base: 40
  climb: 20
attacks:
  melee:
  - - text: 2 claws +16 (1d4+6)
      entries:
      - - damage: 1d4+6
      count: 2
      attack: claws
      bonus:
      - 16
  ranged:
  - - text: icy bolt +13 (1d6 cold plus slow)
      entries:
      - - damage: 1d6
          type: cold
        - effect: slow
      attack: icy bolt
      bonus:
      - 13
  special:
  - head-butt +16 (1d4+3)
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
  STR: 22
  DEX: 18
  CON:
  INT: 1
  WIS: 11
  CHA: 5
BAB: 8
CMB: 13
CMD: 27
CMD_other: 35 vs. trip
feats:
- name: Improved Initiative
- name: Lightning Reflexes
- name: Skill Focus (Perception)
- name: Weapon Focus (claws)
skills:
  Acrobatics: 6
  Climb: 16
  Perception: 5
  Stealth: 10
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
  Alert (Su): An iron sentinel can take simple orders and identify intruders, and
    it has the ability to alert its creator or another creature to which it's keyed.
    When an iron sentinel detects a trespasser, it can choose to alert the creature
    to which it's keyed in one of two ways. The sentinel can create a loud sound like
    that of a bell, chime, or gong that can be clearly heard within 500 feet. Alternatively,
    an iron sentinel can send a mental alert to the creature to which it is keyed
    as long as that creature is within 1 mile of the sentinel. The mental alert wakes
    the keyed creature from sleep but doesn't affect normal concentration. An iron
    sentinel's creator is the first creature it is keyed to, and the creator can pass
    its link to another creature as part of a 4-hour ritual that uses materials costing
    500 gp.
  Head-Butt (Ex): Once every 3 rounds, if an iron sentinel hits the same creature
    with both claw attacks, it can also attempt to head-butt that creature. If this
    attack is successful, in addition to the damage, the target is staggered for 1
    round unless it succeeds at a DC 14 Fortitude save. The save DC is Constitution-based.
  Icy Bolt (Su): As a standard action, an iron sentinel can fire a bolt of ice as
    a ranged touch attack out to a maximum range of 30 feet. This bolt deals 1d6 points
    of cold damage. The target is also slowed (as per the spell slow) for 1d6+1 rounds
    (a DC 14 Fortitude save negates this slow effect). The save DC is Constitution-based.
  Immunity to Magic (Ex): An iron sentinel is immune to spells or spell-like abilities
    that allow spell resistance, except for spells with the electricity descriptor.
desc_long: Popular in the more brutish Thassilonian lands of Bakrakhan, Gastash, and
  Haruka, iron sentinels were commonly employed in large platoons to repel organized,
  armed assaults. They most often begin combat with an icy bolt intended to slow advancing
  hostiles, who are then easier targets for the constructs' physical attacks.

---

# Thassilonian Sentinel, Iron Sentinel
An apelike head with demonic features cast in black iron sits on six segmented mechanical legs.
**Source** Pathfinder #134: It Came from Hollow Mountain pg. 90
**XP** 1,600

N Small construct
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +5

##### Defense

**AC** 19, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 Dex, +4 natural, +1 size)
**hp** 54 (8d10+10)
**Fort** +2, **Ref** +8, **Will** +2
**Immune** cold, _[[universal monster rules/Construct Traits|construct traits]]_, magic

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** 2 claws +16 (1d4+6)
**Ranged** icy bolt +13 (1d6 cold plus _[[spells/Slow|slow]]_)
**Special Attacks** head-butt +16 (1d4+3)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 2nd; concentration -1)
Constant—_detect magic_

##### Statistics
**Str** 22, **Dex** 18, **Con** —, **Int** 1, **Wis** 11, **Cha** 5
**Base Atk** +8; **CMB** +13; **CMD** 27 (35 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Weapon Focus|Weapon Focus]]_ (claws)
**Skills** Acrobatics +6, _Climb_ +16, Perception +5, Stealth +10
**Languages** Thassilonian (can’t speak)
**SQ** alert, _[[universal monster rules/Freeze|freeze]]_

##### Ecology

**Environment** any
**Organization** solitary, pair, or troop (3-7)
**Treasure** none

### Special Abilities

**Alert (Su)** An iron sentinel can take simple orders and _[[spells/Identify|identify]]_ intruders, and it has the ability to alert its creator or another creature to which it’s keyed. When an iron sentinel detects a trespasser, it can choose to alert the creature to which it’s keyed in one of two ways. The sentinel can create a loud sound like that of a _[[items/Mundane/Bell|bell]]_, chime, or gong that can be clearly heard within 500 feet. Alternatively, an iron sentinel can send a mental alert to the creature to which it is keyed as long as that creature is within 1 mile of the sentinel. The mental alert wakes the keyed creature from sleep but doesn’t affect normal concentration. An iron sentinel’s creator is the first creature it is keyed to, and the creator can pass its link to another creature as part of a 4-hour ritual that uses materials costing 500 gp.

**Head-Butt (Ex)** Once every 3 rounds, if an iron sentinel hits the same creature with both claw attacks, it can also attempt to head-butt that creature. If this attack is successful, in addition to the damage, the target is _[[conditions/Staggered|staggered]]_ for 1 round unless it succeeds at a DC 14 Fortitude save. The save DC is Constitution-based.

**Icy Bolt (Su)** As a standard action, an iron sentinel can fire a bolt of ice as a ranged touch attack out to a maximum range of 30 feet. This bolt deals 1d6 points of cold damage. The target is also slowed (as per the spell _slow_) for 1d6+1 rounds (a DC 14 Fortitude save negates this _slow_ effect). The save DC is Constitution-based.

**_[[universal monster rules/Immunity|Immunity]]_ to Magic (Ex)** An iron sentinel is immune to spells or _spell-like abilities_ that allow _[[universal monster rules/Spell Resistance|spell resistance]]_, except for spells with the electricity descriptor.

##### Description

Popular in the more brutish Thassilonian lands of Bakrakhan, Gastash, and Haruka, iron sentinels were commonly employed in large platoons to repel organized, armed assaults. They most often begin combat with an icy bolt intended to _slow_ _[[items/Weapon Magic Abilities/Advancing|advancing]]_ hostiles, who are then easier targets for the constructs’ physical attacks.
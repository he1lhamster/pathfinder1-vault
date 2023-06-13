---
cssclass: [monsters]
title1: Demon, Derakni
desc_short: 'The size of a horse, this demonic locust has a scorpion's stinger and
  an almost-human face. Its front legs end in clawed hands. '
title2: Derakni
CR: 10
sources:
- name: The Worldwound
  page: 43
  link: http://paizo.com/products/btpy8yvk?Pathfinder-Campaign-Setting-The-Worldwound
XP: 9600
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 10
senses:
  darkvision: 60
  scent: true
AC:
  AC: 25
  touch: 15
  flat_footed: 19
  components:
    dex: 6
    natural: 10
    size: -1
HP:
  HP: 126
  long: 11d10+66
saves:
  fort: 13
  ref: 13
  will: 8
DR:
- amount: 10
  weakness: good
immunities:
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 21
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +18 (1d4+8 plus poison)
      entries:
      - - damage: 1d4+8
        - effect: poison
      attack: bite
      bonus:
      - 18
    - text: 2 claws +18 (1d4+8)
      entries:
      - - damage: 1d4+8
      count: 2
      attack: claws
      bonus:
      - 18
    - text: sting +18 (1d8+8/19-20 plus poison)
      entries:
      - - damage: 1d8+8
          crit_range: 19-20
        - effect: poison
      attack: sting
      bonus:
      - 18
  special:
  - drone
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: contagion
    source: default
    freq: At will
    DC: 17
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: gust of wind
    source: default
    freq: At will
  - name: enervation
    source: default
    freq: 3/day
  - name: quickened summon swarm
    source: default
    freq: 3/day
  - name: insect plague
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: derakni
      amount: 1
    - name: vescavor swarms
      amount: 1d4
      chance: 40%
  sources:
  - name: default
    CL: 12
    concentration: 15
ability_scores:
  STR: 26
  DEX: 23
  CON: 22
  INT: 9
  WIS: 17
  CHA: 16
BAB: 11
CMB: 20
CMD: 36
CMD_other: 44 vs. trip
feats:
- name: Flyby Attack
- name: Improved Critical (sting)
- name: Improved Initiative
- name: Iron Will
- name: Power Attack
- name: Quicken Spell-Like Ability (summon swarm)
skills:
  Acrobatics: 20
  Fly: 22
  Perception: 25
  Stealth: 16
  Survival: 17
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
ecology:
  environment: any (Abyss)
  organization: solitary, pair, or swarm (3-10)
  treasure_type: standard
special_abilities:
  Drone (Su): The sound of a derakni in flight is a mesmerizing, unsettling drone
    that causes confusion in all non-demons who hear the sound. A derakni must fly
    at least 10 feet to activate this ability (which it can do as a free action as
    part of its move action). Any non-demon creature that begins its turn within 30
    feet of a derakni that moved in this manner on its previous turn must succeed
    at a DC 18 Will save or become confused for 1d4 rounds. A creature that makes
    this save is immune to the drone of that derakni for 24 hours. Demons are immune
    to this sonic, mind-affecting effect. The save DC is Charisma-based.
  Poison (Ex): Bite or sting-injury; save Fort DC 21; frequency 1/ round for 6 rounds;
    effect 1d4 Con; cure 2 consecutive saves. The save DC is Constitution-based.
desc_long: |-
  Deraknis, also known as locust demons, are among Deskari's favorite minions, both in the Abyss and in the Worldwound. Great flights of these creatures plague the skies above the Wounded Lands in particular, but they can be encountered anywhere in the Worldwound. These creatures' leering humanoid visages are armored with chitinous plates, and their front feet end in small claws that look strangely like human hands. A derakni can use these hands to manipulate objects or wield items, but generally eschews using weapons or shields entirely. 

  Often, deraknis are encountered in the vicinity of hives of vescavors (Pathfinder Campaign Setting: Lost Kingdoms 50). Indeed, vescavor swarms eagerly serve deraknis as minions, and, save for truly unusual circumstances, a derakni never needs to worry about taking damage from or being distracted by a vescavor swarm that shares its space. Deraknis typically aid in the devastation of large regions, often in preparation for the advance of larger demonic armies, and the Worldwound is one of their crowning glories. 

  A derakni is 14 feet long and weighs 1,200 pounds. These wretched demons arise from the souls of those who, in life, purposefully engineered disasters or aided in their development-particularly souls whose disasters resulted in mass famines or droughts.

---

# Demon, Derakni
The size of a _[[monsters/Horse|horse]]_, this demonic locust has a scorpion’s stinger
and an almost-human face. Its front legs end in clawed hands.

**Source** The Worldwound pg. 43
**XP** 9,600
CE Large outsider (chaotic, demon, evil, extraplanar)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +25

##### Defense

**AC** 25, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+6 Dex, +10 natural, –1 size)
**hp** 126 (11d10+66)
**Fort** +13, **Ref** +13, **Will** +8
**DR** 10/good; **Immune** electricity, poison; **Resist** acid 10, cold 10,
fire 10; **SR** 21

##### Offense
**Speed** 30 ft., fly 60 ft. (good)
**Melee** bite +18 (1d4+8 plus poison), 2 claws +18 (1d4+8),
sting +18 (1d8+8/19–20 plus poison)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** drone
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +15)
At will—_[[spells/Contagion|contagion]]_ (DC 17), greater teleport (self plus 50 lbs.
of objects only), _[[spells/Gust Of Wind|gust of wind]]_
3/day—_[[spells/Enervation|enervation]]_, quickened
_[[spells/Summon Swarm|summon swarm]]_
1/day—_[[spells/Insect Plague|insect plague]]_, _[[universal monster rules/Summon|summon]]_ (level 4,
 1 derakni or 1d4 vescavor swarms 40%)

##### Statistics
**Str** 26, **Dex** 23, **Con** 22, **Int** 9, **Wis** 17, **Cha** 16
**Base Atk** +11; **CMB** +20; **CMD** 36 (44 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Critical|Improved Critical]]_ (sting), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_summon swarm_)
**Skills** Acrobatics +20, Fly +22, Perception +25,
Stealth +16, Survival +17; **Racial Modifiers** +8 Perception
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abyss)
**Organization** solitary, pair, or swarm (3–10)
**Treasure** standard

### Special Abilities

**Drone (Su)** The sound of a derakni in _[[universal monster rules/Flight|flight]]_ is a mesmerizing,
unsettling drone that causes _[[spells/Confusion|confusion]]_ in all non-demons who
hear the sound. A derakni must fly at least 10 feet to activate
this ability (which it can do as a free action as part of its move
action). Any non-demon creature that begins its turn within 30
feet of a derakni that moved in this manner on its previous turn
must succeed at a DC 18 Will save or become _[[conditions/Confused|confused]]_ for 1d4
rounds. A creature that makes this save is immune to the drone
of that derakni for 24 hours. Demons are immune to this sonic,
mind-affecting effect. The save DC is Charisma-based.

**Poison (Ex)** Bite or sting—injury; save Fort DC 21; frequency 1/
round for 6 rounds; effect 1d4 Con; cure 2 consecutive saves.
The save DC is Constitution-based.

##### Description

Deraknis, also known as locust demons, are among Deskari’s
favorite minions, both in the Abyss and in the Worldwound.
Great flights of these creatures plague the skies above the
Wounded Lands in particular, but they can be encountered
anywhere in the Worldwound. These creatures’ leering
humanoid visages are armored with chitinous plates, and
their front feet end in small claws that look strangely like
human hands. A derakni can use these hands to manipulate
objects or wield items, but generally eschews using weapons
or shields entirely.

Often, deraknis are encountered in the vicinity of hives
of vescavors (Pathfinder Campaign Setting: Lost Kingdoms 50).
Indeed, vescavor swarms eagerly serve deraknis as minions,
and, save for truly unusual circumstances, a derakni never
needs to worry about taking damage from or being distracted
by a _[[monsters/Vescavor Swarm|vescavor swarm]]_ that shares its space. Deraknis typically
aid in the devastation of large regions, often in preparation for
the advance of larger demonic armies, and the Worldwound
is one of their crowning glories.

A derakni is 14 feet long and weighs 1,200 pounds. These
wretched demons arise from the souls of those who, in life,
purposefully engineered disasters or aided in their
development—particularly souls whose disasters
resulted in mass famines or droughts.
---
cssclass: [monsters]
second_statblock: true
title1: Ghoul, Ghoul Huntsmaster
title2: Ghoul Huntsmaster
CR: 7
sources:
- name: Monster Codex
  page: 83
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 3200
race: Ghoul
classes:
- ranger 6
alignment: CE
size: Medium
type: undead
initiative:
  bonus: 5
senses:
  darkvision: 60
AC:
  AC: 20
  touch: 15
  flat_footed: 15
  components:
    armor: 3
    dex: 5
    natural: 2
HP:
  HP: 80
  long: 2d8+6d10+38
  HD: 8
saves:
  fort: 9
  ref: 10
  will: 8
defensive_abilities:
- channel resistance +2
immunities:
- undead traits
speeds:
  base: 40
attacks:
  melee:
  - - text: +1 bite +13 (1d6+3 plus disease and paralysis)
      entries:
      - - damage: 1d6+3
        - effect: disease
        - effect: paralysis
      attack: +1 bite
      bonus:
      - 13
    - text: 2 +1 claws +14 (1d8+3 plus paralysis)
      entries:
      - - damage: 1d8+3
        - effect: paralysis
      count: 2
      attack: +1 claws
      bonus:
      - 14
  ranged:
  - - text: mwk composite longbow +13/+8 (1d8+2/×3)
      entries:
      - - damage: 1d8+2
          crit_multiplier: 3
      attack: mwk composite longbow
      bonus:
      - 13
      - 8
  special:
  - combat style (archery)
  - disease (DC 15)
  - favored enemy (elves +2, humans +4)
  - paralysis (1d4+1 rounds, DC 15, elves are immune to this effect)
spells:
  entries:
  - name: longstrider
    source: Ranger
    level: 1
  - name: magic fang
    source: Ranger
    level: 1
  sources:
  - name: Ranger
    type: prepared
    CL: 3
    concentration: 6
tactics:
  Before Combat: The huntsmaster casts longstrider and uses his wand of greater magic
    fang on himself as well as on his animal companion.
  Base Statistics: Without longstrider and greater magic fang, the huntsmaster's statistics
    are Speed 30 ft.; Melee bite +12 (1d6+2 plus disease and paralysis), 2 claws +13
    (1d8+2 plus paralysis).
ability_scores:
  STR: 15
  DEX: 20
  CON:
  INT: 13
  WIS: 16
  CHA: 18
BAB: 7
CMB: 9
CMD: 24
feats:
- name: Corpse Companion
- name: Endurance
- name: Improved Natural Attack (claw)
- name: Point-Blank Shot
- name: Rapid Shot
- name: Weapon Finesse
- name: Weapon Focus (claw)
skills:
  Acrobatics: 13
    when jumping: 17
  Climb: 13
  Disable Device: 13
  Perception: 14
  Stealth: 16
  Survival: 14
  Swim: 9
languages:
- Common
- Undercommon
special_qualities:
- favored terrain (underground +2)
- hunter's bond (animal)
- track +3
- wild empathy +10
gear:
  combat:
  - +1 human-bane arrows (3)
  - +1 seeking arrows (2)
  - potion of inflict moderate wounds
  - wand of greater magic fang (12 charges)
  other:
  - mwk studded leather
  - mwk composite longbow with 50 arrows
  - 42 gp
ecology:
  environment: any land
desc_long: ''

---

# Ghoul, Ghoul Huntsmaster

**Source** Monster Codex pg. 83
**XP** 3,200
_[[monsters/Ghoul|Ghoul]]_ _[[classes/Ranger|ranger]]_ 6
CE Medium undead
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +14

##### Defense

**AC** 20, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+3 armor, +5 Dex, +2 natural)
**hp** 80 (8 HD; 2d8+6d10+38)
**Fort** +9, **Ref** +10, **Will** +8
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +2; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 40 ft.
**Melee** +1 bite +13 (1d6+3 plus disease and _[[universal monster rules/Paralysis|paralysis]]_), 2 +1 claws +14 (1d8+3 plus _paralysis_)
**Ranged** mwk _[[items/Weapon/Composite longbow|composite longbow]]_ +13/+8 (1d8+2/×3)
**Special Attacks** combat style (archery), disease (DC 15), favored enemy (elves +2, humans +4), _paralysis_ (1d4+1 rounds, DC 15, elves are immune to this effect)
**_Ranger_ Spells Prepared **(CL 3rd; concentration +6)
1st—_[[spells/Longstrider|longstrider]]_, _[[spells/Magic Fang|magic fang]]_

### Tactics

**Before Combat** The huntsmaster casts _longstrider_ and uses his wand of greater _magic fang_ on himself as well as on his animal companion.
 **Base Statistics** Without _longstrider_ and greater _magic fang_, the huntsmaster’s statistics are **Speed** 30 ft.; **Melee** bite +12 (1d6+2 plus disease and _paralysis_), 2 claws +13 (1d8+2 plus _paralysis_).

##### Statistics
**Str** 15, **Dex** 20, **Con** —, **Int** 13, **Wis** 16, **Cha** 18
**Base Atk** +7; **CMB** +9; **CMD** 24
**Feats** _[[feats/Corpse Companion|Corpse Companion]]_, _[[feats/Endurance|Endurance]]_, _[[feats/Improved Natural Attack|Improved Natural Attack]]_ (claw), _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Acrobatics +13 (+17 when jumping), _[[universal monster rules/Climb|Climb]]_ +13, Disable Device +13, Perception +14, Stealth +16, Survival +14, Swim +9
**Languages** Common, Undercommon
**SQ** favored terrain (underground +2), _[[classes/Hunter|hunter]]_’s bond (animal), track +3, wild _[[feats/Empathy|empathy]]_ +10
**Combat Gear** +1 human-bane arrows (3), +1 seeking arrows (2), potion of _[[spells/Inflict Moderate Wounds|inflict moderate wounds]]_, wand of greater _magic fang_ (12 charges); **Other Gear** mwk studded leather, mwk _composite longbow_ with 50 arrows, 42 gp

##### Ecology

**Environment** any land

##### Description

## Corpse Cat


N Small undead
 **Init **+6; **Senses **_darkvision_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +5

##### Defense

**AC **20, touch 17, _flat-footed_ 14 (+6 Dex, +3 natural, +1 size)
 **hp **16 (3d8+3)
 **Fort **+4, **Ref **+9, **Will **+2
 **Immune **_undead traits_

##### Offense
**Speed **50 ft.
 **Melee **+1 bite +10 (1d4+2 plus _[[universal monster rules/Trip|trip]]_), 2 +1 claws +11 (1d2+2)

### Tactics

**Base Statistics** Without greater _magic fang_, the cat’s statistics are **Melee **bite +9 (1d4+1 plus _trip_), 2 claws +10 (1d2+1).

##### Statistics
**Str **13, **Dex **22, **Con **-, **Int **2, **Wis **12, **Cha **12
 **Base Atk** +2; **CMB **+2; **CMD **18 (22 vs. _trip_)
 **Feats **_Weapon Finesse_, _Weapon Focus_ (claw)
 **Skills **Acrobatics +10 (+18 when jumping), Perception +5, Stealth +14
 **SQ **tricks (attack [all creatures], come, fetch, _[[npcs/Guard|guard]]_, seek, stay, track)

Though most ghouls hunt and kill to satiate their hunger, a huntsmaster relishes the chase as much as the feast after.
---
cssclass: [monsters]
title1: Giant (Fire), Fire Giant King
title2: Fire Giant King
CR: 20
sources:
- name: Monster Codex
  page: 63
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 307200
race: Fire
classes:
- giant ranger 10
alignment: LE
size: Large
type: humanoid
subtypes:
- fire
- giant
initiative:
  bonus: 2
senses:
  low-light vision: true
AC:
  AC: 34
  touch: 10
  flat_footed: 34
  components:
    armor: 11
    deflection: 3
    dex: -2
    natural: 13
    size: -1
HP:
  HP: 382
  long: 15d8+10d10+260
  HD: 25
saves:
  fort: 26
  ref: 10
  will: 14
defensive_abilities:
- evasion
- rock catching
immunities:
- fire
weaknesses:
- vulnerable to cold
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 brilliant energy greatsword +36/+31/+26/+21 (3d6+22/17-20)
      entries:
      - - damage: 3d6+22
          crit_range: 17-20
      attack: +1 brilliant energy greatsword
      bonus:
      - 36
      - 31
      - 26
      - 21
  - - text: 2 slams +34 (1d8+14)
      entries:
      - - damage: 1d8+14
      count: 2
      attack: slams
      bonus:
      - 34
  ranged:
  - - text: rock +19 (1d8+21 plus 1d6 fire)
      entries:
      - - damage: 1d8+21
        - damage: 1d6
          type: fire
      attack: rock
      bonus:
      - 19
  special:
  - combat style (two-handed weapon)
  - favored enemy (animals +2, dragons +4, dwarves +4)
  - heated rock
  - rock throwing (120 ft.)
space: 10
reach: 10
spells:
  entries:
  - name: cure moderate wounds
    source: Ranger
    level: 3
  - superscripts:
    - APG
    name: aspect of the bear
    source: Ranger
    level: 2
  - name: spike growth
    source: Ranger
    level: 2
    DC: 16
  - name: entangle
    source: Ranger
    level: 1
    DC: 15
  - name: longstrider
    source: Ranger
    level: 1
  - name: resist energy
    source: Ranger
    level: 1
  sources:
  - name: Ranger
    type: prepared
    CL: 7
    concentration: 11
tactics:
  Before Combat: The fire giant king casts aspect of the bear and longstrider.
  During Combat: The king typically leads his warriors into battle, supporting his
    troops and tearing through his enemies.
  Base Statistics: Without aspect of the bear and longstrider, the fire giant king's
    statistics are AC 32, touch 10, flat-footed 32, Speed 30 ft.; CMB +36 (+38 bull
    rush, +38 overrun, +38 sunder)
ability_scores:
  STR: 39
  DEX: 7
  CON: 30
  INT: 13
  WIS: 18
  CHA: 14
BAB: 21
CMB: 38
CMB_other: +40 bull rush, +40 overrun, +40 sunder
CMD: 47
CMD_other: 49 vs. bull rush, 49 vs. overrun, 49 vs. sunder
feats:
- name: Cleave
- name: Endurance
- name: Great Cleave
- name: Improved Bull Rush
- name: Improved Critical (greatsword)
- name: Improved Initiative
- name: Improved Natural Armor
- name: Improved Overrun
- name: Improved Sunder
- name: Iron Will
- name: Power Attack
- name: Skill Focus (Perception)
- name: Vital Strike
- name: Weapon Focus (greatsword)
skills:
  Climb: 28
  Craft (armor): 9
  Intimidate: 30
  Knowledge (geography): 14
  Knowledge (nobility): 11
  Perception: 38
  Spellcraft: 17
  Stealth: 7
languages:
- Common
- Giant
special_qualities:
- favored terrain (mountain +4, underground +2)
- hunter's bond (companions)
- swift tracker
- track +5
- wild empathy +12
- woodland stride
gear:
  combat:
  - boots of speed
  - potions of cure serious wounds (2)
  other:
  - +5 breastplate
  - +1 brilliant energy greatsword
  - amulet of natural armor +2
  - belt of physical might +4 (Str, Con)
  - headband of mental superiority +2
  - ring of protection +3
ecology:
  environment: warm mountains
desc_long: Fire giant kings rule over their volcanic dominions with a cruel and heavy
  hand. Most kings seek the hand of a queen to reign beside them, both to secure their
  own power and to provide heirs to accede to their thrones when they inevitably fall
  in battle. A fire giant king must always watch his back, however, for there are
  always claimants eager to seize his position.

---

# Giant (Fire), Fire Giant King

**Source** Monster Codex pg. 63
**XP** 307,200
Fire giant _[[classes/Ranger|ranger]]_ 10

LE Large humanoid (fire, giant)
**Init** +2; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +38

##### Defense

**AC** 34, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 34 (+11 armor, +3 deflection, –2 Dex, +13 natural, –1 size)
**hp** 382 (25 HD; 15d8+10d10+260)
**Fort** +26, **Ref** +10, **Will** +14
**Defensive Abilities** evasion, _[[universal monster rules/Rock Catching|rock catching]]_; **Immune** fire
**Weaknesses** vulnerable to cold

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon Magic Abilities/Brilliant Energy|brilliant energy]]_ _[[items/Weapon/Greatsword|greatsword]]_ +36/+31/+26/+21 (3d6+22/17–20) or 2 slams +34 (1d8+14)
**Ranged** rock +19 (1d8+21 plus 1d6 fire)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** combat style (two-handed weapon), favored enemy (animals +2, dragons +4, dwarves +4), heated rock, _[[universal monster rules/Rock Throwing|rock throwing]]_ (120 ft.)
**_Ranger_ Spells Prepared **(CL 7th; concentration +11)
3rd—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_
2nd—_[[spells/Aspect of the Bear|aspect of the bear]]_, _[[spells/Spike Growth|spike growth]]_ (DC 16)
1st—_[[spells/Entangle|entangle]]_ (DC 15), _[[spells/Longstrider|longstrider]]_, _[[spells/Resist Energy|resist energy]]_

### Tactics

**Before Combat** The fire giant _[[npcs/King|king]]_ casts _aspect of the bear_ and _longstrider_.
 **During Combat** The _king_ typically leads his warriors into battle, supporting his troops and tearing through his enemies.
 **Base Statistics** Without _aspect of the bear_ and _longstrider_, the fire giant _king_’s statistics are **AC** 32, touch 10, _flat-footed_ 32, **Speed** 30 ft.; **CMB** +36 (+38 bull rush, +38 overrun, +38 sunder)

##### Statistics
**Str** 39, **Dex** 7, **Con** 30, **Int** 13, **Wis** 18, **Cha** 14
**Base Atk** +21; **CMB** +38 (+40 bull rush, +40 overrun, +40 sunder); **CMD** 47 (49 vs. bull rush, 49 vs. overrun, 49 vs. sunder)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Endurance|Endurance]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (_greatsword_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Natural Armor|Improved Natural Armor]]_, _[[feats/Improved Overrun|Improved Overrun]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_greatsword_)
**Skills** _[[universal monster rules/Climb|Climb]]_ +28, Craft (armor) +9, Intimidate +30, Knowledge (geography) +14, Knowledge (nobility) +11, Perception +38, Spellcraft +17, Stealth +7
**Languages** Common, Giant
**SQ** favored terrain (mountain +4, underground +2), _[[classes/Hunter|hunter]]_’s bond (companions), swift tracker, track +5, wild _[[feats/Empathy|empathy]]_ +12, woodland stride
**Combat Gear** _[[items/Wondrous Item/Boots of Speed|boots of speed]]_, potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2); **Other Gear** +5 _[[items/Armor/Breastplate|breastplate]]_, +1 _brilliant energy_ _greatsword_, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Belt of Physical Might +4|belt of physical might +4]]_ (Str, Con), _[[items/Wondrous Item/Headband of Mental Superiority +2|headband of mental superiority +2]]_, _[[items/Ring/Ring of Protection +3|ring of protection +3]]_

##### Ecology

**Environment** warm mountains

##### Description

Fire giant kings rule over their _[[items/Armor Magic Abilities/Volcanic|volcanic]]_ dominions with a _[[items/Weapon Magic Abilities/Cruel|cruel]]_ and heavy hand. Most kings seek the hand of a queen to reign beside them, both to secure their own power and to provide heirs to accede to their thrones when they inevitably fall in battle. A fire giant _king_ must always watch his back, however, for there are always claimants eager to seize his position.
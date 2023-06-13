---
cssclass: [monsters]
title1: Sard
desc_short: This wriggling and leafless tree moves on spidery legs. Flickering motes
  of blood-red lightning dance in the cracks of its bark.
title2: Sard
CR: 19
sources:
- name: Bestiary 2
  page: 237
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 204800
alignment: CE
size: Colossal
type: plant
initiative:
  bonus: 8
senses:
  blindsight: 30
  darkvision: 60
  low-light vision: true
  tremorsense: 30
AC:
  AC: 34
  touch: 10
  flat_footed: 26
  components:
    dex: 8
    natural: 24
    size: -8
HP:
  HP: 333
  long: 23d8+230
  fast_healing: 10
saves:
  fort: 23
  ref: 17
  will: 13
defensive_abilities:
- death throes
- electrical jolt
DR:
- amount: 15
  weakness: cold iron and slashing
immunities:
- electricity
- plant traits
resistances:
  cold: 30
  fire: 30
SR: 30
weaknesses:
- vulnerable to sonic
speeds:
  base: 50
  climb: 30
attacks:
  melee:
  - - text: 2 slams +25 (4d10+16/19-20 plus 4d6 electricity)
      entries:
      - - damage: 4d10+16
          crit_range: 19-20
        - damage: 4d6
          type: electricity
      count: 2
      attack: slams
      bonus:
      - 25
  ranged:
  - - text: 4 thorns +17 (2d8+16 plus poison)
      entries:
      - - damage: 2d8+16
        - effect: poison
      count: 4
      attack: thorns
      bonus:
      - 17
space: 30
reach: 30
spell_like_abilities:
  entries:
  - name: control weather
    source: default
    freq: At will
  - name: lightning bolt
    source: default
    freq: At will
    DC: 20
  - name: tree shape
    source: default
    freq: At will
    other: Colossal tree
  - name: transport via plants
    source: default
    freq: At will
  - name: chain lightning
    source: default
    freq: 3/day
    DC: 23
  - name: quickened lightning bolt
    source: default
    freq: 3/day
    DC: 20
  - name: storm of vengeance
    source: default
    freq: 1/day
    DC: 26
  - name: whirlwind
    source: default
    freq: 1/day
    DC: 25
  sources:
  - name: default
    CL: 20
    concentration: 27
ability_scores:
  STR: 42
  DEX: 27
  CON: 30
  INT: 9
  WIS: 22
  CHA: 25
BAB: 17
CMB: 41
CMD: 59
CMD_other: 67 vs. trip
feats:
- name: Awesome Blow
- name: Improved Bull Rush
- name: Improved Critical (slam)
- name: Improved Lightning Reflexes
- name: Improved Precise Shot
- name: Improved Sunder
- name: Lightning Reflexes
- name: Point-Blank Shot
- name: Power Attack
- name: Precise Shot
- name: Quicken Spell-Like Ability (lightning bolt)
- name: Vital Strike
skills:
  Climb: 24
  Perception: 32
languages:
- Aklo
- Sylvan
special_qualities:
- planar acclimation
ecology:
  environment: any forests
  organization: solitary
  treasure_type: triple
special_abilities:
  Death Throes (Su): When a sard dies, its remains explode with a blast of lightning
    into razor-sharp splinters of wood. All creatures within 30 feet of a sard when
    it explodes in this manner take 12d6 points of electricity damage and 12d6 points
    of piercing damage. A DC 31 Reflex save halves this damage. The save DC is Constitution-based.
  Electrical Jolt (Su): Every time a creature strikes a sard with a metal melee weapon,
    arcs of electricity deal 1d10 points of damage to the attacker.
  Planar Acclimation (Ex): A sard is always considered to be on its home plane, regardless
    of what plane it finds itself upon. It never gains the extraplanar subtype.
  Poison (Ex): Thorn-injury; save Fort DC 31; frequency 1/round for 6 rounds; effect
    1d2 Dex and 4d6 electricity; cure 2 consecutive saves.
  Thorns (Ex): A sard's thorns have a range of 180 feet with no range increment.
desc_long: |-
  The sard is an ancient elm, oak, or pine tree that has been infused with lightning and raw life by one of the strange gods of the fey realm. One of the legendary beasts known as the Tane, a sard has “sap” that consists of red lightning-all of the sard's electrical attacks manifest with this same eerie-colored energy.

  A sard can pass for an old dead tree-especially when the creature uses its tree shape spell-like ability. Yet despite its enormous size and ungainly shape, the sard is in fact a swift and agile monster. It can move with unsettling grace and speed, crawling across the ground on long spidery roots like an immense insect. It attacks either with a single slam of its immense trunk or by launching volleys of foot-long thorns that inject the creature's poisonous, electrified sap.

  Sards are nearly as intelligent as most humans, but few actually use this intelligence for productive purposes-the first sards were created as a form of living siege engine, and they quite enjoy this destructive role, often seeking out fortresses or even towns to systematically destroy.

---

# Sard
This wriggling and leafless tree moves on spidery legs. Flickering motes of blood-red lightning dance in the cracks of its bark.
**Source** Bestiary 2 pg. 237
**XP** 204,800
CE Colossal plant
**Init** +8; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 30 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 30 ft.; Perception +32

##### Defense

**AC** 34, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+8 Dex, +24 natural, –8 size)
**hp** 333 (23d8+230); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +23, **Ref** +17, **Will** +13
**Defensive Abilities** death throes, electrical _[[spells/Jolt|jolt]]_; **DR** 15/cold iron and slashing; **Immune** electricity, _[[universal monster rules/Plant Traits|plant traits]]_; **Resist** cold 30, fire 30; **SR** 30
**Weaknesses** vulnerable to sonic

##### Offense
**Speed** 50 ft., _[[universal monster rules/Climb|climb]]_ 30 ft.
**Melee** 2 slams +25 (4d10+16/19–20 plus 4d6 electricity)
**Ranged** 4 thorns +17 (2d8+16 plus poison)
**Space** 30 ft., **Reach** 30 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +27)
At will—_[[spells/Control Weather|control weather]]_, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 20), _[[spells/Tree Shape|tree shape]]_ (Colossal tree), _[[spells/Transport via Plants|transport via plants]]_
3/day—_[[spells/Chain Lightning|chain lightning]]_ (DC 23), quickened _lightning bolt_ (DC 20)
1/day—_[[spells/Storm Of Vengeance|storm of vengeance]]_ (DC 26), _[[universal monster rules/Whirlwind|whirlwind]]_ (DC 25)

##### Statistics
**Str** 42, **Dex** 27, **Con** 30, **Int** 9, **Wis** 22, **Cha** 25
**Base Atk** +17; **CMB** +41; **CMD** 59 (67 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (slam), _[[feats/Improved Lightning Reflexes|Improved Lightning Reflexes]]_, _[[feats/Improved Precise Shot|Improved Precise Shot]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_lightning bolt_), _[[feats/Vital Strike|Vital Strike]]_
**Skills** _Climb_ +24, Perception +32
**Languages** Aklo, Sylvan
**SQ** _[[items/Weapon Magic Abilities/Planar|planar]]_ acclimation

##### Ecology

**Environment** any forests
**Organization** solitary
**Treasure** triple

### Special Abilities

**Death Throes (Su) **When a _[[monsters/Sard|sard]]_ dies, its remains explode with a blast of lightning into razor-sharp splinters of wood. All creatures within 30 feet of a _sard_ when it explodes in this manner take 12d6 points of electricity damage and 12d6 points of piercing damage. A DC 31 Reflex save halves this damage. The save DC is Constitution-based.

**Electrical _Jolt_ (Su)** Every time a creature strikes a _sard_ with a metal melee weapon, arcs of electricity deal 1d10 points of damage to the attacker.

**_Planar_ Acclimation (Ex)** A _sard_ is always considered to be on its home plane, regardless of what plane it finds itself upon. It never gains the extraplanar subtype.

**Poison (Ex)** Thorn—injury; save Fort DC 31; frequency 1/round for 6 rounds; effect 1d2 Dex and 4d6 electricity; cure 2 consecutive saves.

**Thorns (Ex)** A _sard_’s thorns have a range of 180 feet with no range increment.

##### Description

The _sard_ is an ancient elm, oak, or pine tree that has been infused with lightning and raw life by one of the strange gods of the fey realm. One of the legendary beasts known as the Tane, a _sard_ has “_[[items/Weapon/Sap|sap]]_” that consists of red lightning—all of the _sard_’s electrical attacks manifest with this same eerie-colored energy.

A _sard_ can pass for an old dead tree—especially when the creature uses its _tree shape_ spell-like ability. Yet despite its enormous size and ungainly shape, the _sard_ is in fact a swift and _[[items/Weapon Magic Abilities/Agile|agile]]_ monster. It can move with unsettling _[[spells/Grace|grace]]_ and speed, crawling across the ground on long spidery roots like an immense insect. It attacks either with a single slam of its immense trunk or by launching volleys of foot-long thorns that inject the creature’s poisonous, electrified _sap_.

Sards are nearly as intelligent as most humans, but few actually use this intelligence for productive purposes—the first sards were created as a form of living siege engine, and they quite enjoy this destructive role, often seeking out fortresses or even towns to systematically destroy.
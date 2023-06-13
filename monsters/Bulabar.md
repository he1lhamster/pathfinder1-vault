---
cssclass: [monsters]
title1: Bulabar
desc_short: This small blue beetle stands upright on its hindmost legs and wears a
  bandolier full of tools and pouches.
title2: Bulabar
CR: 1
sources:
- name: The First World, Realm of the Fey
  page: 58
  link: http://paizo.com/products/btpy9op9?Pathfinder-Campaign-Setting-The-First-World-Realm-of-the-Fey
XP: 400
alignment: LN
size: Tiny
type: fey
initiative:
  bonus: 1
senses:
  low-light vision: true
AC:
  AC: 16
  touch: 13
  flat_footed: 15
  components:
    dex: 1
    natural: 3
    size: 2
HP:
  HP: 7
  long: 1d6+4
saves:
  fort: 1
  ref: 3
  will: 2
DR:
- amount: 5
  weakness: cold iron
speeds:
  base: 30
  burrow: 10
attacks:
  melee:
  - - text: spear +0 (1d4-2/x3)
      entries:
      - - damage: 1d4-2
          crit_multiplier: 3
      attack: spear
      bonus:
      - 0
  - - text: 2 claws +3 (1d2-2)
      entries:
      - - damage: 1d2-2
      count: 2
      attack: claws
      bonus:
      - 3
  ranged:
  - - text: light crossbow +3 (1d4/19-20)
      entries:
      - - damage: 1d4
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 3
  special:
  - disassemble (DC 12)
space: 2.5
reach: 0
spell_like_abilities:
  entries:
  - name: mending
    source: default
    freq: At will
  sources:
  - name: default
    CL: 1
    concentration: 1
ability_scores:
  STR: 6
  DEX: 13
  CON: 12
  INT: 15
  WIS: 10
  CHA: 11
BAB: 0
CMB: -1
CMD: 7
feats:
- name: Ability Focus (disassemble)
- is_bonus: true
  name: Toughness
- is_bonus: true
  name: Weapon Finesse
skills:
  Appraise: 3
  Climb: 2
  Craft (alchemy): 6
  Disable Device: 10
  Knowledge (engineering): 7
  Perception: 4
  Stealth: 13
  Use Magic Device: 4
  _racial_mods:
    Disable Device:
      _: 8
    Knowledge (engineering):
      _: 4
languages:
- Common
- First Speech
- Gnome
ecology:
  environment: any (First World)
  organization: solitary, pair, or team (3-10)
  treasure_type: standard
  treasure:
  - light crossbow with 20 bolts
  - spear
special_abilities:
  Disassemble (Ex): As a standard action that does not provoke an attack of opportunity,
    a bulabar can touch a nonmagical object no more than one size category larger
    than itself, forcing either it or its wielder to attempt a DC 12 Reflex saving
    throw. On a failed save, the object is reduced to 1 hit point and gains the broken
    condition. Using this ability on an already broken object has no effect. The save
    DC is Charisma-based and includes a +2 racial bonus.
desc_long: |-
  Bulabars are the tinkers of the First World, thought to personify the evolution of tool use in nature. Fascinated by mechanical devices of all sorts, they frequently wander the landscape looking for novel ideas, or else set up schools and laboratories where they can research their findings and uncover new ways for machines to better their lives. While other races sometimes resent the bulabars' tendency to disassemble or prod curiously at any device they don't understand-including those owned by strangers- bulabars' good-natured penchant for teaching others, as well as fixing broken items for the sheer joy of it, makes them welcome in most settlements.

   The main exception to bulabars' happy-go-lucky attitude is gremlins. Bulabars despise the problematic fey, especially the machine-destroying vexgits (Pathfinder RPG Bestiary 2 145), and attempt to exterminate them whenever possible. This racial hatred is only compounded by the fact that many scholars from other races believe that bulabars may be related to gremlins themselves, an insult that's caused more than one academic gathering to devolve into an unscholarly brawl.

   Though they have an uncanny ability to target the weak points of their enemies' weapons and armor, bulabars hate seeing a useful mechanism broken, and are quick to repair any damaged items as soon as hostilities have ended. More often, bulabars prefer to attack from afar with ranged weapons or alchemical items they can throw-the more unusual, the better- and those bulabars with the opportunity to study alchemists, gunslingers, and other such adventurers often take levels in those classes themselves.

   The average bulabar is 2 feet tall and weighs 20 pounds. Most bulabars can't bear to be parted from their tools and instruments for even a short time, and can usually be found wearing bandoliers, backpacks, and utility belts crammed with useful devices and spare parts.

---

# Bulabar
This small blue beetle stands upright on its hindmost legs and wears a _[[items/Mundane/Bandolier|bandolier]]_ full of tools and pouches.
**Source** The First World, Realm of the Fey pg. 58
**XP** 400

LN Tiny fey
**Init** +1; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +4

##### Defense

**AC** 16, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+1 Dex, +3 natural, +2 size)
**hp** 7 (1d6+4)
**Fort** +1, **Ref** +3, **Will** +2
**DR** 5/cold iron

##### Offense
**Speed** 30 ft., _[[universal monster rules/Burrow|burrow]]_ 10 ft.
**Melee** _[[items/Weapon/Spear|spear]]_ +0 (1d4-2/x3) or 
 2 claws +3 (1d2-2)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +3 (1d4/19-20)
**Space** 2-1/2 ft., **Reach** 0 ft.
**Special Attacks** disassemble (DC 12)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 1st; concentration +1)
At will—_[[spells/Mending|mending]]_

##### Statistics
**Str** 6, **Dex** 13, **Con** 12, **Int** 15, **Wis** 10, **Cha** 11
**Base Atk** +0; **CMB** -1; **CMD** 7
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (disassemble), _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Appraise +3, _[[universal monster rules/Climb|Climb]]_ +2, Craft (alchemy) +6, Disable Device +10, Knowledge (engineering) +7, Perception +4, Stealth +13, Use Magic Device +4; **Racial Modifiers** +8 Disable Device, +4 Knowledge (engineering)
**Languages** Common, First Speech, Gnome

##### Ecology

**Environment** any (First World)
**Organization** solitary, pair, or team (3-10)
**Treasure** standard (_light crossbow_ with 20 bolts, _spear_)

### Special Abilities

**Disassemble (Ex)** As a standard action that does not provoke an attack of opportunity, a _[[monsters/Bulabar|bulabar]]_ can touch a nonmagical object no more than one size category larger than itself, forcing either it or its wielder to attempt a DC 12 Reflex saving throw. On a failed save, the object is reduced to 1 hit point and gains the _[[conditions/Broken|broken]]_ condition. Using this ability on an already _broken_ object has no effect. The save DC is Charisma-based and includes a +2 racial bonus.

##### Description

Bulabars are the tinkers of the First World, thought to personify the evolution of tool use in nature. _[[conditions/Fascinated|Fascinated]]_ by mechanical devices of all sorts, they frequently wander the landscape looking for novel ideas, or else set up schools and laboratories where they can research their findings and uncover new ways for machines to better their lives. While other races sometimes resent the bulabars’ tendency to disassemble or prod curiously at any device they don’t understand—including those owned by strangers— bulabars’ good-natured penchant for teaching others, as well as fixing _broken_ items for the sheer joy of it, makes them welcome in most settlements.

The main exception to bulabars’ happy-go-lucky attitude is gremlins. Bulabars despise the problematic fey, especially the machine-destroying vexgits (Pathfinder RPG Bestiary 2 145), and attempt to exterminate them whenever possible. This racial hatred is only compounded by the fact that many scholars from other races believe that bulabars may be related to gremlins themselves, an insult that’s caused more than one academic gathering to devolve into an unscholarly brawl.

Though they have an uncanny ability to target the weak points of their enemies’ weapons and armor, bulabars hate seeing a useful mechanism _broken_, and are quick to repair any damaged items as soon as hostilities have ended. More often, bulabars prefer to attack from afar with ranged weapons or alchemical items they can throw—the more unusual, the better— and those bulabars with the opportunity to study alchemists, gunslingers, and other such adventurers often take levels in those classes themselves.

The average _bulabar_ is 2 feet tall and weighs 20 pounds. Most bulabars can’t bear to be parted from their tools and instruments for even a short time, and can usually be found wearing bandoliers, backpacks, and utility belts crammed with useful devices and spare parts.
---
cssclass: [monsters]
title1: Emerald Automaton
desc_short: An eerie green glow shines through the seams of this mechanical creature's
  armor.
title2: Emerald Automaton
CR: 4
sources:
- name: The Emerald Spire Superdungeon
  page: 154
  link: http://paizo.com/products/btpy8yqx?Pathfinder-Module-The-Emerald-Spire-Superdungeon
XP: 1200
alignment: N
size: Medium
type: construct
initiative:
  bonus: 1
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: electricity
  radius: 5
  DC: 12
AC:
  AC: 17
  touch: 11
  flat_footed: 16
  components:
    dex: 1
    natural: 6
HP:
  HP: 47
  long: 5d10+20
saves:
  fort: 1
  ref: 2
  will: 1
DR:
- amount: 5
  weakness: adamantine
immunities:
- construct traits
weaknesses:
- magic dependent
speeds:
  base: 30
attacks:
  melee:
  - - text: guisarme +10 (2d4+7/×3)
      entries:
      - - damage: 2d4+7
          crit_multiplier: 3
      attack: guisarme
      bonus:
      - 10
  - - text: longsword +10 (1d8+5/19-20)
      entries:
      - - damage: 1d8+5
          crit_range: 19-20
      attack: longsword
      bonus:
      - 10
    - text: slam +5 (1d4+2)
      entries:
      - - damage: 1d4+2
      attack: slam
      bonus:
      - 5
space: 5
reach: 5
reach_other: 10 ft. with guisarme
ability_scores:
  STR: 20
  DEX: 13
  CON:
  INT:
  WIS: 11
  CHA: 1
BAB: 5
CMB: 10
CMB_other: +12 sunder
CMD: 21
CMD_other: 23 vs. sunder
feats:
- is_bonus: true
  name: Improved Sunder
- is_bonus: true
  name: Power Attack
skills: {}
special_qualities:
- proficient
ecology:
  environment: any
  organization: solitary, pair, or squad (3-8)
  treasure_type: incidental
  treasure:
  - guisarme
  - other treasure
special_abilities:
  Electricity Aura (Su): An emerald automaton reduced to half its hit points or fewer
    emits hazardous energy from its damaged magical battery. Any non-construct creature
    that ends its turn within 5 feet of a damaged emerald automaton takes 1d10 points
    of electricity damage (Reflex DC 12 negates). The save DC is Constitution-based.
  Magic Dependent (Su): An emerald automaton is partially powered by magic. When deprived
    of magic, the automaton is affected as if it were exhausted. The automaton's magic
    can be cut off by antimagic, or suppressed by a dispel magic or mage's disjunction
    effect as if it were a magic item.
  Proficient (Ex): An emerald automaton is proficient with all simple and martial
    weapons.
desc_long: |-
  Like other constructs, an emerald automaton is a mindless, unliving machine that exists only to follow the orders of its creator. It is a capable soldier and can wield almost any weapon its creator chooses to provide it, fighting until it or its target is destroyed.

  In combat, emerald automatons often wield polearms and make use of their reach. When multiple automatons are fighting together, it's common for one to sunder a target's shield or weapon and the rest to gang up against the target. Getting inside the reach of an emerald automaton is no guarantee of safety-the constructs are quite strong, and can strike with a powerful slam attack at need. When badly damaged, an emerald automaton begins to emit crackling green sparks of electricity that can severely shock nearby creatures.

---

# Emerald Automaton
An eerie green glow shines through the seams of this mechanical creature’s armor.
**Source** The Emerald Spire Superdungeon pg. 154
**XP** 1,200

N Medium construct
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +0
**Aura** electricity (5 ft., DC 12)

##### Defense

**AC** 17, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+1 Dex, +6 natural)
**hp** 47 (5d10+20)
**Fort** +1, **Ref** +2, **Will** +1
**DR** 5/adamantine; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_
**Weaknesses** magic dependent

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Guisarme|guisarme]]_ +10 (2d4+7/×3) or _[[items/Weapon/Longsword|longsword]]_ +10 (1d8+5/19–20), slam +5 (1d4+2)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with _guisarme_)

##### Statistics
**Str** 20, **Dex** 13, **Con** —, **Int** —, **Wis** 11, **Cha** 1
**Base Atk** +5; **CMB** +10 (+12 sunder); **CMD** 21 (23 vs. sunder)
**Feats** _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Power Attack|Power Attack]]_
**SQ** proficient

##### Ecology

**Environment** any
**Organization** solitary, pair, or squad (3–8)
**Treasure** incidental (_guisarme_, other treasure)

### Special Abilities

**Electricity Aura (Su)** An _[[monsters/Emerald Automaton|emerald automaton]]_ reduced to half its hit points or fewer emits hazardous energy from its damaged magical battery. Any non-construct creature that ends its turn within 5 feet of a damaged _emerald automaton_ takes 1d10 points of electricity damage (Reflex DC 12 negates). The save DC is Constitution-based.

**Magic Dependent (Su)** An _emerald automaton_ is partially powered by magic. When deprived of magic, the automaton is affected as if it were _[[conditions/Exhausted|exhausted]]_. The automaton’s magic can be cut off by antimagic, or suppressed by a _[[spells/Dispel Magic|dispel magic]]_ or mage’s disjunction effect as if it were a magic item.

**Proficient (Ex)** An _emerald automaton_ is proficient with all simple and martial weapons.

##### Description

Like other constructs, an _emerald automaton_ is a mindless, unliving machine that exists only to follow the orders of its creator. It is a capable soldier and can wield almost any weapon its creator chooses to provide it, fighting until it or its target is destroyed.

In combat, emerald automatons often wield polearms and make use of their reach. When multiple automatons are fighting together, it’s common for one to sunder a target’s _[[spells/Shield|shield]]_ or weapon and the rest to _[[feats/Gang Up|gang up]]_ against the target. Getting inside the reach of an _emerald automaton_ is no guarantee of safety—the constructs are quite strong, and can strike with a powerful slam attack at need. When badly damaged, an _emerald automaton_ begins to emit crackling green sparks of electricity that can severely _[[items/Weapon Magic Abilities/Shock|shock]]_ nearby creatures.
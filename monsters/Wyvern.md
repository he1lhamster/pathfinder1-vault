---
cssclass: [monsters]
title1: Wyvern
desc_short: This serpentine dragon has huge wings, two taloned legs, and a tail stinger,
  and its blue scales are mottled with other colors.
title2: Mythic Wyvern
CR: 8
MR: 3
sources:
- name: Mythic Adventures
  page: 223
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 4800
alignment: N
size: Large
type: dragon
subtypes:
- mythic
initiative:
  bonus: 8
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 22
  touch: 10
  flat_footed: 21
  components:
    dex: 1
    natural: 12
    size: -1
HP:
  HP: 103
  long: 7d12+58
saves:
  fort: 9
  ref: 6
  will: 8
DR:
- amount: 5
  weakness: epic
immunities:
- dragon traits
- paralysis
- sleep
resistances:
  acid: 10
  cold: 10
  electricity: 10
  fire: 10
speeds:
  base: 20
  fly: 100
  fly_maneuverability: average
attacks:
  melee:
  - - text: bite +11 (2d6+5 plus grab)
      entries:
      - - damage: 2d6+5
        - effect: grab
      attack: bite
      bonus:
      - 11
    - text: sting +11 (1d8+5 plus poison)
      entries:
      - - damage: 1d8+5
        - effect: poison
      attack: sting
      bonus:
      - 11
    - text: 2 wings +6 (1d8+2)
      entries:
      - - damage: 1d8+2
      count: 2
      attack: wings
      bonus:
      - 6
  special:
  - power lift
  - mythic power (3/day, surge +1d6)
  - rake (2 talons +10, 1d6+5)
  - swallow whole (1d6+5 bludgeoning, AC 14, 10 hp)
space: 10
reach: 5
ability_scores:
  STR: 21
  DEX: 12
  CON: 18
  INT: 7
  WIS: 12
  CHA: 9
BAB: 7
CMB: 13
CMB_other: +17 grapple
CMD: 24
feats:
- name: Flyby Attack
- is_mythic: true
  name: Improved Initiative
- is_mythic: true
  name: Iron Will
- name: Skill Focus (Perception)
skills:
  Fly: 9
  Perception: 18
  Sense Motive: 11
  Stealth: 7
  _racial_mods:
    Perception:
      _: 4
languages:
- Draconic
ecology:
  environment: temperate or warm hills
  organization: solitary, pair, or flight (3-6)
  treasure_type: standard
special_abilities:
  Poison (Ex): Sting-injury; save DC 17; frequency 1/round for 6 rounds; effect 1d4
    Constitution damage; cure 2 consecutive saves. The save DC is Constitution-based.
  Power Lift (Ex): A mythic wyvern can expend one use of mythic power to withdraw
    as a move action (instead of a full-round action), moving up to its speed instead
    of double. It can even move straight up. If it's grappling a creature, the wyvern
    can bring the grappled creature with it. Usually a wyvern uses this ability to
    carry off its prey and drop it from above onto a hard surface. Since this is a
    move action, the wyvern can damage its target, withdraw, and drop its target all
    in the same round.
desc_long: A mythic wyvern has one or more true dragons in its recent ancestry, making
  it strong and resilient. Despite its greater power and ego, it is more inclined
  to accept a rider than other wyverns, perhaps because it recognizes the value of
  an alliance.

---

# Wyvern
A dark blue dragon, its wings immense and its tail tipped with a hooked stinger, lands on two taloned feet and roars a challenge.
**Source** Pathfinder RPG Bestiary pg. 282
**XP** 2,400

N Large dragon
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +18

##### Defense

**AC** 19, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+1 Dex, +9 natural, –1 size)
**hp** 73 (7d12+28)
**Fort** +9, **Ref** +6, **Will** +8
**Immune** sleep, _[[universal monster rules/Paralysis|paralysis]]_

##### Offense
**Speed** 20 ft., fly 60 ft. (poor)
**Melee** sting +10 melee (1d6+4 plus poison), bite +10 melee (2d6+4 plus _[[universal monster rules/Grab|grab]]_), 2 wings +5 (1d6+2)
**Space** 10 ft., **Reach** 5 ft.

##### Statistics
**Str** 19, **Dex** 12, **Con** 18, **Int** 7, **Wis** 12, **Cha** 9
**Base Atk** +7; **CMB** +12 (+16 grapple); **CMD** 23
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** Fly +5, Perception +18, Sense Motive +11, Stealth +7; **Racial Modifier** +4 Perception
**Languages** Draconic

##### Ecology

**Environment** temperate or warm hills
**Organization** solitary, pair, or _[[universal monster rules/Flight|flight]]_ (3–6)
**Treasure** standard

### Special Abilities

**Poison (Ex)** Sting—injury; save DC 17; frequency 1/round for 6 rounds; effect 1d4 Constitution damage; cure 2 consecutive saves. The save DC is Constitution-based.

##### Description

Wyverns are nasty, brutish, and violent reptilian beasts akin to more powerful dragons. They are always aggressive and impatient, and are quick to resort to force in order to accomplish their goals. For this reason, dragons generally look down upon wyverns, considering their distant cousins nothing more than primitive savages with a distinct lack of style or wit. In most cases, this generalization is spot-on. Although far from animalistic in intellect, and capable of speech, most wyverns simply can’t be bothered with the subtlety of diplomacy, and prefer to fight first and parley later, and even then only if faced with a foe they can neither defeat nor flee from.

Wyverns are territorial creatures. Though they occasionally hunt in small groups for large prey, they are generally solitary creatures, hunting in areas ranging in size from 100 to 200 square miles. Wyverns have been known to fight to the death among themselves for the right to hunt a territory rich with prey.

Although constantly hungry and _[[conditions/Prone|prone]]_ to mayhem, a _[[monsters/Wyvern|wyvern]]_ that can be befriended (usually through a delicate combination of flattery, intimidation, food, and treasure) becomes a powerful ally. They often serve giants and monstrous humanoids as guardians, and some _[[monsters/Lizardfolk|lizardfolk]]_ and _[[monsters/Boggard|boggard]]_ tribes even use them as mounts, although such arrangements are quite costly in terms of food and gold, for few are the wyverns who would willingly serve as steeds for lesser creatures for long.

A _wyvern_ is about 16 feet in length, half of which is tail. The average _wyvern_ weighs 2,000 pounds.
---
cssclass: [monsters]
title1: Xenopterid
desc_short: What appears to be this creature's cloak unfurls into bug wings, and its
  apparently human face is merely patterns on its head.
title2: Xenopterid
CR: 7
sources:
- name: Bestiary 4
  page: 283
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 3200
alignment: N
size: Medium
type: vermin
initiative:
  bonus: 3
senses:
  darkvision: 60
  lifesense: true
AC:
  AC: 21
  touch: 13
  flat_footed: 18
  components:
    dex: 3
    natural: 8
HP:
  HP: 93
  long: 11d8+44
saves:
  fort: 11
  ref: 6
  will: 4
defensive_abilities:
- ferocity
immunities:
- mind-affecting effects
speeds:
  base: 40
  climb: 20
  fly: 20
  fly_maneuverability: clumsy
attacks:
  melee:
  - - text: 2 claws +13 (1d6+5 plus grab)
      entries:
      - - damage: 1d6+5
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 13
    - text: bite +13 (1d6+5 plus poison)
      entries:
      - - damage: 1d6+5
        - effect: poison
      attack: bite
      bonus:
      - 13
  special:
  - blood drain (1d2 Constitution)
  - poison
ability_scores:
  STR: 20
  DEX: 17
  CON: 19
  INT:
  WIS: 12
  CHA: 7
BAB: 8
CMB: 13
CMB_other: +17 grapple
CMD: 26
CMD_other: 34 vs. trip
feats:
- is_bonus: true
  name: Improved Critical (claw)
skills:
  Climb: 13
  Disguise: 6
    when disguised as a humanoid: 14
  Fly: -5
  Stealth: 11
  Perception: 1
  _racial_mods:
    Disguise:
      _: 8
      when disguised as a humanoid: 16
    Stealth:
      _: 8
special_qualities:
- entangling slime
ecology:
  environment: any land or underground
  organization: solitary, pair, or hive (3-30)
  treasure_type: none
special_abilities:
  Entangling Slime (Ex): A xenopterid can produce a sticky, slimy secretion it uses
    to protect its territory and eggs. The xenopterid can slime up to a 10-foot-square
    area per day at a rate of 1 square foot per minute. For 1 week thereafter, any
    creature coming in direct contact with the slime must succeed at a DC 19 Strength
    check or be entangled and glued to it as if it had failed its save against a tanglefoot
    bag. The save DC is Constitution-based.
  Poison (Ex): Bite-injury; save Fort DC 19; frequency 1/round for 6 rounds; effect
    1d4 Dex; cure 2 consecutive saves. The save DC is Constitution-based.
desc_long: |-
  Xenopterids are human-sized predatory insects with the insidious ability to mimic the form of their favorite prey-humanoids. Xenopterids can be encountered nearly anywhere they can find food, quickly adapting their mimicry to resemble whatever humanoids are most common in a particular region. They can bend their wings to form cowls and cloaks, and they can fold their limbs to imitate humanoids' weapons and armor. A xenopterid's eeriest feature is its mouth-a crude chitinous beak that, when closed, resembles a human face. Up close, the xenopterid's unsettling nature is obvious, but from a distance or in dim light, the creature easily passes for its prey. Because their mimicking abilities require concealment, xenopterids commonly hunt their prey at night. Once a xenopterid captures and kills a victim, it liquefies the creature's remains in order to bring the putrid slurry back to the hive where it stuffs this substance into small spherical capsules the creatures use as food. Some evil races prize these capsules, and make gruesome liquors by fermenting the contents.

  Xenopterids live in colonies in abandoned ruins, old castles, decrepit farmsteads, and similarly abandoned human structures. A colony typically consists of 19 to 28 sterile drones and a fertile hive king and hive queen (xenopterids with the advanced creature simple template). Each colony has only one fertile male, so xenopterids reproduce slowly. Still, the only way to destroy a xenopterid colony is to kill both the king and the queen, and neither one of them ever leaves the safety of the hive. Xenopterid drones become fiercely aggressive when defending the hive against invaders.

---

# Xenopterid
What appears to be this creature’s cloak unfurls into bug wings, and its apparently human face is merely patterns on its head.
**Source** Bestiary 4 pg. 283
**XP** 3,200

N Medium vermin
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Lifesense|lifesense]]_; Perception +1

##### Defense

**AC** 21, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+3 Dex, +8 natural)
**hp** 93 (11d8+44)
**Fort** +11, **Ref** +6, **Will** +4
**Defensive Abilities** _[[universal monster rules/Ferocity|ferocity]]_; **Immune** mind-affecting effects

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 20 ft., fly 20 ft. (clumsy)
**Melee** 2 claws +13 (1d6+5 plus _[[universal monster rules/Grab|grab]]_), bite +13 (1d6+5 plus poison)
**Special Attacks** _[[universal monster rules/Blood Drain|blood drain]]_ (1d2 Constitution), poison

##### Statistics
**Str** 20, **Dex** 17, **Con** 19, **Int** —, **Wis** 12, **Cha** 7
**Base Atk** +8; **CMB** +13 (+17 grapple); **CMD** 26 (34 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Improved Critical|Improved Critical]]_ (claw)
**Skills** _Climb_ +13, Disguise +6 (+14 when disguised as a humanoid), Fly –5, Stealth +11; **Racial Modifiers** +8 Disguise (+16 when disguised as a humanoid), +8 Stealth
**SQ** entangling slime

##### Ecology

**Environment** any land or underground
**Organization** solitary, pair, or hive (3–30)
**Treasure** none

### Special Abilities

**Entangling Slime (Ex)** A _[[monsters/Xenopterid|xenopterid]]_ can produce a _[[items/Weapon Magic Abilities/Sticky|sticky]]_, slimy secretion it uses to protect its territory and eggs. The _xenopterid_ can slime up to a 10-foot-square area per day at a rate of 1 square foot per minute. For 1 week thereafter, any creature coming in direct contact with the slime must succeed at a DC 19 Strength check or be _[[conditions/Entangled|entangled]]_ and glued to it as if it had failed its save against a _[[items/Mundane/Tanglefoot bag|tanglefoot bag]]_. The save DC is Constitution-based.

**Poison (Ex)** Bite—injury; save Fort DC 19; frequency 1/round for 6 rounds; effect 1d4 Dex; cure 2 consecutive saves. The save DC is Constitution-based.

##### Description

Xenopterids are human-sized predatory insects with the insidious ability to _[[monsters/Mimic|mimic]]_ the form of their favorite prey—humanoids. Xenopterids can be encountered nearly anywhere they can find food, quickly adapting their mimicry to resemble whatever humanoids are most common in a particular region. They can bend their wings to form cowls and cloaks, and they can fold their limbs to imitate humanoids’ weapons and armor. A _xenopterid_’s eeriest feature is its mouth—a crude chitinous beak that, when closed, resembles a human face. Up close, the _xenopterid_’s unsettling nature is obvious, but from a distance or in dim light, the creature easily passes for its prey. Because their mimicking abilities require concealment, xenopterids commonly hunt their prey at night. Once a _xenopterid_ captures and kills a victim, it liquefies the creature’s remains in order to bring the _[[items/Armor Magic Abilities/Putrid|putrid]]_ slurry back to the hive where it stuffs this substance into small spherical capsules the creatures use as food. Some evil races prize these capsules, and make gruesome liquors by fermenting the contents.

Xenopterids live in colonies in abandoned ruins, old castles, decrepit farmsteads, and similarly abandoned human structures. A colony typically consists of 19 to 28 sterile drones and a fertile hive _[[npcs/King|king]]_ and hive queen (xenopterids with the advanced creature simple template). Each colony has only one fertile male, so xenopterids reproduce slowly. Still, the only way to destroy a _xenopterid_ colony is to kill both the _king_ and the queen, and neither one of them ever leaves the safety of the hive. _Xenopterid_ drones become fiercely aggressive when _[[items/Weapon Magic Abilities/Defending|defending]]_ the hive against invaders.
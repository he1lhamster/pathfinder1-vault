---
cssclass: [monsters]
title1: Heartrot Tree
desc_short: Fungus drips from this grotesque tree's ridged bark as its branches wave
  like boneless arms.
title2: Heartrot Tree
CR: 13
sources:
- name: 'Pathfinder #119: Prisoners of the Blight'
  page: 86
  link: http://paizo.com/products/btpy9npn
XP: 25600
alignment: NE
size: Huge
type: plant
initiative:
  bonus: 4
senses:
  blindsense: 60
  low-light vision: true
AC:
  AC: 28
  touch: 8
  flat_footed: 28
  components:
    natural: 20
    size: -2
HP:
  HP: 184
  long: 16d8+112
saves:
  fort: 17
  ref: 7
  will: 5
defensive_abilities:
- all-around vision
DR:
- amount: 10
  weakness: slashing
immunities:
- plant traits
- poison
speeds:
  base: 10
attacks:
  melee:
  - - text: 2 tendrils +20 (2d6+9/19-20)
      entries:
      - - damage: 2d6+9
          crit_range: 19-20
      count: 2
      attack: tendrils
      bonus:
      - 20
    - text: slam +20 (1d8+13/19-20 plus disease)
      entries:
      - - damage: 1d8+13
          crit_range: 19-20
        - effect: disease
      attack: slam
      bonus:
      - 20
  special:
  - disease
space: 15
reach: 15
ability_scores:
  STR: 29
  DEX: 10
  CON: 24
  INT: 2
  WIS: 11
  CHA: 3
BAB: 12
CMB: 23
CMD: 33
CMD_other: can't be tripped
feats:
- name: Improved Critical (slam)
- name: Improved Critical (tendril)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Power Attack
- name: Skill Focus (Perception)
- name: Weapon Focus (slam)
- name: Weapon Focus (tendril)
skills:
  Perception: 14
  Stealth: 3
    in forests: 11
  _racial_mods:
    Stealth:
      in forests: 8
special_qualities:
- hardy stump
- virulent roots
ecology:
  environment: any forest or underground
  organization: solitary, pair, or festering grove (6-12)
  treasure_type: incidental
special_abilities:
  Disease (Ex): |-
    Unlike other diseases, heartrot disease is particularly insidious due to having an immediate effect in addition to a lasting effect.

     Heartrot Disease: Slam-contact; save Fort DC 25; onset immediate; frequency 1/round for 5 rounds, then 1/day for 10 days; initial effect 1d2 Wis damage and nauseated; secondary effect 1d3 Con drain; cure 3 consecutive saves.
  Hardy Stump (Ex): A heartrot tree is difficult to kill. After it sustains fatal
    damage, a heartrot tree begins to regenerate and can grow back to its previous
    size in 1d4 weeks. Dealing 50 points of fire damage to the heartrot tree's stump
    after it has sustained fatal damage prevents this regeneration.
  Virulent Roots (Ex): A heartrot tree's roots grow deep beneath the surface. If the
    tree grows above a cave, cavern, or other large underground opening, its roots
    have the same statistics as the aboveground tree and can menace creatures underground
    in the same way. In this case, though they grow from the ceiling, treat a heartrot
    tree's roots exactly as a normal heartrot tree. A heartrot tree can't fight with
    its branches and roots simultaneously.
desc_long: |-
  Disgusting products of blight or other magical plagues, heartrot trees represent nature warped to its most insidious. Heartrot trees typically lurk in the deepest depths of fouled forests; they are the manifestations of the very forces that poison the land. As a result, evil and disease pulse within heartrot trees, and the behemoths hunger to destroy anything good or natural still left around them.

   Heartrot trees are typically 30 feet tall from the base of their trunks to the tips of their tendril-like branches. When the trees grow above a cave or another large underground space, their roots are horrifically similar to their branches and dangle just as far from the ceiling. Heartrot trees' trunks are typically 15 feet in circumference, and the plant's entire mass weighs around 15 tons.

---

# Heartrot Tree
Fungus drips from this grotesque tree’s ridged bark as its branches wave like boneless arms.
**Source** Pathfinder #119: Prisoners of the _[[spells/Blight|Blight]]_ pg. 86
**XP** 25,600

NE Huge plant
**Init** +4; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +14

##### Defense

**AC** 28, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+20 natural, –2 size)
**hp** 184 (16d8+112)
**Fort** +17, **Ref** +7, **Will** +5
**Defensive Abilities** _[[universal monster rules/All-Around Vision|all-around vision]]_; **DR** 10/slashing; **Immune** _[[universal monster rules/Plant Traits|plant traits]]_, poison

##### Offense
**Speed** 10 ft.
**Melee** 2 tendrils +20 (2d6+9/19–20), slam +20 (1d8+13/19–20 plus disease)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** disease

##### Statistics
**Str** 29, **Dex** 10, **Con** 24, **Int** 2, **Wis** 11, **Cha** 3
**Base Atk** +12; **CMB** +23; **CMD** 33 (can’t be tripped)
**Feats** _[[feats/Improved Critical|Improved Critical]]_ (slam, tendril), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Weapon Focus|Weapon Focus]]_ (slam, tendril)
**Skills** Perception +14, Stealth +3 (+11 in forests); **Racial Modifiers** +8 Stealth in forests
**SQ** hardy stump, _[[items/Weapon Magic Abilities/Virulent|virulent]]_ roots

##### Ecology

**Environment** any forest or underground
**Organization** solitary, pair, or festering grove (6–12)
**Treasure** incidental

### Special Abilities

**Disease (Ex)** Unlike other diseases, heartrot disease is particularly insidious due to having an immediate effect in addition to a lasting effect.

Heartrot Disease: Slam—contact; save Fort DC 25; onset immediate; frequency 1/round for 5 rounds, then 1/day for 10 days; initial effect 1d2 Wis damage and _[[conditions/Nauseated|nauseated]]_; secondary effect 1d3 Con drain; cure 3 consecutive saves.

**Hardy Stump (Ex)** A _[[monsters/Heartrot Tree|heartrot tree]]_ is difficult to kill. After it sustains fatal damage, a _heartrot tree_ begins to _[[spells/Regenerate|regenerate]]_ and can grow back to its previous size in 1d4 weeks. Dealing 50 points of fire damage to the _heartrot tree_’s stump after it has sustained fatal damage prevents this _[[universal monster rules/Regeneration|regeneration]]_.

**_Virulent_ Roots (Ex)** A _heartrot tree_’s roots grow deep beneath the surface. If the tree grows above a cave, cavern, or other large underground opening, its roots have the same statistics as the aboveground tree and can menace creatures underground in the same way. In this case, though they grow from the ceiling, treat a _heartrot tree_’s roots exactly as a normal _heartrot tree_. A _heartrot tree_ can’t fight with its branches and roots simultaneously.

##### Description

Disgusting products of _blight_ or other magical plagues, heartrot trees represent nature warped to its most insidious. Heartrot trees typically lurk in the deepest depths of fouled forests; they are the manifestations of the very forces that poison the land. As a result, evil and disease pulse within heartrot trees, and the behemoths hunger to destroy anything good or natural still left around them.

Heartrot trees are typically 30 feet tall from the base of their trunks to the tips of their tendril-like branches. When the trees grow above a cave or another large underground space, their roots are horrifically similar to their branches and dangle just as far from the ceiling. Heartrot trees’ trunks are typically 15 feet in circumference, and the plant’s entire mass weighs around 15 tons.
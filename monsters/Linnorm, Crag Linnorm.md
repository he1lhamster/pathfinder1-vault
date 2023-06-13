---
cssclass: [monsters]
title1: Linnorm, Crag Linnorm
desc_short: This immense, wingless dragon rears up on a serpentine body. Its triple
  tail and powerful talons swipe at the air.
title2: Crag Linnorm
CR: 14
sources:
- name: Pathfinder RPG Bestiary
  page: 190
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 38400
alignment: CE
size: Gargantuan
type: dragon
initiative:
  bonus: 8
senses:
  darkvision: 120
  low-light vision: true
  scent: true
  true seeing: true
AC:
  AC: 29
  touch: 10
  flat_footed: 25
  components:
    dex: 4
    natural: 19
    size: -4
HP:
  HP: 202
  long: 15d12+105
  regeneration: 10
  regeneration_weakness: cold iron
saves:
  fort: 16
  ref: 15
  will: 13
defensive_abilities:
- freedom of movement
DR:
- amount: 15
  weakness: cold iron
immunities:
- curse effects
- fire
- mind-affecting effects
- paralysis
- poison
- sleep
SR: 25
speeds:
  base: 40
  fly: 100
  fly_maneuverability: average
  swim: 60
attacks:
  melee:
  - - text: bite +23 (2d8+12/19-20 plus poison)
      entries:
      - - damage: 2d8+12
          crit_range: 19-20
        - effect: poison
      attack: bite
      bonus:
      - 23
    - text: 2 claws +23 (1d8+12)
      entries:
      - - damage: 1d8+12
      count: 2
      attack: claws
      bonus:
      - 23
    - text: tail +18 (2d6+6 plus grab)
      entries:
      - - damage: 2d6+6
        - effect: grab
      attack: tail
      bonus:
      - 18
  special:
  - breath weapon
  - constrict (tail, 2d6+18)
  - death curse
space: 20
reach: 20
ability_scores:
  STR: 34
  DEX: 18
  CON: 25
  INT: 5
  WIS: 18
  CHA: 21
BAB: 15
CMB: 31
CMB_other: +35 grapple
CMD: 45
CMD_other: can't be tripped
feats:
- name: Blind-Fight
- name: Cleave
- name: Combat Reflexes
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Power Attack
skills:
  Fly: 16
  Perception: 22
  Swim: 38
languages:
- Aklo
- Draconic
- Sylvan
ecology:
  environment: cold hills
  organization: solitary
  treasure_type: triple
special_abilities:
  Breath Weapon (Su): Once every 1d4 rounds as a standard action, a crag linnorm can
    expel a 120-foot line of magma, dealing 15d8 points of fire damage to all creatures
    struck (Reflex DC 24 halves). This line of magma remains red-hot for 1 round after
    the linnorm creates it. Creatures that took damage on the first round take 6d6
    fire damage the second round (Reflex DC 24 negates), as does any creature that
    walks across the line of magma. If the magma was expelled while the linnorm was
    airborne, it instead rains downward during the second round as a sheet of fire
    no more than 60 feet high that does 6d6 damage (Reflex DC 24 negates) to any creature
    that passes through it. On the third round, the line of magma cools to a thin
    layer of brittle stone that quickly degrades to powder and sand over the course
    of several hours; magma that's turned to a sheet of fire is consumed entirely
    during the second round, leaving behind only a stain of smoke in the air that
    swiftly disperses. The save DC is Constitution-based.
  Death Curse (Su): |-
    When a creature slays a crag linnorm, the slayer is affected by the curse of fire.Curse of Fire: save Will DC 22; effect creature gains vulnerability to fire. The save DC is Charisma-based.

    Freedom of Movement (Ex) A crag linnorm is under the constant effect of freedom of movement, as per the spell of the same name. This effect cannot be dispelled.
  Poison (Su): Bite-injury; save Fort DC 24; frequency 1/round for 10 rounds; effect
    2d6 fire damage and 1d4 Con drain; cure 2 consecutive saves. The save DC is Constitution-based.
  True Seeing (Ex): A crag linnorm has constant true seeing, as per the spell of the
    same name.
desc_long: Like all linnorms, the deadly crag linnorm is a powerful, primeval dragon,
  a denizen of the wild regions far north of where most civilizations dare to tread.
  The crag linnorm is among the weakest of its kind, yet still a devastating predator
  in its own right. Favored, if not by the gods, then by some primal intelligence
  of the mysterious world of the fey, the linnorm bestows a powerful curse on any
  who manage to slay it. A crag linnorm is 60 feet long and weighs 12,000 pounds.

---

# Linnorm, Crag Linnorm
This immense, wingless dragon rears up on a serpentine body. Its triple tail and powerful talons _[[spells/Swipe|swipe]]_ at the air.
**Source** Pathfinder RPG Bestiary pg. 190
**XP** 38,400
CE Gargantuan dragon
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_, _[[spells/True Seeing|true seeing]]_; Perception +22

##### Defense

**AC** 29, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+4 Dex, +19 natural, –4 size)
**hp** 202 (15d12+105); _[[universal monster rules/Regeneration|regeneration]]_ 10 (cold iron)
**Fort** +16, **Ref** +15, **Will** +13
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 15/cold iron; **Immune** curse effects, fire, mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, poison, sleep; **SR** 25

##### Offense
**Speed** 40 ft., fly 100 ft. (average), swim 60 ft.
**Melee** bite +23 (2d8+12/19–20 plus poison), 2 claws +23 (1d8+12), tail +18 (2d6+6 plus _[[universal monster rules/Grab|grab]]_)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_, _[[universal monster rules/Constrict|constrict]]_ (tail, 2d6+18), death curse

##### Statistics
**Str** 34, **Dex** 18, **Con** 25, **Int** 5, **Wis** 18, **Cha** 21
**Base Atk** +15; **CMB** +31 (+35 grapple); **CMD** 45 (can’t be tripped)
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Fly +16, Perception +22, Swim +38
**Languages** Aklo, Draconic, Sylvan

##### Ecology

**Environment** cold hills
**Organization** solitary
**Treasure** triple

### Special Abilities

**_Breath Weapon_ (Su)** Once every 1d4 rounds as a standard action, a crag linnorm can expel a 120-foot line of magma, dealing 15d8 points of fire damage to all creatures struck (Reflex DC 24 halves). This line of magma remains red-hot for 1 round after the linnorm creates it. Creatures that took damage on the first round take 6d6 fire damage the second round (Reflex DC 24 negates), as does any creature that walks across the line of magma. If the magma was expelled while the linnorm was airborne, it instead rains downward during the second round as a sheet of fire no more than 60 feet high that does 6d6 damage (Reflex DC 24 negates) to any creature that passes through it. On the third round, the line of magma cools to a thin layer of brittle stone that quickly degrades to _[[items/Mundane/Powder|powder]]_ and sand over the course of several hours; magma that’s turned to a sheet of fire is consumed entirely during the second round, leaving behind only a stain of smoke in the air that swiftly disperses. The save DC is Constitution-based.

**Death Curse (Su)** When a creature slays a crag linnorm, the _[[classes/Slayer|slayer]]_ is affected by the curse of fire.Curse of Fire: save Will DC 22; effect creature gains _[[curses/Vulnerability|vulnerability]]_ to fire. The save DC is Charisma-based.

_Freedom of Movement_ (Ex) A crag linnorm is under the constant effect of _freedom of movement_, as per the spell of the same name. This effect cannot be dispelled.

**Poison (Su)** Bite—injury; save Fort DC 24; frequency 1/round for 10 rounds; effect 2d6 fire damage and 1d4 Con drain; cure 2 consecutive saves. The save DC is Constitution-based.

**_True Seeing_ (Ex)** A crag linnorm has constant _true seeing_, as per the spell of the same name.

##### Description

Like all linnorms, the _[[items/Weapon Magic Abilities/Deadly|deadly]]_ crag linnorm is a powerful, primeval dragon, a denizen of the wild regions far north of where most civilizations dare to tread. The crag linnorm is among the weakest of its kind, yet still a devastating predator in its own right. Favored, if not by the gods, then by some primal intelligence of the mysterious world of the fey, the linnorm bestows a powerful curse on any who manage to slay it. A crag linnorm is 60 feet long and weighs 12,000 pounds.
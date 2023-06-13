---
cssclass: [monsters]
title1: Dog
desc_short: This small dog has a rough coat and a hungry look in its dark brown eyes.
title2: Dog
CR: 1/3
sources:
- name: Pathfinder RPG Bestiary
  page: 87
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 135
alignment: N
size: Small
type: animal
initiative:
  bonus: 1
senses:
  low-light vision: true
  scent: true
AC:
  AC: 13
  touch: 12
  flat_footed: 12
  components:
    dex: 1
    natural: 1
    size: 1
HP:
  HP: 6
  long: 1d8+2
saves:
  fort: 4
  ref: 3
  will: 1
speeds:
  base: 40
attacks:
  melee:
  - - text: bite +2 (1d4+1)
      entries:
      - - damage: 1d4+1
      attack: bite
      bonus:
      - 2
ability_scores:
  STR: 13
  DEX: 13
  CON: 15
  INT: 2
  WIS: 12
  CHA: 6
BAB: 0
CMB: 0
CMD: 11
CMD_other: 15 vs. trip
feats:
- name: Skill Focus (Perception)
skills:
  Acrobatics: 1
    jumping: 9
  Perception: 8
  Survival: 1
    scent tracking: 5
  _racial_mods:
    Acrobatics:
      when jumping: 4
    Survival:
      when tracking by scent: 4
ecology:
  environment: any
  organization: solitary, pair, or pack (3-12)
  treasure_type: none
desc_long: |-
  The normal dog statistics presented here describe any small dog of about 20-50 pounds in weight. They can also be used for small wild canines such as coyotes, jackals, and feral dogs.

  In the wild, dogs are vicious and territorial creatures. Yet even more harrowing than a pack of wild dogs is the rabid dog. Rabies often affects animals like bats, wolverines, and rats, but the transformation of a normally friendly family pet goes through when it becomes rabid makes the dog perhaps the most notorious of the disease's classic carriers.

  A rabid creature can transmit rabies to a victim with a bite. Its CR increases by 1 (or up one step, in the case of a creature whose CR is less than 1). 

---

# Dog
This small _[[monsters/Dog|dog]]_ has a rough coat and a hungry look in its dark brown eyes.
**Source** Pathfinder RPG Bestiary pg. 87
**XP** 135

N Small animal
**Init** +1; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +8

##### Defense

**AC** 13, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+1 Dex, +1 natural, +1 size)
**hp** 6 (1d8+2)
**Fort** +4, **Ref** +3, **Will** +1

##### Offense
**Speed** 40 ft.
**Melee** bite +2 (1d4+1)

##### Statistics
**Str** 13, **Dex** 13, **Con** 15, **Int** 2, **Wis** 12, **Cha** 6
**Base Atk** +0; **CMB** +0; **CMD** 11 (15 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** Acrobatics +1 (+9 jumping), Perception +8, Survival +1 (+5 _scent_ tracking); **Racial Modifiers** +4 Acrobatics when jumping, +4 Survival when tracking by _scent_

##### Ecology

**Environment** any
**Organization** solitary, pair, or pack (3–12)
**Treasure** none

##### Description

The normal _dog_ statistics presented here describe any small _dog_ of about 20–50 pounds in weight. They can also be used for small wild canines such as coyotes, jackals, and feral dogs.

In the wild, dogs are _[[items/Weapon Magic Abilities/Vicious|vicious]]_ and territorial creatures. Yet even more _[[spells/Harrowing|harrowing]]_ than a pack of wild dogs is the rabid _dog_. Rabies often affects animals like bats, wolverines, and rats, but the _[[spells/Transformation|transformation]]_ of a normally friendly family pet goes through when it becomes rabid makes the _dog_ perhaps the most notorious of the disease’s classic carriers.

A rabid creature can transmit rabies to a victim with a bite. Its CR increases by 1 (or up one step, in the case of a creature whose CR is less than 1).

## Rabies

**Type **disease, injury; **Save **Fortitude DC 14
 **Onset **2d6 weeks; **Frequency **1/day
 **Effect **1 Con damage plus 1d3 Wis damage (minimum reduction to 1 Wis); **Cure **2 consecutive saves
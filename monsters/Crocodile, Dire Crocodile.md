---
cssclass: [monsters]
title1: Crocodile, Dire Crocodile
desc_short: This reptilian behemoth, a crocodile of monstrous proportions, is large
  enough to swallow a horse in one tremendous bite.
title2: Dire Crocodile
CR: 9
sources:
- name: Pathfinder RPG Bestiary
  page: 51
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 6400
alignment: N
size: Gargantuan
type: animal
initiative:
  bonus: 4
senses:
  low-light vision: true
AC:
  AC: 21
  touch: 6
  flat_footed: 21
  components:
    natural: 15
    size: -4
HP:
  HP: 138
  long: 12d8+84
saves:
  fort: 15
  ref: 8
  will: 8
speeds:
  base: 20
  other_semicolon: sprint
  swim: 30
attacks:
  melee:
  - - text: bite +18 (3d6+13/19-20 plus grab)
      entries:
      - - damage: 3d6+13
          crit_range: 19-20
        - effect: grab
      attack: bite
      bonus:
      - 18
    - text: tail slap +13 (4d8+6)
      entries:
      - - damage: 4d8+6
      attack: tail slap
      bonus:
      - 13
  special:
  - death roll (3d6+19 plus trip)
  - swallow whole (3d6+13, AC 16, 13 hp)
space: 20
reach: 15
ability_scores:
  STR: 37
  DEX: 10
  CON: 25
  INT: 1
  WIS: 14
  CHA: 2
BAB: 9
CMB: 26
CMB_other: +30 grapple
CMD: 36
CMD_other: 40 vs. trip
feats:
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Iron Will
- name: Run
- name: Skill Focus (Perception)
- name: Skill Focus (Stealth)
skills:
  Perception: 14
  Stealth: 0
    in water: 8
  Swim: 21
  _racial_mods:
    Stealth:
      in water: 8
special_qualities:
- hold breath
ecology:
  environment: warm rivers and marshes
  organization: solitary, pair, or colony (3-6)
  treasure_type: none
desc_long: The immense sarcosuchus, or dire crocodile, is an enormous predator capable
  of catching and eating prey as large as the largest dinosaurs.

---

# Crocodile, Dire Crocodile
This reptilian behemoth, a _[[monsters/Crocodile|crocodile]]_ of monstrous proportions, is large enough to swallow a _[[monsters/Horse|horse]]_ in one tremendous bite.
**Source** Pathfinder RPG Bestiary pg. 51
**XP** 6,400

N Gargantuan animal
**Init** +4; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +14

##### Defense

**AC** 21, touch 6, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+15 natural, –4 size)
**hp** 138 (12d8+84)
**Fort** +15, **Ref** +8, **Will** +8

##### Offense
**Speed** 20 ft., swim 30 ft.; sprint
**Melee** bite +18 (3d6+13/19–20 plus _[[universal monster rules/Grab|grab]]_) and tail slap +13 (4d8+6)
**Space** 20 ft., **Reach** 15 ft.
**Special Attacks** _[[feats/Death Roll|death roll]]_ (3d6+19 plus _[[universal monster rules/Trip|trip]]_), _[[universal monster rules/Swallow Whole|swallow whole]]_ (3d6+13, AC 16, 13 hp)

##### Statistics
**Str** 37, **Dex** 10, **Con** 25, **Int** 1, **Wis** 14, **Cha** 2
**Base Atk** +9; **CMB** +26 (+30 grapple); **CMD** 36 (40 vs. _trip_)
**Feats** _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, Run, _[[feats/Skill Focus|Skill Focus]]_ (Perception, Stealth)
**Skills** Perception +14, Stealth +0 (+8 in water), Swim +21; **Racial Modifiers** +8 Stealth in water
**SQ** _[[universal monster rules/Hold Breath|hold breath]]_

##### Ecology

**Environment** warm rivers and marshes
**Organization** solitary, pair, or colony (3–6)
**Treasure** none

##### Description

The immense sarcosuchus, or dire _crocodile_, is an enormous predator capable of catching and eating prey as large as the largest dinosaurs.
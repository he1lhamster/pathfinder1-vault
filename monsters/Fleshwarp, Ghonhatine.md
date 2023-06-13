---
cssclass: [monsters]
title1: Fleshwarp, Ghonhatine
desc_short: Even hunched and creeping upon all fours, this reptilian behemoth towers
  over its prey, its protruding teeth snapping wildly.
title2: Ghonhatine
CR: 10
sources:
- name: Bestiary 4
  page: 102
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
- name: 'Pathfinder #16: Endless Night'
  page: 84
  link: http://paizo.com/pathfinder/adventurePath/secondDarkness/v5748btpy85er
XP: 9600
alignment: CE
size: Large
type: aberration
initiative:
  bonus: -2
senses:
  darkvision: 60
  scent: true
auras:
- name: powerful stench
  radius: 10
  DC: 24
  duration: 1d4 rounds
AC:
  AC: 24
  touch: 7
  flat_footed: 24
  components:
    dex: -2
    natural: 17
    size: -1
HP:
  HP: 162
  long: 12d8+108
saves:
  fort: 13
  ref: 2
  will: 6
immunities:
- acid
- critical hits
- disease
- poison
speeds:
  base: 40
attacks:
  melee:
  - - text: 2 claws +16 (1d6+8)
      entries:
      - - damage: 1d6+8
      count: 2
      attack: claws
      bonus:
      - 16
    - text: bite +16 (2d6+8)
      entries:
      - - damage: 2d6+8
      attack: bite
      bonus:
      - 16
    - text: tail slap +14 (1d8+4)
      entries:
      - - damage: 1d8+4
      attack: tail slap
      bonus:
      - 14
  ranged:
  - - text: regurgitate +6 (2d6 acid plus filth fever)
      entries:
      - - damage: 2d6
          type: acid
        - effect: filth fever
      attack: regurgitate
      bonus:
      - 6
  special:
  - feed
  - filth fever
space: 10
reach: 10
reach_other: 15 ft. with tail
ability_scores:
  STR: 27
  DEX: 7
  CON: 28
  INT: 4
  WIS: 7
  CHA: 8
BAB: 9
CMB: 18
CMB_other: +20 bull rush
CMD: 26
CMD_other: 28 vs. bull rush
feats:
- name: Awesome Blow
- name: Cleave
- name: Improved Bull Rush
- name: Multiattack
- name: Power Attack
- name: Vital Strike
skills:
  Climb: 12
  Perception: 9
  Stealth: 0
    when underground: 4
  _racial_mods:
    Stealth:
      when underground: 4
languages:
- Draconic
ecology:
  environment: any underground
  organization: solitary or squad (2-8)
  treasure_type: none
special_abilities:
  Feed (Su): By spending a full-round action devouring the body of a dead or unconscious
    creature, a ghonhatine gains 1d8+9 temporary hit points and a +2 bonus on attack
    and damage rolls for 1 minute. The bonus to hit points is Constitution-based.
  Filth Fever (Ex): Disease-injury; save Fort DC 25; onset 1d3 days; frequency 1 day;
    effect 1d3 Dex damage and 1d3 Con damage; cure 2 consecutive saves. The save DC
    is Constitution-based.
  Powerful Stench (Ex): An enraged ghonhatine secretes a tarry, musk-like chemical.
    Any living, nonghonhatine creature within 10 feet must succeed at a DC 24 Fortitude
    save or be nauseated as long as it remains within the affected area and for 1d4
    rounds afterward. A creature that saves is sickened as long as it remains in the
    area, and can't be affected again by the same ghonhatine's stench for 24 hours.
    This is a poison effect. The save DC is Constitution-based.
  Regurgitate (Ex): A ghonhatine can expel the contents of its stomach as a ranged
    attack with a splash weapon that has a range increment of 20 feet. It deals 2d6
    acid damage to the target and splashes all adjacent creatures. In addition to
    taking damage, a target directly hit by a ghonhatine's regurgitation must make
    two DC 24 Fortitude saves, the first to resist contracting filth fever, and the
    second to avoid being nauseated for 1 minute. A nauseated creature can end its
    nausea early by dousing itself in a gallon of water. All creatures adjacent to
    the target must make DC 24 Fortitude saves to avoid being sickened for 1 minute.
    Once a ghonhatine uses this ability it can't use it again until it feeds. The
    save DCs are Constitution-based.
desc_long: Troglodytes forced to undergo fleshwarping by the drow, ghonhatines harken
  to what troglodytes might have been in savage prehistory. They stand over 10 feet
  tall (hunched to about 8 feet) and weigh upward of 5,000 pounds.

---

# Fleshwarp, Ghonhatine
Even hunched and _[[items/Armor Magic Abilities/Creeping|creeping]]_ upon all fours, this reptilian behemoth towers over its prey, its protruding teeth snapping wildly.
**Source** Bestiary 4 pg. 102, Pathfinder #16: Endless Night pg. 84
**XP** 9,600
CE Large aberration
**Init** –2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +9
**Aura** powerful _[[universal monster rules/Stench|stench]]_ (10 ft., DC 24, 1d4 rounds)

##### Defense

**AC** 24, touch 7, _[[conditions/Flat-Footed|flat-footed]]_ 24 (–2 Dex, +17 natural, –1 size)
**hp** 162 (12d8+108)
**Fort** +13, **Ref** +2, **Will** +6
**Immune** acid, critical hits, disease, poison

##### Offense
**Speed** 40 ft.
**Melee** 2 claws +16 (1d6+8), bite +16 (2d6+8), tail slap +14 (1d8+4)
**Ranged** regurgitate +6 (2d6 acid plus _[[diseases/Filth Fever|filth fever]]_)
**Space** 10 ft., **Reach** 10 ft. (15 ft. with tail)
**Special Attacks** feed, _filth fever_

##### Statistics
**Str** 27, **Dex** 7, **Con** 28, **Int** 4, **Wis** 7, **Cha** 8
**Base Atk** +9; **CMB** +18 (+20 bull rush); **CMD** 26 (28 vs. bull rush)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +12, Perception +9, Stealth +0 (+4 when underground); **Racial Modifiers** +4 Stealth when underground
**Languages** Draconic

##### Ecology

**Environment** any underground
**Organization** solitary or squad (2–8)
**Treasure** none

### Special Abilities

**Feed (Su)** By spending a full-round action devouring the body of a dead or _[[conditions/Unconscious|unconscious]]_ creature, a ghonhatine gains 1d8+9 temporary hit points and a +2 bonus on attack and damage rolls for 1 minute. The bonus to hit points is Constitution-based.

**_Filth Fever_ (Ex)** Disease—injury; save Fort DC 25; onset 1d3 days; frequency 1 day; effect 1d3 Dex damage and 1d3 Con damage; cure 2 consecutive saves. The save DC is Constitution-based.

**Powerful _Stench_ (Ex)** An enraged ghonhatine secretes a tarry, musk-like chemical. Any living, nonghonhatine creature within 10 feet must succeed at a DC 24 Fortitude save or be _[[conditions/Nauseated|nauseated]]_ as long as it remains within the affected area and for 1d4 rounds afterward. A creature that saves is _[[conditions/Sickened|sickened]]_ as long as it remains in the area, and can’t be affected again by the same ghonhatine’s _stench_ for 24 hours. This is a poison effect. The save DC is Constitution-based.

**Regurgitate (Ex)** A ghonhatine can expel the contents of its stomach as a ranged attack with a splash weapon that has a range increment of 20 feet. It deals 2d6 acid damage to the target and splashes all adjacent creatures. In addition to taking damage, a target directly hit by a ghonhatine’s regurgitation must make two DC 24 Fortitude saves, the first to resist contracting _filth fever_, and the second to avoid being _nauseated_ for 1 minute. A _nauseated_ creature can end its nausea early by dousing itself in a gallon of water. All creatures adjacent to the target must make DC 24 Fortitude saves to avoid being _sickened_ for 1 minute. Once a ghonhatine uses this ability it can’t use it again until it feeds. The save DCs are Constitution-based.

##### Description

Troglodytes forced to undergo fleshwarping by the _[[monsters/Drow|drow]]_, ghonhatines harken to what troglodytes might have been in savage prehistory. They stand over 10 feet tall (hunched to about 8 feet) and weigh upward of 5,000 pounds.
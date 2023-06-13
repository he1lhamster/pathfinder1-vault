---
cssclass: [monsters]
title1: Snallygaster
desc_short: This lean, scaly beast has broad wings, horns, a single eye, and writhing
  tentacles within its sharp, toothy beak.
title2: Snallygaster
CR: 3
sources:
- name: Bestiary 4
  page: 247
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
- name: 'Pathfinder #61: Shards of Sin'
  page: 88
  link: http://paizo.com/products/btpy8rcj?Pathfinder-Adventure-Path-61-Shards-of-Sin
XP: 800
alignment: CE
size: Medium
type: aberration
initiative:
  bonus: 2
senses:
  darkvision: 60
  scent: true
AC:
  AC: 15
  touch: 12
  flat_footed: 13
  components:
    dex: 2
    natural: 3
HP:
  HP: 30
  long: 4d8+12
saves:
  fort: 4
  ref: 3
  will: 6
speeds:
  base: 20
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +6 (1d8+3/×3 plus bleed)
      entries:
      - - damage: 1d8+3
          crit_multiplier: 3
        - effect: bleed
      attack: bite
      bonus:
      - 6
    - text: 2 claws +6 (1d4+3)
      entries:
      - - damage: 1d4+3
      count: 2
      attack: claws
      bonus:
      - 6
    - text: sucking tentacles +1 (1d4+1 plus grab)
      entries:
      - - damage: 1d4+1
        - effect: grab
      attack: sucking tentacles
      bonus:
      - 1
  special:
  - aerial charge
  - bleed (1d6)
  - sucking tentacles
ability_scores:
  STR: 17
  DEX: 15
  CON: 16
  INT: 5
  WIS: 14
  CHA: 9
BAB: 3
CMB: 6
CMB_other: +10 grapple
CMD: 18
CMD_other: 22 vs. trip
feats:
- name: Flyby Attack
- name: Skill Focus (Stealth)
skills:
  Fly: 10
  Perception: 7
  Stealth: 9
    in forests: 13
  _racial_mods:
    Stealth:
      in forests: 4
languages:
- Aklo (can't speak)
ecology:
  environment: temperate forests or mountains
  organization: solitary or pair
  treasure_type: none
special_abilities:
  Aerial Charge (Ex): When a snallygaster charges downward at an angle of 45 degrees
    or more, its bite attack deals double damage (or triple damage on a critical hit).
    Bleed damage is not multiplied for this attack.
  Sucking Tentacles (Ex): A snallygaster uses its retractable tentacles to suck blood
    from its victim's bleeding wounds. If a target has a bleed effect and the snallygaster
    grabs it with tentacles or maintains a grapple against it, the target takes double
    the normal bleed damage at the beginning of its next turn. When the snallygaster
    is using its tentacles, it cannot make bite attacks.
desc_long: |-
  The snallygaster is a hideous amalgamation of lizard and bird that preys on unwary travelers. Its claws and beak have an almost metallic sheen to them, hinting at their sharpness and strength. Black stripes run the length of its scaly blue hide all the way to the tip of its long, sinuous tail. The snallygaster's serpentine neck terminates at a small, birdlike head with a single eye set in the center of the forehead. In place of a tongue, its long throat contains a slobbering mass of tentacles that twist and squirm grotesquely whenever the creature extends them.

  A typical snallygaster measures 9 feet from the tip of its tail to the point of its beak, with a wingspan of 15 feet and a weight of approximately 200 pounds.

  The snallygaster is an ambush predator, attacking its prey from above. Once it spots a potential victim, it dives toward its unsuspecting foe, using the fall to build up momentum. Once its foe lies dead or unconscious, the snallygaster uses its tonguelike tentacles to slurp up the victim's blood. The only thing a snallygaster craves more than blood is alcohol, and it spends much of each autumn scouring its territory for fermenting fruit, on which it gorges itself until thoroughly inebriated. Intoxicated snallygasters are extremely aggressive.

  Snallygasters prefer to nest in wooded, mountainous regions. They are primarily active during the day, which they spend searching for food or scaring off rivals. Whether or not a female snallygaster finds a mate, it lays one to two eggs per year.

---

# Snallygaster
This lean, scaly beast has broad wings, horns, a single eye, and writhing tentacles within its sharp, toothy beak.
**Source** Bestiary 4 pg. 247, Pathfinder #61: Shards of Sin pg. 88
**XP** 800
CE Medium aberration
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +7

##### Defense

**AC** 15, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+2 Dex, +3 natural)
**hp** 30 (4d8+12)
**Fort** +4, **Ref** +3, **Will** +6

##### Offense
**Speed** 20 ft., fly 60 ft. (good)
**Melee** bite +6 (1d8+3/×3 plus _[[universal monster rules/Bleed|bleed]]_), 2 claws +6 (1d4+3), sucking tentacles +1 (1d4+1 plus _[[universal monster rules/Grab|grab]]_)
**Special Attacks** aerial charge, _bleed_ (1d6), sucking tentacles

##### Statistics
**Str** 17, **Dex** 15, **Con** 16, **Int** 5, **Wis** 14, **Cha** 9
**Base Atk** +3; **CMB** +6 (+10 grapple); **CMD** 18 (22 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth)
**Skills** Fly +10, Perception +7, Stealth +9 (+13 in forests); **Racial Modifiers** +4 Stealth in forests
**Languages** Aklo (can’t speak)

##### Ecology

**Environment** temperate forests or mountains
**Organization** solitary or pair
**Treasure** none

### Special Abilities

**Aerial Charge (Ex)** When a _[[monsters/Snallygaster|snallygaster]]_ charges downward at an angle of 45 degrees or more, its bite attack deals double damage (or triple damage on a critical hit). _Bleed_ damage is not multiplied for this attack.
**Sucking Tentacles (Ex)** A _snallygaster_ uses its retractable tentacles to suck blood from its victim’s bleeding wounds. If a target has a _bleed_ effect and the _snallygaster_ grabs it with tentacles or maintains a grapple against it, the target takes double the normal _bleed_ damage at the beginning of its next turn. When the _snallygaster_ is using its tentacles, it cannot make bite attacks.

##### Description

The _snallygaster_ is a hideous amalgamation of lizard and bird that preys on unwary travelers. Its claws and beak have an almost metallic sheen to them, hinting at their sharpness and strength. Black stripes run the length of its scaly blue hide all the way to the tip of its long, sinuous tail. The _snallygaster_’s serpentine neck terminates at a small, birdlike head with a single eye set in the center of the forehead. In place of a tongue, its long throat contains a slobbering mass of tentacles that twist and squirm grotesquely whenever the creature extends them.

A typical _snallygaster_ measures 9 feet from the tip of its tail to the point of its beak, with a wingspan of 15 feet and a weight of approximately 200 pounds.

The _snallygaster_ is an ambush predator, attacking its prey from above. Once it spots a potential victim, it dives toward its unsuspecting foe, using the fall to build up momentum. Once its foe lies dead or _[[conditions/Unconscious|unconscious]]_, the _snallygaster_ uses its tonguelike tentacles to slurp up the victim’s blood. The only thing a _snallygaster_ craves more than blood is alcohol, and it spends much of each autumn scouring its territory for fermenting fruit, on which it gorges itself until thoroughly inebriated. Intoxicated snallygasters are extremely aggressive.

Snallygasters prefer to nest in wooded, mountainous regions. They are primarily active during the day, which they spend searching for food or scaring off rivals. Whether or not a female _snallygaster_ finds a mate, it lays one to two eggs per year.
---
cssclass: [monsters]
title1: Boggard, Boggard Farcroaker
title2: Boggard Farcroaker
CR: 3
sources:
- name: Monster Codex
  page: 11
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 800
race: Boggard
classes:
- bard 2
alignment: CE
size: Medium
type: humanoid
subtypes:
- boggard
initiative:
  bonus: 0
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 15
  touch: 10
  flat_footed: 15
  components:
    armor: 2
    natural: 3
HP:
  HP: 32
  long: 5d8+10
saves:
  fort: 5
  ref: 4
  will: 5
  other: +4 vs. bardic performance, language-dependent, and sonic
speeds:
  base: 20
  swim: 30
attacks:
  melee:
  - - text: mwk shortspear +5 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: mwk shortspear
      bonus:
      - 5
    - text: tongue -1 touch (sticky tongue)
      entries:
      - - effect: sticky tongue
      attack: tongue
      bonus:
      - -1
      touch: true
  ranged:
  - - text: shortspear +4 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: shortspear
      bonus:
      - 4
  special:
  - bardic performance 8 rounds/day (countersong, distraction, fascinate [DC 13],
    inspire courage +1)
  - terrifying croak (DC 15)
spells:
  entries:
  - name: alarm
    source: Bard
    level: 1
  - name: grease
    source: Bard
    level: 1
    DC: 13
  - name: ventriloquism
    source: Bard
    level: 1
    DC: 13
  - name: dancing lights
    source: Bard
    level: 0
  - name: daze
    source: Bard
    level: 0
    DC: 12
  - name: flare
    source: Bard
    level: 0
    DC: 12
  - name: ghost sound
    source: Bard
    level: 0
    DC: 12
  - name: message
    source: Bard
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 2
    concentration: 4
    slots:
      1: 3
      0: at-will
ability_scores:
  STR: 13
  DEX: 11
  CON: 14
  INT: 12
  WIS: 13
  CHA: 14
BAB: 3
CMB: 4
CMD: 14
feats:
- name: Skill Focus (Perform [sing])
- name: Sonic Croak
- name: Throat Pouch
skills:
  Acrobatics: 6
    when jumping: 22
  Diplomacy: 8
  Knowledge (geography): 7
  Knowledge (history): 7
  Knowledge (nature): 7
  Knowledge (nobility): 7
  Linguistics: 5
  Perception: 11
  Perform (sing): 13
  Stealth: 5
    in swamps: 13
  Swim: 9
languages:
- Boggard
- Common
- Draconic
special_qualities:
- bardic knowledge +1
- hold breath
- swamp stride
- versatile performance (Perform [sing])
gear:
  gear:
  - leather armor
  - mwk shortspear
  - shortspear
  - 468 gp
ecology:
  environment: temperate marshes
desc_long: A few boggards serve their tribes in specialized roles.

---

# Boggard, Boggard Farcroaker

**Source** Monster Codex pg. 11
**XP** 800
_[[monsters/Boggard|Boggard]]_ _[[classes/Bard|bard]]_ 2
CE Medium humanoid (_boggard_)
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +11

##### Defense

**AC** 15, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+2 armor, +3 natural)
**hp** 32 (5d8+10)
**Fort** +5, **Ref** +4, **Will** +5; +4 vs. bardic performance, language-dependent, and sonic

##### Offense
**Speed** 20 ft., swim 30 ft.
**Melee** mwk _[[items/Weapon/Shortspear|shortspear]]_ +5 (1d6+1), tongue –1 touch (_[[items/Weapon Magic Abilities/Sticky|sticky]]_ tongue)
**Ranged** _shortspear_ +4 (1d6+1)
**Special Attacks** bardic performance 8 rounds/day (countersong, _[[universal monster rules/Distraction|distraction]]_, fascinate [DC 13], inspire courage +1), terrifying croak (DC 15)
**_Bard_ Spells Known** (CL 2nd; concentration +4)
1st (3/day)—_[[spells/Alarm|alarm]]_, _[[spells/Grease|grease]]_ (DC 13), _[[spells/Ventriloquism|ventriloquism]]_ (DC 13)
 0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 12), _[[spells/Flare|flare]]_ (DC 12), _[[spells/Ghost Sound|ghost sound]]_ (DC 12), _[[spells/Message|message]]_

##### Statistics
**Str** 13, **Dex** 11, **Con** 14, **Int** 12, **Wis** 13, **Cha** 14
**Base Atk** +3; **CMB** +4; **CMD** 14
**Feats** _[[feats/Skill Focus|Skill Focus]]_ (Perform [sing]), _[[feats/Sonic Croak|Sonic Croak]]_, _[[feats/Throat Pouch|Throat Pouch]]_
**Skills** Acrobatics +6 (+22 when jumping), Diplomacy +8, Knowledge (geography, history, nature, nobility) +7, Linguistics +5, Perception +11, Perform (sing) +13, Stealth +5 (+13 in swamps), Swim +9
**Languages** _Boggard_, Common, Draconic
**SQ** bardic knowledge +1, _[[universal monster rules/Hold Breath|hold breath]]_, swamp stride, versatile performance (Perform [sing])
**Gear** _[[items/Armor/Leather armor|leather armor]]_, mwk _shortspear_, _shortspear_, 468 gp

##### Ecology

**Environment** temperate marshes

##### Description

A few boggards serve their tribes in specialized roles.
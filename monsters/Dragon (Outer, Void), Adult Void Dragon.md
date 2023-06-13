---
cssclass: [monsters]
title1: Dragon (Outer, Void), Adult Void Dragon
title2: Adult Void Dragon
CR: 13
sources:
- name: Bestiary 4
  page: 72
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 25600
alignment: NE
size: Huge
type: dragon
initiative:
  bonus: 5
senses:
  dragon senses: true
  see in darkness: true
auras:
- name: alien presence
  radius: 180
  DC: 23
AC:
  AC: 29
  touch: 9
  flat_footed: 28
  components:
    dex: 1
    natural: 20
    size: -2
HP:
  HP: 184
  long: 16d12+80
saves:
  fort: 15
  ref: 11
  will: 15
DR:
- amount: 5
  weakness: magic
immunities:
- cold
- confusion
- insanity effects
- paralysis
- sleep
SR: 24
speeds:
  base: 40
  fly: 200
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +23 (2d8+12/19-20 plus obliterate)
      entries:
      - - damage: 2d8+12
          crit_range: 19-20
        - effect: obliterate
      attack: bite
      bonus:
      - 23
    - text: 2 claws +22 (2d6+8)
      entries:
      - - damage: 2d6+8
      count: 2
      attack: claws
      bonus:
      - 22
    - text: 2 wings +20 (1d8+4)
      entries:
      - - damage: 1d8+4
      count: 2
      attack: wings
      bonus:
      - 20
    - text: tail slap +20 (2d6+12)
      entries:
      - - damage: 2d6+12
      attack: tail slap
      bonus:
      - 20
  special:
  - breath weapon (50-ft. cone, 12d8 cold, DC 23)
  - crush
  - obliterate (DC 23)
  - suffocating breath (DC 23)
  - void gaze (DC 23)
space: 15
reach: 10
reach_other: 15 ft. with bite
spell_like_abilities:
  entries:
  - name: blur
    source: default
    freq: At will
  - name: ray of enfeeblement
    source: default
    freq: At will
    DC: 16
  - name: ray of exhaustion
    source: default
    freq: At will
    DC: 18
  sources:
  - name: default
    CL: 16
    concentration: 21
spells:
  entries:
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: lightning bolt
    source: Sorcerer
    level: 3
    DC: 18
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: resist energy
    source: Sorcerer
    level: 2
  - name: touch of idiocy
    source: Sorcerer
    level: 2
    DC: 17
  - name: alarm
    source: Sorcerer
    level: 1
  - name: cause fear
    source: Sorcerer
    level: 1
    DC: 17
  - name: hypnotism
    source: Sorcerer
    level: 1
    DC: 17
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: obscuring mist
    source: Sorcerer
    level: 1
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: 4 more
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 7
    concentration: 12
    slots:
      3: 5
      2: 7
      1: 8
      0: at-will
ability_scores:
  STR: 27
  DEX: 12
  CON: 21
  INT: 20
  WIS: 17
  CHA: 20
BAB: 16
CMB: 26
CMD: 37
CMD_other: 41 vs. trip
feats:
- name: Flyby Attack
- name: Hover
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Iron Will
- name: Multiattack
- name: Weapon Focus (bite)
- name: Wingover
skills:
  Acrobatics: 17
  Bluff: 24
  Diplomacy: 18
  Fly: 20
  Intimidate: 22
  Knowledge (arcana): 24
  Knowledge (planes): 24
  Perception: 22
  Sense Motive: 22
  Spellcraft: 20
  Stealth: 12
  Survival: 14
  Use Magic Device: 16
languages:
- Abyssal
- Aklo
- Celestial
- Draconic
- Ignan
- Infernal
special_qualities:
- agile
- no breath
- starflight
ecology:
  environment: vacuum
  organization: solitary
  treasure_type: triple
desc_long: Void dragons have been tainted by long exposure to the terrible alien entities
  that dwell in deep space. Though some continue to struggle against the inevitable
  tide of annihilation, many have embraced the encroaching void and exist only to
  feed and destroy.

---

# Dragon (Outer, Void), Adult Void Dragon

**Source** Bestiary 4 pg. 72
**XP** 25,600

NE Huge dragon
**Init** +5; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +22
**Aura** alien presence (180 ft., DC 23)

##### Defense

**AC** 29, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+1 Dex, +20 natural, –2 size)
**hp** 184 (16d12+80)
**Fort** +15, **Ref** +11, **Will** +15
**DR** 5/magic; **Immune** cold, _[[spells/Confusion|confusion]]_, _[[spells/Insanity|insanity]]_ effects, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 24

##### Offense
**Speed** 40 ft., fly 200 ft. (good)
**Melee** bite +23 (2d8+12/19–20 plus obliterate), 2 claws +22 (2d6+8), 2 wings +20 (1d8+4), tail slap +20 (2d6+12)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (50-ft. cone, 12d8 cold, DC 23), crush, obliterate (DC 23), suffocating breath (DC 23), void _[[universal monster rules/Gaze|gaze]]_ (DC 23)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +21)
At will—_[[spells/Blur|blur]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 16), _[[spells/Ray of Exhaustion|ray of exhaustion]]_ (DC 18)
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 7th; concentration +12)
3rd (5/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 18)
2nd (7/day)—_[[spells/Invisibility|invisibility]]_, _[[spells/Resist Energy|resist energy]]_, _[[spells/Touch of Idiocy|touch of idiocy]]_ (DC 17)
1st (8/day)—_[[spells/Alarm|alarm]]_, _[[spells/Cause Fear|cause fear]]_ (DC 17), _[[spells/Hypnotism|hypnotism]]_ (DC 17), _[[spells/Mage Armor|mage armor]]_, _[[spells/Obscuring Mist|obscuring mist]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Read Magic|read magic]]_, 4 more

##### Statistics
**Str** 27, **Dex** 12, **Con** 21, **Int** 20, **Wis** 17, **Cha** 20
**Base Atk** +16; **CMB** +26; **CMD** 37 (41 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite), _[[feats/Wingover|Wingover]]_
**Skills** Acrobatics +17, Bluff +24, Diplomacy +18, Fly +20, Intimidate +22, Knowledge (arcana, planes) +24, Perception +22, Sense Motive +22, Spellcraft +20, Stealth +12, Survival +14, Use Magic Device +16
**Languages** Abyssal, Aklo, Celestial, Draconic, Ignan, Infernal
**SQ** _[[items/Weapon Magic Abilities/Agile|agile]]_, _[[universal monster rules/No Breath|no breath]]_, starflight

##### Ecology

**Environment** vacuum
**Organization** solitary
**Treasure** triple

Void dragons have been tainted by long exposure to the terrible alien entities that dwell in deep space. Though some continue to struggle against the inevitable tide of annihilation, many have embraced the encroaching void and exist only to feed and destroy.
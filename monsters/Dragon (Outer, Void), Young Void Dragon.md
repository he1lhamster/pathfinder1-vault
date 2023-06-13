---
cssclass: [monsters]
title1: Dragon (Outer, Void), Young Void Dragon
desc_short: This dragon's ebony scales and horns are flecked with a substance that
  glows an eerie green. The folds of its wings ref lect a starry sky.
title2: Young Void Dragon
CR: 9
sources:
- name: Bestiary 4
  page: 72
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 6400
alignment: NE
size: Large
type: dragon
initiative:
  bonus: 2
senses:
  dragon senses: true
  see in darkness: true
AC:
  AC: 22
  touch: 11
  flat_footed: 20
  components:
    dex: 2
    natural: 11
    size: -1
HP:
  HP: 95
  long: 10d12+30
saves:
  fort: 10
  ref: 9
  will: 10
immunities:
- cold
- confusion
- insanity effects
- paralysis
- sleep
speeds:
  base: 40
  fly: 200
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +15 (2d6+7 plus obliterate)
      entries:
      - - damage: 2d6+7
        - effect: obliterate
      attack: bite
      bonus:
      - 15
    - text: 2 claws +14 (1d8+5)
      entries:
      - - damage: 1d8+5
      count: 2
      attack: claws
      bonus:
      - 14
    - text: 2 wings +12 (1d6+2)
      entries:
      - - damage: 1d6+2
      count: 2
      attack: wings
      bonus:
      - 12
    - text: tail slap +12 (1d8+7)
      entries:
      - - damage: 1d8+7
      attack: tail slap
      bonus:
      - 12
  special:
  - breath weapon (40-ft. cone, 6d8 cold, DC 18)
  - obliterate (DC 18)
  - suffocating breath (DC 18)
space: 10
reach: 5
reach_other: 10 ft. with bite
spell_like_abilities:
  entries:
  - name: ray of enfeeblement
    source: default
    freq: At will
    DC: 14
  sources:
  - name: default
    CL: 10
    concentration: 13
spells:
  entries:
  - name: hypnotism
    source: Sorcerer
    level: 1
    DC: 15
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 1
    concentration: 4
    slots:
      1: 4
      0: at-will
ability_scores:
  STR: 21
  DEX: 14
  CON: 17
  INT: 16
  WIS: 13
  CHA: 16
BAB: 10
CMB: 16
CMD: 28
CMD_other: 32 vs. trip
feats:
- name: Flyby Attack
- name: Iron Will
- name: Multiattack
- name: Weapon Focus (bite)
- name: Wingover
skills:
  Acrobatics: 12
  Bluff: 16
  Diplomacy: 13
  Fly: 19
  Intimidate: 16
  Knowledge (arcana): 13
  Knowledge (planes): 13
  Perception: 14
  Sense Motive: 14
  Spellcraft: 11
  Stealth: 11
  Survival: 8
languages:
- Abyssal
- Aklo
- Draconic
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

# Dragon (Outer, Void), Young Void Dragon
This dragon’s ebony scales and horns are flecked with a substance that glows an eerie green. The folds of its wings ref lect a starry sky.
**Source** Bestiary 4 pg. 72
**XP** 6,400

NE Large dragon
**Init** +2; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +14

##### Defense

**AC** 22, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+2 Dex, +11 natural, –1 size)
**hp** 95 (10d12+30)
**Fort** +10, **Ref** +9, **Will** +10
**Immune** cold, _[[spells/Confusion|confusion]]_, _[[spells/Insanity|insanity]]_ effects, _[[universal monster rules/Paralysis|paralysis]]_, sleep

##### Offense
**Speed** 40 ft., fly 200 ft. (good)
**Melee** bite +15 (2d6+7 plus obliterate), 2 claws +14 (1d8+5), 2 wings +12 (1d6+2), tail slap +12 (1d8+7)
**Space** 10 ft., **Reach** 5 ft. (10 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (40-ft. cone, 6d8 cold, DC 18), obliterate (DC 18), suffocating breath (DC 18)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +13)
At will—_[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 14)
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 1st; concentration +4)
1st (4/day)—_[[spells/Hypnotism|hypnotism]]_ (DC 15), _[[spells/Mage Armor|mage armor]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 21, **Dex** 14, **Con** 17, **Int** 16, **Wis** 13, **Cha** 16
**Base Atk** +10; **CMB** +16; **CMD** 28 (32 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite), _[[feats/Wingover|Wingover]]_
**Skills** Acrobatics +12, Bluff +16, Diplomacy +13, Fly +19, Intimidate +16, Knowledge (arcana, planes) +13, Perception +14, Sense Motive +14, Spellcraft +11, Stealth +11, Survival +8
**Languages** Abyssal, Aklo, Draconic, Infernal
**SQ** _[[items/Weapon Magic Abilities/Agile|agile]]_, _[[universal monster rules/No Breath|no breath]]_, starflight

##### Ecology

**Environment** vacuum
**Organization** solitary
**Treasure** triple

##### Description

Void dragons have been tainted by long exposure to the terrible alien entities that dwell in deep space. Though some continue to struggle against the inevitable tide of annihilation, many have embraced the encroaching void and exist only to feed and destroy.
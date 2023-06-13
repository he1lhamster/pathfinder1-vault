---
cssclass: [monsters]
title1: Dragon (Esoteric, Occult), Young Occult Dragon
desc_short: Its parchment-colored scales rustling like dry leaves, this dragon seems
  unusually attentive, as if always on the lookout.
title2: Young Occult Dragon
CR: 6
sources:
- name: Bestiary 5
  page: 96
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 2400
alignment: NG
size: Medium
type: dragon
initiative:
  bonus: 2
senses:
  appraising sight: true
  dragon senses: true
auras:
- name: protective aura
  radius: 20
AC:
  AC: 21
  touch: 12
  flat_footed: 19
  components:
    dex: 2
    natural: 9
HP:
  HP: 57
  long: 6d12+18
saves:
  fort: 8
  ref: 7
  will: 7
immunities:
- paralysis
- sleep
SR: 17
speeds:
  base: 40
  fly: 150
  fly_maneuverability: average
attacks:
  melee:
  - - text: bite +10 (1d8+6)
      entries:
      - - damage: 1d8+6
      attack: bite
      bonus:
      - 10
    - text: 2 claws +10 (1d6+4)
      entries:
      - - damage: 1d6+4
      count: 2
      attack: claws
      bonus:
      - 10
    - text: 2 wings +8 (1d4+2)
      entries:
      - - damage: 1d4+2
      count: 2
      attack: wings
      bonus:
      - 8
  special:
  - breath weapon (30-ft. cone, DC 16, 6d6 cold or fire)
space: 5
reach: 5
reach_other: 10 ft. with bite
psychic_magic:
  entries:
  - name: forbid action
    PE: 1
    DC: 14
  - name: mending
    PE: 0
  sources:
  - name: default
    CL: 6
    concentration: 9
  PE: 3
spells:
  entries:
  - name: mage armor
    source: Psychic
    level: 1
  - name: sleep
    source: Psychic
    level: 1
    DC: 14
  - name: detect magic
    source: Psychic
    level: 0
  - name: detect psychic significance
    source: Psychic
    level: 0
  - name: mage hand
    source: Psychic
    level: 0
  - name: read magic
    source: Psychic
    level: 0
  sources:
  - name: Psychic
    type: known
    CL: 1
    concentration: 4
    slots:
      1: 4
      0: at-will
ability_scores:
  STR: 18
  DEX: 14
  CON: 17
  INT: 16
  WIS: 14
  CHA: 13
BAB: 6
CMB: 10
CMD: 22
CMD_other: 26 vs. trip
feats:
- name: Deceitful
- name: Multiattack
- name: Skill Focus (Perception)
skills:
  Appraise: 12
  Bluff: 12
  Disguise: 9
  Fly: 11
  Knowledge (arcana): 12
  Knowledge (history): 12
  Knowledge (religion): 12
  Perception: 14
  Sense Motive: 11
languages:
- Celestial
- Common
- Draconic
desc_long: Occult dragons infiltrate large urban centers in humanoid form to search
  for esoteric secrets and psychically charged artifacts to add to their hoards.

---

# Dragon (Esoteric, Occult), Young Occult Dragon
Its parchment-colored scales rustling like dry leaves, this dragon seems unusually attentive, as if always on the _[[feats/Lookout|lookout]]_.
**Source** Bestiary 5 pg. 96
**XP** 2,400

NG Medium dragon
**Init** +2; **Senses** appraising sight, _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +14
**Aura** protective aura (20 ft.)

##### Defense

**AC** 21, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+2 Dex, +9 natural)
**hp** 57 (6d12+18)
**Fort** +8, **Ref** +7, **Will** +7
**Immune** _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 17

##### Offense
**Speed** 40 ft., fly 150 ft. (average)
**Melee** bite +10 (1d8+6), 2 claws +10 (1d6+4), 2 wings +8 (1d4+2)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (30-ft. cone, DC 16, 6d6 cold or fire)
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_** (CL 6th; concentration +9)
3 PE—_[[spells/Forbid Action|forbid action]]_ (1 PE, DC 14), _[[spells/Mending|mending]]_ (0 PE)
 **_[[classes/Psychic|Psychic]]_ Spells Known** (CL 1st; concentration +4)
 1st (4/day)—_[[spells/Mage Armor|mage armor]]_, sleep (DC 14)
 0 (at-will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Detect _Psychic_ Significance|detect _psychic_ significance]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 18, **Dex** 14, **Con** 17, **Int** 16, **Wis** 14, **Cha** 13
**Base Atk** +6; **CMB** +10; **CMD** 22 (26 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Deceitful|Deceitful]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** Appraise +12, Bluff +12, Disguise +9, Fly +11, Knowledge (arcana, history, religion) +12, Perception +14, Sense Motive +11
**Languages** Celestial, Common, Draconic

##### Description

Occult dragons infiltrate large urban centers in humanoid form to search for esoteric secrets and psychically charged artifacts to add to their hoards.
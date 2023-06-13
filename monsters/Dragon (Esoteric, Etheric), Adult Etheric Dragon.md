---
cssclass: [monsters]
title1: Dragon (Esoteric, Etheric), Adult Etheric Dragon
title2: Adult Etheric Dragon
CR: 11
sources:
- name: Bestiary 5
  page: 92
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 12800
alignment: N
size: Large
type: dragon
subtypes:
- extraplanar
initiative:
  bonus: 4
senses:
  dragon senses: true
  see in darkness: true
auras:
- name: frightful presence
  radius: 180
  DC: 20
AC:
  AC: 27
  touch: 9
  flat_footed: 27
  components:
    natural: 18
    size: -1
HP:
  HP: 175
  long: 14d12+84
saves:
  fort: 15
  ref: 9
  will: 12
DR:
- amount: 5
  weakness: magic
immunities:
- paralysis
- sleep
SR: 22
speeds:
  base: 40
  other_semicolon: ghost stride
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +23 (2d6+15)
      entries:
      - - damage: 2d6+15
      attack: bite
      bonus:
      - 23
    - text: 2 claws +24 (1d8+10)
      entries:
      - - damage: 1d8+10
      count: 2
      attack: claws
      bonus:
      - 24
    - text: 2 wings +21 (1d6+5)
      entries:
      - - damage: 1d6+5
      count: 2
      attack: wings
      bonus:
      - 21
    - text: tail slap +21 (1d8+15)
      entries:
      - - damage: 1d8+15
      attack: tail slap
      bonus:
      - 21
  special:
  - breath weapon (80-ft. line, DC 23, 12d8 force)
  - spectral attacks
  - spirit eater
space: 10
reach: 5
reach_other: 10 ft. with bite
psychic_magic:
  entries:
  - name: mage hand
    PE: 0
  - name: mind thrust I
    PE: 1
  sources:
  - name: default
    CL: 14
    concentration: 17
  PE: 9
spells:
  entries:
  - name: blindness/deafness
    source: Psychic
    level: 2
    DC: 15
  - name: false life
    source: Psychic
    level: 2
  - name: anticipate peril
    source: Psychic
    level: 1
  - name: detect thoughts
    source: Psychic
    level: 1
    DC: 14
  - name: magic missile
    source: Psychic
    level: 1
  - name: shield
    source: Psychic
    level: 1
  - name: bleed
    source: Psychic
    level: 0
    DC: 13
  - name: detect magic
    source: Psychic
    level: 0
  - name: detect poison
    source: Psychic
    level: 0
  - name: ghost sound
    source: Psychic
    level: 0
    DC: 13
  - name: grave words
    source: Psychic
    level: 0
  sources:
  - name: Psychic
    type: known
    CL: 5
    concentration: 9
    slots:
      2: 5
      1: 7
      0: at-will
ability_scores:
  STR: 30
  DEX: 11
  CON: 22
  INT: 19
  WIS: 16
  CHA: 17
BAB: 14
CMB: 25
CMD: 35
CMD_other: 39 vs. trip
feats:
- name: Flyby Attack
- name: Improved Initiative
- name: Intimidating Prowess
- name: Multiattack
- name: Power Attack
- name: Skill Focus (Perception)
- name: Weapon Focus (claw)
skills:
  Appraise: 21
  Fly: 11
  Intimidate: 30
  Knowledge (arcana): 21
  Knowledge (planes): 21
  Knowledge (religion): 21
  Perception: 26
  Sense Motive: 20
  Stealth: 13
  Survival: 20
languages:
- Aklo
- Common
- Draconic
special_qualities:
- compression
desc_long: Etheric dragons are pragmatic and survival-oriented beings who dwell in
  the farthest reaches of the Ethereal Plane.

---

# Dragon (Esoteric, Etheric), Adult Etheric Dragon

**Source** Bestiary 5 pg. 92
**XP** 12,800

N Large dragon (extraplanar)
**Init** +4; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +26
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 20)

##### Defense

**AC** 27, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+18 natural, –1 size)
**hp** 175 (14d12+84)
**Fort** +15, **Ref** +9, **Will** +12
**DR** 5/magic; **Immune** _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 22

##### Offense
**Speed** 40 ft., fly 200 ft. (poor); _[[monsters/Ghost|ghost]]_ stride
**Melee** bite +23 (2d6+15), 2 claws +24 (1d8+10), 2 wings +21 (1d6+5), tail slap +21 (1d8+15)
**Space** 10 ft., **Reach** 5 ft. (10 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (80-ft. line, DC 23, 12d8 force), spectral attacks, spirit eater
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_** (CL 14th; concentration +17)
9 PE—_[[spells/Mage Hand|mage hand]]_ (0 PE), _[[spells/Mind Thrust I|mind thrust I]]_ (1 PE)
 **_[[classes/Psychic|Psychic]]_ Spells Known** (CL 5th; concentration +9)
 2nd (5/day)—blindness/deafness (DC 15), _[[spells/False Life|false life]]_
 1st (7/day)—_[[spells/Anticipate Peril|anticipate peril]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 14), _[[spells/Magic Missile|magic missile]]_, _[[spells/Shield|shield]]_
 0 (at-will)—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 13), _[[spells/Grave Words|grave words]]_

##### Statistics
**Str** 30, **Dex** 11, **Con** 22, **Int** 19, **Wis** 16, **Cha** 17
**Base Atk** +14; **CMB** +25; **CMD** 35 (39 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Intimidating Prowess|Intimidating Prowess]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Appraise +21, Fly +11, Intimidate +30, Knowledge (arcana, planes, religion) +21, Perception +26, Sense Motive +20, Stealth +13, Survival +20
**Languages** Aklo, Common, Draconic
**SQ** _[[universal monster rules/Compression|compression]]_

Etheric dragons are pragmatic and survival-oriented beings who dwell in the farthest reaches of the Ethereal Plane.
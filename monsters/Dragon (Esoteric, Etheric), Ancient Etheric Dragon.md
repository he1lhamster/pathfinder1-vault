---
cssclass: [monsters]
title1: Dragon (Esoteric, Etheric), Ancient Etheric Dragon
title2: Ancient Etheric Dragon
CR: 16
sources:
- name: Bestiary 5
  page: 93
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 76800
alignment: N
size: Huge
type: dragon
subtypes:
- extraplanar
initiative:
  bonus: 3
senses:
  dragon senses: true
  see in darkness: true
auras:
- name: frightful presence
  radius: 300
  DC: 25
AC:
  AC: 37
  touch: 7
  flat_footed: 37
  components:
    dex: -1
    natural: 30
    size: -2
HP:
  HP: 319
  long: 22d12+176
saves:
  fort: 21
  ref: 12
  will: 18
DR:
- amount: 15
  weakness: magic
immunities:
- paralysis
- sleep
SR: 27
speeds:
  base: 40
  other_semicolon: ghost stride
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +34 (2d8+21/19-20)
      entries:
      - - damage: 2d8+21
          crit_range: 19-20
      attack: bite
      bonus:
      - 34
    - text: 2 claws +35 (2d6+14/19-20)
      entries:
      - - damage: 2d6+14
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 35
    - text: 2 wings +32 (1d8+7)
      entries:
      - - damage: 1d8+7
      count: 2
      attack: wings
      bonus:
      - 32
    - text: tail slap +32 (2d6+21)
      entries:
      - - damage: 2d6+21
      attack: tail slap
      bonus:
      - 32
  special:
  - crush
  - breath weapon (100-ft. line, DC 28, 20d8 force)
  - grave breath
  - spectral attacks
  - spirit eater
space: 15
reach: 10
reach_other: 15 ft. with bite
psychic_magic:
  entries:
  - name: chill metal
    PE: 2
    DC: 17
  - name: mage hand
    PE: 0
  - name: mind thrust I
    PE: 1
  - name: telekinetic maneuver
    PE: 3
  sources:
  - name: default
    CL: 21
    concentration: 27
  PE: 17
spells:
  entries:
  - name: contingency
    source: Psychic
    level: 6
  - name: heroism
    source: Psychic
    level: 6
    other: greater
  - name: hold monster
    source: Psychic
    level: 5
    DC: 20
  - name: plane shift
    source: Psychic
    level: 5
    DC: 20
  - name: wall of ectoplasm
    source: Psychic
    level: 5
    DC: 20
  - name: arcane eye
    source: Psychic
    level: 4
  - name: condensed ether
    source: Psychic
    level: 4
  - name: dimension door
    source: Psychic
    level: 4
  - name: phantasmal killer
    source: Psychic
    level: 4
    DC: 19
  - name: aura sight
    source: Psychic
    level: 3
  - name: deep slumber
    source: Psychic
    level: 3
    DC: 18
  - name: heroism
    source: Psychic
    level: 3
  - name: thought shield II
    source: Psychic
    level: 3
  - name: blindness/deafness
    source: Psychic
    level: 2
    DC: 17
  - name: false life
    source: Psychic
    level: 2
  - name: pain strike
    source: Psychic
    level: 2
  - name: see invisibility
    source: Psychic
    level: 2
  - name: silence
    source: Psychic
    level: 2
    DC: 17
  - name: anticipate peril
    source: Psychic
    level: 1
  - name: detect thoughts
    source: Psychic
    level: 1
    DC: 16
  - name: shield
    source: Psychic
    level: 1
  - name: silent image
    source: Psychic
    level: 1
    DC: 16
  - name: magic missile
    source: Psychic
    level: 1
  - name: bleed
    source: Psychic
    level: 0
    DC: 15
  - name: dancing lights
    source: Psychic
    level: 0
  - name: daze
    source: Psychic
    level: 0
    DC: 15
  - name: detect magic
    source: Psychic
    level: 0
  - name: detect poison
    source: Psychic
    level: 0
  - name: ghost sound
    source: Psychic
    level: 0
    DC: 15
  - name: grave words
    source: Psychic
    level: 0
  - name: resistance
    source: Psychic
    level: 0
  - name: virtue
    source: Psychic
    level: 0
  sources:
  - name: Psychic
    type: known
    CL: 13
    concentration: 19
    slots:
      6: 5
      5: 7
      4: 7
      3: 7
      2: 8
      1: 8
      0: at-will
ability_scores:
  STR: 38
  DEX: 9
  CON: 26
  INT: 23
  WIS: 20
  CHA: 21
BAB: 22
CMB: 38
CMD: 47
CMD_other: 51 vs. trip
feats:
- name: Flyby Attack
- name: Hover
- name: Improved Critical (bite)
- name: Improved Critical (claws)
- name: Improved Initiative
- name: Intimidating Prowess
- name: Multiattack
- name: Power Attack
- name: Skill Focus (Perception)
- name: Vital Strike
- name: Weapon Focus (claw)
skills:
  Appraise: 31
  Bluff: 30
  Fly: 16
  Intimidate: 44
  Knowledge (arcana): 31
  Knowledge (geography): 31
  Knowledge (planes): 31
  Knowledge (religion): 31
  Perception: 36
  Sense Motive: 30
  Stealth: 16
  Survival: 30
languages:
- Abyssal
- Aklo
- Common
- Draconic
- Infernal
special_qualities:
- compression
desc_long: Etheric dragons are pragmatic and survival-oriented beings who dwell in
  the farthest reaches of the Ethereal Plane.

---

# Dragon (Esoteric, Etheric), Ancient Etheric Dragon

**Source** Bestiary 5 pg. 93
**XP** 76,800

N Huge dragon (extraplanar)
**Init** +3; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +36
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 25)

##### Defense

**AC** 37, touch 7, _[[conditions/Flat-Footed|flat-footed]]_ 37 (–1 Dex, +30 natural, –2 size)
**hp** 319 (22d12+176)
**Fort** +21, **Ref** +12, **Will** +18
**DR** 15/magic; **Immune** _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 27

##### Offense
**Speed** 40 ft., fly 200 ft. (poor); _[[monsters/Ghost|ghost]]_ stride
**Melee** bite +34 (2d8+21/19–20), 2 claws +35 (2d6+14/19–20), 2 wings +32 (1d8+7), tail slap +32 (2d6+21)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** crush, _[[universal monster rules/Breath Weapon|breath weapon]]_ (100-ft. line, DC 28, 20d8 force), grave breath, spectral attacks, spirit eater
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_** (CL 21st; concentration +27)
17 PE—_[[spells/Chill Metal|chill metal]]_ (2 PE, DC 17), _[[spells/Mage Hand|mage hand]]_ (0 PE), _[[spells/Mind Thrust I|mind thrust I]]_ (1 PE), _[[spells/Telekinetic Maneuver|telekinetic maneuver]]_ (3 PE)
 **_[[classes/Psychic|Psychic]]_ Spells Known** (CL 13th; concentration +19)
 6th (5/day)—_[[spells/Contingency|contingency]]_, _[[spells/Heroism|heroism]]_ (greater)
 5th (7/day)—_[[spells/Hold Monster|hold monster]]_ (DC 20), _[[spells/Plane Shift|plane shift]]_ (DC 20), _[[spells/Wall Of Ectoplasm|wall of ectoplasm]]_ (DC 20)
 4th (7/day)—_[[spells/Arcane Eye|arcane eye]]_, _[[spells/Condensed Ether|condensed ether]]_, _[[spells/Dimension Door|dimension door]]_, _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 19)
 3rd (7/day)—_[[spells/Aura Sight|aura sight]]_, _[[spells/Deep Slumber|deep slumber]]_ (DC 18), _heroism_, _[[spells/Thought _[[spells/Shield|Shield]]_ II|thought _shield_ II]]_
 2nd (8/day)—blindness/deafness (DC 17), _[[spells/False Life|false life]]_, _[[spells/Pain Strike|pain strike]]_, _[[spells/See Invisibility|see invisibility]]_, _[[spells/Silence|silence]]_ (DC 17)
 1st (8/day)—_[[spells/Anticipate Peril|anticipate peril]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 16), _shield_, _[[spells/Silent Image|silent image]]_ (DC 16), _[[spells/Magic Missile|magic missile]]_
 0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 15), _[[spells/Grave Words|grave words]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Virtue|virtue]]_

##### Statistics
**Str** 38, **Dex** 9, **Con** 26, **Int** 23, **Wis** 20, **Cha** 21
**Base Atk** +22; **CMB** +38; **CMD** 47 (51 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _Improved Critical_ (claws), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Intimidating Prowess|Intimidating Prowess]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Appraise +31, Bluff +30, Fly +16, Intimidate +44, Knowledge (arcana, geography, planes, religion) +31, Perception +36, Sense Motive +30, Stealth +16, Survival +30
**Languages** Abyssal, Aklo, Common, Draconic, Infernal
**SQ** _[[universal monster rules/Compression|compression]]_

Etheric dragons are pragmatic and survival-oriented beings who dwell in the farthest reaches of the Ethereal Plane.
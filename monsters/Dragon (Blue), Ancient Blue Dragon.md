---
cssclass: [monsters]
title1: Dragon (Blue), Ancient Blue Dragon
title2: Ancient Blue Dragon
CR: 18
sources:
- name: Pathfinder RPG Bestiary
  page: 95
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 153600
alignment: LE
size: Gargantuan
type: dragon
subtypes:
- earth
initiative:
  bonus: 3
senses:
  dragon senses: true
auras:
- name: electricity
  radius: 10
  other:
  - 2d6 electricity
- name: frightful presence
  radius: 300
  DC: 27
AC:
  AC: 37
  touch: 5
  flat_footed: 37
  components:
    dex: -1
    natural: 32
    size: -4
HP:
  HP: 324
  long: 24d12+168
saves:
  fort: 21
  ref: 13
  will: 19
DR:
- amount: 15
  weakness: magic
immunities:
- electricity
- paralysis
- sleep
SR: 29
speeds:
  base: 40
  burrow: 20
  fly: 250
  fly_maneuverability: clumsy
attacks:
  melee:
  - - text: bite +33 (4d6+18/19-20)
      entries:
      - - damage: 4d6+18
          crit_range: 19-20
      attack: bite
      bonus:
      - 33
    - text: 2 claws +32 (2d8+12)
      entries:
      - - damage: 2d8+12
      count: 2
      attack: claws
      bonus:
      - 32
    - text: 2 wings +30 (2d6+6)
      entries:
      - - damage: 2d6+6
      count: 2
      attack: wings
      bonus:
      - 30
    - text: tail slap +30 (2d8+18)
      entries:
      - - damage: 2d8+18
      attack: tail slap
      bonus:
      - 30
  special:
  - breath weapon (120-ft. line, DC 29, 20d8 electricity)
  - crush
  - desert thirst (DC 27)
  - mirage
  - storm breath (DC 29, 20d8 electricity)
  - tail sweep
space: 20
reach: 15
reach_other: 20 ft. with bite
spell_like_abilities:
  entries:
  - name: ghost sound
    source: default
    freq: At will
    DC: 15
  - name: hallucinatory terrain
    source: default
    freq: At will
    DC: 19
  - name: minor image
    source: default
    freq: At will
    DC: 17
  - name: veil
    source: default
    freq: At will
  - name: ventriloquism
    source: default
    freq: At will
    DC: 16
  sources:
  - name: default
    CL: 24
spells:
  entries:
  - name: forceful hand
    source: '?'
    level: 6
  - name: mislead
    source: '?'
    level: 6
  - name: dream
    source: '?'
    level: 5
  - name: persistent image
    source: '?'
    level: 5
  - name: hold monster
    source: '?'
    level: 5
    DC: 20
  - name: dimension door
    source: '?'
    level: 4
  - name: enervation
    source: '?'
    level: 4
  - name: fire shield
    source: '?'
    level: 4
  - name: stoneskin
    source: '?'
    level: 4
  - name: dispel magic
    source: '?'
    level: 3
  - name: displacement
    source: '?'
    level: 3
  - name: haste
    source: '?'
    level: 3
  - name: vampiric touch
    source: '?'
    level: 3
  - name: darkness
    source: '?'
    level: 2
  - name: false life
    source: '?'
    level: 2
  - name: invisibility
    source: '?'
    level: 2
  - name: resist energy
    source: '?'
    level: 2
  - name: shatter
    source: '?'
    level: 2
  - name: alarm
    source: '?'
    level: 1
  - name: mage armor
    source: '?'
    level: 1
  - name: shield
    source: '?'
    level: 1
  - name: true strike
    source: '?'
    level: 1
  - name: unseen servant
    source: '?'
    level: 1
  - name: arcane mark
    source: '?'
    level: 0
  - name: bleed
    source: '?'
    level: 0
    DC: 15
  - name: detect magic
    source: '?'
    level: 0
  - name: light
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: mending
    source: '?'
    level: 0
  - name: message
    source: '?'
    level: 0
  - name: read magic
    source: '?'
    level: 0
  - name: resistance
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 13
    slots:
      6: 4
      5: 7
      4: 7
      3: 7
      2: 7
      1: 7
      0: at-will
ability_scores:
  STR: 35
  DEX: 8
  CON: 25
  INT: 20
  WIS: 21
  CHA: 20
BAB: 24
CMB: 40
CMD: 49
CMD_other: 53 vs. trip
feats:
- name: Combat Casting
- name: Dazzling Display
- name: Deadly Stroke
- name: Extend Spell
- name: Hover
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Multiattack
- name: Quicken Spell
- name: Silent Spell
- name: Shatter Defenses
- name: Weapon Focus (bite)
skills:
  Bluff: 32
  Fly: 10
  Intimidate: 32
  Knowledge (arcana): 32
  Knowledge (history): 32
  Knowledge (local): 32
  Knowledge (geography): 32
  Perception: 32
  Spellcraft: 32
  Stealth: 14
  Survival: 32
languages:
- Auran
- Common
- Draconic
- Giant
- Ignan
- Infernal
special_qualities:
- sound imitation
ecology:
  environment: warm deserts
desc_long: Blue dragons are consummate schemers and obsessively orderly. In combat,
  blue dragons prefer to surprise foes if possible, and are not above retreating if
  the odds turn against them. They prefer to lair near those that they control, sometimes
  even within the confines of a city.

---

# Dragon (Blue), Ancient Blue Dragon

**Source** Pathfinder RPG Bestiary pg. 95
**XP** 153,600

LE Gargantuan dragon (earth)
**Init** +3; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +32
**Aura** electricity (10 ft., 2d6 electricity), _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 27)

##### Defense

**AC** 37, touch 5, _[[conditions/Flat-Footed|flat-footed]]_ 37 (–1 Dex, +32 natural, –4 size)
**hp** 324 (24d12+168)
**Fort** +21, **Ref** +13, **Will** +19
**DR** 15/magic; **Immune** electricity, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 29

##### Offense
**Speed** 40 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft., fly 250 ft. (clumsy)
**Melee** bite +33 (4d6+18/19–20), 2 claws +32 (2d8+12), 2 wings +30 (2d6+6), tail slap +30 (2d8+18)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (120-ft. line, DC 29, 20d8 electricity), crush, desert thirst (DC 27), _[[spells/Mirage|mirage]]_, storm breath (DC 29, 20d8 electricity), tail sweep
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 24th)
At will—_[[spells/Ghost Sound|ghost sound]]_ (DC 15), _[[spells/Hallucinatory Terrain|hallucinatory terrain]]_ (DC 19), _[[spells/Minor Image|minor image]]_ (DC 17), _[[spells/Veil|veil]]_, _[[spells/Ventriloquism|ventriloquism]]_ (DC 16)
**Spells Known **(CL 13th)
6th (4/day)—_[[spells/Forceful Hand|forceful hand]]_, _[[spells/Mislead|mislead]]_
5th (7/day)—_[[spells/Dream|dream]]_, _[[spells/Persistent Image|persistent image]]_, _[[spells/Hold Monster|hold monster]]_ (DC 20)
4th (7/day)—_[[spells/Dimension Door|dimension door]]_, _[[spells/Enervation|enervation]]_, _[[spells/Fire Shield|fire shield]]_, _[[spells/Stoneskin|stoneskin]]_
3rd (7/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Displacement|displacement]]_, _[[spells/Haste|haste]]_, _[[spells/Vampiric Touch|vampiric touch]]_
2nd (7/day)—_[[spells/Darkness|darkness]]_, _[[spells/False Life|false life]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Resist Energy|resist energy]]_, _[[spells/Shatter|shatter]]_
1st (7/day)—_[[spells/Alarm|alarm]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_, _[[spells/Unseen Servant|unseen servant]]_
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Message|message]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_

##### Statistics
**Str** 35, **Dex** 8, **Con** 25, **Int** 20, **Wis** 21, **Cha** 20
**Base Atk** +24; **CMB** +40; **CMD** 49 (53 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Dazzling Display|Dazzling Display]]_, _[[feats/Deadly Stroke|Deadly Stroke]]_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Silent Spell|Silent Spell]]_, _[[feats/Shatter Defenses|Shatter Defenses]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Bluff +32, Fly +10, Intimidate +32, Knowledge (arcana) +32, Knowledge (history) +32, Knowledge (local) +32, Knowledge (geography) +32, Perception +32, Spellcraft +32, Stealth +14, Survival +32
**Languages** Auran, Common, Draconic, Giant, Ignan, Infernal
**SQ** sound imitation

##### Ecology

**Environment** warm deserts

Blue dragons are consummate schemers and obsessively orderly. In combat, blue dragons prefer to surprise foes if possible, and are not above retreating if the odds turn against them. They prefer to lair near those that they control, sometimes even within the confines of a city.
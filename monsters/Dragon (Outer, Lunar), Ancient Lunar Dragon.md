---
cssclass: [monsters]
title1: Dragon (Outer, Lunar), Ancient Lunar Dragon
title2: Ancient Lunar Dragon
CR: 18
sources:
- name: Bestiary 4
  page: 67
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 153600
alignment: CN
size: Gargantuan
type: dragon
initiative:
  bonus: 2
senses:
  dragon senses: true
  see in darkness: true
auras:
- name: alien presence
  radius: 300
  DC: 29
AC:
  AC: 37
  touch: 4
  flat_footed: 37
  components:
    dex: -2
    natural: 33
    size: -4
HP:
  HP: 348
  long: 24d12+192
saves:
  fort: 21
  ref: 12
  will: 22
defensive_abilities:
- reflect rays
- reflected light
DR:
- amount: 15
  weakness: magic
immunities:
- cold
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
  - - text: bite +32 (4d6+18)
      entries:
      - - damage: 4d6+18
      attack: bite
      bonus:
      - 32
    - text: 2 claws +32 (2d8+12)
      entries:
      - - damage: 2d8+12
      count: 2
      attack: claws
      bonus:
      - 32
    - text: 2 wings +30 (2d8+6)
      entries:
      - - damage: 2d8+6
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
  - bewildering breath
  - breath weapon (120-ft. line, 20d8 cold, DC 29)
  - crush
  - moonsilver
  - tail sweep
space: 20
reach: 15
reach_other: 20 ft. with bite
spell_like_abilities:
  entries:
  - name: dancing lights
    source: default
    freq: At will
  - superscripts:
    - APG
    name: life bubble
    source: default
    freq: At will
  - superscripts:
    - APG
    name: moonstruck
    source: default
    freq: At will
  - name: scrying
    source: default
    freq: At will
  - superscripts:
    - APG
    name: quickened moonstruck
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 24
    concentration: 31
spells:
  entries:
  - name: greater teleport
    source: Sorcerer
    level: 7
  - name: waves of exhaustion
    source: Sorcerer
    level: 7
  - superscripts:
    - UM
    name: cold ice strike
    source: Sorcerer
    level: 6
    DC: 23
  - name: greater dispel magic
    source: Sorcerer
    level: 6
  - name: true seeing
    source: Sorcerer
    level: 6
  - name: dominate person
    source: Sorcerer
    level: 5
    DC: 22
  - name: feeblemind
    source: Sorcerer
    level: 5
    DC: 22
  - name: fire snake
    source: Sorcerer
    level: 5
    DC: 22
  - name: mage's private sanctum
    source: Sorcerer
    level: 5
  - name: charm monster
    source: Sorcerer
    level: 4
    DC: 21
  - name: fire shield
    source: Sorcerer
    level: 4
  - name: greater invisibility
    source: Sorcerer
    level: 4
  - name: lesser globe of invulnerability
    source: Sorcerer
    level: 4
  - name: haste
    source: Sorcerer
    level: 3
  - name: heroism
    source: Sorcerer
    level: 3
  - name: tongues
    source: Sorcerer
    level: 3
  - name: vampiric touch
    source: Sorcerer
    level: 3
  - name: bear's endurance
    source: Sorcerer
    level: 2
  - name: detect thoughts
    source: Sorcerer
    level: 2
    DC: 19
  - name: hypnotic pattern
    source: Sorcerer
    level: 2
    DC: 19
  - name: minor image
    source: Sorcerer
    level: 2
    DC: 19
  - name: mirror image
    source: Sorcerer
    level: 2
  - name: comprehend languages
    source: Sorcerer
    level: 1
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: protection from evil
    source: Sorcerer
    level: 1
  - name: shocking grasp
    source: Sorcerer
    level: 1
  - superscripts:
    - APG
    name: vanish
    source: Sorcerer
    level: 1
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: light
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
    CL: 15
    concentration: 22
    slots:
      7: 5
      6: 7
      5: 7
      4: 7
      3: 8
      2: 8
      1: 8
      0: at-will
ability_scores:
  STR: 35
  DEX: 7
  CON: 24
  INT: 24
  WIS: 26
  CHA: 25
BAB: 24
CMB: 40
CMD: 48
CMD_other: 52 vs. trip
feats:
- name: Arcane Strike
- name: Combat Casting
- superscripts:
  - APG
  name: Dazing Assault
- name: Flyby Attack
- name: Improved Initiative
- name: Improved Vital Strike
- name: Multiattack
- name: Power Attack
- superscripts:
  - APG
  name: Quicken Spell-Like Ability (moonstruck)
- name: Toughness
- name: Vital Strike
- name: Wingover
skills:
  Bluff: 34
  Diplomacy: 34
  Fly: 11
  Intimidate: 34
  Knowledge (arcana): 30
  Knowledge (geography): 30
  Knowledge (history): 30
  Knowledge (local): 30
  Knowledge (nature): 30
  Knowledge (planes): 30
  Perception: 35
  Sense Motive: 35
  Spellcraft: 34
  Use Magic Device: 34
languages:
- Aklo
- Aquan
- Auran
- Common
- Draconic
- Ignan
- Terran
special_qualities:
- absolute cold
- no breath
- starflight
ecology:
  environment: vacuum
  organization: solitary
  treasure_type: triple
desc_long: Lunar dragons frequently interact with mortals, spending long hours watching
  the activities occurring on planets that interest them.

---

# Dragon (Outer, Lunar), Ancient Lunar Dragon

**Source** Bestiary 4 pg. 67
**XP** 153,600

CN Gargantuan dragon
**Init** +2; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +35
**Aura** alien presence (300 ft., DC 29)

##### Defense

**AC** 37, touch 4, _[[conditions/Flat-Footed|flat-footed]]_ 37 (–2 Dex, +33 natural, –4 size)
**hp** 348 (24d12+192)
**Fort** +21, **Ref** +12, **Will** +22
**Defensive Abilities** reflect rays, reflected light; **DR** 15/magic; **Immune** cold, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 29

##### Offense
**Speed** 40 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft., fly 250 ft. (clumsy)
**Melee** bite +32 (4d6+18), 2 claws +32 (2d8+12), 2 wings +30 (2d8+6), tail slap +30 (2d8+18)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite)
**Special Attacks** _[[items/Weapon Magic Abilities/Bewildering|bewildering]]_ breath, _[[universal monster rules/Breath Weapon|breath weapon]]_ (120-ft. line, 20d8 cold, DC 29), crush, moonsilver, tail sweep
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 24th; concentration +31)
At will—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Life Bubble|life bubble]]_, _[[spells/Moonstruck|moonstruck]]_, _[[spells/Scrying|scrying]]_
3/day—quickened _moonstruck_
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 15th; concentration +22)
7th (5/day)—greater teleport, _[[spells/Waves of Exhaustion|waves of exhaustion]]_
6th (7/day)—_[[spells/Cold Ice Strike|cold ice strike]]_ (DC 23), greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/True Seeing|true seeing]]_
5th (7/day)—_[[spells/Dominate Person|dominate person]]_ (DC 22), _[[spells/Feeblemind|feeblemind]]_ (DC 22), _[[spells/Fire Snake|fire snake]]_ (DC 22), mage’s private sanctum
4th (7/day)—_[[spells/Charm Monster|charm monster]]_ (DC 21), _[[spells/Fire Shield|fire shield]]_, greater _[[spells/Invisibility|invisibility]]_, lesser _[[spells/Globe Of Invulnerability|globe of invulnerability]]_
3rd (8/day)—_[[spells/Haste|haste]]_, _[[spells/Heroism|heroism]]_, _[[spells/Tongues|tongues]]_, _[[spells/Vampiric Touch|vampiric touch]]_
2nd (8/day)—bear’s _[[feats/Endurance|endurance]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 19), _[[spells/Hypnotic Pattern|hypnotic pattern]]_ (DC 19), _[[spells/Minor Image|minor image]]_ (DC 19), _[[spells/Mirror Image|mirror image]]_
1st (8/day)—_[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Protection From Evil|protection from evil]]_, _[[spells/Shocking Grasp|shocking grasp]]_, _[[spells/Vanish|vanish]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, light, _[[spells/Read Magic|read magic]]_, 4 more

##### Statistics
**Str** 35, **Dex** 7, **Con** 24, **Int** 24, **Wis** 26, **Cha** 25
**Base Atk** +24; **CMB** +40; **CMD** 48 (52 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Arcane Strike|Arcane Strike]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Dazing Assault|Dazing Assault]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_moonstruck_), _[[feats/Toughness|Toughness]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Wingover|Wingover]]_
**Skills** Bluff +34, Diplomacy +34, Fly +11, Intimidate +34, Knowledge (arcana, geography, history, local, nature, planes) +30, Perception +35, Sense Motive +35, Spellcraft +34, Use Magic Device +34
**Languages** Aklo, Aquan, Auran, Common, Draconic, Ignan, Terran
**SQ** absolute cold, _[[universal monster rules/No Breath|no breath]]_, starflight

##### Ecology

**Environment** vacuum
**Organization** solitary
**Treasure** triple

Lunar dragons frequently interact with mortals, spending long hours watching the activities occurring on planets that interest them.
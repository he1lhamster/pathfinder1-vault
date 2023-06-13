---
cssclass: [monsters]
title1: Dragon (White), Adult White Dragon
title2: Adult White Dragon
CR: 10
sources:
- name: Pathfinder RPG Bestiary
  page: 100
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 9600
alignment: CE
size: Large
type: dragon
subtypes:
- cold
initiative:
  bonus: 5
senses:
  dragon senses: true
  snow vision: true
auras:
- name: cold
  radius: 5
  other:
  - 1d6 cold damage
- name: frightful presence
  radius: 180
  DC: 17
AC:
  AC: 27
  touch: 10
  flat_footed: 26
  components:
    dex: 1
    natural: 17
    size: -1
HP:
  HP: 149
  long: 13d12+65
saves:
  fort: 13
  ref: 9
  will: 10
DR:
- amount: 5
  weakness: magic
immunities:
- cold
- paralysis
- sleep
SR: 21
weaknesses:
- vulnerability to fire
speeds:
  base: 30
  burrow: 30
  fly: 200
  fly_maneuverability: poor
  swim: 60
attacks:
  melee:
  - - text: bite +20 (2d6+10/19-20)
      entries:
      - - damage: 2d6+10
          crit_range: 19-20
      attack: bite
      bonus:
      - 20
    - text: 2 claws +19 (1d8+7)
      entries:
      - - damage: 1d8+7
      count: 2
      attack: claws
      bonus:
      - 19
    - text: 2 wings +14 (1d6+3)
      entries:
      - - damage: 1d6+3
      count: 2
      attack: wings
      bonus:
      - 14
    - text: tail slap +14 (1d8+10)
      entries:
      - - damage: 1d8+10
      attack: tail slap
      bonus:
      - 14
  special:
  - breath weapon (40-ft. cone, DC 21, 12d4 cold)
space: 10
reach: 5
reach_other: 10 ft. with bite
spell_like_abilities:
  entries:
  - name: fog cloud
    source: default
    freq: At will
  - name: gust of wind
    source: default
    freq: At will
  sources:
  - name: default
    CL: 13
spells:
  entries:
  - name: shield
    source: '?'
    level: 1
  - name: true strike
    source: '?'
    level: 1
  - name: dancing lights
    source: '?'
    level: 0
  - name: detect magic
    source: '?'
    level: 0
  - name: ray of frost
    source: '?'
    level: 0
  - name: mending
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 1
    slots:
      1: 4
      0: at-will
ability_scores:
  STR: 25
  DEX: 12
  CON: 21
  INT: 12
  WIS: 15
  CHA: 12
BAB: 13
CMB: 21
CMD: 32
CMD_other: 36 vs. trip
feats:
- name: Alertness
- name: Flyby Attack
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Power Attack
- name: Vital Strike
- name: Weapon Focus (bite)
skills:
  Fly: 11
  Intimidate: 17
  Knowledge (arcane): 17
  Perception: 22
  Spellcraft: 17
  Stealth: 13
  Swim: 31
languages:
- Common
- Draconic
special_qualities:
- icewalking
- ice shape
ecology:
  environment: cold mountains
desc_long: Although most consider it to be the weakest and most feral of the chromatic
  dragons, the white dragon makes up for its lack of cunning with sheer ferocity.
  White dragons dwell on remote, frozen mountaintops and in arctic lowlands, making
  their home in glittering caves full of ice and snow. They prefer their meals completely
  frozen.

---

# Dragon (White), Adult White Dragon

**Source** Pathfinder RPG Bestiary pg. 100
**XP** 9,600
CE Large dragon (cold)
**Init** +5; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, snow _[[spells/Vision|vision]]_; Perception +22
**Aura** cold (5 ft., 1d6 cold damage), _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 17)

##### Defense

**AC** 27, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+1 Dex, +17 natural, –1 size)
**hp** 149 (13d12+65)
**Fort** +13, **Ref** +9, **Will** +10
**DR** 5/magic; **Immune** cold, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 21
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to fire

##### Offense
**Speed** 30 ft., _[[universal monster rules/Burrow|burrow]]_ 30 ft., fly 200 ft. (poor), swim 60 ft.
**Melee** bite +20 (2d6+10/19–20), 2 claws +19 (1d8+7), 2 wings +14 (1d6+3), tail slap +14 (1d8+10)
**Space** 10 ft., **Reach** 5 ft. (10 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (40-ft. cone, DC 21, 12d4 cold)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th)
At will—_[[spells/Fog Cloud|fog cloud]]_, _[[spells/Gust Of Wind|gust of wind]]_
**Spells Known **(CL 1st)
1st (4/day)—_[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Mending|mending]]_

##### Statistics
**Str** 25, **Dex** 12, **Con** 21, **Int** 12, **Wis** 15, **Cha** 12
**Base Atk** +13; **CMB** +21; **CMD** 32 (36 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Fly +11, Intimidate +17, Knowledge (arcane) +17, Perception +22, Spellcraft +17, Stealth +13, Swim +31
**Languages** Common, Draconic
**SQ** icewalking, ice shape

##### Ecology

**Environment** cold mountains

Although most consider it to be the weakest and most feral of the chromatic dragons, the white dragon makes up for its lack of _[[items/Weapon Magic Abilities/Cunning|cunning]]_ with sheer _[[universal monster rules/Ferocity|ferocity]]_. White dragons dwell on remote, frozen mountaintops and in arctic lowlands, making their home in glittering caves full of ice and snow. They prefer their meals completely frozen.
---
cssclass: [monsters]
title1: Dragon (Outer, Time), Adult Time Dragon
title2: Adult Time Dragon
CR: 15
sources:
- name: Bestiary 4
  page: 70
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 51200
alignment: N
size: Huge
type: dragon
initiative:
  bonus: 11
senses:
  detect magic: true
  dragon senses: true
  see in darkness: true
auras:
- name: alien presence
  radius: 180
  DC: 23
AC:
  AC: 28
  touch: 9
  flat_footed: 27
  components:
    dex: 1
    natural: 19
    size: -2
HP:
  HP: 256
  long: 19d12+133
saves:
  fort: 18
  ref: 12
  will: 15
DR:
- amount: 5
  weakness: magic
immunities:
- cold
- paralysis
- sleep
- staggered
SR: 26
speeds:
  base: 50
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +28 (2d8+15)
      entries:
      - - damage: 2d8+15
      attack: bite
      bonus:
      - 28
    - text: 2 claws +28 (2d6+10/19-20)
      entries:
      - - damage: 2d6+10
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 28
    - text: 2 wings +25 (1d8+5)
      entries:
      - - damage: 1d8+5
      count: 2
      attack: wings
      bonus:
      - 25
    - text: tail slap +25 (2d6+15)
      entries:
      - - damage: 2d6+15
      attack: tail slap
      bonus:
      - 25
  special:
  - breath weapon (50-ft. cone, 12d10 electricity, DC 26)
  - crush
space: 15
reach: 10
reach_other: 15 ft. with bite
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: clairaudience/clairvoyance
    source: default
    freq: At will
  - superscripts:
    - UM
    name: share memory
    source: default
    freq: At will
  sources:
  - name: default
    CL: 19
    concentration: 23
spells:
  entries:
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: slow
    source: Sorcerer
    level: 3
    DC: 17
  - name: arcane lock
    source: Sorcerer
    level: 2
  - name: blur
    source: Sorcerer
    level: 2
  - name: detect thoughts
    source: Sorcerer
    level: 2
    DC: 16
  - name: erase
    source: Sorcerer
    level: 1
  - name: feather fall
    source: Sorcerer
    level: 1
  - name: identify
    source: Sorcerer
    level: 1
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: light
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
  - name: 3 more
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 7
    concentration: 11
    slots:
      3: 5
      2: 7
      1: 7
      0: at-will
ability_scores:
  STR: 30
  DEX: 13
  CON: 24
  INT: 19
  WIS: 18
  CHA: 19
BAB: 19
CMB: 31
CMB_other: +33 sunder
CMD: 44
CMD_other: 48 vs. trip
feats:
- name: Cleave
- name: Great Cleave
- name: Improved Critical (claw)
- name: Improved Initiative
- name: Multiattack
- name: Power Attack
- name: Skill Focus (Knowledge [history])
- name: Step Up
- name: Weapon Focus (bite)
- name: Weapon Focus (claw)
skills:
  Diplomacy: 26
  Fly: 15
  Knowledge (arcana): 26
  Knowledge (geography): 26
  Knowledge (planes): 26
  Knowledge (religion): 26
  Knowledge (history): 32
  Perception: 26
  Sense Motive: 26
  Spellcraft: 26
languages:
- Common
- Draconic
- Dwarven
- Elven
- Sylvan
special_qualities:
- immortal
- no breath
- read the threads
- starflight
ecology:
  environment: vacuum
  organization: solitary
  treasure_type: triple
desc_long: Guardians of history, time dragons are the most powerful of the outer dragons.
  Watchers and waiters, time dragons guard the universe against those that would interfere
  with the natural temporal order.

---

# Dragon (Outer, Time), Adult Time Dragon

**Source** Bestiary 4 pg. 70
**XP** 51,200

N Huge dragon
**Init** +11; **Senses** _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/Dragon Senses|dragon senses]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +26
**Aura** alien presence (180 ft., DC 23)

##### Defense

**AC** 28, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+1 Dex, +19 natural, –2 size)
**hp** 256 (19d12+133)
**Fort** +18, **Ref** +12, **Will** +15
**DR** 5/magic; **Immune** cold, _[[universal monster rules/Paralysis|paralysis]]_, sleep, _[[conditions/Staggered|staggered]]_; **SR** 26

##### Offense
**Speed** 50 ft., fly 200 ft. (poor)
**Melee** bite +28 (2d8+15), 2 claws +28 (2d6+10/19–20), 2 wings +25 (1d8+5), tail slap +25 (2d6+15)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (50-ft. cone, 12d10 electricity, DC 26), crush
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 19th; concentration +23)
Constant—_detect magic_
At will—clairaudience/clairvoyance, _[[spells/Share Memory|share memory]]_
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 7th; concentration +11)
3rd (5/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Slow|slow]]_ (DC 17)
2nd (7/day)—_[[spells/Arcane Lock|arcane lock]]_, _[[spells/Blur|blur]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 16)
1st (7/day)—_[[spells/Erase|erase]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Identify|identify]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_
0 (at will)—light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Read Magic|read magic]]_, 3 more

##### Statistics
**Str** 30, **Dex** 13, **Con** 24, **Int** 19, **Wis** 18, **Cha** 19
**Base Atk** +19; **CMB** +31 (+33 sunder); **CMD** 44 (48 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Knowledge [history]), _[[feats/Step Up|Step Up]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite, claw)
**Skills** Diplomacy +26, Fly +15, Knowledge (arcana, geography, planes, religion) +26, Knowledge (history) +32, Perception +26, Sense Motive +26, Spellcraft +26
**Languages** Common, Draconic, Dwarven, Elven, Sylvan
**SQ** immortal, _[[universal monster rules/No Breath|no breath]]_, read the threads, starflight

##### Ecology

**Environment** vacuum
**Organization** solitary
**Treasure** triple

Guardians of history, time dragons are the most powerful of the outer dragons. Watchers and waiters, time dragons _[[npcs/Guard|guard]]_ the universe against those that would interfere with the natural temporal order.
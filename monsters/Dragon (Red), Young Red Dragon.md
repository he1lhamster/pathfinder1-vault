---
cssclass: [monsters]
title1: Dragon (Red), Young Red Dragon
desc_short: A ruddy glow emanates from beneath this dragon's red, gemencrusted scales,
  like lava visible between cracks of cooling stone.
title2: Mythic Young Red Dragon
CR: 12
MR: 5
sources:
- name: Mythic Adventures
  page: 190
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 19200
alignment: CE
size: Large
type: dragon
subtypes:
- fire
- mythic
initiative:
  bonus: 10
senses:
  blindsense: 60
  darkvision: 120
  low-light vision: true
  smoke vision: true
  x-ray vision: true
AC:
  AC: 27
  touch: 10
  flat_footed: 26
  components:
    dex: 1
    natural: 17
    size: -1
HP:
  HP: 165
  long: 11d12+94
  fast_healing: 5
saves:
  fort: 11
  ref: 8
  will: 10
defensive_abilities:
- dragon blood (1d6 fire)
- fortification (50%)
DR:
- amount: 10
  weakness: epic
immunities:
- dragon traits
- fire
- paralysis
- sleep
weaknesses:
- vulnerable to cold
speeds:
  base: 40
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +18 (2d6+10 plus grab)
      entries:
      - - damage: 2d6+10
        - effect: grab
      attack: bite
      bonus:
      - 18
    - text: 2 claws +18 (1d8+8 plus grab)
      entries:
      - - damage: 1d8+8
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 18
    - text: tail slap +13 (1d8+12)
      entries:
      - - damage: 1d8+12
      attack: tail slap
      bonus:
      - 13
    - text: 2 wings +13 (1d6+4)
      entries:
      - - damage: 1d6+4
      count: 2
      attack: wings
      bonus:
      - 13
  special:
  - breath weapon (40-ft. cone, 6d10 fire, Reflex DC 19 half, usable every 1d4 rounds)
  - lingering breath (2d6 fire, 5 rounds)
  - mythic power (5/day, surge +1d8)
  - swallow whole (1d6 bludgeoning and 1d6 fire damage, AC 18, 16 hp)
space: 10
reach: 5
reach_other: 10 ft. with bite
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: At will
  sources:
  - name: default
    CL: 11
    concentration: 13
spells:
  entries:
  - name: shield
    source: Sorcerer
    level: 1
  - name: true strike
    source: Sorcerer
    level: 1
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 1
    concentration: 3
    slots:
      1: 3
      0: at-will
ability_scores:
  STR: 27
  DEX: 12
  CON: 19
  INT: 12
  WIS: 13
  CHA: 14
BAB: 11
CMB: 20
CMB_other: +24 grapple
CMD: 31
CMD_other: 35 vs. trip
feats:
- name: Cleave
- is_mythic: true
  name: Improved Initiative
- name: Improved Vital Strike
- is_mythic: true
  name: Iron Will
- is_mythic: true
  name: Power Attack
- name: Vital Strike
skills:
  Appraise: 15
  Bluff: 16
  Fly: 9
  Intimidate: 16
  Perception: 15
  Sense Motive: 15
  Stealth: 11
languages:
- Common
- Draconic
special_qualities:
- dragon cantrips
ecology:
  environment: warm mountains
  organization: solitary
  treasure_type: triple
special_abilities:
  Smoke Vision (Ex): A very young red dragon can see perfectly in smoky conditions
    (such as those created by pyrotechnics).
desc_long: A young mythic red dragon is the offspring of an older mythic dragon, inheriting
  its power and rage. It tends to gorge itself on livestock, then sleep for nearly
  a year, only to repeat this cycle when it awakens again.

---

# Dragon (Red), Young Red Dragon
A crown of _[[items/Weapon Magic Abilities/Cruel|cruel]]_ horns surrounds the head of this mighty dragon. Thick scales the color of molten rock cover its long body.
**Source** Pathfinder RPG Bestiary pg. 98
**XP** 9,600
CE Large dragon (fire)
**Init** +5; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, smoke _[[spells/Vision|vision]]_; Perception +15

##### Defense

**AC** 22, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+1 Dex, +12 natural, –1 size)
**hp** 115 (11d12+44)
**Fort** +11, **Ref** +8, **Will** +10
**Immune** fire, _[[universal monster rules/Paralysis|paralysis]]_, sleep
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to cold

##### Offense
**Speed** 40 ft., fly 200 ft. (poor)
**Melee** bite +17 (2d6+10), 2 claws +17 (1d8+7), 2 wings +12 (1d6+3), tail slap +12 (1d8+10)
**Space** 10 ft., **Reach** 5 ft. (10 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (40-ft. cone, DC 19, 6d10 fire)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th)
At will—_[[spells/Detect Magic|detect magic]]_
**Spells Known **(CL 1st)
1st (3/day)—_[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 25, **Dex** 12, **Con** 19, **Int** 12, **Wis** 13, **Cha** 12
**Base Atk** +11; **CMB** +19; **CMD** 30 (34 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Appraise +15, Bluff +15, Fly +9, Intimidate +15, Perception +15, Sense Motive +15, Stealth +11
**Languages** Common, Draconic

##### Ecology

**Environment** warm mountains

##### Description

Few creatures are more _cruel_ and fearsome than the mighty red dragon. _[[npcs/King|King]]_ of the chromatics, this terrible beast brings ruin and death to the lands that fall under its _[[items/Armor Magic Abilities/Shadow|shadow]]_.
---
cssclass: [monsters]
title1: Dragon (Primal, Umbral), Young Umbral Dragon
desc_short: 'This sleek, dark dragon moves with a disturbing, serpentine grace, its
  eyes glowing as if lit from within by crimson embers. '
title2: Young Umbral Dragon
CR: 10
sources:
- name: Bestiary 2
  page: 102
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 9600
alignment: CE
size: Large
type: dragon
subtypes:
- extraplanar
initiative:
  bonus: 5
senses:
  dragon senses: true
AC:
  AC: 22
  touch: 10
  flat_footed: 21
  components:
    dex: 1
    natural: 12
    size: -1
HP:
  HP: 104
  long: 11d12+33
saves:
  fort: 10
  ref: 8
  will: 10
immunities:
- cold
- death effects
- energy drain
- paralysis
- sleep
speeds:
  base: 40
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +15 (2d6+7/19-20)
      entries:
      - - damage: 2d6+7
          crit_range: 19-20
      attack: bite
      bonus:
      - 15
    - text: 2 claws +15 (1d8+5)
      entries:
      - - damage: 1d8+5
      count: 2
      attack: claws
      bonus:
      - 15
    - text: 2 wings +13 (1d6+2)
      entries:
      - - damage: 1d6+2
      count: 2
      attack: wings
      bonus:
      - 13
    - text: tail slap +13 (1d8+7)
      entries:
      - - damage: 1d8+7
      attack: tail slap
      bonus:
      - 13
  special:
  - breath weapon (40-ft. cone, 6d8 neg. energy, DC 18)
space: 10
reach: 5
reach_other: 10 ft. with bite
spell_like_abilities:
  entries:
  - name: darkness
    source: default
    freq: At will
  sources:
  - name: default
    CL: 11
    concentration: 14
spells:
  entries:
  - name: inflict light wounds
    source: '?'
    level: 1
    DC: 14
  - name: shield
    source: '?'
    level: 1
  - name: bleed
    source: '?'
    level: 0
    DC: 13
  - name: detect magic
    source: '?'
    level: 0
  - name: detect poison
    source: '?'
    level: 0
  - name: read magic
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 1
    concentration: 4
    slots:
      1: 4
      0: at-will
ability_scores:
  STR: 21
  DEX: 12
  CON: 17
  INT: 16
  WIS: 17
  CHA: 16
BAB: 11
CMB: 17
CMD: 28
CMD_other: 32 vs. trip
feats:
- name: Hover
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Multiattack
- name: Power Attack
- name: Vital Strike
skills:
  Bluff: 17
  Diplomacy: 17
  Fly: 9
  Knowledge (arcana): 17
  Knowledge (local): 17
  Knowledge (planes): 17
  Perception: 17
  Sense Motive: 17
  Stealth: 11
languages:
- Abyssal
- Common
- Draconic
- Undercommon
special_qualities:
- ghost bane
- umbral scion
ecology:
  environment: any
  organization: solitary
  treasure_type: triple
desc_long: Cruel and sadistic, umbral dragons prefer the taste of undead flesh or
  ghostly ectoplasm, yet never turn down opportunities to consume living flesh.

---

# Dragon (Primal, Umbral), Young Umbral Dragon
This sleek, dark dragon moves with a disturbing, serpentine _[[spells/Grace|grace]]_, its eyes glowing as if lit from within by crimson embers.

**Source** Bestiary 2 pg. 102
**XP** 9,600
CE Large dragon (extraplanar)
**Init** +5; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +17

##### Defense

**AC** 22, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+1 Dex, +12 natural, –1 size)
**hp** 104 (11d12+33)
**Fort** +10, **Ref** +8, **Will** +10
**Immune** cold, death effects, _[[universal monster rules/Energy Drain|energy drain]]_, _[[universal monster rules/Paralysis|paralysis]]_, sleep

##### Offense
**Speed** 40 ft., fly 200 ft. (poor)
**Melee** bite +15 (2d6+7/19–20), 2 claws +15 (1d8+5), 2 wings +13 (1d6+2), tail slap +13 (1d8+7)
**Space** 10 ft., **Reach** 5 ft. (10 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (40-ft. cone, 6d8 neg. energy, DC 18)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +14)
At will—_[[spells/Darkness|darkness]]_
**Spells Known **(CL 1st; concentration +4)
1st (4/day)—_[[spells/Inflict Light Wounds|inflict light wounds]]_ (DC 14), _[[spells/Shield|shield]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 21, **Dex** 12, **Con** 17, **Int** 16, **Wis** 17, **Cha** 16
**Base Atk** +11; **CMB** +17; **CMD** 28 (32 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Bluff +17, Diplomacy +17, Fly +9, Knowledge (arcana, local, planes) +17, Perception +17, Sense Motive +17, Stealth +11
**Languages** Abyssal, Common, Draconic, Undercommon
**SQ** _[[monsters/Ghost|ghost]]_ _[[spells/Bane|bane]]_, _[[feats/Umbral Scion|umbral scion]]_

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** triple

##### Description

_[[items/Weapon Magic Abilities/Cruel|Cruel]]_ and sadistic, _[[items/Weapon Magic Abilities/Umbral|umbral]]_ dragons prefer the taste of undead flesh or ghostly ectoplasm, yet never turn down opportunities to consume living flesh.
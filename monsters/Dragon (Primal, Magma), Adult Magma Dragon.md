---
cssclass: [monsters]
title1: Dragon (Primal, Magma), Adult Magma Dragon
title2: Adult Magma Dragon
CR: 12
sources:
- name: Bestiary 2
  page: 100
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 19200
alignment: CN
size: Large
type: dragon
subtypes:
- extraplanar
- fire
initiative:
  bonus: 5
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 180
  DC: 20
AC:
  AC: 29
  touch: 10
  flat_footed: 28
  components:
    dex: 1
    natural: 19
    size: -1
HP:
  HP: 172
  long: 15d12+75
saves:
  fort: 16
  ref: 10
  will: 15
DR:
- amount: 5
  weakness: magic
immunities:
- fire
- paralysis
- sleep
SR: 23
weaknesses:
- vulnerable to cold
speeds:
  base: 40
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +22 (2d6+12/19-20 plus 6 fire)
      entries:
      - - damage: 2d6+12
          crit_range: 19-20
        - damage: '6'
          type: fire
      attack: bite
      bonus:
      - 22
    - text: 2 claws +22 (1d8+8/19-20)
      entries:
      - - damage: 1d8+8
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 22
    - text: tail slap +17 (1d8+12)
      entries:
      - - damage: 1d8+12
      attack: tail slap
      bonus:
      - 17
    - text: 2 wings +17 (1d6+4)
      entries:
      - - damage: 1d6+4
      count: 2
      attack: wings
      bonus:
      - 17
  special:
  - breath weapon (40-ft. cone, 12d6 fire, DC 22)
space: 10
reach: 5
reach_other: 10 ft. with bite
spell_like_abilities:
  entries:
  - name: burning hands
    source: default
    freq: At will
    DC: 14
  - name: scorching ray
    source: default
    freq: At will
  - name: wall of fire
    source: default
    freq: At will
  sources:
  - name: default
    CL: 15
    concentration: 18
spells:
  entries:
  - name: dispel magic
    source: '?'
    level: 3
  - name: fireball
    source: '?'
    level: 3
    DC: 16
  - name: dust of twilight
    source: '?'
    level: 2
  - name: flaming sphere
    source: '?'
    level: 2
    DC: 15
  - name: glitterdust
    source: '?'
    level: 2
    DC: 15
  - name: pyrotechnics
    source: '?'
    level: 2
    DC: 15
  - name: feather fall
    source: '?'
    level: 1
  - name: flare burst
    source: '?'
    level: 1
    DC: 14
  - name: grease
    source: '?'
    level: 1
    DC: 14
  - name: shield
    source: '?'
    level: 1
  - name: true strike
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
  - name: open/close
    source: '?'
    level: 0
  - name: read magic
    source: '?'
    level: 0
  - name: spark
    source: '?'
    level: 0
  - name: touch of fatigue
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 7
    concentration: 10
    slots:
      3: 5
      2: 7
      1: 7
      0: at-will
ability_scores:
  STR: 27
  DEX: 12
  CON: 21
  INT: 18
  WIS: 18
  CHA: 17
BAB: 15
CMB: 24
CMD: 35
CMD_other: 39 vs. trip
feats:
- name: Great Fortitude
- name: Improved Critical (bite)
- name: Improved Critical (claws)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Iron Will
- name: Power Attack
- name: Vital Strike
skills:
  Acrobatics: 16
    jump: 20
  Climb: 26
  Escape Artist: 16
  Fly: 13
  Intimidate: 21
  Perception: 22
  Sense Motive: 22
  Sleight of Hand: 16
  Stealth: 15
  Swim: 26
languages:
- Common
- Draconic
- Dwarven
- Elven
- Ignan
special_qualities:
- superheated
ecology:
  environment: any mountains or underground (Plane of Fire)
  organization: solitary
  treasure_type: triple
desc_long: Temperamental and prone to violent outbursts, magma dragons are regarded
  by most other dragons as dangerously insane-an assumption that, more often than
  not, proves correct. One can rarely predict a magma dragon's state of mind until
  it either attacks or attempts to engage in conversation. For their part, magma dragons
  can justify all of their actions-they just rarely feel the need to do so.

---

# Dragon (Primal, Magma), Adult Magma Dragon

**Source** Bestiary 2 pg. 100
**XP** 19,200

CN Large dragon (extraplanar, fire)
**Init** +5; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +22
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 20)

##### Defense

**AC** 29, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+1 Dex, +19 natural, –1 size)
**hp** 172 (15d12+75)
**Fort** +16, **Ref** +10, **Will** +15
**DR** 5/magic; **Immune** fire, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 23
**Weaknesses** vulnerable to cold

##### Offense
**Speed** 40 ft., fly 200 ft. (poor)
**Melee** bite +22 (2d6+12/19–20 plus 6 fire), 2 claws +22 (1d8+8/19–20), tail slap +17 (1d8+12), 2 wings +17 (1d6+4)
**Space** 10 ft., **Reach** 5 ft. (10 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (40-ft. cone, 12d6 fire, DC 22)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +18)
At will—_[[spells/Burning Hands|burning hands]]_ (DC 14), _[[spells/Scorching Ray|scorching ray]]_, _[[spells/Wall Of Fire|wall of fire]]_
**Spells Known **(CL 7th; concentration +10)
3rd (5/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Fireball|fireball]]_ (DC 16)
2nd (7/day)—_[[spells/Dust Of Twilight|dust of twilight]]_, _[[spells/Flaming Sphere|flaming sphere]]_ (DC 15), _[[spells/Glitterdust|glitterdust]]_ (DC 15), _[[spells/Pyrotechnics|pyrotechnics]]_ (DC 15)
1st (7/day)—_[[spells/Feather Fall|feather fall]]_, _[[spells/Flare Burst|flare burst]]_ (DC 14), _[[spells/Grease|grease]]_ (DC 14), _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, open/close, _[[spells/Read Magic|read magic]]_, _[[spells/Spark|spark]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_

##### Statistics
**Str** 27, **Dex** 12, **Con** 21, **Int** 18, **Wis** 18, **Cha** 17
**Base Atk** +15; **CMB** +24; **CMD** 35 (39 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _Improved Critical_ (claws), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +16 (+20 _[[spells/Jump|jump]]_), _[[universal monster rules/Climb|Climb]]_ +26, Escape Artist +16, Fly +13, Intimidate +21, Perception +22, Sense Motive +22, Sleight of Hand +16, Stealth +15, Swim +26
**Languages** Common, Draconic, Dwarven, Elven, Ignan
**SQ** superheated

##### Ecology

**Environment** any mountains or underground (Plane of Fire)
**Organization** solitary
**Treasure** triple

Temperamental and _[[conditions/Prone|prone]]_ to violent outbursts, magma dragons are regarded by most other dragons as dangerously insane—an assumption that, more often than not, proves correct. One can rarely predict a magma dragon’s state of mind until it either attacks or attempts to engage in conversation. For their part, magma dragons can justify all of their actions—they just rarely feel the need to do so.
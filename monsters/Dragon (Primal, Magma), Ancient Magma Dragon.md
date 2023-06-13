---
cssclass: [monsters]
title1: Dragon (Primal, Magma), Ancient Magma Dragon
title2: Ancient Magma Dragon
CR: 17
sources:
- name: Bestiary 2
  page: 101
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 102400
alignment: CN
size: Huge
type: dragon
subtypes:
- extraplanar
- fire
initiative:
  bonus: 4
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 300
  DC: 26
AC:
  AC: 39
  touch: 8
  flat_footed: 39
  components:
    natural: 31
    size: -2
HP:
  HP: 310
  long: 23d12+161
saves:
  fort: 22
  ref: 13
  will: 21
DR:
- amount: 15
  weakness: magic
immunities:
- fire
- paralysis
- sleep
SR: 28
weaknesses:
- vulnerable to cold
speeds:
  base: 40
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +33 (2d8+18/19-20 plus 10 fire)
      entries:
      - - damage: 2d8+18
          crit_range: 19-20
        - damage: '10'
          type: fire
      attack: bite
      bonus:
      - 33
    - text: 2 claws +33 (2d6+12/19-20)
      entries:
      - - damage: 2d6+12
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 33
    - text: tail slap +31 (2d6+18)
      entries:
      - - damage: 2d6+18
      attack: tail slap
      bonus:
      - 31
    - text: 2 wings +31 (1d8+6)
      entries:
      - - damage: 1d8+6
      count: 2
      attack: wings
      bonus:
      - 31
  special:
  - breath weapon (50-ft. cone, DC 28, 20d6 fire plus special)
  - crush
  - magma breath
space: 15
reach: 10
reach_other: 15 ft. with bite
spell_like_abilities:
  entries:
  - name: fire shield
    source: default
    freq: Constant
    other: warm
  - name: burning hands
    source: default
    freq: At will
    DC: 16
  - name: scorching ray
    source: default
    freq: At will
  - name: wall of fire
    source: default
    freq: At will
  - name: delayed blast fireball
    source: default
    freq: 3/day
    DC: 22
  sources:
  - name: default
    CL: 23
    concentration: 28
spells:
  entries:
  - name: greater polymorph
    source: '?'
    level: 7
  - name: prismatic spray
    source: '?'
    level: 7
    DC: 22
  - name: chain lightning
    source: '?'
    level: 6
    DC: 21
  - name: contagious flame
    source: '?'
    level: 6
    DC: 21
  - name: eyebite
    source: '?'
    level: 6
    DC: 21
  - name: hungry pit
    source: '?'
    level: 5
    DC: 20
  - name: polymorph
    source: '?'
    level: 5
  - name: teleport
    source: '?'
    level: 5
  - name: wall of force
    source: '?'
    level: 5
  - name: confusion
    source: '?'
    level: 4
    DC: 19
  - name: acid pit
    source: '?'
    level: 4
    DC: 19
  - name: dimensional anchor
    source: '?'
    level: 4
  - name: fire shield
    source: '?'
    level: 4
  - name: displacement
    source: '?'
    level: 3
  - name: dispel magic
    source: '?'
    level: 3
  - name: fireball
    source: '?'
    level: 3
    DC: 18
  - name: wind wall
    source: '?'
    level: 3
  - name: darkness
    source: '?'
    level: 2
  - name: dust of twilight
    source: '?'
    level: 2
  - name: flaming sphere
    source: '?'
    level: 2
    DC: 17
  - name: glitterdust
    source: '?'
    level: 2
    DC: 17
  - name: pyrotechnics
    source: '?'
    level: 2
    DC: 17
  - name: feather fall
    source: '?'
    level: 1
  - name: flare burst
    source: '?'
    level: 1
    DC: 16
  - name: grease
    source: '?'
    level: 1
    DC: 16
  - name: shield
    source: '?'
    level: 1
  - name: true strike
    source: '?'
    level: 1
  - name: bleed
    source: '?'
    level: 0
    DC: 15
  - name: detect magic
    source: '?'
    level: 0
  - name: detect poison
    source: '?'
    level: 0
  - name: ghost sound
    source: '?'
    level: 0
  - name: light
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
    CL: 15
    concentration: 20
    slots:
      7: 4
      6: 6
      5: 7
      4: 7
      3: 7
      2: 7
      1: 8
      0: at-will
ability_scores:
  STR: 35
  DEX: 10
  CON: 25
  INT: 22
  WIS: 22
  CHA: 21
BAB: 23
CMB: 37
CMD: 47
CMD_other: 51 vs. trip
feats:
- name: Flyby Attack
- name: Great Fortitude
- name: Greater Vital Strike
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Improved Critical (claws)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Iron Will
- name: Multiattack
- name: Power Attack
- name: Vital Strike
skills:
  Acrobatics: 23
    jump: 27
  Climb: 38
  Escape Artist: 23
  Fly: 18
  Intimidate: 31
  Knowledge (planes): 32
  Perception: 32
  Sense Motive: 32
  Sleight of Hand: 23
  Stealth: 18
  Survival: 32
  Swim: 38
languages:
- Common
- Draconic
- Dwarven
- Elven
- Gnome
- Halfling
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

# Dragon (Primal, Magma), Ancient Magma Dragon

**Source** Bestiary 2 pg. 101
**XP** 102,400

CN Huge dragon (extraplanar, fire)
**Init** +4; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +32
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 26)

##### Defense

**AC** 39, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 39 (+31 natural, –2 size)
**hp** 310 (23d12+161)
**Fort** +22, **Ref** +13, **Will** +21
**DR** 15/magic; **Immune** fire, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 28
**Weaknesses** vulnerable to cold

##### Offense
**Speed** 40 ft., fly 200 ft. (poor)
**Melee** bite +33 (2d8+18/19–20 plus 10 fire), 2 claws +33 (2d6+12/19–20), tail slap +31 (2d6+18), 2 wings +31 (1d8+6)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (50-ft. cone, DC 28, 20d6 fire plus special), crush, magma breath
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 23rd; concentration +28)
Constant—_[[spells/Fire Shield|fire shield]]_ (warm)
At will—_[[spells/Burning Hands|burning hands]]_ (DC 16), _[[spells/Scorching Ray|scorching ray]]_, _[[spells/Wall Of Fire|wall of fire]]_
3/day—_[[spells/Delayed Blast Fireball|delayed blast fireball]]_ (DC 22)
**Spells Known **(CL 15th; concentration +20)
7th (4/day)—greater _[[spells/Polymorph|polymorph]]_, _[[spells/Prismatic Spray|prismatic spray]]_ (DC 22)
6th (6/day)—_[[spells/Chain Lightning|chain lightning]]_ (DC 21), _[[spells/Contagious Flame|contagious flame]]_ (DC 21), _[[spells/Eyebite|eyebite]]_ (DC 21)
5th (7/day)—_[[spells/Hungry Pit|hungry pit]]_ (DC 20), _polymorph_, teleport, _[[spells/Wall Of Force|wall of force]]_
4th (7/day)—_[[spells/Confusion|confusion]]_ (DC 19), _[[spells/Acid Pit|acid pit]]_ (DC 19), _[[spells/Dimensional Anchor|dimensional anchor]]_, _fire shield_
3rd (7/day)—_[[spells/Displacement|displacement]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Fireball|fireball]]_ (DC 18), _[[spells/Wind Wall|wind wall]]_
2nd (7/day)—_[[spells/Darkness|darkness]]_, _[[spells/Dust Of Twilight|dust of twilight]]_, _[[spells/Flaming Sphere|flaming sphere]]_ (DC 17), _[[spells/Glitterdust|glitterdust]]_ (DC 17), _[[spells/Pyrotechnics|pyrotechnics]]_ (DC 17)
1st (8/day)—_[[spells/Feather Fall|feather fall]]_, _[[spells/Flare Burst|flare burst]]_ (DC 16), _[[spells/Grease|grease]]_ (DC 16), _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Ghost Sound|ghost sound]]_, light, open/close, _[[spells/Read Magic|read magic]]_, _[[spells/Spark|spark]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_

##### Statistics
**Str** 35, **Dex** 10, **Con** 25, **Int** 22, **Wis** 22, **Cha** 21
**Base Atk** +23; **CMB** +37; **CMD** 47 (51 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _Improved Critical_ (claws), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +23 (+27 _[[spells/Jump|jump]]_), _[[universal monster rules/Climb|Climb]]_ +38, Escape Artist +23, Fly +18, Intimidate +31, Knowledge (planes) +32, Perception +32, Sense Motive +32, Sleight of Hand +23, Stealth +18, Survival +32, Swim +38
**Languages** Common, Draconic, Dwarven, Elven, Gnome, Halfling, Ignan
**SQ** superheated

##### Ecology

**Environment** any mountains or underground (Plane of Fire)
**Organization** solitary
**Treasure** triple

Temperamental and _[[conditions/Prone|prone]]_ to violent outbursts, magma dragons are regarded by most other dragons as dangerously insane—an assumption that, more often than not, proves correct. One can rarely predict a magma dragon’s state of mind until it either attacks or attempts to engage in conversation. For their part, magma dragons can justify all of their actions—they just rarely feel the need to do so.
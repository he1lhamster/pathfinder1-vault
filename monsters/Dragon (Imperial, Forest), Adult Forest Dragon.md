---
cssclass: [monsters]
title1: Dragon (Imperial, Forest), Adult Forest Dragon
title2: Adult Forest Dragon
CR: 14
sources:
- name: Bestiary 3
  page: 94
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 38400
alignment: CE
size: Huge
type: dragon
subtypes:
- earth
initiative:
  bonus: 4
senses:
  dragon senses: true
  tremorsense: 60
auras:
- name: frightful presence
  radius: 180
  DC: 21
AC:
  AC: 30
  touch: 8
  flat_footed: 30
  components:
    natural: 22
    size: -2
HP:
  HP: 229
  long: 17d12+119
saves:
  fort: 16
  ref: 10
  will: 15
DR:
- amount: 2
  weakness: adamantine
immunities:
- paralysis
- poison
- sleep
SR: 25
speeds:
  base: 40
  burrow: 20
  climb: 30
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +25 (2d8+13)
      entries:
      - - damage: 2d8+13
      attack: bite
      bonus:
      - 25
    - text: 2 claws +24 (2d6+9)
      entries:
      - - damage: 2d6+9
      count: 2
      attack: claws
      bonus:
      - 24
    - text: gore +24 (2d6+13)
      entries:
      - - damage: 2d6+13
      attack: gore
      bonus:
      - 24
    - text: tail slap +22 (2d6+13)
      entries:
      - - damage: 2d6+13
      attack: tail slap
      bonus:
      - 22
  special:
  - breath weapon (50-ft. cone, 12d6 piercing damage, DC 24)
  - crush (DC 24, 2d8+13)
space: 15
reach: 10
reach_other: 15 ft. with bite and gore
spell_like_abilities:
  entries:
  - name: blight
    source: default
    freq: At will
    DC: 18
  - name: entangle
    source: default
    freq: At will
    DC: 14
  - name: pass without trace
    source: default
    freq: At will
  sources:
  - name: default
    CL: 17
    concentration: 20
spells:
  entries:
  - name: wind wall
    source: '?'
    level: 3
  - name: stinking cloud
    source: '?'
    level: 3
    DC: 16
  - name: fog cloud
    source: '?'
    level: 2
  - name: hideous laughter
    source: '?'
    level: 2
    DC: 15
  - name: touch of idiocy
    source: '?'
    level: 2
  - name: hypnotism
    source: '?'
    level: 1
    DC: 14
  - name: obscuring mist
    source: '?'
    level: 1
  - name: magic missile
    source: '?'
    level: 1
  - name: ray of enfeeblement
    source: '?'
    level: 1
    DC: 14
  - name: shield
    source: '?'
    level: 1
  - name: daze
    source: '?'
    level: 0
    DC: 13
  - name: detect magic
    source: '?'
    level: 0
  - name: ghost sound
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: read magic
    source: '?'
    level: 0
  - name: resistance
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
  STR: 29
  DEX: 10
  CON: 22
  INT: 16
  WIS: 17
  CHA: 16
BAB: 17
CMB: 28
CMD: 38
CMD_other: 42 vs. trip
feats:
- name: Improved Initiative
- name: Improved Natural Armor
- name: Iron Will
- name: Multiattack
- name: Power Attack
- name: Skill Focus (Stealth)
- name: Stealthy
- name: Toughness
- name: Weapon Focus (bite)
skills:
  Acrobatics: 8
    when jumping: 11
  Bluff: 23
  Climb: 37
  Escape Artist: 2
  Fly: 12
  Intimidate: 23
  Knowledge (arcana): 14
  Knowledge (nature): 14
  Perception: 23
  Spellcraft: 23
  Stealth: 22
  Survival: 16
languages:
- Common
- Draconic
- Sylvan
special_qualities:
- change shape
- sound imitation
- woodland stride
ecology:
  environment: any forest
  organization: solitary
  treasure_type: triple
desc_long: Forest dragons, or dilung, are fickle and malevolent dragons that dwell
  in deep, rugged woodlands. While a forest dragon can fly, it prefers to stalk the
  earth, flying only to pursue objects of its wrath.

---

# Dragon (Imperial, Forest), Adult Forest Dragon

**Source** Bestiary 3 pg. 94
**XP** 38,400
CE Huge dragon (earth)
**Init** +4; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 60 ft.; Perception +23
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 21)

##### Defense

**AC** 30, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+22 natural, –2 size)
**hp** 229 (17d12+119)
**Fort** +16, **Ref** +10, **Will** +15
**DR** 2/adamantine; **Immune** _[[universal monster rules/Paralysis|paralysis]]_, poison, sleep; **SR** 25

##### Offense
**Speed** 40 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft., _[[universal monster rules/Climb|climb]]_ 30 ft., fly 200 ft. (poor)
**Melee** bite +25 (2d8+13), 2 claws +24 (2d6+9), gore +24 (2d6+13), tail slap +22 (2d6+13)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite and gore)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (50-ft. cone, 12d6 piercing damage, DC 24), crush (DC 24, 2d8+13)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +20)
At will—_[[spells/Blight|blight]]_ (DC 18), _[[spells/Entangle|entangle]]_ (DC 14), _[[spells/Pass without Trace|pass without trace]]_
**Spells Known **(CL 7th; concentration +10)
3rd (5/day)—_[[spells/Wind Wall|wind wall]]_, _[[spells/Stinking Cloud|stinking cloud]]_ (DC 16)
2nd (7/day)—_[[spells/Fog Cloud|fog cloud]]_, _[[spells/Hideous Laughter|hideous laughter]]_ (DC 15), _[[spells/Touch of Idiocy|touch of idiocy]]_
1st (7/day)—_[[spells/Hypnotism|hypnotism]]_ (DC 14), _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 14), _[[spells/Shield|shield]]_
0 (at-will)—_[[spells/Daze|daze]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_

##### Statistics
**Str** 29, **Dex** 10, **Con** 22, **Int** 16, **Wis** 17, **Cha** 16
**Base Atk** +17; **CMB** +28; **CMD** 38 (42 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Natural Armor|Improved Natural Armor]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth), _[[feats/Stealthy|Stealthy]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Acrobatics +8 (+11 when jumping), Bluff +23, _Climb_ +37, Escape Artist +2, Fly +12, Intimidate +23, Knowledge (arcana, nature) +14, Perception +23, Spellcraft +23, Stealth +22, Survival +16
**Languages** Common, Draconic, Sylvan
**SQ** _[[universal monster rules/Change Shape|change shape]]_, sound imitation, woodland stride

##### Ecology

**Environment** any forest
**Organization** solitary
**Treasure** triple

Forest dragons, or dilung, are fickle and _[[items/Armor Magic Abilities/Malevolent|malevolent]]_ dragons that dwell in deep, rugged woodlands. While a forest dragon can fly, it prefers to stalk the earth, flying only to pursue objects of its wrath.
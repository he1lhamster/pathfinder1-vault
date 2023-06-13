---
cssclass: [monsters]
title1: Tunche
desc_short: Standing on three legs, this creature is a mix of dangerous jungle animals
  and plants fused into one deadly predator.
title2: Tunche
CR: 17
sources:
- name: Bestiary 4
  page: 265
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 102400
alignment: CN
size: Huge
type: fey
initiative:
  bonus: 9
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 31
  touch: 13
  flat_footed: 26
  components:
    dex: 5
    natural: 18
    size: -2
HP:
  HP: 262
  long: 25d6+175
saves:
  fort: 15
  ref: 19
  will: 19
DR:
- amount: 15
  weakness: cold iron and slashing
speeds:
  base: 50
  other_semicolon: feather step
  climb: 20
  swim: 20
attacks:
  melee:
  - - text: bite +22 (2d8+11/19-20 plus poison)
      entries:
      - - damage: 2d8+11
          crit_range: 19-20
        - effect: poison
      attack: bite
      bonus:
      - 22
    - text: 4 claws +22 (3d6+11)
      entries:
      - - damage: 3d6+11
      count: 4
      attack: claws
      bonus:
      - 22
  special:
  - poison
  - rend (2 claws, 3d6+16)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: speak with plants
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - superscripts:
    - UM
    name: burst of nettles
    source: default
    freq: At will
    DC: 20
  - name: entangle
    source: default
    freq: At will
    DC: 18
  - name: tree shape
    source: default
    freq: At will
  - name: tree stride
    source: default
    freq: At will
  - name: ventriloquism
    source: default
    freq: At will
  - name: warp wood
    source: default
    freq: At will
    DC: 19
  - name: diminish plants
    source: default
    freq: 7/day
  - name: plant growth
    source: default
    freq: 7/day
  - name: wall of thorns
    source: default
    freq: 7/day
  - name: control plants
    source: default
    freq: 3/day
    DC: 25
  - name: move earth
    source: default
    freq: 3/day
  - name: true seeing
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 20
    concentration: 27
ability_scores:
  STR: 33
  DEX: 21
  CON: 24
  INT: 12
  WIS: 20
  CHA: 25
BAB: 12
CMB: 25
CMB_other: +27 bull rush
CMD: 40
CMD_other: 42 vs. bull rush, 42 vs. trip
feats:
- name: Awesome Blow
- name: Blind-Fight
- name: Cleave
- name: Combat Reflexes
- name: Great Cleave
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Power Attack
- name: Vital Strike
- name: Weapon Focus (bite)
- name: Weapon Focus (claw)
skills:
  Acrobatics: 21
    when jumping: 29
  Bluff: 22
  Climb: 19
  Intimidate: 32
  Knowledge (geography): 29
  Knowledge (nature): 29
  Perception: 33
  Sense Motive: 33
  Stealth: 25
    in forests: 33
  Swim: 19
  _racial_mods:
    Acrobatics:
      when jumping: 8
    Stealth:
      in forests: 8
languages:
- Aklo
- Sylvan
- speak with plants
- tongues
special_qualities:
- change shape (Small or Medium humanoid; alter self)
- sound mimicry (sounds and voices)
ecology:
  environment: warm forests
  organization: solitary
  treasure_type: standard
special_abilities:
  Feather Step (Su): A tunche in a forest ignores the adverse movement effects of
    difficult terrain, and can even take 5-foot steps in difficult terrain.
  Poison (Ex): Bite-injury; save Fort DC 29; frequency 1/round for 6 rounds; effect
    1d4 Con and 1d4 Wis plus nauseated for 1 round; cure 2 consecutive saves.
desc_long: |-
  A tunche is a bizarre forest creature with twisted feline legs, a dense body resembling jungle undergrowth, clawed arms like those of a praying mantis, and a head resembling a cross between a monstrous spider's head and a jungle orchid. Although it has plant and animal features, a tunche is neither plant nor animal and is immune to effects that specifically target such creatures. Considering itself the ultimate protector of the jungle, a tunche prowls its domain in search of any who might despoil this vibrant and lush environment. If a tunche encounters travelers who treat the jungle with proper respect, it might simply observe them or demand an offering in exchange for allowing them to pass through its territory.

  A tunche especially enjoys toying with its victims, using its magic to confuse and mislead its opponents. A tunche rarely kills a foe without toying with it first, unless the target is actively harming plants or animals.

  A tunche stands 20 feet tall and weighs 4,000 pounds.

---

# Tunche
Standing on three legs, this creature is a mix of dangerous jungle animals and plants fused into one _[[items/Weapon Magic Abilities/Deadly|deadly]]_ predator.
**Source** Bestiary 4 pg. 265
**XP** 102,400

CN Huge fey
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +33

##### Defense

**AC** 31, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+5 Dex, +18 natural, –2 size)
**hp** 262 (25d6+175)
**Fort** +15, **Ref** +19, **Will** +19
**DR** 15/cold iron and slashing

##### Offense
**Speed** 50 ft., _[[universal monster rules/Climb|climb]]_ 20 ft., swim 20 ft.; _[[spells/Feather Step|feather step]]_
**Melee** bite +22 (2d8+11/19–20 plus poison), 4 claws +22 (3d6+11)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** poison, _[[universal monster rules/Rend|rend]]_ (2 claws, 3d6+16)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +27)
Constant—_[[spells/Speak with Plants|speak with plants]]_, _[[spells/Tongues|tongues]]_
At will—_[[spells/Burst of Nettles|burst of nettles]]_ (DC 20), _[[spells/Entangle|entangle]]_ (DC 18), _[[spells/Tree Shape|tree shape]]_, _[[spells/Tree Stride|tree stride]]_, _[[spells/Ventriloquism|ventriloquism]]_, _[[spells/Warp Wood|warp wood]]_ (DC 19)
7/day—_[[spells/Diminish Plants|diminish plants]]_, _[[spells/Plant Growth|plant growth]]_, _[[spells/Wall Of Thorns|wall of thorns]]_
3/day—_[[spells/Control Plants|control plants]]_ (DC 25), _[[spells/Move Earth|move earth]]_, _[[spells/True Seeing|true seeing]]_

##### Statistics
**Str** 33, **Dex** 21, **Con** 24, **Int** 12, **Wis** 20, **Cha** 25
**Base Atk** +12; **CMB** +25 (+27 bull rush); **CMD** 40 (42 vs. bull rush, 42 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite), _Weapon Focus_ (claw)
**Skills** Acrobatics +21 (+29 when jumping), Bluff +22, _Climb_ +19, Intimidate +32, Knowledge (geography) +29, Knowledge (nature) +29, Perception +33, Sense Motive +33, Stealth +25 (+33 in forests), Swim +19; **Racial Modifiers** +8 Acrobatics when jumping, +8 Stealth in forests
**Languages** Aklo, Sylvan; _speak with plants_, _tongues_
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (Small or Medium humanoid; _[[spells/Alter Self|alter self]]_), _[[universal monster rules/Sound Mimicry|sound mimicry]]_ (sounds and voices)

##### Ecology

**Environment** warm forests
**Organization** solitary
**Treasure** standard

### Special Abilities

**_Feather Step_ (Su)** A _[[monsters/Tunche|tunche]]_ in a forest ignores the adverse movement effects of difficult terrain, and can even take 5-foot steps in difficult terrain.

**Poison (Ex)** Bite—injury; save Fort DC 29; frequency 1/round for 6 rounds; effect 1d4 Con and 1d4 Wis plus _[[conditions/Nauseated|nauseated]]_ for 1 round; cure 2 consecutive saves.

##### Description

A _tunche_ is a bizarre forest creature with twisted feline legs, a dense body resembling jungle undergrowth, clawed arms like those of a praying mantis, and a head resembling a cross between a monstrous spider’s head and a jungle orchid. Although it has plant and animal features, a _tunche_ is neither plant nor animal and is immune to effects that specifically target such creatures. Considering itself the ultimate protector of the jungle, a _tunche_ prowls its domain in search of any who might despoil this vibrant and lush environment. If a _tunche_ encounters travelers who treat the jungle with proper respect, it might simply observe them or _[[spells/Demand|demand]]_ an offering in exchange for allowing them to pass through its territory.

A _tunche_ especially enjoys toying with its victims, using its magic to confuse and _[[spells/Mislead|mislead]]_ its opponents. A _tunche_ rarely kills a foe without toying with it first, unless the target is actively harming plants or animals.

A _tunche_ stands 20 feet tall and weighs 4,000 pounds.
---
cssclass: [monsters]
title1: Herald, Basileus
desc_short: This comely man is clad in fine silken robes. His eyes smolder with infernal
  flames.
title2: Basileus
CR: 15
sources:
- name: Inner Sea Gods
  page: 278
  link: http://paizo.com/products/btpy94wj?Pathfinder-Campaign-Setting-Inner-Sea-Gods-Hardcover
- name: 'Pathfinder #29: Mother of Flies'
  page: 78
  link: http://paizo.com/pathfinder/adventurePath/councilOfThieves/v5748btpy8bc1
XP: 51200
alignment: LE
size: Medium
type: outsider
subtypes:
- devil
- evil
- extraplanar
- herald
- lawful
initiative:
  bonus: 10
senses:
  darkvision: 60
  low-light vision: true
  see in darkness: true
AC:
  AC: 28
  touch: 16
  flat_footed: 22
  components:
    dex: 6
    natural: 12
HP:
  HP: 200
  long: 16d10+112
saves:
  fort: 12
  ref: 18
  will: 16
DR:
- amount: 10
  weakness: good
immunities:
- fire
- poison
resistances:
  acid: 10
  cold: 10
SR: 26
speeds:
  base: 30
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: touch +19 (1d8+8)
      entries:
      - - damage: 1d8+8
      attack: touch
      bonus:
      - 19
  - - text: 5 slams +24 (1d8+8 plus grab)
      entries:
      - - damage: 1d8+8
        - effect: grab
      count: 5
      attack: slams
      bonus:
      - 24
  special:
  - terror
  - terror shape
space: 5
reach: 5
reach_other: 15 ft. with slam
spell_like_abilities:
  entries:
  - name: cloudkill
    source: default
    freq: At will
    DC: 22
  - name: false vision
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: mirage arcana
    source: default
    freq: At will
    DC: 22
  - name: persistent image
    source: default
    freq: At will
    DC: 22
  - name: scorching ray
    source: default
    freq: At will
  - name: crushing despair
    source: default
    freq: 3/day
    DC: 21
  - name: dimensional anchor
    source: default
    freq: 3/day
    DC: 21
  - name: ethereal jaunt
    source: default
    freq: 3/day
  - name: greater dispel magic
    source: default
    freq: 3/day
  - name: greater invisibility
    source: default
    freq: 3/day
  - name: legend lore
    source: default
    freq: 3/day
  - name: nightmare
    source: default
    freq: 3/day
    DC: 22
  - name: phantasmal killer
    source: default
    freq: 3/day
    DC: 21
  - name: true seeing
    source: default
    freq: 3/day
  - name: geas/quest
    source: default
    freq: 1/day
  - name: grant 1 wish
    source: default
    freq: 1/day
    other: to mortals only
  - name: summon
    source: default
    freq: 1/day
    level: 5
    summons:
    - name: bone devils
      amount: 2
      chance: 75%
  sources:
  - name: default
    CL: 16
    concentration: 23
ability_scores:
  STR: 26
  DEX: 22
  CON: 25
  INT: 26
  WIS: 19
  CHA: 25
BAB: 16
CMB: 24
CMB_other: +28 grapple
CMD: 40
feats:
- name: Blind-Fight
- name: Combat Reflexes
- name: Deceitful
- name: Improved Initiative
- name: Improved Iron Will
- name: Iron Will
- name: Lightning Reflexes
- name: Persuasive
skills:
  Acrobatics: 22
  Bluff: 30
  Diplomacy: 38
  Disguise: 30
  Fly: 14
  Intimidate: 38
  Knowledge (arcana): 24
  Knowledge (history): 16
  Knowledge (nobility): 16
  Knowledge (planes): 27
  Perception: 23
  Perform (oratory): 23
  Sense Motive: 23
  Sleight of Hand: 22
  Spellcraft: 27
  Stealth: 25
  _racial_mods:
    Diplomacy:
      _: 8
    Intimidate:
      _: 8
languages:
- Abyssal
- Aklo
- Aquan
- Celestial
- Common
- Draconic
- Elven
- Giant
- Infernal
- Undercommon
- tongues
- telepathy 100 ft.
special_qualities:
- veil of forms
ecology:
  environment: any (Hell)
  organization: solitary
  treasure_type: double
special_abilities:
  Gaze (Su): Death (if 6 HD or less) or 6d6 damage and panicked for 2d4 rounds (7
    HD or more), range 30 feet, Will DC 25 negates the death or panicked effect. This
    gaze is a mind-affecting fear effect that causes its targets to perceive Basileus
    as the most terrifying thing that it can imagine. The save DC is Charisma-based.
  Terror Shape (Su): While using his gaze ability, Basileus manifests one to five
    monstrous limbs that can make slam attacks.
  Veil of Forms (Su): All creatures see Basileus as a powerful and attractive member
    of their own race. While using this ability, Basileus's gaze ability is suppressed.
    He can activate or suppress this ability as a free action.
desc_long: An infernal paradox at once wondrous and terrifying, tempting and blasphemous,
  Basileus serves as the herald of Asmodeus and the harbinger of Hell's will. Few
  who have met him survive the experience unchanged, for he is the very word of Hell.

---

# Herald, Basileus
This comely man is clad in fine silken robes. His eyes smolder with infernal flames.
**Source** Inner Sea Gods pg. 278, Pathfinder #29: Mother of Flies pg. 78
**XP** 51,200

LE Medium outsider (devil, evil, extraplanar, herald, lawful)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +23

##### Defense

**AC** 28, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+6 Dex, +12 natural)
**hp** 200 (16d10+112)
**Fort** +12, **Ref** +18, **Will** +16
**DR** 10/good; **Immune** fire, poison; **Resist** acid 10, cold 10; **SR** 26

##### Offense
**Speed** 30 ft., fly 60 ft. (perfect)
**Melee** touch +19 (1d8+8) or 5 slams +24 (1d8+8 plus _[[universal monster rules/Grab|grab]]_)
**Space** 5 ft., **Reach** 5 ft. (15 ft. with slam)
**Special Attacks** terror, terror shape
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +23)
At will—_[[spells/Cloudkill|cloudkill]]_ (DC 22), _[[spells/False _[[spells/Vision|Vision]]_, Greater|false _vision_, greater]]_ teleport (self plus 50 lbs. of objects only), _[[spells/Mirage Arcana|mirage arcana]]_ (DC 22), _[[spells/Persistent Image|persistent image]]_ (DC 22), _[[spells/Scorching Ray|scorching ray]]_
3/day—_[[spells/Crushing Despair|crushing despair]]_ (DC 21), _[[spells/Dimensional Anchor|dimensional anchor]]_ (DC 21), _[[spells/Ethereal Jaunt|ethereal jaunt]]_, greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ _[[spells/Invisibility|invisibility]]_, _[[spells/Legend Lore|legend lore]]_, _[[spells/Nightmare|nightmare]]_ (DC 22), _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 21), _[[spells/True Seeing|true seeing]]_
1/day—geas/quest, grant 1 _[[spells/Wish|wish]]_ (to mortals only), _[[universal monster rules/Summon|summon]]_ (level 5, 2 bone devils 75%)

##### Statistics
**Str** 26, **Dex** 22, **Con** 25, **Int** 26, **Wis** 19, **Cha** 25
**Base Atk** +16; **CMB** +24 (+28 grapple); **CMD** 40
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deceitful|Deceitful]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Persuasive|Persuasive]]_
**Skills** Acrobatics +22, Bluff +30, Diplomacy +38, Disguise +30, Fly +14, Intimidate +38, Knowledge (arcana) +24, Knowledge (history, nobility) +16, Knowledge (planes) +27, Perception +23, Perform (oratory) +23, Sense Motive +23, Sleight of Hand +22, Spellcraft +27, Stealth +25; **Racial Modifiers** +8 Diplomacy, +8 Intimidate
**Languages** Abyssal, Aklo, Aquan, Celestial, Common, Draconic, Elven, Giant, Infernal, Undercommon; _[[spells/Tongues|tongues]]_, _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[spells/Veil|veil]]_ of forms

##### Ecology

**Environment** any (Hell)
**Organization** solitary
**Treasure** double

### Special Abilities

**_[[universal monster rules/Gaze|Gaze]]_ (Su)** Death (if 6 HD or less) or 6d6 damage and _[[conditions/Panicked|panicked]]_ for 2d4 rounds (7 HD or more), range 30 feet, Will DC 25 negates the death or _panicked_ effect. This _gaze_ is a mind-affecting _[[universal monster rules/Fear|fear]]_ effect that causes its targets to perceive Basileus as the most terrifying thing that it can imagine. The save DC is Charisma-based.

**Terror Shape (Su)** While using his _gaze_ ability, Basileus manifests one to five monstrous limbs that can make slam attacks.

**_Veil_ of Forms (Su)** All creatures see Basileus as a powerful and attractive member of their own race. While using this ability, Basileus’s _gaze_ ability is suppressed. He can activate or suppress this ability as a free action.

##### Description

An infernal paradox at once wondrous and terrifying, tempting and blasphemous, Basileus serves as the herald of Asmodeus and the harbinger of Hell’s will. Few who have met him survive the experience unchanged, for he is the very word of Hell.
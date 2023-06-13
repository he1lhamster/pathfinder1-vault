---
cssclass: [monsters]
title1: Daemon, Hydrodaemon
desc_short: 'The skin on this frog-like fiend is clammy and its eyes look dead and
  milky; its wide face is split by a fanged maw. '
title2: Hydrodaemon
CR: 8
sources:
- name: Bestiary 2
  page: 67
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 4800
alignment: NE
size: Large
type: outsider
subtypes:
- aquatic
- daemon
- evil
- extraplanar
initiative:
  bonus: 2
senses:
  darkvision: 60
  detect magic: true
AC:
  AC: 20
  touch: 11
  flat_footed: 18
  components:
    dex: 2
    natural: 9
    size: -1
HP:
  HP: 95
  long: 10d10+40
saves:
  fort: 11
  ref: 9
  will: 3
DR:
- amount: 10
  weakness: cold iron or silver
immunities:
- acid
- death effects
- disease
- poison
- waters of the River Styx
resistances:
  cold: 10
  electricity: 10
  fire: 10
SR: 19
speeds:
  base: 30
  fly: 40
  fly_other: average; see glide, below
  swim: 60
attacks:
  melee:
  - - text: bite +13 (1d8+4 plus grab)
      entries:
      - - damage: 1d8+4
        - effect: grab
      attack: bite
      bonus:
      - 13
    - text: 2 claws +13 (1d6+4)
      entries:
      - - damage: 1d6+4
      count: 2
      attack: claws
      bonus:
      - 13
  ranged:
  - - text: sleep spittle +11 (sleep)
      entries:
      - - effect: sleep
      attack: sleep spittle
      bonus:
      - 11
  special:
  - rake (2 claws +13, 1d6+4)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: water walk
    source: default
    freq: Constant
  - name: acid arrow
    source: default
    freq: At will
  - name: deeper darkness
    source: default
    freq: At will
  - name: control water
    source: default
    freq: 3/day
  - name: greater teleport
    source: default
    freq: 3/day
    other: self plus 50 lbs. of objects only
  - name: summon monster V
    source: default
    freq: 3/day
    other: Large water elemental only
  - name: desecrate
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 3
    summons:
    - name: hydrodaemon
      amount: 1
      chance: 50%
  sources:
  - name: default
    CL: 9
    concentration: 11
ability_scores:
  STR: 18
  DEX: 15
  CON: 18
  INT: 9
  WIS: 11
  CHA: 14
BAB: 10
CMB: 15
CMB_other: +9 grapple
CMD: 27
feats:
- name: Cleave
- name: Point-Blank Shot
- name: Power Attack
- name: Precise Shot
- name: Skill Focus (Perception)
skills:
  Fly: 0
  Intimidate: 14
  Knowledge (planes): 10
  Perception: 15
  Sense Motive: 12
  Stealth: 10
  Swim: 21
languages:
- Abyssal
- Infernal
- telepathy 100 ft.
special_qualities:
- amphibious
- glide
ecology:
  environment: any (Abaddon)
  organization: solitary, gang (2-5), or mob (6-12)
  treasure_type: standard
special_abilities:
  Glide (Ex): A hydrodaemon can launch itself into the air and glide along for 1 minute,
    gaining a fly speed of 40 feet with average maneuverability. While gliding, the
    hydrodaemon gains the pounce ability.
  Sleep Spittle (Su): A hydrodaemon can spit at a single target within 20 feet, making
    a ranged touch attack as a standard action. A target hit by this spittle must
    succeed on a DC 19 Will save or fall asleep for 6 rounds. The save DC is Constitution-based.
desc_long: |-
  While at first glance these creatures seem like enormous and foul boggards, their dangerous gait, dead eyes, and wicked claws give away their fiendish nature. In their home environment, hydrodaemons swim the sickening rivers and seas of Abaddon and the River Styx, ducking beneath the rivers of pus and bile only to leap out at enemies and rend their flesh with tooth and claw. It is said these are among the few creatures able to survive in the deadly waters of the River Styx. When called to the Material Plane, hydrodaemons serve powerful spellcasters, protecting domains dotted with pools, streams, and even sewer complexes. Associated with death by drowning, these fiends use a favored tactic to draw the most anguish from their victims. Hydrodaemons first attack with their inky black sleep spittle, hoping to render victims unconscious. With their opponents unable to fight back, hydrodaemons drag their enemies into the foul waters they call home and delight as the liquid fills their victims' gasping lungs. If unable to drown a victim, they finish the job with jaws and claws. 

  Hydrodaemons possess an awkward gait, springing back on their heels and leaping about like humanoid frogs. Even so, they move in an unpredictable manner, twisting their bodies with each hopping movement. Hydrodaemons can also unfurl flaps of skin that allow them to glide through the air. Hydrodaemons stand 10 feet tall and weigh upward of 3,000 pounds.

---

# Daemon, Hydrodaemon
The skin on this frog-like fiend is clammy and its eyes look dead and milky; its wide face is _[[universal monster rules/Split|split]]_ by a fanged maw.

**Source** Bestiary 2 pg. 67
**XP** 4,800

NE Large outsider (aquatic, daemon, evil, extraplanar)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Magic|detect magic]]_; Perception +15

##### Defense

**AC** 20, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+2 Dex, +9 natural, –1 size)
**hp** 95 (10d10+40)
**Fort** +11, **Ref** +9, **Will** +3
**DR** 10/cold iron or silver; **Immune** acid, death effects, disease, poison, waters of the River Styx; **Resist** cold 10, electricity 10, fire 10; **SR** 19

##### Offense
**Speed** 30 ft., fly 40 ft. (average; see _[[spells/Glide|glide]]_, below), swim 60 ft.
**Melee** bite +13 (1d8+4 plus _[[universal monster rules/Grab|grab]]_), 2 claws +13 (1d6+4)
**Ranged** sleep spittle +11 (sleep)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Rake|rake]]_ (2 claws +13, 1d6+4)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +11)
Constant—_detect magic_, _[[spells/Water Walk|water walk]]_
At will—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Deeper Darkness|deeper darkness]]_
3/day—_[[spells/Control Water|control water]]_, greater teleport (self plus 50 lbs. of objects only), _[[spells/Summon Monster V|summon monster V]]_ (Large water elemental only)
1/day—_[[spells/Desecrate|desecrate]]_, _[[universal monster rules/Summon|summon]]_ (level 3, 1 hydrodaemon 50%)

##### Statistics
**Str** 18, **Dex** 15, **Con** 18, **Int** 9, **Wis** 11, **Cha** 14
**Base Atk** +10; **CMB** +15 (+9 grapple); **CMD** 27
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** Fly +0, Intimidate +14, Knowledge (planes) +10, Perception +15, Sense Motive +12, Stealth +10, Swim +21
**Languages** Abyssal, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Amphibious|amphibious]]_, _glide_

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary, gang (2–5), or mob (6–12)
**Treasure** standard

### Special Abilities

**_Glide_ (Ex)** A hydrodaemon can launch itself into the air and _glide_ along for 1 minute, gaining a fly speed of 40 feet with average maneuverability. While gliding, the hydrodaemon gains the _[[universal monster rules/Pounce|pounce]]_ ability.
**Sleep Spittle (Su)** A hydrodaemon can spit at a single target within 20 feet, making a ranged touch attack as a standard action. A target hit by this spittle must succeed on a DC 19 Will save or fall asleep for 6 rounds. The save DC is Constitution-based.

##### Description

While at first glance these creatures seem like enormous and foul boggards, their dangerous gait, dead eyes, and wicked claws give away their fiendish nature. In their home environment, hydrodaemons swim the sickening rivers and seas of Abaddon and the River Styx, ducking beneath the rivers of pus and bile only to leap out at enemies and _[[universal monster rules/Rend|rend]]_ their flesh with tooth and claw. It is said these are among the few creatures able to survive in the _[[items/Weapon Magic Abilities/Deadly|deadly]]_ waters of the River Styx. When _[[items/Weapon Magic Abilities/Called|called]]_ to the Material Plane, hydrodaemons serve powerful spellcasters, protecting domains dotted with pools, streams, and even sewer complexes. Associated with death by drowning, these fiends use a favored tactic to draw the most anguish from their victims. Hydrodaemons first attack with their inky black sleep spittle, hoping to render victims _[[conditions/Unconscious|unconscious]]_. With their opponents unable to fight back, hydrodaemons drag their enemies into the foul waters they call home and delight as the liquid fills their victims’ gasping lungs. If unable to drown a victim, they finish the job with jaws and claws.

Hydrodaemons possess an awkward gait, springing back on their heels and leaping about like humanoid frogs. Even so, they move in an unpredictable manner, twisting their bodies with each hopping movement. Hydrodaemons can also unfurl flaps of skin that allow them to _glide_ through the air. Hydrodaemons stand 10 feet tall and weigh upward of 3,000 pounds.
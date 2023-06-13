---
cssclass: [monsters]
title1: Giant, Tomb Giant
desc_short: This towering, lean figure is hairless and has smooth, milky white skin.
  A scythe gleams in her hands.
title2: Tomb Giant
CR: 12
sources:
- name: 'Pathfinder #94: Ice Tomb of the Giant Queen'
  page: 84
  link: http://paizo.com/products/btpy9dz6?Pathfinder-Adventure-Path-94-Ice-Tomb-of-the-Giant-Queen
- name: Bestiary 6
  page: 136
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 19200
alignment: NE
size: Large
type: humanoid
subtypes:
- giant
initiative:
  bonus: 3
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 28
  touch: 12
  flat_footed: 25
  components:
    armor: 6
    dex: 3
    natural: 10
    size: -1
HP:
  HP: 162
  long: 13d8+104
saves:
  fort: 16
  ref: 7
  will: 10
defensive_abilities:
- negative energy affinity
- rock catching
immunities:
- death effects
- paralysis
speeds:
  base: 40
  base_other: 30 ft. in armor
attacks:
  melee:
  - - text: mwk scythe +20/+15 (2d6+16/19-20/×4 plus energy drain)
      entries:
      - - damage: 2d6+16
          crit_range: 19-20
          crit_multiplier: 4
        - effect: energy drain
      attack: mwk scythe
      bonus:
      - 20
      - 15
  - - text: 2 slams +19 (1d6+11 plus energy drain)
      entries:
      - - damage: 1d6+11
        - effect: energy drain
      count: 2
      attack: slams
      bonus:
      - 19
  ranged:
  - - text: rock +12 (1d8+11)
      entries:
      - - damage: 1d8+11
      attack: rock
      bonus:
      - 12
  special:
  - energy drain (1 level, DC 18)
  - rock throwing (120 ft.)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: deathwatch
    source: default
    freq: Constant
  - name: detect undead
    source: default
    freq: At will
  - name: make whole
    source: default
    freq: 3/day
  - superscripts:
    - APG
    name: sculpt corpse
    source: default
    freq: 3/day
  - name: animate dead
    source: default
    freq: 1/day
  - name: control undead
    source: default
    freq: 1/day
    DC: 19
  sources:
  - name: default
    CL: 12
    concentration: 14
ability_scores:
  STR: 32
  DEX: 17
  CON: 26
  INT: 13
  WIS: 19
  CHA: 14
BAB: 9
CMB: 21
CMB_other: +23 trip
CMD: 34
CMD_other: 36 vs. trip
feats:
- name: Combat Expertise
- name: Improved Critical (scythe)
- name: Improved Iron Will
- name: Improved Trip
- name: Iron Will
- name: Martial Weapon Proficiency (scythe)
- name: Power Attack
skills:
  Climb: 12
  Heal: 12
  Knowledge (religion): 14
  Perception: 15
  Stealth: 5
  Survival: 10
languages:
- Common
- Giant
special_qualities:
- corpse stitcher
- sinister synergy
ecology:
  environment: any land or underground
  organization: solitary, pair, or cabal (3-13)
  treasure_type: standard
  treasure:
  - mwk breastplate
  - mwk scythe
special_abilities:
  Corpse Stitcher (Sp): Tomb giants can cast make whole as a spell-like ability, but
    only for the purposes of creating undead creatures. For example, a tomb giant
    can use this ability to aid in the creation of a necrocraft (Pathfinder RPG Bestiary
    4 200), to restore armor to be used for the creation of a phantom armor (Bestiary
    4 213), or even to repair the armor of a graveknight (Pathfinder RPG Bestiary
    3 138).
  Energy Drain (Su): A tomb giant can channel its energy drain attack through any
    melee weapon it wields.
  Sinister Synergy (Su): Multiple tomb giants can combine their efforts to gain the
    ability to create undead. When two or more tomb giants are within 30 feet of each
    other, they can work together to use create undead as a spell-like ability (caster
    level 13th). Three or more tomb giants working in unison in this way can use greater
    create undead as a spell-like ability (caster level 15th). Every additional tomb
    giant beyond the third who participates in this synergy increases the caster level
    of this effect by 1.
desc_long: |-
  Since the time Urgathoa first fled the Boneyard, there have been living creatures that have given their allegiance to powers that offer the promise of existence eternal. Tomb giants are an entire race of humanoids who have given themselves over to necromancy, and in so doing have gained sinister powers. These giants are born as the living agents of undeath, and they show great skill in creating all manner of undead creatures-even from their own kind. Tomb giants fully expect to be transformed after they die, though most don't have to worry about the cost of sacrificing their experiences and memories, for they know their brothers and sisters can raise intelligent undead much greater than shambling zombies or clattering skeletons.

  Tomb giants possess an alabaster complexion. They are devoid of all body hair and have smooth, rounded features and marbleized skin. Tomb giants often tattoo their pale skin with arcane symbols in stark black ink. The sclerae of their eyes are jet black, and ghostly white pupils glow in the centers. They move with an eerie, silent grace for humanoids of their size, and rarely talk unless it is necessary. Tomb giants favor simple clothing, typically wearing togas at home and hooded cloaks when they emerge from their shadowy lairs. The average tomb giant stands 11 to 13 feet tall and weighs approximately 1,300 pounds. Tomb giants can live for up to 400 years.

---

# Giant, Tomb Giant
This towering, lean figure is hairless and has smooth, milky white skin. A _[[items/Weapon/Scythe|scythe]]_ gleams in her hands.
**Source** Pathfinder #94: Ice Tomb of the Giant Queen pg. 84, Bestiary 6 pg. 136
**XP** 19,200

NE Large humanoid (giant)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +15

##### Defense

**AC** 28, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+6 armor, +3 Dex, +10 natural, –1 size)
**hp** 162 (13d8+104)
**Fort** +16, **Ref** +7, **Will** +10
**Defensive Abilities** _[[universal monster rules/Negative Energy Affinity|negative energy affinity]]_, _[[universal monster rules/Rock Catching|rock catching]]_; **Immune** death effects, _[[universal monster rules/Paralysis|paralysis]]_

##### Offense
**Speed** 40 ft. (30 ft. in armor)
**Melee** mwk _scythe_ +20/+15 (2d6+16/19–20/×4 plus _[[universal monster rules/Energy Drain|energy drain]]_) or 2 slams +19 (1d6+11 plus _energy drain_)
**Ranged** rock +12 (1d8+11)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _energy drain_ (1 level, DC 18), _[[universal monster rules/Rock Throwing|rock throwing]]_ (120 ft.)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +14)
Constant—_[[spells/Deathwatch|deathwatch]]_
At will—_[[spells/Detect Undead|detect undead]]_
3/day—_[[spells/Make Whole|make whole]]_, _[[spells/Sculpt Corpse|sculpt corpse]]_
1/day—_[[spells/Animate Dead|animate dead]]_, _[[spells/Control Undead|control undead]]_ (DC 19)

##### Statistics
**Str** 32, **Dex** 17, **Con** 26, **Int** 13, **Wis** 19, **Cha** 14
**Base Atk** +9; **CMB** +21 (+23 _[[universal monster rules/Trip|trip]]_); **CMD** 34 (36 vs. _trip_)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Improved Critical|Improved Critical]]_ (_scythe_), _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Martial Weapon Proficiency|Martial Weapon Proficiency]]_ (_scythe_), _[[feats/Power Attack|Power Attack]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +12, _[[spells/Heal|Heal]]_ +12, Knowledge (religion) +14, Perception +15, Stealth +5, Survival +10
**Languages** Common, Giant
**SQ** corpse stitcher, sinister synergy

##### Ecology

**Environment** any land or underground
**Organization** solitary, pair, or cabal (3–13)
**Treasure** standard (mwk _[[items/Armor/Breastplate|breastplate]]_, mwk _scythe_)

### Special Abilities

**Corpse Stitcher (Sp)** Tomb giants can cast _make whole_ as a spell-like ability, but only for the purposes of creating undead creatures. For example, a tomb giant can use this ability to aid in the creation of a _[[monsters/Necrocraft|necrocraft]]_ (Pathfinder RPG Bestiary 4 200), to restore armor to be used for the creation of a phantom armor (Bestiary 4 213), or even to repair the armor of a _[[monsters/Graveknight|graveknight]]_ (Pathfinder RPG Bestiary 3 138).

**_Energy Drain_ (Su)** A tomb giant can channel its _energy drain_ attack through any melee weapon it wields.
**Sinister Synergy (Su)** Multiple tomb giants can combine their efforts to gain the ability to _[[spells/Create Undead|create undead]]_. When two or more tomb giants are within 30 feet of each other, they can work together to use _create undead_ as a spell-like ability (caster level 13th). Three or more tomb giants working in unison in this way can use greater _create undead_ as a spell-like ability (caster level 15th). Every additional tomb giant beyond the third who participates in this synergy increases the caster level of this effect by 1.

##### Description

Since the time Urgathoa first fled the Boneyard, there have been living creatures that have given their allegiance to powers that offer the promise of existence eternal. Tomb giants are an entire race of humanoids who have given themselves over to necromancy, and in so doing have gained sinister powers. These giants are born as the living agents of undeath, and they show great skill in creating all manner of undead creatures—even from their own kind. Tomb giants fully expect to be transformed after they die, though most don’t have to worry about the cost of sacrificing their experiences and memories, for _[[spells/They Know|they know]]_ their brothers and sisters can raise intelligent undead much greater than shambling zombies or clattering skeletons.

Tomb giants possess an alabaster complexion. They are devoid of all body hair and have smooth, rounded features and marbleized skin. Tomb giants often _[[items/Mundane/Tattoo|tattoo]]_ their pale skin with arcane symbols in stark black _[[items/Mundane/Ink|ink]]_. The sclerae of their eyes are _[[universal monster rules/Jet|jet]]_ black, and ghostly white pupils glow in the centers. They move with an eerie, silent _[[spells/Grace|grace]]_ for humanoids of their size, and rarely talk unless it is necessary. Tomb giants favor simple clothing, typically wearing togas at home and hooded cloaks when they emerge from their shadowy lairs. The average tomb giant stands 11 to 13 feet tall and weighs approximately 1,300 pounds. Tomb giants can live for up to 400 years.
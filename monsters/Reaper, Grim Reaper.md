---
cssclass: [monsters]
title1: Reaper, Grim Reaper
desc_short: This tall, cloaked figure stares out from the black hood that covers its
  head. It wields an enormous scythe in its skeletal, bone-white hands, looking as
  though it is freezing the very air around it.
title2: Grim Reaper
CR: 20
sources:
- name: 'Pathfinder #48: Shadows of Gallowspire'
  page: 86
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderAdventurePath/carrionCrown/v5748btpy8mgb
XP: 307200
alignment: NE
size: Large
type: undead
subtypes:
- evil
- extraplanar
- incorporeal
initiative:
  bonus: 6
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: fear aura
  radius: 40
  DC: 36
AC:
  AC: 32
  touch: 20
  flat_footed: 30
  components:
    deflection: 9
    dex: 2
    natural: 12
    size: -1
HP:
  HP: 378
  long: 28d8+252
saves:
  fort: 18
  ref: 11
  will: 20
defensive_abilities:
- channel resistance +4
- incorporeal
DR:
- amount: 15
  weakness: cold iron and good
immunities:
- undead traits
SR: 31
speeds:
  base: 40
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: +3 scythe +27/+22/+17/+12 (2d6+13/19-20/×4 plus death touch)
      entries:
      - - damage: 2d6+13
          crit_range: 19-20
          crit_multiplier: 4
        - effect: death touch
      attack: +3 scythe
      bonus:
      - 27
      - 22
      - 17
      - 12
space: 10
reach: 15
spell_like_abilities:
  entries:
  - name: fly
    source: default
    freq: Constant
  - name: foresight
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: circle of death
    source: default
    freq: At will
    DC: 25
  - name: control undead
    source: default
    freq: At will
    DC: 26
  - name: invisibility
    source: default
    freq: At will
  - name: plane shift
    source: default
    freq: At will
    DC: 26
  - name: polymorph
    source: default
    freq: At will
  - name: energy drain
    source: default
    freq: 3/day
    DC: 28
  - name: finger of death
    source: default
    freq: 3/day
    DC: 26
  - name: soul bind
    source: default
    freq: 3/day
    DC: 28
  - name: summon minor reapers
    source: default
    freq: 3/day
    level: 8
    summons:
    - name: minor reapers
      amount: 1d4
  - name: unwilling shield
    source: default
    freq: 3/day
    DC: 25
  - name: quickened destruction
    source: default
    freq: 1/day
    DC: 26
  - name: wail of the banshee
    source: default
    freq: 1/day
    DC: 28
  sources:
  - name: default
    CL: 20
    concentration: 29
ability_scores:
  STR: 24
  DEX: 15
  CON:
  INT: 16
  WIS: 19
  CHA: 29
BAB: 21
CMB: 24
CMD: 50
CMD_other: can't be tripped
feats:
- name: Cleave
- name: Combat Casting
- name: Combat Expertise
- name: Combat Reflexes
- name: Critical Focus
- name: Great Cleave
- name: Greater Weapon Focus (scythe)
- name: Improved Critical (scythe)
- name: Improved Disarm
- name: Improved Initiative
- name: Power Attack
- name: Quicken Spell-Like Ability (destruction)
- name: Vital Strike
- name: Weapon Focus (scythe)
skills:
  Diplomacy: 37
  Disguise: 40
  Fly: 39
  Knowledge (planes): 31
  Perception: 35
  Sense Motive: 35
  Stealth: 29
languages:
- Common
- Celestial
- Infernal
- truespeech
ecology:
  environment: any
  organization: solitary
  treasure_type: double
  treasure:
  - +3 scythe
  - other treasure
special_abilities:
  Death Touch (Su): Creatures hit by either a grim reaper's touch attack or by a weapon
    wielded by a grim reaper must succeed at a DC 33 Fortitude save or gain 2d4 negative
    levels. The save DC is Charisma-based. A grim reaper can channel this ability
    through any weapon it wields. A humanoid slain by a reaper's death touch is consumed
    in unholy fire and has its remains destroyed as the destruction spell. This is
    a death effect.
  Summon Minor Reapers (Sp): Three times per day, a reaper can summon 1d4 minor reapers
    as a standard action. Each of these minor reapers is assigned a single creature
    to attack, and the targeted creature must battle the minor reaper by itself. The
    target that the grim reaper assigns to its minor reapers need not be in sight,
    but it must be on the same plane on which the minor reaper was summoned. A grim
    reaper may only assign one minor reaper to any creature at a given time, even
    if it uses this ability multiple times.
desc_long: |-
  Known by many names throughout nearly all cultures, grim reapers are the personifications of death and all the pain and fear associated with that state. They are universally feared by the living as harbingers of destruction and masters of all that has already passed from life. These hooded beings travel through the planes with the sole intent of bringing about the end of life, slaying with a deliberateness inscrutable to all but themselves.

  While grim reapers are the most feared of their kind, they are not alone. The towering, ghostlike grim reapers are served by minor reapers, corporeal servitors that enact their master's dreadful will and meet out death's unrelenting touch. A grim reaper is 15 feet tall and, as an incorporeal creature, has no physical weight except for its equipment. Minor reapers stand 7 feet tall and weigh approximately 70 pounds.

---

# Reaper, Grim Reaper
This tall, cloaked figure stares out from the black hood that covers its head. It wields an enormous _[[items/Weapon/Scythe|scythe]]_ in its skeletal, bone-white hands, looking as though it is freezing the very air around it.
**Source** Pathfinder #48: Shadows of Gallowspire pg. 86
**XP** 307,200

NE Large undead (evil, extraplanar, _[[universal monster rules/Incorporeal|incorporeal]]_)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +35
**Aura** _[[universal monster rules/Fear|fear]]_ aura (40 ft., DC 36)

##### Defense

**AC** 32, touch 20, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+9 deflection, +2 Dex, +12 natural, –1 size)
**hp** 378 (28d8+252)
**Fort** +18, **Ref** +11, **Will** +20
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4, _incorporeal_; **DR** 15/cold iron and good; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_; **SR** 31

##### Offense
**Speed** 40 ft., fly 60 ft. (perfect)
**Melee** +3 _scythe_ +27/+22/+17/+12 (2d6+13/19–20/×4 plus death touch)
**Space** 10 ft., **Reach** 15 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +29)
Constant—fly, _[[spells/Foresight|foresight]]_, _[[spells/True Seeing|true seeing]]_
At will—_[[spells/Circle Of Death|circle of death]]_ (DC 25), _[[spells/Control Undead|control undead]]_ (DC 26), _[[spells/Invisibility|invisibility]]_, _[[spells/Plane Shift|plane shift]]_ (DC 26), _[[spells/Polymorph|polymorph]]_
3/day—_[[universal monster rules/Energy Drain|energy drain]]_ (DC 28), _[[spells/Finger Of Death|finger of death]]_ (DC 26), _[[spells/Soul Bind|soul bind]]_ (DC 28), _[[universal monster rules/Summon|summon]]_ minor reapers (level 8, 1d4 minor reapers), _[[spells/Unwilling Shield|unwilling shield]]_ (DC 25)
1/day—quickened _[[spells/Destruction|destruction]]_ (DC 26), _[[spells/Wail of the Banshee|wail of the banshee]]_ (DC 28)

##### Statistics
**Str** 24, **Dex** 15, **Con** —, **Int** 16, **Wis** 19, **Cha** 29
**Base Atk** +21; **CMB** +24; **CMD** 50 (can’t be tripped)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Greater Weapon Focus|Greater Weapon Focus]]_ (_scythe_), _[[feats/Improved Critical|Improved Critical]]_ (_scythe_), _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_destruction_), _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_scythe_)
**Skills** Diplomacy +37, Disguise +40, Fly +39, Knowledge (planes) +31, Perception +35, Sense Motive +35, Stealth +29
**Languages** Common, Celestial, Infernal; truespeech

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** double (+3 _scythe_, other treasure)

### Special Abilities

**Death Touch (Su)** Creatures hit by either a grim reaper’s touch attack or by a weapon wielded by a grim reaper must succeed at a DC 33 Fortitude save or gain 2d4 negative levels. The save DC is Charisma-based. A grim reaper can channel this ability through any weapon it wields. A humanoid slain by a reaper’s death touch is consumed in _[[items/Weapon Magic Abilities/Unholy|unholy]]_ fire and has its remains destroyed as the _destruction_ spell. This is a death effect.
**_Summon_ Minor Reapers (Sp)** Three times per day, a reaper can _summon_ 1d4 minor reapers as a standard action. Each of these minor reapers is assigned a single creature to attack, and the targeted creature must battle the minor reaper by itself. The target that the grim reaper assigns to its minor reapers need not be in sight, but it must be on the same plane on which the minor reaper was summoned. A grim reaper may only assign one minor reaper to any creature at a given time, even if it uses this ability multiple times.

##### Description

Known by many names throughout nearly all cultures, grim reapers are the personifications of death and all the pain and _fear_ associated with that state. They are universally feared by the living as harbingers of _destruction_ and masters of all that has already passed from life. These hooded beings travel through the planes with the sole intent of bringing about the end of life, slaying with a deliberateness inscrutable to all but themselves.

While grim reapers are the most feared of their kind, they are not alone. The towering, ghostlike grim reapers are served by minor reapers, corporeal servitors that enact their master’s dreadful will and meet out death’s unrelenting touch. A grim reaper is 15 feet tall and, as an _incorporeal_ creature, has no physical weight except for its equipment. Minor reapers stand 7 feet tall and weigh approximately 70 pounds.
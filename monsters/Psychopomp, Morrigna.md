---
cssclass: [monsters]
title1: Psychopomp, Morrigna
desc_short: This beautiful woman wears a mask and is completely wrapped in spider
  silk. Magical fetishes adorn her clothing and staff.
title2: Morrigna
CR: 13
sources:
- name: Bestiary 4
  page: 219
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
- name: 'Pathfinder #48: Shadows of Gallowspire'
  page: 86
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderAdventurePath/carrionCrown/v5748btpy8mgb
XP: 25600
alignment: N
size: Medium
type: outsider
subtypes:
- extraplanar
- psychopomp
initiative:
  bonus: 8
senses:
  darkvision: 60
  low-light vision: true
  spiritsense: true
AC:
  AC: 28
  touch: 13
  flat_footed: 25
  components:
    armor: 8
    dex: 3
    natural: 5
    shield: 2
HP:
  HP: 171
  long: 18d10+72
  regeneration: 5
  regeneration_weakness: acid or fire
saves:
  fort: 10
  ref: 15
  will: 16
DR:
- amount: 10
  weakness: adamantine
immunities:
- death effects
- disease
- poison
resistances:
  cold: 10
  electricity: 10
SR: 24
speeds:
  base: 40
  base_other: 30 ft. in armor
  climb: 15
attacks:
  melee:
  - - text: 2 slams +24 (2d6+6)
      entries:
      - - damage: 2d6+6
      count: 2
      attack: slams
      bonus:
      - 24
    - text: 2 wrappings +19 (1d6+3 plus grab)
      entries:
      - - damage: 1d6+3
        - effect: grab
      count: 2
      attack: wrappings
      bonus:
      - 19
  special:
  - wrappings
space: 5
reach: 5
reach_other: 10 ft. with wrappings
spell_like_abilities:
  entries:
  - name: detect undead
    source: default
    freq: At will
  - name: stone tell
    source: default
    freq: At will
  - name: speak with dead
    source: default
    freq: 5/day
  - name: summon
    source: default
    freq: 3/day
    level: 7
    summons:
    - name: giant tarantulas [Pathfinder RPG Bestiary 2 256]
      amount: 1d4
      chance: 75%
    - name: spider swarms
      amount: 1d4
      chance: 100%
  sources:
  - name: default
    CL: 12
    concentration: 15
spells:
  entries:
  - name: cure critical wounds
    source: Inquisitor
    level: 4
  - name: divination
    source: Inquisitor
    level: 4
  - name: freedom of movement
    source: Inquisitor
    level: 4
  - name: spell immunity
    source: Inquisitor
    level: 4
  - superscripts:
    - APG
    name: blood biography
    source: Inquisitor
    level: 3
    DC: 16
  - name: dimensional anchor
    source: Inquisitor
    level: 3
  - name: dispel magic
    source: Inquisitor
    level: 3
  - name: halt undead
    source: Inquisitor
    level: 3
    DC: 16
  - superscripts:
    - APG
    name: confess
    source: Inquisitor
    level: 2
    DC: 15
  - name: detect thoughts
    source: Inquisitor
    level: 2
    DC: 15
  - name: hold person
    source: Inquisitor
    level: 2
    DC: 15
  - name: invisibility
    source: Inquisitor
    level: 2
  - name: see invisibility
    source: Inquisitor
    level: 2
  - name: bane
    source: Inquisitor
    level: 1
    DC: 14
  - name: command
    source: Inquisitor
    level: 1
    DC: 14
  - name: comprehend languages
    source: Inquisitor
    level: 1
  - name: expeditious retreat
    source: Inquisitor
    level: 1
  - name: sanctuary
    source: Inquisitor
    level: 1
    DC: 14
  - superscripts:
    - APG
    name: wrath
    source: Inquisitor
    level: 1
  - name: bleed
    source: Inquisitor
    level: 0
    DC: 13
  - name: detect magic
    source: Inquisitor
    level: 0
  - name: disrupt undead
    source: Inquisitor
    level: 0
  - name: read magic
    source: Inquisitor
    level: 0
  - superscripts:
    - APG
    name: sift
    source: Inquisitor
    level: 0
  - name: stabilize
    source: Inquisitor
    level: 0
  sources:
  - name: Inquisitor
    type: known
    CL: 12
    concentration: 15
    slots:
      4: 3
      3: 5
      2: 6
      1: 6
ability_scores:
  STR: 22
  DEX: 19
  CON: 18
  INT: 13
  WIS: 17
  CHA: 16
BAB: 18
CMB: 24
CMB_other: +28 grapple
CMD: 38
feats:
- name: Alertness
- name: Combat Expertise
- name: Combat Reflexes
- is_bonus: true
  name: Deflect Arrows
- is_bonus: true
  name: Eschew Materials
- superscripts:
  - APG
  name: Following Step
- name: Improved Initiative
- name: Iron Will
- name: Persuasive
- name: Step Up
- superscripts:
  - APG
  name: Step Up and Strike
skills:
  Bluff: 15
  Climb: 11
  Diplomacy: 25
  Disguise: 15
  Intimidate: 17
  Knowledge (planes): 13
  Perception: 28
  Sense Motive: 25
  Sleight of Hand: 10
  Stealth: 22
  Survival: 15
  Swim: 6
languages:
- Abyssal
- Celestial
- Infernal
- speak with animals (including vermin)
- tongues
special_qualities:
- change shape (any animal or humanoid)
- spirit touch
ecology:
  environment: any (Purgatory)
  organization: solitary of group (3-15)
  treasure_type: standard
  treasure:
  - +2 glamered breastplate
  - other treasure
special_abilities:
  Spells: A morrigna casts spells as a 12th-level inquisitor.
  Spider Sight (Su): A morrigna can see through the eyes of a spider swarm she summons
    as though it were the sensor of an arcane eye spell. She does not have to concentrate
    to use this ability.
  Wrappings (Su): A morrigna's web wrappings grant her a +2 shield bonus to AC and
    can make secondary natural attacks.
desc_long: |-
  Morrignas are Purgatory's investigators, bounty hunters, and assassins, tracking down those who flout the natural cycle of death and judgment. They stand 7 to 8 feet tall and weigh 200 to 250 pounds.

  Many morrignas prefer to assume the appearances of those who have died. They ensure the smooth operation of death's bureaucratic machine by eliminating complications, dedicating their existence to wiping out any forces that circumvent or corrupt the natural cycle of death and judgment.

---

# Psychopomp, Morrigna
This beautiful woman wears a _[[items/Mundane/Mask|mask]]_ and is completely wrapped in spider silk. Magical fetishes adorn her clothing and staff.
**Source** Bestiary 4 pg. 219, Pathfinder #48: Shadows of Gallowspire pg. 86
**XP** 25,600

N Medium outsider (extraplanar, psychopomp)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, spiritsense; Perception +28

##### Defense

**AC** 28, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+8 armor, +3 Dex, +5 natural, +2 _[[spells/Shield|shield]]_)
**hp** 171 (18d10+72); _[[universal monster rules/Regeneration|regeneration]]_ 5 (acid or fire)
**Fort** +10, **Ref** +15, **Will** +16
**DR** 10/adamantine; **Immune** death effects, disease, poison; **Resist** cold 10, electricity 10; **SR** 24

##### Offense
**Speed** 40 ft. (30 ft. in armor), _[[universal monster rules/Climb|climb]]_ 15 ft.
**Melee** 2 slams +24 (2d6+6), 2 wrappings +19 (1d6+3 plus _[[universal monster rules/Grab|grab]]_)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with wrappings)
**Special Attacks** wrappings
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +15)
At will—_[[spells/Detect Undead|detect undead]]_, _[[spells/Stone Tell|stone tell]]_
5/day—_[[spells/Speak with Dead|speak with dead]]_
3/day—_[[universal monster rules/Summon|summon]]_ (level 7, 1d4 giant tarantulas [Pathfinder RPG Bestiary 2 256] 75% or 1d4 spider swarms 100%)
**_[[classes/Inquisitor|Inquisitor]]_ Spells Known **(CL 12th; concentration +15)
4th (3)—_[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Divination|divination]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Spell Immunity|spell immunity]]_
3rd (5)—_[[spells/Blood Biography|blood biography]]_ (DC 16), _[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Halt Undead|halt undead]]_ (DC 16)
2nd (6)—_[[spells/Confess|confess]]_ (DC 15), _[[spells/Detect Thoughts|detect thoughts]]_ (DC 15), _[[spells/Hold Person|hold person]]_ (DC 15), _[[spells/Invisibility|invisibility]]_, _[[spells/See Invisibility|see invisibility]]_
1st (6)—_[[spells/Bane|bane]]_ (DC 14), _[[spells/Command|command]]_ (DC 14), _[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 14), wrath
0—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, _[[spells/Disrupt Undead|disrupt undead]]_, _[[spells/Read Magic|read magic]]_, _[[spells/Sift|sift]]_, stabilize

##### Statistics
**Str** 22, **Dex** 19, **Con** 18, **Int** 13, **Wis** 17, **Cha** 16
**Base Atk** +18; **CMB** +24 (+28 grapple); **CMD** 38
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deflect Arrows|Deflect Arrows]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Following Step|Following Step]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Persuasive|Persuasive]]_, _[[feats/Step Up|Step Up]]_, _[[feats/Step Up and Strike|Step Up and Strike]]_
**Skills** Bluff +15, _Climb_ +11, Diplomacy +25, Disguise +15, Intimidate +17, Knowledge (planes) +13, Perception +28, Sense Motive +25, Sleight of Hand +10, Stealth +22, Survival +15, Swim +6
**Languages** Abyssal, Celestial, Infernal; _[[spells/Speak with Animals|speak with animals]]_ (including vermin), _[[spells/Tongues|tongues]]_
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (any animal or humanoid), spirit touch

##### Ecology

**Environment** any (Purgatory)
**Organization** solitary of group (3–15)
**Treasure** standard (+2 _[[items/Weapon Magic Abilities/Glamered|glamered]]_ _[[items/Armor/Breastplate|breastplate]]_, other treasure)

### Special Abilities
**Spells** A morrigna casts spells as a 12th-level _inquisitor_.
**Spider Sight (Su)** A morrigna can see through the eyes of a spider swarm she summons as though it were the sensor of an _[[spells/Arcane Eye|arcane eye]]_ spell. She does not have to concentrate to use this ability.

**Wrappings (Su)** A morrigna’s web wrappings grant her a +2 _shield_ bonus to AC and can make secondary _[[universal monster rules/Natural Attacks|natural attacks]]_.

##### Description

Morrignas are Purgatory’s investigators, bounty hunters, and assassins, tracking down those who flout the natural cycle of death and judgment. They stand 7 to 8 feet tall and weigh 200 to 250 pounds.

Many morrignas prefer to assume the appearances of those who have died. They ensure the smooth operation of death’s bureaucratic machine by eliminating complications, dedicating their existence to wiping out any forces that circumvent or corrupt the natural cycle of death and judgment.
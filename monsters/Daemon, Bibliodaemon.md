---
cssclass: [monsters]
title1: Daemon, Bibliodaemon
desc_short: Flowing black robes hang all around this four-armed, weasel-faced humanoid.
  Feathers that resemble quills emerge from each knuckle of its clawed upper hands.
title2: Bibliodaemon
CR: 8
sources:
- name: Druma, Profit and Prophecy
  page: 57
  link: https://paizo.com/products/btq01zow
XP: 4800
alignment: NE
size: Medium
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 3
senses:
  darkvision: 60
  detect thoughts: true
AC:
  AC: 22
  touch: 14
  flat_footed: 18
  components:
    dex: 3
    dodge: 1
    natural: 8
HP:
  HP: 85
  long: 10d10+30
saves:
  fort: 6
  ref: 10
  will: 9
DR:
- amount: 10
  weakness: good or silver
immunities:
- acid
- death effects
- disease
- poison
resistances:
  cold: 10
  electricity: 10
  fire: 10
SR: 19
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 light mace +15/+10 (1d6+4/19-20)
      entries:
      - - damage: 1d6+4
          crit_range: 19-20
      attack: +1 light mace
      bonus:
      - 15
      - 10
    - text: 2 claws +8 (1d6+1)
      entries:
      - - damage: 1d6+1
      count: 2
      attack: claws
      bonus:
      - 8
  special:
  - final verdict
spell_like_abilities:
  entries:
  - name: detect thoughts
    source: default
    freq: Constant
    DC: 13
  - name: erase
    source: default
    freq: At will
  - name: identify
    source: default
    freq: At will
  - name: secret page
    source: default
    freq: At will
  - name: acid arrow
    source: default
    freq: 3/day
  - name: dispel magic
    source: default
    freq: 3/day
  - name: greater teleport
    source: default
    freq: 3/day
  - name: slow
    source: default
    freq: 3/day
    DC: 14
  - name: corrosive consumption lesser geas
    source: default
    freq: 1/day
    DC: 16
  - name: misdirection
    source: default
    freq: 1/day
  - name: modify memory
    source: default
    freq: 1/day
    DC: 16
  sources:
  - name: default
    CL: 10
    concentration: 12
ability_scores:
  STR: 16
  DEX: 17
  CON: 16
  INT: 14
  WIS: 15
  CHA: 15
BAB: 10
CMB: 13
CMD: 27
feats:
- name: Dodge
- name: Improved Critical (light mace)
- name: Mobility
- name: Vital Strike
- name: Weapon Focus (light mace)
skills:
  Bluff: 15
  Intimidate: 12
  Knowledge (nobility): 15
  Linguistics: 15
  Perception: 15
  Profession (barrister): 15
  Sense Motive: 15
  Spellcraft: 15
languages:
- Abyssal
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Abaddon)
  organization: solitary, partners, or firm (3-8)
  treasure_type: standard
  treasure:
  - +1 light mace
  - other treasure
special_abilities:
  Final Verdict (Su): When a bibliodaemon hits a creature with its light mace, the
    target must succeed at a DC 17 Will save or be cursed. A creature that succeeds
    at its save is immune to that bibliodaemon's curse for 24 hours. If the bibliodaemon
    confirms a critical hit with its light mace, the save DC increases by 4, and the
    curse can affect even creatures that have already succeeded at a prior save against
    this effect. A creature that fails this save interprets any contract as favorable
    to itself, even in cases when the contract is one-sided and potentially lethal.
    In addition, an affected creature takes a -4 penalty on saves against spells and
    effects reliant on spoken commands or verbal contracts, such as geas. A remove
    curse or more powerful spell can remove this curse. The save DC is Charisma-based.
desc_long: |-
  Bibliodaemons are daemons that personify death by paperwork. A village that starves due to bureaucracy-delayed aid or an innocent person sent to hang because of a transcription error-these and more are the domain of bibliodaemons. These daemons actively work to ensure such deaths, forging important documents or duping others into deadly contracts.

   A bibliodaemon is 6 feet tall and weighs 200 pounds.

---

# Daemon, Bibliodaemon
Flowing black robes hang all around this four-armed, weasel-faced humanoid. Feathers that resemble quills emerge from each knuckle of its clawed upper hands.
**Source** Druma, Profit and Prophecy pg. 57
**XP** 4,800

NE Medium outsider (daemon, evil, extraplanar)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Thoughts|detect thoughts]]_; Perception +15

##### Defense

**AC** 22, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+3 Dex, +1 _[[feats/Dodge|dodge]]_, +8 natural)
**hp** 85 (10d10+30)
**Fort** +6, **Ref** +10, **Will** +9
**DR** 10/good or silver; **Immune** acid, death effects, disease, poison; **Resist** cold 10, electricity 10, fire 10; **SR** 19

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon/Light mace|light mace]]_ +15/+10 (1d6+4/19–20), 2 claws +8 (1d6+1)
**Special Attacks** final verdict
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +12)
Constant—_detect thoughts_ (DC 13) 
At will—_[[spells/Erase|erase]]_, _[[spells/Identify|identify]]_, _[[spells/Secret Page|secret page]]_ 
3/day—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport, _[[spells/Slow|slow]]_ (DC 14) 
1/day—_[[spells/Corrosive Consumption|corrosive consumption]]_ lesser geas (DC 16), _[[spells/Misdirection|misdirection]]_, _[[spells/Modify Memory|modify memory]]_ (DC 16)

##### Statistics
**Str** 16, **Dex** 17, **Con** 16, **Int** 14, **Wis** 15, **Cha** 15
**Base Atk** 10; **CMB** 13; **CMD** 27
**Feats** _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (_light mace_), _[[feats/Mobility|Mobility]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_light mace_)
**Skills** Bluff +15, Intimidate +12, Knowledge (nobility) +15, Linguistics +15, Perception +15, Profession (barrister) +15, Sense Motive +15, Spellcraft +15
**Languages** Abyssal, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary, partners, or firm (3–8)
**Treasure** standard (+1 _light mace_, other treasure)

### Special Abilities

**Final Verdict (Su)** When a bibliodaemon hits a creature with its _light mace_, the target must succeed at a DC 17 Will save or be cursed. A creature that succeeds at its save is immune to that bibliodaemon’s curse for 24 hours. If the bibliodaemon confirms a critical hit with its _light mace_, the save DC increases by 4, and the curse can affect even creatures that have already succeeded at a prior save against this effect. A creature that fails this save interprets any contract as favorable to itself, even in cases when the contract is one-sided and potentially lethal. In addition, an affected creature takes a –4 penalty on saves against spells and effects reliant on spoken commands or verbal contracts, such as geas. A _[[spells/Remove Curse|remove curse]]_ or more powerful spell can remove this curse. The save DC is Charisma-based.

##### Description

Bibliodaemons are daemons that personify death by paperwork. A village that starves due to bureaucracy-delayed aid or an innocent person sent to hang because of a transcription error—these and more are the domain of bibliodaemons. These daemons actively work to ensure such deaths, forging important documents or duping others into _[[items/Weapon Magic Abilities/Deadly|deadly]]_ contracts.

A bibliodaemon is 6 feet tall and weighs 200 pounds.
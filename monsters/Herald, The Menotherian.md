---
cssclass: [monsters]
title1: Herald, The Menotherian
desc_short: This gangly black wasp has delicate wings, articulate hands on its front
  legs, and a pair of jagged stingers the length of a human arm.
title2: The Menotherian
CR: 15
sources:
- name: Inner Sea Gods
  page: 280
  link: http://paizo.com/products/btpy94wj?Pathfinder-Campaign-Setting-Inner-Sea-Gods-Hardcover
XP: 51200
alignment: CN
size: Large
type: outsider
subtypes:
- chaotic
- extraplanar
- herald
- shapechanger
initiative:
  bonus: 9
senses:
  darkvision: 60
  low-light vision: true
  scent: true
auras:
- name: alluring scent
  radius: 30
  DC: 25
  duration: 1 hour
AC:
  AC: 31
  touch: 14
  flat_footed: 26
  components:
    dex: 5
    natural: 17
    size: -1
HP:
  HP: 202
  long: 15d10+120
saves:
  fort: 17
  ref: 16
  will: 9
DR:
- amount: 15
  weakness: lawful
immunities:
- disease
- poison
resistances:
  electricity: 10
  fire: 10
SR: 26
speeds:
  base: 50
  climb: 20
  fly: 50
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +24 (1d8+9)
      entries:
      - - damage: 1d8+9
      attack: bite
      bonus:
      - 24
    - text: 2 claws +23 (1d6+9)
      entries:
      - - damage: 1d6+9
      count: 2
      attack: claws
      bonus:
      - 23
    - text: sting +24 (2d8+9 plus poison)
      entries:
      - - damage: 2d8+9
        - effect: poison
      attack: sting
      bonus:
      - 24
  special:
  - implant
  - mind control
  - poison
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: dimension door
    source: default
    freq: At will
  - name: dispel magic
    source: default
    freq: At will
  - superscripts:
    - ISWG
    name: lover's vengeance
    source: default
    freq: At will
  - name: message
    source: default
    freq: At will
  - name: neutralize poison
    source: default
    freq: At will
  - name: rage
    source: default
    freq: At will
  - name: secret speech
    source: default
    freq: At will
  - name: crushing despair
    source: default
    freq: 5/day
    DC: 19
  - name: cat's grace
    source: default
    freq: 5/day
  - name: cure moderate wounds
    source: default
    freq: 5/day
  - name: remove disease
    source: default
    freq: 5/day
  - name: suggestion
    source: default
    freq: 5/day
    DC: 18
  - name: summon swarm
    source: default
    freq: 5/day
  - name: telekinesis
    source: default
    freq: 5/day
  - name: teleport
    source: default
    freq: 5/day
  - name: wall of thorns
    source: default
    freq: 5/day
  - name: heal
    source: default
    freq: 1/day
  - name: insect plague
    source: default
    freq: 1/day
  - name: scrying
    source: default
    freq: 1/day
    DC: 19
  sources:
  - name: default
    CL: 14
    concentration: 19
ability_scores:
  STR: 28
  DEX: 20
  CON: 26
  INT: 18
  WIS: 18
  CHA: 20
BAB: 15
CMB: 25
CMD: 40
CMD_other: 48 vs. trip
feats:
- name: Combat Reflexes
- name: Hover
- name: Improved Initiative
- name: Lightning Reflexes
- name: Power Attack
- name: Step Up
- name: Weapon Focus (bite)
- name: Weapon Focus (sting)
skills:
  Acrobatics: 20
  Bluff: 23
  Climb: 17
  Diplomacy: 23
  Fly: -1
  Heal: 11
  Intimidate: 23
  Knowledge (history): 15
  Knowledge (planes): 15
  Knowledge (nature): 12
  Perception: 22
  Perform (dance): 12
  Sense Motive: 22
  Spellcraft: 14
  Stealth: 19
languages:
- Abyssal
- Common
- Elven
- telepathy 100 ft.
special_qualities:
- change shape (elf, wasp, or giant wasp; alter self or vermin shape II)
ecology:
  environment: any (Elysium)
  organization: solitary
  treasure_type: none
special_abilities:
  Alluring Scent (Ex): The Menotherian's subtle aroma causes creatures in her vicinity
    to become placid and react favorably toward her. Any creature that fails a DC
    25 Fortitude save against the aura improves its attitude toward the Menotherian
    one step closer to friendly. Creatures with the scent ability take a -4 penalty
    on this saving throw. Creatures in the aura must attempt a saving throw each minute.
    This is a mind-affecting poison effect. The DC is Constitution-based.
  Implant (Ex): Once per day, the Menotherian can implant eggs in a creature using
    its sting. The creature must succeed at a DC 25 Fortitude save to resist implantation.
    The target is nauseated for the next 2d4 rounds while the eggs gestate. When the
    eggs hatch, they form a chaotic neutral hellwasp swarm (Pathfinder RPG Bestiary
    3 146), kill the host in 1 round, and inhabit the corpse. The eggs can be surgically
    removed with a successful DC 30 Heal check (this check deals 2d6 points of damage
    to the host regardless of success) or by remove disease or similar spells. The
    save DC is Constitution-based.
  Mind Control (Ex): The menotherian can inject its scent into the brain of a helpless
    or willing target, controlling it for the next 24 hours (as the spell dominate
    person, Fortitude DC 25 negates), although the Menotherian must verbally give
    the target instructions. The save DC is Constitution-based.
  Poison (Ex): Sting-injury; save Fort DC 25; frequency 1/round for 6 rounds; effect
    1d3 Dex damage; cure 2 consecutive saves.
desc_long: The Menotherian is a personification of lust and vengeance. Bereft of morals,
  she seduces, tricks, or murders any creature necessary to complete whatever mission
  Calistria sends her to upon. The herald stands 14 feet tall, has a wingspan nearing
  30 feet, and weighs 1,400 pounds.

---

# Herald, The Menotherian
This gangly black wasp has delicate wings, articulate hands on its front legs, and a pair of jagged stingers the length of a human arm.
**Source** Inner Sea Gods pg. 280
**XP** 51,200

CN Large outsider (chaotic, extraplanar, herald, shapechanger)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +22
**Aura** alluring _scent_ (30 ft., DC 25, 1 hour)

##### Defense

**AC** 31, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+5 Dex, +17 natural, –1 size)
**hp** 202 (15d10+120)
**Fort** +17, **Ref** +16, **Will** +9
**DR** 15/lawful; **Immune** disease, poison; **Resist** electricity 10, fire 10; **SR** 26

##### Offense
**Speed** 50 ft., _[[universal monster rules/Climb|climb]]_ 20 ft., fly 50 ft. (poor)
**Melee** bite +24 (1d8+9), 2 claws +23 (1d6+9), sting +24 (2d8+9 plus poison)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** implant, mind control, poison
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +19)
At will—_[[spells/Dimension Door|dimension door]]_, _[[spells/Dispel Magic|dispel magic]]_, lover’s _[[feats/Vengeance|vengeance]]_, _[[spells/Message|message]]_, _[[spells/Neutralize Poison|neutralize poison]]_, _[[spells/Rage|rage]]_, _[[spells/Secret Speech|secret speech]]_
5/day—_[[spells/Crushing Despair|crushing despair]]_ (DC 19), cat’s _[[spells/Grace|grace]]_, _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Remove Disease|remove disease]]_, _[[spells/Suggestion|suggestion]]_ (DC 18), _[[spells/Summon Swarm|summon swarm]]_, _[[spells/Telekinesis|telekinesis]]_, teleport, _[[spells/Wall Of Thorns|wall of thorns]]_
1/day—_[[spells/Heal|heal]]_, _[[spells/Insect Plague|insect plague]]_, _[[spells/Scrying|scrying]]_ (DC 19)

##### Statistics
**Str** 28, **Dex** 20, **Con** 26, **Int** 18, **Wis** 18, **Cha** 20
**Base Atk** +15; **CMB** +25; **CMD** 40 (48 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Step Up|Step Up]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite), _Weapon Focus_ (sting)
**Skills** Acrobatics +20, Bluff +23, _Climb_ +17, Diplomacy +23, Fly –1, _Heal_ +11, Intimidate +23, Knowledge (history, planes) +15, Knowledge (nature) +12, Perception +22, Perform (dance) +12, Sense Motive +22, Spellcraft +14, Stealth +19
**Languages** Abyssal, Common, Elven; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (elf, wasp, or giant wasp; _[[spells/Alter Self|alter self]]_ or _[[spells/Vermin Shape II|vermin shape II]]_)

##### Ecology

**Environment** any (Elysium)
**Organization** solitary
**Treasure** none

### Special Abilities

**Alluring _Scent_ (Ex)** The _[[monsters/Menotherian|Menotherian]]_’s subtle aroma causes creatures in her vicinity to become placid and react favorably toward her. Any creature that fails a DC 25 Fortitude save against the aura improves its attitude toward the _Menotherian_ one step closer to friendly. Creatures with the _scent_ ability take a –4 penalty on this saving throw. Creatures in the aura must attempt a saving throw each minute. This is a mind-affecting poison effect. The DC is Constitution-based.

**Implant (Ex)** Once per day, the _Menotherian_ can implant eggs in a creature using its sting. The creature must succeed at a DC 25 Fortitude save to resist implantation. The target is _[[conditions/Nauseated|nauseated]]_ for the next 2d4 rounds while the eggs gestate. When the eggs hatch, they form a chaotic neutral _[[monsters/Hellwasp Swarm|hellwasp swarm]]_ (Pathfinder RPG Bestiary 3 146), kill the host in 1 round, and inhabit the corpse. The eggs can be surgically removed with a successful DC 30 _Heal_ check (this check deals 2d6 points of damage to the host regardless of success) or by _remove disease_ or similar spells. The save DC is Constitution-based.

**Mind Control (Ex)** The _menotherian_ can inject its _scent_ into the brain of a _[[conditions/Helpless|helpless]]_ or willing target, controlling it for the next 24 hours (as the spell _[[spells/Dominate Person|dominate person]]_, Fortitude DC 25 negates), although the _Menotherian_ must verbally give the target instructions. The save DC is Constitution-based.

**Poison (Ex)** Sting—injury; save Fort DC 25; frequency 1/round for 6 rounds; effect 1d3 Dex damage; cure 2 consecutive saves.

##### Description

The _Menotherian_ is a personification of lust and _vengeance_. Bereft of morals, she seduces, tricks, or murders any creature necessary to complete whatever mission Calistria sends her to upon. The herald stands 14 feet tall, has a wingspan nearing 30 feet, and weighs 1,400 pounds.
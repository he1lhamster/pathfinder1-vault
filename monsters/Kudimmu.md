---
cssclass: [monsters]
title1: Kudimmu
desc_short: Tumorous, misshapen vines laden with dark red fruit make up the form of
  this lumbering humanoid creature, and its face is marked only by a pair of glowing,
  crimson eyes.
title2: Kudimmu
CR: 16
sources:
- name: 'Pathfinder #114: Black Stars Beckon'
  page: 86
  link: http://paizo.com/products/btpy9qcm?Pathfinder-Adventure-Path-114-Black-Stars-Beckon
XP: 76800
alignment: NE
size: Large
type: plant
initiative:
  bonus: 10
senses:
  low-light vision: true
  tremorsense: 30
AC:
  AC: 31
  touch: 15
  flat_footed: 25
  components:
    dex: 6
    natural: 16
    size: -1
HP:
  HP: 252
  long: 24d8+144
  fast_healing: 15
saves:
  fort: 20
  ref: 14
  will: 15
defensive_abilities:
- amorphous
DR:
- amount: 10
  weakness: magic and slashing
immunities:
- death effects
- energy drain
- negative energy
- plant traits
resistances:
  cold: 10
  fire: 10
SR: 27
speeds:
  base: 30
  burrow: 15
attacks:
  melee:
  - - text: 2 slam +28 (2d4+11 plus grab)
      entries:
      - - damage: 2d4+11
        - effect: grab
      count: 2
      attack: slam
      bonus:
      - 28
    - text: 4 tentacles +27 (1d6+5 plus bleed and pull)
      entries:
      - - damage: 1d6+5
        - effect: bleed
        - effect: pull
      count: 4
      attack: tentacles
      bonus:
      - 27
  ranged:
  - - text: bombardment +23 touch (8d6 negative energy plus splash)
      entries:
      - - damage: 8d6
          type: negative energy
        - effect: splash
      attack: bombardment
      bonus:
      - 23
      touch: true
  special:
  - bleed (1d6)
  - blood drain (1d4 Constitution)
  - bombardment
  - create spawn
  - pull (tentacle, 5 ft.)
space: 10
reach: 10
reach_other: 30 ft. with tentacles
spell_like_abilities:
  entries:
  - name: wall of thorns
    source: default
    freq: 3/day
  - name: animate plants
    source: default
    freq: 1/day
    DC: 20
  sources:
  - name: default
    CL: 24
    concentration: 27
ability_scores:
  STR: 32
  DEX: 22
  CON: 22
  INT: 13
  WIS: 21
  CHA: 17
BAB: 18
CMB: 30
CMD: 46
CMD_other: 48 vs. trip
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Dimensional Agility
- name: Dimensional Assault
- name: Dimensional Dervish
- name: Dimensional Savant
- name: Improved Initiative
- name: Improved Trip
- name: Iron Will
- name: Multiattack
- name: Power Attack
- name: Weapon Focus (tentacle)
skills:
  Perception: 32
  Sense Motive: 29
  Stealth: 29
languages:
- Azlanti
- Sylvan (can't speak)
- telepathy 100 ft.
special_qualities:
- bloodfruit
- fieldbound
ecology:
  environment: any land
  organization: solitary
  treasure_type: standard
special_abilities:
  Bloodfruit (Su): 'Fruit-bearing plants in a kudimmu's field produce sickly, misshapen,
    blood-red versions of normal fruits of the same variety. An undead creature can
    consume a kudimmu's bloodfruit in place of whatever bodily material it normally
    hungers for, whether blood, flesh, or something else. Doing so temporarily sates
    the undead creature's hunger, but does not provide any other benefits normally
    gained from consumption. Upon consuming bloodfruit, an undead creature must succeed
    at a DC 25 Will saving throw or fall under the kudimmu's control, as per control
    undead. A living creature treats bloodfruit as a drug with the following statistics
    (see page 236 of the Pathfinder RPG GameMastery Guide for full rules on drugs
    and addiction): type ingested; addiction severe, Fortitude DC 25; effects 1 hour;
    +2 alchemical bonus on saving throws against necromancy spells and effects, fester
    as per the spell (caster level 24th); damage 1d4 Con. The save DC is Charisma-based.'
  Bombardment (Su): A kudimmu can produce bloodfruit from its body, which are charged
    with negative energy and can be thrown as splash weapons. These bloodfruit deal
    8d6 points of negative energy damage on a direct hit, and 8 points of damage to
    creatures adjacent to the targeted square. A successful DC 25 Will saving throw
    halves this damage. The save DC is Charisma-based.
  Create Spawn (Su): A creature killed by the kudimmu's blood drain ability or by
    Constitution damage accrued through consuming bloodfruit rises as a vampire spawn
    under the kudimmu's control 1d4 days later. A kudimmu can have a number of enslaved
    spawn totaling at most double its own Hit Dice; any spawn it creates that would
    exceed this limit become free-willed undead.
  Fieldbound (Ex, Sp, Su): A kudimmu can designate an area of natural vegetation up
    to 100 feet by 100 feet per side as its field, fusing the root systems of the
    area's plants into an interconnected mass. While in physical contact with the
    ground of its field, a kudimmu gains fast healing 15, tremorsense, and a 15-foot
    burrow speed. Additionally, the kudimmu can teleport to any location in its field
    as per dimension door. Spells and effects that attempt to alter the field's earth
    or vegetation must overcome the kudimmu's spell resistance to succeed. The kudimmu
    is physically dependent on its field, as the root system beneath it is in many
    ways an extension of the kudimmu's body. A kudimmu separated from its field for
    more than 24 hours instantly decays into a lump of inanimate matter. A kudimmu
    that is slain or destroyed reforms in the ground beneath its field in a process
    that takes 1d10 days to complete. To prevent a kudimmu from reviving, its field
    must be sown with salt or destroyed by magic (merely destroying the surface plants
    is not sufficient-the roots must also be entirely destroyed). A kudimmu must maintain
    its field with the blood of the living. The field must soak up the blood of a
    Medium or larger creature once per week. For each week the kudimmu fails to feed
    its field, it takes 2 points of Constitution damage. This damage cannot be healed
    until the kudimmu feeds its field. A kudimmu can designate a new field once per
    month in a process that takes 1 hour to complete. It can have only one active
    field at a time.
desc_long: |-
  When a city is destroyed, it is customary for the conquering army to sow salt or thorns to render the ground forever infertile and curse those who would dare to rebuild. In most cases, this is simply a symbolic gesture. However, this ritual has eminently practical roots. Death and devastation are potent seeds, and the blood of conquered peoples can mingle with the roots of burned fields to produce terrible creatures. These are called kudimmus, twisted weeds that corrupt the ground of vanquished cities and exact a terrible price upon invaders.

  A kudimmu's body is diffused throughout its field, and it can weigh tens of thousands of pounds. Its primary fruiting body is vaguely humanoid in shape, standing 10 feet tall and weighing 4,000 pounds.

---

# Kudimmu
Tumorous, misshapen vines laden with dark red fruit make up the form of this lumbering humanoid creature, and its face is marked only by a pair of glowing, crimson eyes.
**Source** Pathfinder #114: Black Stars Beckon pg. 86
**XP** 76,800

NE Large plant
**Init** +10; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 30 ft.; Perception +32

##### Defense

**AC** 31, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+6 Dex, +16 natural, –1 size)
**hp** 252 (24d8+144); _[[universal monster rules/Fast Healing|fast healing]]_ 15
**Fort** +20, **Ref** +14, **Will** +15
**Defensive Abilities** _[[universal monster rules/Amorphous|amorphous]]_; **DR** 10/magic and slashing; **Immune** death effects, _[[universal monster rules/Energy Drain|energy drain]]_, negative energy, _[[universal monster rules/Plant Traits|plant traits]]_; **Resist** cold 10, fire 10; **SR** 27

##### Offense
**Speed** 30 ft., _[[universal monster rules/Burrow|burrow]]_ 15 ft.
**Melee** 2 slam +28 (2d4+11 plus _[[universal monster rules/Grab|grab]]_), 4 tentacles +27 (1d6+5 plus _[[universal monster rules/Bleed|bleed]]_ and _[[universal monster rules/Pull|pull]]_)
**Ranged** bombardment +23 touch (8d6 negative energy plus splash)
**Space** 10 ft., **Reach** 10 ft. (30 ft. with tentacles)
**Special Attacks** _bleed_ (1d6), _[[universal monster rules/Blood Drain|blood drain]]_ (1d4 Constitution), bombardment, create spawn, _pull_ (tentacle, 5 ft.)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 24th; concentration +27)
3/day—_[[spells/Wall Of Thorns|wall of thorns]]_
1/day—_[[spells/Animate Plants|animate plants]]_ (DC 20)

##### Statistics
**Str** 32, **Dex** 22, **Con** 22, **Int** 13, **Wis** 21, **Cha** 17
**Base Atk** +18; **CMB** +30; **CMD** 46 (48 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Dimensional Agility|Dimensional Agility]]_, _[[feats/Dimensional Assault|Dimensional Assault]]_, _[[feats/Dimensional Dervish|Dimensional Dervish]]_, _[[feats/Dimensional Savant|Dimensional Savant]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (tentacle)
**Skills** Perception +32, Sense Motive +29, Stealth +29
**Languages** Azlanti, Sylvan (can’t speak); _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** bloodfruit, fieldbound

##### Ecology

**Environment** any land
**Organization** solitary
**Treasure** standard

### Special Abilities

**Bloodfruit (Su)** Fruit-bearing plants in a _[[monsters/Kudimmu|kudimmu]]_’s field produce sickly, misshapen, blood-red versions of normal fruits of the same variety. An undead creature can consume a _kudimmu_’s bloodfruit in place of whatever bodily material it normally hungers for, whether blood, flesh, or something else. Doing so temporarily sates the undead creature’s hunger, but does not provide any other benefits normally gained from _[[feats/Consumption|consumption]]_. Upon consuming bloodfruit, an undead creature must succeed at a DC 25 Will saving throw or fall under the _kudimmu_’s control, as per _[[spells/Control Undead|control undead]]_. A living creature treats bloodfruit as a drug with the following statistics (see page 236 of the Pathfinder RPG GameMastery Guide for full rules on drugs and addiction): type ingested; addiction severe, Fortitude DC 25; effects 1 hour; +2 alchemical bonus on saving throws against necromancy spells and effects, _[[spells/Fester|fester]]_ as per the spell (caster level 24th); damage 1d4 Con. The save DC is Charisma-based.

**Bombardment (Su)** A _kudimmu_ can produce bloodfruit from its body, which are charged with negative energy and can be thrown as splash weapons. These bloodfruit deal 8d6 points of negative energy damage on a direct hit, and 8 points of damage to creatures adjacent to the targeted square. A successful DC 25 Will saving throw halves this damage. The save DC is Charisma-based.

**Create Spawn (Su)** A creature killed by the _kudimmu_’s _blood drain_ ability or by Constitution damage accrued through consuming bloodfruit rises as a _[[monsters/Vampire Spawn|vampire spawn]]_ under the _kudimmu_’s control 1d4 days later. A _kudimmu_ can have a number of enslaved spawn totaling at most double its own Hit Dice; any spawn it creates that would exceed this limit become free-willed undead.

**Fieldbound (Ex, Sp, Su)** A _kudimmu_ can designate an area of natural vegetation up to 100 feet by 100 feet per side as its field, fusing the _[[spells/Root|root]]_ systems of the area’s plants into an interconnected mass. While in physical contact with the ground of its field, a _kudimmu_ gains _fast healing_ 15, _tremorsense_, and a 15-foot _burrow_ speed. Additionally, the _kudimmu_ can teleport to any location in its field as per _[[spells/Dimension Door|dimension door]]_. Spells and effects that attempt to alter the field’s earth or vegetation must overcome the _kudimmu_’s _[[universal monster rules/Spell Resistance|spell resistance]]_ to succeed. The _kudimmu_ is physically dependent on its field, as the _root_ system beneath it is in many ways an extension of the _kudimmu_’s body. A _kudimmu_ separated from its field for more than 24 hours instantly decays into a lump of inanimate matter. A _kudimmu_ that is slain or destroyed reforms in the ground beneath its field in a process that takes 1d10 days to complete. To prevent a _kudimmu_ from reviving, its field must be sown with salt or destroyed by magic (merely destroying the surface plants is not sufficient—the roots must also be entirely destroyed). A _kudimmu_ must maintain its field with the blood of the living. The field must soak up the blood of a Medium or larger creature once per week. For each week the _kudimmu_ fails to feed its field, it takes 2 points of Constitution damage. This damage cannot be healed until the _kudimmu_ feeds its field. A _kudimmu_ can designate a new field once per month in a process that takes 1 hour to complete. It can have only one active field at a time.

##### Description

When a city is destroyed, it is customary for the conquering army to sow salt or thorns to render the ground forever infertile and curse those who would dare to rebuild. In most cases, this is simply a symbolic gesture. However, this ritual has eminently practical roots. Death and devastation are _[[items/Weapon Magic Abilities/Potent|potent]]_ seeds, and the blood of conquered peoples can mingle with the roots of burned fields to produce terrible creatures. These are _[[items/Weapon Magic Abilities/Called|called]]_ kudimmus, twisted weeds that corrupt the ground of vanquished cities and exact a terrible price upon invaders.

A _kudimmu_’s body is diffused throughout its field, and it can weigh tens of thousands of pounds. Its primary fruiting body is vaguely humanoid in shape, standing 10 feet tall and weighing 4,000 pounds.
---
cssclass: [monsters]
title1: Treant
desc_short: Standing upright and powerful, this mighty tree-person channels nature's
  fury into green energy in its gnarled hands.
title2: Mythic Treant
CR: 10
MR: 4
sources:
- name: Mythic Adventures
  page: 218
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 9600
alignment: NG
size: Huge
type: plant
subtypes:
- mythic
initiative:
  bonus: -1
senses:
  low-light vision: true
AC:
  AC: 25
  touch: 7
  flat_footed: 25
  components:
    dex: -1
    natural: 18
    size: -2
HP:
  HP: 146
  long: 12d8+92
saves:
  fort: 13
  ref: 3
  will: 10
DR:
- amount: 10
  weakness: epic and slashing
immunities:
- plant traits
weaknesses:
- vulnerable to fire
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 slams +19 (3d6+10/18-20)
      entries:
      - - damage: 3d6+10
          crit_range: 18-20
      count: 2
      attack: slams
      bonus:
      - 19
  ranged:
  - - text: rock +7 (2d6+15)
      entries:
      - - damage: 2d6+15
      attack: rock
      bonus:
      - 7
  special:
  - mythic power (4/day, surge +1d8)
  - rock throwing (180 ft.)
  - trample (3d6+15, DC 26)
  - druidic magic
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: animal messenger
    source: default
    freq: 7/day
  - name: calm animals
    source: default
    freq: 7/day
    DC: 15
  - name: create water
    source: default
    freq: 7/day
  - name: entangle
    source: default
    freq: 7/day
    DC: 15
  - name: magic fang
    source: default
    freq: 7/day
  - name: neutralize poison
    source: default
    freq: 7/day
  - name: quench
    source: default
    freq: 7/day
    DC: 17
  - name: sleep
    source: default
    freq: 7/day
    DC: 15
  - name: wind wall
    source: default
    freq: 7/day
  - name: wood shape
    source: default
    freq: 7/day
  - name: cure serious wounds
    source: default
    freq: 3/day
  - name: darkness
    source: default
    freq: 3/day
  - name: rusting grasp
    source: default
    freq: 3/day
  - name: shout
    source: default
    freq: 3/day
    DC: 18
  - name: summon nature's ally IV
    source: default
    freq: 3/day
  - name: call lightning storm
    source: default
    freq: 1/day
    DC: 19
  sources:
  - name: default
    CL: 10
    concentration: 14
    DC_ability_score: Wisdom
ability_scores:
  STR: 31
  DEX: 8
  CON: 21
  INT: 12
  WIS: 18
  CHA: 13
BAB: 9
CMB: 21
CMB_other: +23 sunder
CMD: 32
CMD_other: 34 vs. sunder
feats:
- name: Alertness
- is_mythic: true
  name: Improved Critical (slam)
- name: Improved Sunder
- name: Iron Will
- name: Power Attack
- is_mythic: true
  name: Weapon Focus (slam)
skills:
  Diplomacy: 9
  Intimidate: 9
  Knowledge (nature): 9
  Perception: 17
  Sense Motive: 10
  Stealth: -9
    in forests: 7
  _racial_mods:
    Stealth:
      in forests: 16
languages:
- Common
- Sylvan
- Treant
- treespeech
special_qualities:
- animate trees
- double damage against objects
- drink deep
- woodland stride
ecology:
  environment: any forest
  organization: solitary or grove (2-7)
  treasure_type: standard
special_abilities:
  Animate Trees (Sp): A mythic treant can animate and control up to two trees within
    180 feet at will. It takes 1 full round for a tree to uproot itself, after which
    it moves at a speed of 10 feet and fights as a non-mythic treant (Bestiary 266).
    It has only one slam attack, lacks the treant's animation and rock-throwing abilities,
    and has the treant's vulnerability to fire. If the treant terminates the animation,
    moves out of range, or is incapacitated, the tree immediately takes root wherever
    it is and returns to its normal state. If the treant expends one use of mythic
    power when it animates a tree, the tree remains animated and under the treant's
    control up to a range of 1 mile, and it doesn't count toward the treant's limit
    of controlling up to two trees at a time.
  Double Damage Against Objects (Ex): A mythic treant or animated tree that makes
    a full attack against an object or structure deals double damage.
  Drink Deep (Su): A mythic treant can expend one use of mythic power to lose its
    vulnerability to fire for 1 hour.
  Treespeech (Ex): A treant has the ability to converse with plants as if subject
    to a continual speak with plants spell, and most plants greet it with an attitude
    of friendly or helpful.
  Druidic Magic (Su): A mythic treant can expend one use of mythic power to cast any
    druid spell of 3rd level or lower, or two uses of mythic power to cast any druid
    spell of 5th level or lower. Its caster level for this spell is 10th.
desc_long: A mythic treant is an ancient entity granted power by a deity or magical
  pool. They're the shepherds of forests, and even less likely to converse with shortlived
  races.

---

# Treant
This _[[items/Armor Magic Abilities/Animated|animated]]_ tree’s bark is knotted into vaguely humanoid features, with branches for arms and roots for legs.
**Source** Pathfinder RPG Bestiary pg. 266
**XP** 4,800

NG Huge plant
**Init** –1; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +12

##### Defense

**AC** 21, touch 7, _[[conditions/Flat-Footed|flat-footed]]_ 21 (–1 Dex, +14 natural, –2 size)
**hp** 114 (12d8+60)
**Fort** +13, **Ref** +3, **Will** +9
**DR** 10/slashing; **Immune** _[[universal monster rules/Plant Traits|plant traits]]_
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to fire

##### Offense
**Speed** 30 ft.
**Melee** 2 slams +17 (2d6+9/19–20)
**Ranged** rock +7 (2d6+13)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _[[universal monster rules/Rock Throwing|rock throwing]]_ (180 ft.), _[[universal monster rules/Trample|trample]]_ (2d6+13, DC 25)

##### Statistics
**Str** 29, **Dex** 8, **Con** 21, **Int** 12, **Wis** 16, **Cha** 13
**Base Atk** +9; **CMB** +20; **CMD** 29
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Improved Critical|Improved Critical]]_ (slam), _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (slam)
**Skills** Diplomacy +9, Intimidate +9, Knowledge (nature) +9, Perception +12, Sense Motive +9, Stealth –9 (+7 in forests); **Racial Modifiers** +16 Stealth in forests
**Languages** Common, Sylvan, _[[monsters/Treant|Treant]]_
**SQ** animate trees, double damage against objects, treespeech

##### Ecology

**Environment** any forest
**Organization** solitary or grove (2–7)
**Treasure** standard

### Special Abilities

**Animate Trees (Sp)** A _treant_ can animate any trees within 180 feet at will, controlling up to two trees at a time. It takes 1 full round for a tree to uproot itself, after which it moves at a speed of 10 feet and fights as a _treant_ (although it has only one slam attack and lacks the _treant_’s animation and rock-throwing abilities), gaining the _treant_’s _vulnerability_ to fire. If the _treant_ that _animated_ it terminates the animation, moves out of range, or is incapacitated, the tree immediately takes _[[spells/Root|root]]_ wherever it is and returns to its normal state.

**Double Damage Against Objects (Ex)** A _treant_ or _animated_ tree that makes a full attack against an object or structure deals double damage.

**Treespeech (Ex)** A _treant_ has the ability to converse with plants as if subject to a continual _[[spells/Speak with Plants|speak with plants]]_ spell, and most plants greet them with an attitude of friendly or helpful.

##### Description

Treants are guardians of the forest and speakers for the trees. As long-lived as the forests themselves, and seeing themselves as parents and shepherds rather than gardeners, treants are _[[spells/Slow|slow]]_ and methodical in most things but terrifying when forced to fight in defense of their flock. Though they rarely seek out the companionship of the short-lived races, and have an inherent distrust of change, they have been known to tolerate those who seek to learn from their long, rambling monologues, especially if the pupils express a desire to help protect the wildlands. Yet against those who would threaten the forest, especially loggers who seek to harvest wood for lumber or those who try to clearcut a section of forest in order to build a fort or establish a town, the treants’ wrath is swift and devastating. They are particularly gifted at tearing down what others build—a trait that serves angry treants well.

Treants are primarily solitary creatures, with a given individual sometimes responsible for an entire forest, but they occasionally come together in small groups _[[items/Weapon Magic Abilities/Called|called]]_ groves to share news and reproduce. In times of grave danger, all of the groves in a region may gather for a great months-long meeting _called_ a moot, but such events are exceedingly rare, and millennia may go by between them.

The typical _treant_ is 30 feet tall, with a trunk 2 feet in diameter, and weighs 4,500 pounds. Treants tend to resemble the species of trees most common in their woodland territories.
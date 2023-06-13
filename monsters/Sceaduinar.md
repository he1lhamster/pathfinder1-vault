---
cssclass: [monsters]
title1: Sceaduinar
desc_short: This gargoyle-like creature has long spiky legs and a bat-like head-its
  body seems to be made of living, dark purple crystal.
title2: Sceaduinar
CR: 7
sources:
- name: Bestiary 2
  page: 239
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 3200
alignment: NE
size: Medium
type: outsider
subtypes:
- extraplanar
initiative:
  bonus: 5
senses:
  darkvision: 120
  lifesense: true
  low-light vision: true
AC:
  AC: 20
  touch: 16
  flat_footed: 14
  components:
    dex: 5
    dodge: 1
    natural: 4
HP:
  HP: 85
  long: 9d10+36
saves:
  fort: 10
  ref: 11
  will: 5
defensive_abilities:
- entropic flesh
- negative energy affinity
- void child
DR:
- amount: 10
  weakness: adamantine or good
immunities:
- cold
- death effects
- disease
- energy drain
- poison
resistances:
  acid: 10
  electricity: 10
  sonic: 10
SR: 18
speeds:
  base: 40
  fly: 90
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +14 (1d6+3 plus 1d6 negative energy and energy drain)
      entries:
      - - damage: 1d6+3
        - damage: 1d6
          type: negative energy
        - effect: energy drain
      attack: bite
      bonus:
      - 14
    - text: 2 wings +9 (1d6+1 plus 1d6 negative energy)
      entries:
      - - damage: 1d6+1
        - damage: 1d6
          type: negative energy
      count: 2
      attack: wings
      bonus:
      - 9
  special:
  - energy drain (1 level, DC 17)
  - entropic touch
spell_like_abilities:
  entries:
  - name: entropic shield
    source: default
    freq: Constant
  - name: hide from undead
    source: default
    freq: Constant
    DC: 14
  - name: bleed
    source: default
    freq: At will
    DC: 13
  - name: dimension door
    source: default
    freq: At will
    other: self only
  - name: dispel magic
    source: default
    freq: At will
  - name: death knell
    source: default
    freq: 3/day
    DC: 15
  - name: deeper darkness
    source: default
    freq: 3/day
  - name: enervation
    source: default
    freq: 3/day
  - name: inflict serious wounds
    source: default
    freq: 3/day
    DC: 16
  - name: silence
    source: default
    freq: 3/day
  - name: antilife shell
    source: default
    freq: 1/day
  - name: greater teleport
    source: default
    freq: 1/day
    other: self plus 50 lbs. of objects only
  - name: harm
    source: default
    freq: 1/day
    DC: 19
  - name: slay living
    source: default
    freq: 1/day
    DC: 18
  sources:
  - name: default
    CL: 9
    concentration: 12
ability_scores:
  STR: 17
  DEX: 20
  CON: 18
  INT: 13
  WIS: 14
  CHA: 17
BAB: 9
CMB: 12
CMD: 28
feats:
- name: Dodge
- name: Mobility
- name: Skill Focus (Perception)
- name: Step Up
- name: Weapon Finesse
skills:
  Escape Artist: 17
  Fly: 9
  Intimidate: 15
  Knowledge (nature): 13
  Knowledge (planes): 17
  Perception: 17
  Sense Motive: 14
  Stealth: 25
  _racial_mods:
    Knowledge (planes):
      _: 4
    Stealth:
      _: 8
languages:
- Aklo
- Common
ecology:
  environment: any (Negative Energy Plane)
  organization: solitary or death squad (2-11)
  treasure_type: standard
special_abilities:
  Entropic Flesh (Ex): Any creature that hits a sceaduinar with a melee attack takes
    1d6 points of negative energy damage. Attacking with a weapon that provides reach
    allows a creature to avoid taking this damage.
  Entropic Touch (Ex): A sceaduinar's natural attacks can strike incorporeal creatures
    as if they were ghost touch weapons. All of a sceaduinar's natural attacks deal
    +1d6 points of negative energy damage to the target. This energy does not heal
    creatures healed by inflict spells.
  Void Child (Ex): Sceaduinars are immune to effects that target souls (such as trap
    the soul) or require knowledge of a creature's identity (such as scrying). When
    one is slain, it cannot be restored to life by magic save by a miracle or wish,
    or by divine intervention.
desc_long: |-
  Sceaduinars are strange creatures born of pure entropy, the antithesis of creation and life. In the cold heart of the Negative Energy Plane, the un-substance of that realm coalesces into snowflake-like crystals, and it is from these strange formations that sceaduinars arise, breaking free from their jagged “eggs” fully grown. They hate the living and the undead with equal passion, perhaps out of jealousy for those who have a spark of life (even if that spark is provided by a corruption of life in the form of undeath), though they usually ignore creatures from the Outer Sphere. They believe their positive energy counterparts, the jyoti, long ago stole their ability to create, breaking the parallel between the two energy planes and forcing these void-dwellers into an unwanted role of pure destruction.

  In a way, their hatred parallels that of another native of the Negative Energy Plane-the nightshade. Yet despite their similar goals, the sceaduinars see nightshades as just another corruption of life worthy of destruction-even though very few sceaduinars are powerful enough to directly oppose one of these deadly undead. Sceaduinars are quite intelligent, yet they have no real society to speak of. When they gather together, it is always to form a larger band to strike against a particularly dangerous foe.

---

# Sceaduinar
This gargoyle-like creature has long spiky legs and a bat-like head—its body seems to be made of living, dark purple crystal.
**Source** Bestiary 2 pg. 239
**XP** 3,200

NE Medium outsider (extraplanar)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Lifesense|lifesense]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +17

##### Defense

**AC** 20, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+5 Dex, +1 _[[feats/Dodge|dodge]]_, +4 natural)
**hp** 85 (9d10+36)
**Fort** +10, **Ref** +11, **Will** +5
**Defensive Abilities** entropic flesh, _[[universal monster rules/Negative Energy Affinity|negative energy affinity]]_, void child; **DR** 10/adamantine or good; **Immune** cold, death effects, disease, _[[universal monster rules/Energy Drain|energy drain]]_, poison; **Resist** acid 10, electricity 10, sonic 10; **SR** 18

##### Offense
**Speed** 40 ft., fly 90 ft. (good)
**Melee** bite +14 (1d6+3 plus 1d6 negative energy and _energy drain_), 2 wings +9 (1d6+1 plus 1d6 negative energy)
**Special Attacks** _energy drain_ (1 level, DC 17), entropic touch
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +12)
Constant—_[[spells/Entropic Shield|entropic shield]]_, _[[spells/Hide from Undead|hide from undead]]_ (DC 14)
At will—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Dimension Door|dimension door]]_ (self only), _[[spells/Dispel Magic|dispel magic]]_
3/day—_[[spells/Death Knell|death knell]]_ (DC 15), _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Enervation|enervation]]_, _[[spells/Inflict Serious Wounds|inflict serious wounds]]_ (DC 16), _[[spells/Silence|silence]]_
1/day—_[[spells/Antilife Shell|antilife shell]]_, greater teleport (self plus 50 lbs. of objects only), _[[spells/Harm|harm]]_ (DC 19), _[[spells/Slay Living|slay living]]_ (DC 18)

##### Statistics
**Str** 17, **Dex** 20, **Con** 18, **Int** 13, **Wis** 14, **Cha** 17
**Base Atk** +9; **CMB** +12; **CMD** 28
**Feats** _Dodge_, _[[feats/Mobility|Mobility]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Step Up|Step Up]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Escape Artist +17, Fly +9, Intimidate +15, Knowledge (nature) +13, Knowledge (planes) +17, Perception +17, Sense Motive +14, Stealth +25; **Racial Modifiers** +4 Knowledge (planes), +8 Stealth
**Languages** Aklo, Common

##### Ecology

**Environment** any (Negative Energy Plane)
**Organization** solitary or death squad (2–11)
**Treasure** standard

### Special Abilities

**Entropic Flesh (Ex)** Any creature that hits a _[[monsters/Sceaduinar|sceaduinar]]_ with a melee attack takes 1d6 points of negative energy damage. Attacking with a weapon that provides reach allows a creature to avoid taking this damage.

**Entropic Touch (Ex)** A _sceaduinar_’s _[[universal monster rules/Natural Attacks|natural attacks]]_ can strike _[[universal monster rules/Incorporeal|incorporeal]]_ creatures as if they were _[[items/Weapon Magic Abilities/Ghost Touch|ghost touch]]_ weapons. All of a _sceaduinar_’s _natural attacks_ deal +1d6 points of negative energy damage to the target. This energy does not _[[spells/Heal|heal]]_ creatures healed by inflict spells.

**Void Child (Ex)** Sceaduinars are immune to effects that target souls (such as _[[spells/Trap the Soul|trap the soul]]_) or require knowledge of a creature’s identity (such as _[[spells/Scrying|scrying]]_). When one is slain, it cannot be restored to life by magic save by a _[[spells/Miracle|miracle]]_ or _[[spells/Wish|wish]]_, or by divine intervention.

##### Description

Sceaduinars are strange creatures born of pure entropy, the antithesis of creation and life. In the cold heart of the Negative Energy Plane, the un-substance of that realm coalesces into snowflake-like crystals, and it is from these strange formations that sceaduinars arise, _[[items/Weapon Magic Abilities/Breaking|breaking]]_ free from their jagged “eggs” fully grown. They hate the living and the undead with equal passion, perhaps out of jealousy for those who have a _[[spells/Spark|spark]]_ of life (even if that _spark_ is provided by a corruption of life in the form of undeath), though they usually ignore creatures from the Outer Sphere. They believe their positive energy counterparts, the _[[monsters/Jyoti|jyoti]]_, long ago stole their ability to create, _breaking_ the parallel between the two energy planes and forcing these void-dwellers into an unwanted role of pure _[[spells/Destruction|destruction]]_.

In a way, their hatred parallels that of another native of the Negative Energy Plane—the nightshade. Yet despite their similar goals, the sceaduinars see nightshades as just another corruption of life worthy of _destruction_—even though very few sceaduinars are powerful enough to directly oppose one of these _[[items/Weapon Magic Abilities/Deadly|deadly]]_ undead. Sceaduinars are quite intelligent, yet they have no real society to speak of. When they gather together, it is always to form a larger band to strike against a particularly dangerous foe.
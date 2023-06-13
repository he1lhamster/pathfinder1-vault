---
cssclass: [monsters]
title1: Asura, Asurendra
desc_short: This four-armed humanoid horror is garbed in golden armor and surrounded
  by a nimbus of floating, glowing weaponry.
title2: Asurendra
CR: 20
sources:
- name: Bestiary 3
  page: 23
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 307200
alignment: LE
size: Huge
type: outsider
subtypes:
- asura
- evil
- extraplanar
- lawful
initiative:
  bonus: 12
senses:
  all-around vision: true
  darkvision: 60
  low-light vision: true
  scent: true
  true seeing: true
auras:
- name: dimensional lock
  radius: 20
  other:
  - enemies only
- name: elusive
  radius: 100
AC:
  AC: 35
  touch: 25
  flat_footed: 26
  components:
    deflection: 5
    dex: 8
    dodge: 1
    insight: 3
    natural: 10
    size: -2
HP:
  HP: 385
  long: 22d10+264
  regeneration: 10
  regeneration_weakness: good weapons, good spells
saves:
  fort: 25
  ref: 17
  will: 20
  other: +2 vs. enchantment spells
DR:
- amount: 15
  weakness: chaotic and good
immunities:
- curse effects
- disease
- flanking
- poison
- polymorph
resistances:
  acid: 10
  electricity: 10
SR: 31
speeds:
  base: 50
  climb: 50
  fly: 50
  fly_maneuverability: perfect
  swim: 50
attacks:
  melee:
  - - text: bite +33 (2d6+13 plus grab and poison)
      entries:
      - - damage: 2d6+13
        - effect: grab
        - effect: poison
      attack: bite
      bonus:
      - 33
    - text: 6 claws +33 (2d6+13 plus curse)
      entries:
      - - damage: 2d6+13
        - effect: curse
      count: 6
      attack: claws
      bonus:
      - 33
  special:
  - curse of false wisdom
  - spirit blades (+29, 3d6+7/19-20)
  - swallow whole (4d6+19 bludgeoning plus 4d8+12 acid damage, AC 15, 38 hp)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: dimensional lock
    source: default
    freq: Constant
    other: enemies only
  - name: freedom of movement
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: death knell
    source: default
    freq: At will
    DC: 22
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater scrying
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: quickened baleful polymorph
    source: default
    freq: 3/day
    DC: 25
  - name: quickened blade barrier
    source: default
    freq: 3/day
    DC: 26
  - name: blasphemy
    source: default
    freq: 3/day
    DC: 27
  - name: quickened death knell
    source: default
    freq: 3/day
    DC: 22
  - name: deeper darkness
    source: default
    freq: 3/day
  - name: demand
    source: default
    freq: 3/day
    DC: 28
  - name: power word stun
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 9
    summons:
    - name: any 1 CR 19
    - name: lower asura
      chance: 100%
  - name: time stop
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 20
    concentration: 30
ability_scores:
  STR: 36
  DEX: 26
  CON: 34
  INT: 25
  WIS: 25
  CHA: 31
BAB: 22
CMB: 37
CMB_other: +41 grapple
CMD: 64
feats:
- name: Awesome Blow
- name: Cleave
- is_bonus: true
  name: Combat Reflexes
- name: Critical Focus
- is_bonus: true
  name: Deflect Arrows
- is_bonus: true
  name: Dodge
- name: Great Cleave
- name: Improved Bull Rush
- name: Improved Initiative
- name: Lightning Reflexes
- is_bonus: true
  name: Mobility
- name: Power Attack
- name: Quicken Spell-Like Ability (baleful polymorph)
- name: Quicken Spell-Like Ability (blade barrier)
- name: Quicken Spell-Like Ability (death knell)
- is_bonus: true
  name: Snatch Arrows
- is_bonus: true
  name: Spring Attack
skills:
  Acrobatics: 31
    when jumping: 39
  Bluff: 33
  Climb: 21
  Diplomacy: 30
  Escape Artist: 14
  Fly: 35
  Intimidate: 33
  Knowledge (arcana): 27
  Knowledge (history): 13
  Knowledge (planes): 30
  Knowledge (religion): 27
  Perception: 34
  Perform (dance): 33
  Sense Motive: 30
  Spellcraft: 27
  Stealth: 23
  Swim: 21
  Use Magic Device: 30
  _racial_mods:
    Escape Artist:
      _: 6
    Perception:
      _: 4
languages:
- Common
- Infernal
- tongues
- telepathy 100 ft.
ecology:
  environment: any (Hell)
  organization: solitary or pair
  treasure_type: double
special_abilities:
  Curse of False Wisdom (Su): Claw-contact; save Will DC 31; frequency 1 day; effect
    1d6 Wis drain.
  Poison (Ex): Bite-injury; save Fort DC 33; frequency 1/round for 6 rounds; effect
    1d6 Con; cure 2 consecutive saves.
  Spirit Blades (Su): As a swift action, an asurendra can call forth up to six longsword-shaped
    force effects that float near the asurendra until directed. The asurendra can
    use a standard action to direct one blade to attack a target up to a distance
    of 50 feet away, or use a full-attack action to cause all six blades to attack
    up to six different targets up to a distance of 50 feet away, each to a different
    location if desired. Once an asurendra directs a spirit blade to attack a foe,
    the blade continues to make a single attack against that foe each round on the
    asurendra's turn until directed otherwise by the asurendra and as long as the
    foe remains within 50 feet of the asurendra. As a move action, the asurendra can
    direct all currently attacking blades to switch targets to new foes within 50
    feet. These weapons attack using the asurendra's base attack bonus modified by
    its Wisdom modifier (+29 for most asurendras), and deal 3d6 points of damage plus
    an amount of force damage equal to the asurendra's Wisdom modifier (3d6+7 for
    most asurendras). Physical attacks do no affect these blades, but disintegrate,
    a sphere of annihilation, or a rod of cancellation (touch AC 25) causes them to
    vanish. If a spirit blade's target dies or moves beyond a 50-foot range and the
    asurendra does not retarget that blade by the end of its turn, the blade vanishes.
    Likewise, any blades that are not within 50 feet of the asurendra at the end of
    its turn also vanish.
desc_long: |-
  With the notable exception of the unique asura ranas, asurendras are the mightiest of their kind. Although few asurendras possess anything resembling an extended realm, in Hell or elsewhere, these asuras are the “wise ones” of asura kind. Most dwell within shrinelike fortresses in which they can practice their ruinous mysticism and command lesser asuras who seek their teachings. To most asuras, an asurendra's order is something akin to a deific edict.

  Each asurendra is a humanoid creature of immense proportions. Their exact appearance varies just as the appearances of humanoids vary, but all asurendras have six arms and multiple eyes and heads. An asurendra's body is an example of physical perfection, athletically and gracefully built, but its face has monstrous or inhuman features, such as tusks or bizarrely placed features. Most asurendras are 19 feet tall and weigh 8,000 pounds.

  Few asurendras were born to their might-they achieve their power only over the course of countless lifetimes spent as lesser asuras. Throughout each incarnation, these tenacious asuras sought unity with some concept of destruction. Eventually, through dark meditation and vile action, the asuras ascended to a state of being united with some aspect of unmaking. They also gained power over their own being and slowly reshaped themselves into a vision of their perfect selves, instruments of annihilation ideally suited to fell gods and their divine works.

  In battle, an asurendra does its best to destroy all enemies, taking a moment to ensure death when any foe falls. Asurendras enjoy eating the bodies of fallen foes, and some can even use the flesh and bone of those they consume to create new asuras to serve them.

---

# Asura, Asurendra
This four-armed humanoid horror is garbed in golden armor and surrounded by a nimbus of floating, glowing weaponry.
**Source** Bestiary 3 pg. 23
**XP** 307,200

LE Huge outsider (asura, evil, extraplanar, lawful)
**Init** +12; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_, _[[spells/True Seeing|true seeing]]_; Perception +34
**Aura** _[[spells/Dimensional Lock|dimensional lock]]_ (20 ft., enemies only), elusive (100 ft.)

##### Defense

**AC** 35, touch 25, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+5 deflection, +8 Dex, +1 _[[feats/Dodge|dodge]]_, +3 insight, +10 natural, –2 size)
**hp** 385 (22d10+264); _[[universal monster rules/Regeneration|regeneration]]_ 10 (good weapons, good spells)
**Fort** +25, **Ref** +17, **Will** +20; +2 vs. enchantment spells,
**DR** 15/chaotic and good; **Immune** curse effects, disease, flanking, poison, _[[spells/Polymorph|polymorph]]_; **Resist** acid 10, electricity 10; **SR** 31

##### Offense
**Speed** 50 ft., _[[universal monster rules/Climb|climb]]_ 50 ft., fly 50 ft. (perfect), swim 50 ft.
**Melee** bite +33 (2d6+13 plus _[[universal monster rules/Grab|grab]]_ and poison), 6 claws +33 (2d6+13 plus curse)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** curse of false wisdom, spirit blades (+29, 3d6+7/19–20), _[[universal monster rules/Swallow Whole|swallow whole]]_ (4d6+19 bludgeoning plus 4d8+12 acid damage, AC 15, 38 hp)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +30)
Constant—_dimensional lock_ (enemies only), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Tongues|tongues]]_, _true seeing_
At will—_[[spells/Death Knell|death knell]]_ (DC 22), greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ _[[spells/Scrying, Greater|scrying, greater]]_ teleport (self plus 50 lbs. of objects only)
3/day—quickened _[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 25), quickened _[[spells/Blade Barrier|blade barrier]]_ (DC 26), _[[spells/Blasphemy|blasphemy]]_ (DC 27), quickened _death knell_ (DC 22), _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Demand|demand]]_ (DC 28)
1/day—_[[spells/Power Word Stun|power word stun]]_, _[[universal monster rules/Summon|summon]]_ (level 9, any 1 CR 19 or lower asura 100%), _[[spells/Time Stop|time stop]]_

##### Statistics
**Str** 36, **Dex** 26, **Con** 34, **Int** 25, **Wis** 25, **Cha** 31
**Base Atk** +22; **CMB** +37 (+41 grapple); **CMD** 64
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Deflect Arrows|Deflect Arrows]]_, _Dodge_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_baleful polymorph_, _blade barrier_, _death knell_), _[[feats/Snatch Arrows|Snatch Arrows]]_, _[[feats/Spring Attack|Spring Attack]]_
**Skills** Acrobatics +31 (+39 when jumping), Bluff +33, _Climb_ +21, Diplomacy +30, Escape Artist +14, Fly +35, Intimidate +33, Knowledge (arcana) +27, Knowledge (history) +13, Knowledge (planes) +30, Knowledge (religion) +27, Perception +34, Perform (dance) +33, Sense Motive +30, Spellcraft +27, Stealth +23, Swim +21, Use Magic Device +30; **Racial Modifiers** +6 Escape Artist, +4 Perception
**Languages** Common, Infernal; _tongues_, _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Hell)
**Organization** solitary or pair
**Treasure** double

### Special Abilities

**Curse of False Wisdom (Su)** Claw—contact; save Will DC 31; frequency 1 day; effect 1d6 Wis drain.

**Poison (Ex)** Bite—injury; save Fort DC 33; frequency 1/round for 6 rounds; effect 1d6 Con; cure 2 consecutive saves.
**Spirit Blades (Su)** As a swift action, an asurendra can call forth up to six longsword-shaped force effects that float near the asurendra until directed. The asurendra can use a standard action to direct one blade to attack a target up to a distance of 50 feet away, or use a full-attack action to cause all six blades to attack up to six different targets up to a distance of 50 feet away, each to a different location if desired. Once an asurendra directs a _[[items/Weapon/Spirit Blade|spirit blade]]_ to attack a foe, the blade continues to make a single attack against that foe each round on the asurendra’s turn until directed otherwise by the asurendra and as long as the foe remains within 50 feet of the asurendra. As a move action, the asurendra can direct all currently attacking blades to switch targets to new foes within 50 feet. These weapons attack using the asurendra’s base attack bonus modified by its Wisdom modifier (+29 for most asurendras), and deal 3d6 points of damage plus an amount of force damage equal to the asurendra’s Wisdom modifier (3d6+7 for most asurendras). Physical attacks do no affect these blades, but _[[spells/Disintegrate|disintegrate]]_, a _[[items/Wondrous Item/Sphere of Annihilation|sphere of annihilation]]_, or a _[[items/Rod/Rod of Cancellation|rod of cancellation]]_ (touch AC 25) causes them to _[[spells/Vanish|vanish]]_. If a _spirit blade_’s target dies or moves beyond a 50-foot range and the asurendra does not retarget that blade by the end of its turn, the blade vanishes. Likewise, any blades that are not within 50 feet of the asurendra at the end of its turn also _vanish_.

##### Description

With the notable exception of the unique asura ranas, asurendras are the mightiest of their kind. Although few asurendras possess anything resembling an extended realm, in Hell or elsewhere, these asuras are the “wise ones” of asura kind. Most dwell within shrinelike fortresses in which they can practice their ruinous mysticism and _[[spells/Command|command]]_ lesser asuras who seek their teachings. To most asuras, an asurendra’s order is something akin to a deific edict.

Each asurendra is a humanoid creature of immense proportions. Their exact appearance varies just as the appearances of humanoids vary, but all asurendras have six arms and multiple eyes and heads. An asurendra’s body is an example of physical perfection, athletically and gracefully built, but its face has monstrous or inhuman features, such as tusks or bizarrely placed features. Most asurendras are 19 feet tall and weigh 8,000 pounds.

Few asurendras were born to their might—they achieve their power only over the course of countless lifetimes spent as lesser asuras. Throughout each incarnation, these tenacious asuras sought unity with some concept of _[[spells/Destruction|destruction]]_. Eventually, through dark meditation and vile action, the asuras ascended to a state of being united with some aspect of unmaking. They also gained power over their own being and slowly reshaped themselves into a _[[spells/Vision|vision]]_ of their perfect selves, instruments of annihilation ideally suited to fell gods and their divine works.

In battle, an asurendra does its best to destroy all enemies, taking a moment to ensure death when any foe falls. Asurendras enjoy eating the bodies of _[[monsters/Fallen|fallen]]_ foes, and some can even use the flesh and bone of those they consume to create new asuras to serve them.
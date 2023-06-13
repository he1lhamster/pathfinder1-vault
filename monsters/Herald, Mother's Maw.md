---
cssclass: [monsters]
title1: Herald, Mother's Maw
desc_short: This skull is as large as an ogre and surrounded by buzzing flies. Its
  bat wings are too small to actually carry it, yet it moves through the air as easily
  as a bird. It is surrounded by the stink of rotting meat, spice, and perfume.
title2: Mother's Maw
CR: 15
sources:
- name: 'Pathfinder #47: Ashes at Dawn'
  page: 82
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderAdventurePath/carrionCrown/v5748btpy8lv2
XP: 51200
alignment: NE
size: Large
type: undead
subtypes:
- evil
- extraplanar
initiative:
  bonus: 11
senses:
  darkvision: 60
  lifesense: true
  scent: true
auras:
- name: desecrate
AC:
  AC: 30
  touch: 16
  flat_footed: 23
  components:
    dex: 7
    natural: 14
    size: -1
HP:
  HP: 230
  long: 20d8+140
  other: fast healing 5 or 20 (see Devour Soul)
saves:
  fort: 13
  ref: 16
  will: 18
defensive_abilities:
- channel resistance +4
DR:
- amount: 15
  weakness: bludgeoning and good
immunities:
- cold
- electricity
- undead traits
resistances:
  fire: 30
SR: 26
speeds:
  base: 10
  fly: 40
  fly_maneuverability: average
attacks:
  melee:
  - - text: bite +26 (5d6+17/19-20 plus 1d10 bleed, 1d6 Con drain, grab, and mummy
        rot [DC 26])
      entries:
      - - damage: 5d6+17
          crit_range: 19-20
        - damage: 1d10
          type: bleed
        - damage: 1d6
          type: Con drain
        - effect: grab
        - effect: mummy rot [DC 26]
      attack: bite
      bonus:
      - 26
  special:
  - breath weapon (60-ft. cone, 15d6 negative energy, Reflex DC 26 half, usable every
    1d4 rounds)
  - channel negative energy 9/day (DC 19, 6d6)
  - devour soul
  - swallow whole (special acid damage, AC 17, 20 hp)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: desecrate
    source: default
    freq: Constant
  - name: contagion
    source: default
    freq: At will
    DC: 19
  - name: dimension door
    source: default
    freq: At will
  - name: ghoul hunger
    source: default
    freq: At will
    DC: 18
  - name: inflict critical wounds
    source: default
    freq: At will
    DC: 20
  - name: animate dead
    source: default
    freq: 1/day
  - name: create undead
    source: default
    freq: 1/day
  - name: eyebite
    source: default
    freq: 1/day
    DC: 22
  - name: plane shift
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 12
    concentration: 18
ability_scores:
  STR: 33
  DEX: 25
  CON:
  INT: 21
  WIS: 20
  CHA: 22
BAB: 15
CMB: 27
CMB_other: +31 grapple
CMD: 44
CMD_other: can't be tripped
feats:
- name: Cleave
- is_bonus: true
  name: Command Undead
- name: Critical Focus
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Iron Will
- name: Improved Lightning Reflexes
- name: Lightning Reflexes
- name: Power Attack
- name: Staggering Critical
- is_bonus: true
  name: Stunning Critical
- name: Toughness
skills:
  Acrobatics: 27
    jump: 19
  Fly: 28
  Intimidate: 29
  Knowledge (planes): 25
  Knowledge (religion): 28
  Perception: 28
  Profession (cook): 25
  Sense Motive: 28
  Stealth: 26
special_qualities:
- deathless
- true herald
special_abilities:
  Constitution Drain (Su): Creatures that are hit by the Maw's bite must succeed at
    a DC 26 Fortitude save or take 1d6 points of Constitution drain. On each successful
    attack, the herald gains 5 temporary hit points. The save DC is Charisma-based.
  Create Spawn (Su): Any creature slain by the Maw (including those that die from
    any of its special attacks or disease) rises 1 round later as a bloody skeleton
    loyal to the herald.
  Deathless (Su): The Maw is destroyed when reduced to 0 hit points, but it returns
    to unlife 1 hour later at 1 hit point, allowing its fast healing to resume healing
    it thereafter. The Maw can be permanently destroyed if it is destroyed by positive
    energy, if it is reduced to 0 hit points in the area of a bless or hallow spell,
    or if its remains are sprinkled with 20 vials of holy water.
  Desecrate (Sp): The bonuses from the Maw's constant desecrate spell-like ability
    (always centered on it) are calculated into the stats above.
  Devour Soul (Su): By using its swallow whole ability, the herald can deal 12d6+18
    points of damage to a swallowed creature as if using a slay living spell. A DC
    21 Fortitude save reduces this damage to 3d6+18. A swallowed creature must make
    this save every round on the herald's turn. The soul of a creature slain by this
    attack becomes trapped within the herald's skull (the creature's body is regurgitated
    immediately as a mangled wreck of shattered bone and chewed meat). The creature
    cannot be brought back to life until the herald's destruction (or a spell deflection-see
    below) releases its soul. The Maw can hold only one soul at a time. The trapped
    essence provides the Maw with fast healing 20, lasting 1 round for every Hit Die
    of the devoured soul. The trapped soul gains one permanent negative level for
    every round it spends within the Maw-these negative levels remain if the creature
    is brought back to life (but they do not stack with any negative levels imparted
    by being brought back to life). A soul that is completely consumed may only be
    restored to life by a miracle or wish spell. The save DC is Charisma-based.
  Spell Deflection (Su): 'If any of the following spells is cast at the Maw and overcomes
    its spell resistance, it instead affects the devoured soul: banishment, chaos
    hammer, confusion, crushing despair, detect thoughts, dispel evil, dominate person,
    fear, geas/quest, holy word, hypnotism, imprisonment, magic jar, maze, suggestion,
    trap the soul, or any form of charm or compulsion. While none of these effects
    harms the soul, the caster makes a DC 25 caster level check when a spell is deflected-success
    indicates that the trapped soul is released from its prison and the creature whose
    body it belonged to can now be restored to life as normal.'
  Swallow Whole (Ex): If a creature cuts its way out of the Maw after being swallowed,
    the Maw can use swallow whole once its fast healing repairs the damage caused
    by its prey cutting itself free.
  True Herald: Despite its type and Hit Dice, Mother's Maw is the herald of Urgathoa.
    Despite its type and Hit Dice, it can be conjured using the spell greater planar
    binding.
  Vomit Swarm (Su): Once per round as a free action, the Maw can vomit forth a swarm
    of maggots (use the statistics for army ants on page 16 of the Pathfinder RPG
    Bestiary) into a square adjacent to it, after which the swarm moves in a direction
    of the Maw's choosing. These swarms persist for 10 rounds.
desc_long: |-
  The Mother's Maw is the herald of Urgathoa. A disgusting undead creature that comes to the mortal realm at the command of the Pallid Princess, it is an unsubtle thing of ravenous hunger, with little purpose but to kill, eat, and animate corpses as undead. Though it is as brilliant as a lich, its only interests are in satisfy its cravings for sensation.

  The Maw has little interest in the desires of mortals (or of undead in the mortal world) except for how they intersect with Urgathoa's orders. If it is necessary to eat a hundred members of her cult, or to drive an entire city of ghouls into a lava pit, the Maw does it. It can speak but finds little worth talking about, so many assume it is as mindless as an animated skeleton. However, when not on a mission of death, disease, or gluttony, it is a font of knowledge about food, wine, exotic scents, and other strange experiences only an undead creature can understand, and is quite willing to speak on these matters to an interested party-assuming the sight of the enormous talking, winged skull isn't a distraction to listeners.

  Although the Maw normally appears as a bare skull, it sometimes covers itself with its swarms. Whether this is out of a morbid sense of humor or an attempt to remember an old sensation from its life is unknown. It has confirmed that it was once a devourer, and before that a living creature, but it does not give further details.

---

# Herald, Mother's Maw
This skull is as large as an _[[monsters/Ogre|ogre]]_ and surrounded by buzzing flies. Its bat wings are too small to actually carry it, yet it moves through the air as easily as a bird. It is surrounded by the stink of rotting meat, spice, and perfume.
**Source** Pathfinder #47: Ashes at Dawn pg. 82
**XP** 51,200

NE Large undead (evil, extraplanar)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Lifesense|lifesense]]_, _[[universal monster rules/Scent|scent]]_; Perception +28
**Aura** _[[spells/Desecrate|desecrate]]_

##### Defense

**AC** 30, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+7 Dex, +14 natural, -1 size)
**hp** 230 (20d8+140); _[[universal monster rules/Fast Healing|fast healing]]_ 5 or 20 (see Devour Soul)
**Fort** +13, **Ref** +16, **Will** +18
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4; **DR** 15/bludgeoning and good; **Immune** cold, electricity, _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** fire 30; **SR** 26

##### Offense
**Speed** 10 ft., fly 40 ft. (average)
**Melee** bite +26 (5d6+17/19-20 plus 1d10 _[[universal monster rules/Bleed|bleed]]_, 1d6 Con drain, _[[universal monster rules/Grab|grab]]_, and _[[curses/Mummy rot|mummy rot]]_ [DC 26])
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, 15d6 negative energy, Reflex DC 26 half, usable every 1d4 rounds), channel negative energy 9/day (DC 19, 6d6), devour soul, _[[universal monster rules/Swallow Whole|swallow whole]]_ (special acid damage, AC 17, 20 hp)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +18)
Constant - _desecrate_
At will - _[[spells/Contagion|contagion]]_ (DC 19), _[[spells/Dimension Door|dimension door]]_, _[[spells/Ghoul Hunger|ghoul hunger]]_ (DC 18), _[[spells/Inflict Critical Wounds|inflict critical wounds]]_ (DC 20)
1/day - _[[spells/Animate Dead|animate dead]]_, _[[spells/Create Undead|create undead]]_, _[[spells/Eyebite|eyebite]]_ (DC 22), _[[spells/Plane Shift|plane shift]]_

##### Statistics
**Str** 33, **Dex** 25, **Con** —, **Int** 21, **Wis** 20, **Cha** 22
**Base Atk** +15; **CMB** +27 (+31 grapple); **CMD** 44 (can't be tripped)
**Feats** _[[feats/Cleave|Cleave]]_, _[[spells/Command Undead|Command Undead]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Lightning Reflexes|Improved Lightning Reflexes]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Stunning Critical|Stunning Critical]]_, _[[feats/Toughness|Toughness]]_
**Skills** Acrobatics +27 (+19 _[[spells/Jump|jump]]_), Fly +28, Intimidate +29, Knowledge (planes) +25, Knowledge (religion) +28, Perception +28, Profession (cook) +25, Sense Motive +28, Stealth +26
**SQ** _[[spells/Deathless|deathless]]_, true herald

### Special Abilities

**Constitution Drain (Su)** Creatures that are hit by the Maw’s bite must succeed at a DC 26 Fortitude save or take 1d6 points of Constitution drain. On each successful attack, the herald gains 5 temporary hit points. The save DC is Charisma-based.

**Create Spawn (Su)** Any creature slain by the Maw (including those that die from any of its special attacks or disease) rises 1 round later as a bloody skeleton loyal to the herald.

**_Deathless_ (Su)** The Maw is destroyed when reduced to 0 hit points, but it returns to unlife 1 hour later at 1 hit point, allowing its _fast healing_ to resume healing it thereafter. The Maw can be permanently destroyed if it is destroyed by positive energy, if it is reduced to 0 hit points in the area of a _[[spells/Bless|bless]]_ or _[[spells/Hallow|hallow]]_ spell, or if its remains are sprinkled with 20 vials of _[[items/Mundane/Holy water|holy water]]_.

**_Desecrate_ (Sp)** The bonuses from the Maw’s constant _desecrate_ spell-like ability (always centered on it) are calculated into the stats above.

**Devour Soul (Su)** By using its _swallow whole_ ability, the herald can deal 12d6+18 points of damage to a swallowed creature as if using a _[[spells/Slay Living|slay living]]_ spell. A DC 21 Fortitude save reduces this damage to 3d6+18. A swallowed creature must make this save every round on the herald’s turn. The soul of a creature slain by this attack becomes trapped within the herald’s skull (the creature’s body is regurgitated immediately as a mangled wreck of shattered bone and chewed meat). The creature cannot be brought back to life until the herald’s _[[spells/Destruction|destruction]]_ (or a spell deflection—see below) releases its soul. The Maw can hold only one soul at a time. The trapped essence provides the Maw with _fast healing_ 20, lasting 1 round for every Hit Die of the devoured soul. The trapped soul gains one permanent negative level for every round it spends within the Maw—these negative levels remain if the creature is brought back to life (but they do not stack with any negative levels imparted by being brought back to life). A soul that is completely consumed may only be restored to life by a _[[spells/Miracle|miracle]]_ or _[[spells/Wish|wish]]_ spell. The save DC is Charisma-based.
**Spell _Deflection_ (Su)** If any of the following spells is cast at the Maw and overcomes its _[[universal monster rules/Spell Resistance|spell resistance]]_, it instead affects the devoured soul: _[[spells/Banishment|banishment]]_, _[[spells/Chaos Hammer|chaos hammer]]_, _[[spells/Confusion|confusion]]_, _[[spells/Crushing Despair|crushing despair]]_, _[[spells/Detect Thoughts|detect thoughts]]_, _[[spells/Dispel Evil|dispel evil]]_, _[[spells/Dominate Person|dominate person]]_, _[[universal monster rules/Fear|fear]]_, geas/quest, _[[spells/Holy Word|holy word]]_, _[[spells/Hypnotism|hypnotism]]_, _[[spells/Imprisonment|imprisonment]]_, _[[spells/Magic Jar|magic jar]]_, _[[spells/Maze|maze]]_, _[[spells/Suggestion|suggestion]]_, _[[spells/Trap the Soul|trap the soul]]_, or any form of charm or compulsion. While none of these effects harms the soul, the caster makes a DC 25 caster level check when a spell is deflected—success indicates that the trapped soul is released from its prison and the creature whose body it belonged to can now be restored to life as normal.
**_Swallow Whole_ (Ex)** If a creature cuts its way out of the Maw after being swallowed, the Maw can use _swallow whole_ once its _fast healing_ repairs the damage caused by its prey cutting itself free.

**True Herald** Despite its type and Hit Dice, Mother’s Maw is the herald of Urgathoa. Despite its type and Hit Dice, it can be conjured using the spell greater _[[spells/Planar Binding|planar binding]]_.

**_[[spells/Vomit Swarm|Vomit Swarm]]_ (Su)** Once per round as a free action, the Maw can vomit forth a swarm of maggots (use the statistics for army ants on page 16 of the Pathfinder RPG Bestiary) into a square adjacent to it, after which the swarm moves in a direction of the Maw’s choosing. These swarms persist for 10 rounds.

##### Description

The Mother’s Maw is the herald of Urgathoa. A disgusting undead creature that comes to the mortal realm at the _[[spells/Command|command]]_ of the Pallid _[[npcs/Princess|Princess]]_, it is an unsubtle thing of _[[curses/Ravenous|ravenous]]_ hunger, with little purpose but to kill, eat, and animate corpses as undead. Though it is as brilliant as a _[[monsters/Lich|lich]]_, its only interests are in satisfy its cravings for sensation.

The Maw has little interest in the desires of mortals (or of undead in the mortal world) except for how they intersect with Urgathoa’s orders. If it is necessary to eat a hundred members of her cult, or to drive an entire city of ghouls into a lava pit, the Maw does it. It can speak but finds little worth talking about, so many assume it is as mindless as an _[[items/Armor Magic Abilities/Animated|animated]]_ skeleton. However, when not on a mission of death, disease, or gluttony, it is a font of knowledge about food, wine, exotic scents, and other strange experiences only an undead creature can understand, and is quite willing to speak on these matters to an interested party—assuming the sight of the enormous talking, winged skull isn’t a _[[universal monster rules/Distraction|distraction]]_ to listeners.

Although the Maw normally appears as a bare skull, it sometimes covers itself with its swarms. Whether this is out of a morbid sense of humor or an attempt to remember an old sensation from its life is _[[monsters/Unknown|unknown]]_. It has confirmed that it was once a _[[monsters/Devourer|devourer]]_, and before that a living creature, but it does not give further details.
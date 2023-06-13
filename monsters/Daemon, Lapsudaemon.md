---
cssclass: [monsters]
title1: Daemon, Lapsudaemon
desc_short: This grotesque and malevolent creature appears to be a crushed ball of
  broken humanoid body parts spraying blood.
title2: Lapsudaemon
CR: 14
sources:
- name: 'Pathfinder #106: For Queen and Empire'
  page: 88
  link: http://paizo.com/products/btpy9l3b?Pathfinder-Adventure-Path-106-For-Queen-Empire
XP: 38400
alignment: NE
size: Medium
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 10
senses:
  blindsense: 200
  darkvision: 60
auras:
- name: frightful presence
  radius: 30
  DC: 22
AC:
  AC: 29
  touch: 24
  flat_footed: 18
  components:
    deflection: 3
    dex: 10
    dodge: 1
    natural: 5
HP:
  HP: 199
  long: 19d10+95
saves:
  fort: 11
  ref: 21
  will: 15
defensive_abilities:
- amorphous
- vertigo's grace
DR:
- amount: 10
  weakness: good
immunities:
- acid
- bludgeoning
- death effects
- disease
- poison
resistances:
  cold: 10
  electricity: 10
  fire: 10
SR: 25
speeds:
  fly: 200
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: slam +23 (2d6+6 plus momentum/19-20 and grab)
      entries:
      - - damage: 2d6+6
        - effect: momentum/19-20
        - effect: grab
      attack: slam
      bonus:
      - 23
  special:
  - momentum
  - must come down (DC 22)
spell_like_abilities:
  entries:
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 pounds only
  - name: quickened gust of wind
    source: default
    freq: 3/day
    DC: 15
  - name: reverse gravity
    source: default
    freq: 3/day
  - superscripts:
    - UM
    name: fickle winds
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 7
    summons:
    - name: 'suspiridaemons [Pathfinder Campaign Setting: Horsemen of the Apocalypse,
        Book of the Damned, Vol. 3 56]'
      amount: 1d3
      chance: 80%
  sources:
  - name: default
    CL: 14
    concentration: 16
ability_scores:
  STR: 18
  DEX: 31
  CON: 21
  INT: 13
  WIS: 18
  CHA: 16
BAB: 19
CMB: 29
CMB_other: +31 bull rush or trip, +33 grapple
CMD: 43
CMD_other: 45 vs. bull rush, can't be tripped
feats:
- name: Acrobatic
- name: Agile Maneuvers
- name: Combat Expertise
- name: Dodge
- name: Improved Bull Rush
- name: Improved Critical (slam)
- name: Improved Trip
- name: Mobility
- name: Power Attack
- name: Quicken Spell-Like Ability (gust of wind)
skills:
  Acrobatics: 32
  Bluff: 21
  Escape Artist: 28
  Fly: 35
  Knowledge (geography): 14
  Knowledge (local): 14
  Knowledge (planes): 14
  Perception: 26
  Sense Motive: 26
  Stealth: 23
    _other: see below
languages:
- Abyssal
- Common
- Draconic
- telepathy 200 ft.
special_qualities:
- constant motion
ecology:
  environment: any (Abaddon)
  organization: solitary or storm (2-11)
  treasure_type: standard
special_abilities:
  Constant Motion (Su): |-
    Lapsudaemons never cease their falling motion. They must move their full movement speed in straight lines every round, making their slam attacks and grabs without stopping. A lapsudaemon doesn't lose altitude or speed for aerial maneuvers and makes no Fly checks when changing directions. It “falls” vertically, horizontally, or diagonally and attacks any creature in its way, regardless of the number of creatures in its path. It can change directions each round to maximize the number of creatures it can slam, moving through other creatures' spaces without the need for an Acrobatics check regardless of their size, but it still provokes attacks of opportunity, and it can only attack a particular creature once per round. It can fall at its full speed while grappling a single creature without needing to succeed at a check to do so; while grappling, it can make slam attacks only against the grappled creature, and it can't use its grab ability.

     Lapsudaemons are immune to effects that change their movement speed or alter their flight ability, even if the effect would be harmless or beneficial. Lapsudaemons don't take damage from falling or from bludgeoning attacks. The only exception is that any lapsudaemon somehow prevented from moving takes 1d6 points of damage each round for every 30 feet it doesn't move. So great is the creature's supernatural propulsion that forcing the lapsudaemon to remain still eventually tears it apart.

     Because lapsudaemons shout in horror as they fall, if a creature can hear, it can always notice the sound of a lapsudaemon's presence with a Perception check DC of -10, regardless of the daemon's Stealth.
  Momentum (Ex): When a lapsudaemon makes a slam attack while moving into a creature's
    square, the attack deals an additional 1d6 points of damage for every 10 feet
    that the lapsudaemon moved since the last time it made a slam attack or struck
    a surface, to a maximum of 20d6. This damage isn't multiplied on a critical hit.
  Must Come Down (Su): Any flying creature struck by a lapsudaemon must succeed at
    a DC 22 Will save or lose its ability to fly for 1 round. Such a creature falls
    until it regains the ability to fly or it hits the ground, whichever comes first.
    This affects both natural and magical flight. This doesn't dispel magical flight
    effects, but instead suppresses them (functioning similar to antimagic field)
    for 1 round. When a lapsudaemon dies, it unleashes this ability a final time on
    all creatures within 30 feet. A creature falling for 1 round generally falls 200
    feet. The save DC is Charisma-based.
  Vertigo's Grace (Su): A lapsudaemon's constant motion protects it from attacks.
    It gains a deflection bonus to AC equal to its Charisma bonus.
desc_long: |-
  A mortal that dies hopelessly after a sudden fall may eventually serve the Four Horsemen as a powerful lapsudaemon. On the bleak plane of Abaddon, these awful creatures exist in a state of perpetual plummeting, never ceasing their movement. Even when addressed by ranking daemon lords, lapsudaemons never stop their falling motion or incessant screaming. Their lieges frequently must teleport to some great height and fall with them to maintain telepathic conversation. Lapsudaemons always shriek as they fall-a residual impulse taken from the last moment of their mortal lives. Loud cries and cold blasts of wind herald their approach as they teleport into combat mid-fall and continue their merciless assault.

  Lapsudaemons attack their victims by falling into them, whether they approach vertically or horizontally. They frequently employ spell-like abilities before attacking as many enemies as possible in melee, colliding for one mighty strike against each target until every foe is dead. When not outnumbered, they prefer to murder their nonflying targets by pushing them from ledges or carrying them to great heights before releasing them to their doom.

  A lapsudaemon appears as a crushed human-often an amalgamation of the parts of several victims of such terminal tumbles seamlessly fused together. Its limbs protrude at awkward angles and strike out as it collides with its enemies. A lapsudaemon is between 5 and 6 feet tall and weighs 150 pounds.

---

# Daemon, Lapsudaemon
This grotesque and _[[items/Armor Magic Abilities/Malevolent|malevolent]]_ creature appears to be a crushed ball of _[[conditions/Broken|broken]]_ humanoid body parts spraying blood.
**Source** Pathfinder #106: For Queen and Empire pg. 88
**XP** 38,400

NE Medium outsider (daemon, evil, extraplanar)
**Init** +10; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 200 ft., _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +26
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (30 ft., DC 22)

##### Defense

**AC** 29, touch 24, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+3 _[[spells/Deflection|deflection]]_, +10 Dex, +1 _[[feats/Dodge|dodge]]_, +5 natural)
**hp** 199 (19d10+95)
**Fort** +11, **Ref** +21, **Will** +15
**Defensive Abilities** _[[universal monster rules/Amorphous|amorphous]]_, vertigo’s _[[spells/Grace|grace]]_; **DR** 10/good; **Immune** acid, bludgeoning, death effects, disease, poison; **Resist** cold 10, electricity 10, fire 10; **SR** 25

##### Offense
**Speed** fly 200 ft. (perfect)
**Melee** slam +23 (2d6+6 plus momentum/19–20 and _[[universal monster rules/Grab|grab]]_)
**Special Attacks** momentum, must come down (DC 22)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +16)
At will—greater teleport (self plus 50 pounds only)
3/day—quickened _[[spells/Gust Of Wind|gust of wind]]_ (DC 15), _[[spells/Reverse Gravity|reverse gravity]]_
1/day—_[[spells/Fickle Winds|fickle winds]]_, _[[universal monster rules/Summon|summon]]_ (level 7, 1d3 suspiridaemons [Pathfinder Campaign Setting: Horsemen of the Apocalypse, _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_, Vol. 3 56] 80%)

##### Statistics
**Str** 18, **Dex** 31, **Con** 21, **Int** 13, **Wis** 18, **Cha** 16
**Base Atk** +19; **CMB** +29 (+31 bull rush or _[[universal monster rules/Trip|trip]]_, +33 grapple); **CMD** 43 (45 vs. bull rush, can’t be tripped)
**Feats** _[[feats/Acrobatic|Acrobatic]]_, _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _Dodge_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (slam), _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_gust of wind_)
**Skills** Acrobatics +32, Bluff +21, Escape Artist +28, Fly +35, Knowledge (geography) +14, Knowledge (local) +14, Knowledge (planes) +14, Perception +26, Sense Motive +26, Stealth +23 (see below)
**Languages** Abyssal, Common, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 200 ft.
**SQ** constant motion

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary or storm (2–11)
**Treasure** standard

### Special Abilities

**Constant Motion (Su)** Lapsudaemons never cease their falling motion. They must move their full movement speed in straight lines every round, making their slam attacks and grabs without stopping. A lapsudaemon doesn’t lose altitude or speed for aerial maneuvers and makes no Fly checks when changing directions. It “falls” vertically, horizontally, or diagonally and attacks any creature in its way, regardless of the number of creatures in its path. It can change directions each round to maximize the number of creatures it can slam, moving through other creatures’ spaces without the need for an Acrobatics check regardless of their size, but it still provokes attacks of opportunity, and it can only attack a particular creature once per round. It can fall at its full speed while grappling a single creature without needing to succeed at a check to do so; while grappling, it can make slam attacks only against the _[[conditions/Grappled|grappled]]_ creature, and it can’t use its _grab_ ability.

Lapsudaemons are immune to effects that change their movement speed or alter their _[[universal monster rules/Flight|flight]]_ ability, even if the effect would be harmless or beneficial. Lapsudaemons don’t take damage from falling or from bludgeoning attacks. The only exception is that any lapsudaemon somehow prevented from moving takes 1d6 points of damage each round for every 30 feet it doesn’t move. So great is the creature’s supernatural propulsion that forcing the lapsudaemon to remain still eventually tears it apart.

Because lapsudaemons _[[spells/Shout|shout]]_ in horror as they fall, if a creature can hear, it can always notice the sound of a lapsudaemon’s presence with a Perception check DC of –10, regardless of the daemon’s Stealth.

**Momentum (Ex)** When a lapsudaemon makes a slam attack while moving into a creature’s square, the attack deals an additional 1d6 points of damage for every 10 feet that the lapsudaemon moved since the last time it made a slam attack or struck a surface, to a maximum of 20d6. This damage isn’t multiplied on a critical hit.

**Must Come Down (Su)** Any flying creature struck by a lapsudaemon must succeed at a DC 22 Will save or lose its ability to fly for 1 round. Such a creature falls until it regains the ability to fly or it hits the ground, whichever comes first. This affects both natural and magical _flight_. This doesn’t dispel magical _flight_ effects, but instead suppresses them (functioning similar to _[[spells/Antimagic Field|antimagic field]]_) for 1 round. When a lapsudaemon dies, it unleashes this ability a final time on all creatures within 30 feet. A creature falling for 1 round generally falls 200 feet. The save DC is Charisma-based.

**Vertigo’s _Grace_ (Su)** A lapsudaemon’s constant motion protects it from attacks. It gains a _deflection_ bonus to AC equal to its Charisma bonus.

##### Description

A mortal that dies hopelessly after a sudden fall may eventually serve the Four Horsemen as a powerful lapsudaemon. On the bleak plane of Abaddon, these awful creatures exist in a state of perpetual plummeting, never ceasing their movement. Even when addressed by ranking daemon lords, lapsudaemons never stop their falling motion or incessant screaming. Their lieges frequently must teleport to some great height and fall with them to maintain telepathic conversation. Lapsudaemons always shriek as they fall—a residual impulse taken from the last moment of their mortal lives. Loud cries and cold blasts of wind herald their approach as they teleport into combat mid-fall and continue their merciless assault.

Lapsudaemons attack their victims by falling into them, whether they approach vertically or horizontally. They frequently employ _spell-like abilities_ before attacking as many enemies as possible in melee, colliding for one mighty strike against each target until every foe is dead. When not outnumbered, they prefer to murder their nonflying targets by pushing them from ledges or carrying them to great heights before releasing them to their _[[spells/Doom|doom]]_.

A lapsudaemon appears as a crushed human—often an amalgamation of the parts of several victims of such terminal tumbles seamlessly fused together. Its limbs protrude at awkward angles and strike out as it collides with its enemies. A lapsudaemon is between 5 and 6 feet tall and weighs 150 pounds.
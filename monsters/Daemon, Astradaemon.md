---
cssclass: [monsters]
title1: Daemon, Astradaemon
desc_short: 'Vaguely humanoid in shape, this gaunt fiend has the face of a hideous
  fish and a body of lanky limbs and writhing tendrils. '
title2: Astradaemon
CR: 16
sources:
- name: Bestiary 2
  page: 63
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
- name: The Great Beyond - A Guide to the Multiverse
  page: 54
  link: http://paizo.com/store/byCompany/p/paizoPublishingLLC/pathfinder/campaignSetting/35E/v5748btpy87uz
XP: 76800
alignment: NE
size: Large
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 7
senses:
  darkvision: 60
  deathwatch: true
  true seeing: true
auras:
- name: soul siphon
  radius: 10
AC:
  AC: 29
  touch: 17
  flat_footed: 21
  components:
    dex: 7
    dodge: 1
    natural: 12
    size: -1
HP:
  HP: 212
  long: 17d10+119
saves:
  fort: 12
  ref: 17
  will: 14
defensive_abilities:
- displacement
DR:
- amount: 10
  weakness: good and silver
immunities:
- acid
- death effects
- disease
- poison
resistances:
  cold: 10
  electricity: 10
  fire: 10
SR: 27
speeds:
  base: 90
  fly: 90
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +23 (2d6+5 plus energy drain and grab)
      entries:
      - - damage: 2d6+5
        - effect: energy drain
        - effect: grab
      attack: bite
      bonus:
      - 23
    - text: 2 claws +23 (1d8+5 plus energy drain)
      entries:
      - - damage: 1d8+5
        - effect: energy drain
      count: 2
      attack: claws
      bonus:
      - 23
    - text: tail slap +18 (1d12+2 plus energy drain)
      entries:
      - - damage: 1d12+2
        - effect: energy drain
      attack: tail slap
      bonus:
      - 18
  special:
  - devour soul
  - energy drain (1 level, DC 25)
space: 10
reach: 10
reach_other: 15 ft. with tail
spell_like_abilities:
  entries:
  - name: deathwatch
    source: default
    freq: Constant
  - name: displacement
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: enervation
    source: default
    freq: At will
  - name: fear
    source: default
    freq: At will
    other: DC21
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: vampiric touch
    source: default
    freq: At will
  - name: locate creature
    source: default
    freq: 3/day
  - name: plane shift
    source: default
    freq: 3/day
    DC: 24
  - name: energy drain
    source: default
    freq: 1/day
    DC: 24
  - name: finger of death
    source: default
    freq: 1/day
    DC: 24
  - name: summon
    source: default
    freq: 1/day
    level: 6
    summons:
    - name: derghodaemons
      amount: 1d3
      chance: 50%
  sources:
  - name: default
    CL: 17
    concentration: 24
ability_scores:
  STR: 21
  DEX: 25
  CON: 24
  INT: 14
  WIS: 15
  CHA: 24
BAB: 17
CMB: 23
CMD: 41
feats:
- name: Combat Reflexes
- name: Dodge
- name: Flyby Attack
- name: Iron Will
- name: Mobility
- name: Nimble Moves
- name: Power Attack
- name: Spring Attack
- name: Weapon Finesse
skills:
  Acrobatics: 24
    jump: 48
  Escape Artist: 27
  Fly: 9
  Intimidate: 27
  Knowledge (planes): 22
  Perception: 22
  Sense Motive: 22
  Stealth: 23
  Survival: 22
languages:
- Abyssal
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Abaddon or Astral Plane)
  organization: solitary, pair, or pack (3-6)
  treasure_type: standard
special_abilities:
  Devour Soul (Su): As a standard action, an astradaemon that begins its turn with
    a grappled opponent can attempt to draw out and consume the soul of its victim,
    killing it instantly. This ability only works on living creatures, which may resist
    with a DC 25 Fortitude saving throw. The save is Constitution-based. For every
    5 HD of the slain creature, the daemon gains a +1 profane bonus on attacks, saving
    throws, and checks for 24 hours. This ability does not consume all of the soul,
    and pieces of it still exist after the daemon completes its feast (enough to be
    able to resurrect the slain victim normally).
  Soul Siphon (Su): If a Small or larger living creature dies within 10 feet of an
    astradaemon, the daemon gains 1d8 temporary hit points and a +2 bonus to Strength
    for 10 minutes. These bonuses stack with themselves. Incorporeal undead and living
    spirits traveling outside the body (such as a person using astral projection or
    magic jar) take 1d8 points of damage each round within the daemon's aura.
desc_long: Believed to be creations of the Four Horsemen, astradaemons live out their
  existence in search of souls to harvest. These deadly creatures are ravening planar
  predators, openly hunting throughout the void for souls on which to feed. These
  voracious creatures are the personifications of death resulting from negative energy
  or level drain. Their vile touch drains life force from their enemies, and even
  perishing near them sates their thirst for life and souls.

---

# Daemon, Astradaemon
Vaguely humanoid in shape, this gaunt fiend has the face of a hideous fish and a body of lanky limbs and writhing tendrils.

**Source** Bestiary 2 pg. 63, The Great Beyond - A Guide to the Multiverse pg. 54
**XP** 76,800

NE Large outsider (daemon, evil, extraplanar)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Deathwatch|deathwatch]]_, _[[spells/True Seeing|true seeing]]_; Perception +22
**Aura** soul siphon (10 ft.)

##### Defense

**AC** 29, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+7 Dex, +1 dodge, +12 natural, –1 size)
**hp** 212 (17d10+119)
**Fort** +12, **Ref** +17, **Will** +14
**Defensive Abilities** _[[spells/Displacement|displacement]]_; **DR** 10/good and silver; **Immune** acid, death effects, disease, poison; **Resist** cold 10, electricity 10, fire 10; **SR** 27

##### Offense
**Speed** 90 ft., fly 90 ft. (good)
**Melee** bite +23 (2d6+5 plus _[[universal monster rules/Energy Drain|energy drain]]_ and _[[universal monster rules/Grab|grab]]_), 2 claws +23 (1d8+5 plus _energy drain_), tail slap +18 (1d12+2 plus _energy drain_)
**Space** 10 ft., **Reach** 10 ft. (15 ft. with tail)
**Special Attacks** devour soul, _energy drain_ (1 level, DC 25)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +24)
Constant—_deathwatch_, _displacement_, _true seeing_
At will—_[[spells/Enervation|enervation]]_, _[[universal monster rules/Fear|fear]]_ (DC21), greater teleport (self plus 50 lbs. of objects only), _[[spells/Vampiric Touch|vampiric touch]]_
3/day—_[[spells/Locate Creature|locate creature]]_, _[[spells/Plane Shift|plane shift]]_ (DC 24)
1/day—_energy drain_ (DC 24), _[[spells/Finger Of Death|finger of death]]_ (DC 24), _[[universal monster rules/Summon|summon]]_ (level 6, 1d3 derghodaemons 50%)

##### Statistics
**Str** 21, **Dex** 25, **Con** 24, **Int** 14, **Wis** 15, **Cha** 24
**Base Atk** +17; **CMB** +23; **CMD** 41
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Nimble Moves|Nimble Moves]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +24 (+48 _[[spells/Jump|jump]]_), Escape Artist +27, Fly +9, Intimidate +27, Knowledge (planes) +22, Perception +22, Sense Motive +22, Stealth +23, Survival +22
**Languages** Abyssal, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abaddon or Astral Plane)
**Organization** solitary, pair, or pack (3–6)
**Treasure** standard

### Special Abilities

**Devour Soul (Su)** As a standard action, an astradaemon that begins its turn with a _[[conditions/Grappled|grappled]]_ opponent can attempt to draw out and consume the soul of its victim, killing it instantly. This ability only works on living creatures, which may resist with a DC 25 Fortitude saving throw. The save is Constitution-based. For every 5 HD of the slain creature, the daemon gains a +1 profane bonus on attacks, saving throws, and checks for 24 hours. This ability does not consume all of the soul, and pieces of it still exist after the daemon completes its feast (enough to be able to resurrect the slain victim normally).
**Soul Siphon (Su)** If a Small or larger living creature dies within 10 feet of an astradaemon, the daemon gains 1d8 temporary hit points and a +2 bonus to Strength for 10 minutes. These bonuses stack with themselves. _[[universal monster rules/Incorporeal|Incorporeal]]_ undead and living spirits traveling outside the body (such as a person using _[[spells/Astral Projection|astral projection]]_ or _[[spells/Magic Jar|magic jar]]_) take 1d8 points of damage each round within the daemon’s aura.

##### Description

Believed to be creations of the Four Horsemen, astradaemons live out their existence in search of souls to harvest. These _[[items/Weapon Magic Abilities/Deadly|deadly]]_ creatures are ravening _[[items/Weapon Magic Abilities/Planar|planar]]_ predators, openly hunting throughout the void for souls on which to feed. These voracious creatures are the personifications of death resulting from negative energy or level drain. Their vile touch drains life force from their enemies, and even perishing near them sates their thirst for life and souls.
---
cssclass: [monsters]
title1: Daemon, Phasmadaemon
desc_short: This serpentine monstrosity has the long snout of a crocodile,ram's horns,
  and mantis claws projecting from its sinuous body.
title2: Phasmadaemon
CR: 17
sources:
- name: Bestiary 6
  page: 74
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
- name: 'Book of the Damned - Volume 3: Horsemen of the Apocalypse'
  page: 52
  link: http://paizo.com/products/btpy8odg?Pathfinder-Campaign-Setting-Book-of-the-Damned-Volume-3-Horsemen-of-the-Apocalypse
XP: 102400
alignment: NE
size: Large
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 11
senses:
  darkvision: 60
  deathwatch: true
  true seeing: true
auras:
- name: frightful presence
  radius: 60
  DC: 27
AC:
  AC: 32
  touch: 17
  flat_footed: 24
  components:
    dex: 7
    dodge: 1
    natural,-1 size: 15
HP:
  HP: 264
  long: 23d10+138
saves:
  fort: 19
  ref: 14
  will: 19
immunities:
- acid
- death effects
- disease
- fear
- poison
resistances:
  cold: 10
  electricity: 10
  fire: 10
SR: 28
speeds:
  base: 30
  fly: 40
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +30 (3d8+8/19-20 plusgrab)
      entries:
      - - damage: 3d8+8
          type: plusgrab
          crit_range: 19-20
      attack: bite
      bonus:
      - 30
    - text: 2 claws +30 (2d6+8)
      entries:
      - - damage: 2d6+8
      count: 2
      attack: claws
      bonus:
      - 30
    - text: tail slap+25 (2d6+4)
      entries:
      - - damage: 2d6+4
      attack: tail slap
      bonus:
      - 25
  special:
  - consume fear
  - constrict(2d6+8)
  - rend (2 claws, 2d6+12)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: deathwatch
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: persistent image
    source: default
    freq: At will
    DC: 21
  - name: greater shadow conjuration
    source: default
    freq: 3/day
    DC: 23
  - name: greater shadow evocation
    source: default
    freq: 3/day
    DC: 24
  - name: mirage arcana
    source: default
    freq: 3/day
    DC: 21
  - name: nightmare
    source: default
    freq: 3/day
    DC: 21
  - name: permanent image
    source: default
    freq: 3/day
    DC: 22
  - name: quickened phantasmal killer
    source: default
    freq: 3/day
    DC: 20
  - name: mislead
    source: default
    freq: 1/day
    DC: 22
  - name: summon
    source: default
    freq: 1/day
    level: 8
    summons:
    - name: temerdaemon
      amount: 1
    - name: suspiridaemons
      amount: 1d3
      chance: 50%
  - name: symbol of fear
    source: default
    freq: 1/day
    DC: 22
  - name: weird
    source: default
    freq: 1/day
    DC: 25
  sources:
  - name: default
    CL: 18
    concentration: 24
ability_scores:
  STR: 26
  DEX: 25
  CON: 23
  INT: 17
  WIS: 18
  CHA: 22
BAB: 23
CMB: 32
CMB_other: +36 grapple
CMD: 50
CMD_other: can't be tripped
feats:
- name: Combat Casting
- name: Combat Reflexes
- name: Dodge
- name: Greater Spell Penetration
- name: Greater Vital Strike
- name: ImprovedCritical (bite)
- name: ImprovedInitiative
- name: Improved Vital Strike
- name: Iron Will
- name: Quicken Spell-LikeAbility (phantasmal killer)
- name: SpellPenetration
- name: Vital Strike
skills:
  Bluff: 32
  Fly: 35
  Intimidate: 32
  Knowledge (arcana,planes): 29
  Perception: 30
  Sense Motive: 30
  Spellcraft: 29
  Stealth: 29
languages:
- Abyssal
- Celestial
- Common
- Draconic
- Infernal;telepathy 100 ft.
special_qualities:
- compression
- tangible horror
ecology:
  environment: any (Abaddon)
  organization: solitary, pair, or cabal (3-4)
  treasure_type: standard
special_abilities:
  Consume Fear (Su): As a standard action, a phasmadaemon that begins its turn grappling
    an opponent can attempt to feed on the creature's mortality and innate terror.
    Any creature that does not succeed at a DC 27 Will save takes 1d6 points of Charisma
    drain and becomes shaken for 2d4 rounds; in addition, the phasmadaemon gains 5
    temporary hit points for every point of Charisma drain dealt this way. If the
    creature being grappled is already panicked at the beginning of the phasmadaemon's
    turn, it must instead succeed at a DC 27 Fortitude save or be slain instantly
    by the phasmadaemon, which gains a +4 profane bonus on attack rolls, saving throws,
    and checks for 24 hours as a result of feeding on the death fears of its victim.
    The save DCs are Charisma-based.
  Tangible Horror (Su): A phasmadaemon's illusion abilities are partially real at
    a level above and beyond those normally conjured forth by similar illusion spells.
    If a creature succeeds at its Will save to disbelieve either a phasmadaemon's
    greater shadow conjuration or greater shadow evocation spell-like ability, the
    conjured or evoked spell has 80% of the normal effect or is 80% likely to occur,
    rather than 60%.
desc_long: Among the most powerful members of daemonkind, the phasmadaemons personify
  death by fright, and conjure powers of illusion so terrifying that they steal the
  life from their victims. A phasmadaemon is 25 feet long from snout to tail, but
  can compress itself into surprisingly small areas thanks to its strange, elastic
  anatomy. It weighs half a ton.

---

# Daemon, Phasmadaemon
This serpentine monstrosity has the long snout of a _[[monsters/Crocodile|crocodile]]_,

ram’s horns, and mantis claws projecting from its sinuous body.
**Source** Bestiary 6 pg. 74, _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_ - Volume 3: Horsemen of the Apocalypse pg. 52
**XP** 102,400

NE Large outsider (daemon, evil, extraplanar)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Deathwatch|deathwatch]]_, _[[spells/True Seeing|true seeing]]_;

Perception +30
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (60 ft., DC 27)

##### Defense

**AC** 32, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+7 Dex, +1 dodge, +15 natural,

–1 size)
**hp** 264 (23d10+138)
**Fort** +19, **Ref** +14, **Will** +19
**Immune** acid, death effects, disease, _[[universal monster rules/Fear|fear]]_, poison; **Resist** cold 10,

electricity 10, fire 10; **SR** 28

##### Offense
**Speed** 30 ft., fly 40 ft. (good)
**Melee** bite +30 (3d8+8/19–20 plus

_[[universal monster rules/Grab|grab]]_), 2 claws +30 (2d6+8), tail slap

+25 (2d6+4)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** consume _fear_, _[[universal monster rules/Constrict|constrict]]_

(2d6+8), _[[universal monster rules/Rend|rend]]_ (2 claws, 2d6+12)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th;

concentration +24)
Constant—_deathwatch_, _true seeing_ 
At will—greater teleport (self plus 50 lbs. of objects only), _[[spells/Persistent Image|persistent image]]_ (DC 21) 
3/day—greater _[[spells/Shadow Conjuration|shadow conjuration]]_ (DC 23), greater _[[spells/Shadow Evocation|shadow evocation]]_ (DC 24), _[[spells/Mirage Arcana|mirage arcana]]_ (DC 21), _[[spells/Nightmare|nightmare]]_ (DC 21), _[[spells/Permanent Image|permanent image]]_ (DC 22), quickened _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 20) 
1/day—_[[spells/Mislead|mislead]]_ (DC 22), _[[universal monster rules/Summon|summon]]_ (level 8, 1 temerdaemon or 1d3 suspiridaemons 50%), _[[spells/Symbol of Fear|symbol of fear]]_ (DC 22), _[[spells/Weird|weird]]_ (DC 25)

##### Statistics
**Str** 26, **Dex** 25, **Con** 23, **Int** 17, **Wis** 18, **Cha** 22
**Base Atk** +23; **CMB** +32 (+36 grapple); **CMD** 50 (can’t be tripped)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Greater Spell Penetration|Greater Spell Penetration]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, Improved

Critical (bite), Improved

Initiative, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, Quicken Spell-Like

Ability (_phantasmal killer_), Spell

Penetration, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Bluff +32, Fly +35, Intimidate +32, Knowledge (arcana,

planes) +29, Perception +30, Sense Motive +30, Spellcraft +29,

Stealth +29
**Languages** Abyssal, Celestial, Common, Draconic, Infernal;

_[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Compression|compression]]_, tangible horror

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary, pair, or cabal (3–4)
**Treasure** standard

### Special Abilities

**Consume _Fear_ (Su)** As a standard action, a phasmadaemon that begins its turn grappling an opponent can attempt to feed on the creature’s mortality and innate terror. Any creature that does not succeed at a DC 27 Will save takes 1d6 points of Charisma drain and becomes _[[conditions/Shaken|shaken]]_ for 2d4 rounds; in addition, the phasmadaemon gains 5 temporary hit points for every point of Charisma drain dealt this way. If the creature being _[[conditions/Grappled|grappled]]_ is already _[[conditions/Panicked|panicked]]_ at the beginning of the phasmadaemon’s turn, it must instead succeed at a DC 27 Fortitude save or be slain instantly by the phasmadaemon, which gains a +4 profane bonus on attack rolls, saving throws, and checks for 24 hours as a result of feeding on the death fears of its victim. The save DCs are Charisma-based.

**Tangible Horror (Su)** A phasmadaemon’s illusion abilities are partially real at a level above and beyond those normally conjured forth by similar illusion spells. If a creature succeeds at its Will save to disbelieve either a phasmadaemon’s greater _shadow conjuration_ or greater _shadow evocation_ spell-like ability, the conjured or evoked spell has 80% of the normal effect or is 80% likely to occur, rather than 60%.

##### Description

Among the most powerful members of daemonkind, the phasmadaemons personify death by fright, and conjure powers of illusion so terrifying that they steal the life from their victims. A phasmadaemon is 25 feet long from snout to tail, but can compress itself into surprisingly small areas thanks to its strange, elastic anatomy. It weighs half a ton.
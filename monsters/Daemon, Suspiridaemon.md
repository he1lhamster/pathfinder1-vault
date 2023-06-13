---
cssclass: [monsters]
title1: Daemon, Suspiridaemon
desc_short: This tall, three-legged, vulture-headed fiend has a grotesquely long,
  suckered tongue and gangly arms that end in claws.
title2: Suspiridaemon
CR: 7
sources:
- name: Bestiary 6
  page: 76
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
- name: 'Book of the Damned - Volume 3: Horsemen of the Apocalypse'
  page: 56
  link: http://paizo.com/products/btpy8odg?Pathfinder-Campaign-Setting-Book-of-the-Damned-Volume-3-Horsemen-of-the-Apocalypse
XP: 3200
alignment: NE
size: Medium
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 7
senses:
  darkvision: 60
auras:
- name: thin air
  radius: 30
AC:
  AC: 20
  touch: 14
  flat_footed: 16
  components:
    dex: 3
    dodge: 1
    natural: 6
HP:
  HP: 85
  long: 9d10+36
saves:
  fort: 9
  ref: 9
  will: 8
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
  sonic: 30
SR: 18
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 claws +14 (1d6+5)
      entries:
      - - damage: 1d6+5
      count: 2
      attack: claws
      bonus:
      - 14
    - text: tongue +14 (1d6+7/19-20 plus grab)
      entries:
      - - damage: 1d6+7
          crit_range: 19-20
        - effect: grab
      attack: tongue
      bonus:
      - 14
  special:
  - concussive gasp
  - constrict (1d6+7)
  - strangle
  - suffocate
  - tongue
space: 5
reach: 5
reach_other: 10 ft. with tongue
spell_like_abilities:
  entries:
  - name: death knell
    source: default
    freq: At will
    DC: 15
  - name: ghoul touch
    source: default
    freq: At will
    DC: 15
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: ray of enfeeblement
    source: default
    freq: At will
    DC: 14
  - name: stinking cloud
    source: default
    freq: 3/day
    DC: 16
  - name: vampiric touch
    source: default
    freq: 3/day
  - name: cloudkill
    source: default
    freq: 1/day
    DC: 18
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: lacridaemons
      amount: 1d3
      chance: 35%
  sources:
  - name: default
    CL: 9
    concentration: 12
ability_scores:
  STR: 21
  DEX: 17
  CON: 18
  INT: 14
  WIS: 15
  CHA: 16
BAB: 9
CMB: 14
CMB_other: +18 grapple
CMD: 28
CMD_other: 30 vs. trip
feats:
- name: Combat Reflexes
- name: Dodge
- name: Great Fortitude
- name: Improved Critical (tongue)
- name: Improved Initiative
skills:
  Climb: 17
  Diplomacy: 15
  Intimidate: 15
  Knowledge (nature): 14
  Knowledge (planes): 14
  Perception: 14
  Sense Motive: 14
  Stealth: 15
languages:
- Abyssal
- Draconic
- Infernal (cannot speak)
- telepathy 100 ft.
special_qualities:
- no breath
ecology:
  environment: any (Abaddon)
  organization: solitary, gang (2-4), or mob (5-9)
  treasure_type: standard
special_abilities:
  Concussive Gasp (Su): Once per day as a standard action, a suspiridaemon can inhale
    with such sudden force as to evacuate the air in its proximity, causing a sudden
    wave of air pressure from the implosion. Every creature within 30 feet must succeed
    at a DC 18 Fortitude save or take 5d6 points of sonic damage and become sickened
    for 1d4 rounds. Any creature that succeeds at this save takes half damage and
    is not sickened. A suspiridaemon cannot perform this ability if it is currently
    grappling a creature with its tongue. The save DC is Constitution-based.
  Suffocate (Ex): A creature affected by the daemon's strangle ability cannot breathe
    and must hold its breath. Because of the daemon's thin air aura, this can quickly
    render an opponent unconscious.
  Thin Air (Su): A suspiridaemon's aura makes the air within 30 feet of it difficult
    to breathe. Creatures that need to breathe can hold their breath only half as
    long as normal while within this aura, and suffer from altitude effects as if
    on a low peak or in a high pass (see Altitude Zones on page 430 of the Pathfinder
    RPG Core Rulebook).
  Tongue (Ex): The tongue of a suspiridaemon is a primary attack and always applies
    1-1/2 times its Strength bonus on damage rolls.
desc_long: |-
  Horrid, vulture-headed fiends whose very presence makes the air difficult to breathe, suspiridaemons personify death by suffocation and strangulation. Their flesh is discolored and blotched like the stagnant blood under a suffocated corpse's skin, they don't breathe, and their bodies convulse and twitch like those of hanging victims. A suspiridaemon enjoys nothing more than the last choked gasp of a victim as it wraps its tongue around the creature's throat. Thanks to its utterly silent demeanor, it excels at committing slow, gruesome murders while hiding in the shadows. The only time a suspiridaemon makes a noticeable noise is when it loosens the tissues around its neck and inhales a booming breath- the sudden loss of air that results is enough to make foes fall ill. 

  A suspiridaemon is 6 feet tall and weighs 250 pounds.

---

# Daemon, Suspiridaemon
This tall, three-legged, vulture-headed fiend has a grotesquely long, suckered tongue and gangly arms that end in claws.
**Source** Bestiary 6 pg. 76, _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_ - Volume 3: Horsemen of the Apocalypse pg. 56
**XP** 3,200

NE Medium outsider (daemon, evil, extraplanar)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +14
**Aura** thin air (30 ft.)

##### Defense

**AC** 20, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+3 Dex, +1 _[[feats/Dodge|dodge]]_, +6 natural)
**hp** 85 (9d10+36)
**Fort** +9, **Ref** +9, **Will** +8
**DR** 10/good or silver; **Immune** acid, death effects, disease, poison; **Resist** cold 10, electricity 10, fire 10, sonic 30; **SR** 18

##### Offense
**Speed** 30 ft.
**Melee** 2 claws +14 (1d6+5), tongue +14 (1d6+7/19–20 plus _[[universal monster rules/Grab|grab]]_)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with tongue)
**Special Attacks** concussive gasp, _[[universal monster rules/Constrict|constrict]]_ (1d6+7), _[[universal monster rules/Strangle|strangle]]_, suffocate, tongue
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +12)
At will—_[[spells/Death Knell|death knell]]_ (DC 15), _[[spells/Ghoul touch|ghoul touch]]_ (DC 15), greater teleport (self plus 50 lbs. of objects only), _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 14) 
3/day—_[[spells/Stinking Cloud|stinking cloud]]_ (DC 16), _[[spells/Vampiric Touch|vampiric touch]]_ 
1/day—_[[spells/Cloudkill|cloudkill]]_ (DC 18), _[[universal monster rules/Summon|summon]]_ (level 4, 1d3 lacridaemons 35%)

##### Statistics
**Str** 21, **Dex** 17, **Con** 18, **Int** 14, **Wis** 15, **Cha** 16
**Base Atk** +9; **CMB** +14 (+18 grapple); **CMD** 28 (30 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Critical|Improved Critical]]_ (tongue), _[[feats/Improved Initiative|Improved Initiative]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +17, Diplomacy +15, Intimidate +15, Knowledge (nature, planes) +14, Perception +14, Sense Motive +14, Stealth +15
**Languages** Abyssal, Draconic, Infernal (cannot speak); _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/No Breath|no breath]]_

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary, gang (2–4), or mob (5–9)
**Treasure** standard

### Special Abilities

**Concussive Gasp (Su)** Once per day as a standard action, a suspiridaemon can inhale with such sudden force as to evacuate the air in its proximity, causing a sudden wave of air pressure from the _[[spells/Implosion|implosion]]_. Every creature within 30 feet must succeed at a DC 18 Fortitude save or take 5d6 points of sonic damage and become _[[conditions/Sickened|sickened]]_ for 1d4 rounds. Any creature that succeeds at this save takes half damage and is not _sickened_. A suspiridaemon cannot perform this ability if it is currently grappling a creature with its tongue. The save DC is Constitution-based.
**Suffocate (Ex)** A creature affected by the daemon’s _strangle_ ability cannot breathe and must hold its breath. Because of the daemon’s thin air aura, this can quickly render an opponent _[[conditions/Unconscious|unconscious]]_.

**Thin Air (Su)** A suspiridaemon’s aura makes the air within 30 feet of it difficult to breathe. Creatures that need to breathe can hold their breath only half as long as normal while within this aura, and suffer from altitude effects as if on a low peak or in a high pass (see Altitude Zones on page 430 of the Pathfinder RPG Core Rulebook).

**Tongue (Ex)** The tongue of a suspiridaemon is a primary attack and always applies 1-1/2 times its Strength bonus on damage rolls.

##### Description

Horrid, vulture-headed fiends whose very presence makes the air difficult to breathe, suspiridaemons personify death by _[[spells/Suffocation|suffocation]]_ and strangulation. Their flesh is discolored and blotched like the stagnant blood under a suffocated corpse’s skin, they don’t breathe, and their bodies convulse and twitch like those of hanging victims. A suspiridaemon enjoys nothing more than the last choked gasp of a victim as it wraps its tongue around the creature’s throat. Thanks to its utterly silent demeanor, it excels at committing _[[spells/Slow|slow]]_, gruesome murders while hiding in the shadows. The only time a suspiridaemon makes a noticeable noise is when it loosens the tissues around its neck and inhales a booming breath— the sudden loss of air that results is enough to make foes fall ill.

A suspiridaemon is 6 feet tall and weighs 250 pounds.
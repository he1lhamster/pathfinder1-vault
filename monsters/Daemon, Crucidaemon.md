---
cssclass: [monsters]
title1: Daemon, Crucidaemon
desc_short: Its body seemingly made of iron, this shapely feminine form has wrists
  pierced by chains that end in curved blades.
title2: Crucidaemon
CR: 15
sources:
- name: Bestiary 3
  page: 62
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 51200
alignment: NE
size: Medium
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 9
senses:
  darkvision: 60
  deathwatch: true
  detect good: true
  true seeing: true
AC:
  AC: 29
  touch: 16
  flat_footed: 23
  components:
    dex: 5
    dodge: 1
    natural: 13
HP:
  HP: 212
  long: 17d10+119
saves:
  fort: 17
  ref: 12
  will: 13
DR:
- amount: 10
  weakness: good and silver
immunities:
- acid
- bleed
- death effects
- disease
- poison
resistances:
  cold: 10
  electricity: 10
  fire: 10
SR: 26
speeds:
  base: 50
attacks:
  melee:
  - - text: daggers +29/+29/+24/+19/+14 (1d4+11/17-20)
      entries:
      - - damage: 1d4+11
          crit_range: 17-20
      attack: daggers
      bonus:
      - 29
      - 29
      - 24
      - 19
      - 14
  special:
  - bleed (2d6)
  - chained daggers
  - trap making
space: 5
reach: 10
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: deathwatch
    source: default
    freq: Constant
  - name: detect good
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: fear
    source: default
    freq: At will
    DC: 23
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: invisibility
    source: default
    freq: At will
  - name: greater glyph of warding
    source: default
    freq: 3/day
    DC: 25
  - name: hold monster
    source: default
    freq: 3/day
    DC: 24
  - name: insanity
    source: default
    freq: 1/day
    DC: 26
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: piscodaemons
      amount: 2
      chance: 50%
  - name: symbol of pain
    source: default
    freq: 1/day
    DC: 24
  sources:
  - name: default
    CL: 16
    concentration: 25
ability_scores:
  STR: 28
  DEX: 21
  CON: 24
  INT: 16
  WIS: 17
  CHA: 29
BAB: 17
CMB: 26
CMD: 42
feats:
- name: Dodge
- name: Improved Critical (daggers)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Mobility
- name: Spring Attack
- name: Stealthy
- name: Step Up
- name: Weapon Focus (daggers)
skills:
  Bluff: 29
  Craft (traps): 31
  Disable Device: 25
  Escape Artist: 7
  Intimidate: 29
  Knowledge (arcana): 11
  Knowledge (engineering): 11
  Perception: 23
  Sense Motive: 16
  Spellcraft: 18
  Stealth: 29
  Use Magic Device: 19
  _racial_mods:
    Craft (traps):
      _: 8
languages:
- Abyssal
- Draconic
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Abaddon)
  organization: solitary, pair, or inquisition (3-6)
  treasure_type: standard
special_abilities:
  Chained Daggers (Su): A crucidaemon fights with the two daggers chained to its wrists
    as if dual wielding daggers with a reach of 10 feet (although it can also attack
    adjacent foes with no penalty). It takes no penalty on attack or damage rolls
    while wielding both of these daggers at once. These daggers are considered to
    be +2 daggers that deal 2d6 points of bleed damage. The daggers become nonmagical
    upon the daemon's death, and cannot be disarmed. A crucidaemon may remanifest
    a destroyed dagger as a standard action.
  Trap Making (Ex): A crucidaemon can use Disable Device to disarm magic traps. When
    it uses its greater glyph of warding spell-like ability to create a spell glyph,
    it may utilize any 6th-level or lower spell from the cleric or the wizard spell
    list, even though it otherwise can't cast these spells. The Perception and Disable
    Device DCs for any traps a crucidaemon creates gain a +2 bonus.
desc_long: |-
  Bloody representations of death by traps or torture, crucidaemons spend their existence subjecting creatures to an eternity of pain and terror. Whereas many daemons are quick to feed on the soul of mortals they capture, a crucidaemon lets its victims linger, marinating their souls in torment and pain so that when the time for feeding finally comes, they welcome their final oblivion with tears of gratitude.

  Crucidaemons are 6 feet tall and weigh 250 pounds.

---

# Daemon, Crucidaemon
Its body seemingly made of iron, this shapely feminine form has wrists pierced by chains that end in curved blades.
**Source** Bestiary 3 pg. 62
**XP** 51,200

NE Medium outsider (daemon, evil, extraplanar)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Deathwatch|deathwatch]]_, _[[spells/Detect Good|detect good]]_, _[[spells/True Seeing|true seeing]]_; Perception +23

##### Defense

**AC** 29, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+5 Dex, +1 _[[feats/Dodge|dodge]]_, +13 natural)
**hp** 212 (17d10+119)
**Fort** +17, **Ref** +12, **Will** +13
**DR** 10/good and silver; **Immune** acid, _[[universal monster rules/Bleed|bleed]]_, death effects, disease, poison; **Resist** cold 10, electricity 10, fire 10; **SR** 26

##### Offense
**Speed** 50 ft.
**Melee** daggers +29/+29/+24/+19/+14 (1d4+11/17–20)
**Space** 5 ft., **Reach** 10 ft.
**Special Attacks** _bleed_ (2d6), chained daggers, trap making
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +25)
Constant—_[[spells/Air Walk|air walk]]_, _deathwatch_, _detect good_, _true seeing_
At will—_[[universal monster rules/Fear|fear]]_ (DC 23), greater teleport (self plus 50 lbs. of objects only), _[[spells/Invisibility|invisibility]]_
3/day—greater _[[spells/Glyph Of Warding|glyph of warding]]_ (DC 25), _[[spells/Hold Monster|hold monster]]_ (DC 24)
1/day—_[[spells/Insanity|insanity]]_ (DC 26), _[[universal monster rules/Summon|summon]]_ (level 4, 2 piscodaemons 50%), _[[spells/Symbol of Pain|symbol of pain]]_ (DC 24)

##### Statistics
**Str** 28, **Dex** 21, **Con** 24, **Int** 16, **Wis** 17, **Cha** 29
**Base Atk** +17; **CMB** +26; **CMD** 42
**Feats** _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (daggers), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Stealthy|Stealthy]]_, _[[feats/Step Up|Step Up]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (daggers)
**Skills** Bluff +29, Craft (traps) +31, Disable Device +25, Escape Artist +7, Intimidate +29, Knowledge (arcana, engineering) +11, Perception +23, Sense Motive +16, Spellcraft +18, Stealth +29, Use Magic Device +19; **Racial Modifiers** +8 Craft (traps)
**Languages** Abyssal, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary, pair, or inquisition (3–6)
**Treasure** standard

### Special Abilities

**Chained Daggers (Su)** A crucidaemon fights with the two daggers chained to its wrists as if dual wielding daggers with a reach of 10 feet (although it can also attack adjacent foes with no penalty). It takes no penalty on attack or damage rolls while wielding both of these daggers at once. These daggers are considered to be +2 daggers that deal 2d6 points of _bleed_ damage. The daggers become nonmagical upon the daemon’s death, and cannot be disarmed. A crucidaemon may remanifest a destroyed _[[items/Weapon/Dagger|dagger]]_ as a standard action.

**Trap Making (Ex)** A crucidaemon can use Disable Device to disarm magic traps. When it uses its greater _glyph of warding_ spell-like ability to create a spell glyph, it may utilize any 6th-level or lower spell from the _[[classes/Cleric|cleric]]_ or the _[[classes/Wizard|wizard]]_ spell list, even though it otherwise can’t cast these spells. The Perception and Disable Device DCs for any traps a crucidaemon creates gain a +2 bonus.

##### Description

Bloody representations of death by traps or torture, crucidaemons spend their existence subjecting creatures to an eternity of pain and terror. Whereas many daemons are quick to feed on the soul of mortals they capture, a crucidaemon lets its victims linger, marinating their souls in torment and pain so that when the time for feeding finally comes, they welcome their final _[[monsters/Oblivion|oblivion]]_ with tears of gratitude.

Crucidaemons are 6 feet tall and weigh 250 pounds.
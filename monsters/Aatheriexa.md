---
cssclass: [monsters]
title1: Aatheriexa
desc_short: A tangle of thin, tentacle-like eyestalks floats in the air, its innumerable
  unblinking eyes each projecting an air of cruelty.
title2: Aatheriexa
CR: 7
sources:
- name: Bestiary 5
  page: 7
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 3200
alignment: NE
size: Medium
type: aberration
initiative:
  bonus: 9
senses:
  all-around vision: true
  darkvision: 120
  low-light vision: true
  see invisibility: true
auras:
- name: unnatural aura
  radius: 30
AC:
  AC: 21
  touch: 15
  flat_footed: 16
  components:
    dex: 5
    natural: 6
HP:
  HP: 84
  long: 13d8+26
saves:
  fort: 6
  ref: 9
  will: 8
DR:
- amount: 5
  weakness: magic
immunities:
- cold
- disease
- poison
speeds:
  base: 5
  fly: 50
  fly_maneuverability: good
attacks:
  melee:
  - - text: tentacles +15 (3d6 plus grab and withering)
      entries:
      - - damage: 3d6
        - effect: grab
        - effect: withering
      attack: tentacles
      bonus:
      - 15
  special:
  - constrict (3d6 plus withering)
  - gnaw
  - pull (tentacles, 5 feet)
space: 5
reach: 5
reach_other: 15 ft. with tentacles
spell_like_abilities:
  entries:
  - name: calm emotions
    source: default
    freq: At will
    DC: 16
  - name: charm monster
    source: default
    freq: At will
    DC: 18
  - name: clairaudience/clairvoyance
    source: default
    freq: At will
    other: clairvoyance only
  - name: daze monster
    source: default
    freq: At will
    DC: 16
  - name: feather fall
    source: default
    freq: At will
  - name: dispel magic
    source: default
    freq: 3/day
  - name: lightning bolt
    source: default
    freq: 3/day
    DC: 17
  - name: dominate monster
    source: default
    freq: 1/day
    DC: 23
  - name: interplanetary teleport
    source: default
    freq: 1/month
  sources:
  - name: default
    CL: 13
    concentration: 17
ability_scores:
  STR: 11
  DEX: 21
  CON: 14
  INT: 18
  WIS: 10
  CHA: 19
BAB: 9
CMB: 9
CMB_other: +21 grapple
CMD: 24
CMD_other: 32 vs. grapple, can't be tripped
feats:
- name: Combat Reflexes
- name: Critical Focus
- name: Flyby Attack
- is_bonus: true
  name: Hover
- name: Improved Initiative
- name: Skill Focus (Perception)
- name: Weapon Finesse
- name: Weapon Focus (tentacle)
- is_bonus: true
  name: Wingover
skills:
  Acrobatics: 21
  Diplomacy: 17
  Fly: 20
  Knowledge (arcana): 14
  Perception: 28
  Sense Motive: 13
  Spellcraft: 15
  Stealth: 21
  Use Magic Device: 17
  _racial_mods:
    Perception:
      _: 6
languages:
- Aklo
- Common
- Draconic
- Undercommon
- telepathy 100 ft.
special_qualities:
- compression
- float
- no breath
ecology:
  environment: any land
  organization: solitary, pair, pod (3-5), or invasion (6-36)
  treasure_type: standard
special_abilities:
  Gnaw (Ex): When an aatheriexa shares the same square as a helpless creature, it
    can automatically deal 3d6 points of damage as a swift action by gnawing with
    its central maw.
  Float (Ex): Aatheriexa can fly, though they must remain with 2 feet of a solid or
    liquid surface.
  Tentacles (Ex): An aatheriexa's barbed eyestalk tentacles must all strike at a single
    target, but they do so as a primary attack. The tentacles deal bludgeoning and
    slashing damage and grant the aatheriexa a +8 bonus on grapple combat maneuver
    checks.
  Withering (Ex): An aatheriexa's tentacles secrete a toxin that causes flesh to swiftly
    rot and slough off the bone. A creature damaged by an aatheriexa's tentacles or
    constrict attack must succeed at a DC 18 Fortitude save or take 1d4 points of
    Strength damage and 1d4 points of Constitution damage. This is a poison effect
    and the save DC is Constitution-based.
desc_long: |-
  Aatheriexas were once a race of conquerors and slavers, but since the destruction of their homeworld, the survivors have wandered the cosmos. Exceedingly cruel, they find perverse pleasure in tormenting those they capture, using them as disposable bodyguards or subjecting them to sadistic magic experiments.

   An aatheriexa's fleshy pink center is roughly 2 feet in diameter, and features a maw of gnashing teeth. Its grasping eye-tentacles hang down like the leaves of a weeping willow and extend its effective diameter to 5 feet. Aatheriexas weigh approximately 150 pounds.

---

# Aatheriexa
A tangle of thin, tentacle-like eyestalks floats in the air, its innumerable unblinking eyes each projecting an air of _[[feats/Cruelty|cruelty]]_.
**Source** Bestiary 5 pg. 7
**XP** 3,200

NE Medium aberration
**Init** +9; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +28
**Aura** _[[universal monster rules/Unnatural Aura|unnatural aura]]_ (30 ft.)

##### Defense

**AC** 21, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+5 Dex, +6 natural)
**hp** 84 (13d8+26)
**Fort** +6, **Ref** +9, **Will** +8
**DR** 5/magic; **Immune** cold, disease, poison

##### Offense
**Speed** 5 ft., fly 50 ft. (good)
**Melee** tentacles +15 (3d6 plus _[[universal monster rules/Grab|grab]]_ and withering)
**Space** 5 ft., **Reach** 5 ft. (15 ft. with tentacles)
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (3d6 plus withering), gnaw, _[[universal monster rules/Pull|pull]]_ (tentacles, 5 feet)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +17)
At will—_[[spells/Calm Emotions|calm emotions]]_ (DC 16), _[[spells/Charm Monster|charm monster]]_ (DC 18), clairaudience/clairvoyance (clairvoyance only), _[[spells/Daze Monster|daze monster]]_ (DC 16), _[[spells/Feather Fall|feather fall]]_
3/day—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 17)
1/day—_[[spells/Dominate Monster|dominate monster]]_ (DC 23)
1/month—_[[spells/Interplanetary Teleport|interplanetary teleport]]_

##### Statistics
**Str** 11, **Dex** 21, **Con** 14, **Int** 18, **Wis** 10, **Cha** 19
**Base Atk** +9; **CMB** +9 (+21 grapple); **CMD** 24 (32 vs. grapple, can’t be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (tentacle), _[[feats/Wingover|Wingover]]_
**Skills** Acrobatics +21, Diplomacy +17, Fly +20, Knowledge (arcana) +14, Perception +28, Sense Motive +13, Spellcraft +15, Stealth +21, Use Magic Device +17; **Racial Modifiers** +6 Perception
**Languages** Aklo, Common, Draconic, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Compression|compression]]_, float, _[[universal monster rules/No Breath|no breath]]_

##### Ecology

**Environment** any land
**Organization** solitary, pair, pod (3–5), or invasion (6–36)
**Treasure** standard

### Special Abilities

**Gnaw (Ex)** When an _[[monsters/Aatheriexa|aatheriexa]]_ shares the same square as a _[[conditions/Helpless|helpless]]_ creature, it can automatically deal 3d6 points of damage as a swift action by gnawing with its central maw.

**Float (Ex)** _Aatheriexa_ can fly, though they must remain with 2 feet of a solid or liquid surface.

**Tentacles (Ex)** An _aatheriexa_’s barbed eyestalk tentacles must all strike at a single target, but they do so as a primary attack. The tentacles deal bludgeoning and slashing damage and grant the _aatheriexa_ a +8 bonus on grapple combat maneuver checks.

**Withering (Ex)** An _aatheriexa_’s tentacles secrete a toxin that causes flesh to swiftly rot and _[[spells/Slough|slough]]_ off the bone. A creature damaged by an _aatheriexa_’s tentacles or _constrict_ attack must succeed at a DC 18 Fortitude save or take 1d4 points of Strength damage and 1d4 points of Constitution damage. This is a poison effect and the save DC is Constitution-based.

##### Description

Aatheriexas were once a race of conquerors and slavers, but since the _[[spells/Destruction|destruction]]_ of their homeworld, the survivors have wandered the cosmos. Exceedingly _[[items/Weapon Magic Abilities/Cruel|cruel]]_, they find perverse pleasure in tormenting those they capture, using them as disposable bodyguards or subjecting them to sadistic magic experiments.

An _aatheriexa_’s fleshy pink center is roughly 2 feet in diameter, and features a maw of gnashing teeth. Its grasping eye-tentacles hang down like the leaves of a _[[items/Armor Magic Abilities/Weeping|weeping]]_ willow and extend its effective diameter to 5 feet. Aatheriexas weigh approximately 150 pounds.
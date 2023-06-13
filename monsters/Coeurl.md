---
cssclass: [monsters]
title1: Coeurl
is_3.5: true
desc_short: Powerfully corded muscles ripple beneath the ebon flesh of this strange,
  sleek feline. Similar in shape to an oversized panther, the lean beast's forelegs
  stretch farther than those to the rear, each ending in powerful claws. Rather than
  ears, curling tendrils flit at the sides of its head. Most distinctive, though,
  are the twin tentacles rising from the beast's shoulders, powerful appendages that
  slice through the air like living whips and terminate in clusters of thin spines.
title2: Coeurl
CR: 8
sources:
- name: 'Pathfinder #22: The End of Eternity'
  page: 78
  link: http://paizo.com/pathfinder/adventurePath/legacyOfFire/v5748btpy87ux
alignment: CN
size: Large
type: magical beast
initiative:
  bonus: 4
senses:
  blindsense: 60
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 19
  touch: 13
  flat_footed: 15
  components:
    dex: 4
    natural: 6
    size: -1
HP:
  HP: 95
  long: 10d10+40
saves:
  fort: 11
  ref: 11
  will: 4
immunities:
- sonic
resistances:
  electricity: 10
SR: 19
speeds:
  base: 40
attacks:
  melee:
  - - text: 2 tentacles +15 (1d6+6)
      entries:
      - - damage: 1d6+6
      count: 2
      attack: tentacles
      bonus:
      - 15
    - text: 2 claws +10 (1d6+3)
      entries:
      - - damage: 1d6+3
      count: 2
      attack: claws
      bonus:
      - 10
    - text: bite +10 (1d8+3)
      entries:
      - - damage: 1d8+3
      attack: bite
      bonus:
      - 10
  special:
  - rend (2d6+9)
  - rust
space: 10
reach: 10
reach_other: 15 ft. with tentacles
spell_like_abilities:
  entries:
  - name: entropic shield
    source: default
    freq: 3/day
  - name: mage hand
    source: default
    freq: 3/day
  - name: shatter
    source: default
    freq: 3/day
    DC: 13
  - name: sympathetic vibration
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 12
ability_scores:
  STR: 22
  DEX: 19
  CON: 18
  INT: 15
  WIS: 12
  CHA: 12
BAB: 10
grapple_3.5: 20
feats:
- name: Dodge
- name: Mobility
- name: Spring Attack
- name: Stealthy
skills:
  Balance: 9
  Bluff: 8
  Disable Device: 6
  Hide: 15
  Listen: 4
  Move Silently: 19
  Open Lock: 16
  Spot: 4
  Survival: 4
  Tumble: 11
  _racial_mods:
    Bluff:
      _: 4
    Disable Device:
      _: 4
    Open Lock:
      _: 8
languages:
- telepathy 100 ft.
special_qualities:
- vibration manipulation
ecology:
  environment: any land
  organization: solitary
  treasure_type: standard
  advancement_3.5:
  - type: size
    HD_min: 11
    size: Large
    HD_max: 16
  - type: size
    HD_min: 17
    size: Huge
    HD_max: 22
special_abilities:
  Blindsense (Ex): A coeurl can locate creatures within 60 feet by nonvisual means
    (mostly by noticing vibrations and other environmental clues). Opponents the coeurl
    can't actually see still have total concealment against the coeurl.
  Rend (Ex): If a coeurl hits with both tentacle attacks, it latches onto the opponent's
    body and tears the flesh. This attack automatically deals an additional 2d6+9
    points of damage.
  Rust (Ex): A coeurl that holds its tentacle in contact with metal for a full minute
    causes the target metal to corrode, falling to pieces and becoming useless immediately.
    The touch can destroy two metal objects or up to a 10-foot-cube of metal per minute.
    Magic armor and weapons, and other magic items made of metal, must succeed on
    a DC 19 Reflex save or be dissolved. The save DC is Constitution-based.
  Vibration Manipulation (Ex): A coeurl can manipulate vibrations to disrupt the workings
    of machines and constructs. At will, a coeurl can lock or unlock any non-magical
    locking mechanisim within 15 feet. Once per round, it can also attempt a Disable
    Device check on any mechanical device within 15 feet. A coeurl always knows whether
    or not its Disable Device check has succeeded. In addition, a coeurl's tentacle
    attacks deal an additional +2d6 points of sonic damage to constructs. None of
    this ability's aspects function while a coeurl is within an area of magical silence.
desc_long: |-
  Lean and deadly, the animalistic appearance of the alien coeurls belies a keen intelligence and the tempered patience of a masterful hunter. Although similar in form to a wiry jungle cat, coeurls' forelegs are longer than their rear, giving the shadowy-skinned, hairless creatures a more elevated posture than a common feline. Rather than ears, bundles of wavering antennae extend from either side of their heads, delicate organs capable of detecting sounds and other, more enigmatic sensations. A coeurl's most distinguishing trait is the pair of powerful black tentacles that extend from its shoulders, each ending in a cluster of flexible, barb-like digits capable of manipulating objects just as nimbly as a human hand.

  A typical coeurl stands approximately 3-1/2 feet tall and about 8 feet long, with a densely muscled body weighing around 650 pounds.

---

# Coeurl
Powerfully corded muscles ripple beneath the ebon flesh of this strange, sleek feline. Similar in shape to an oversized panther, the lean beast’s forelegs stretch farther than those to the rear, each ending in powerful claws. Rather than ears, curling tendrils flit at the sides of its head. Most distinctive, though, are the twin tentacles rising from the beast’s shoulders, powerful appendages that slice through the air like living whips and terminate in clusters of thin spines.
**Source** Pathfinder #22: The End of Eternity pg. 78

CN Large magical beast
**Init** +4; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 60 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Listen +4, Spot +4

##### Defense

**AC** 19, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 Dex, +6 natural, -1 size)
**hp** 95 (10d10+40)
**Fort** +11, **Ref** +11, **Will** +4
**Immune** sonic; **Resist** electricity 10; **SR** 19

##### Offense
**Speed** 40 ft.
**Melee** 2 tentacles +15 (1d6+6) and 2 claws +10 (1d6+3) and bite +10 (1d8+3)
**Space** 10 ft., **Reach** 10 ft. (15 ft. with tentacles)
**Special Attacks** _[[universal monster rules/Rend|rend]]_ (2d6+9), rust
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th)
3/day - _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Shatter|shatter]]_ (DC 13), _[[spells/Sympathetic Vibration|sympathetic vibration]]_

##### Statistics
**Str** 22, **Dex** 19, **Con** 18, **Int** 15, **Wis** 12, **Cha** 12
**Base Atk** +10; **Grapple** +20
**Feats** Dodge, _[[feats/Mobility|Mobility]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Stealthy|Stealthy]]_
**Skills** Balance +9, Bluff +8, Disable Device +6, Hide +15, Listen +4, Move Silently +19, Open Lock +16, Spot +4, Survival +4, Tumble +11; **Racial Modifiers** +4 Bluff, +4 Disable Device, +8 Open Lock
**Languages** _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** vibration manipulation

##### Ecology

**Environment** any land
**Organization** solitary
**Treasure** standard
**Advancement** 11-16 HD (Large), 17-22 HD (Huge)

### Special Abilities

**_Blindsense_ (Ex)** A _[[monsters/Coeurl|coeurl]]_ can locate creatures within 60 feet by nonvisual means (mostly by noticing vibrations and other environmental clues). Opponents the _coeurl_ can’t actually see still have total concealment against the _coeurl_.

**_Rend_ (Ex)** If a _coeurl_ hits with both tentacle attacks, it latches onto the opponent’s body and tears the flesh. This attack automatically deals an additional 2d6+9 points of damage.

**Rust (Ex)** A _coeurl_ that holds its tentacle in contact with metal for a full minute causes the target metal to corrode, falling to pieces and becoming useless immediately. The touch can destroy two metal objects or up to a 10-foot-cube of metal per minute. Magic armor and weapons, and other magic items made of metal, must succeed on a DC 19 Reflex save or be dissolved. The save DC is Constitution-based.

**Vibration Manipulation (Ex)** A _coeurl_ can manipulate vibrations to disrupt the workings of machines and constructs. At will, a _coeurl_ can lock or unlock any non-magical locking mechanisim within 15 feet. Once per round, it can also attempt a Disable Device check on any mechanical device within 15 feet. A _coeurl_ always knows whether or not its Disable Device check has succeeded. In addition, a _coeurl_’s tentacle attacks deal an additional +2d6 points of sonic damage to constructs. None of this ability’s aspects function while a _coeurl_ is within an area of magical _[[spells/Silence|silence]]_.

##### Description

Lean and _[[items/Weapon Magic Abilities/Deadly|deadly]]_, the animalistic appearance of the alien coeurls belies a _[[items/Weapon Magic Abilities/Keen|keen]]_ intelligence and the tempered patience of a masterful _[[classes/Hunter|hunter]]_. Although similar in form to a wiry jungle cat, coeurls’ forelegs are longer than their rear, giving the shadowy-skinned, hairless creatures a more elevated posture than a common feline. Rather than ears, bundles of wavering antennae extend from either side of their heads, delicate organs capable of detecting sounds and other, more enigmatic sensations. A _coeurl_’s most distinguishing trait is the pair of powerful _[[spells/Black Tentacles|black tentacles]]_ that extend from its shoulders, each ending in a cluster of flexible, barb-like digits capable of manipulating objects just as nimbly as a human hand.

A typical _coeurl_ stands approximately 3-1/2 feet tall and about 8 feet long, with a densely muscled body weighing around 650 pounds.
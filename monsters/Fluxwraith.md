---
cssclass: [monsters]
title1: Fluxwraith
desc_short: This hovering, translucent humanoid appears to sleep serenely, even as
  shards of flickering energy encircle it, each fragment reflecting younger or older
  versions of itself.
title2: Fluxwraith
CR: 17
sources:
- name: 'Pathfinder #126: Beyond the Veiled Past'
  page: 86
  link: http://paizo.com/products/btpy9xf0?Pathfinder-Adventure-Path-126-Beyond-the-Veiled-Past
XP: 102400
alignment: NE
size: Medium
type: undead
subtypes:
- incorporeal
initiative:
  bonus: 13
senses:
  darkvision: 60
  lifesense: true
auras:
- name: slow aura
  radius: 30
AC:
  AC: 26
  touch: 26
  flat_footed: 16
  components:
    deflection: 6
    dex: 9
    dodge: 1
HP:
  HP: 273
  long: 26d8+156
saves:
  fort: 14
  ref: 17
  will: 20
defensive_abilities:
- channel resistance +4
- incorporeal
immunities:
- undead traits
speeds:
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: incorporeal touch +28 (15d6 plus time shift)
      entries:
      - - damage: 15d6
        - effect: time shift
      attack: incorporeal touch
      bonus:
      - 28
  special:
  - temporal madness
  - time shift
spell_like_abilities:
  entries:
  - name: arcane sight
    source: default
    freq: At will
  - name: deja vu
    source: default
    freq: At will
  - name: haste
    source: default
    freq: At will
  - name: quickened deja vu
    source: default
    freq: 3/day
  - name: hold monster
    source: default
    freq: 3/day
    DC: 21
  - name: mirror image
    source: default
    freq: 3/day
  - name: temporal stasis
    source: default
    freq: 3/day
    DC: 24
  - name: time stop
    source: default
    freq: 1/day
    DC: 25
  sources:
  - name: default
    CL: 20
    concentration: 26
ability_scores:
  STR:
  DEX: 28
  CON:
  INT: 18
  WIS: 20
  CHA: 23
BAB: 19
CMB: 28
CMD: 45
feats:
- name: Ability Focus (time shift)
- name: Alertness
- name: Combat Casting
- name: Combat Expertise
- name: Combat Reflexes
- name: Dodge
- name: Flyby Attack
- name: Hover
- name: Improved Initiative
- name: Lunge
- name: Mobility
- name: Quicken Spell-Like Ability (deja vu)
- name: Stand Still
skills:
  Acrobatics: 25
  Diplomacy: 25
  Fly: 36
  Intimidate: 28
  Knowledge (arcana): 23
  Knowledge (dungeoneering): 18
  Knowledge (planes): 18
  Knowledge (history): 24
  Perception: 37
  Sense Motive: 37
  Spellcraft: 23
  Stealth: 20
languages:
- Ancient Osiriani
- Azlanti
- Common
- Cyclops
- Thassilonian
ecology:
  environment: any
  organization: solitary or cluster (2-4)
  treasure_type: standard
special_abilities:
  Slow Aura (Su): Fluxwraiths constantly emit a 30-foot-radius aura of temporal distortion.
    Any creature within this aura is affected as if by slow, but it gets no saving
    throw. If a creature exits the radius, the effect ceases at the end of its turn.
    If the fluxwraith moves more than 30 feet away from an affected creature, the
    effect ends immediately for that creature. Creatures affected by freedom, freedom
    of movement, or haste are unaffected by the slow aura.
  Temporal Madness (Su): As a ranged touch attack with a range increment of 30 feet,
    a fluxwraith can grant a target a mind-shattering glimpse of its own existence
    as it appears to a time-displaced entity. The attack deals 1d6 points of Wisdom
    drain, although this drain is reduced to 1 point if the target succeeds at a DC
    29 Will saving throw. This is a mind-affecting effect. The save DC is Charisma-based.
  Time Shift (Su): A creature struck by the fluxwraith's touch attack must succeed
    at a DC 31 Will saving throw or be thrust forward in time, vanishing and then,
    1d4 rounds later, reappearing in the same location. If the space has become occupied
    by an object or another creature, the affected creature is shunted to a random
    adjacent space, taking 6d6 points of damage. From the creature's perspective,
    the time shift is instantaneous. Any duration effects active upon the creature
    become suspended during the time shift, resuming when the creature reappears.
    Creatures that succeed at their saving throws cannot be affected by the same fluxwraith's
    time shift ability for 24 hours. The save DC is Charisma-based.
desc_long: |-
  A fluxwraith is an incorporeal undead with a host of extraordinary powers owing to its singular status as a time-displaced entity. Its serene appearance and dreamlike demeanor harken to its origins, for in life it slept away the centuries in a state of magical or technological stasis. Now, whether by accident or malign intent, the fluxwraith's soul lies scattered across the timestream. Demented by its paradoxical consciousness, it yearns to destroy any living being audacious enough to exist within a single point of time.

   Because its appearance depends upon its state when it first entered suspended animation, viewers may sometimes be able to deduce clues about its former life, as well as its motivations for entering hibernation. Some seek interminable sleep while they are in the prime of life, aiming to awaken and embrace immortality as a perfect specimen, while others hope to defer a terminal diagnosis. However, the sleeper's motivations in life seldom define a fluxwraith's outlook, as the process of becoming undead erases all but the most deeply ingrained mortal traits.

   The first hint of the fluxwraith's destructive nature manifests in the caul of energy that winks on and off around it. This ever-shifting network of temporal energy contains fragments of its consciousness, appearing as flickering aspects of itself as a youth, an adult, or a corpse. Scrutinizing these vignettes may provide further clues about the fluxwraith's former existence, although any creature that enters the fluxwraith's aura, or any creature affected by its attacks, may begin to see its own reflections appear within the shards as well. These disturbing images depict a creature not as it is, but as the fluxwraith perceives it in the past or future.

   Fluxwraiths tend to speak ancient or dead languages, often murmuring incomplete or garbled statements that blend past and future tenses in unsettling ways.

---

# Fluxwraith
This hovering, translucent humanoid appears to sleep serenely, even as shards of flickering energy encircle it, each fragment _[[items/Armor Magic Abilities/Reflecting|reflecting]]_ younger or older versions of itself.
**Source** Pathfinder #126: Beyond the Veiled Past pg. 86
**XP** 102,400

NE Medium undead (_[[universal monster rules/Incorporeal|incorporeal]]_)
**Init** +13; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Lifesense|lifesense]]_; Perception +37
**Aura** _[[spells/Slow|slow]]_ aura (30 ft.)

##### Defense

**AC** 26, touch 26, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+6 _[[spells/Deflection|deflection]]_, +9 Dex, +1 _[[feats/Dodge|dodge]]_)
**hp** 273 (26d8+156)
**Fort** +14, **Ref** +17, **Will** +20
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4, _incorporeal_; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** fly 60 ft. (perfect)
**Melee** _incorporeal_ touch +28 (15d6 plus time shift)
**Special Attacks** temporal madness, time shift
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +26)
At will—_[[spells/Arcane Sight|arcane sight]]_, _[[spells/Deja Vu|deja vu]]_, _[[spells/Haste|haste]]_ 
3/day—quickened _deja vu_, _[[spells/Hold Monster|hold monster]]_ (DC 21), _[[spells/Mirror Image|mirror image]]_, _[[spells/Temporal Stasis|temporal stasis]]_ (DC 24) 
1/day—_[[spells/Time Stop|time stop]]_ (DC 25)

##### Statistics
**Str** —, **Dex** 28, **Con** —, **Int** 18, **Wis** 20, **Cha** 23
**Base Atk** +19; **CMB** +28; **CMD** 45
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (time shift), _[[feats/Alertness|Alertness]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_deja vu_), _[[feats/Stand Still|Stand Still]]_
**Skills** Acrobatics +25, Diplomacy +25, Fly +36, Intimidate +28, Knowledge (arcana) +23, Knowledge (dungeoneering, planes) +18, Knowledge (history) +24, Perception +37, Sense Motive +37, Spellcraft +23, Stealth +20
**Languages** Ancient Osiriani, Azlanti, Common, _[[monsters/Cyclops|Cyclops]]_, Thassilonian

##### Ecology

**Environment** any
**Organization** solitary or cluster (2-4)
**Treasure** standard

### Special Abilities
**_Slow_ Aura (Su)** Fluxwraiths constantly emit a 30-foot-radius aura of temporal distortion. Any creature within this aura is affected as if by _slow_, but it gets no saving throw. If a creature exits the radius, the effect ceases at the end of its turn. If the _[[monsters/Fluxwraith|fluxwraith]]_ moves more than 30 feet away from an affected creature, the effect ends immediately for that creature. Creatures affected by _[[spells/Freedom|freedom]]_, _[[spells/Freedom of Movement|freedom of movement]]_, or _haste_ are unaffected by the _slow_ aura.

**Temporal Madness (Su)** As a ranged touch attack with a range increment of 30 feet, a _fluxwraith_ can grant a target a mind-shattering glimpse of its own existence as it appears to a time-displaced entity. The attack deals 1d6 points of Wisdom drain, although this drain is reduced to 1 point if the target succeeds at a DC 29 Will saving throw. This is a mind-affecting effect. The save DC is Charisma-based.

**Time Shift (Su)** A creature struck by the _fluxwraith_’s touch attack must succeed at a DC 31 Will saving throw or be thrust forward in time, vanishing and then, 1d4 rounds later, reappearing in the same location. If the space has become occupied by an object or another creature, the affected creature is shunted to a random adjacent space, taking 6d6 points of damage. From the creature’s perspective, the time shift is instantaneous. Any duration effects active upon the creature become suspended during the time shift, resuming when the creature reappears. Creatures that succeed at their saving throws cannot be affected by the same _fluxwraith_’s time shift ability for 24 hours. The save DC is Charisma-based.

##### Description

A _fluxwraith_ is an _incorporeal_ undead with a host of extraordinary powers owing to its singular _[[spells/Status|status]]_ as a time-displaced entity. Its serene appearance and dreamlike demeanor harken to its origins, for in life it slept away the centuries in a state of magical or technological stasis. Now, whether by accident or malign intent, the _fluxwraith_’s soul lies scattered across the timestream. Demented by its paradoxical consciousness, it yearns to destroy any living being audacious enough to exist within a single point of time.

Because its appearance depends upon its state when it first entered suspended animation, viewers may sometimes be able to deduce clues about its former life, as well as its motivations for entering hibernation. Some seek interminable sleep while they are in the prime of life, aiming to _[[spells/Awaken|awaken]]_ and embrace immortality as a perfect specimen, while others hope to defer a terminal diagnosis. However, the _[[feats/Sleeper|sleeper]]_’s motivations in life seldom define a _fluxwraith_’s outlook, as the process of becoming undead erases all but the most deeply ingrained mortal traits.

The first hint of the _fluxwraith_’s destructive nature manifests in the _[[items/Mundane/Caul|caul]]_ of energy that winks on and off around it. This ever-shifting network of temporal energy contains fragments of its consciousness, appearing as flickering aspects of itself as a youth, an adult, or a corpse. Scrutinizing these vignettes may provide further clues about the _fluxwraith_’s former existence, although any creature that enters the _fluxwraith_’s aura, or any creature affected by its attacks, may begin to see its own reflections appear within the shards as well. These disturbing images depict a creature not as it is, but as the _fluxwraith_ perceives it in the past or future.

Fluxwraiths tend to speak ancient or dead languages, often murmuring incomplete or garbled statements that _[[spells/Blend|blend]]_ past and future tenses in unsettling ways.
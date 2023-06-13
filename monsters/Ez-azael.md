---
cssclass: [monsters]
title1: Ez-azael
desc_short: This goat-like creature has a thick, snowy-white woolen coat. Its eyes
  gleam with a metallic golden sheen. Its hooves have sharpened, serrated edges and
  are soaked in blood. A single strand of scarlet thread is tangled between its curled
  ram horns.
title2: Ez-azael
CR: 12
sources:
- name: 'Pathfinder #107: Scourge of the Godclaw'
  page: 84
  link: http://paizo.com/products/btpy9n0j?Pathfinder-Adventure-Path-107-Scourge-of-the-Godclaw
XP: 19200
alignment: LG
size: Large
type: outsider
subtypes:
- good
- lawful
- native
initiative:
  bonus: 8
senses:
  darkvision: 60
  scent: true
  true seeing: true
AC:
  AC: 28
  touch: 14
  flat_footed: 23
  components:
    dex: 4
    dodge: 1
    natural: 14
    size: -1
HP:
  HP: 168
  long: 16d10+80
saves:
  fort: 15
  ref: 9
  will: 16
DR:
- amount: 10
  weakness: cold iron and evil
immunities:
- fire
- poison
- death effects
resistances:
  acid: 10
  cold: 10
  electricity: 10
SR: 23
speeds:
  base: 40
attacks:
  melee:
  - - text: slam +25 (2d6+10)
      entries:
      - - damage: 2d6+10
      attack: slam
      bonus:
      - 25
    - text: 2 hooves +20 (1d8+5 plus bleed)
      entries:
      - - damage: 1d8+5
        - effect: bleed
      count: 2
      attack: hooves
      bonus:
      - 20
  special:
  - bleed 1
  - fiendbane headbutt
  - smiting absolution
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: detect evil
    source: default
    freq: At will
  - name: light
    source: default
    freq: At will
  - name: protection from evil
    source: default
    freq: At will
  - name: virtue
    source: default
    freq: At will
  - name: break enchantment
    source: default
    freq: 3/day
  - name: dispel chaos
    source: default
    freq: 3/day
    DC: 21
  - name: dispel evil
    source: default
    freq: 3/day
    DC: 21
  - name: find the path
    source: default
    freq: 3/day
  - name: holy smite
    source: default
    freq: 3/day
    DC: 17
  - name: atonement
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 16
    concentration: 19
ability_scores:
  STR: 30
  DEX: 18
  CON: 20
  INT: 12
  WIS: 18
  CHA: 16
BAB: 16
CMB: 27
CMD: 42
CMD_other: 46 vs. trip
feats:
- name: Ability Focus (smiting absolution)
- name: Cleave
- name: Dodge
- name: Improved Initiative
- name: Iron Will
- name: Mobility
- name: Power Attack
- name: Spring Attack
skills:
  Acrobatics: 24
    when jumping: 28
  Climb: 18
  Intimidate: 22
  Knowledge (local): 20
  Knowledge (planes): 20
  Perception: 23
  Sense Motive: 23
  Survival: 23
  _racial_mods:
    Acrobatics:
      _: 4
      when jumping: 8
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Common
special_qualities:
- ritual of atonement
- sacrificial wound
- true resurrection
ecology:
  environment: any (Material Plane)
  organization: solitary
  treasure_type: none
special_abilities:
  Fiendbane Headbutt (Ex): An ez-azael's slam attack gains a +2 enhancement bonus
    on attack and damage rolls against outsiders with the evil subtype, and it deals
    an additional 2d6 points of damage to such targets.
  Ritual of Atonement (Su): |-
    An ez-azael can perform a ritual of atonement for a group of willing participants upon some high precipice. As a full-round action, it can unravel the scarlet thread from around its horns, allowing the thread to be grasped by up to 8 Medium or Small creatures (or 4 Large creatures or 16 Tiny creatures). Once the participants have all grasped the woolen strand, the ez-azael flings itself from the precipice to its death as a move action while the participants continue to hang on to the thread. The fall is always fatal to the ez-azael, and it cannot be saved by any means, magical or mundane. As the ez-azael falls, the thread breaks and the portion remaining in the participants' hands changes from scarlet to pure white. Those participants of a nonevil alignment who are holding the thread immediately receive the benefits of an atonement, a greater restoration, and a bless spell (with a duration of 24 hours).

    As an additional benefit of the atonement ritual, if the participants who grasp the thread are officially appointed representatives of a specific population (such as city leaders, high priests, heads of families, etc.), all members of the group they represent within a quarter mile of where the ritual occurs receive the above benefits.

    The effects granted by an ez-azael through this ritual never requires an expenditure of incense or other monetary offerings. The sacrifice of the ez-azael itself satisfies any such requirements.
  Sacrificial Wound (Su): Once per day as an immediate action, an ez-azael can convert
    hit point damage it takes from any single attack into a boost for its allies.
    The ez-azael takes the full amount of damage (even if such damage would kill the
    ez-azael), but any allies within 60 feet receive a number of temporary hit points
    equal to half of the amount of damage the ez-azael sustained (rounded down). These
    temporary hit points last for 1 hour. The number of temporary hit points a recipient
    gains through the use of this ability can't exceed double its normal maximum hit
    points.
  Smiting Absolution (Su): As a standard action once every 1d4 rounds, an ez-azael
    can cause its golden eyes to flash with an almost blinding light that affects
    all evil creatures within a 40-foot radius centered on the ez-azael. The purifying
    rays of this light affect evil creatures differently according to their alignments
    if they fail a DC 23 Will saving throw. Chaotic evil creatures that fail the save
    are paralyzed for 1d10 rounds, neutral evil creatures are stunned for 1d4 rounds,
    and lawful evil creatures are confused for 1d4 rounds. Sinspawn (Pathfinder RPG
    Bestiary 2 246) are destroyed on a failed save. The save DC is Charisma-based
    with a +2 bonus from Ability Focus.
  True Resurrection (Su): An ez-azael can, as a standard action, give up its own life
    in order to cast a true resurrection spell on one target of its choice. Alternately,
    an ez-azael can use this ability to cast destruction on one evil target within
    60 feet. This use of the spell deals 160 points of damage to the target unless
    it succeeds at a DC 22 Fortitude saving throw, in which case it deals only 10d6
    points of damage. In either use of this ability, the ez-azael is utterly destroyed,
    having fulfilled its purpose for existence. The save DC is Wisdom-based.
desc_long: The ways of Heaven are often unknown or opaque in purpose and meaning to
  mortals, and the ritual of the ez-azael is no exception. In the eternal battle between
  the powers of good and evil, powerful angelic beings occasionally capture a type
  of goat-like demon called a schir (Pathfinder RPG Bestiary 3 74) and subject it
  to a powerful cleansing ritual in which it is used as an offering of atonement for
  some mortal population to relieve them of both the physical and spiritual burdens
  of their sins or other acts of moral error they have committed. Upon the ritual's
  completion, the mortal population receives absolution and the schir is released
  to wander free with its new burden of forgiven mortal sin. Almost invariably, these
  demons die from the trauma of being used as a vessel for divine mercy. However,
  sometimes the ritual of clemency changes the schir in a fundamental way, in which
  case it transforms into an ez-azael.

---

# Ez-azael
This goat-like creature has a thick, snowy-white woolen coat. Its eyes gleam with a metallic golden sheen. Its hooves have sharpened, serrated edges and are soaked in blood. A single strand of scarlet thread is tangled between its curled ram horns.
**Source** Pathfinder #107: Scourge of the Godclaw pg. 84
**XP** 19,200

LG Large outsider (good, lawful, native)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_, _[[spells/True Seeing|true seeing]]_; Perception +23

##### Defense

**AC** 28, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+4 Dex, +1 dodge, +14 natural, –1 size)
**hp** 168 (16d10+80)
**Fort** +15, **Ref** +9, **Will** +16
**DR** 10/cold iron and evil; **Immune** fire, poison, death effects; **Resist** acid 10, cold 10, electricity 10; **SR** 23

##### Offense
**Speed** 40 ft.
**Melee** slam +25 (2d6+10), 2 hooves +20 (1d8+5 plus _[[universal monster rules/Bleed|bleed]]_)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** _bleed_ 1, fiendbane headbutt, smiting _[[spells/Absolution|absolution]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +19)
Constant—_true seeing_
At will—_[[spells/Detect Evil|detect evil]]_, light, _[[spells/Protection From Evil|protection from evil]]_, _[[spells/Virtue|virtue]]_
3/day—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Dispel Chaos|dispel chaos]]_ (DC 21), _[[spells/Dispel Evil|dispel evil]]_ (DC 21), _[[spells/Find the Path|find the path]]_, _[[spells/Holy Smite|holy smite]]_ (DC 17)
1/day—_[[spells/Atonement|atonement]]_

##### Statistics
**Str** 30, **Dex** 18, **Con** 20, **Int** 12, **Wis** 18, **Cha** 16
**Base Atk** +16; **CMB** +27; **CMD** 42 (46 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (smiting _absolution_), _[[feats/Cleave|Cleave]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spring Attack|Spring Attack]]_
**Skills** Acrobatics +24 (+28 when jumping), _[[universal monster rules/Climb|Climb]]_ +18, Intimidate +22, Knowledge (local) +20, Knowledge (planes) +20, Perception +23, Sense Motive +23, Survival +23; **Racial Modifiers** +4 Acrobatics (+8 when jumping), +8 Perception
**Languages** Abyssal, Celestial, Common
**SQ** ritual of _atonement_, sacrificial wound, _[[spells/True Resurrection|true resurrection]]_

##### Ecology

**Environment** any (Material Plane)
**Organization** solitary
**Treasure** none

### Special Abilities

**Fiendbane Headbutt (Ex)** An _[[monsters/Ez-azael|ez-azael]]_’s slam attack gains a +2 enhancement bonus on attack and damage rolls against outsiders with the evil subtype, and it deals an additional 2d6 points of damage to such targets.

**Ritual of _Atonement_ (Su)** An _ez-azael_ can perform a ritual of _atonement_ for a group of willing participants upon some high precipice. As a full-round action, it can unravel the scarlet thread from around its horns, allowing the thread to be grasped by up to 8 _[[classes/Medium|Medium]]_ or Small creatures (or 4 Large creatures or 16 Tiny creatures). Once the participants have all grasped the woolen strand, the _ez-azael_ flings itself from the precipice to its death as a move action while the participants continue to hang on to the thread. The fall is always fatal to the _ez-azael_, and it cannot be saved by any means, magical or mundane. As the _ez-azael_ falls, the thread breaks and the portion remaining in the participants’ hands changes from scarlet to pure white. Those participants of a nonevil alignment who are holding the thread immediately receive the benefits of an _atonement_, a greater _[[spells/Restoration|restoration]]_, and a _[[spells/Bless|bless]]_ spell (with a duration of 24 hours).

As an additional benefit of the _atonement_ ritual, if the participants who _[[spells/Grasp|grasp]]_ the thread are officially appointed representatives of a specific population (such as city leaders, high priests, heads of families, etc.), all members of the group they represent within a quarter mile of where the ritual occurs receive the above benefits.

The effects granted by an _ez-azael_ through this ritual never requires an expenditure of _[[items/Mundane/Incense|incense]]_ or other monetary offerings. The _[[spells/Sacrifice|sacrifice]]_ of the _ez-azael_ itself satisfies any such requirements.
**Sacrificial Wound (Su)** Once per day as an immediate action, an _ez-azael_ can convert hit point damage it takes from any single attack into a boost for its allies. The _ez-azael_ takes the full amount of damage (even if such damage would kill the _ez-azael_), but any allies within 60 feet receive a number of temporary hit points equal to half of the amount of damage the _ez-azael_ sustained (rounded down). These temporary hit points last for 1 hour. The number of temporary hit points a recipient gains through the use of this ability can’t exceed double its normal maximum hit points.
**Smiting _Absolution_ (Su)** As a standard action once every 1d4 rounds, an _ez-azael_ can cause its golden eyes to flash with an almost _[[feats/Blinding Light|blinding light]]_ that affects all evil creatures within a 40-foot radius centered on the _ez-azael_. The purifying rays of this light affect evil creatures differently according to their alignments if they fail a DC 23 Will saving throw. Chaotic evil creatures that fail the save are _[[conditions/Paralyzed|paralyzed]]_ for 1d10 rounds, neutral evil creatures are _[[conditions/Stunned|stunned]]_ for 1d4 rounds, and lawful evil creatures are _[[conditions/Confused|confused]]_ for 1d4 rounds. _[[monsters/Sinspawn|Sinspawn]]_ (Pathfinder RPG Bestiary 2 246) are destroyed on a failed save. The save DC is Charisma-based with a +2 bonus from _Ability Focus_.

**_True Resurrection_ (Su)** An _ez-azael_ can, as a standard action, give up its own life in order to cast a _true resurrection_ spell on one target of its choice. Alternately, an _ez-azael_ can use this ability to cast _[[spells/Destruction|destruction]]_ on one evil target within 60 feet. This use of the spell deals 160 points of damage to the target unless it succeeds at a DC 22 Fortitude saving throw, in which case it deals only 10d6 points of damage. In either use of this ability, the _ez-azael_ is utterly destroyed, having fulfilled its purpose for existence. The save DC is Wisdom-based.

##### Description

The ways of Heaven are often _[[monsters/Unknown|unknown]]_ or opaque in purpose and meaning to mortals, and the ritual of the _ez-azael_ is no exception. In the eternal battle between the powers of good and evil, powerful angelic beings occasionally capture a type of goat-like demon _[[items/Weapon Magic Abilities/Called|called]]_ a schir (Pathfinder RPG Bestiary 3 74) and subject it to a powerful cleansing ritual in which it is used as an offering of _atonement_ for some mortal population to relieve them of both the physical and spiritual burdens of their sins or other acts of moral error they have committed. Upon the ritual’s completion, the mortal population receives _absolution_ and the schir is released to wander free with its new burden of forgiven mortal sin. Almost invariably, these demons die from the trauma of being used as a vessel for divine mercy. However, sometimes the ritual of clemency changes the schir in a fundamental way, in which case it transforms into an _ez-azael_.
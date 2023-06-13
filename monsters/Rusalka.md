---
cssclass: [monsters]
title1: Rusalka
desc_short: This beguiling female figure is partly obscured by long flowing hair that
  dances and flows around her as if she were underwater.
title2: Rusalka
CR: 12
sources:
- name: Bestiary 3
  page: 232
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 19200
alignment: NE
size: Medium
type: fey
subtypes:
- aquatic
initiative:
  bonus: 10
senses:
  low-light vision: true
AC:
  AC: 25
  touch: 17
  flat_footed: 18
  components:
    dex: 6
    dodge: 1
    natural: 8
HP:
  HP: 150
  long: 20d6+80
saves:
  fort: 12
  ref: 18
  will: 15
DR:
- amount: 15
  weakness: cold iron
immunities:
- fire
SR: 23
speeds:
  base: 30
  swim: 60
attacks:
  melee:
  - - text: staggering touch +16 (stagger)
      entries:
      - - effect: stagger
      attack: staggering touch
      bonus:
      - 16
    - text: 4 tresses +16 (2d6+5 plus grab)
      entries:
      - - damage: 2d6+5
        - effect: grab
      count: 4
      attack: tresses
      bonus:
      - 16
  special:
  - beckoning call
  - constrict (2d6+7)
  - tresses
space: 5
reach: 5
reach_other: 15 ft. with tresses
spell_like_abilities:
  entries:
  - name: blur
    source: default
    freq: Constant
  - name: water walk
    source: default
    freq: Constant
  - name: entangle
    source: default
    freq: At will
    DC: 18
  - name: fog cloud
    source: default
    freq: At will
  - name: invisibility
    source: default
    freq: At will
  - name: quickened charm monster
    source: default
    freq: 3/day
    DC: 21
  - name: control water
    source: default
    freq: 3/day
  - name: summon nature's ally VI
    source: default
    freq: 1/day
    other: water elementals only
  sources:
  - name: default
    CL: 20
    concentration: 27
ability_scores:
  STR: 20
  DEX: 23
  CON: 19
  INT: 12
  WIS: 13
  CHA: 24
BAB: 10
CMB: 16
CMB_other: +23 tresses, +27 grapple with tresses
CMD: 32
feats:
- name: Agile Maneuvers
- name: Combat Reflexes
- name: Dodge
- name: Great Fortitude
- name: Improved Initiative
- name: Iron Will
- name: Quicken Spell-Like Ability (charm monster)
- name: Skill Focus (Perception)
- name: Skill Focus (Stealth)
- name: Weapon Finesse
skills:
  Acrobatics: 14
  Bluff: 24
  Diplomacy: 15
  Escape Artist: 18
  Knowledge (arcana): 6
  Knowledge (nature): 18
  Perception: 22
  Perform (dance): 14
  Perform (sing): 27
  Sense Motive: 15
  Spellcraft: 18
  Stealth: 27
  Swim: 31
languages:
- Common
- Sylvan
special_qualities:
- amphibious
ecology:
  environment: any water
  organization: solitary, pair, or eddy (3-6)
  treasure_type: standard
special_abilities:
  Beckoning Call (Su): As a standard action, a rusalka can sing or speak, causing
    all non-fey creatures within a 300-foot spread to approach its position as if
    compelled to do so via a suggestion spell (DC 27 Will negates). A creature that
    successfully saves is not subject to the same rusalka's beckoning call for 24
    hours. When an affected creature begins its turn adjacent to the rusalka, it is
    dazed for that round. These effects continue as long as the rusalka takes a standard
    action to maintain the effect, plus 1 additional round. This is a sonic mind-affecting
    effect. The save DC is Charisma-based.
  Staggering Touch (Su): A creature touched by a rusalka must make a DC 27 Fortitude
    save or be staggered for 1 round by overwhelming feelings of desire and shame.
    This is a mind-affecting effect. The save DC is Charisma-based.
  Tresses (Su): A rusalka's long hair is strong and capable of making powerful primary
    natural attacks. When it uses its tresses to grapple an opponent, a rusalka does
    not gain the grappled condition itself. In addition, a rusalka uses its Charisma
    modifier in addition to its Strength modifier for all combat maneuver checks made
    with its tresses.
desc_long: Rusalkas are cruel and bitter fey who inhabit waterways near humanoid settlements.
  Although rusalkas are not undead, some persist in believing that these fey form
  from the spirits of those who met a sinister end in the water. Rusalkas do little
  to dissuade such rumors. Rusalkas are fond of keeping a few charmed monsters or
  powerful humanoids nearby to aid in their defense or for other forms of cruel and
  humiliating entertainment, but quickly grow bored with such pets. When this occurs,
  rusalkas generally murder the creatures and seek more interesting replacement pets.

---

# Rusalka
This beguiling female figure is partly obscured by long flowing hair that dances and flows around her as if she were _[[items/Weapon Magic Abilities/Underwater|underwater]]_.
**Source** Bestiary 3 pg. 232
**XP** 19,200

NE Medium fey (aquatic)
**Init** +10; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +22

##### Defense

**AC** 25, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+6 Dex, +1 _[[feats/Dodge|dodge]]_, +8 natural)
**hp** 150 (20d6+80)
**Fort** +12, **Ref** +18, **Will** +15
**DR** 15/cold iron; **Immune** fire; **SR** 23

##### Offense
**Speed** 30 ft., swim 60 ft.
**Melee** staggering touch +16 (stagger), 4 tresses +16 (2d6+5 plus _[[universal monster rules/Grab|grab]]_)
**Space** 5 ft., **Reach** 5 ft. (15 ft. with tresses)
**Special Attacks** beckoning call, _[[universal monster rules/Constrict|constrict]]_ (2d6+7), tresses
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +27)
Constant—_[[spells/Blur|blur]]_, _[[spells/Water Walk|water walk]]_
At will—_[[spells/Entangle|entangle]]_ (DC 18), _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Invisibility|invisibility]]_
3/day—quickened _[[spells/Charm Monster|charm monster]]_ (DC 21), _[[spells/Control Water|control water]]_
1/day—_[[universal monster rules/Summon|summon]]_ nature’s ally VI (water elementals only)

##### Statistics
**Str** 20, **Dex** 23, **Con** 19, **Int** 12, **Wis** 13, **Cha** 24
**Base Atk** +10; **CMB** +16 (+23 tresses, +27 grapple with tresses); **CMD** 32
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_charm monster_), _[[feats/Skill Focus|Skill Focus]]_ (Perception), _Skill Focus_ (Stealth), _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +14, Bluff +24, Diplomacy +15, Escape Artist +18, Knowledge (arcana) +6, Knowledge (nature) +18, Perception +22, Perform (dance) +14, Perform (sing) +27, Sense Motive +15, Spellcraft +18, Stealth +27, Swim +31
**Languages** Common, Sylvan
**SQ** _[[universal monster rules/Amphibious|amphibious]]_

##### Ecology

**Environment** any water
**Organization** solitary, pair, or eddy (3–6)
**Treasure** standard

### Special Abilities

**Beckoning Call (Su)** As a standard action, a _[[monsters/Rusalka|rusalka]]_ can sing or speak, causing all non-fey creatures within a 300-foot spread to approach its position as if compelled to do so via a _[[spells/Suggestion|suggestion]]_ spell (DC 27 Will negates). A creature that successfully saves is not subject to the same _rusalka_’s beckoning call for 24 hours. When an affected creature begins its turn adjacent to the _rusalka_, it is _[[conditions/Dazed|dazed]]_ for that round. These effects continue as long as the _rusalka_ takes a standard action to maintain the effect, plus 1 additional round. This is a sonic mind-affecting effect. The save DC is Charisma-based.
**Staggering Touch (Su)** A creature touched by a _rusalka_ must make a DC 27 Fortitude save or be _[[conditions/Staggered|staggered]]_ for 1 round by overwhelming feelings of desire and shame. This is a mind-affecting effect. The save DC is Charisma-based.

**Tresses (Su)** A _rusalka_’s long hair is strong and capable of making powerful primary _[[universal monster rules/Natural Attacks|natural attacks]]_. When it uses its tresses to grapple an opponent, a _rusalka_ does not gain the _[[conditions/Grappled|grappled]]_ condition itself. In addition, a _rusalka_ uses its Charisma modifier in addition to its Strength modifier for all combat maneuver checks made with its tresses.

##### Description

Rusalkas are _[[items/Weapon Magic Abilities/Cruel|cruel]]_ and _[[items/Armor Magic Abilities/Bitter|bitter]]_ fey who inhabit waterways near humanoid settlements. Although rusalkas are not undead, some persist in believing that these fey form from the spirits of those who met a sinister end in the water. Rusalkas do little to dissuade such rumors. Rusalkas are fond of keeping a few charmed monsters or powerful humanoids nearby to aid in their defense or for other forms of _cruel_ and humiliating entertainment, but quickly grow bored with such pets. When this occurs, rusalkas generally murder the creatures and seek more interesting replacement pets.
---
cssclass: [monsters]
title1: Demon, Seraptis
desc_short: This woman's flesh is pale and clammy, as if her body had been drained
  of blood from the fanged slashes on her four arms.
title2: Seraptis
CR: 15
sources:
- name: Bestiary 5
  page: 76
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
- name: 'Book of the Damned - Volume 2: Lords of Chaos'
  page: 58
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderChronicles/v5748btpy8hij
XP: 51200
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 10
senses:
  darkvision: 60
  deathwatch: true
  true seeing: true
auras:
- name: gaze of despair
  radius: 30
  DC: 22
- name: unholy aura
  DC: 23
AC:
  AC: 30
  touch: 20
  flat_footed: 24
  components:
    deflection: 4
    dex: 6
    natural: 10
HP:
  HP: 217
  long: 15d10+135
  other: blood healing
saves:
  fort: 22
  ref: 15
  will: 17
DR:
- amount: 10
  weakness: cold iron and good
immunities:
- bleed
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 26
speeds:
  base: 50
attacks:
  melee:
  - - text: +3 wounding scimitar +27/+22/+17 (1d6+11/15-20)
      entries:
      - - damage: 1d6+11
          crit_range: 15-20
      attack: +3 wounding scimitar
      bonus:
      - 27
      - 22
      - 17
    - text: 3 claws +21 (1d6+4 plus grab)
      entries:
      - - damage: 1d6+4
        - effect: grab
      count: 3
      attack: claws
      bonus:
      - 21
    - text: gore +21 (2d6+4)
      entries:
      - - damage: 2d6+4
      attack: gore
      bonus:
      - 21
  - - text: 4 claws +23 (1d6+8 plus grab)
      entries:
      - - damage: 1d6+8
        - effect: grab
      count: 4
      attack: claws
      bonus:
      - 23
    - text: gore +23 (2d6+8)
      entries:
      - - damage: 2d6+8
      attack: gore
      bonus:
      - 23
  special:
  - compelling domination
  - constrict (4d6+12 plus 2d6 bleed and 1d4 Strength drain)
  - multi-arm grab
spell_like_abilities:
  entries:
  - name: deathwatch
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 23
  - name: crushing despair
    source: default
    freq: At will
    DC: 18
  - name: dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: telekinesis
    source: default
    freq: At will
    DC: 20
  - name: confusion
    source: default
    freq: 3/day
    DC: 19
  - name: demand
    source: default
    freq: 3/day
    DC: 23
  - name: dominate person
    source: default
    freq: 3/day
    DC: 19
  - name: fly
    source: default
    freq: 3/day
  - name: symbol of insanity
    source: default
    freq: 1/day
    DC: 23
  - name: summon
    source: default
    freq: 1/day
    level: 5
    summons:
    - name: seraptis
      amount: 1
      chance: 20%
    - name: glabrezu
      amount: 1
      chance: 40%
  sources:
  - name: default
    CL: 15
    concentration: 20
ability_scores:
  STR: 26
  DEX: 23
  CON: 28
  INT: 16
  WIS: 19
  CHA: 21
BAB: 15
CMB: 21
CMB_other: +25 grapple
CMD: 41
feats:
- name: Bleeding Critical
- name: Combat Reflexes
- name: Critical Focus
- name: Improved Critical (scimitar)
- name: Improved Initiative
- name: Multiattack
- name: Power Attack
- name: Weapon Focus (scimitar)
skills:
  Acrobatics: 24
    when jumping: 32
  Bluff: 23
  Fly: 24
  Intimidate: 23
  Knowledge (planes): 21
  Knowledge (religion): 21
  Perception: 30
  Sense Motive: 22
  Stealth: 24
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
ecology:
  environment: any (Abyss)
  organization: solitary or cult (1 plus 2-6 succubi)
  treasure_type: double
  treasure:
  - +3 wounding scimitar
  - other
special_abilities:
  Blood Healing (Su): Whenever a creature within 30 feet of a seraptis takes bleed
    damage caused by that seraptis, the blood flows through the air into the seraptis's
    maw, and the seraptis heals an equal amount of damage.
  Compelling Domination (Su): When a seraptis uses dominate person, its victims do
    not actively resist and never gain a new saving throw when ordered to take actions
    against their nature.
  Gaze of Despair (Su): Creatures within 30 feet of a seraptis that fail a DC 22 Will
    save take 1d6 points of Charisma drain and are staggered for 1d6 rounds. If the
    Charisma drain would reduce a creature's Charisma to 0, that creature instead
    succumbs to overwhelming suicidal urges and attempts to end its life by the most
    convenient method at hand, subject to the GM's discretion. The creature remains
    in that state until its Charisma is restored to its normal maximum-otherwise,
    the victim must be restrained at all times to prevent further suicide attempts.
    This is a mind-affecting effect. The save DC is Charisma-based.
  Multi-Arm Grab (Ex): When a seraptis successfully grabs a creature, the maws on
    her arms begin to gnaw on it. This ability functions as constrict, except the
    damage type is bludgeoning, piercing, and slashing. A seraptis gains a cumulative
    +4 bonus on grapple attempts with her grab ability for each successive claw attack
    after the first that hits a given target that round.
desc_long: Seraptis demons form from souls of those who inspired widespread despair
  or destruction by committing suicide.

---

# Demon, Seraptis
This woman’s flesh is pale and clammy, as if her body had been drained of blood from the fanged slashes on her four arms.
**Source** Bestiary 5 pg. 76, _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_ - Volume 2: Lords of Chaos pg. 58
**XP** 51,200
CE Medium outsider (chaotic, demon, evil, extraplanar)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Deathwatch|deathwatch]]_, _[[spells/True Seeing|true seeing]]_; Perception +30
**Aura** _[[universal monster rules/Gaze|gaze]]_ of despair (30 ft., DC 22), _[[spells/Unholy Aura|unholy aura]]_ (DC 23)

##### Defense

**AC** 30, touch 20, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+4 _[[spells/Deflection|deflection]]_, +6 Dex, +10 natural)
**hp** 217 (15d10+135); blood healing
**Fort** +22, **Ref** +15, **Will** +17
**DR** 10/cold iron and good; **Immune** _[[universal monster rules/Bleed|bleed]]_, electricity, poison; **Resist** acid 10, cold 10, fire 10; **SR** 26

##### Offense
**Speed** 50 ft.
**Melee** +3 _[[items/Weapon Magic Abilities/Wounding|wounding]]_ _[[items/Weapon/Scimitar|scimitar]]_ +27/+22/+17 (1d6+11/15-20), 3 claws +21 (1d6+4 plus _[[universal monster rules/Grab|grab]]_), gore +21 (2d6+4) or 4 claws +23 (1d6+8 plus _grab_), gore +23 (2d6+8)
**Special Attacks** compelling domination, _[[universal monster rules/Constrict|constrict]]_ (4d6+12 plus 2d6 _bleed_ and 1d4 Strength drain), multi-arm _grab_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +20)
Constant—_deathwatch_, _true seeing_, _unholy aura_ (DC 23) 
At will—_[[spells/Crushing Despair|crushing despair]]_ (DC 18), _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport (self plus 50 lbs. of objects only), _[[spells/Telekinesis|telekinesis]]_ (DC 20) 
3/day—_[[spells/Confusion|confusion]]_ (DC 19), _[[spells/Demand|demand]]_ (DC 23), _[[spells/Dominate Person|dominate person]]_ (DC 19), fly 
1/day—_[[spells/Symbol of Insanity|symbol of insanity]]_ (DC 23), _[[universal monster rules/Summon|summon]]_ (level 5, 1 seraptis 20% or 1 glabrezu 40%)

##### Statistics
**Str** 26, **Dex** 23, **Con** 28, **Int** 16, **Wis** 19, **Cha** 21
**Base Atk** +15; **CMB** +21 (+25 grapple); **CMD** 41
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (_scimitar_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_scimitar_)
**Skills** Acrobatics +24 (+32 when jumping), Bluff +23, Fly +24, Intimidate +23, Knowledge (planes) +21, Knowledge (religion) +21, Perception +30, Sense Motive +22, Stealth +24; **Racial Modifiers** +8 Perception
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abyss)
**Organization** solitary or cult (1 plus 2-6 succubi)
**Treasure** double (+3 _wounding_ _scimitar_, other)

### Special Abilities

**Blood Healing (Su)** Whenever a creature within 30 feet of a seraptis takes _bleed_ damage caused by that seraptis, the blood flows through the air into the seraptis’s maw, and the seraptis heals an equal amount of damage.

**Compelling Domination (Su)** When a seraptis uses _dominate person_, its victims do not actively resist and never gain a new saving throw when ordered to take actions against their nature.

**_Gaze_ of Despair (Su)** Creatures within 30 feet of a seraptis that fail a DC 22 Will save take 1d6 points of Charisma drain and are _[[conditions/Staggered|staggered]]_ for 1d6 rounds. If the Charisma drain would reduce a creature’s Charisma to 0, that creature instead succumbs to overwhelming suicidal urges and attempts to end its life by the most convenient method at hand, subject to the GM’s discretion. The creature remains in that state until its Charisma is restored to its normal maximum—otherwise, the victim must be restrained at all times to prevent further suicide attempts. This is a mind-affecting effect. The save DC is Charisma-based.

**Multi-Arm _Grab_ (Ex)** When a seraptis successfully grabs a creature, the maws on her arms begin to gnaw on it. This ability functions as _constrict_, except the damage type is bludgeoning, piercing, and slashing. A seraptis gains a cumulative +4 bonus on grapple attempts with her _grab_ ability for each successive claw attack after the first that hits a given target that round.

##### Description

Seraptis demons form from souls of those who _[[items/Weapon Magic Abilities/Inspired|inspired]]_ widespread despair or _[[spells/Destruction|destruction]]_ by committing suicide.
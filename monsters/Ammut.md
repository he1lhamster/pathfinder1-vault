---
cssclass: [monsters]
title1: Ammut
desc_short: This massive creature has the head of a crocodile, the mane and torso
  of a lion, and the hindquarters of a hippopotamus. The wickedly curved claws on
  the creature's forepaws pale in comparison to the danger of its mighty jaws.
title2: Ammut
CR: 18
sources:
- name: 'Pathfinder #84: Pyramid of the Sky Pharaoh'
  page: 82
  link: http://paizo.com/products/btpy97av?Pathfinder-Adventure-Path-84-Pyramid-of-the-Sky-Pharaoh
XP: 153600
alignment: LE
size: Huge
type: outsider
subtypes:
- evil
- native
initiative:
  bonus: 10
senses:
  darkvision: 60
  scent: true
  tremorsense: 60
  true seeing: true
auras:
- name: fear aura
  radius: 30
  DC: 29
AC:
  AC: 34
  touch: 14
  flat_footed: 28
  components:
    dex: 6
    natural: 20
    size: -2
HP:
  HP: 290
  long: 20d10+180
saves:
  fort: 21
  ref: 20
  will: 13
DR:
- amount: 15
  weakness: good and slashing
immunities:
- disease
- exhaustion
- fatigue
- fire
- poison
resistances:
  acid: 10
  cold: 10
  electricity: 10
SR: 29
speeds:
  base: 40
attacks:
  melee:
  - - text: bite +31 (4d6+19/19-20 plus grab)
      entries:
      - - damage: 4d6+19
          crit_range: 19-20
        - effect: grab
      attack: bite
      bonus:
      - 31
    - text: 2 claws +31 (2d6+13)
      entries:
      - - damage: 2d6+13
      count: 2
      attack: claws
      bonus:
      - 31
  special:
  - breath weapon (30-ft. cone, 14d6 fire damage, Reflex DC 29 half, usable every
    1d4 rounds)
  - devour soul
  - powerful jaw
  - swallow whole (3d6+13 bludgeoning plus 4d6 fire plus wasting curse, AC 20, 29
    hp)
  - wasting curse
space: 15
reach: 10
reach_other: 15 ft. with bite
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: detect good
    source: default
    freq: Constant
  - name: detect chaos
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - superscripts:
    - UM
    name: quickened ear-piercing scream
    source: default
    freq: 3/day
    DC: 20
  - name: dominate monster
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 14
    concentration: 23
ability_scores:
  STR: 36
  DEX: 22
  CON: 29
  INT: 11
  WIS: 24
  CHA: 29
BAB: 20
CMB: 35
CMB_other: +37 bull rush
CMD: 51
CMD_other: 53 vs. bull rush, 55 vs. trip
feats:
- name: Blind-Fight
- name: Critical Focus
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Lunge
- name: Power Attack
- is_bonus: true
  name: Quicken Spell-Like Ability (ear-piercing scream)
- name: Staggering Critical
skills:
  Climb: 24
  Intimidate: 30
  Knowledge (planes): 20
  Knowledge (religion): 20
  Perception: 30
  Sense Motive: 30
  Stealth: 21
languages:
- Celestial
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Osirion)
  organization: solitary
  treasure_type: none
special_abilities:
  Devour Soul (Su): If a creature dies while swallowed whole by an ammut, its soul
    is consumed along with its body. A creature killed in this way cannot be brought
    back to life via any effect short of true resurrection, miracle, or wish, but
    even these spells require the caster to succeed at a caster level check equal
    to 10 + the targeted creature's Hit Dice. If this check fails, the caster can't
    attempt to return the targeted creature to life for the next 24 hours (though
    the caster can try again after this period).
  Powerful Jaw (Ex): An ammut's bite attack deals 4d6 points of damage plus one and
    a half times its Strength bonus. In addition, its reach with this attack is 5
    feet further than normal and it gains the grab ability when attacking with its
    bite.
  Swallow Whole (Ex): An ammut can swallow creatures size Large or smaller with this
    special ability, and can only swallow one creature at a time regardless of the
    creature's size. In addition, creatures swallowed by an ammut are subject to its
    wasting curse.
  Wasting Curse (Su): Swallow whole-contact; save Will DC 29; frequency 1 hour; effect
    1d4 Cha drain. A creature whose Charisma score is reduced to 0 by this wasting
    curse dies; its body is destroyed and it is subject to the ammut's devour soul
    ability as if it had died while within the ammut's gut. The save DC is Charisma-based.
desc_long: Ammuts are beastly but cunning creatures that consume souls in an attempt
  to satisfy their insatiable hungers. Few ammuts exist, and those that do wander
  the vast deserts of Osirion preying on the souls of any creature they can catch.
  These creatures prefer the taste of thoroughly evil souls or those who have experienced
  full and complex lives. Ammuts show disdain for creatures of inferior intelligence,
  but also tend to leave them alone, as they claim their souls are shallow and flavorless.
  The rarity of ammuts and their nomadic nature makes it difficult to determine how
  long they live, or even if they age at all. Ammuts are approximately 20 feet long
  and 9 feet tall at the shoulder. Their rounded and muscular hindquarters makes them
  denser than would be expected for their size, and ammuts can weigh up to 10 tons.

---

# Ammut
This massive creature has the head of a _[[monsters/Crocodile|crocodile]]_, the mane and torso of a _[[monsters/Lion|lion]]_, and the hindquarters of a _[[monsters/Hippopotamus|hippopotamus]]_. The wickedly curved claws on the creature’s forepaws pale in comparison to the danger of its mighty jaws.
**Source** Pathfinder #84: Pyramid of the Sky Pharaoh pg. 82
**XP** 153,600

LE Huge outsider (evil, native)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +30
**Aura** _[[universal monster rules/Fear|fear]]_ aura (30 ft., DC 29)

##### Defense

**AC** 34, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+6 Dex, +20 natural, –2 size)
**hp** 290 (20d10+180)
**Fort** +21, **Ref** +20, **Will** +13
**DR** 15/good and slashing; **Immune** disease, exhaustion, fatigue, fire, poison; **Resist** acid 10, cold 10, electricity 10; **SR** 29

##### Offense
**Speed** 40 ft.
**Melee** bite +31 (4d6+19/19–20 plus _[[universal monster rules/Grab|grab]]_), 2 claws +31 (2d6+13)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (30-ft. cone, 14d6 fire damage, Reflex DC 29 half, usable every 1d4 rounds), devour soul, powerful jaw, _[[universal monster rules/Swallow Whole|swallow whole]]_ (3d6+13 bludgeoning plus 4d6 fire plus wasting curse, AC 20, 29 hp), wasting curse
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +23)
Constant—_[[spells/Detect Evil|detect evil]]_, _[[spells/Detect Good|detect good]]_, _[[spells/Detect Chaos|detect chaos]]_, _true seeing_
3/day—quickened _[[spells/Ear-Piercing Scream|ear-piercing scream]]_ (DC 20)
1/day—_[[spells/Dominate Monster|dominate monster]]_

##### Statistics
**Str** 36, **Dex** 22, **Con** 29, **Int** 11, **Wis** 24, **Cha** 29
**Base Atk** +20; **CMB** +35 (+37 bull rush); **CMD** 51 (53 vs. bull rush, 55 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_ear-piercing scream_), _[[feats/Staggering Critical|Staggering Critical]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +24, Intimidate +30, Knowledge (planes) +20, Knowledge (religion) +20, Perception +30, Sense Motive +30, Stealth +21
**Languages** Celestial, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Osirion)
**Organization** solitary
**Treasure** none

### Special Abilities

**Devour Soul (Su)** If a creature dies while swallowed whole by an _[[monsters/Ammut|ammut]]_, its soul is consumed along with its body. A creature killed in this way cannot be brought back to life via any effect short of _[[spells/True Resurrection|true resurrection]]_, _[[spells/Miracle|miracle]]_, or _[[spells/Wish|wish]]_, but even these spells require the caster to succeed at a caster level check equal to 10 + the targeted creature’s Hit Dice. If this check fails, the caster can’t attempt to return the targeted creature to life for the next 24 hours (though the caster can try again after this period).

**Powerful Jaw (Ex)** An _ammut_’s bite attack deals 4d6 points of damage plus one and a half times its Strength bonus. In addition, its reach with this attack is 5 feet further than normal and it gains the _grab_ ability when attacking with its bite.
**_Swallow Whole_ (Ex)** An _ammut_ can swallow creatures size Large or smaller with this special ability, and can only swallow one creature at a time regardless of the creature’s size. In addition, creatures swallowed by an _ammut_ are subject to its wasting curse.

**Wasting Curse (Su)** _Swallow whole_—contact; save Will DC 29; frequency 1 hour; effect 1d4 Cha drain. A creature whose Charisma score is reduced to 0 by this wasting curse dies; its body is destroyed and it is subject to the _ammut_’s devour soul ability as if it had died while within the _ammut_’s gut. The save DC is Charisma-based.

##### Description

Ammuts are beastly but _[[items/Weapon Magic Abilities/Cunning|cunning]]_ creatures that consume souls in an attempt to satisfy their insatiable hungers. Few ammuts exist, and those that do wander the vast deserts of Osirion preying on the souls of any creature they can catch. These creatures prefer the taste of thoroughly evil souls or those who have experienced full and complex lives. Ammuts show disdain for creatures of inferior intelligence, but also tend to leave them alone, as they claim their souls are shallow and flavorless. The rarity of ammuts and their nomadic nature makes it difficult to determine how long they live, or even if they age at all. Ammuts are approximately 20 feet long and 9 feet tall at the shoulder. Their rounded and muscular hindquarters makes them denser than would be expected for their size, and ammuts can weigh up to 10 tons.
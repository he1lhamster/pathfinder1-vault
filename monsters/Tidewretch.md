---
cssclass: [monsters]
title1: Tidewretch
desc_short: This ancient, empty-eyed woman appears to have flesh made from damp, rotting
  wood, and sparse clumps of seaweed serve as her hair.
title2: Tidewretch
CR: 6
sources:
- name: 'Pathfinder #122: Into the Shattered Continent'
  page: 90
  link: http://paizo.com/products/btpy9uk0?Pathfinder-Adventure-Path-122-Into-the-Shattered-Continent
XP: 2400
alignment: NE
size: Medium
type: undead
initiative:
  bonus: 6
senses:
  darkvision: 60
AC:
  AC: 19
  touch: 13
  flat_footed: 16
  components:
    dex: 2
    dodge: 1
    natural: 6
HP:
  HP: 76
  long: 9d8+36
saves:
  fort: 7
  ref: 5
  will: 9
defensive_abilities:
- channel resistance +4
DR:
- amount: 10
  weakness: slashing
immunities:
- undead traits
weaknesses:
- driftwood-dependent
speeds:
  base: 30
  swim: 30
attacks:
  melee:
  - - text: 2 claws +10 (1d6+3 plus parasites)
      entries:
      - - damage: 1d6+3
        - effect: parasites
      count: 2
      attack: claws
      bonus:
      - 10
spell_like_abilities:
  entries:
  - name: entangle
    source: default
    freq: At will
    DC: 16
  - name: tree shape
    source: default
    freq: At will
    other: dead tree only
  - name: wood shape
    source: default
    freq: At will
    DC: 16
  - name: aqueous orb
    source: default
    freq: 3/day
    DC: 17
  - name: crushing despair
    source: default
    freq: 3/day
    DC: 17
  - name: enervation
    source: default
    freq: 3/day
  - name: blight
    source: default
    freq: 1/day
    DC: 18
  sources:
  - name: default
    CL: 9
    concentration: 13
ability_scores:
  STR: 16
  DEX: 14
  CON:
  INT: 7
  WIS: 13
  CHA: 18
BAB: 6
CMB: 9
CMD: 22
feats:
- name: Alertness
- name: Dodge
- name: Improved Initiative
- name: Iron Will
- name: Weapon Focus (claw)
skills:
  Diplomacy: 7
  Handle Animal: 7
  Intimidate: 10
  Perception: 12
  Sense Motive: 3
  Swim: 14
languages:
- Common
- Sylvan
special_qualities:
- vermin empathy
ecology:
  environment: any coastlines
  organization: solitary, pair, or tangle (3-8)
  treasure_type: standard
special_abilities:
  Driftwood-Dependent (Su): A tidewretch is mystically bonded to a single piece of
    driftwood originating from the tree to which she was bonded in life. The tidewretch
    can never stray more than 300 yards from this piece of driftwood. A tidewretch
    who moves more than 300 yards beyond her bonded driftwood immediately becomes
    staggered and takes a -2 penalty on her attack and damage rolls and ability and
    skill checks and to the save DCs of her special abilities (including spell-like
    abilities). Every hour thereafter, she must succeed at a DC 15 Will save or these
    penalties increase by 2 (increases are cumulative). A tidewretch that is out of
    range of her bonded driftwood for 24 hours gains 1 negative level, which becomes
    permanent 24 hours thereafter, at which time she gains another negative level.
    Eventually, this separation destroys the tidewretch. Unlike a dryad, a tidewretch
    can't forge a new bond with another piece of driftwood, though many tidewretches
    find that they can carry their driftwood with them, as it is not rooted to the
    ground like a living tree.
  Parasites (Ex): The first time each round a tidewretch hits a target with a melee
    attack, a swarm of small parasites issues forth from the rotting wood that makes
    up her body, covering the target and causing discomfort and distraction. The target
    becomes staggered, but it can spend a standard action to brush the parasites off
    its body and end the effect.
  Vermin Empathy (Ex): This ability functions as a druid's wild empathy, except a
    tidewretch can use this ability only on vermin. A tidewretch gains a +4 racial
    bonus on this check. Vermin empathy treats swarms as one creature having a single
    mind; a tidewretch can thus use this ability to influence and direct swarms with
    relative ease.
desc_long: |-
  Tidewretches are undead dryads whose trees have died and become waterlogged driftwood. The dead state of the tree to which a tidewretch is bound is reflected in her disfigured appearance, especially her wrinkled and cracked wooden skin. Bits and pieces of the tidewretch have completely rotted away, leaving nothing but scar-like holes in her decomposing flesh. A tidewretch's fingers have sharpened into claws, and her eyes have become cold and dark. Tidewretches are home to hosts of parasites, and small insects can be seen skittering in and out of their cracked skin. When alone, tidewretches regularly weep tears of dirty water in lament for their fallen trees.

   Tidewretches are usually around 5 feet tall and weigh about 90 pounds.

---

# Tidewretch
This ancient, empty-eyed woman appears to have flesh made from damp, rotting wood, and sparse clumps of seaweed serve as her hair.
**Source** Pathfinder #122: Into the Shattered Continent pg. 90
**XP** 2,400

NE Medium undead
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +12

##### Defense

**AC** 19, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+2 Dex, +1 _[[feats/Dodge|dodge]]_, +6 natural)
**hp** 76 (9d8+36)
**Fort** +7, **Ref** +5, **Will** +9
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4; **DR** 10/slashing; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_
**Weaknesses** driftwood-dependent

##### Offense
**Speed** 30 ft., swim 30 ft.
**Melee** 2 claws +10 (1d6+3 plus parasites)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +13)
At will—_[[spells/Entangle|entangle]]_ (DC 16), _[[spells/Tree Shape|tree shape]]_ (dead tree only), _[[spells/Wood Shape|wood shape]]_ (DC 16) 
3/day—_[[spells/Aqueous Orb|aqueous orb]]_ (DC 17), _[[spells/Crushing Despair|crushing despair]]_ (DC 17), _[[spells/Enervation|enervation]]_ 
1/day—_[[spells/Blight|blight]]_ (DC 18)

##### Statistics
**Str** 16, **Dex** 14, **Con** —, **Int** 7, **Wis** 13, **Cha** 18
**Base Atk** +6; **CMB** +9; **CMD** 22
**Feats** _[[feats/Alertness|Alertness]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Diplomacy +7, Handle Animal +7, Intimidate +10, Perception +12, Sense Motive +3, Swim +14
**Languages** Common, Sylvan
**SQ** vermin _[[feats/Empathy|empathy]]_

##### Ecology

**Environment** any coastlines
**Organization** solitary, pair, or tangle (3-8)
**Treasure** standard

### Special Abilities

**Driftwood-Dependent (Su)** A _[[monsters/Tidewretch|tidewretch]]_ is mystically bonded to a single piece of driftwood originating from the tree to which she was bonded in life. The _tidewretch_ can never stray more than 300 yards from this piece of driftwood. A _tidewretch_ who moves more than 300 yards beyond her bonded driftwood immediately becomes _[[conditions/Staggered|staggered]]_ and takes a –2 penalty on her attack and damage rolls and ability and skill checks and to the save DCs of her special abilities (including _spell-like abilities_). Every hour thereafter, she must succeed at a DC 15 Will save or these penalties increase by 2 (increases are cumulative). A _tidewretch_ that is out of range of her bonded driftwood for 24 hours gains 1 negative level, which becomes permanent 24 hours thereafter, at which time she gains another negative level. Eventually, this separation destroys the _tidewretch_. Unlike a _[[monsters/Dryad|dryad]]_, a _tidewretch_ can’t forge a new bond with another piece of driftwood, though many tidewretches find that they can carry their driftwood with them, as it is not rooted to the ground like a living tree.

**Parasites (Ex)** The first time each round a _tidewretch_ hits a target with a melee attack, a swarm of small parasites issues forth from the rotting wood that makes up her body, covering the target and causing discomfort and _[[universal monster rules/Distraction|distraction]]_. The target becomes _staggered_, but it can spend a standard action to brush the parasites off its body and end the effect.

**Vermin _Empathy_ (Ex)** This ability functions as a _[[classes/Druid|druid]]_’s wild _empathy_, except a _tidewretch_ can use this ability only on vermin. A _tidewretch_ gains a +4 racial bonus on this check. Vermin _empathy_ treats swarms as one creature having a single mind; a _tidewretch_ can thus use this ability to influence and direct swarms with relative ease.

##### Description

Tidewretches are undead dryads whose trees have died and become waterlogged driftwood. The dead state of the tree to which a _tidewretch_ is bound is reflected in her disfigured appearance, especially her wrinkled and cracked wooden skin. Bits and pieces of the _tidewretch_ have completely rotted away, leaving nothing but scar-like holes in her decomposing flesh. A _tidewretch_’s fingers have sharpened into claws, and her eyes have become cold and dark. Tidewretches are home to hosts of parasites, and small insects can be seen skittering in and out of their cracked skin. When alone, tidewretches regularly weep tears of dirty water in lament for their _[[monsters/Fallen|fallen]]_ trees.

Tidewretches are usually around 5 feet tall and weigh about 90 pounds.
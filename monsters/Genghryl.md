---
cssclass: [monsters]
title1: Genghryl
desc_short: A mix of burly and slender tentacles extend from the body of this large,
  wormlike creature. Rows of frightful fangs line the maw beneath its sharp beak.
title2: Genghryl
CR: 11
sources:
- name: 'Pathfinder #117: Assault on Longshadow'
  page: 86
  link: http://paizo.com/products/btpy9p1h
XP: 12800
alignment: N
size: Large
type: magical beast
initiative:
  bonus: 6
senses:
  darkvision: 60
  low-light vision: true
  tremorsense: 60
AC:
  AC: 23
  touch: 11
  flat_footed: 21
  components:
    dex: 2
    natural: 12
    size: -1
HP:
  HP: 152
  long: 16d10+64
saves:
  fort: 14
  ref: 12
  will: 9
DR:
- amount: 5
  weakness: piercing or slashing
resistances:
  acid: 10
  cold: 10
speeds:
  base: 20
  burrow: 20
attacks:
  melee:
  - - text: bite +20 (2d8+5)
      entries:
      - - damage: 2d8+5
      attack: bite
      bonus:
      - 20
    - text: 4 tentacles +19 (1d8+2 plus grab or pull)
      entries:
      - - damage: 1d8+2
        - effect: grab or pull
      count: 4
      attack: tentacles
      bonus:
      - 19
  special:
  - constrict (1d8+2)
  - disturbing vocalizations
  - pull (tentacle, 5 ft.)
  - sinkhole
space: 10
reach: 5
reach_other: 10 ft. with tentacle
ability_scores:
  STR: 20
  DEX: 15
  CON: 19
  INT: 6
  WIS: 14
  CHA: 15
BAB: 16
CMB: 22
CMB_other: +26 grapple
CMD: 34
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Improved Initiative
- name: Iron Will
- name: Multiattack
- name: Power Attack
- name: Skill Focus (Disguise)
- name: Skill Focus (Perception)
- name: Weapon Focus (tentacle)
skills:
  Disguise: 9
    as burrowing animals: 17
  Perception: 16
  Stealth: 5
    underground: 10
  _racial_mods:
    Disguise:
      as burrowing animals: 8
    Stealth:
      underground: 5
languages:
- Terran (can't speak)
special_qualities:
- compression
- lure tentacles
ecology:
  environment: any plains
  organization: solitary or pair
  treasure_type: incidental
special_abilities:
  Disturbing Vocalizations (Su): A genghryl can emit different sounds from its lure
    tentacles, allowing it to mimic the barks, howls, shrieks, yips, and other noises
    common among burrowing mammals. Additionally, once per round as a free action,
    it can also use one of its tentacles to target a creature with one of two sounds,
    imposing either the frightened or stunned condition for 1d6 rounds unless the
    target succeeds at a DC 20 Will save. A creature that successfully saves cannot
    be affected by the same genghryl's disturbing vocalizations for 24 hours. This
    is a sonic mind-affecting effect. The save DC is Charisma-based.
  Lure Tentacles (Ex): A genghryl has a number of specialized tentacles equal to half
    its Hit Dice. It uses these tentacles to animate and manipulate the corpses of
    Small or smaller creatures and to emit its disturbing vocalizations. A genghryl
    typically uses these tentacles to maintain the illusion that a colony of burrowing
    animals is alive and well, drawing in larger, predatory animals. When it uses
    animals' corpses in this way, it gains a +8 bonus on Disguise checks (in addition
    to its normal racial bonus). Although the genghryl can animate Small humanoids
    in this manner, it does not gain the additional bonus on Disguise checks when
    doing so. Severing a lure tentacle requires a sunder attempt with a slashing weapon
    targeting the tentacle. A lure tentacle is considered a separate weapon with hardness
    0 and hit points equal to the genghryl's Hit Dice (typically 16 hp). To sever
    a tentacle, an opponent must deal enough damage to reduce the tentacle's hit points
    to 0 or fewer. Severing a tentacle deals an amount of damage to the genghryl's
    body equal to its Hit Dice. A genghryl with no remaining lure tentacles can't
    use its disturbing vocalizations.
  Sinkhole (Ex): A genghryl can cause an adjacent area of the ground above it (up
    to a 10-foot-by-10-foot square) to collapse, dropping any creatures in the affected
    squares into a 10-foot-deep hole unless they succeed at a DC 23 Reflex save, as
    though they had been subjected to the effects of a pit trap. The genghryl waits
    adjacent to the bottom of the pit and can immediately make a single melee attack
    against the flat-footed AC of one creature that fell in. A creature that fails
    the Reflex save by 5 or more also falls prone. The save DC is Strength-based.
desc_long: |-
  Genghryls are subterranean, wormlike creatures that use specialized tentacles to lure and weaken their prey. Genghryls are to verdant lands what seaweed sirens are to shipping lanes or wolves-in-sheep's-clothing are to plentiful woodlands-a menace.

  A genghryl's mottled, pinkish-brown body is about 3 feet wide at the front and tapers down to its tail, resembling a hideous segmented worm. Its head consists of a tooth-lined opening behind a sharp beak, which is surrounded by four powerful tentacles and three black eyes spaced evenly around it. A number of longer, thinner tentacles sprout from the segment just behind the genghryl's head. The older and larger the genghryl, the more tentacles it has.

  An adult genghryl weighs approximately 300 pounds.

---

# Genghryl
A mix of burly and slender tentacles extend from the body of this large, wormlike creature. Rows of frightful fangs line the maw beneath its sharp beak.
**Source** Pathfinder #117: Assault on Longshadow pg. 86
**XP** 12,800

N Large magical beast
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 60 ft.; Perception +16

##### Defense

**AC** 23, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+2 Dex, +12 natural, –1 size)
**hp** 152 (16d10+64)
**Fort** +14, **Ref** +12, **Will** +9
**DR** 5/piercing or slashing; **Resist** acid 10, cold 10

##### Offense
**Speed** 20 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft.
**Melee** bite +20 (2d8+5), 4 tentacles +19 (1d8+2 plus _[[universal monster rules/Grab|grab]]_ or _[[universal monster rules/Pull|pull]]_)
**Space** 10 ft., **Reach** 5 ft. (10 ft. with tentacle)
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (1d8+2), disturbing vocalizations, _pull_ (tentacle, 5 ft.), sinkhole

##### Statistics
**Str** 20, **Dex** 15, **Con** 19, **Int** 6, **Wis** 14, **Cha** 15
**Base Atk** +16; **CMB** +22 (+26 grapple); **CMD** 34 (can’t be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Disguise, Perception), _[[feats/Weapon Focus|Weapon Focus]]_ (tentacle)
**Skills** Disguise +9 (+17 as burrowing animals), Perception +16, Stealth +5 (+10 underground); **Racial Modifiers** +8 Disguise as burrowing animals, +5 Stealth underground
**Languages** Terran (can’t speak)
**SQ** _[[universal monster rules/Compression|compression]]_, lure tentacles

##### Ecology

**Environment** any plains
**Organization** solitary or pair
**Treasure** incidental

### Special Abilities

**Disturbing Vocalizations (Su)** A _[[monsters/Genghryl|genghryl]]_ can emit different sounds from its lure tentacles, allowing it to _[[monsters/Mimic|mimic]]_ the barks, howls, shrieks, yips, and other noises common among burrowing mammals. Additionally, once per round as a free action, it can also use one of its tentacles to target a creature with one of two sounds, imposing either the _[[conditions/Frightened|frightened]]_ or _[[conditions/Stunned|stunned]]_ condition for 1d6 rounds unless the target succeeds at a DC 20 Will save. A creature that successfully saves cannot be affected by the same _genghryl_’s disturbing vocalizations for 24 hours. This is a sonic mind-affecting effect. The save DC is Charisma-based.

**Lure Tentacles (Ex)** A _genghryl_ has a number of specialized tentacles equal to half its Hit Dice. It uses these tentacles to animate and manipulate the corpses of Small or smaller creatures and to emit its disturbing vocalizations. A _genghryl_ typically uses these tentacles to maintain the illusion that a colony of burrowing animals is alive and well, drawing in larger, predatory animals. When it uses animals’ corpses in this way, it gains a +8 bonus on Disguise checks (in addition to its normal racial bonus). Although the _genghryl_ can animate Small humanoids in this manner, it does not gain the additional bonus on Disguise checks when doing so. Severing a lure tentacle requires a sunder attempt with a slashing weapon targeting the tentacle. A lure tentacle is considered a separate weapon with hardness 0 and hit points equal to the _genghryl_’s Hit Dice (typically 16 hp). To sever a tentacle, an opponent must deal enough damage to reduce the tentacle’s hit points to 0 or fewer. Severing a tentacle deals an amount of damage to the _genghryl_’s body equal to its Hit Dice. A _genghryl_ with no remaining lure tentacles can’t use its disturbing vocalizations.
**Sinkhole (Ex)** A _genghryl_ can cause an adjacent area of the ground above it (up to a 10-foot-by-10-foot square) to collapse, dropping any creatures in the affected squares into a 10-foot-deep hole unless they succeed at a DC 23 Reflex save, as though they had been subjected to the effects of a pit trap. The _genghryl_ waits adjacent to the bottom of the pit and can immediately make a single melee attack against the _flat-footed_ AC of one creature that fell in. A creature that fails the Reflex save by 5 or more also falls _[[conditions/Prone|prone]]_. The save DC is Strength-based.

##### Description

Genghryls are subterranean, wormlike creatures that use specialized tentacles to lure and weaken their prey. Genghryls are to verdant lands what seaweed sirens are to shipping lanes or wolves-in-sheep’s-clothing are to plentiful woodlands—a menace.

A _genghryl_’s mottled, pinkish-brown body is about 3 feet wide at the front and tapers down to its tail, resembling a hideous segmented worm. Its head consists of a tooth-lined opening behind a sharp beak, which is surrounded by four powerful tentacles and three black eyes spaced evenly around it. A number of longer, thinner tentacles sprout from the segment just behind the _genghryl_’s head. The older and larger the _genghryl_, the more tentacles it has.

An adult _genghryl_ weighs approximately 300 pounds.
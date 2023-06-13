---
cssclass: [monsters]
title1: Protean, Ibshaunet
desc_short: This nightmarish serpentine creature bears crackling wings of chaotic
  energy and bristling fins of insubstantial fire.
title2: Ibshaunet
CR: 11
sources:
- name: Concordance of Rivals
  page: 58
  link: https://paizo.com/products/btq01x4d?Pathfinder-Campaign-Setting-Concordance-of-Rivals
XP: 12800
alignment: CN
size: Huge
type: outsider
subtypes:
- chaotic
- extraplanar
- protean
- shapechanger
initiative:
  bonus: 7
senses:
  blindsense: 30
  darkvision: 60
  detect law: true
auras:
- name: corrosive aura
  radius: 30
  DC: 19
AC:
  AC: 27
  touch: 15
  flat_footed: 20
  components:
    dex: 6
    dodge: 1
    natural: 12
    size: -2
HP:
  HP: 149
  long: 13d10+78
  fast_healing: 5
saves:
  fort: 14
  ref: 14
  will: 7
defensive_abilities:
- amorphous anatomy
- freedom of movement
DR:
- amount: 10
  weakness: lawful
immunities:
- acid
- polymorph
resistances:
  electricity: 10
  sonic: 10
SR: 22
speeds:
  base: 30
  fly: 30
  fly_maneuverability: perfect
  swim: 30
attacks:
  melee:
  - - text: bite +20 (1d8+8/19-20 plus grab)
      entries:
      - - damage: 1d8+8
          crit_range: 19-20
        - effect: grab
      attack: bite
      bonus:
      - 20
    - text: 2 claws +19 (1d6+8)
      entries:
      - - damage: 1d6+8
      count: 2
      attack: claws
      bonus:
      - 19
    - text: tail slap +14 (1d8+4 plus grab)
      entries:
      - - damage: 1d8+4
        - effect: grab
      attack: tail slap
      bonus:
      - 14
  special:
  - constrict (1d8+12)
  - fast swallow
  - swallow whole (2d8 acid damage plus warpwave, AC 16, hp 14)
  - warpwave breath (50-ft. cone, 10d6 acid damage plus warpwave, Reflex DC 22 half)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: detect law
    source: default
    freq: Constant
  - name: dimension door
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: plane shift
    source: default
    freq: 1/day
    DC: 20
  - name: resilient sphere
    source: default
    freq: 1/day
    DC: 19
  sources:
  - name: default
    CL: 9
    concentration: 12
ability_scores:
  STR: 27
  DEX: 22
  CON: 22
  INT: 13
  WIS: 16
  CHA: 17
BAB: 13
CMB: 23
CMB_other: +27 grapple
CMD: 40
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Dodge
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Mobility
- name: Power Attack
- name: Weapon Focus (bite)
skills:
  Acrobatics: 22
  Fly: 26
  Intimidate: 19
  Knowledge (planes): 17
  Perception: 19
  Survival: 19
  Swim: 29
languages:
- Protean
special_qualities:
- change shape (greater polymorph)
ecology:
  environment: any (Maelstrom)
  organization: solitary or devouring (3-5)
  treasure_type: standard
special_abilities:
  Corrosive Aura (Su): A creature that enters an ibshaunet's aura must succeed at
    a DC 19 Fortitude save or take 3d6 points of acid damage. Once a creature is affected
    by this aura, it is not affected again unless it leaves and reenters the aura.
    The save DC is Charisma-based.
  Warpwave Breath (Su): An ibshaunet can exhale a 50-foot cone of entropic energy
    every 1d4 rounds, dealing 10d6 points of acid damage to creatures in the area
    of effect (Reflex DC 22 half). A creature damaged by the breath must succeed at
    a DC 22 Fortitude save or be subject to a warpwave. The save DC is Constitution-based.
desc_long: Ibshaunet proteans are rarely seen engines of destruction.

---

# Protean, Ibshaunet
This nightmarish serpentine creature bears crackling wings of chaotic energy and bristling fins of insubstantial fire.
**Source** Concordance of Rivals pg. 58
**XP** 12,800

CN Huge outsider (chaotic, extraplanar, protean, shapechanger)
**Init** +7; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 30 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Law|detect law]]_; Perception +19
**Aura** _[[items/Weapon Magic Abilities/Corrosive|corrosive]]_ aura (30 ft., DC 19)

##### Defense

**AC** 27, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+6 Dex, +1 dodge, +12 natural, –2 size)
**hp** 149 (13d10+78); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +14, **Ref** +14, **Will** +7
**Defensive Abilities** _[[universal monster rules/Amorphous|amorphous]]_ anatomy, _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 10/lawful; **Immune** acid, _[[spells/Polymorph|polymorph]]_; **Resist** electricity 10, sonic 10; **SR** 22

##### Offense
**Speed** 30 ft., fly 30 ft. (perfect),

swim 30 ft.
**Melee** bite +20 (1d8+8/19–20 plus _[[universal monster rules/Grab|grab]]_), 2 claws +19 (1d6+8), tail slap +14 (1d8+4 plus _grab_)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (1d8+12), _[[universal monster rules/Fast Swallow|fast swallow]]_, _[[universal monster rules/Swallow Whole|swallow whole]]_ (2d8 acid damage plus warpwave, AC 16, hp 14), warpwave breath (50-ft. cone, 10d6 acid damage plus warpwave, Reflex DC 22 half)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +12)
Constant—_detect law_
 At will—_[[spells/Dimension Door|dimension door]]_ (self plus 50 lbs. of objects only)
 1/day—_[[spells/Plane Shift|plane shift]]_ (DC 20), _[[spells/Resilient Sphere|resilient sphere]]_ (DC 19)

##### Statistics
**Str** 27, **Dex** 22, **Con** 22, **Int** 13, **Wis** 16, **Cha** 17
**Base Atk** +13; **CMB** +23 (+27 grapple); **CMD** 40 (can’t be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Acrobatics +22, Fly +26, Intimidate +19, Knowledge (planes) +17, Perception +19, Survival +19, Swim +29
**Languages** Protean
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (greater _polymorph_)

##### Ecology

**Environment** any (Maelstrom)
**Organization** solitary or devouring (3–5)
**Treasure** standard

### Special Abilities

**_Corrosive_ Aura (Su)** A creature that enters an ibshaunet’s aura must succeed at a DC 19 Fortitude save or take 3d6 points of acid damage. Once a creature is affected by this aura, it is not affected again unless it leaves and reenters the aura. The save DC is Charisma-based.
**Warpwave Breath (Su)** An ibshaunet can exhale a 50-foot cone of entropic energy every 1d4 rounds, dealing 10d6 points of acid damage to creatures in the area of effect (Reflex DC 22 half). A creature damaged by the breath must succeed at a DC 22 Fortitude save or be subject to a warpwave. The save DC is Constitution-based.

##### Description

Ibshaunet proteans are rarely seen engines of _[[spells/Destruction|destruction]]_.
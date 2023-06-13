---
cssclass: [monsters]
title1: Witchwyrd
desc_short: This gray-skinned humanoid wears fine red robes. The being has four arms,
  each ending in a three-fingered hand.
title2: Witchwyrd
CR: 6
sources:
- name: Bestiary 2
  page: 285
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
- name: 'Pathfinder #14: Children of the Void'
  page: 88
  link: http://paizo.com/pathfinder/adventurePath/secondDarkness/v5748btpy85ed
XP: 2400
alignment: LN
size: Medium
type: monstrous humanoid
initiative:
  bonus: 6
senses:
  darkvision: 60
  detect magic: true
AC:
  AC: 19
  touch: 12
  flat_footed: 17
  components:
    armor: 4
    dex: 2
    natural: 3
HP:
  HP: 68
  long: 8d10+24
saves:
  fort: 7
  ref: 8
  will: 9
defensive_abilities:
- absorb force
DR:
- amount: 5
  weakness: magic
speeds:
  base: 30
attacks:
  melee:
  - - text: ranseur +11/+6 (2d4+4/×3)
      entries:
      - - damage: 2d4+4
          crit_multiplier: 3
      attack: ranseur
      bonus:
      - 11
      - 6
    - text: 2 slams +6 (1d4+1 plus grab)
      entries:
      - - damage: 1d4+1
        - effect: grab
      count: 2
      attack: slams
      bonus:
      - 6
  - - text: 4 slams +11 (1d4+3 plus grab)
      entries:
      - - damage: 1d4+3
        - effect: grab
      count: 4
      attack: slams
      bonus:
      - 11
  special:
  - force bolt
space: 5
reach: 5
reach_other: 10 ft. with ranseur
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: floating disk
    source: default
    freq: Constant
  - name: mage armor
    source: default
    freq: Constant
  - name: resist energy
    source: default
    freq: Constant
    other: one at a time
  - name: unseen servant
    source: default
    freq: Constant
  - name: dispel magic
    source: default
    freq: 3/day
  - name: displacement
    source: default
    freq: 3/day
  - name: suggestion
    source: default
    freq: 3/day
    DC: 18
  - name: dimension door
    source: default
    freq: 1/day
  - name: resilient sphere
    source: default
    freq: 1/day
    DC: 19
  sources:
  - name: default
    CL: 8
    concentration: 13
ability_scores:
  STR: 16
  DEX: 15
  CON: 17
  INT: 18
  WIS: 13
  CHA: 20
BAB: 8
CMB: 11
CMB_other: +15 grapple
CMD: 23
feats:
- is_bonus: true
  name: Deflect Arrows
- name: Great Fortitude
- name: Improved Initiative
- name: Iron Will
- name: Persuasive
skills:
  Appraise: 12
  Bluff: 13
  Diplomacy: 11
  Intimidate: 18
  Knowledge (arcana): 12
  Knowledge (geography): 12
  Knowledge (planes): 12
  Perception: 8
  Sense Motive: 5
  Use Magic Device: 9
languages:
- Common
- Draconic
- one or more planar languages
- tongues
ecology:
  environment: any land
  organization: solitary, entourage (1 witchwyrd and 2-5 humanoid guards), or enclave
    (2-5 witchwyrds and 11-20 humanoid guards)
  treasure_type: double
special_abilities:
  Absorb Force (Su): Once per round, a witchwyrd can use a free hand to “catch” a
    magic missile fired at it. This absorbs the missile and manifests as a glowing
    nimbus around that hand (which is no longer considered free). The energy lasts
    6 rounds or until it is used to create a force bolt. To use this ability, the
    witchwyrd must be aware of the incoming magic missile and cannot be flat-footed.
  Force Bolt (Su): A witchwyrd can “throw” a magic missile (1d4+1 damage) from each
    free hand as a free action (maximum of two per round). If it has absorbed a magic
    missile, it can throw an additional force bolt that round, expending the absorbed
    energy (maximum of two additional bolts per round).
desc_long: Alien merchants that travel between planets and planes, witchwyrds stand
  7 feet tall, weigh 300 pounds, and are covered in hairless blue-gray skin. Witchwyrds
  new to a market or eager to avoid identification during an important business deal
  fold their second sets of flexible arms behind their backs and dress in robes, the
  better to pass as a less-infamous humanoid race. Witchwyrds tend to prefer the driest,
  warmest regions of the areas they visit-perhaps an indicator of their mysterious
  home world.

---

# Witchwyrd
This gray-skinned humanoid wears fine red robes. The being has four arms, each ending in a three-fingered hand.
**Source** Bestiary 2 pg. 285, Pathfinder #14: Children of the Void pg. 88
**XP** 2,400

LN Medium monstrous humanoid
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Magic|detect magic]]_; Perception +8

##### Defense

**AC** 19, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+4 armor, +2 Dex, +3 natural)
**hp** 68 (8d10+24)
**Fort** +7, **Ref** +8, **Will** +9
**Defensive Abilities** absorb force; **DR** 5/magic

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Ranseur|ranseur]]_ +11/+6 (2d4+4/×3), 2 slams +6 (1d4+1 plus _[[universal monster rules/Grab|grab]]_) or 4 slams +11 (1d4+3 plus _grab_)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with _ranseur_)
**Special Attacks** force bolt
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +13)
Constant—_detect magic_, _[[spells/Floating Disk|floating disk]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Resist Energy|resist energy]]_ (one at a time), _[[spells/Unseen Servant|unseen servant]]_
3/day—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Displacement|displacement]]_, _[[spells/Suggestion|suggestion]]_ (DC 18)
1/day—_[[spells/Dimension Door|dimension door]]_, _[[spells/Resilient Sphere|resilient sphere]]_ (DC 19)

##### Statistics
**Str** 16, **Dex** 15, **Con** 17, **Int** 18, **Wis** 13, **Cha** 20
**Base Atk** +8; **CMB** +11 (+15 grapple); **CMD** 23
**Feats** _[[feats/Deflect Arrows|Deflect Arrows]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Persuasive|Persuasive]]_
**Skills** Appraise +12, Bluff +13, Diplomacy +11, Intimidate +18, Knowledge (arcana) +12, Knowledge (geography) +12, Knowledge (planes) +12, Perception +8, Sense Motive +5, Use Magic Device +9
**Languages** Common, Draconic, one or more _[[items/Weapon Magic Abilities/Planar|planar]]_ languages; _[[spells/Tongues|tongues]]_

##### Ecology

**Environment** any land
**Organization** solitary, entourage (1 _[[monsters/Witchwyrd|witchwyrd]]_ and 2–5 humanoid guards), or enclave (2–5 witchwyrds and 11–20 humanoid guards)
**Treasure** double

### Special Abilities

**Absorb Force (Su)** Once per round, a _witchwyrd_ can use a free hand to “catch” a _[[spells/Magic Missile|magic missile]]_ fired at it. This absorbs the missile and manifests as a glowing nimbus around that hand (which is no longer considered free). The energy lasts 6 rounds or until it is used to create a force bolt. To use this ability, the _witchwyrd_ must be aware of the incoming _magic missile_ and cannot be _flat-footed_.

**Force Bolt (Su)** A _witchwyrd_ can “throw” a _magic missile_ (1d4+1 damage) from each free hand as a free action (maximum of two per round). If it has absorbed a _magic missile_, it can throw an additional force bolt that round, expending the absorbed energy (maximum of two additional bolts per round).

##### Description

Alien merchants that travel between planets and planes, witchwyrds stand 7 feet tall, weigh 300 pounds, and are covered in hairless blue-gray skin. Witchwyrds new to a market or eager to avoid identification during an important business deal fold their second sets of flexible arms behind their backs and dress in robes, the better to pass as a less-infamous humanoid race. Witchwyrds tend to prefer the driest, warmest regions of the areas they visit—perhaps an indicator of their mysterious home world.
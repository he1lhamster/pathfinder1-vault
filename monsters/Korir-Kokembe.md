---
cssclass: [monsters]
title1: Korir-Kokembe
desc_short: This green-tined dragon has multiple sets of legs down its long, sinuous
  body. An oversized gullet bulges in its throat.
title2: Korir-Kokembe
CR: 10
sources:
- name: Inner Sea Bestiary
  page: 23
  link: http://paizo.com/products/btpy8v2x?Pathfinder-Campaign-Setting-Inner-Sea-Bestiary
XP: 9600
alignment: N
size: Huge
type: dragon
initiative:
  bonus: 6
senses:
  darkvision: 60
  low-light vision: true
  scent: true
auras:
- name: frightful presence
  radius: 30
  DC: 18
AC:
  AC: 24
  touch: 10
  flat_footed: 22
  components:
    dex: 2
    natural: 14
    size: -2
HP:
  HP: 136
  long: 13d12+52
saves:
  fort: 12
  ref: 12
  will: 10
immunities:
- disease
- dragon traits
- magic paralysis and sleep
speeds:
  base: 40
  climb: 40
  fly: 80
  fly_maneuverability: good
  swim: 40
attacks:
  melee:
  - - text: bite +18 (2d6+10 plus disease and grab)
      entries:
      - - damage: 2d6+10
        - effect: disease
        - effect: grab
      attack: bite
      bonus:
      - 18
    - text: 2 claws +18 (2d6+7/19-20 plus grab)
      entries:
      - - damage: 2d6+7
          crit_range: 19-20
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 18
    - text: tail slap +13 (2d6+3 plus grab)
      entries:
      - - damage: 2d6+3
        - effect: grab
      attack: tail slap
      bonus:
      - 13
  special:
  - constrict (2d6+7)
  - grab (Gargantuan)
  - rake (2 claws +18, 2d6+7/19-20)
space: 15
reach: 15
reach_other: 20 ft. with bite
spell_like_abilities:
  entries:
  - name: freedom of movement
    source: default
    freq: Constant
  - name: repel vermin
    source: default
    freq: At will
    DC: 16
  - superscripts:
    - APG
    name: vomit swarm
    source: default
    freq: At will
    other: must wait 1d4 rounds before using this ability again
  - name: entangle
    source: default
    freq: 3/day
    DC: 13
  - name: creeping doom
    source: default
    freq: 1/day
    DC: 19
  - name: insect plague
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 13
    concentration: 15
ability_scores:
  STR: 25
  DEX: 15
  CON: 18
  INT: 10
  WIS: 14
  CHA: 15
BAB: 13
CMB: 22
CMB_other: +26 grapple
CMD: 34
CMD_other: 46 vs. trip
feats:
- name: Critical Focus
- name: Improved Critical (claw)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Power Attack
- name: Sickening Critical
- name: Wingover
skills:
  Climb: 21
  Fly: 15
  Intimidate: 15
  Knowledge (nature): 13
  Perception: 18
  Spellcraft: 10
  Stealth: 10
    in jungles: 18
  Survival: 10
  Swim: 25
  _racial_mods:
    Stealth:
      in jungles: 8
languages:
- Draconic
special_qualities:
- compression
ecology:
  environment: warm jungles (Mwangi Expanse)
  organization: solitary or nest (2-5)
  treasure_type: standard
special_abilities:
  Disease (Ex): Bite-injury; save Fort DC 20; onset 1 round; frequency 1 day; effect
    1d3 Dex damage and 1d3 Str damage; cure 2 consecutive saves.
desc_long: Korir-kokembe live in the deep, watery jungles of central Garund, plaguing
  the major rivers and lake systems. While young korir-kokembe may swim near populated
  waterways to claim their prey, their elder kin prefer more remote backwaters, sloughs,
  and heavily wooded swamps where they can hunt undisturbed. These degenerate dragons
  live in a violent symbiosis with the tiny vermin that infest the jungle, hosting
  colonies of such creatures within their own bodies. Such tiny vermin constantly
  swarm in and out of the korir-kokembe's gullet, bringing contagion to creatures
  bitten and allowing the wyrm to expel swarms of pests, or to summon yet more vermin
  to its aid. While korir-kokembe are capable of flight, they generally prefer to
  crawl or climb on their eight legs, hunching their bodies like inchworms or twining
  their coils around their prey while savaging creatures with a barrage of slashing
  claws.

---

# Korir-Kokembe
This green-tined dragon has multiple sets of legs down its long, sinuous body. An oversized gullet bulges in its throat.
**Source** Inner Sea Bestiary pg. 23
**XP** 9,600

N Huge dragon
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +18
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (30 ft., DC 18)

##### Defense

**AC** 24, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+2 Dex, +14 natural, –2 size)
**hp** 136 (13d12+52)
**Fort** +12, **Ref** +12, **Will** +10
**Immune** disease, dragon traits, magic _[[universal monster rules/Paralysis|paralysis]]_ and sleep

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 40 ft., fly 80 ft. (good), swim 40 ft.
**Melee** bite +18 (2d6+10 plus disease and _[[universal monster rules/Grab|grab]]_), 2 claws +18 (2d6+7/19–20 plus _grab_), tail slap +13 (2d6+3 plus _grab_)
**Space** 15 ft., **Reach** 15 ft. (20 ft. with bite)
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (2d6+7), _grab_ (Gargantuan), _[[universal monster rules/Rake|rake]]_ (2 claws +18, 2d6+7/19–20)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +15)
Constant—_[[spells/Freedom of Movement|freedom of movement]]_
At will—_[[spells/Repel Vermin|repel vermin]]_ (DC 16), _[[spells/Vomit Swarm|vomit swarm]]_ (must wait 1d4 rounds before using this ability again)
3/day—_[[spells/Entangle|entangle]]_ (DC 13)
1/day—_[[spells/Creeping Doom|creeping doom]]_ (DC 19), _[[spells/Insect Plague|insect plague]]_

##### Statistics
**Str** 25, **Dex** 15, **Con** 18, **Int** 10, **Wis** 14, **Cha** 15
**Base Atk** +13; **CMB** +22 (+26 grapple); **CMD** 34 (46 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Sickening Critical|Sickening Critical]]_, _[[feats/Wingover|Wingover]]_
**Skills** _Climb_ +21, Fly +15, Intimidate +15, Knowledge (nature) +13, Perception +18, Spellcraft +10, Stealth +10 (+18 in jungles), Survival +10, Swim +25; **Racial Modifiers** +8 Stealth in jungles
**Languages** Draconic
**SQ** _[[universal monster rules/Compression|compression]]_

##### Ecology

**Environment** warm jungles (Mwangi Expanse)
**Organization** solitary or nest (2–5)
**Treasure** standard

### Special Abilities

**Disease (Ex)** Bite—injury; save Fort DC 20; onset 1 round; frequency 1 day; effect 1d3 Dex damage and 1d3 Str damage; cure 2 consecutive saves.

##### Description

_[[monsters/Korir-Kokembe|Korir-kokembe]]_ live in the deep, watery jungles of central Garund, plaguing the major rivers and lake systems. While young _korir-kokembe_ may swim near populated waterways to claim their prey, their elder kin prefer more remote backwaters, sloughs, and heavily wooded swamps where they can hunt undisturbed. These degenerate dragons live in a violent symbiosis with the tiny vermin that infest the jungle, hosting colonies of such creatures within their own bodies. Such tiny vermin constantly swarm in and out of the _korir-kokembe_’s gullet, bringing _[[spells/Contagion|contagion]]_ to creatures bitten and allowing the wyrm to expel swarms of pests, or to _[[universal monster rules/Summon|summon]]_ yet more vermin to its aid. While _korir-kokembe_ are capable of _[[universal monster rules/Flight|flight]]_, they generally prefer to crawl or _climb_ on their eight legs, hunching their bodies like inchworms or twining their coils around their prey while savaging creatures with a barrage of slashing claws.
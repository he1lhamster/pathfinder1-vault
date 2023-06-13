---
cssclass: [monsters]
title1: Clockwork, Clockwork Priest
desc_short: This four-armed clockwork construct has a glowing crystal globe as a head
  and a shining crystal set into its chest.
title2: Clockwork Priest
CR: 11
sources:
- name: Construct Handbook
  page: 34
  link: https://paizo.com/products/btq01vam
XP: 12800
alignment: N
size: Medium
type: construct
subtypes:
- clockwork
initiative:
  bonus: 10
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 25
  touch: 18
  flat_footed: 17
  components:
    dex: 6
    dodge: 2
    natural: 7
HP:
  HP: 119
  long: 18d10+20
saves:
  fort: 6
  ref: 14
  will: 10
immunities:
- construct traits
weaknesses:
- vulnerable to electricity
speeds:
  base: 30
attacks:
  melee:
  - - text: 4 slams +21 (1d4+3)
      entries:
      - - damage: 1d4+3
      count: 4
      attack: slams
      bonus:
      - 21
  special:
  - domain magic
spell_like_abilities:
  entries:
  - name: animate rope
    source: default
    freq: At will
  - name: cure light wounds
    source: default
    freq: At will
  - name: cure moderate wounds
    source: default
    freq: 3/day
  - name: wood shape
    source: default
    freq: 3/day
    DC: 16
  - name: cure serious wounds
    source: default
    freq: 1/day
  - name: stone shape
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 11
    concentration: 6
    domains:
    - artifice
ability_scores:
  STR: 17
  DEX: 22
  CON:
  INT:
  WIS: 18
  CHA: 1
BAB: 18
CMB: 21
CMD: 39
feats:
- is_bonus: true
  name: Improved Initiative
- is_bonus: true
  name: Lightning Reflexes
skills: {}
special_qualities:
- difficult to create
- swift reactions
- winding
ecology:
  environment: any
  organization: solitary, pair, or clergy (3-8)
  treasure_type: none
special_abilities:
  Domain Magic (Su): The crystal embedded into a clockwork priest's chest serves as
    a divine focus, granting it a number of spell-like abilities (CL 11th). The spells
    it can use are determined by its cleric domain and whether the creator instilled
    positive or negative energy into the creation. Once chosen, the domain and type
    of energy cannot be changed. A clockwork priest can cast either cure or inflict
    spells (depending on the energy it was instilled with at creation) of 1st through
    3rd levels, as well as the spells granted by its chosen domain up to 3rd level.
    It can cast 1st-level spells at will, 2nd-level spells three times per day, and
    3rd-level spells once per day. The save DCs are Wisdom-based.
desc_long: |-
  A clockwork priest combines raw divine energy with clockwork engineering through an integrated divine focus nestled in its chest. Through divine conduits and specially sanctified parts, these creations act as vessels of divinities, granting them a reservoir of divine energy they can use to generate spell effects. They often serve as healers, offering aid to the afflicted and to those ravaged in battle. Because of their unwavering loyalty to their deities, clockwork priests are willing to sacrifice themselves for their missions.

   Within a church, clockwork priests serve as assistants and aides, carrying out commands with unquestioned loyalty. While rare, churches staffed entirely by clockwork priests do exist. Stories tell of cathedrals dedicated to Amaznen, the Azlanti god of invention and magic, still operating in the ruins of Azlant, despite the fact that that god is now dead.

---

# Clockwork, Clockwork Priest
This four-armed clockwork construct has a glowing crystal globe as a head and a shining crystal set into its chest.
**Source** Construct Handbook pg. 34
**XP** 12,800

N Medium construct (clockwork)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +4

##### Defense

**AC** 25, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+6 Dex, +2 _[[feats/Dodge|dodge]]_, +7 natural)
**hp** 119 (18d10+20)
**Fort** +6, **Ref** +14, **Will** +10
**Immune** _[[universal monster rules/Construct Traits|construct traits]]_
**Weaknesses** vulnerable to electricity

##### Offense
**Speed** 30 ft.
**Melee** 4 slams +21 (1d4+3)
**Special Attacks** domain magic
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +6)
At will—_[[spells/Animate Rope|animate rope]]_, _[[spells/Cure Light Wounds|cure light wounds]]_ 
3/day—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Wood Shape|wood shape]]_ (DC 16) 
1/day—_[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Stone Shape|stone shape]]_ 
**Domain** Artifice

##### Statistics
**Str** 17, **Dex** 22, **Con** —, **Int** —, **Wis** 18, **Cha** 1
**Base Atk** +18; **CMB** +21; **CMD** 39
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**SQ** difficult to create, swift reactions, winding

##### Ecology

**Environment** any
**Organization** solitary, pair, or clergy (3-8)
**Treasure** none

### Special Abilities

**Domain Magic (Su)** The crystal embedded into a clockwork priest’s chest serves as a divine focus, granting it a number of _spell-like abilities_ (CL 11th). The spells it can use are determined by its _[[classes/Cleric|cleric]]_ domain and whether the creator instilled positive or negative energy into the creation. Once chosen, the domain and type of energy cannot be changed. A clockwork priest can cast either cure or inflict spells (depending on the energy it was instilled with at creation) of 1st through 3rd levels, as well as the spells granted by its chosen domain up to 3rd level. It can cast 1st-level spells at will, 2nd-level spells three times per day, and 3rd-level spells once per day. The save DCs are Wisdom-based.

##### Description

A clockwork priest combines raw divine energy with clockwork engineering through an integrated divine focus nestled in its chest. Through divine conduits and specially sanctified parts, these creations act as vessels of divinities, granting them a reservoir of divine energy they can use to generate spell effects. They often serve as healers, offering aid to the afflicted and to those ravaged in battle. Because of their unwavering loyalty to their deities, clockwork priests are willing to _[[spells/Sacrifice|sacrifice]]_ themselves for their missions.

Within a church, clockwork priests serve as assistants and aides, carrying out commands with unquestioned loyalty. While rare, churches staffed entirely by clockwork priests do exist. Stories tell of cathedrals dedicated to Amaznen, the Azlanti god of invention and magic, still operating in the ruins of Azlant, despite the fact that that god is now dead.
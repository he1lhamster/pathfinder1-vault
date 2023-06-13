---
cssclass: [monsters]
title1: Angel, Choral
desc_short: This shimmering being looks like a miniature human with broad, iridescent
  wings and hair that slowly ripples through the air.
title2: Choral
CR: 6
sources:
- name: Bestiary 5
  page: 23
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
- name: Chronicle of the Righteous
  page: 60
  link: http://paizo.com/products/btpy8xe9?Pathfinder-Campaign-Setting-Chronicle-of-the-Righteous
XP: 2400
alignment: NG
size: Small
type: outsider
subtypes:
- angel
- extraplanar
- good
initiative:
  bonus: 7
senses:
  darkvision: 60
  detect evil: true
auras:
- name: protective aura
AC:
  AC: 19
  touch: 14
  flat_footed: 16
  components:
    dex: 3
    natural: 5
    size: 1
    deflection vs. evil: 4
HP:
  HP: 68
  long: 8d10+24
saves:
  fort: 6
  ref: 9
  will: 9
  other: +4 vs. poison, +4 resistance vs. evil
DR:
- amount: 5
  weakness: evil
immunities:
- acid
- cold
- petrification
resistances:
  electricity: 10
  fire: 10
SR: 17
speeds:
  base: 40
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: slam +10 (1d3+1)
      entries:
      - - damage: 1d3+1
      attack: slam
      bonus:
      - 10
  ranged:
  - - text: piercing hymn +12 touch (4d6 sonic plus deafened)
      entries:
      - - damage: 4d6
          type: sonic
        - effect: deafened
      attack: piercing hymn
      bonus:
      - 12
      touch: true
  special:
  - countersong
  - harmonize
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: aid
    source: default
    freq: At will
  - name: ghost sound
    source: default
    freq: At will
    DC: 13
  - name: dispel evil
    source: default
    freq: At will
    DC: 18
  - name: dispel magic
    source: default
    freq: At will
  - name: invisibility
    source: default
    freq: At will
    other: self only
  - name: plane shift
    source: default
    freq: At will
    other: self only
  - name: remove curse
    source: default
    freq: At will
  - name: remove disease
    source: default
    freq: At will
  - name: remove fear
    source: default
    freq: At will
  - name: cure moderate wounds
    source: default
    freq: 3/day
  - name: sculpt sound
    source: default
    freq: 3/day
    DC: 16
  - name: sound burst
    source: default
    freq: 3/day
    DC: 15
  sources:
  - name: default
    CL: 8
    concentration: 11
ability_scores:
  STR: 13
  DEX: 16
  CON: 15
  INT: 16
  WIS: 16
  CHA: 17
BAB: 8
CMB: 8
CMD: 21
feats:
- name: Alertness
- name: Great Fortitude
- name: Improved Initiative
- name: Toughness
skills:
  Acrobatics: 14
  Diplomacy: 14
  Escape Artist: 11
  Fly: 20
  Knowledge (planes): 14
  Knowledge (religion): 14
  Perception: 16
  Perform (sing): 14
  Sense Motive: 16
languages:
- Celestial
- Draconic
- Infernal
- truespeech
ecology:
  environment: any good-aligned planes
  organization: solo, duet, or Ensemble (3-8)
  treasure_type: standard
special_abilities:
  Countersong (Su): A choral can attempt a Perform (sing) check to counter magic effects
    that depend on sound. This ability functions as the bard ability of the same name.
  Harmonize (Sp): When chorals work together, they can use their complementary voices
    to create mystical harmonies. Two or more chorals within 60 feet of one another
    can use calm emotions or heroism as a spell-like ability, four or more chorals
    can use shout, and six or more chorals can use greater heroism or holy word. Only
    the choral that actually casts the spell-like ability in question must take a
    standard action to achieve this effect-the other chorals need only take swift
    actions during the same round.
  Piercing Hymn (Su): As a standard action, a choral can launch a concentrated blast
    of sonic energy from its mouth as a ranged touch attack. This attack has a range
    of 90 feet with no range increment and deals 4d6 points of sonic damage. Any creature
    struck by a piercing hymn must succeed at a DC 17 Fortitude save or be deafened
    for 1d4 minutes. The save DC is Charisma-based.
desc_long: Choral angels are singers of great skill, and their ranks fill the halls
  of good deities with soaring hymns and solemn chants. They manifest from the spirits
  of the pious dead who had exceptional musical talent. While they aren't soldiers,
  chorals can defend themselves with their magical voices. Chorals sometimes visit
  the Material Plane with auspicious messages for mortals.

---

# Angel, Choral
This shimmering being looks like a miniature human with broad, iridescent wings and hair that slowly ripples through the air.
**Source** Bestiary 5 pg. 23, _[[items/Wondrous Item/Chronicle of the Righteous|Chronicle of the Righteous]]_ pg. 60
**XP** 2,400

NG Small outsider (angel, extraplanar, good)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Evil|detect evil]]_; Perception +16
**Aura** protective aura

##### Defense

**AC** 19, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+3 Dex, +5 natural, +1 size; +4 deflection vs. evil)
**hp** 68 (8d10+24)
**Fort** +6, **Ref** +9, **Will** +9; +4 vs. poison, +4 _[[universal monster rules/Resistance|resistance]]_ vs. evil
**DR** 5/evil; **Immune** acid, cold, petrification; **Resist** electricity 10, fire 10; **SR** 17

##### Offense
**Speed** 40 ft., fly 60 ft. (good)
**Melee** slam +10 (1d3+1)
**Ranged** piercing hymn +12 touch (4d6 sonic plus _[[conditions/Deafened|deafened]]_)
**Special Attacks** countersong, harmonize
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +11)
Constant—_detect evil_
At will—aid, _[[spells/Ghost Sound|ghost sound]]_ (DC 13), _[[spells/Dispel Evil|dispel evil]]_ (DC 18), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Invisibility|invisibility]]_ (self only), _[[spells/Plane Shift|plane shift]]_ (self only), _[[spells/Remove Curse|remove curse]]_, _[[spells/Remove Disease|remove disease]]_, _[[spells/Remove Fear|remove fear]]_
3/day—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Sculpt Sound|sculpt sound]]_ (DC 16), _[[spells/Sound Burst|sound burst]]_ (DC 15)

##### Statistics
**Str** 13, **Dex** 16, **Con** 15, **Int** 16, **Wis** 16, **Cha** 17
**Base Atk** +8; **CMB** +8; **CMD** 21
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Toughness|Toughness]]_
**Skills** Acrobatics +14, Diplomacy +14, Escape Artist +11, Fly +20, Knowledge (planes) +14, Knowledge (religion) +14, Perception +16, Perform (sing) +14, Sense Motive +16
**Languages** Celestial, Draconic, Infernal; truespeech

##### Ecology

**Environment** any good-aligned planes
**Organization** solo, duet, or _[[feats/Ensemble|Ensemble]]_ (3-8)
**Treasure** standard

### Special Abilities

**Countersong (Su)** A choral can attempt a Perform (sing) check to counter magic effects that depend on sound. This ability functions as the _[[classes/Bard|bard]]_ ability of the same name.

**Harmonize (Sp)** When chorals work together, they can use their complementary voices to create mystical harmonies. Two or more chorals within 60 feet of one another can use _[[spells/Calm Emotions|calm emotions]]_ or _[[spells/Heroism|heroism]]_ as a spell-like ability, four or more chorals can use _[[spells/Shout|shout]]_, and six or more chorals can use greater _heroism_ or _[[spells/Holy Word|holy word]]_. Only the choral that actually casts the spell-like ability in question must take a standard action to achieve this effect—the other chorals need only take swift actions during the same round.

**Piercing Hymn (Su)** As a standard action, a choral can launch a concentrated blast of sonic energy from its mouth as a ranged touch attack. This attack has a range of 90 feet with no range increment and deals 4d6 points of sonic damage. Any creature struck by a piercing hymn must succeed at a DC 17 Fortitude save or be _deafened_ for 1d4 minutes. The save DC is Charisma-based.

##### Description

Choral angels are singers of great skill, and their ranks fill the halls of good deities with soaring hymns and solemn chants. They manifest from the spirits of the pious dead who had exceptional musical talent. While they aren’t soldiers, chorals can defend themselves with their magical voices. Chorals sometimes visit the Material Plane with auspicious messages for mortals.
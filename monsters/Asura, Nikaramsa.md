---
cssclass: [monsters]
title1: Asura, Nikaramsa
desc_short: This muscular giant has two ferocious lion heads, each with a long, black,
  lashing tongue.
title2: Nikaramsa
CR: 14
sources:
- name: Book of the Damned
  page: 242
  link: http://paizo.com/products/btpy9tok
XP: 38400
alignment: LE
size: Large
type: outsider
subtypes:
- asura
- evil
- extraplanar
- lawful
initiative:
  bonus: 11
senses:
  darkvision: 60
  detect chaos: true
  detect evil: true
  detect good: true
  detect law: true
  see invisibility: true
auras:
- name: elusive
  radius: 75
AC:
  AC: 29
  touch: 17
  flat_footed: 21
  components:
    dex: 7
    dodge: 1
    natural: 12
    size: -1
HP:
  HP: 200
  long: 16d10+112
  regeneration: 10
  regeneration_weakness: good
saves:
  fort: 14
  ref: 17
  will: 17
  other: +2 vs. enchant.
DR:
- amount: 10
  weakness: good
immunities:
- curses
- disease
- poison
resistances:
  acid: 10
  electricity: 10
SR: 25
speeds:
  base: 50
  fly: 50
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 bites +20 (1d8+5)
      entries:
      - - damage: 1d8+5
      count: 2
      attack: bites
      bonus:
      - 20
    - text: 2 claws +20 (1d6+5)
      entries:
      - - damage: 1d6+5
      count: 2
      attack: claws
      bonus:
      - 20
    - text: 2 tongues +20 (1d6+5 plus trip)
      entries:
      - - damage: 1d6+5
        - effect: trip
      count: 2
      attack: tongues
      bonus:
      - 20
  special:
  - pervert miracle
  - rend (2 tongues, 1d6+7)
space: 10
reach: 10
reach_other: 20 ft. with tongues
spell_like_abilities:
  entries:
  - name: detect chaos
    source: default
    freq: Constant
  - name: detect evil
    source: default
    freq: Constant
  - name: detect good
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: invisibility
    source: default
    freq: At will
  - name: magic aura
    source: default
    freq: At will
  - name: veil
    source: default
    freq: At will
    other: self only
  - name: ventriloquism
    source: default
    freq: At will
    DC: 16
  - name: bless
    source: default
    freq: 3/day
  - name: cure serious wounds
    source: default
    freq: 3/day
  - name: good hope
    source: default
    freq: 3/day
  - name: neutralize poison
    source: default
    freq: 3/day
  - name: remove blindness/deafness
    source: default
    freq: 3/day
  - name: remove curse
    source: default
    freq: 3/day
  - name: remove disease
    source: default
    freq: 3/day
  - name: blasphemy
    source: default
    freq: 1/day
    DC: 22
  - name: dream
    source: default
    freq: 1/day
  - name: limited wish
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 6
    summons:
    - name: upasundas
      amount: 1d3
      chance: 50%
  sources:
  - name: default
    CL: 14
    concentration: 19
ability_scores:
  STR: 20
  DEX: 25
  CON: 25
  INT: 18
  WIS: 25
  CHA: 20
BAB: 16
CMB: 22
CMB_other: +24 trip
CMD: 40
CMD_other: 42 vs. trip
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Deflect ArrowsB
- name: Dodge
- name: Great Fortitude
- name: Improved Initiative
- name: Improved Trip
- name: Mobility
- name: Spring Attack
skills:
  Bluff: 24
  Disguise: 24
  Escape Artist: 32
  Fly: 24
  Knowledge (planes): 19
  Knowledge (religion): 19
  Perception: 30
  Sense Motive: 26
  Spellcraft: 20
  Stealth: 22
  Use Magic Device: 24
  _racial_mods:
    Escape Artist:
      _: 6
    Perception:
      _: 4
languages:
- Common
- Infernal
- telepathy 100 ft.
special_qualities:
- savor heresy
ecology:
  environment: any (Hell)
  organization: solitary or perversion (2-5)
  treasure_type: standard
special_abilities:
  Pervert Miracle (Su): As an immediate action, when a creature within 60 feet either
    casts a spell that a nikaramsa can use as a spell-like ability three times per
    day or casts a spell that would counter or remove one of those spells (i.e., bane,
    bestow curse, blindness/deafness, contagion, crushing despair, inflict serious
    wounds, or poison), the nikaramsa can attempt an opposed Charisma check against
    the caster. If successful, the nikaramsa converts the spell into its opposite
    against each original target as it's cast.
  Savor Heresy (Su): A nikaramsa gains a +2 profane bonus on attack rolls and a +5
    profane bonus on damage rolls against any creature that has committed an act of
    heresy or changed its alignment in the last year. Furthermore, the asura's natural
    attacks also ignore such a creature's damage reduction.
desc_long: A nikaramsa exploits the hubris and awe of mortal priests by disguising
  itself as a deity's chosen messenger and granting divine boons to a congregation,
  confusing believers by imparting more and more heretical lessons as gospel truths.
  The nikaramsa then corrupts the faith's blessings, causing the religion to collapse
  in the wake of its own clergy's atrocities.

---

# Asura, Nikaramsa
This muscular giant has two ferocious _[[monsters/Lion|lion]]_ heads, each with a long, black, lashing tongue.
**Source** _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_ pg. 242
**XP** 38,400

LE Large outsider (asura, evil, extraplanar, lawful)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Chaos|detect chaos]]_, _[[spells/Detect Evil|detect evil]]_, _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +30
**Aura** elusive (75 ft.)

##### Defense

**AC** 29, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+7 Dex, +1 dodge, +12 natural, -1 size)
**hp** 200 (16d10+112); _[[universal monster rules/Regeneration|regeneration]]_ 10 (good)
**Fort** +14, **Ref** +17, **Will** +17; +2 vs. enchant.
**DR** 10/good; **Immune** curses, disease, poison; **Resist** acid 10, electricity 10; **SR** 25

##### Offense
**Speed** 50 ft., fly 50 ft. (perfect)
**Melee** 2 bites +20 (1d8+5), 2 claws +20 (1d6+5), 2 _[[spells/Tongues|tongues]]_ +20 (1d6+5 plus _[[universal monster rules/Trip|trip]]_)
**Space** 10 ft., **Reach** 10 ft. (20 ft. with _tongues_)
**Special Attacks** pervert _[[spells/Miracle|miracle]]_, _[[universal monster rules/Rend|rend]]_ (2 _tongues_, 1d6+7)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +19)
Constant—_detect chaos_, _detect evil_, _detect good_, _detect law_, _see invisibility_
 At will—greater teleport (self plus 50 lbs. of objects only), _[[spells/Invisibility|invisibility]]_, _[[spells/Magic Aura|magic aura]]_, _[[spells/Veil|veil]]_ (self only), _[[spells/Ventriloquism|ventriloquism]]_ (DC 16)
3/day—_[[spells/Bless|bless]]_, _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Good Hope|good hope]]_, _[[spells/Neutralize Poison|neutralize poison]]_, remove blindness/deafness, _[[spells/Remove Curse|remove curse]]_, _[[spells/Remove Disease|remove disease]]_
1/day—_[[spells/Blasphemy|blasphemy]]_ (DC 22), _[[spells/Dream|dream]]_, _[[spells/Limited Wish|limited wish]]_, _[[universal monster rules/Summon|summon]]_ (level 6, 1d3 upasundas 50%)

##### Statistics
**Str** 20, **Dex** 25, **Con** 25, **Int** 18, **Wis** 25, **Cha** 20
**Base Atk** +16; **CMB** +22 (+24 _trip_); **CMD** 40 (42 vs. _trip_)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, Deflect ArrowsB, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Spring Attack|Spring Attack]]_
**Skills** Bluff +24, Disguise +24, Escape Artist +32, Fly +24, Knowledge (planes, religion) +19, Perception +30, Sense Motive +26, Spellcraft +20, Stealth +22, Use Magic Device +24; **Racial Modifiers** +6 Escape Artist, +4 Perception
**Languages** Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** savor heresy

##### Ecology

**Environment** any (Hell)
**Organization** solitary or perversion (2-5)
**Treasure** standard

### Special Abilities

**Pervert _Miracle_ (Su)** As an immediate action, when a creature within 60 feet either casts a spell that a nikaramsa can use as a spell-like ability three times per day or casts a spell that would counter or remove one of those spells (i.e., _[[spells/Bane|bane]]_, _[[spells/Bestow Curse|bestow curse]]_, blindness/deafness, _[[spells/Contagion|contagion]]_, _[[spells/Crushing Despair|crushing despair]]_, _[[spells/Inflict Serious Wounds|inflict serious wounds]]_, or poison), the nikaramsa can attempt an opposed Charisma check against the caster. If successful, the nikaramsa converts the spell into its opposite against each original target as it’s cast.
**Savor Heresy (Su)** A nikaramsa gains a +2 profane bonus on attack rolls and a +5 profane bonus on damage rolls against any creature that has committed an act of heresy or changed its alignment in the last year. Furthermore, the asura’s _[[universal monster rules/Natural Attacks|natural attacks]]_ also ignore such a creature’s _[[universal monster rules/Damage Reduction|damage reduction]]_.

##### Description

A nikaramsa exploits the hubris and awe of mortal priests by disguising itself as a deity’s chosen messenger and granting divine boons to a congregation, confusing believers by imparting more and more _[[items/Weapon Magic Abilities/Heretical|heretical]]_ lessons as gospel truths. The nikaramsa then corrupts the faith’s blessings, causing the religion to collapse in the wake of its own clergy’s atrocities.
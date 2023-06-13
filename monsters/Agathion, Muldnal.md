---
cssclass: [monsters]
title1: Agathion, Muldnal
desc_short: This diminutive, small-eyed creature is covered in dense, charcoal-gray
  fur and wears a dirt-stained smock; its pink nose twitches ceaselessly.
title2: Muldnal
CR: 3
sources:
- name: 'Pathfinder #117: Assault on Longshadow'
  page: 80
  link: http://paizo.com/products/btpy9p1h
XP: 800
alignment: NG
size: Small
type: outsider
subtypes:
- agathion
- extraplanar
- good
initiative:
  bonus: -1
senses:
  darkvision: 120
  detect snares and pits: true
  low-light vision: true
  tremorsense: 30
AC:
  AC: 14
  touch: 10
  flat_footed: 14
  components:
    dex: -1
    natural: 4
    size: 1
HP:
  HP: 38
  long: 4d10+16
saves:
  fort: 8
  ref: 3
  will: 6
  other: +4 vs. poison
DR:
- amount: 5
  weakness: evil or silver
immunities:
- electricity
- paralysis
- petrification
resistances:
  acid: 10
  cold: 10
  sonic: 10
SR: 14
weaknesses:
- light sensitivity
- revulsion
speeds:
  base: 20
  burrow: 40
attacks:
  melee:
  - - text: mwk quarterstaff +6 (1d4)
      entries:
      - - damage: 1d4
      attack: mwk quarterstaff
      bonus:
      - 6
  - - text: bite +5 (1d8 plus paralysis)
      entries:
      - - damage: 1d8
        - effect: paralysis
      attack: bite
      bonus:
      - 5
    - text: 2 claws +5 (1d3)
      entries:
      - - damage: 1d3
      count: 2
      attack: claws
      bonus:
      - 5
  special:
  - paralysis (1 round, DC 16)
spell_like_abilities:
  entries:
  - name: detect snares and pits
    source: default
    freq: Constant
  - name: create pit
    source: default
    freq: 3/day
    DC: 13
  - name: move earth
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: silvanshee
      amount: 1
      chance: 35%
  sources:
  - name: default
    CL: 4
    concentration: 5
spells:
  entries:
  - name: control vermin
    source: Druid
    level: 2
    DC: 17
  - name: soften earth and stone
    source: Druid
    level: 2
  - name: summon swarm
    source: Druid
    level: 2
  - name: call animal
    source: Druid
    level: 1
  - name: cure light wounds
    source: Druid
    level: 1
  - name: expeditious excavation
    source: Druid
    level: 1
  - name: shillelagh
    source: Druid
    level: 1
  - name: thunderstomp
    source: Druid
    level: 1
  - name: detect poison
    source: Druid
    level: 0
  - name: know direction
    source: Druid
    level: 0
  - name: purify food and drink
    source: Druid
    level: 0
    DC: 15
  - name: stabilize
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 4
    concentration: 9
ability_scores:
  STR: 11
  DEX: 9
  CON: 19
  INT: 10
  WIS: 20
  CHA: 12
BAB: 4
CMB: 3
CMD: 12
feats:
- name: Bludgeoner
- name: Vermin Heart
skills:
  Craft (traps): 11
  Knowledge (engineering): 11
  Knowledge (nature): 7
  Perception: 12
  Stealth: 10
    underground: 14
  Survival: 12
  _racial_mods:
    Craft (traps):
      _: 4
    Knowledge (engineering):
      _: 4
    Stealth:
      underground: 4
languages:
- Celestial
- Draconic
- Infernal
- speak with animals
- truespeech
special_qualities:
- dust child
- hold breath
- lay on hands (2d6, 3/day)
- wild empathy +1
ecology:
  environment: any underground (Nirvana)
  organization: solitary, pair, or labor (3-10)
  treasure_type: standard
special_abilities:
  Dust Child (Ex): Muldnals are innately attuned to the structure of the earth and
    stone around them. They gain a +4 racial bonus on Craft (traps) and Knowledge
    (engineering) checks.
  Revulsion (Ex): A muldnal is repelled by the presence of freshly spilled blood.
    When within 30 feet of a creature that is taking bleed damage, or if a muldnal
    is taking bleed damage itself, the muldnal must succeed at a DC 17 Will saving
    throw each round or become shaken until the start of the next round or until the
    bleeding creature is healed. In addition, a muldnal can't use its burrow or earth
    glide abilities while under the effects of revulsion. A muldnal that successfully
    saves against revulsion can't be affected by the same source of blood for 24 hours.
  Spells: A muldnal prepares spells as per a druid of a level equal to its Hit Dice,
    with a focus on animal-, earth-, and vermin-related spells.
desc_long: |-
  Muldnals' appearance does not immediately command respect. They stand roughly 3 feet in height, and their wide, dirt-encrusted, clawed hands and equally filthy smocks of undyed linen belie their true extraplanar nature. Dense fur of black, brown, and gray coats their muscular bodies, while a pink nose and whiskers twitch as they sense their surrounding environment, their small black eyes lost in the fur and dirt on their bodies.

   While the ferocious leonal agathions guard the portals to Nirvana, the overlooked muldnals tend to the innumerable underground passages of that plane. When found on the Material Plane, a muldnal tends to sites of magical power associated with agriculture and nature. Many people have been fooled by their friendly and furred countenances; when provoked, a muldnal uses both a paralytic bite and command over the earth to drive off its enemies.

---

# Agathion, Muldnal
This diminutive, small-eyed creature is covered in dense, charcoal-gray fur and wears a dirt-stained smock; its pink nose twitches ceaselessly.
**Source** Pathfinder #117: Assault on Longshadow pg. 80
**XP** 800

NG Small outsider (agathion, extraplanar, good)
**Init** –1; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[spells/Detect Snares and Pits|detect snares and pits]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 30 ft.; Perception +12

##### Defense

**AC** 14, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 14 (–1 Dex, +4 natural, +1 size)
**hp** 38 (4d10+16)
**Fort** +8, **Ref** +3, **Will** +6; +4 vs. poison
**DR** 5/evil or silver; **Immune** electricity, _[[universal monster rules/Paralysis|paralysis]]_, petrification; **Resist** acid 10, cold 10, sonic 10; **SR** 14
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_, revulsion

##### Offense
**Speed** 20 ft., _[[universal monster rules/Burrow|burrow]]_ 40 ft.
**Melee** mwk _[[items/Weapon/Quarterstaff|quarterstaff]]_ +6 (1d4) or bite +5 (1d8 plus _paralysis_), 2 claws +5 (1d3)
**Special Attacks** _paralysis_ (1 round, DC 16)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +5)
Constant—_detect snares and pits_
3/day—_[[spells/Create Pit|create pit]]_ (DC 13)
1/day—_[[spells/Move Earth|move earth]]_, _[[universal monster rules/Summon|summon]]_ (level 4, 1 silvanshee 35%)
**_[[classes/Druid|Druid]]_ Spells Prepared **(CL 4th; concentration +9)
2nd—_[[spells/Control Vermin|control vermin]]_ (DC 17), _[[spells/Soften Earth and Stone|soften earth and stone]]_, _[[spells/Summon Swarm|summon swarm]]_
1st—_[[spells/Call Animal|call animal]]_, _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Expeditious Excavation|expeditious excavation]]_, _[[spells/Shillelagh|shillelagh]]_, _[[spells/Thunderstomp|thunderstomp]]_
0—_[[spells/Detect Poison|detect poison]]_, _[[spells/Know Direction|know direction]]_, _[[spells/Purify Food and Drink|purify food and drink]]_ (DC 15), stabilize

##### Statistics
**Str** 11, **Dex** 9, **Con** 19, **Int** 10, **Wis** 20, **Cha** 12
**Base Atk** +4; **CMB** +3; **CMD** 12
**Feats** _[[feats/Bludgeoner|Bludgeoner]]_, _[[feats/Vermin Heart|Vermin Heart]]_
**Skills** Craft (traps) +11, Knowledge (engineering) +11, Knowledge (nature) +7, Perception +12, Stealth +10 (+14 underground), Survival +12; **Racial Modifiers** +4 Craft (traps), +4 Knowledge (engineering), +4 Stealth underground
**Languages** Celestial, Draconic, Infernal; _[[spells/Speak with Animals|speak with animals]]_, truespeech
**SQ** dust child, _[[universal monster rules/Hold Breath|hold breath]]_, lay on hands (2d6, 3/day), wild _[[feats/Empathy|empathy]]_ +1

##### Ecology

**Environment** any underground (Nirvana)
**Organization** solitary, pair, or labor (3–10)
**Treasure** standard

### Special Abilities

**Dust Child (Ex)** Muldnals are innately attuned to the structure of the earth and stone around them. They gain a +4 racial bonus on Craft (traps) and Knowledge (engineering) checks.

**Revulsion (Ex)** A muldnal is repelled by the presence of freshly spilled blood. When within 30 feet of a creature that is taking _[[universal monster rules/Bleed|bleed]]_ damage, or if a muldnal is taking _bleed_ damage itself, the muldnal must succeed at a DC 17 Will saving throw each round or become _[[conditions/Shaken|shaken]]_ until the start of the next round or until the bleeding creature is healed. In addition, a muldnal can’t use its _burrow_ or _[[universal monster rules/Earth Glide|earth glide]]_ abilities while under the effects of revulsion. A muldnal that successfully saves against revulsion can’t be affected by the same source of blood for 24 hours.
**Spells** A muldnal prepares spells as per a _druid_ of a level equal to its Hit Dice, with a focus on animal-, earth-, and vermin-related spells.

##### Description

Muldnals’ appearance does not immediately _[[spells/Command|command]]_ respect. They stand roughly 3 feet in height, and their wide, dirt-encrusted, clawed hands and equally filthy smocks of undyed linen belie their true extraplanar nature. Dense fur of black, brown, and _[[monsters/Gray|gray]]_ coats their muscular bodies, while a pink nose and whiskers twitch as they sense their surrounding environment, their small black eyes lost in the fur and dirt on their bodies.

While the ferocious leonal agathions _[[npcs/Guard|guard]]_ the portals to Nirvana, the overlooked muldnals tend to the innumerable underground passages of that plane. When found on the Material Plane, a muldnal tends to sites of magical power associated with agriculture and nature. Many people have been fooled by their friendly and furred countenances; when provoked, a muldnal uses both a paralytic bite and _command_ over the earth to drive off its enemies.
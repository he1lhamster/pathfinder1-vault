---
cssclass: [monsters]
title1: Angel, Planetar
desc_short: Muscular, bald, and tall, this humanoid creature has emerald skin and
  two pairs of shining, white-feathered wings.
title2: Planetar
CR: 16
sources:
- name: Pathfinder RPG Bestiary
  page: 11
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 76800
alignment: NG
size: Large
type: outsider
subtypes:
- angel
- extraplanar
- good
initiative:
  bonus: 8
senses:
  darkvision: 60
  detect evil: true
  detect snares and pits: true
  low-light vision: true
  true seeing: true
auras:
- name: protective aura
AC:
  AC: 32
  touch: 13
  flat_footed: 28
  components:
    dex: 4
    natural: 19
    size: -1
    deflection vs. evil: 4
HP:
  HP: 229
  long: 17d10+136
  regeneration: 10
  regeneration_weakness: evil weapons and effects
saves:
  fort: 19
  ref: 11
  will: 19
  other: +4 vs. poison, +4 resistance vs. evil
DR:
- amount: 10
  weakness: evil
immunities:
- acid
- cold
- petrification
resistances:
  electricity: 10
  fire: 10
SR: 27
speeds:
  base: 30
  fly: 90
  fly_maneuverability: good
attacks:
  melee:
  - - text: +3 holy greatsword +27/+22/+17 (3d6+15/19-20)
      entries:
      - - damage: 3d6+15
          crit_range: 19-20
      attack: +3 holy greatsword
      bonus:
      - 27
      - 22
      - 17
  - - text: slam +24 (2d8+12)
      entries:
      - - damage: 2d8+12
      attack: slam
      bonus:
      - 24
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: detect snares and pits
    source: default
    freq: Constant
  - name: discern lies
    source: default
    freq: Constant
    DC: 20
  - name: true seeing
    source: default
    freq: Constant
  - name: continual flame
    source: default
    freq: At will
  - name: dispel magic
    source: default
    freq: At will
  - name: holy smite
    source: default
    freq: At will
    DC: 21
  - name: invisibility
    source: default
    freq: At will
    other: self only
  - name: lesser restoration
    source: default
    freq: At will
  - name: remove curse
    source: default
    freq: At will
  - name: remove disease
    source: default
    freq: At will
  - name: remove fear
    source: default
    freq: At will
    DC: 18
  - name: speak with dead
    source: default
    freq: At will
    DC: 20
  - name: blade barrier
    source: default
    freq: 3/day
    DC: 21
  - name: flame strike
    source: default
    freq: 3/day
    DC: 22
  - name: power word stun
    source: default
    freq: 3/day
  - name: raise dead
    source: default
    freq: 3/day
  - name: waves of fatigue
    source: default
    freq: 3/day
  - name: earthquake
    source: default
    freq: 1/day
    DC: 25
  - name: greater restoration
    source: default
    freq: 1/day
  - name: mass charm monster
    source: default
    freq: 1/day
    DC: 25
  - name: waves of exhaustion
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 16
spells:
  entries:
  - name: earthquake
    source: '?'
    level: 8
    DC: 25
  - name: fire storm
    source: '?'
    level: 8
    DC: 25
  - name: holy word
    source: '?'
    level: 7
    DC: 24
  - name: regenerate
    source: '?'
    level: 7
    count: 2
  - name: banishment
    source: '?'
    level: 6
    DC: 23
  - name: greater dispel magic
    source: '?'
    level: 6
  - name: heal
    source: '?'
    level: 6
  - name: mass cure moderate wounds
    source: '?'
    level: 6
    DC: 23
  - name: break enchantment
    source: '?'
    level: 5
  - name: dispel evil
    source: '?'
    level: 5
    count: 2
    DC: 22
  - name: plane shift
    source: '?'
    level: 5
    DC: 22
  - name: righteous might
    source: '?'
    level: 5
  - name: death ward
    source: '?'
    level: 4
  - name: dismissal
    source: '?'
    level: 4
    DC: 21
  - name: neutralize poison
    source: '?'
    level: 4
    DC: 21
  - name: summon monster IV
    source: '?'
    level: 4
  - name: cure serious wounds
    source: '?'
    level: 3
    count: 2
  - name: daylight
    source: '?'
    level: 3
  - name: invisibility purge
    source: '?'
    level: 3
  - name: summon monster III
    source: '?'
    level: 3
  - name: wind wall
    source: '?'
    level: 3
  - name: align weapon
    source: '?'
    level: 2
    count: 2
  - name: bear's endurance
    source: '?'
    level: 2
    count: 2
  - name: cure moderate wounds
    source: '?'
    level: 2
    count: 2
  - name: eagle's splendor
    source: '?'
    level: 2
  - name: bless
    source: '?'
    level: 1
    count: 2
  - name: cure light wounds
    source: '?'
    level: 1
    count: 4
  - name: shield of faith
    source: '?'
    level: 1
  - name: detect magic
    source: '?'
    level: 0
  - name: purify food and drink
    source: '?'
    level: 0
  - name: stabilize
    source: '?'
    level: 0
  - name: virtue
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: prepared
    CL: 16
    slots:
      0: at-will
ability_scores:
  STR: 27
  DEX: 19
  CON: 24
  INT: 22
  WIS: 25
  CHA: 24
BAB: 17
CMB: 26
CMD: 40
feats:
- name: Blind-Fight
- name: Cleave
- name: Great Fortitude
- name: Improved Initiative
- name: Improved Sunder
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
- name: Toughness
skills:
  Acrobatics: 24
  Craft (any one): 26
  Diplomacy: 27
  Fly: 26
  Heal: 24
  Intimidate: 27
  Knowledge (history): 23
  Knowledge (planes): 26
  Knowledge (religion): 26
  Perception: 27
  Sense Motive: 27
  Stealth: 20
languages:
- Celestial
- Draconic
- Infernal
- truespeech
special_qualities:
- change shape (alter self)
ecology:
  environment: any good-aligned plane
  organization: solitary or pair
  treasure_type: double
  treasure:
  - +3 holy greatsword
special_abilities:
  Spells: Planetars cast divine spells as 16th-level clerics. They do not gain access
    to domains or other cleric abilities.
desc_long: Planetars are the generals of celestial armies. A typical planetar stands
  9 feet tall and weighs 500 pounds. They focus on combat and the destruction of evil;
  though they understand diplomacy, a planetar would rather lead the charge against
  an army of fiends than negotiate peace.

---

# Angel, Planetar
Muscular, bald, and tall, this humanoid creature has emerald skin and two pairs of shining, white-feathered wings.
**Source** Pathfinder RPG Bestiary pg. 11
**XP** 76,800

NG Large outsider (angel, extraplanar, good)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Evil|detect evil]]_, _[[spells/Detect Snares and Pits|detect snares and pits]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/True Seeing|true seeing]]_; Perception +27
**Aura** protective aura

##### Defense

**AC** 32, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+4 Dex, +19 natural, –1 size; +4 deflection vs. evil)
**hp** 229 (17d10+136); _[[universal monster rules/Regeneration|regeneration]]_ 10 (evil weapons and effects)
**Fort** +19, **Ref** +11, **Will** +19; +4 vs. poison, +4 _[[universal monster rules/Resistance|resistance]]_ vs. evil
**DR** 10/evil; **Immune** acid, cold, petrification; **Resist** electricity 10, fire 10; **SR** 27

##### Offense
**Speed** 30 ft., fly 90 ft. (good)
**Melee** +3 holy _[[items/Weapon/Greatsword|greatsword]]_ +27/+22/+17 (3d6+15/19–20) or slam +24 (2d8+12)
**Space** 10 ft., **Reach** 10 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th)
Constant—_detect evil_, _detect snares and pits_, _[[spells/Discern Lies|discern lies]]_ (DC 20), _true seeing_
At will—_[[spells/Continual Flame|continual flame]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Holy Smite|holy smite]]_ (DC 21), _[[spells/Invisibility|invisibility]]_ (self only), lesser _[[spells/Restoration|restoration]]_, _[[spells/Remove Curse|remove curse]]_, _[[spells/Remove Disease|remove disease]]_, _[[spells/Remove Fear|remove fear]]_ (DC 18), _[[spells/Speak with Dead|speak with dead]]_ (DC 20)
3/day—_[[spells/Blade Barrier|blade barrier]]_ (DC 21), _[[spells/Flame Strike|flame strike]]_ (DC 22), _[[spells/Power Word Stun|power word stun]]_, _[[spells/Raise Dead|raise dead]]_, _[[spells/Waves of Fatigue|waves of fatigue]]_
1/day—_[[spells/Earthquake|earthquake]]_ (DC 25), greater _restoration_, mass _[[spells/Charm Monster|charm monster]]_ (DC 25), _[[spells/Waves of Exhaustion|waves of exhaustion]]_
**Spells Prepared **(CL 16th)
8th—_earthquake_ (DC 25), _[[spells/Fire Storm|fire storm]]_ (DC 25)
7th—_[[spells/Holy Word|holy word]]_ (DC 24), _[[spells/Regenerate|regenerate]]_ (2)
6th—_[[spells/Banishment|banishment]]_ (DC 23), greater _dispel magic_, _[[spells/Heal, Mass|heal, mass]]_ _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (DC 23)
5th—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Dispel Evil|dispel evil]]_ (2, DC 22), _[[spells/Plane Shift|plane shift]]_ (DC 22), _[[spells/Righteous Might|righteous might]]_
4th—_[[spells/Death Ward|death ward]]_, _[[spells/Dismissal|dismissal]]_ (DC 21), _[[spells/Neutralize Poison|neutralize poison]]_ (DC 21), _[[spells/Summon Monster IV|summon monster IV]]_
3rd—_[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), _[[spells/Daylight|daylight]]_, _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Summon Monster III|summon monster III]]_, _[[spells/Wind Wall|wind wall]]_
2nd—_[[spells/Align Weapon|align weapon]]_ (2), bear’s _[[feats/Endurance|endurance]]_ (2), _cure moderate wounds_ (2), _[[monsters/Eagle|eagle]]_’s splendor
1st—_[[spells/Bless|bless]]_ (2), _[[spells/Cure Light Wounds|cure light wounds]]_ (4), _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Purify Food and Drink|purify food and drink]]_, stabilize, _[[spells/Virtue|virtue]]_

##### Statistics
**Str** 27, **Dex** 19, **Con** 24, **Int** 22, **Wis** 25, **Cha** 24
**Base Atk** +17; **CMB** +26; **CMD** 40
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_
**Skills** Acrobatics +24, Craft (any one) +26, Diplomacy +27, Fly +26, _[[spells/Heal|Heal]]_ +24, Intimidate +27, Knowledge (history) +23, Knowledge (planes) +26, Knowledge (religion) +26, Perception +27, Sense Motive +27, Stealth +20
**Languages** Celestial, Draconic, Infernal; truespeech
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_[[spells/Alter Self|alter self]]_)

##### Ecology

**Environment** any good-aligned plane
**Organization** solitary or pair
**Treasure** double (+3 holy _greatsword_)

### Special Abilities
**Spells **Planetars cast divine spells as 16th-level clerics. They do not gain access to domains or other _[[classes/Cleric|cleric]]_ abilities.

##### Description

Planetars are the generals of celestial armies. A typical planetar stands 9 feet tall and weighs 500 pounds. They focus on combat and the _[[spells/Destruction|destruction]]_ of evil; though they understand diplomacy, a planetar would rather lead the charge against an army of fiends than negotiate peace.
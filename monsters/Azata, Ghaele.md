---
cssclass: [monsters]
title1: Azata, Ghaele
desc_short: This elegantly armored sentinel stands alert, her eyes radiating divine
  light and her noble blade crackling with power.
title2: Ghaele
CR: 13
sources:
- name: Pathfinder RPG Bestiary
  page: 25
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 25600
alignment: CG
size: Medium
type: outsider
subtypes:
- azata
- chaotic
- extraplanar
- good
- shapechanger
initiative:
  bonus: 5
senses:
  darkvision: 60
  detect evil: true
  low-light vision: true
  see invisibility: true
auras:
- name: holy aura
AC:
  AC: 28
  touch: 16
  flat_footed: 26
  components:
    deflection: 4
    dex: 1
    dodge: 1
    natural: 12
HP:
  HP: 136
  long: 13d10+65
saves:
  fort: 17
  ref: 11
  will: 16
DR:
- amount: 10
  weakness: cold iron and evil
immunities:
- electricity
- petrification
resistances:
  cold: 10
  fire: 10
SR: 25
speeds:
  base: 50
  fly: 150
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: +2 holy greatsword +22/+17/+12 (2d6+12)
      entries:
      - - damage: 2d6+12
      attack: +2 holy greatsword
      bonus:
      - 22
      - 17
      - 12
  ranged:
  - - text: 2 light rays +14 ranged touch (2d12)
      entries:
      - - damage: 2d12
      count: 2
      attack: light rays
      bonus:
      - 14
      touch: true
  special:
  - gaze
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: holy aura
    source: default
    freq: Constant
    DC: 21
  - name: see invisibility
    source: default
    freq: Constant
  - name: aid
    source: default
    freq: At will
  - name: charm monster
    source: default
    freq: At will
    DC: 17
  - name: continual flame
    source: default
    freq: At will
  - name: cure light wounds
    source: default
    freq: At will
  - name: dancing lights
    source: default
    freq: At will
  - name: detect thoughts
    source: default
    freq: At will
    DC: 15
  - name: disguise self
    source: default
    freq: At will
  - name: dispel magic
    source: default
    freq: At will
  - name: hold monster
    source: default
    freq: At will
    DC: 18
  - name: greater invisibility
    source: default
    freq: At will
    other: self only
  - name: major image
    source: default
    freq: At will
    DC: 16
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: globe of invulnerability
    source: default
    freq: 3/day
  - name: chain lightning
    source: default
    freq: 1/day
    DC: 19
  - name: prismatic spray
    source: default
    freq: 1/day
    DC: 20
  - name: wall of force
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 13
spells:
  entries:
  - name: holy word
    source: '?'
    level: 7
    DC: 21
  - name: banishment
    source: '?'
    level: 6
    DC: 20
  - name: heal
    source: '?'
    level: 6
    DC: 20
  - name: flame strike
    source: '?'
    level: 5
    DC: 19
  - name: raise dead
    source: '?'
    level: 5
  - name: true seeing
    source: '?'
    level: 5
  - name: death ward
    source: '?'
    level: 4
  - name: dismissal
    source: '?'
    level: 4
    count: 2
    DC: 18
  - name: divine power
    source: '?'
    level: 4
  - name: restoration
    source: '?'
    level: 4
  - name: cure serious wounds
    source: '?'
    level: 3
    count: 3
  - name: searing light
    source: '?'
    level: 3
    count: 2
  - name: aid
    source: '?'
    level: 2
  - name: align weapon
    source: '?'
    level: 2
  - name: bear's endurance
    source: '?'
    level: 2
  - name: lesser restoration
    source: '?'
    level: 2
    count: 2
  - name: bless
    source: '?'
    level: 1
  - name: command
    source: '?'
    level: 1
    DC: 15
  - name: divine favor
    source: '?'
    level: 1
  - name: obscuring mist
    source: '?'
    level: 1
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
    CL: 13
    slots:
      0: at-will
ability_scores:
  STR: 25
  DEX: 12
  CON: 20
  INT: 16
  WIS: 19
  CHA: 17
BAB: 13
CMB: 20
CMD: 31
feats:
- name: Combat Casting
- name: Combat Expertise
- name: Dodge
- name: Improved Disarm
- name: Improved Initiative
- name: Improved Trip
- name: Lightning Reflexes
skills:
  Diplomacy: 19
  Escape Artist: 17
  Fly: 25
  Handle Animal: 19
  Knowledge (nature): 16
  Knowledge (planes): 19
  Perception: 20
  Sense Motive: 20
  Stealth: 17
languages:
- Celestial
- Draconic
- Infernal
- truespeech
special_qualities:
- light form
ecology:
  environment: any (Elysium)
  organization: solitary, pair, or squad (3-6)
  treasure_type: triple
  treasure:
  - +2 holy greatsword
special_abilities:
  Gaze (Su): In humanoid form, a ghaele's gaze attack slays evil creatures of 5 HD
    or less (range 60 feet, Will DC 18 negates, shaken for 2d10 rounds on a successful
    save). Nonevil creatures, and evil creatures with more than 5 HD, must succeed
    on a DC 18 Will save or be shaken for 2d10 rounds. A creature that saves against
    a ghaele's gaze is immune to that particular ghaele's gaze for 24 hours. This
    is a mind-affecting fear effect. The save DCs are Charisma-based.
  Light Form (Su): A ghaele can shift between its solid body and one made of light
    as a standard action. In solid form, it cannot fly or use light rays. In light
    form, it can fly and gains the incorporeal quality-it can make light ray attacks
    or use spell-like abilities in this form, but can't make physical attacks or cast
    spells. This ability otherwise functions similarly to a bralani's wind form ability.
  Light Ray (Ex): A ghaele's light rays have a range of 300 feet. This attack bypasses
    all damage reduction.
  Spells: Ghaeles cast divine spells as 13th-level clerics. They do not gain access
    to domains or other cleric abilities.
desc_long: Ghaeles are the most knightly of the azatas, hunting fiends, dragons, and
  undead with equal vigor. Most appear like idealized humans or elves and are quick
  to smile-and equally quick to strike against those they perceive as wicked.

---

# Azata, Ghaele
This elegantly armored sentinel stands alert, her eyes radiating divine light and her noble blade crackling with power.
**Source** Pathfinder RPG Bestiary pg. 25
**XP** 25,600

CG Medium outsider (azata, chaotic, extraplanar, good, shapechanger)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Evil|detect evil]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +20
**Aura** _[[spells/Holy Aura|holy aura]]_

##### Defense

**AC** 28, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+4 _[[spells/Deflection|deflection]]_, +1 Dex, +1 _[[feats/Dodge|dodge]]_, +12 natural)
**hp** 136 (13d10+65)
**Fort** +17, **Ref** +11, **Will** +16
**DR** 10/cold iron and evil; **Immune** electricity, petrification; **Resist** cold 10, fire 10; **SR** 25

##### Offense
**Speed** 50 ft., fly 150 ft. (perfect)
**Melee** +2 holy _[[items/Weapon/Greatsword|greatsword]]_ +22/+17/+12 (2d6+12)
**Ranged** 2 light rays +14 ranged touch (2d12)
**Special Attacks** _[[universal monster rules/Gaze|gaze]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th)
Constant—_detect evil_, _holy aura_ (DC 21), _see invisibility_
At will—aid, _[[spells/Charm Monster|charm monster]]_ (DC 17), _[[spells/Continual Flame|continual flame]]_, _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 15), _[[spells/Disguise Self|disguise self]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Hold Monster|hold monster]]_ (DC 18), greater _[[spells/Invisibility|invisibility]]_ (self only), _[[spells/Major Image|major image]]_ (DC 16), greater teleport (self plus 50 lbs. of objects only)
3/day—_[[spells/Globe Of Invulnerability|globe of invulnerability]]_
1/day—_[[spells/Chain Lightning|chain lightning]]_ (DC 19), _[[spells/Prismatic Spray|prismatic spray]]_ (DC 20), _[[spells/Wall Of Force|wall of force]]_
**Spells Prepared **(CL 13th)
7th—_[[spells/Holy Word|holy word]]_ (DC 21)
6th—_[[spells/Banishment|banishment]]_ (DC 20), _[[spells/Heal|heal]]_ (DC 20)
5th—_[[spells/Flame Strike|flame strike]]_ (DC 19), _[[spells/Raise Dead|raise dead]]_, _[[spells/True Seeing|true seeing]]_
4th—_[[spells/Death Ward|death ward]]_, _[[spells/Dismissal|dismissal]]_ (2) (DC 18), _[[spells/Divine Power|divine power]]_, _[[spells/Restoration|restoration]]_
3rd—_[[spells/Cure Serious Wounds|cure serious wounds]]_ (3), _[[spells/Searing Light|searing light]]_ (2)
2nd—aid, _[[spells/Align Weapon|align weapon]]_, bear’s _[[feats/Endurance|endurance]]_, lesser _restoration_ (2)
1st—_[[spells/Bless|bless]]_, _[[spells/Command|command]]_ (DC 15), _[[spells/Divine Favor|divine favor]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Purify Food and Drink|purify food and drink]]_, stabilize, _[[spells/Virtue|virtue]]_

##### Statistics
**Str** 25, **Dex** 12, **Con** 20, **Int** 16, **Wis** 19, **Cha** 17
**Base Atk** +13; **CMB** +20; **CMD** 31
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _Dodge_, _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Diplomacy +19, Escape Artist +17, Fly +25, Handle Animal +19, Knowledge (nature) +16, Knowledge (planes) +19, Perception +20, Sense Motive +20, Stealth +17
**Languages** Celestial, Draconic, Infernal; truespeech
**SQ** light form

##### Ecology

**Environment** any (Elysium)
**Organization** solitary, pair, or squad (3–6)
**Treasure** triple (+2 holy _greatsword_)

### Special Abilities

**_Gaze_ (Su) **In humanoid form, a ghaele’s _gaze_ attack slays evil creatures of 5 HD or less (range 60 feet, Will DC 18 negates, _[[conditions/Shaken|shaken]]_ for 2d10 rounds on a successful save). Nonevil creatures, and evil creatures with more than 5 HD, must succeed on a DC 18 Will save or be _shaken_ for 2d10 rounds. A creature that saves against a ghaele’s _gaze_ is immune to that particular ghaele’s _gaze_ for 24 hours. This is a mind-affecting _[[universal monster rules/Fear|fear]]_ effect. The save DCs are Charisma-based.

**Light Form (Su) **A ghaele can shift between its solid body and one made of light as a standard action. In solid form, it cannot fly or use light rays. In light form, it can fly and gains the _[[universal monster rules/Incorporeal|incorporeal]]_ quality—it can make light ray attacks or use _spell-like abilities_ in this form, but can’t make physical attacks or cast spells. This ability otherwise functions similarly to a bralani’s wind form ability.

**Light Ray (Ex) **A ghaele’s light rays have a range of 300 feet. This attack bypasses all _[[universal monster rules/Damage Reduction|damage reduction]]_.
**Spells **Ghaeles cast divine spells as 13th-level clerics. They do not gain access to domains or other _[[classes/Cleric|cleric]]_ abilities.

##### Description

Ghaeles are the most knightly of the azatas, hunting fiends, dragons, and undead with equal _[[spells/Vigor|vigor]]_. Most appear like idealized humans or elves and are quick to smile—and equally quick to strike against those they perceive as wicked.
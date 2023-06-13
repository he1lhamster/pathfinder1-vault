---
cssclass: [monsters]
title1: Angel, Empyrean
desc_short: Light spills out through cracks in this humanoid being's clothing and
  armor, and its four wings are composed of wispy blue light.
title2: Empyrean
CR: 20
sources:
- name: Bestiary 5
  page: 24
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 307200
alignment: NG
size: Large
type: outsider
subtypes:
- angel
- extraplanar
- good
initiative:
  bonus: 12
senses:
  darkvision: 60
  low-light vision: true
  detect evil: true
  detect snares and pits: true
  true seeing: true
auras:
- name: protective aura
AC:
  AC: 38
  touch: 38
  flat_footed: 30
  components:
    dex: 8
    insight: 7
    sacred: 14
    size: -1
    deflection vs. evil: 4
HP:
  HP: 387
  long: 25d10+250
  regeneration: 15
  regeneration_weakness: evil artifacts
saves:
  fort: 24
  ref: 18
  will: 24
  other: +4 vs. poison, +4 resistance vs. evil
defensive_abilities:
- heed no call
- uncanny dodge
DR:
- amount: 15
  weakness: piercing and evil
immunities:
- acid
- cold
- petrification
resistances:
  electricity: 10
  fire: 10
SR: 31
speeds:
  base: 50
  fly: 120
  fly_maneuverability: good
attacks:
  melee:
  - - text: +1 holy merciful halberd +36/+31/+26/+21 (2d8+16/19-20/×3) or
      entries: []
      attack: +1 holy merciful halberd +36/+31/+26/+21 (2d8+16/19-20/×3) or
  ranged:
  - - text: +1 holy merciful composite longbow +33/+28/+23/+18 (2d6+11/×3)
      entries:
      - - damage: 2d6+11
          crit_multiplier: 3
      attack: +1 holy merciful composite longbow
      bonus:
      - 33
      - 28
      - 23
      - 18
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
    DC: 21
  - name: true seeing
    source: default
    freq: Constant
  - name: aid
    source: default
    freq: At will
  - name: atonement
    source: default
    freq: At will
  - name: break enchantment
    source: default
    freq: At will
  - name: commune
    source: default
    freq: At will
  - name: continual flame
    source: default
    freq: At will
  - name: dimensional anchor
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: lesser restoration
    source: default
    freq: At will
  - name: mark of justice
    source: default
    freq: At will
  - name: neutralize poison
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
  - name: resist energy
    source: default
    freq: At will
  - name: speak with dead
    source: default
    freq: At will
  - name: blade barrier
    source: default
    freq: 3/day
    DC: 23
  - name: dispel evil
    source: default
    freq: 3/day
    DC: 22
  - name: heal
    source: default
    freq: 3/day
    DC: 23
  - name: mass charm monster
    source: default
    freq: 3/day
    DC: 25
  - name: permanency
    source: default
    freq: 3/day
  - name: resurrection
    source: default
    freq: 3/day
  - name: sympathy
    source: default
    freq: 3/day
    DC: 25
  - name: greater restoration
    source: default
    freq: 1/day
  - name: power word stun
    source: default
    freq: 1/day
  - name: wish
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 20
    concentration: 27
spells:
  entries:
  - name: gate
    source: Cleric
    level: 9
  - name: mass heal
    source: Cleric
    level: 9
    DC: 29
  - name: miracle
    source: Cleric
    level: 9
  - name: overwhelming presence
    source: Cleric
    level: 9
    DC: 29
  - name: quickened righteous might
    source: Cleric
    level: 9
  - name: antimagic field
    source: Cleric
    level: 8
  - name: discern location
    source: Cleric
    level: 8
  - name: quickened divine power
    source: Cleric
    level: 8
  - name: greater spell immunity
    source: Cleric
    level: 8
  - name: holy aura
    source: Cleric
    level: 8
    DC: 28
  - name: control weather
    source: Cleric
    level: 7
  - name: holy word
    source: Cleric
    level: 7
    DC: 27
  - name: greater scrying
    source: Cleric
    level: 7
    DC: 27
  - name: repulsion
    source: Cleric
    level: 7
    DC: 27
  - name: waves of ecstasy
    source: Cleric
    level: 7
    DC: 27
  - name: heal
    source: Cleric
    level: 6
    DC: 26
  - name: heroes' feast
    source: Cleric
    level: 6
  - name: joyful rapture
    source: Cleric
    level: 6
  - name: quickened silence
    source: Cleric
    level: 6
    DC: 22
  - name: wind walk
    source: Cleric
    level: 6
  - name: word of recall
    source: Cleric
    level: 6
  - name: breath of life
    source: Cleric
    level: 5
  - name: quickened divine favor
    source: Cleric
    level: 5
  - name: fickle winds
    source: Cleric
    level: 5
  - name: greater command
    source: Cleric
    level: 5
    DC: 25
  - name: plane shift
    source: Cleric
    level: 5
    DC: 25
  - name: serenity
    source: Cleric
    level: 5
    DC: 25
  - name: death ward
    source: Cleric
    level: 4
  - name: dismissal
    source: Cleric
    level: 4
    DC: 24
  - name: divine power
    source: Cleric
    level: 4
  - name: freedom of movement
    source: Cleric
    level: 4
  - name: greater magic weapon
    source: Cleric
    level: 4
    count: 2
  - name: daylight
    source: Cleric
    level: 3
  - name: invisibility purge
    source: Cleric
    level: 3
  - name: locate object
    source: Cleric
    level: 3
  - name: prayer
    source: Cleric
    level: 3
  - name: stone shape
    source: Cleric
    level: 3
  - name: wind wall
    source: Cleric
    level: 3
  - name: consecrate
    source: Cleric
    level: 2
  - name: find traps
    source: Cleric
    level: 2
  - name: grace
    source: Cleric
    level: 2
    count: 2
  - name: make whole
    source: Cleric
    level: 2
  - name: remove paralysis
    source: Cleric
    level: 2
  - name: silence
    source: Cleric
    level: 2
    DC: 22
  - name: bless
    source: Cleric
    level: 1
  - name: divine favor
    source: Cleric
    level: 1
  - name: endure elements
    source: Cleric
    level: 1
  - name: obscuring mist
    source: Cleric
    level: 1
    count: 2
  - name: remove sickness
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
  - name: create water
    source: Cleric
    level: 0
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: purify food and drink
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 20
    concentration: 30
ability_scores:
  STR: 30
  DEX: 27
  CON: 30
  INT: 23
  WIS: 30
  CHA: 25
BAB: 25
CMB: 36
CMD: 75
feats:
- name: Combat Reflexes
- name: Dazing Assault
- name: Deadly Aim
- name: Furious Focus
- name: Improved Critical (halberd)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Manyshot
- name: Point-Blank Shot
- name: Power Attack
- name: Quicken Spell
- name: Rapid Shot
- name: Weapon Focus (halberd)
skills:
  Craft (any): 34
  Diplomacy: 35
  Disguise: 15
  Fly: 23
  Heal: 17
  Knowledge (history): 34
  Knowledge (planes): 34
  Knowledge (religion): 34
  Perception: 38
  Perform (any one): 35
  Sense Motive: 38
  Spellcraft: 31
  Stealth: 32
  Use Magic Device: 32
languages:
- Celestial
- Draconic
- Infernal
- truespeech
special_qualities:
- change shape (alter self)
- empyrean insights
- lucent arms
- lucent body
ecology:
  environment: any good-aligned planes
  organization: solitary
  treasure_type: double
  treasure:
  - mwk halberd
  - mwk composite longbow [+10 Str]
  - other treasure
special_abilities:
  Empyrean Insights (Ex): Empyreans have insight into the way creatures act, and it
    serves them well in battle. Empyreans gain an insight bonus to their Armor Class
    equal to their Charisma bonuses.
  Heed No Call (Ex): Empyreans are ancient beyond measure and directly serve the gods.
    They are immune to all calling spells, unless they choose to allow themselves
    to be called.
  Lucent Arms (Ex): An empyrean infuses its weapons with its own inner light. Any
    weapon an empyrean wields gains the holy and merciful special abilities. The empyrean
    can suppress the merciful special ability on command as normal. An empyrean needs
    no ammunition for its bow (or for any other ranged weapon it may possess), as
    it can simply fire arrows of light. An empyrean's weapons count as having the
    brilliant energy special ability whenever it would be beneficial to the empyrean.
  Lucent Body (Ex): Each empyrean is formed of the ancient essence of good. Its lucent
    body melds perfectly with its armor and clothing, forming a single whole. An empyrean
    gains a sacred bonus to its Armor Class equal to the total armor bonus of its
    infused armor (typically +14 from infused +5 full plate), but it suffers no restrictions
    or penalties for wearing armor. An empyrean can never gain an armor bonus or natural
    armor bonus to its Armor Class through any means.
  Spells: Empyreans can cast divine spells as 20th-level clerics. They do not gain
    access to domains or other cleric abilities.
desc_long: |+
  Empyreans are a race of ancient angels created by the gods before the dawn of mortalkind. Among the angelic hosts, empyreans serve outside of the usual chain of command. Standing 15 feet tall and clad in the trappings of mortality, which wrap their brilliant forms in a shape mortals and other angels can easily understand, empyreans are physical embodiments of the good energy of a deity or deific being, and they answer only to that higher power.

  While other angels arise from an amalgam of good souls or the soul of an ascended mortal, the birth of a new empyrean is a momentous event, for it occurs only if another empyrean is slain. To fill the void, the remaining empyreans temporarily become receptive to the energy of good deities other than their original progenitors, which can eventually cause an empyrean to split in two. The offspring empyrean shares many of the memories and personality traits of the original, but its power is influenced by the deity who sparked its creation.

  Empyreans serve as secret agents for deities-operatives who can be trusted to perform sensitive tasks, especially those that require a long view. Unlike solars, who often become slayers of great evils, empyreans rarely pick fights, but when they do, they prefer to use their deities' favorite weapons.

...

---

# Angel, Empyrean
Light spills out through cracks in this humanoid being’s clothing and armor, and its four wings are composed of wispy blue light.
**Source** Bestiary 5 pg. 24
**XP** 307,200

NG Large outsider (angel, extraplanar, good)
**Init** +12; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/Detect Evil|detect evil]]_, _[[spells/Detect Snares and Pits|detect snares and pits]]_, _[[spells/True Seeing|true seeing]]_; Perception +38
**Aura** protective aura

##### Defense

**AC** 38, touch 38, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+8 Dex, +7 insight, +14 _[[items/Weapon Magic Abilities/Sacred|sacred]]_, -1 size; +4 deflection vs. evil)
**hp** 387 (25d10+250); _[[universal monster rules/Regeneration|regeneration]]_ 15 (evil artifacts)
**Fort** +24, **Ref** +18, **Will** +24; +4 vs. poison, +4 _[[universal monster rules/Resistance|resistance]]_ vs. evil
**Defensive Abilities** heed no call, uncanny _[[feats/Dodge|dodge]]_; **DR** 15/piercing and evil; **Immune** acid, cold, petrification; **Resist** electricity 10, fire 10; **SR** 31

##### Offense
**Speed** 50 ft., fly 120 ft. (good)
**Melee** +1 holy _[[items/Weapon Magic Abilities/Merciful|merciful]]_ _[[items/Weapon/Halberd|halberd]]_ +36/+31/+26/+21 (2d8+16/19-20/×3) or
**Ranged** +1 holy _merciful_ _[[items/Weapon/Composite longbow|composite longbow]]_ +33/+28/+23/+18 (2d6+11/×3)
**Space** 10 ft., **Reach** 10 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +27)
Constant—_detect evil_, _detect snares and pits_, _[[spells/Discern Lies|discern lies]]_ (DC 21), _true seeing_
At will—aid, _[[spells/Atonement|atonement]]_, _[[spells/Break Enchantment|break enchantment]]_, _[[spells/Commune|commune]]_, _[[spells/Continual Flame|continual flame]]_, _[[spells/Dimensional Anchor|dimensional anchor]]_, greater _[[spells/Dispel Magic|dispel magic]]_, lesser _[[spells/Restoration|restoration]]_, _[[spells/Mark of Justice|mark of justice]]_, _[[spells/Neutralize Poison|neutralize poison]]_, _[[spells/Remove Curse|remove curse]]_, _[[spells/Remove Disease|remove disease]]_, _[[spells/Remove Fear|remove fear]]_, _[[spells/Resist Energy|resist energy]]_, _[[spells/Speak with Dead|speak with dead]]_
3/day—_[[spells/Blade Barrier|blade barrier]]_ (DC 23), _[[spells/Dispel Evil|dispel evil]]_ (DC 22), _[[spells/Heal|heal]]_ (DC 23), mass _[[spells/Charm Monster|charm monster]]_ (DC 25), _[[spells/Permanency|permanency]]_, _[[spells/Resurrection|resurrection]]_, _[[spells/Sympathy|sympathy]]_ (DC 25)
1/day—greater _restoration_, _[[spells/Power Word Stun|power word stun]]_, _[[spells/Wish|wish]]_
**_[[classes/Cleric|Cleric]]_ Spells Prepared **(CL 20th; concentration +30)
9th—_[[spells/Gate|gate]]_, mass _heal_ (DC 29), _[[spells/Miracle|miracle]]_, _[[spells/Overwhelming Presence|overwhelming presence]]_(DC 29), quickened _[[spells/Righteous Might|righteous might]]_
8th—_[[spells/Antimagic Field|antimagic field]]_, _[[spells/Discern Location|discern location]]_, quickened _[[spells/Divine Power|divine power]]_, greater _[[spells/Spell Immunity|spell immunity]]_, _[[spells/Holy Aura|holy aura]]_ (DC 28)
7th—_[[spells/Control Weather|control weather]]_, _[[spells/Holy Word|holy word]]_ (DC 27), greater _[[spells/Scrying|scrying]]_ (DC 27), _[[spells/Repulsion|repulsion]]_ (DC 27), _[[spells/Waves of Ecstasy|waves of ecstasy]]_ (DC 27)
6th—_heal_ (DC 26), heroes’ feast, _[[spells/Joyful Rapture|joyful rapture]]_, quickened _[[spells/Silence|silence]]_ (DC 22), _[[spells/Wind Walk|wind walk]]_, _[[spells/Word of Recall|word of recall]]_
5th—_[[spells/Breath Of Life|breath of life]]_, quickened _[[spells/Divine Favor|divine favor]]_, _[[spells/Fickle Winds|fickle winds]]_, greater _[[spells/Command|command]]_ (DC 25), _[[spells/Plane Shift|plane shift]]_ (DC 25), _[[spells/Serenity|serenity]]_ (DC 25)
4th—_[[spells/Death Ward|death ward]]_, _[[spells/Dismissal|dismissal]]_ (DC 24), _divine power_, _[[spells/Freedom of Movement|freedom of movement]]_, greater _[[spells/Magic Weapon|magic weapon]]_ (2)
3rd—_[[spells/Daylight|daylight]]_, _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Locate Object|locate object]]_, _[[spells/Prayer|prayer]]_, _[[spells/Stone Shape|stone shape]]_, _[[spells/Wind Wall|wind wall]]_
2nd—_[[spells/Consecrate|consecrate]]_, _[[spells/Find Traps|find traps]]_, _[[spells/Grace|grace]]_ (2), _[[spells/Make Whole|make whole]]_, _[[spells/Remove Paralysis|remove paralysis]]_, _silence_ (DC 22)
1st—_[[spells/Bless|bless]]_, _divine favor_, _[[spells/Endure Elements|endure elements]]_, _[[spells/Obscuring Mist|obscuring mist]]_ (2), _[[spells/Remove Sickness|remove sickness]]_, _[[spells/Shield Of Faith|shield of faith]]_
0—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Purify Food and Drink|purify food and drink]]_

##### Statistics
**Str** 30, **Dex** 27, **Con** 30, **Int** 23, **Wis** 30, **Cha** 25
**Base Atk** +25; **CMB** +36; **CMD** 75
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Dazing Assault|Dazing Assault]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Furious Focus|Furious Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (_halberd_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Manyshot|Manyshot]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_halberd_)
**Skills** Craft (any) +34, Diplomacy +35, Disguise +15, Fly +23, _Heal_ +17, Knowledge (history, planes, religion) +34, Perception +38, Perform (any one) +35, Sense Motive +38, Spellcraft +31, Stealth +32, Use Magic Device +32
**Languages** Celestial, Draconic, Infernal; truespeech
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_[[spells/Alter Self|alter self]]_), empyrean insights, lucent arms, lucent body

##### Ecology

**Environment** any good-aligned planes
**Organization** solitary
**Treasure** double (mwk _halberd_, mwk _composite longbow_ [+10 Str], other treasure)

### Special Abilities

**Empyrean Insights (Ex)** Empyreans have insight into the way creatures act, and it serves them well in battle. Empyreans gain an insight bonus to their Armor Class equal to their Charisma bonuses.

**Heed No Call (Ex)** Empyreans are ancient beyond measure and directly serve the gods. They are immune to all calling spells, unless they choose to allow themselves to be _[[items/Weapon Magic Abilities/Called|called]]_.

**Lucent Arms (Ex)** An empyrean infuses its weapons with its own _[[feats/Inner Light|inner light]]_. Any weapon an empyrean wields gains the holy and _merciful_ special abilities. The empyrean can suppress the _merciful_ special ability on _command_ as normal. An empyrean needs no ammunition for its bow (or for any other ranged weapon it may possess), as it can simply fire arrows of light. An empyrean’s weapons count as having the _[[items/Weapon Magic Abilities/Brilliant Energy|brilliant energy]]_ special ability whenever it would be beneficial to the empyrean.

**Lucent Body (Ex)** Each empyrean is formed of the ancient essence of good. Its lucent body melds perfectly with its armor and clothing, forming a single whole. An empyrean gains a _sacred_ bonus to its Armor Class equal to the total armor bonus of its infused armor (typically +14 from infused +5 _[[items/Armor/Full plate|full plate]]_), but it suffers no restrictions or penalties for wearing armor. An empyrean can never gain an armor bonus or natural armor bonus to its Armor Class through any means.
**Spells **Empyreans can cast divine spells as 20th-level clerics. They do not gain access to domains or other _cleric_ abilities.

##### Description

Empyreans are a race of ancient angels created by the gods before the dawn of mortalkind. Among the angelic hosts, empyreans serve outside of the usual chain of _command_. Standing 15 feet tall and clad in the trappings of mortality, which wrap their brilliant forms in a shape mortals and other angels can easily understand, empyreans are physical embodiments of the good energy of a deity or deific being, and they answer only to that higher power.

While other angels arise from an amalgam of good souls or the soul of an ascended mortal, the birth of a new empyrean is a momentous event, for it occurs only if another empyrean is slain. To fill the void, the remaining empyreans temporarily become receptive to the energy of good deities other than their original progenitors, which can eventually cause an empyrean to _[[universal monster rules/Split|split]]_ in two. The offspring empyrean shares many of the memories and personality traits of the original, but its power is influenced by the deity who sparked its creation.

Empyreans serve as secret agents for deities—operatives who can be trusted to perform sensitive tasks, especially those that require a long view. Unlike solars, who often become slayers of great evils, empyreans rarely pick fights, but when they do, they prefer to use their deities’ favorite weapons.
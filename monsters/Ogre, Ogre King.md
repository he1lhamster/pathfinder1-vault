---
cssclass: [monsters]
title1: Ogre, Ogre King
title2: Ogre King
CR: 13
sources:
- name: Monster Codex
  page: 159
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 25600
race: Ogre
classes:
- oracle 12 (Pathfinder RPG Advanced Player's Guide 42)
alignment: CE
size: Large
type: humanoid
subtypes:
- giant
initiative:
  bonus: 4
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 28
  touch: 10
  flat_footed: 28
  components:
    armor: 12
    deflection: 1
    natural: 6
    size: -1
HP:
  HP: 180
  long: 16d8+108
saves:
  fort: 14
  ref: 8
  will: 11
DR:
- amount: 10
  weakness: adamantine
  max_absorb: 120
immunities:
- fatigue
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 falchion +22/+17/+12 (2d6+12/15-20)
      entries:
      - - damage: 2d6+12
          crit_range: 15-20
      attack: +1 falchion
      bonus:
      - 22
      - 17
      - 12
space: 10
reach: 10
spells:
  entries:
  - name: mass bull's strength
    source: Oracle
    level: 6
  - name: mass inflict moderate wounds
    source: Oracle
    level: 6
  - name: summon monster VI
    source: Oracle
    level: 6
  - name: breath of life
    source: Oracle
    level: 5
  - name: mass inflict light wounds
    source: Oracle
    level: 5
  - name: righteous might
    source: Oracle
    level: 5
  - name: wall of stone
    source: Oracle
    level: 5
    DC: 18
  - name: air walk
    source: Oracle
    level: 4
  - name: cure critical wounds
    source: Oracle
    level: 4
  - name: greater magic weapon
    source: Oracle
    level: 4
  - name: inflict critical wounds
    source: Oracle
    level: 4
  - name: wall of fire
    source: Oracle
    level: 4
  - name: cure serious wounds
    source: Oracle
    level: 3
  - name: dispel magic
    source: Oracle
    level: 3
  - name: inflict serious wounds
    source: Oracle
    level: 3
  - name: magic vestment
    source: Oracle
    level: 3
  - name: prayer
    source: Oracle
    level: 3
  - name: aid
    source: Oracle
    level: 2
  - name: bull's strength
    source: Oracle
    level: 2
  - name: cure moderate wounds
    source: Oracle
    level: 2
  - name: fog cloud
    source: Oracle
    level: 2
  - superscripts:
    - APG
    name: grace
    source: Oracle
    level: 2
  - name: inflict moderate wounds
    source: Oracle
    level: 2
  - name: resist energy
    source: Oracle
    level: 2
  - name: cure light wounds
    source: Oracle
    level: 1
  - name: divine favor
    source: Oracle
    level: 1
  - name: enlarge person
    source: Oracle
    level: 1
    DC: 14
  - name: entropic shield
    source: Oracle
    level: 1
  - name: inflict light wounds
    source: Oracle
    level: 1
  - name: obscuring mist
    source: Oracle
    level: 1
  - name: protection from good
    source: Oracle
    level: 1
  - name: bleed
    source: Oracle
    level: 0
    DC: 13
  - name: create water
    source: Oracle
    level: 0
  - name: detect magic
    source: Oracle
    level: 0
  - name: guidance
    source: Oracle
    level: 0
  - name: mending
    source: Oracle
    level: 0
  - name: purify food and drink
    source: Oracle
    level: 0
  - superscripts:
    - APG
    name: spark
    source: Oracle
    level: 0
  - name: stabilize
    source: Oracle
    level: 0
  - name: virtue
    source: Oracle
    level: 0
  sources:
  - name: Oracle
    type: known
    CL: 12
    concentration: 15
    slots:
      6: 3
      5: 5
      4: 6
      3: 7
      2: 7
      1: 7
      0: at-will
    mystery: battle
tactics:
  Before Combat: The ogre king casts greater magic weapon and magic vestment on his
    weapon and armor respectively, and activates his iron skin revelation.
  During Combat: The ogre king relies on buffing spells, his quickened spells, and
    his combat healing to bolster his combat abilities and keep himself in prime shape.
    If faced with archers or spellcasters, he casts wall of stone or quickened obscuring
    mist to prevent anyone from obtaining line of sight while he engages melee combatants.
  Base Statistics: Without the benefits of greater magic weapon, iron skin, and magic
    vestment, the ogre kings statistics are AC 25, no damage reduction; Melee +1 falchion
    +20/+15/+10 (2d6+10/15-20).
ability_scores:
  STR: 23
  DEX: 10
  CON: 21
  INT: 6
  WIS: 8
  CHA: 16
BAB: 12
CMB: 19
CMD: 30
feats:
- name: Critical Focus
- name: Extra Revelation (Combat Healer)
- name: Extra Revelation (Iron Skin)
- name: Greater Weapon Focus (falchion)
- name: Improved Critical (falchion)
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Quicken Spell
- name: Toughness
- name: Weapon Focus (falchion)
skills:
  Intimidate: 16
  Perception: 17
  Spellcraft: 4
languages:
- Giant
special_qualities:
- oracle's curse (lame)
- revelations (battlefield clarity 2/day, combat healer 2/day, iron skin 1/day, skill
  at arms, surprising charge 2/day, weapon mastery)
gear:
  combat:
  - boots of speed
  other:
  - mwk full plate
  - +1 falchion
  - amulet of natural armor +1
  - belt of mighty constitution +2
  - cloak of resistance +1
  - headband of alluring charisma +2
  - ring of protection +1
  - jewelry and gems (worth 5,000 gp in total)
  - 775 gp
ecology:
  environment: temperate or cold hills
desc_long: Few ogres live long enough to amass great power-which makes an army commanded
  by a powerful ogre king or queen a terrifying force to behold.

---

# Ogre, Ogre King

**Source** Monster Codex pg. 159
**XP** 25,600
_[[monsters/Ogre|Ogre]]_ _[[classes/Oracle|oracle]]_ 12 (Pathfinder RPG Advanced Player’s Guide 42)
CE Large humanoid (giant)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +17

##### Defense

**AC** 28, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+12 armor, +1 deflection, +6 natural, –1 size)
**hp** 180 (16d8+108)
**Fort** +14, **Ref** +8, **Will** +11
**DR** 10/adamantine (120 hit points); **Immune** fatigue

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon/Falchion|falchion]]_ +22/+17/+12 (2d6+12/15–20)
**Space** 10 ft., **Reach** 10 ft.
**_Oracle_ Spells Known **(CL 12th; concentration +15)
6th (3/day)—mass bull’s strength, mass _[[spells/Inflict Moderate Wounds|inflict moderate wounds]]_, _[[spells/Summon Monster VI|summon monster VI]]_
5th (5/day)—_[[spells/Breath Of Life|breath of life]]_, mass _[[spells/Inflict Light Wounds|inflict light wounds]]_, _[[spells/Righteous Might|righteous might]]_, _[[spells/Wall Of Stone|wall of stone]]_ (DC 18)
4th (6/day)—_[[spells/Air Walk|air walk]]_, _[[spells/Cure Critical Wounds|cure critical wounds]]_, greater _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Inflict Critical Wounds|inflict critical wounds]]_, _[[spells/Wall Of Fire|wall of fire]]_
3rd (7/day)—_[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Inflict Serious Wounds|inflict serious wounds]]_, _[[spells/Magic Vestment|magic vestment]]_, _[[spells/Prayer|prayer]]_
2nd (7/day)—aid, bull’s strength, _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Grace|grace]]_, _inflict moderate wounds_, _[[spells/Resist Energy|resist energy]]_
1st (7/day)—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Enlarge Person|enlarge person]]_ (DC 14), _[[spells/Entropic Shield|entropic shield]]_, _inflict light wounds_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Protection From Good|protection from good]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Mending|mending]]_, _[[spells/Purify Food and Drink|purify food and drink]]_, _[[spells/Spark|spark]]_, stabilize, _[[spells/Virtue|virtue]]_
**Mystery **battle

### Tactics

**Before Combat** The _ogre_ _[[npcs/King|king]]_ casts greater _magic weapon_ and _magic vestment_ on his weapon and armor respectively, and activates his iron skin _[[spells/Revelation|revelation]]_.

**During Combat** The _ogre_ _king_ relies on buffing spells, his quickened spells, and his combat healing to bolster his combat abilities and keep himself in prime shape. If faced with archers or spellcasters, he casts _wall of stone_ or quickened _obscuring mist_ to prevent anyone from obtaining line of sight while he engages melee combatants.

**Base Statistics** Without the benefits of greater _magic weapon_, iron skin, and _magic vestment_, the _ogre_ kings statistics are **AC **25, no _[[universal monster rules/Damage Reduction|damage reduction]]_; **Melee **+1 _falchion_ +20/+15/+10 (2d6+10/15–20).

##### Statistics
**Str** 23, **Dex** 10, **Con** 21, **Int** 6, **Wis** 8, **Cha** 16
**Base Atk** +12; **CMB** +19; **CMD** 30
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Extra Revelation|Extra Revelation]]_ (Combat _[[npcs/Healer|Healer]]_), _Extra Revelation_ (Iron Skin), _[[feats/Greater Weapon Focus|Greater Weapon Focus]]_ (_falchion_), _[[feats/Improved Critical|Improved Critical]]_ (_falchion_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_falchion_)
**Skills** Intimidate +16, Perception +17, Spellcraft +4
**Languages** Giant
**SQ** _oracle_’s curse (lame), revelations (battlefield _[[items/Weapon/Clarity|clarity]]_ 2/day, combat _healer_ 2/day, iron skin 1/day, skill at arms, surprising charge 2/day, weapon mastery)
**Combat Gear** _[[items/Wondrous Item/Boots of Speed|boots of speed]]_; **Other Gear** mwk _[[items/Armor/Full plate|full plate]]_, +1 _falchion_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Mighty Constitution +2|belt of mighty constitution +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Mundane/Jewelry|jewelry]]_ and gems (worth 5,000 gp in total), 775 gp

##### Ecology

**Environment** temperate or cold hills

##### Description

Few ogres live long enough to amass great power—which makes an army commanded by a powerful _ogre_ _king_ or queen a terrifying force to behold.
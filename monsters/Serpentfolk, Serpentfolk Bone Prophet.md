---
cssclass: [monsters]
title1: Serpentfolk, Serpentfolk Bone Prophet
title2: Serpentfolk Bone Prophet
CR: 11
sources:
- name: Monster Codex
  page: 205
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 12800
race: Advanced
classes:
- serpentfolk oracle 7 (Pathfinder RPG Advanced Player's Guide 42)
alignment: NE
size: Medium
type: monstrous humanoid
initiative:
  bonus: 8
senses:
  darkvision: 60
  scent: true
AC:
  AC: 23
  touch: 13
  flat_footed: 20
  components:
    armor: 7
    dex: 2
    dodge: 1
    natural: 3
HP:
  HP: 137
  long: 5d10+7d8+79
  HD: 12
saves:
  fort: 11
  ref: 11
  will: 16
immunities:
- mind-affecting effects
- paralysis
- poison
SR: 22
speeds:
  base: 15
attacks:
  melee:
  - - text: +1 quarterstaff +12/+7 (1d6+2)
      entries:
      - - damage: 1d6+2
      attack: +1 quarterstaff
      bonus:
      - 12
      - 7
    - text: bite +6 (1d6 plus poison)
      entries:
      - - damage: 1d6
        - effect: poison
      attack: bite
      bonus:
      - 6
spell_like_abilities:
  entries:
  - name: disguise self
    source: default
    freq: At will
    DC: 16
    other: humanoid form only
  - name: ventriloquism
    source: default
    freq: At will
    DC: 16
  - name: blur
    source: default
    freq: 1/day
  - name: dominate person
    source: default
    freq: 1/day
    DC: 20
  - name: major image
    source: default
    freq: 1/day
    DC: 18
  - name: mirror image
    source: default
    freq: 1/day
  - name: suggestion
    source: default
    freq: 1/day
    DC: 18
  sources:
  - name: default
    CL: 4
    concentration: 9
spells:
  entries:
  - name: animate dead
    source: Oracle
    level: 3
  - name: bestow curse
    source: Oracle
    level: 3
    DC: 18
  - superscripts:
    - UC
    name: chain of perdition
    source: Oracle
    level: 3
  - name: inflict serious wounds
    source: Oracle
    level: 3
  - superscripts:
    - UM
    name: dread bolt
    source: Oracle
    level: 2
    DC: 17
  - name: false life
    source: Oracle
    level: 2
  - name: hold person
    source: Oracle
    level: 2
    DC: 17
  - name: inflict moderate wounds
    source: Oracle
    level: 2
  - superscripts:
    - UC
    name: instrument of agony
    source: Oracle
    level: 2
  - name: cause fear
    source: Oracle
    level: 1
    DC: 16
  - name: cure light wounds
    source: Oracle
    level: 1
  - name: inflict light wounds
    source: Oracle
    level: 1
  - superscripts:
    - UM
    name: murderous command
    source: Oracle
    level: 1
    DC: 16
  - name: obscuring mist
    source: Oracle
    level: 1
  - superscripts:
    - UM
    name: ray of sickening
    source: Oracle
    level: 1
    DC: 16
  - name: shield of faith
    source: Oracle
    level: 1
  - name: bleed
    source: Oracle
    level: 0
    DC: 15
  - name: detect magic
    source: Oracle
    level: 0
  - name: detect poison
    source: Oracle
    level: 0
  - name: guidance
    source: Oracle
    level: 0
  - name: light
    source: Oracle
    level: 0
  - name: resistance
    source: Oracle
    level: 0
  - name: stabilize
    source: Oracle
    level: 0
  sources:
  - name: Oracle
    type: known
    CL: 7
    concentration: 12
    slots:
      3: 5
      2: 7
      1: 8
      0: at-will
    mystery: bones
tactics:
  During Combat: The bone prophet enforces mental control over enemies with hold person,
    murderous command, and suggestion. It casts bestow curse and chain of perdition
    to hamper those that come too close, and uses its damaging spells and scrolls
    against its most dangerous opponents.
ability_scores:
  STR: 12
  DEX: 19
  CON: 20
  INT: 18
  WIS: 19
  CHA: 20
BAB: 10
CMB: 11
CMD: 26
feats:
- name: Combat Casting
- name: Command Undead
- name: Dodge
- name: Great Fortitude
- name: Improved Initiative
- name: Iron Will
- name: Toughness
skills:
  Acrobatics: 5
    when jumping: 1
  Bluff: 15
  Diplomacy: 15
  Disguise: 15
  Escape Artist: 10
  Heal: 11
  Intimidate: 13
  Knowledge (arcana): 17
  Knowledge (history): 17
  Knowledge (religion): 17
  Perception: 19
  Sense Motive: 14
  Spellcraft: 18
  Use Magic Device: 15
  _racial_mods:
    Escape Artist:
      _: 8
    Use Magic Device:
      _: 4
languages:
- Aklo
- Common
- Draconic
- Undercommon
- telepathy 100 ft.
special_qualities:
- oracle's curse (lame)
- revelations (bleeding wounds, death's touch, undead servitude [8/day, DC 18])
gear:
  combat:
  - bead of force
  - potions of cure moderate wounds (2)
  - potion of invisibility
  - scroll of greater command
  - scroll of slay living
  - wand of cure moderate wounds (10 charges)
  other:
  - +1 chainmail
  - +1 quarterstaff
  - cloak of resistance +1
  - headband of inspired wisdom +2
  - unholy symbol
  - 175 gp
ecology:
  environment: any land (usually jungles or underground)
special_abilities:
  Poison (Ex): Bite-injury; save Fort DC 17; frequency 1/round for 6 rounds; effect
    1d2 Str; cure 2 saves. The save DC is Constitution-based.
desc_long: The serpentfolk bone prophet uses its powers to control slaves and convert
  the dead into mindless minions. It constantly hears the otherworldly whispers of
  the skeletal head of its god and relays those cryptic words to its mage colleagues.

---

# Serpentfolk, Serpentfolk Bone Prophet

**Source** Monster Codex pg. 205
**XP** 12,800
Advanced _[[monsters/Serpentfolk|serpentfolk]]_ _[[classes/Oracle|oracle]]_ 7 (Pathfinder RPG Advanced Player’s Guide 42)

NE Medium monstrous humanoid
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +19

##### Defense

**AC** 23, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+7 armor, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +3 natural)
**hp** 137 (12 HD; 5d10+7d8+79)
**Fort** +11, **Ref** +11, **Will** +16
**Immune** mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, poison; **SR** 22

##### Offense
**Speed** 15 ft.
**Melee** +1 _[[items/Weapon/Quarterstaff|quarterstaff]]_ +12/+7 (1d6+2), bite +6 (1d6 plus poison)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +9)
At will—_[[spells/Disguise Self|disguise self]]_ (DC 16, humanoid form only), _[[spells/Ventriloquism|ventriloquism]]_ (DC 16)
1/day—_[[spells/Blur|blur]]_, _[[spells/Dominate Person|dominate person]]_ (DC 20), _[[spells/Major Image|major image]]_ (DC 18), _[[spells/Mirror Image|mirror image]]_, _[[spells/Suggestion|suggestion]]_ (DC 18)
**_Oracle_ Spells Known **(CL 7th; concentration +12)
3rd (5/day)—_[[spells/Animate Dead|animate dead]]_, _[[spells/Bestow Curse|bestow curse]]_ (DC 18), _[[spells/Chain of Perdition|chain of perdition]]_, _[[spells/Inflict Serious Wounds|inflict serious wounds]]_
2nd (7/day)—_[[spells/Dread Bolt|dread bolt]]_ (DC 17), _[[spells/False Life|false life]]_, _[[spells/Hold Person|hold person]]_ (DC 17), _[[spells/Inflict Moderate Wounds|inflict moderate wounds]]_, _[[spells/Instrument of Agony|instrument of agony]]_
1st (8/day)—_[[spells/Cause Fear|cause fear]]_ (DC 16), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Inflict Light Wounds|inflict light wounds]]_, _[[spells/Murderous Command|murderous command]]_ (DC 16), _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Ray of Sickening|ray of sickening]]_ (DC 16), _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, light, _[[universal monster rules/Resistance|resistance]]_, stabilize
**Mystery** bones

### Tactics

**During Combat** The bone _[[feats/Prophet|prophet]]_ enforces mental control over enemies with _hold person_, _murderous command_, and _suggestion_. It casts _bestow curse_ and _chain of perdition_ to hamper those that come too close, and uses its damaging spells and scrolls against its most dangerous opponents.

##### Statistics
**Str** 12, **Dex** 19, **Con** 20, **Int** 18, **Wis** 19, **Cha** 20
**Base Atk** +10; **CMB** +11; **CMD** 26
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[spells/Command Undead|Command Undead]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Toughness|Toughness]]_
**Skills** Acrobatics +5 (+1 when jumping), Bluff +15, Diplomacy +15, Disguise +15, Escape Artist +10, _[[spells/Heal|Heal]]_ +11, Intimidate +13, Knowledge (arcana, history, religion) +17, Perception +19, Sense Motive +14, Spellcraft +18, Use Magic Device +15; **Racial Modifiers** +8 Escape Artist, +4 Use Magic Device
**Languages** Aklo, Common, Draconic, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _oracle_’s curse (lame), revelations (bleeding wounds, death’s touch, undead servitude [8/day, DC 18])
**Combat Gear** _[[items/Wondrous Item/Bead of Force|bead of force]]_, potions of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (2), potion of _[[spells/Invisibility|invisibility]]_, scroll of greater _[[spells/Command|command]]_, scroll of _[[spells/Slay Living|slay living]]_, wand of _cure moderate wounds_ (10 charges); **Other Gear** +1 _[[items/Armor/Chainmail|chainmail]]_, +1 _quarterstaff_, _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol, 175 gp

##### Ecology

**Environment** any land (usually jungles or underground)

### Special Abilities

**Poison (Ex)** Bite—injury; save Fort DC 17; frequency 1/round for 6 rounds; effect 1d2 Str; cure 2 saves. The save DC is Constitution-based.

##### Description

The _serpentfolk_ bone _prophet_ uses its powers to control slaves and convert the dead into mindless minions. It constantly hears the otherworldly whispers of the skeletal head of its god and relays those cryptic words to its mage colleagues.
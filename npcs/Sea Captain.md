---
cssclass: [monsters]
title1: Sea Captain
title2: Sea Captain
CR: 7
sources:
- name: NPC Codex
  page: 67
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 3200
race: Halfling
classes:
- druid 8
alignment: NE
size: Small
type: humanoid
subtypes:
- halfling
initiative:
  bonus: 7
AC:
  AC: 26
  touch: 14
  flat_footed: 23
  components:
    armor: 7
    dex: 3
    natural: 3
    shield: 2
    size: 1
HP:
  HP: 61
  long: 8d8+22
saves:
  fort: 9
  ref: 7
  will: 12
  other: +2 vs. fear, +4 vs. fey and plant-targeted effects
speeds:
  base: 15
attacks:
  melee:
  - - text: mwk scimitar +11/+6 (1d4+3/18-20)
      entries:
      - - damage: 1d4+3
          crit_range: 18-20
      attack: mwk scimitar
      bonus:
      - 11
      - 6
  ranged:
  - - text: mwk sling +11/+6 (1d3+3)
      entries:
      - - damage: 1d3+3
      attack: mwk sling
      bonus:
      - 11
      - 6
  special:
  - wild shape 3/day
spell_like_abilities:
  entries:
  - name: lightning lord
    source: default
    freq: 8/day
  - name: storm burst
    source: default
    freq: 7/day
  sources:
  - name: default
    CL: 8
    concentration: 12
spells:
  entries:
  - name: control water
    source: Druid
    level: 4
  - name: flame strike
    source: Druid
    level: 4
    DC: 18
  - name: freedom of movement
    source: Druid
    level: 4
  - is_domain_spell: true
    name: sleet storm
    source: Druid
    level: 4
  - is_domain_spell: true
    name: call lightning
    source: Druid
    level: 3
    DC: 17
  - name: greater magic fang
    source: Druid
    level: 3
  - name: protection from energy
    source: Druid
    level: 3
  - name: quench
    source: Druid
    level: 3
  - name: wind wall
    source: Druid
    level: 3
  - name: barkskin
    source: Druid
    level: 2
  - name: bull's strength
    source: Druid
    level: 2
  - is_domain_spell: true
    name: fog cloud
    source: Druid
    level: 2
  - name: gust of wind
    source: Druid
    level: 2
    DC: 16
  - name: warp wood
    source: Druid
    level: 2
  - name: cure light wounds
    source: Druid
    level: 1
    count: 4
  - name: endure elements
    source: Druid
    level: 1
  - name: obscuring mist
    source: Druid
    level: 1
  - name: create water
    source: Druid
    level: 0
  - name: detect magic
    source: Druid
    level: 0
  - name: flare
    source: Druid
    level: 0
    DC: 14
  - name: light
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 8
    concentration: 12
    slots:
      0: at-will
    domains:
    - weather
tactics:
  Before Combat: The druid casts barkskin and bull's strength.
  During Combat: The druid is well aware of his physical shortcomings, and wild shapes
    into a Medium air elemental the first chance he gets to escape melee combat. Once
    at a safe altitude, he casts wind wall and freedom of movement. If still threatened,
    he casts offensive spells such as flame strike or sleet storm, or uses his Weather
    domain spell-like abilities. If targeted by spellcasters, he casts fog cloud to
    obscure vision. If forced into melee, he casts greater magic fang before wild
    shaping into a Huge animal (preferably a triceratops or an orca).
  Base Statistics: Without barkskin and bull's strength, the druid's statistics are
    AC 23, touch 14, flat-footed 20; Melee mwk scimitar +11/+6 (1d4+1/18-20); Ranged
    mwk sling +11/+6 (1d3+1); Str 12; CMB +6; CMD 19; Skills Climb +6, Swim +3.
ability_scores:
  STR: 16
  DEX: 16
  CON: 12
  INT: 10
  WIS: 18
  CHA: 10
BAB: 6
CMB: 8
CMD: 21
feats:
- name: Improved Initiative
- name: Natural Spell
- name: Toughness
- name: Weapon Finesse
skills:
  Acrobatics: 1
    when jumping: -3
  Climb: 8
  Fly: 6
  Handle Animal: 5
  Heal: 11
  Knowledge (nature): 10
  Perception: 15
  Spellcraft: 7
  Survival: 13
  Swim: 5
languages:
- Common
- Druidic
- Goblin
- Halfling
special_qualities:
- nature bond (Weather domain)
- nature sense
- trackless step
- wild empathy +8
- woodland stride
gear:
  combat:
  - scroll of owl's wisdom
  - alchemist's fire (3)
  - thunderstone
  other:
  - +1 dragonhide breastplate
  - masterwork heavy wooden shield
  - masterwork scimitar
  - masterwork sling with 20 bullets
  - cloak of resistance +1
  - headband of inspired wisdom +2
  - grappling hook
  - healer's kit
  - holly and mistletoe
  - silk rope (50 ft.)
  - spell component pouch
  - 22 gp
desc_long: With their ability to control and harness the powers of winds and storms,
  a number of druids become sea captains, using their abilities sometimes for trade
  and other times for piracy.

---

# Sea Captain

**Source** NPC Codex pg. 67
**XP** 3,200
Halfling _[[classes/Druid|druid]]_ 8

NE Small humanoid (halfling)
**Init** +7; **Senses** Perception +15

##### Defense

**AC** 26, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+7 armor, +3 Dex, +3 natural, +2 _[[spells/Shield|shield]]_, +1 size)
**hp** 61 (8d8+22)
**Fort** +9, **Ref** +7, **Will** +12; +2 vs. _[[universal monster rules/Fear|fear]]_, +4 vs. fey and plant-targeted effects

##### Offense
**Speed** 15 ft.
**Melee** mwk _[[items/Weapon/Scimitar|scimitar]]_ +11/+6 (1d4+3/18–20)
**Ranged** mwk _[[items/Weapon/Sling|sling]]_ +11/+6 (1d3+3)
**Special Attacks** wild shape 3/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +12)
8/day—lightning lord
7/day—storm burst
**_Druid_ Spells Prepared **(CL 8th; concentration +12)
4th—_[[spells/Control Water|control water]]_, _[[spells/Flame Strike|flame strike]]_ (DC 18), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Sleet Storm|sleet storm]]_
3rd—call lightningD (DC 17), greater _[[spells/Magic Fang|magic fang]]_, _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Quench|quench]]_, _[[spells/Wind Wall|wind wall]]_
2nd—_[[spells/Barkskin|barkskin]]_, bull’s strength, _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Gust Of Wind|gust of wind]]_ (DC 16), _[[spells/Warp Wood|warp wood]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_ (4), _[[spells/Endure Elements|endure elements]]_, _[[spells/Obscuring Mist|obscuring mist]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 14), light
**D **Domain spell; **Domain **Weather

### Tactics

**Before Combat **The _druid_ casts _barkskin_ and bull’s strength.
**During Combat **The _druid_ is well aware of his physical shortcomings, and wild shapes into a Medium air elemental the first chance he gets to escape melee combat. Once at a safe altitude, he casts _wind wall_ and _freedom of movement_. If still threatened, he casts offensive spells such as _flame strike_ or _sleet storm_, or uses his Weather domain _spell-like abilities_. If targeted by spellcasters, he casts _fog cloud_ to obscure _[[spells/Vision|vision]]_. If forced into melee, he casts greater _magic fang_ before wild shaping into a Huge animal (preferably a triceratops or an orca).
**Base Statistics **Without _barkskin_ and bull’s strength, the _druid_’s statistics are **AC **23, touch 14, _flat-footed_ 20; **Melee **mwk _scimitar_ +11/+6 (1d4+1/18–20); **Ranged **mwk _sling_ +11/+6 (1d3+1); **Str **12; **CMB **+6; **CMD **19; **Skills **_[[universal monster rules/Climb|Climb]]_ +6, Swim +3.

##### Statistics
**Str** 16, **Dex** 16, **Con** 12, **Int** 10, **Wis** 18, **Cha** 10
**Base Atk** +6; **CMB** +8; **CMD** 21
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +1 (–3 when jumping), _Climb_ +8, Fly +6, Handle Animal +5, _[[spells/Heal|Heal]]_ +11, Knowledge (nature) +10, Perception +15, Spellcraft +7, Survival +13, Swim +5
**Languages** Common, Druidic, _[[monsters/Goblin|Goblin]]_, Halfling
**SQ** nature bond (Weather domain), nature sense, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, wild _[[feats/Empathy|empathy]]_ +8, woodland stride
**Combat Gear** scroll of owl’s wisdom, _[[classes/Alchemist|alchemist]]_’s fire (3), _[[items/Mundane/Thunderstone|thunderstone]]_; **Other Gear** +1 dragonhide _[[items/Armor/Breastplate|breastplate]]_, masterwork _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, masterwork _scimitar_, masterwork _sling_ with 20 bullets, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Weapon/Grappling hook|grappling hook]]_, _[[npcs/Healer|healer]]_’s kit, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, _[[items/Mundane/Silk rope|silk rope]]_ (50 ft.), _[[items/Mundane/Spell component pouch|spell component pouch]]_, 22 gp

With their ability to control and harness the powers of winds and storms, a number of druids become sea captains, using their abilities sometimes for trade and other times for piracy.
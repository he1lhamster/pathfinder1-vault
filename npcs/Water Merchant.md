---
cssclass: [monsters]
title1: Water Merchant
title2: Water Merchant
CR: 9
sources:
- name: NPC Codex
  page: 69
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 6400
race: Gnome
classes:
- druid 10
alignment: NE
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 7
senses:
  low-light vision: true
AC:
  AC: 28
  touch: 15
  flat_footed: 25
  components:
    armor: 7
    deflection: 1
    dex: 3
    natural: 3
    shield: 3
    size: 1
HP:
  HP: 88
  long: 10d8+40
saves:
  fort: 10
  ref: 9
  will: 12
  other: +2 vs. illusions, +4 vs. fey and plant-targeted effects
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
immunities:
- poison
resistances:
  cold: 10
speeds:
  base: 15
attacks:
  melee:
  - - text: 1 scimitar +7/+2 (1d4-1/18-20)
      entries:
      - - damage: 1d4-1
          crit_range: 18-20
      count: 1
      attack: scimitar
      bonus:
      - 7
      - 2
  ranged:
  - - text: dart +11/+6 (1d3-2)
      entries:
      - - damage: 1d3-2
      attack: dart
      bonus:
      - 11
      - 6
  special:
  - +1 on attack rolls against goblinoid and reptilian humanoids
  - wild shape 4/day
spell_like_abilities:
  entries:
  - name: icicle
    source: default
    freq: 7/day
  - name: dancing lights
    source: gnome
    freq: 1/day
  - name: ghost sound
    source: gnome
    freq: 1/day
  - name: prestidigitation
    source: gnome
    freq: 1/day
  - name: speak with animals
    source: gnome
    freq: 1/day
  sources:
  - name: default
    CL: 10
    concentration: 14
  - name: gnome
    CL: 10
    concentration: 11
spells:
  entries:
  - name: call lightning storm
    source: Druid
    level: 5
    DC: 19
  - is_domain_spell: true
    name: ice storm
    source: Druid
    level: 5
  - name: wall of thorns
    source: Druid
    level: 5
  - is_domain_spell: true
    name: control water
    source: Druid
    level: 4
  - name: dispel magic
    source: Druid
    level: 4
  - name: flame strike
    source: Druid
    level: 4
    count: 2
    DC: 18
  - name: freedom of movement
    source: Druid
    level: 4
  - name: call lightning
    source: Druid
    level: 3
    DC: 17
  - name: cure moderate wounds
    source: Druid
    level: 3
  - name: greater magic fang
    source: Druid
    level: 3
    count: 2
  - is_domain_spell: true
    name: water breathing
    source: Druid
    level: 3
  - name: barkskin
    source: Druid
    level: 2
    count: 2
  - name: cat's grace
    source: Druid
    level: 2
  - is_domain_spell: true
    name: fog cloud
    source: Druid
    level: 2
  - name: lesser restoration
    source: Druid
    level: 2
  - name: resist energy
    source: Druid
    level: 2
  - name: cure light wounds
    source: Druid
    level: 1
    count: 2
  - name: endure elements
    source: Druid
    level: 1
  - name: faerie fire
    source: Druid
    level: 1
  - is_domain_spell: true
    name: obscuring mist
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
  - name: create water
    source: Druid
    level: 0
  - name: detect poison
    source: Druid
    level: 0
  - name: light
    source: Druid
    level: 0
  - name: purify food and drink
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 10
    concentration: 14
    slots:
      0: at-will
    domains:
    - water
tactics:
  Before Combat: The druid casts barkskin and cat's grace. She casts endure elements
    every morning.
  During Combat: The druid keeps her distance from opponents. She casts freedom of
    movement, then wild shapes into an air elemental to fly away. Once she feels she
    has the tactical advantage, she relies on summon spells and ranged abilities to
    avoid melee.
  Base Statistics: Without barkskin and cat's grace, the druid's statistics are Init
    +5; AC 23, touch 13, flat-footed 22; Ref +7; Ranged dart +9/+4 (1d3-2); Dex 12;
    CMD 16; Skills Fly +5.
ability_scores:
  STR: 6
  DEX: 16
  CON: 15
  INT: 15
  WIS: 18
  CHA: 12
BAB: 7
CMB: 4
CMD: 18
feats:
- name: Improved Initiative
- name: Lightning Reflexes
- name: Natural Spell
- name: Skill Focus (Bluff)
- name: Toughness
skills:
  Bluff: 10
  Diplomacy: 5
  Fly: 7
  Handle Animal: 10
  Knowledge (geography): 9
  Knowledge (nature): 11
  Linguistics: 4
  Perception: 13
  Profession (merchant): 15
  Sense Motive: 10
  Spellcraft: 12
  Survival: 17
languages:
- Abyssal
- Common
- Draconic
- Druidic
- Elf
- Gnome
- Sylvan
special_qualities:
- nature bond (Water domain)
- nature sense
- trackless step
- wild empathy +11
- woodland stride
gear:
  combat:
  - feather token (whip)
  - scroll of longstrider
  other:
  - +1 dragonhide breastplate
  - +1 heavy wooden shield
  - +1 scimitar
  - darts (5)
  - cloak of resistance +1
  - headband of inspired wisdom +2
  - ring of protection +1
  - holly and mistletoe
  - ink vial
  - inkpens (2)
  - paper (5 sheets)
  - scroll case
  - spell component pouch
  - waterskin
  - 33 gp
desc_long: Typically found in arid regions, these druids use magic to supply others
  with water for a price.

---

# Water Merchant

**Source** NPC Codex pg. 69
**XP** 6,400
Gnome _[[classes/Druid|druid]]_ 10

NE Small humanoid (gnome)
**Init** +7; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +13

##### Defense

**AC** 28, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+7 armor, +1 deflection, +3 Dex, +3 natural, +3 _[[spells/Shield|shield]]_, +1 size)
**hp** 88 (10d8+40)
**Fort** +10, **Ref** +9, **Will** +12; +2 vs. illusions, +4 vs. fey and plant-targeted effects
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _[[feats/Dodge|dodge]]_ bonus to AC vs. giants); **Immune** poison; **Resist** cold 10

##### Offense
**Speed** 15 ft.
**Melee** 1 _[[items/Weapon/Scimitar|scimitar]]_ +7/+2 (1d4–1/18–20)
**Ranged** _[[items/Weapon/Dart|dart]]_ +11/+6 (1d3–2)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids, wild shape 4/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +14)
7/day—icicle
**Gnome _Spell-Like Abilities_** (CL 10th; concentration +11)
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Speak with Animals|speak with animals]]_
**_Druid_ Spells Prepared **(CL 10th; concentration +14)
5th—_[[spells/Call Lightning Storm|call lightning storm]]_ (DC 19), _[[spells/Ice Storm|ice storm]]_, _[[spells/Wall Of Thorns|wall of thorns]]_
4th—_[[spells/Control Water|control water]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Flame Strike|flame strike]]_ (2, DC 18), _[[spells/Freedom of Movement|freedom of movement]]_
3rd—_[[spells/Call Lightning|call lightning]]_ (DC 17), _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, greater _[[spells/Magic Fang|magic fang]]_ (2), _[[universal monster rules/Water Breathing|water breathing]]_
2nd—_[[spells/Barkskin|barkskin]]_ (2), cat’s _[[spells/Grace|grace]]_, _[[spells/Fog Cloud|fog cloud]]_, lesser _[[spells/Restoration|restoration]]_, _[[spells/Resist Energy|resist energy]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_ (2), _[[spells/Endure Elements|endure elements]]_, _[[spells/Faerie Fire|faerie fire]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _speak with animals_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Poison|detect poison]]_, light, _[[spells/Purify Food and Drink|purify food and drink]]_
**D **Domain spell; **Domain **Water

### Tactics

**Before Combat **The _druid_ casts _barkskin_ and cat’s _grace_. She casts _endure elements_ every morning.
**During Combat **The _druid_ keeps her distance from opponents. She casts _freedom of movement_, then wild shapes into an air elemental to fly away. Once she feels she has the tactical advantage, she relies on _[[universal monster rules/Summon|summon]]_ spells and ranged abilities to avoid melee.
**Base Statistics **Without _barkskin_ and cat’s _grace_, the _druid_’s statistics are **Init **+5; **AC **23, touch 13, _flat-footed_ 22; **Ref **+7; **Ranged **_dart_ +9/+4 (1d3–2); **Dex **12; **CMD **16; **Skills **Fly +5.

##### Statistics
**Str** 6, **Dex** 16, **Con** 15, **Int** 15, **Wis** 18, **Cha** 12
**Base Atk** +7; **CMB** +4; **CMD** 18
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Skill Focus|Skill Focus]]_ (Bluff), _[[feats/Toughness|Toughness]]_
**Skills** Bluff +10, Diplomacy +5, Fly +7, Handle Animal +10, Knowledge (geography) +9, Knowledge (nature) +11, Linguistics +4, Perception +13, Profession (merchant) +15, Sense Motive +10, Spellcraft +12, Survival +17
**Languages** Abyssal, Common, Draconic, Druidic, Elf, Gnome, Sylvan
**SQ** nature bond (Water domain), nature sense, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, wild _[[feats/Empathy|empathy]]_ +11, woodland stride
**Combat Gear** feather token (_[[items/Weapon/Whip|whip]]_), scroll of _[[spells/Longstrider|longstrider]]_; **Other Gear** +1 dragonhide _[[items/Armor/Breastplate|breastplate]]_, +1 _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, +1 _scimitar_, darts (5), _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, _[[items/Mundane/Ink|ink]]_ _[[items/Mundane/Vial|vial]]_, inkpens (2), paper (5 sheets), _[[items/Mundane/Scroll case|scroll case]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, _[[items/Mundane/Waterskin|waterskin]]_, 33 gp

Typically found in arid regions, these druids use magic to supply others with water for a price.
---
cssclass: [monsters]
title1: Island Defender
title2: Island Defender
CR: 6
sources:
- name: NPC Codex
  page: 66
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 2400
race: Elf
classes:
- druid 7
alignment: LN
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 6
senses:
  low-light vision: true
AC:
  AC: 24
  touch: 14
  flat_footed: 22
  components:
    armor: 7
    deflection: 2
    dex: 2
    shield: 3
HP:
  HP: 47
  long: 7d8+12
saves:
  fort: 6
  ref: 6
  will: 8
  other: +2 vs. enchantments, +4 vs. fey and plant-targeted effects
immunities:
- sleep
resistances:
  cold: 10
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk shortspear +6 (1d6)
      entries:
      - - damage: 1d6
      attack: mwk shortspear
      bonus:
      - 6
  - - text: club +5 (1d6)
      entries:
      - - damage: 1d6
      attack: club
      bonus:
      - 5
  ranged:
  - - text: mwk shortspear +8 (1d6)
      entries:
      - - damage: 1d6
      attack: mwk shortspear
      bonus:
      - 8
  special:
  - wild shape 2/day
spell_like_abilities:
  entries:
  - name: icicle
    source: default
    freq: 6/day
  sources:
  - name: default
    CL: 7
    concentration: 10
spells:
  entries:
  - is_domain_spell: true
    name: control water
    source: Druid
    level: 4
  - name: ice storm
    source: Druid
    level: 4
  - name: cure moderate wounds
    source: Druid
    level: 3
  - name: daylight
    source: Druid
    level: 3
  - name: sleet storm
    source: Druid
    level: 3
  - is_domain_spell: true
    name: water breathing
    source: Druid
    level: 3
  - name: animal messenger
    source: Druid
    level: 2
  - name: barkskin
    source: Druid
    level: 2
  - name: bear's endurance
    source: Druid
    level: 2
  - is_domain_spell: true
    name: fog cloud
    source: Druid
    level: 2
  - name: resist energy
    source: Druid
    level: 2
  - name: cure light wounds
    source: Druid
    level: 1
  - name: endure elements
    source: Druid
    level: 1
  - name: magic fang
    source: Druid
    level: 1
  - is_domain_spell: true
    name: obscuring mist
    source: Druid
    level: 1
  - name: shillelagh
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
  - name: light
    source: Druid
    level: 0
  - name: mending
    source: Druid
    level: 0
  - name: purify food and drink
    source: Druid
    level: 0
  - name: read magic
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 7
    concentration: 10
    slots:
      0: at-will
    domains:
    - water
tactics:
  Before Combat: The druid drinks her potion of shield of faith.
  During Combat: The druid prefers to be in or near a body of water to take advantage
    of her abilities. She opens with her ice storm or fog cloud spells in order to
    slow down her opponents. Afterward, she wild shapes into either a dire bear or
    a giant octopus (depending on the terrain), and alternates rounds of attacks with
    spells such as bear's endurance and barkskin.
  Base Statistics: Without shield of faith, the druid's statistics are AC 22, touch
    12, flat-footed 20; CMD 17.
ability_scores:
  STR: 10
  DEX: 14
  CON: 12
  INT: 15
  WIS: 16
  CHA: 8
BAB: 5
CMB: 5
CMD: 19
feats:
- name: Combat Casting
- name: Improved Initiative
- name: Lightning Reflexes
- name: Natural Spell
skills:
  Fly: 4
  Handle Animal: 5
  Heal: 11
  Knowledge (history): 4
  Knowledge (nature): 14
  Linguistics: 3
  Perception: 15
  Spellcraft: 11
    to identify magic item properties: 13
  Survival: 14
  Swim: 5
languages:
- Common
- Aquan
- Draconic
- Druidic
- Elven
- Sylvan
special_qualities:
- elven magic
- nature bond (Water domain)
- nature sense
- trackless step
- weapon familiarity
- wild empathy +6
- woodland stride
gear:
  combat:
  - dust of dryness
  - potion of haste
  - potion of shield of faith
  - wand of cure moderate wounds (8 charges)
  - thunderstone (2)
  other:
  - i>+1 dragonhide breastplate
  - +1 darkwood heavy wooden shield
  - club
  - masterwork shortspear
  - feather token (fan)
  - antitoxin
  - fishing net
  - holly and mistletoe
  - silk rope (50 ft.)
  - spell component pouch
  - gold torc (worth 100 gp)
  - 43 gp
desc_long: Some druids seek the peace and tranquility that only a small island can
  offer and are willing to lay down their life to protect their sanctuary.

---

# Island Defender

**Source** NPC Codex pg. 66
**XP** 2,400
Elf _[[classes/Druid|druid]]_ 7

LN Medium humanoid (elf)
**Init** +6; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +15

##### Defense

**AC** 24, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+7 armor, +2 _[[spells/Deflection|deflection]]_, +2 Dex, +3 _[[spells/Shield|shield]]_)
**hp** 47 (7d8+12)
**Fort** +6, **Ref** +6, **Will** +8; +2 vs. enchantments, +4 vs. fey and plant-targeted effects
**Immune** sleep; **Resist** cold 10

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Shortspear|shortspear]]_ +6 (1d6) or _[[items/Weapon/Club|club]]_ +5 (1d6)
**Ranged** mwk _shortspear_ +8 (1d6)
**Special Attacks** wild shape 2/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +10)
6/day—icicle
**_Druid_ Spells Prepared **(CL 7th; concentration +10)
4th—_[[spells/Control Water|control water]]_, _[[spells/Ice Storm|ice storm]]_
3rd—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Daylight|daylight]]_, _[[spells/Sleet Storm|sleet storm]]_, _[[universal monster rules/Water Breathing|water breathing]]_
2nd—_[[spells/Animal Messenger|animal messenger]]_, _[[spells/Barkskin|barkskin]]_, bear’s _[[feats/Endurance|endurance]]_, _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Resist Energy|resist energy]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Endure Elements|endure elements]]_, _[[spells/Magic Fang|magic fang]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shillelagh|shillelagh]]_, _[[spells/Speak with Animals|speak with animals]]_
0 (at will)—light, _[[spells/Mending|mending]]_, _[[spells/Purify Food and Drink|purify food and drink]]_, _[[spells/Read Magic|read magic]]_
**D **Domain spell; **Domain **Water

### Tactics

**Before Combat **The _druid_ drinks her potion of _[[spells/Shield Of Faith|shield of faith]]_.
**During Combat **The _druid_ prefers to be in or near a body of water to take advantage of her abilities. She opens with her _ice storm_ or _fog cloud_ spells in order to _[[spells/Slow|slow]]_ down her opponents. Afterward, she wild shapes into either a dire bear or a giant _[[monsters/Octopus|octopus]]_ (depending on the terrain), and alternates rounds of attacks with spells such as bear’s _endurance_ and _barkskin_.
**Base Statistics **Without _shield of faith_, the _druid_’s statistics are **AC **22, touch 12, _flat-footed_ 20; **CMD **17.

##### Statistics
**Str** 10, **Dex** 14, **Con** 12, **Int** 15, **Wis** 16, **Cha** 8
**Base Atk** +5; **CMB** +5; **CMD** 19
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Natural Spell|Natural Spell]]_
**Skills** Fly +4, Handle Animal +5, _[[spells/Heal|Heal]]_ +11, Knowledge (history) +4, Knowledge (nature) +14, Linguistics +3, Perception +15, Spellcraft +11 (+13 to _[[spells/Identify|identify]]_ magic item properties), Survival +14, Swim +5
**Languages** Common, Aquan, Draconic, Druidic, Elven, Sylvan
**SQ** elven magic, nature bond (Water domain), nature sense, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, weapon familiarity, wild _[[feats/Empathy|empathy]]_ +6, woodland stride
**Combat Gear** _[[items/Wondrous Item/Dust of Dryness|dust of dryness]]_, potion of _[[spells/Haste|haste]]_, potion of _shield of faith_, wand of _cure moderate wounds_ (8 charges), _[[items/Mundane/Thunderstone|thunderstone]]_ (2); **Other Gear** i&gt;+1 dragonhide _[[items/Armor/Breastplate|breastplate]]_, +1 darkwood _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, _club_, masterwork _shortspear_, feather token (fan), _[[items/Mundane/Antitoxin|antitoxin]]_, _[[items/Mundane/Fishing net|fishing net]]_, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, _[[items/Mundane/Silk rope|silk rope]]_ (50 ft.), _[[items/Mundane/Spell component pouch|spell component pouch]]_, gold torc (worth 100 gp), 43 gp

Some druids seek the peace and tranquility that only a small island can offer and are willing to lay down their life to protect their _[[spells/Sanctuary|sanctuary]]_.
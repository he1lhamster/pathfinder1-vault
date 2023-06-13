---
cssclass: [monsters]
title1: Cavern Defender
title2: Cavern Defender
CR: 4
sources:
- name: NPC Codex
  page: 64
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 1200
race: Half-elf
classes:
- druid 5
alignment: N
size: Medium
type: humanoid
subtypes:
- elf
- human
initiative:
  bonus: 2
senses:
  low-light vision: true
AC:
  AC: 20
  touch: 13
  flat_footed: 17
  components:
    armor: 5
    dex: 2
    dodge: 1
    shield: 2
HP:
  HP: 31
  long: 5d8+5
saves:
  fort: 6
  ref: 6
  will: 9
  other: +2 vs. enchantments, +4 vs. fey and plant-targeted effects
speeds:
  base: 20
attacks:
  melee:
  - - text: quarterstaff +2 (1d6-1)
      entries:
      - - damage: 1d6-1
      attack: quarterstaff
      bonus:
      - 2
  - - text: sickle +2 (1d6-1)
      entries:
      - - damage: 1d6-1
      attack: sickle
      bonus:
      - 2
  ranged:
  - - text: mwk sling +6 (1d4-1)
      entries:
      - - damage: 1d4-1
      attack: mwk sling
      bonus:
      - 6
  special:
  - wild shape 1/day
spell_like_abilities:
  entries:
  - name: acid dart
    source: default
    freq: 7/day
  sources:
  - name: default
    CL: 5
    concentration: 9
spells:
  entries:
  - name: spike growth
    source: Druid
    level: 3
    count: 2
    DC: 17
  - is_domain_spell: true
    name: stone shape
    source: Druid
    level: 3
  - name: barkskin
    source: Druid
    level: 2
  - name: bear's endurance
    source: Druid
    level: 2
  - is_domain_spell: true
    name: soften earth and stone
    source: Druid
    level: 2
  - name: summon swarm
    source: Druid
    level: 2
  - name: cure light wounds
    source: Druid
    level: 1
  - is_domain_spell: true
    name: magic stone
    source: Druid
    level: 1
  - name: obscuring mist
    source: Druid
    level: 1
  - name: shillelagh
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
  - name: create water
    source: Druid
    level: 0
  - name: guidance
    source: Druid
    level: 0
  - name: know direction
    source: Druid
    level: 0
  - name: light
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 5
    concentration: 9
    slots:
      0: at-will
    domains:
    - earth
tactics:
  Before Combat: The druid casts spike growth twice per day to protect her position,
    using stone shape if necessary to limit any viable approaches to her.
  During Combat: The druid wild shapes into a small flying animal at the first opportunity
    to escape melee. On subsequent rounds, she casts soften earth and stone and spike
    growth to distort the terrain beneath her enemies. She intersperses these spells
    with speak with animals and summoning spells to call flying creatures to harass
    those enemies. Once her spells are exhausted, she uses acid dart.
ability_scores:
  STR: 8
  DEX: 14
  CON: 13
  INT: 12
  WIS: 18
  CHA: 10
BAB: 3
CMB: 2
CMD: 15
feats:
- name: Dodge
- name: Lightning Reflexes
- name: Natural Spell
- name: Skill Focus (Survival)
skills:
  Climb: 1
  Fly: 4
  Handle Animal: 6
  Heal: 10
  Knowledge (dungeoneering): 6
  Knowledge (nature): 11
  Perception: 11
  Spellcraft: 7
  Survival: 15
languages:
- Common
- Druidic
- Elven
- Undercommon
special_qualities:
- elf blood
- nature bond (Earth domain)
- nature sense
- trackless step
- wild empathy +5
- woodland stride
gear:
  combat:
  - wand of cure light wounds (50 charges)
  - alchemist's fire (3)
  other:
  - +1 hide armor
  - heavy wooden shield
  - masterwork sling with 20 bullets
  - quarterstaff
  - sickle
  - cloak of resistance +1
  - backpack
  - healer's kit
  - holly and mistletoe
  - silk rope (50 ft.)
  - spell component pouch
  - 91 gp
desc_long: Though most druids tend and protect the wild lands that lie under the open
  sky, others stalk the tunnels that lie beneath the earth, serving as wardens, protectors,
  and tenders of vermin and fungi.

---

# Cavern Defender

**Source** NPC Codex pg. 64
**XP** 1,200
Half-elf _[[classes/Druid|druid]]_ 5

N Medium humanoid (elf, human)
**Init** +2; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +11

##### Defense

**AC** 20, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+5 armor, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +2 _[[spells/Shield|shield]]_)
**hp** 31 (5d8+5)
**Fort** +6, **Ref** +6, **Will** +9; +2 vs. enchantments, +4 vs. fey and plant-targeted effects

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Quarterstaff|quarterstaff]]_ +2 (1d6–1) or _[[items/Weapon/Sickle|sickle]]_ +2 (1d6–1)
**Ranged** mwk _[[items/Weapon/Sling|sling]]_ +6 (1d4–1)
**Special Attacks** wild shape 1/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +9)
7/day—acid _[[items/Weapon/Dart|dart]]_
**_Druid_ Spells Prepared **(CL 5th; concentration +9)
3rd—_[[spells/Spike Growth|spike growth]]_ (2, DC 17), _[[spells/Stone Shape|stone shape]]_
2nd—_[[spells/Barkskin|barkskin]]_, bear’s _[[feats/Endurance|endurance]]_, _[[spells/Soften Earth and Stone|soften earth and stone]]_, _[[spells/Summon Swarm|summon swarm]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Magic Stone|magic stone]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shillelagh|shillelagh]]_, _[[spells/Speak with Animals|speak with animals]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Guidance|guidance]]_, _[[spells/Know Direction|know direction]]_, light
**D **Domain spell; **Domain **Earth

### Tactics

**Before Combat **The _druid_ casts _spike growth_ twice per day to protect her position, using _stone shape_ if necessary to limit any viable approaches to her.
**During Combat **The _druid_ wild shapes into a small flying animal at the first opportunity to escape melee. On subsequent rounds, she casts _soften earth and stone_ and _spike growth_ to distort the terrain beneath her enemies. She intersperses these spells with _speak with animals_ and summoning spells to call flying creatures to harass those enemies. Once her spells are _[[conditions/Exhausted|exhausted]]_, she uses acid _dart_.

##### Statistics
**Str** 8, **Dex** 14, **Con** 13, **Int** 12, **Wis** 18, **Cha** 10
**Base Atk** +3; **CMB** +2; **CMD** 15
**Feats** _Dodge_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Skill Focus|Skill Focus]]_ (Survival)
**Skills** _[[universal monster rules/Climb|Climb]]_ +1, Fly +4, Handle Animal +6, _[[spells/Heal|Heal]]_ +10, Knowledge (dungeoneering) +6, Knowledge (nature) +11, Perception +11, Spellcraft +7, Survival +15
**Languages** Common, Druidic, Elven, Undercommon
**SQ** elf blood, nature bond (Earth domain), nature sense, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, wild _[[feats/Empathy|empathy]]_ +5, woodland stride
**Combat Gear** wand of _cure light wounds_ (50 charges), _[[classes/Alchemist|alchemist]]_’s fire (3); **Other Gear** +1 _[[items/Armor/Hide armor|hide armor]]_, _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, masterwork _sling_ with 20 bullets, _quarterstaff_, _sickle_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, backpack, _[[npcs/Healer|healer]]_’s kit, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, _[[items/Mundane/Silk rope|silk rope]]_ (50 ft.), _[[items/Mundane/Spell component pouch|spell component pouch]]_, 91 gp

Though most druids tend and protect the wild lands that lie under the open sky, others stalk the tunnels that lie beneath the earth, serving as wardens, protectors, and tenders of vermin and fungi.
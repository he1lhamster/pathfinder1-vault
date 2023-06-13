---
cssclass: [monsters]
title1: Strix, Strix Rokoa
desc_short: This proud avian woman stands tall and alert despite her years. Claws,
  bones, and feathers clatter on her crown and staff.
title2: Strix Rokoa
CR: 11
sources:
- name: Inner Sea Monster Codex
  page: 57
  link: http://paizo.com/products/btpy9elc?Pathfinder-Campaign-Setting-Inner-Sea-Monster-Codex
XP: 12800
race: Strix
classes:
- shaman (speaker for the past) 12 (Pathfinder RPG Advanced Race Guide 200, Pathfinder
  RPG Advanced Class Guide 35, 111)
alignment: LN
size: Medium
type: humanoid
subtypes:
- strix
initiative:
  bonus: 1
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 20
  touch: 12
  flat_footed: 19
  components:
    armor: 7
    deflection: 1
    dex: 1
    natural: 1
HP:
  HP: 78
  long: 12d8+24
saves:
  fort: 7
  ref: 7
  will: 14
  other: +2 bonus vs. illusion spells or effects
resistances:
  electricity: 10
speeds:
  base: 20
  fly: 45
  fly_maneuverability: average
attacks:
  melee:
  - - text: mwk quarterstaff +9/+4 (1d6-1 plus 1d6 electricity)
      entries:
      - - damage: 1d6-1
        - damage: 1d6
          type: electricity
      attack: mwk quarterstaff
      bonus:
      - 9
      - 4
  ranged:
  - - text: dart +10 (1d4-1 plus 1d6 electricity)
      entries:
      - - damage: 1d4-1
        - damage: 1d6
          type: electricity
      attack: dart
      bonus:
      - 10
  special:
  - hatred
  - hexes (air barrier, fortune, healing, wind sight, wind ward)
spell_like_abilities:
  entries:
  - name: know direction
    source: default
    freq: Constant
  - name: virtue
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 12
    concentration: 12
spells:
  entries:
  - name: cone of cold
    source: Shaman
    level: 6
    DC: 21
  - name: greater dispel magic
    source: Shaman
    level: 6
  - superscripts:
    - APG
    is_spirit_spell: true
    name: sirocco
    source: Shaman
    level: 6
    DC: 21
  - name: baleful polymorph
    source: Shaman
    level: 5
    DC: 19
  - is_spirit_spell: true
    name: control winds
    source: Shaman
    level: 5
    DC: 19
  - name: dominate person
    source: Shaman
    level: 5
    DC: 19
  - name: wall of fire
    source: Shaman
    level: 5
  - superscripts:
    - ACG
    name: air geyser
    source: Shaman
    level: 4
    DC: 19
  - name: cure critical wounds
    source: Shaman
    level: 4
  - name: ice storm
    source: Shaman
    level: 4
  - name: poison
    source: Shaman
    level: 4
    DC: 18
  - superscripts:
    - APG
    is_spirit_spell: true
    name: river of wind
    source: Shaman
    level: 4
    DC: 19
  - name: bestow curse
    source: Shaman
    level: 3
    DC: 17
  - name: call lightning
    source: Shaman
    level: 3
    DC: 18
  - superscripts:
    - APG
    is_spirit_spell: true
    name: cloak of winds
    source: Shaman
    level: 3
    DC: 17
  - name: deep slumber
    source: Shaman
    level: 3
    DC: 17
  - name: dispel magic
    source: Shaman
    level: 3
  - name: speak with dead
    source: Shaman
    level: 3
    DC: 17
  - name: aid
    source: Shaman
    level: 2
  - superscripts:
    - ACG
    name: focused scrutiny
    source: Shaman
    level: 2
  - is_spirit_spell: true
    name: gust of wind
    source: Shaman
    level: 2
    DC: 17
  - name: hold person
    source: Shaman
    level: 2
    DC: 16
  - name: lesser restoration
    source: Shaman
    level: 2
  - name: summon swarm
    source: Shaman
    level: 2
  - superscripts:
    - APG
    is_spirit_spell: true
    name: alter winds
    source: Shaman
    level: 1
    DC: 15
  - name: bless
    source: Shaman
    level: 1
  - name: hide from animals
    source: Shaman
    level: 1
  - name: magic weapon
    source: Shaman
    level: 1
  - name: obscuring mist
    source: Shaman
    level: 1
  - superscripts:
    - ACG
    name: sense spirit magic
    source: Shaman
    level: 1
  - name: detect magic
    source: Shaman
    level: 0
  - name: guidance
    source: Shaman
    level: 0
  - name: purify food and drink
    source: Shaman
    level: 0
    DC: 14
  - name: read magic
    source: Shaman
    level: 0
  sources:
  - name: Shaman
    type: prepared
    CL: 12
    concentration: 16
    slots:
      0: at-will
    spirit: wind
ability_scores:
  STR: 8
  DEX: 12
  CON: 13
  INT: 14
  WIS: 18
  CHA: 10
BAB: 9
CMB: 8
CMD: 20
feats:
- name: Combat Casting
- superscripts:
  - ACG
  name: Nature Magic
- name: Persuasive
- name: Skill Focus (Knowledge [history])
- name: Spell Focus (evocation)
- superscripts:
  - ACG
  name: Spirit Talker
skills:
  Acrobatics: -2
    when jumping: -6
  Diplomacy: 17
  Fly: 9
  Heal: 17
  Intimidate: 7
  Knowledge (arcana): 7
  Knowledge (history): 23
  Knowledge (nature): 10
  Perception: 12
    in dim light or darkness: 14
  Spellcraft: 15
  Stealth: -2
    in dim light or darkness: 0
  Survival: 9
languages:
- Auran
- Goblin
- Strix
special_qualities:
- nocturnal
- revelations of the past (momentary glimpse, voice of the grave, wisdom of the ancestors)
- shocking touch (1d6+6 electricity)
- spark soul (12d4 electricity)
- suspicious
gear:
  combat:
  - potion of invisibility
  - scroll of eagle's splendor
  - scroll of flame strike
  - scroll of fog cloud
  - wand of owl's wisdom (9 charges)
  other:
  - +3 bone scale mail
  - darts (10)
  - mwk quarterstaff
  - amulet of natural armor +1
  - cloak of resistance +2
  - ring of protection +1
ecology:
  environment: temperate mountains
desc_long: A rokoa is the spiritual leader of a strix tribe. Her duties include deciphering
  portents, performing funeral rites, tending to the bones of the deceased, and recalling
  the names of fallen heroes. She is considered the spiritual mother of the tribe.

---

# Strix, Strix Rokoa
This proud avian woman stands tall and alert despite her years. Claws, bones, and feathers clatter on her crown and staff.
**Source** Inner Sea Monster Codex pg. 57
**XP** 12,800
_[[monsters/Strix|Strix]]_ _[[classes/Shaman|shaman]]_ (speaker for the past) 12 (Pathfinder RPG Advanced Race Guide 200, Pathfinder RPG Advanced Class Guide 35, 111)

LN Medium humanoid (_strix_)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +12 (+14 in dim light or _[[spells/Darkness|darkness]]_)

##### Defense

**AC** 20, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+7 armor, +1 _[[spells/Deflection|deflection]]_, +1 Dex, +1 natural)
**hp** 78 (12d8+24)
**Fort** +7, **Ref** +7, **Will** +14; +2 bonus vs. illusion spells or effects
**Resist** electricity 10

##### Offense
**Speed** 20 ft., fly 45 ft. (average)
**Melee** mwk _[[items/Weapon/Quarterstaff|quarterstaff]]_ +9/+4 (1d6–1 plus 1d6 electricity)
**Ranged** _[[items/Weapon/Dart|dart]]_ +10 (1d4–1 plus 1d6 electricity)
**Special Attacks** hatred, hexes (air barrier, fortune, healing, wind sight, wind ward)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +12)
Constant—_[[spells/Know Direction|know direction]]_
1/day—_[[spells/Virtue|virtue]]_
**_Shaman_ Spells Prepared **(CL 12th; concentration +16)
6th—_[[spells/Cone of Cold|cone of cold]]_ (DC 21), greater _[[spells/Dispel Magic|dispel magic]]_, siroccoS, APG (DC 21)
5th—_[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 19), _[[spells/Control Winds|control winds]]_ (DC 19), _[[spells/Dominate Person|dominate person]]_ (DC 19), _[[spells/Wall Of Fire|wall of fire]]_
4th—_[[spells/Air Geyser|air geyser]]_ (DC 19), _[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Ice Storm|ice storm]]_, poison (DC 18), river of windS, APG (DC 19)
3rd—_[[spells/Bestow Curse|bestow curse]]_ (DC 17), _[[spells/Call Lightning|call lightning]]_ (DC 18), cloak of windsS, APG (DC 17), _[[spells/Deep Slumber|deep slumber]]_ (DC 17), _dispel magic_, _[[spells/Speak with Dead|speak with dead]]_ (DC 17)
2nd—aid, _[[spells/Focused Scrutiny|focused scrutiny]]_, _[[spells/Gust Of Wind|gust of wind]]_ (DC 17), _[[spells/Hold Person|hold person]]_ (DC 16), lesser _[[spells/Restoration|restoration]]_, _[[spells/Summon Swarm|summon swarm]]_
1st—alter windsS, APG (DC 15), _[[spells/Bless|bless]]_, _[[spells/Hide from Animals|hide from animals]]_, _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Sense Spirit Magic|sense spirit magic]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Purify Food and Drink|purify food and drink]]_ (DC 14), _[[spells/Read Magic|read magic]]_
**S** spirit magic spell; **Spirit** Wind

##### Statistics
**Str** 8, **Dex** 12, **Con** 13, **Int** 14, **Wis** 18, **Cha** 10
**Base Atk** +9; **CMB** +8; **CMD** 20
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Nature Magic|Nature Magic]]_, _[[feats/Persuasive|Persuasive]]_, _[[feats/Skill Focus|Skill Focus]]_ (Knowledge [history]), _[[feats/Spell Focus|Spell Focus]]_ (evocation), _[[feats/Spirit Talker|Spirit Talker]]_
**Skills** Acrobatics –2 (–6 when jumping), Diplomacy +17, Fly +9, _[[spells/Heal|Heal]]_ +17, Intimidate +7, Knowledge (arcana) +7, Knowledge (history) +23, Knowledge (nature) +10, Perception +12 (+14 in dim light or _darkness_), Spellcraft +15, Stealth –2 (+0 in dim light or _darkness_), Survival +9
**Languages** Auran, _[[monsters/Goblin|Goblin]]_, _Strix_
**SQ** nocturnal, revelations of the past (momentary glimpse, voice of the grave, wisdom of the ancestors), shocking touch (1d6+6 electricity), _[[spells/Spark|spark]]_ soul (12d4 electricity), suspicious
**Combat Gear** potion of _[[spells/Invisibility|invisibility]]_, scroll of _[[monsters/Eagle|eagle]]_’s splendor, scroll of _[[spells/Flame Strike|flame strike]]_, scroll of _[[spells/Fog Cloud|fog cloud]]_, wand of owl’s wisdom (9 charges); **Other Gear** +3 bone _[[items/Armor/Scale mail|scale mail]]_, darts (10), mwk _quarterstaff_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_

##### Ecology

**Environment** temperate mountains

##### Description

A rokoa is the spiritual leader of a _strix_ tribe. Her duties include deciphering portents, performing funeral rites, tending to the bones of the deceased, and recalling the names of _[[monsters/Fallen|fallen]]_ heroes. She is considered the spiritual mother of the tribe.
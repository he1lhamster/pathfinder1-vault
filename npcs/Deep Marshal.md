---
cssclass: [monsters]
title1: Deep Marshal
title2: Deep Marshal
CR: 15
sources:
- name: NPC Codex
  page: 191
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 51200
race: Dwarf
classes:
- abjurer 16
alignment: LN
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 6
senses:
  darkvision: 60
  see invisibility: true
AC:
  AC: 26
  touch: 17
  flat_footed: 23
  components:
    armor: 4
    deflection: 4
    dex: 2
    dodge: 1
    natural: 3
    shield: 2
HP:
  HP: 130
  long: 16d6+72
saves:
  fort: 13
  ref: 11
  will: 18
  other: +4 vs. mind-affecting, +2 vs. poison, spells, and spell-like abilities
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
- energy absorption (48/day)
- mind blank
DR:
- amount: 10
  weakness: adamantine
  max_absorb: 150
immunities:
- fire (120 points)
resistances:
  cold: 10
  electricity: 30
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 spell storing warhammer +8/+3 (1d8/×3)
      entries:
      - - damage: 1d8
          crit_multiplier: 3
      attack: +1 spell storing warhammer
      bonus:
      - 8
      - 3
  ranged:
  - - text: light crossbow +10 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 10
  special:
  - +1 on attack rolls against goblinoid and orc humanoids
spells:
  entries:
  - name: quickened charm monster
    source: Abjurer
    level: 8
    DC: 23
  - name: mind blank
    source: Abjurer
    level: 8
  - name: prismatic wall
    source: Abjurer
    level: 8
  - name: banishment
    source: Abjurer
    level: 7
    DC: 23
  - name: quickened haste
    source: Abjurer
    level: 7
  - name: mass hold person
    source: Abjurer
    level: 7
    DC: 25
  - name: phase door
    source: Abjurer
    level: 7
  - name: globe of invulnerability
    source: Abjurer
    level: 6
  - name: greater dispel magic
    source: Abjurer
    level: 6
  - name: greater heroism
    source: Abjurer
    level: 6
  - name: mass bull's strength
    source: Abjurer
    level: 6
  - name: mass suggestion
    source: Abjurer
    level: 6
    DC: 24
  - name: break enchantment
    source: Abjurer
    level: 5
  - name: stilled dimension door
    source: Abjurer
    level: 5
  - name: dominate person
    source: Abjurer
    level: 5
    count: 2
    DC: 23
  - name: telepathic bond
    source: Abjurer
    level: 5
  - name: wall of stone
    source: Abjurer
    level: 5
  - name: arcane eye
    source: Abjurer
    level: 4
  - name: charm monster
    source: Abjurer
    level: 4
    DC: 22
  - name: confusion
    source: Abjurer
    level: 4
    DC: 22
  - name: remove curse
    source: Abjurer
    level: 4
  - name: solid fog
    source: Abjurer
    level: 4
  - name: stoneskin
    source: Abjurer
    level: 4
  - name: dispel magic
    source: Abjurer
    level: 3
  - name: haste
    source: Abjurer
    level: 3
    DC: 19
  - name: hold person
    source: Abjurer
    level: 3
    count: 2
    DC: 21
  - name: protection from energy
    source: Abjurer
    level: 3
  - name: wind wall
    source: Abjurer
    level: 3
  - name: acid arrow
    source: Abjurer
    level: 2
  - name: hideous laughter
    source: Abjurer
    level: 2
    DC: 20
  - name: invisibility
    source: Abjurer
    level: 2
  - name: levitate
    source: Abjurer
    level: 2
  - name: resist energy
    source: Abjurer
    level: 2
    count: 2
  - name: see invisibility
    source: Abjurer
    level: 2
  - name: alarm
    source: Abjurer
    level: 1
  - name: charm person
    source: Abjurer
    level: 1
    DC: 19
  - name: expeditious retreat
    source: Abjurer
    level: 1
  - name: feather fall
    source: Abjurer
    level: 1
  - name: grease
    source: Abjurer
    level: 1
  - name: mage armor
    source: Abjurer
    level: 1
  - name: true strike
    source: Abjurer
    level: 1
  - name: dancing lights
    source: Abjurer
    level: 0
  - name: detect magic
    source: Abjurer
    level: 0
  - name: message
    source: Abjurer
    level: 0
  - name: resistance
    source: Abjurer
    level: 0
  sources:
  - name: Abjurer
    type: prepared
    CL: 16
    concentration: 22
    slots:
      0: at-will
    opposition_schools:
    - evocation
    - necromancy
tactics:
  Before Combat: The wizard casts mage armor, mind blank, protection from energy (fire),
    resist energy (electricity), see invisibility, and stoneskin. She casts telepathic
    bond on allies.
  During Combat: The wizard's warhammer contains hold person.
  Base Statistics: Without mage armor, mind blank, protection from energy, resist
    energy, see invisibility, and stoneskin, the wizard's statistics are Senses darkvision
    60 ft.; AC 22, touch 17, flat-footed 19; Fort +13, Ref +11, Will +18; +2 vs. poison,
    spells, and spell-like abilities; Defensive Abilities defensive training (+4 dodge
    bonus to AC vs. giants), energy absorption (48/day); DR none; Immune none; Resist
    cold 10.
ability_scores:
  STR: 8
  DEX: 14
  CON: 18
  INT: 22
  WIS: 14
  CHA: 8
BAB: 8
CMB: 7
CMD: 24
CMD_other: 28 vs. bull rush or trip
feats:
- name: Combat Casting
- name: Craft Wondrous Item
- name: Dodge
- name: Forge Ring
- name: Greater Spell Focus (enchantment)
- name: Improved Initiative
- name: Iron Will
- name: Quicken Spell
- name: Scribe Scroll
- name: Spell Focus (enchantment)
- name: Spell Penetration
- name: Still Spell
skills:
  Appraise: 14
    to assess nonmagical metals or gemstones: 16
  Climb: 2
  Craft (sculpture): 14
  Knowledge (arcana): 24
  Knowledge (dungeoneering): 24
  Knowledge (engineering): 24
  Knowledge (geography): 19
  Knowledge (history): 19
  Knowledge (planes): 19
  Perception: 17
    to notice unusual stonework: 19
  Sense Motive: 12
  Spellcraft: 24
  Survival: 7
  Swim: 2
languages:
- Common
- Dwarven
- Giant
- Gnome
- Goblin
- Orc
- Terran
- Undercommon
special_qualities:
- arcane bond (warhammer)
- protective ward (6 rounds, +4 deflection, 9/day)
gear:
  combat:
  - potion of cure moderate wounds
  - scroll of maze
  - scroll of summon monster VIII
  other:
  - +1 spell storing warhammer
  - amulet of natural armor +3
  - bag of holding (type I)
  - belt of mighty constitution +2
  - cloak of resistance +4
  - gloves of arrow snaring
  - headband of vast intelligence +4
  - ring of force shield
  - ring of protection +4
  - spellbook
  - diamond dust (worth 500 gp)
  - 700 gp
desc_long: These wizards protect underground communities.

---

# Deep Marshal

**Source** NPC Codex pg. 191
**XP** 51,200
Dwarf abjurer 16

LN Medium humanoid (dwarf)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/See Invisibility|see invisibility]]_; Perception +17

##### Defense

**AC** 26, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+4 armor, +4 _[[spells/Deflection|deflection]]_, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +3 natural, +2 _[[spells/Shield|shield]]_)
**hp** 130 (16d6+72)
**Fort** +13, **Ref** +11, **Will** +18; +4 vs. mind-affecting, +2 vs. poison, spells, and _[[universal monster rules/Spell-Like Abilities|spell-like abilities]]_
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _dodge_ bonus to AC vs. giants), energy absorption (48/day), _[[spells/Mind Blank|mind blank]]_; **DR** 10/adamantine (150 points); **Immune** fire (120 points); **Resist** cold 10, electricity 30

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon Magic Abilities/Spell Storing|spell storing]]_ _[[items/Weapon/Warhammer|warhammer]]_ +8/+3 (1d8/×3)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +10 (1d8/19–20)
**Special Attacks** +1 on attack rolls against goblinoid and _[[monsters/Orc|orc]]_ humanoids
**Abjurer Spells Prepared **(CL 16th; concentration +22)
8th—quickened _[[spells/Charm Monster|charm monster]]_ (DC 23), _mind blank_, _[[spells/Prismatic Wall|prismatic wall]]_
7th—_[[spells/Banishment|banishment]]_ (DC 23), quickened _[[spells/Haste|haste]]_, mass _[[spells/Hold Person|hold person]]_ (DC 25), _[[spells/Phase Door|phase door]]_
6th—_[[spells/Globe Of Invulnerability|globe of invulnerability]]_, greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ _[[spells/Heroism|heroism]]_, mass bull’s strength, mass _[[spells/Suggestion|suggestion]]_ (DC 24)
5th—_[[spells/Break Enchantment|break enchantment]]_, stilled _[[spells/Dimension Door|dimension door]]_, _[[spells/Dominate Person|dominate person]]_ (2, DC 23), _[[spells/Telepathic Bond|telepathic bond]]_, _[[spells/Wall Of Stone|wall of stone]]_
4th—_[[spells/Arcane Eye|arcane eye]]_, _charm monster_ (DC 22), _[[spells/Confusion|confusion]]_ (DC 22), _[[spells/Remove Curse|remove curse]]_, _[[spells/Solid Fog|solid fog]]_, _[[spells/Stoneskin|stoneskin]]_
3rd—_[[spells/Dispel Magic|dispel magic]]_, _haste_ (DC 19), _hold person_ (2, DC 21), _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Wind Wall|wind wall]]_
2nd—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Hideous Laughter|hideous laughter]]_ (DC 20), _[[spells/Invisibility|invisibility]]_, _[[spells/Levitate|levitate]]_, _[[spells/Resist Energy|resist energy]]_ (2), _see invisibility_
1st—_[[spells/Alarm|alarm]]_, _[[spells/Charm Person|charm person]]_ (DC 19), _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Grease|grease]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Message|message]]_, _[[universal monster rules/Resistance|resistance]]_
**Opposition Schools **evocation, necromancy

### Tactics

**Before Combat **The _[[classes/Wizard|wizard]]_ casts _mage armor_, _mind blank_, _protection from energy_ (fire), _resist energy_ (electricity), _see invisibility_, and _stoneskin_. She casts _telepathic bond_ on allies.
**During Combat **The _wizard_’s _warhammer_ contains _hold person_.
**Base Statistics **Without _mage armor_, _mind blank_, _protection from energy_, _resist energy_, _see invisibility_, and _stoneskin_, the _wizard_’s statistics are **Senses **_darkvision_ 60 ft.; **AC **22, touch 17, _flat-footed_ 19; **Fort **+13, **Ref **+11, **Will **+18; +2 vs. poison, spells, and _spell-like abilities_; **Defensive Abilities **defensive _training_ (+4 _dodge_ bonus to AC vs. giants), energy absorption (48/day); **DR **none; **Immune **none; **Resist **cold 10.

##### Statistics
**Str** 8, **Dex** 14, **Con** 18, **Int** 22, **Wis** 14, **Cha** 8
**Base Atk** +8; **CMB** +7; **CMD** 24 (28 vs. bull rush or _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _Dodge_, _[[feats/Forge Ring|Forge Ring]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (enchantment), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Focus|Spell Focus]]_ (enchantment), _[[feats/Spell Penetration|Spell Penetration]]_, _[[feats/Still Spell|Still Spell]]_
**Skills** Appraise +14 (+16 to assess nonmagical metals or gemstones), _[[universal monster rules/Climb|Climb]]_ +2, Craft (sculpture) +14, Knowledge (arcana, dungeoneering, engineering) +24, Knowledge (geography, history, planes) +19, Perception +17 (+19 to notice unusual stonework), Sense Motive +12, Spellcraft +24, Survival +7, Swim +2
**Languages** Common, Dwarven, Giant, Gnome, _[[monsters/Goblin|Goblin]]_, _Orc_, Terran, Undercommon
**SQ** arcane bond (_warhammer_), protective ward (6 rounds, +4 _deflection_, 9/day)
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, scroll of _[[spells/Maze|maze]]_, scroll of _[[spells/Summon Monster VIII|summon monster VIII]]_; **Other Gear** +1 _spell storing_ _warhammer_, _[[items/Wondrous Item/Amulet of Natural Armor +3|amulet of natural armor +3]]_, bag of holding (type I), _[[items/Wondrous Item/Belt of Mighty Constitution +2|belt of mighty constitution +2]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +4|cloak of _resistance_ +4]]_, _[[items/Wondrous Item/Gloves of Arrow Snaring|gloves of arrow snaring]]_, _[[items/Wondrous Item/Headband of Vast Intelligence +4|headband of vast intelligence +4]]_, _[[items/Ring/Ring of Force Shield|ring of force shield]]_, _[[items/Ring/Ring of Protection +4|ring of protection +4]]_, _[[items/Mundane/Spellbook|spellbook]]_, diamond dust (worth 500 gp), 700 gp

These wizards protect underground communities.
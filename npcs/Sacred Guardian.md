---
cssclass: [monsters]
title1: Sacred Guardian
title2: Sacred Guardian
CR: 13
sources:
- name: NPC Codex
  page: 55
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 25600
race: Gnome
classes:
- cleric of Shelyn 14
alignment: N
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 6
senses:
  low-light vision: true
AC:
  AC: 24
  touch: 16
  flat_footed: 21
  other: +4 dodge vs. giants
  components:
    armor: 7
    deflection: 2
    dex: 2
    dodge: 1
    natural: 1
    size: 1
HP:
  HP: 129
  long: 14d8+63
saves:
  fort: 16
  ref: 9
  will: 18
  other: +2 vs. illusions
immunities:
- fire (120 points)
speeds:
  base: 15
attacks:
  melee:
  - - text: mwk glaive +11/+6 (1d8-1/×3)
      entries:
      - - damage: 1d8-1
          crit_multiplier: 3
      attack: mwk glaive
      bonus:
      - 11
      - 6
  ranged:
  - - text: mwk light crossbow +14 (1d6/19-20)
      entries:
      - - damage: 1d6
          crit_range: 19-20
      attack: mwk light crossbow
      bonus:
      - 14
  special:
  - channel positive energy 5/day (DC 19, 7d6)
  - +1 on attack rolls against goblinoid and reptilian humanoids
spell_like_abilities:
  entries:
  - name: bit of luck
    source: default
    freq: 9/day
  - name: resistant touch
    source: default
    freq: 9/day
  sources:
  - name: default
    CL: 14
    concentration: 20
spells:
  entries:
  - name: destruction
    source: Cleric
    level: 7
    DC: 23
  - is_domain_spell: true
    name: repulsion
    source: Cleric
    level: 7
    DC: 23
  - name: summon monster VII
    source: Cleric
    level: 7
  - name: antilife shell
    source: Cleric
    level: 6
  - is_domain_spell: true
    name: antimagic field
    source: Cleric
    level: 6
  - name: banishment
    source: Cleric
    level: 6
    DC: 22
  - name: blade barrier
    source: Cleric
    level: 6
    DC: 22
  - name: greater dispel magic
    source: Cleric
    level: 6
  - name: breath of life
    source: Cleric
    level: 5
  - name: greater command
    source: Cleric
    level: 5
    DC: 21
  - name: mark of justice
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: spell resistance
    source: Cleric
    level: 5
  - name: wall of stone
    source: Cleric
    level: 5
  - name: air walk
    source: Cleric
    level: 4
  - name: death ward
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: freedom of movement
    source: Cleric
    level: 4
  - name: neutralize poison
    source: Cleric
    level: 4
  - name: order's wrath
    source: Cleric
    level: 4
    DC: 20
  - name: repel vermin
    source: Cleric
    level: 4
  - name: bestow curse
    source: Cleric
    level: 3
    DC: 19
  - name: blindness/deafness
    source: Cleric
    level: 3
    DC: 19
  - name: glyph of warding
    source: Cleric
    level: 3
    count: 2
  - name: invisibility purge
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: protection from energy
    source: Cleric
    level: 3
    DC: 19
  - name: bear's endurance
    source: Cleric
    level: 2
  - name: delay poison
    source: Cleric
    level: 2
    DC: 18
  - name: hold person
    source: Cleric
    level: 2
    count: 2
    DC: 18
  - name: remove paralysis
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: shield other
    source: Cleric
    level: 2
  - name: cause fear
    source: Cleric
    level: 1
    count: 2
    DC: 17
  - name: command
    source: Cleric
    level: 1
    DC: 17
  - name: divine favor
    source: Cleric
    level: 1
  - name: entropic shield
    source: Cleric
    level: 1
  - name: sanctuary
    source: Cleric
    level: 1
    DC: 17
  - is_domain_spell: true
    name: true strike
    source: Cleric
    level: 1
  - name: create water
    source: Cleric
    level: 0
  - name: detect poison
    source: Cleric
    level: 0
  - name: mending
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 14
    concentration: 20
    slots:
      0: at-will
    domains:
    - luck
    - protection
tactics:
  Before Combat: The cleric casts air walk, bear's endurance, delay poison, freedom
    of movement, and protection from energy (fire).
  During Combat: The cleric prefers to paralyze, repel, or disable opponents with
    greater command and barrier spells, but reacts aggressively if his opponents won't
    surrender or agree to a truce.
  Base Statistics: Without bear's endurance, the cleric's statistics are hp 101; Fort
    +14; Con 14.
ability_scores:
  STR: 8
  DEX: 14
  CON: 18
  INT: 13
  WIS: 22
  CHA: 10
BAB: 10
CMB: 8
CMD: 23
feats:
- name: Combat Casting
- name: Dodge
- name: Extra Channel
- name: Improved Channel
- name: Improved Initiative
- name: Selective Channeling
- name: Turn Undead
skills:
  Craft (armor): 3
  Craft (jewelry): 6
  Diplomacy: 9
  Heal: 15
  Knowledge (arcana): 6
  Knowledge (history): 6
  Knowledge (nobility): 6
  Knowledge (local): 3
  Knowledge (religion): 10
  Perception: 22
  Sense Motive: 12
  Spellcraft: 8
languages:
- Common
- Gnome
- Sylvan
special_qualities:
- aura
- aura of protection (+2 deflection, energy resistance 10, 14 rounds/day)
- good fortune (2/day)
gear:
  combat:
  - potions of invisibility (2)
  - ring of the ram (10 charges)
  other:
  - +1 light fortification breastplate
  - masterwork glaive
  - masterwork light crossbow with 20 bolts
  - amulet of natural armor +1
  - headband of inspired wisdom +4
  - ring of protection +2
  - platinum holy symbol (worth 500 gp)
  - powdered diamond (worth 200 gp)
  - 787 gp
desc_long: The sacred guardian serves the goddess of beauty and love. He protects
  a holy site, preferring to deflect and warn rather than harm or destroy.

---

# Sacred Guardian

**Source** NPC Codex pg. 55
**XP** 25,600
Gnome _[[classes/Cleric|cleric]]_ of Shelyn 14

N Small humanoid (gnome)
**Init** +6; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +22

##### Defense

**AC** 24, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+7 armor, +2 deflection, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +1 natural, +1 size) (+4 _dodge_ vs. giants)
**hp** 129 (14d8+63)
**Fort** +16, **Ref** +9, **Will** +18; +2 vs. illusions
**Immune** fire (120 points)

##### Offense
**Speed** 15 ft.
**Melee** mwk _[[items/Weapon/Glaive|glaive]]_ +11/+6 (1d8–1/×3)
**Ranged** mwk _[[items/Weapon/Light crossbow|light crossbow]]_ +14 (1d6/19–20)
**Special Attacks** channel positive energy 5/day (DC 19, 7d6), +1 on attack rolls against goblinoid and reptilian humanoids
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +20)
9/day—_[[spells/Bit Of Luck|bit of luck]]_, resistant touch
**_Cleric_ Spells Prepared **(CL 14th; concentration +20)
7th—_[[spells/Destruction|destruction]]_ (DC 23), repulsionD (DC 23), _[[spells/Summon Monster VII|summon monster VII]]_
6th—_[[spells/Antilife Shell|antilife shell]]_, _[[spells/Antimagic Field|antimagic field]]_, _[[spells/Banishment|banishment]]_ (DC 22), _[[spells/Blade Barrier|blade barrier]]_ (DC 22), greater _[[spells/Dispel Magic|dispel magic]]_
5th—_[[spells/Breath Of Life|breath of life]]_, greater _[[spells/Command|command]]_ (DC 21), _[[spells/Mark of Justice|mark of justice]]_, _[[universal monster rules/Spell Resistance|spell resistance]]_, _[[spells/Wall Of Stone|wall of stone]]_
4th—_[[spells/Air Walk|air walk]]_, _[[spells/Death Ward|death ward]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Neutralize Poison|neutralize poison]]_, order’s wrath (DC 20), _[[spells/Repel Vermin|repel vermin]]_
3rd—_[[spells/Bestow Curse|bestow curse]]_ (DC 19), blindness/deafness (DC 19), _[[spells/Glyph Of Warding|glyph of warding]]_ (2), _[[spells/Invisibility Purge|invisibility purge]]_, protection from energyD (DC 19)
2nd—bear’s _[[feats/Endurance|endurance]]_, _[[spells/Delay Poison|delay poison]]_ (DC 18), _[[spells/Hold Person|hold person]]_ (2, DC 18), _[[spells/Remove Paralysis|remove paralysis]]_, _[[spells/Shield Other|shield other]]_
1st—_[[spells/Cause Fear|cause fear]]_ (2, DC 17), _command_ (DC 17), _[[spells/Divine Favor|divine favor]]_, _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 17), _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Mending|mending]]_, _[[spells/Read Magic|read magic]]_
**D **Domain spell; **Domains **Luck, Protection

### Tactics

**Before Combat **The _cleric_ casts _air walk_, bear’s _endurance_, _delay poison_, _freedom of movement_, and _[[spells/Protection from Energy|protection from energy]]_ (fire).
**During Combat **The _cleric_ prefers to paralyze, repel, or disable opponents with greater _command_ and barrier spells, but reacts aggressively if his opponents won’t surrender or agree to a truce.
**Base Statistics **Without bear’s _endurance_, the _cleric_’s statistics are **hp **101; **Fort **+14; **Con **14.

##### Statistics
**Str** 8, **Dex** 14, **Con** 18, **Int** 13, **Wis** 22, **Cha** 10
**Base Atk** +10; **CMB** +8; **CMD** 23
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Improved Channel|Improved Channel]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Selective Channeling|Selective Channeling]]_, _[[feats/Turn Undead|Turn Undead]]_
**Skills** Craft (armor) +3, Craft (_[[items/Mundane/Jewelry|jewelry]]_) +6, Diplomacy +9, _[[spells/Heal|Heal]]_ +15, Knowledge (arcana, history, nobility) +6, Knowledge (local) +3, Knowledge (religion) +10, Perception +22, Sense Motive +12, Spellcraft +8
**Languages** Common, Gnome, Sylvan
**SQ** aura, aura of protection (+2 _deflection_, _[[items/Armor Magic Abilities/Energy Resistance|energy resistance]]_ 10, 14 rounds/day), good fortune (2/day)
**Combat Gear** potions of _[[spells/Invisibility|invisibility]]_ (2), _[[items/Ring/Ring of the Ram|ring of the ram]]_ (10 charges); **Other Gear** +1 light _[[universal monster rules/Fortification|fortification]]_ _[[items/Armor/Breastplate|breastplate]]_, masterwork _glaive_, masterwork _light crossbow_ with 20 bolts, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +4|headband of _inspired_ wisdom +4]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, platinum holy symbol (worth 500 gp), powdered diamond (worth 200 gp), 787 gp

The _[[npcs/Sacred Guardian|sacred guardian]]_ serves the goddess of beauty and love. He protects a holy site, preferring to deflect and warn rather than _[[spells/Harm|harm]]_ or destroy.
---
cssclass: [monsters]
title1: Elemental Priest
title2: Elemental Priest
CR: 15
sources:
- name: NPC Codex
  page: 57
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 51200
race: Halfling
classes:
- cleric of Gozreh 16
alignment: CN
size: Small
type: humanoid
subtypes:
- halfling
initiative:
  bonus: 4
AC:
  AC: 21
  touch: 12
  flat_footed: 21
  components:
    armor: 7
    deflection: 1
    natural: 2
    size: 1
HP:
  HP: 155
  long: 16d8+80
saves:
  fort: 17
  ref: 10
  will: 20
  other: +2 vs. fear
immunities:
- fire (120 points)
resistances:
  cold: 20
  electricity: 20
  fire: 30
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk quarterstaff +13/+8/+3 (1d4-1)
      entries:
      - - damage: 1d4-1
      attack: mwk quarterstaff
      bonus:
      - 13
      - 8
      - 3
  ranged:
  - - text: mwk light crossbow +14 (1d6/19-20)
      entries:
      - - damage: 1d6
          crit_range: 19-20
      attack: mwk light crossbow
      bonus:
      - 14
  special:
  - channel negative energy 7/day (DC 20, 8d6)
spell_like_abilities:
  entries:
  - name: icicle
    source: default
    freq: 10/day
    other: 1d6+8 cold damage
  - name: lightning arc
    source: default
    freq: 10/day
    other: 1d6+8 electricity
  sources:
  - name: default
    CL: 16
    concentration: 23
spells:
  entries:
  - is_domain_spell: true
    name: horrid wilting
    source: Cleric
    level: 8
    DC: 25
  - name: summon monster VIII
    source: Cleric
    level: 8
    count: 2
  - is_domain_spell: true
    name: elemental body IV
    source: Cleric
    level: 7
    other: air only
  - name: ethereal jaunt
    source: Cleric
    level: 7
  - name: repulsion
    source: Cleric
    level: 7
    DC: 24
  - name: summon monster VII
    source: Cleric
    level: 7
    count: 2
  - name: banishment
    source: Cleric
    level: 6
    DC: 23
  - is_domain_spell: true
    name: chain lightning
    source: Cleric
    level: 6
    DC: 23
  - name: heal
    source: Cleric
    level: 6
  - name: summon monster VI
    source: Cleric
    level: 6
  - name: word of recall
    source: Cleric
    level: 6
  - name: breath of life
    source: Cleric
    level: 5
  - name: greater command
    source: Cleric
    level: 5
    DC: 22
  - is_domain_spell: true
    name: ice storm
    source: Cleric
    level: 5
  - name: plane shift
    source: Cleric
    level: 5
    DC: 23
  - name: spell resistance
    source: Cleric
    level: 5
  - name: summon monster V
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: air walk
    source: Cleric
    level: 4
  - name: chaos hammer
    source: Cleric
    level: 4
    DC: 21
  - name: dismissal
    source: Cleric
    level: 4
    DC: 21
  - name: freedom of movement
    source: Cleric
    level: 4
  - name: summon monster IV
    source: Cleric
    level: 4
    count: 2
  - name: dispel magic
    source: Cleric
    level: 3
  - name: invisibility purge
    source: Cleric
    level: 3
  - name: prayer
    source: Cleric
    level: 3
  - name: protection from energy
    source: Cleric
    level: 3
    DC: 20
  - name: remove blindness/deafness
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: water breathing
    source: Cleric
    level: 3
  - name: wind wall
    source: Cleric
    level: 3
  - name: bear's endurance
    source: Cleric
    level: 2
  - name: cure moderate wounds
    source: Cleric
    level: 2
  - name: hold person
    source: Cleric
    level: 2
    DC: 19
  - name: resist energy
    source: Cleric
    level: 2
    DC: 19
  - name: shatter
    source: Cleric
    level: 2
  - name: spiritual weapon
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: wind wall
    source: Cleric
    level: 2
  - name: bless
    source: Cleric
    level: 1
  - name: command
    source: Cleric
    level: 1
    count: 2
    DC: 18
  - name: cure light wounds
    source: Cleric
    level: 1
  - name: divine favor
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: obscuring mist
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
  - name: read magic
    source: Cleric
    level: 0
  - name: resistance
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 16
    concentration: 23
    slots:
      0: at-will
    domains:
    - air
    - water
tactics:
  Before Combat: The cleric casts air walk, bear's endurance, freedom of movement,
    protection from energy (fire), and resist energy (fire).
  During Combat: The cleric summons air and water elementals and uses Elemental Channel
    to keep these defenders alive so he can cast attack spells at his opponents.
  Base Statistics: Without bear's endurance, protection from energy, and resist energy,
    the cleric's statistics are hp 123; Fort 15; Immune -; Resist cold 20, electricity
    20; Con 14.
ability_scores:
  STR: 8
  DEX: 10
  CON: 18
  INT: 12
  WIS: 25
  CHA: 15
BAB: 12
CMB: 10
CMD: 21
feats:
- name: Augment Summoning
- name: Combat Casting
- name: Elemental Channel (air)
- name: Elemental Channel (water)
- name: Extra Channel
- name: Improved Initiative
- name: Lightning Reflexes
- name: Spell Focus (conjuration)
skills:
  Acrobatics: 1
    when jumping: -3
  Climb: 0
  Diplomacy: 10
  Knowledge (arcana): 9
  Knowledge (nature): 6
  Knowledge (planes): 14
  Linguistics: 5
  Perception: 19
  Spellcraft: 9
  Stealth: 5
  Swim: 3
languages:
- Aquan
- Auran
- Common
- Halfling
special_qualities:
- aura
gear:
  combat:
  - potions of invisibility (2)
  other:
  - +1 mithral chainmail
  - masterwork light crossbow with 20 bolts
  - masterwork quarterstaff
  - amulet of natural armor +2
  - cloak of resistance +2
  - headband of inspired wisdom +6
  - ring of protection +1
  - forked metal rods (for plane shift)
  - wooden unholy symbol
  - 1,564 gp
desc_long: The elemental priest commands the forces of nature and summons powerful
  air and water spirits to do his bidding.

---

# Elemental Priest

**Source** NPC Codex pg. 57
**XP** 51,200
Halfling _[[classes/Cleric|cleric]]_ of Gozreh 16

CN Small humanoid (halfling)
**Init** +4; **Senses** Perception +19

##### Defense

**AC** 21, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+7 armor, +1 deflection, +2 natural, +1 size)
**hp** 155 (16d8+80)
**Fort** +17, **Ref** +10, **Will** +20; +2 vs. _[[universal monster rules/Fear|fear]]_
**Immune** fire (120 points); **Resist** cold 20, electricity 20, fire 30

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Quarterstaff|quarterstaff]]_ +13/+8/+3 (1d4–1)
**Ranged** mwk _[[items/Weapon/Light crossbow|light crossbow]]_ +14 (1d6/19–20)
**Special Attacks** channel negative energy 7/day (DC 20, 8d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +23)
10/day— icicle (1d6+8 cold damage), _[[spells/Lightning Arc|lightning arc]]_ (1d6+8 electricity)
**_Cleric_ Spells Prepared **(CL 16th; concentration +23)
8th—horrid wiltingD (DC 25), _[[spells/Summon Monster VIII|summon monster VIII]]_ (2)
7th—elemental body IVD (air only), _[[spells/Ethereal Jaunt|ethereal jaunt]]_, _[[spells/Repulsion|repulsion]]_ (DC 24), _[[spells/Summon Monster VII|summon monster VII]]_ (2)
6th—_[[spells/Banishment|banishment]]_ (DC 23), chain lightningD (DC 23), _[[spells/Heal|heal]]_, _[[spells/Summon Monster VI|summon monster VI]]_, _[[spells/Word of Recall|word of recall]]_
5th—_[[spells/Breath Of Life|breath of life]]_, greater _[[spells/Command|command]]_ (DC 22), _[[spells/Ice Storm|ice storm]]_, _[[spells/Plane Shift|plane shift]]_ (DC 23), _[[universal monster rules/Spell Resistance|spell resistance]]_, _[[spells/Summon Monster V|summon monster V]]_
4th—_[[spells/Air Walk|air walk]]_, _[[spells/Chaos Hammer|chaos hammer]]_ (DC 21), _[[spells/Dismissal|dismissal]]_ (DC 21), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Summon Monster IV|summon monster IV]]_ (2)
3rd—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Prayer|prayer]]_, _[[spells/Protection from Energy|protection from energy]]_ (DC 20), remove blindness/deafness, _[[universal monster rules/Water Breathing|water breathing]]_, _[[spells/Wind Wall|wind wall]]_
2nd—bear’s _[[feats/Endurance|endurance]]_, _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Hold Person|hold person]]_ (DC 19), _[[spells/Resist Energy|resist energy]]_ (DC 19), _[[spells/Shatter|shatter]]_, _[[spells/Spiritual Weapon|spiritual weapon]]_, _wind wall_
1st—_[[spells/Bless|bless]]_, _command_ (2, DC 18), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_
**D **Domain spell; **Domains **Air, Water

### Tactics

**Before Combat **The _cleric_ casts _air walk_, bear’s _endurance_, _freedom of movement_, _protection from energy_ (fire), and _resist energy_ (fire).
**During Combat **The _cleric_ summons air and water elementals and uses _[[feats/Elemental Channel|Elemental Channel]]_ to keep these defenders alive so he can cast attack spells at his opponents.
**Base Statistics **Without bear’s _endurance_, _protection from energy_, and _resist energy_, the _cleric_’s statistics are **hp **123; **Fort **15; **Immune **—; **Resist **cold 20, electricity 20; **Con **14.

##### Statistics
**Str** 8, **Dex** 10, **Con** 18, **Int** 12, **Wis** 25, **Cha** 15
**Base Atk** +12; **CMB** +10; **CMD** 21
**Feats** _[[feats/Augment Summoning|Augment Summoning]]_, _[[feats/Combat Casting|Combat Casting]]_, _Elemental Channel_ (air, water), _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Spell Focus|Spell Focus]]_ (conjuration)
**Skills** Acrobatics +1 (–3 when jumping), _[[universal monster rules/Climb|Climb]]_ +0, Diplomacy +10, Knowledge (arcana) +9, Knowledge (nature) +6, Knowledge (planes) +14, Linguistics +5, Perception +19, Spellcraft +9, Stealth +5, Swim +3
**Languages** Aquan, Auran, Common, Halfling
**SQ** aura
**Combat Gear** potions of _[[spells/Invisibility|invisibility]]_ (2); **Other Gear** +1 mithral _[[items/Armor/Chainmail|chainmail]]_, masterwork _light crossbow_ with 20 bolts, masterwork _quarterstaff_, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +6|headband of _inspired_ wisdom +6]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, forked metal rods (for _plane shift_), wooden _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol, 1,564 gp

The _[[npcs/Elemental Priest|elemental priest]]_ commands the forces of nature and summons powerful air and water spirits to do his bidding.
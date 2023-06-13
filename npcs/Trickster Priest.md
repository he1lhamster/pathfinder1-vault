---
cssclass: [monsters]
title1: Trickster Priest
title2: Trickster Priest
CR: 11
sources:
- name: NPC Codex
  page: 53
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 12800
race: Human
classes:
- cleric of Calistria 12
alignment: CN
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 6
AC:
  AC: 26
  touch: 13
  flat_footed: 24
  components:
    armor: 9
    deflection: 1
    dex: 2
    natural: 1
    shield: 3
HP:
  HP: 105
  long: 12d8+24
saves:
  fort: 12
  ref: 9
  will: 14
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk whip +9/+4 (1d3-1 nonlethal)
      entries:
      - - damage: 1d3-1
          type: nonlethal
      attack: mwk whip
      bonus:
      - 9
      - 4
  ranged:
  - - text: mwk heavy crossbow +12 (1d10/19-20)
      entries:
      - - damage: 1d10
          crit_range: 19-20
      attack: mwk heavy crossbow
      bonus:
      - 12
  special:
  - channel negative energy 8/day (DC 21, 6d6)
spell_like_abilities:
  entries:
  - name: charming smile
    source: default
    freq: At will
    other: 12 rounds/day
    DC: 21
  - name: master's illusion
    source: default
    freq: At will
    other: 12 rounds/day
    DC: 21
  - name: copycat
    source: default
    freq: 8/day
    other: 12 rounds
  - name: dazing touch
    source: default
    freq: 8/day
  sources:
  - name: default
    CL: 12
    concentration: 17
spells:
  entries:
  - is_domain_spell: true
    name: geas/quest
    source: Cleric
    level: 6
  - name: greater dispel magic
    source: Cleric
    level: 6
  - name: word of recall
    source: Cleric
    level: 6
  - name: breath of life
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: charm monster
    source: Cleric
    level: 5
    DC: 22
  - name: greater command
    source: Cleric
    level: 5
    DC: 22
  - name: slay living
    source: Cleric
    level: 5
    DC: 20
  - name: spell resistance
    source: Cleric
    level: 5
  - name: chaos hammer
    source: Cleric
    level: 4
    DC: 19
  - name: cure serious wounds
    source: Cleric
    level: 4
  - name: discern lies
    source: Cleric
    level: 4
    DC: 19
  - is_domain_spell: true
    name: heroism
    source: Cleric
    level: 4
  - name: poison
    source: Cleric
    level: 4
    DC: 19
  - name: invisibility purge
    source: Cleric
    level: 3
  - name: magic vestment
    source: Cleric
    level: 3
  - name: prayer
    source: Cleric
    level: 3
  - name: protection from energy
    source: Cleric
    level: 3
    DC: 18
  - name: searing light
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: suggestion
    source: Cleric
    level: 3
    DC: 20
  - name: calm emotions
    source: Cleric
    level: 2
    DC: 19
  - name: delay poison
    source: Cleric
    level: 2
    DC: 17
  - name: enthrall
    source: Cleric
    level: 2
    DC: 19
  - name: hold person
    source: Cleric
    level: 2
    count: 2
    DC: 19
  - is_domain_spell: true
    name: invisibility
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: charm person
    source: Cleric
    level: 1
    DC: 18
  - name: cure light wounds
    source: Cleric
    level: 1
    count: 2
  - name: entropic shield
    source: Cleric
    level: 1
  - name: hide from undead
    source: Cleric
    level: 1
  - name: obscuring mist
    source: Cleric
    level: 1
  - name: remove fear
    source: Cleric
    level: 1
  - name: detect magic
    source: Cleric
    level: 0
  - name: light
    source: Cleric
    level: 0
  - name: mending
    source: Cleric
    level: 0
  - name: purify food and drink
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 12
    concentration: 17
    slots:
      0: at-will
    domains:
    - charm
    - trickery
tactics:
  Before Combat: The cleric uses his wand of bear's endurance, then casts magic vestment.
  During Combat: The cleric uses charm spells, hold spells, and suggestion to disable
    opponents or turn them into allies. He casts heroism and prayer to bolster companions,
    and uses his copycat domain power and spell resistance to protect himself, channeling
    negative energy to harm creatures who resist enchantment.
  Base Statistics: Without bear's endurance and magic vestment, the cleric's statistics
    are AC 24, touch 13, flat-footed 22; hp 81; Fort +10; Con 12.
ability_scores:
  STR: 8
  DEX: 15
  CON: 16
  INT: 10
  WIS: 20
  CHA: 16
BAB: 9
CMB: 8
CMD: 21
feats:
- name: Extra Channel
- name: Greater Spell Focus (enchantment)
- name: Improved Channel
- name: Improved Initiative
- name: Lightning Reflexes
- name: Selective Channeling
- name: Spell Focus (enchantment)
skills:
  Bluff: 11
  Diplomacy: 17
  Heal: 14
  Intimidate: 8
  Perception: 11
  Spellcraft: 6
languages:
- Common
special_qualities:
- aura
gear:
  combat:
  - potion of cure moderate wounds
  - wand of bear's endurance (10 charges)
  other:
  - +1 breastplate
  - +2 light wooden shield
  - masterwork heavy crossbow with 20 bolts
  - masterwork whip
  - amulet of natural armor +1
  - belt of incredible dexterity +2
  - cloak of resistance +1
  - headband of inspired wisdom +2
  - ring of protection +1
  - silver unholy symbol
  - 621 gp
desc_long: The trickster priest serves the goddess of trickery and revenge, using
  guile and magic to manipulate others.

---

# Trickster Priest

**Source** NPC Codex pg. 53
**XP** 12,800
Human _[[classes/Cleric|cleric]]_ of Calistria 12

CN Medium humanoid (human)
**Init** +6; **Senses** Perception +11

##### Defense

**AC** 26, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+9 armor, +1 _[[spells/Deflection|deflection]]_, +2 Dex, +1 natural, +3 _[[spells/Shield|shield]]_)
**hp** 105 (12d8+24)
**Fort** +12, **Ref** +9, **Will** +14

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Whip|whip]]_ +9/+4 (1d3–1 nonlethal)
**Ranged** mwk _[[items/Weapon/Heavy crossbow|heavy crossbow]]_ +12 (1d10/19–20)
**Special Attacks** channel negative energy 8/day (DC 21, 6d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +17)
At will—charming smile (12 rounds/day, DC 21), master’s illusion (12 rounds/day, DC 21)
8/day—copycat (12 rounds), dazing touch
**_Cleric_ Spells Prepared **(CL 12th; concentration +17)
6th—geas/quest, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Word of Recall|word of recall]]_
5th—_[[spells/Breath Of Life|breath of life]]_, _[[spells/Charm Monster|charm monster]]_ (DC 22), greater _[[spells/Command|command]]_ (DC 22), _[[spells/Slay Living|slay living]]_ (DC 20), _[[universal monster rules/Spell Resistance|spell resistance]]_
4th—_[[spells/Chaos Hammer|chaos hammer]]_ (DC 19), _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Discern Lies|discern lies]]_ (DC 19), _[[spells/Heroism|heroism]]_, poison (DC 19)
3rd—_[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Magic Vestment|magic vestment]]_, _[[spells/Prayer|prayer]]_, _[[spells/Protection from Energy|protection from energy]]_ (DC 18), _[[spells/Searing Light|searing light]]_, _[[spells/Suggestion|suggestion]]_ (DC 20)
2nd—_[[spells/Calm Emotions|calm emotions]]_ (DC 19), _[[spells/Delay Poison|delay poison]]_ (DC 17), _[[spells/Enthrall|enthrall]]_ (DC 19), _[[spells/Hold Person|hold person]]_ (2, DC 19), _[[spells/Invisibility|invisibility]]_
1st—_[[spells/Charm Person|charm person]]_ (DC 18), _[[spells/Cure Light Wounds|cure light wounds]]_ (2), _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Hide from Undead|hide from undead]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Remove Fear|remove fear]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mending|mending]]_, _[[spells/Purify Food and Drink|purify food and drink]]_
**D **Domain spell; **Domains **Charm, Trickery

### Tactics

**Before Combat **The _cleric_ uses his wand of bear’s _[[feats/Endurance|endurance]]_, then casts _magic vestment_.
**During Combat **The _cleric_ uses charm spells, hold spells, and _suggestion_ to disable opponents or turn them into allies. He casts _heroism_ and _prayer_ to bolster companions, and uses his copycat domain power and _spell resistance_ to protect himself, _[[items/Armor Magic Abilities/Channeling|channeling]]_ negative energy to _[[spells/Harm|harm]]_ creatures who resist enchantment.
**Base Statistics **Without bear’s _endurance_ and _magic vestment_, the _cleric_’s statistics are **AC **24, touch 13, _flat-footed_ 22; hp 81; Fort +10; Con 12.

##### Statistics
**Str** 8, **Dex** 15, **Con** 16, **Int** 10, **Wis** 20, **Cha** 16
**Base Atk** +9; **CMB** +8; **CMD** 21
**Feats** _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (enchantment), _[[feats/Improved Channel|Improved Channel]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Selective Channeling|Selective Channeling]]_, _[[feats/Spell Focus|Spell Focus]]_ (enchantment)
**Skills** Bluff +11, Diplomacy +17, _[[spells/Heal|Heal]]_ +14, Intimidate +8, Perception +11, Spellcraft +6
**Languages** Common
**SQ** aura
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, wand of bear’s _endurance_ (10 charges); **Other Gear** +1 _[[items/Armor/Breastplate|breastplate]]_, +2 _[[items/Shield/Light wooden shield|light wooden shield]]_, masterwork _heavy crossbow_ with 20 bolts, masterwork _whip_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, silver _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol, 621 gp

The _[[npcs/Trickster Priest|trickster priest]]_ serves the goddess of trickery and revenge, using guile and magic to manipulate others.
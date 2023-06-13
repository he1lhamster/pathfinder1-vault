---
cssclass: [monsters]
title1: Seductive Enchanter
title2: Seductive Enchanter
CR: 7
sources:
- name: NPC Codex
  page: 183
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 3200
race: Elf
classes:
- enchanter 8
alignment: NE
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 7
senses:
  low-light vision: true
AC:
  AC: 19
  touch: 14
  flat_footed: 16
  components:
    armor: 4
    deflection: 1
    dex: 3
    natural: 1
HP:
  HP: 40
  long: 8d6+10
saves:
  fort: 4
  ref: 6
  will: 8
  other: +2 vs. enchantments
immunities:
- sleep
speeds:
  base: 30
attacks:
  melee:
  - - text: rapier +4 (1d6/18-20)
      entries:
      - - damage: 1d6
          crit_range: 18-20
      attack: rapier
      bonus:
      - 4
  ranged:
  - - text: dagger +7 (1d4/19-20)
      entries:
      - - damage: 1d4
          crit_range: 19-20
      attack: dagger
      bonus:
      - 7
  special:
  - aura of despair (8 rounds/day)
spell_like_abilities:
  entries:
  - name: dazing touch
    source: default
    freq: 7/day
  sources:
  - name: default
    CL: 8
    concentration: 12
spells:
  entries:
  - name: confusion
    source: Enchanter
    level: 4
    DC: 19
  - name: dimension door
    source: Enchanter
    level: 4
  - name: greater invisibility
    source: Enchanter
    level: 4
  - name: phantasmal killer
    source: Enchanter
    level: 4
    DC: 18
  - name: deep slumber
    source: Enchanter
    level: 3
    DC: 18
  - name: dispel magic
    source: Enchanter
    level: 3
  - name: hold person
    source: Enchanter
    level: 3
    DC: 18
  - name: phantom steed
    source: Enchanter
    level: 3
  - name: suggestion
    source: Enchanter
    level: 3
    DC: 18
  - name: alter self
    source: Enchanter
    level: 2
  - name: daze monster
    source: Enchanter
    level: 2
    DC: 17
  - name: hideous laughter
    source: Enchanter
    level: 2
    DC: 17
  - name: invisibility
    source: Enchanter
    level: 2
  - name: resist energy
    source: Enchanter
    level: 2
  - name: charm person
    source: Enchanter
    level: 1
    count: 2
    DC: 16
  - name: color spray
    source: Enchanter
    level: 1
    DC: 15
  - name: mage armor
    source: Enchanter
    level: 1
  - name: shield
    source: Enchanter
    level: 1
  - name: ventriloquism
    source: Enchanter
    level: 1
    DC: 15
  - name: daze
    source: Enchanter
    level: 0
    DC: 15
  - name: mage hand
    source: Enchanter
    level: 0
  - name: resistance
    source: Enchanter
    level: 0
  - name: touch of fatigue
    source: Enchanter
    level: 0
    DC: 14
  sources:
  - name: Enchanter
    type: prepared
    CL: 8
    concentration: 12
    slots:
      0: at-will
    opposition_schools:
    - divination
    - necromancy
tactics:
  Before Combat: The wizard casts mage armor.
  During Combat: The wizard uses charm person, confusion, and suggestion to turn opponents
    against each other. By casting greater invisibility on herself, she can remain
    hidden while she manipulates her targets. She uses her wand of touch of idiocy
    against enemy spellcasters.
  Base Statistics: Without mage armor, the wizard's statistics are AC 15, touch 14,
    flat-footed 12.
ability_scores:
  STR: 10
  DEX: 16
  CON: 12
  INT: 18
  WIS: 8
  CHA: 12
BAB: 4
CMB: 4
CMD: 18
feats:
- name: Combat Casting
- name: Craft Wand
- name: Improved Initiative
- name: Iron Will
- name: Scribe Scroll
- name: Spell Focus (enchantment)
skills:
  Acrobatics: 8
  Bluff: 9
  Diplomacy: 6
  Knowledge (arcana): 15
  Knowledge (local): 11
  Knowledge (nobility): 11
  Perception: 9
  Perform (dance): 4
  Sense Motive: 3
  Spellcraft: 15
    identify magic item properties: 17
languages:
- Common
- Draconic
- Elven
- Gnome
- Orc
- Sylvan
special_qualities:
- arcane bond (viper)
- elven magic
- enchanting smile
- weapon familiarity
gear:
  combat:
  - potion of cure moderate wounds
  - potion of invisibility
  - scroll of dispel magic
  - scroll of suggestion
  - wand of charm person (20 charges)
  - wand of fox's cunning (10 charges)
  - wand of touch of idiocy (10 charges)
  other:
  - dagger
  - rapier
  - amulet of natural armor +1
  - cloak of resistance +1
  - ring of protection +1
  - spellbook
  - 303 gp
desc_long: Seductive enchanters use magic so they can enjoy mortal pleasures. This
  usually means influencing people to give them things. These wizards can be found
  anywhere they can get the finer things in life. Many of them become connoisseurs
  of one particular pleasure, going from place to place and scamming people into giving
  them the rarest gems or pieces from master artists, or coercing kisses from the
  most attractive nobles.

---

# Seductive Enchanter

**Source** NPC Codex pg. 183
**XP** 3,200
Elf enchanter 8

NE Medium humanoid (elf)
**Init** +7; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +9

##### Defense

**AC** 19, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+4 armor, +1 _[[spells/Deflection|deflection]]_, +3 Dex, +1 natural)
**hp** 40 (8d6+10)
**Fort** +4, **Ref** +6, **Will** +8; +2 vs. enchantments
**Immune** sleep

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Rapier|rapier]]_ +4 (1d6/18–20)
**Ranged** _[[items/Weapon/Dagger|dagger]]_ +7 (1d4/19–20)
**Special Attacks** aura of despair (8 rounds/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +12)
7/day—dazing touch
**Enchanter Spells Prepared **(CL 8th; concentration +12)
4th—_[[spells/Confusion|confusion]]_ (DC 19), _[[spells/Dimension Door|dimension door]]_, greater _[[spells/Invisibility|invisibility]]_, _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 18)
3rd—_[[spells/Deep Slumber|deep slumber]]_ (DC 18), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Hold Person|hold person]]_ (DC 18), _[[spells/Phantom Steed|phantom steed]]_, _[[spells/Suggestion|suggestion]]_ (DC 18)
2nd—_[[spells/Alter Self|alter self]]_, _[[spells/Daze Monster|daze monster]]_ (DC 17), _[[spells/Hideous Laughter|hideous laughter]]_ (DC 17), _invisibility_, _[[spells/Resist Energy|resist energy]]_
1st—_[[spells/Charm Person|charm person]]_ (2, DC 16), _[[spells/Color Spray|color spray]]_ (DC 15), _[[spells/Mage Armor|mage armor]]_, _[[spells/Shield|shield]]_, _[[spells/Ventriloquism|ventriloquism]]_ (DC 15)
0 (at will)—_[[spells/Daze|daze]]_ (DC 15), _[[spells/Mage Hand|mage hand]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 14)
**Opposition Schools **_[[spells/Divination|divination]]_, necromancy

### Tactics

**Before Combat **The _[[classes/Wizard|wizard]]_ casts _mage armor_.
**During Combat **The _wizard_ uses _charm person_, _confusion_, and _suggestion_ to turn opponents against each other. By casting greater _invisibility_ on herself, she can remain hidden while she manipulates her targets. She uses her wand of _[[spells/Touch of Idiocy|touch of idiocy]]_ against enemy spellcasters.
**Base Statistics **Without _mage armor_, the _wizard_’s statistics are **AC **15, touch 14, _flat-footed_ 12.

##### Statistics
**Str** 10, **Dex** 16, **Con** 12, **Int** 18, **Wis** 8, **Cha** 12
**Base Atk** +4; **CMB** +4; **CMD** 18
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Craft Wand|Craft Wand]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Focus|Spell Focus]]_ (enchantment)
**Skills** Acrobatics +8, Bluff +9, Diplomacy +6, Knowledge (arcana) +15, Knowledge (local, nobility) +11, Perception +9, Perform (dance) +4, Sense Motive +3, Spellcraft +15 (+17 _[[spells/Identify|identify]]_ magic item properties)
**Languages** Common, Draconic, Elven, Gnome, _[[monsters/Orc|Orc]]_, Sylvan
**SQ** arcane bond (viper), elven magic, enchanting smile, weapon familiarity
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, potion of _invisibility_, scroll of _dispel magic_, scroll of _suggestion_, wand of _charm person_ (20 charges), wand of fox’s _[[items/Weapon Magic Abilities/Cunning|cunning]]_ (10 charges), wand of _touch of idiocy_ (10 charges); **Other Gear** _dagger_, _rapier_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Mundane/Spellbook|spellbook]]_, 303 gp

Seductive enchanters use magic so they can enjoy mortal pleasures. This usually means influencing people to give them things. These wizards can be found anywhere they can get the finer things in life. Many of them become connoisseurs of one particular pleasure, going from place to place and scamming people into giving them the rarest gems or pieces from master artists, or coercing kisses from the most attractive nobles.
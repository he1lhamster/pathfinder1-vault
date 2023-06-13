---
cssclass: [monsters]
title1: Celestial Theurge
title2: Celestial Theurge
CR: 8
sources:
- name: NPC Codex
  page: 228
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 4800
race: Human
classes:
- cleric of Sarenrae 3
- sorcerer 4
- mystic theurge 2
alignment: NG
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 0
AC:
  AC: 18
  touch: 10
  flat_footed: 18
  components:
    armor: 7
    natural: 1
HP:
  HP: 69
  long: 3d8+4d6+2d6+31
saves:
  fort: 8
  ref: 4
  will: 11
resistances:
  acid: 5
  cold: 5
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 spear +13 (1d8+7/×3)
      entries:
      - - damage: 1d8+7
          crit_multiplier: 3
      attack: +1 spear
      bonus:
      - 13
  ranged:
  - - text: mwk heavy crossbow +6 (1d10/19-20)
      entries:
      - - damage: 1d10
          crit_range: 19-20
      attack: mwk heavy crossbow
      bonus:
      - 6
  special:
  - channel positive energy 6/day (DC 12 [DC 14 against undead], 2d6)
spell_like_abilities:
  entries:
  - name: heavenly fire
    source: default
    freq: 4/day
    other: 1d4+2
  - name: rebuke death
    source: domain
    freq: 5/day
  - name: touch of glory
    source: domain
    freq: 5/day
  sources:
  - name: default
    CL: 4
    concentration: 5
  - name: domain
    CL: 3
    concentration: 5
spells:
  entries:
  - name: prayer
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: searing light
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: bless weapon
    source: Cleric
    level: 2
  - name: delay poison
    source: Cleric
    level: 2
  - name: remove paralysis
    source: Cleric
    level: 2
  - name: shield other
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: cure light wounds
    source: Cleric
    level: 1
  - name: divine favor
    source: Cleric
    level: 1
    count: 2
  - name: protection from evil
    source: Cleric
    level: 1
  - name: remove fear
    source: Cleric
    level: 1
  - name: create water
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: purify food and drink
    source: Cleric
    level: 0
  - name: stabilize
    source: Cleric
    level: 0
  - name: haste
    source: Sorcerer
    level: 3
  - name: bull's strength
    source: Sorcerer
    level: 2
  - name: protection from arrows
    source: Sorcerer
    level: 2
  - name: bless
    source: Sorcerer
    level: 1
  - name: burning hands
    source: Sorcerer
    level: 1
    DC: 12
  - name: enlarge person
    source: Sorcerer
    level: 1
  - name: shield
    source: Sorcerer
    level: 1
  - name: true strike
    source: Sorcerer
    level: 1
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: detect poison
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: mending
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 5
    concentration: 7
    slots:
      0: at-will
    domains:
    - glory
    - healing
  - name: Sorcerer
    type: known
    CL: 6
    concentration: 7
    failure_chance: 25%
    slots:
      3: 3
      2: 5
      1: 7
      0: at-will
    bloodline: celestial
tactics:
  Before Combat: The mystic theurge casts bull's strength.
  During Combat: The mystic theurge casts haste and shield, then supports her companions
    with spells. She targets undead with channeled energy and searing light.
  Base Statistics: Without bull's strength, the mystic theurge's statistics are Melee
    +1 spear +11 (1d8+5/×3); Str 18; CMB +9; CMD 19.
ability_scores:
  STR: 22
  DEX: 10
  CON: 14
  INT: 8
  WIS: 14
  CHA: 12
BAB: 5
CMB: 11
CMD: 21
feats:
- name: Arcane Armor Mastery
- name: Arcane Armor Training
- name: Combat Casting
- name: Eschew Materials
- name: Extra Channel
- name: Toughness
- name: Weapon Focus (spear)
skills:
  Diplomacy: 7
  Knowledge (arcana): 5
  Knowledge (religion): 5
  Knowledge (nobility): 4
  Perception: 8
  Spellcraft: 3
languages:
- Common
special_qualities:
- aura
- bloodline arcana (summoned creatures gain DR 2/evil)
- combined spells (1st)
gear:
  combat:
  - +1 bolts (3)
  - +1 evil outsider-bane bolts (3)
  - +1 undead-bane bolts (3)
  - scrolls of cure serious wounds (2)
  - scrolls of neutralize poison (2)
  - scroll of remove disease
  - antitoxin (2)
  - holy water (2)
  other:
  - +1 breastplate
  - +1 spear
  - masterwork heavy crossbow with 10 bolts
  - amulet of natural armor +1
  - cloak of resistance +1
  - pair of platinum rings (worth 50 gp)
  - 287 gp
desc_long: These theurges support righteous causes, especially ones that involve destroying
  undead.

---

# Celestial Theurge

**Source** NPC Codex pg. 228
**XP** 4,800
Human _[[classes/Cleric|cleric]]_ of Sarenrae 3/sorcerer 4/mystic theurge 2

NG Medium humanoid (human)
**Init** +0; **Senses** Perception +8

##### Defense

**AC** 18, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+7 armor, +1 natural)
**hp** 69 (3d8+4d6+2d6+31)
**Fort** +8, **Ref** +4, **Will** +11
**Resist** acid 5, cold 5

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Spear|spear]]_ +13 (1d8+7/×3)
**Ranged** mwk _[[items/Weapon/Heavy crossbow|heavy crossbow]]_ +6 (1d10/19–20)
**Special Attacks** channel positive energy 6/day (DC 12 [DC 14 against undead], 2d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +5)
4/day—heavenly fire (1d4+2)
**Domain _Spell-Like Abilities_** (CL 3rd; concentration +5)
5/day—_[[spells/Rebuke|rebuke]]_ death, touch of glory
**_Cleric_ Spells Prepared **(CL 5th; concentration +7)
3rd—_[[spells/Prayer|prayer]]_, _[[spells/Searing Light|searing light]]_
2nd—_[[spells/Bless Weapon|bless weapon]]_, _[[spells/Delay Poison|delay poison]]_, _[[spells/Remove Paralysis|remove paralysis]]_, _[[spells/Shield Other|shield other]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Divine Favor|divine favor]]_ (2), _[[spells/Protection From Evil|protection from evil]]_, _[[spells/Remove Fear|remove fear]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Guidance|guidance]]_, _[[spells/Purify Food and Drink|purify food and drink]]_, stabilize
**D **Domain spell; **Domains **Glory, Healing
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 6th; concentration +7; 25% spell failure)
3rd (3/day)—_[[spells/Haste|haste]]_
2nd (5/day)—bull’s strength, _[[spells/Protection From Arrows|protection from arrows]]_
1st (7/day)—_[[spells/Bless|bless]]_, _[[spells/Burning Hands|burning hands]]_ (DC 12), _[[spells/Enlarge Person|enlarge person]]_, _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Message|message]]_, _[[spells/Read Magic|read magic]]_
**Bloodline **celestial

### Tactics

**Before Combat **The mystic theurge casts bull’s strength.
**During Combat **The mystic theurge casts _haste_ and _shield_, then supports her companions with spells. She targets undead with channeled energy and _searing light_.
**Base Statistics **Without bull’s strength, the mystic theurge’s statistics are **Melee** +1 _spear_ +11 (1d8+5/×3); **Str **18; **CMB **+9; **CMD **19.

##### Statistics
**Str** 22, **Dex** 10, **Con** 14, **Int** 8, **Wis** 14, **Cha** 12
**Base Atk** +5; **CMB** +11; **CMD** 21
**Feats** _[[feats/Arcane Armor Mastery|Arcane Armor Mastery]]_, _[[feats/Arcane Armor Training|Arcane Armor Training]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_spear_)
**Skills** Diplomacy +7, Knowledge (arcana, religion) +5, Knowledge (nobility) +4, Perception +8, Spellcraft +3
**Languages** Common
**SQ** aura, bloodline arcana (summoned creatures gain DR 2/evil), combined spells (1st)
**Combat Gear** +1 bolts (3), +1 evil outsider-bane bolts (3), +1 undead-bane bolts (3), scrolls of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), scrolls of _[[spells/Neutralize Poison|neutralize poison]]_ (2), scroll of _[[spells/Remove Disease|remove disease]]_, _[[items/Mundane/Antitoxin|antitoxin]]_ (2), _[[items/Mundane/Holy water|holy water]]_ (2); **Other Gear** +1 _[[items/Armor/Breastplate|breastplate]]_, +1 _spear_, masterwork _heavy crossbow_ with 10 bolts, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, pair of platinum rings (worth 50 gp), 287 gp

These theurges support _[[items/Armor Magic Abilities/Righteous|righteous]]_ causes, especially ones that involve destroying undead.
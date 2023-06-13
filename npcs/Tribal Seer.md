---
cssclass: [monsters]
title1: Tribal Seer
title2: Tribal Seer
CR: 5
sources:
- name: NPC Codex
  page: 181
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 1600
race: Half-orc
classes:
- diviner 6
alignment: N
size: Medium
type: humanoid
subtypes:
- human
- orc
initiative:
  bonus: 8
senses:
  darkvision: 60
  see invisibility: true
AC:
  AC: 16
  touch: 12
  flat_footed: 15
  components:
    armor: 4
    deflection: 1
    dex: 1
HP:
  HP: 41
  long: 6d6+18
saves:
  fort: 5
  ref: 4
  will: 7
defensive_abilities:
- orc ferocity
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk falchion +3 (2d4-1/18-20)
      entries:
      - - damage: 2d4-1
          crit_range: 18-20
      attack: mwk falchion
      bonus:
      - 3
  ranged:
  - - text: light crossbow +4 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 4
spell_like_abilities:
  entries:
  - name: diviner's fortune
    source: default
    freq: 7/day
    other: '+3'
  sources:
  - name: default
    CL: 6
    concentration: 10
spells:
  entries:
  - name: clairaudience/clairvoyance
    source: Diviner
    level: 3
  - name: deep slumber
    source: Diviner
    level: 3
    DC: 18
  - name: haste
    source: Diviner
    level: 3
    DC: 17
  - name: hold person
    source: Diviner
    level: 3
    DC: 18
  - name: flaming sphere
    source: Diviner
    level: 2
    DC: 16
  - name: fox's cunning
    source: Diviner
    level: 2
  - name: pyrotechnics
    source: Diviner
    level: 2
    DC: 16
  - name: see invisibility
    source: Diviner
    level: 2
  - name: touch of idiocy
    source: Diviner
    level: 2
  - name: charm person
    source: Diviner
    level: 1
    DC: 16
  - name: detect undead
    source: Diviner
    level: 1
  - name: mage armor
    source: Diviner
    level: 1
  - name: magic missile
    source: Diviner
    level: 1
  - name: shield
    source: Diviner
    level: 1
  - name: dancing lights
    source: Diviner
    level: 0
  - name: detect magic
    source: Diviner
    level: 0
  - name: detect poison
    source: Diviner
    level: 0
  - name: message
    source: Diviner
    level: 0
  sources:
  - name: Diviner
    type: prepared
    CL: 6
    concentration: 10
    slots:
      0: at-will
    opposition_schools:
    - illusion
    - necromancy
tactics:
  Before Combat: The wizard casts mage armor and see invisibility. If she has a few
    rounds to prepare, she casts fox's cunning on herself and uses her wand of enlarge
    person on her allies.
  During Combat: The wizard casts haste on her allies, hold person on her most dangerous
    opponent, and touch of idiocy on a spellcaster.
  Base Statistics: Without mage armor, the wizard's statistics are AC 12, touch 12,
    flat-footed 11.
ability_scores:
  STR: 8
  DEX: 12
  CON: 14
  INT: 18
  WIS: 13
  CHA: 10
BAB: 3
CMB: 2
CMD: 14
feats:
- name: Brew Potion
- name: Combat Casting
- name: Improved Initiative
- name: Scribe Scroll
- name: Spell Focus (enchantment)
skills:
  Diplomacy: 3
  Heal: 5
  Intimidate: 6
  Knowledge (arcana): 11
  Knowledge (geography): 8
  Knowledge (history): 8
  Knowledge (local): 8
  Knowledge (nature): 8
  Knowledge (religion): 9
  Perception: 7
  Sense Motive: 3
  Spellcraft: 12
  Survival: 3
languages:
- Auran
- Common
- Draconic
- Dwarven
- Giant
- Orc
special_qualities:
- arcane bond (falchion)
- forewarned
- orc blood
- weapon familiarity
gear:
  combat:
  - potions of cat's grace (2)
  - potions of cure light wounds (2)
  - potion of cure moderate wounds
  - potion of protection from arrows
  - scroll of comprehend languages
  - scrolls of mage armor (2)
  - scroll of mount
  - wand of enlarge person (20 charges)
  other:
  - light crossbow with 20 bolts
  - masterwork falchion
  - cloak of resistance +1
  - ring of protection +1
  - spellbook
  - 239 gp
desc_long: The tribal seer speaks to hostile spirits and interprets omens that affect
  her tribe.

---

# Tribal Seer

**Source** NPC Codex pg. 181
**XP** 1,600
Half-orc diviner 6

N Medium humanoid (human, _[[monsters/Orc|orc]]_)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/See Invisibility|see invisibility]]_; Perception +7

##### Defense

**AC** 16, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 armor, +1 _[[spells/Deflection|deflection]]_, +1 Dex)
**hp** 41 (6d6+18)
**Fort** +5, **Ref** +4, **Will** +7
**Defensive Abilities** _orc_ _[[universal monster rules/Ferocity|ferocity]]_

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Falchion|falchion]]_ +3 (2d4–1/18–20)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +4 (1d8/19–20)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +10)
7/day—diviner's fortune (+3)
**Diviner Spells Prepared **(CL 6th; concentration +10)
3rd—clairaudience/clairvoyance, _[[spells/Deep Slumber|deep slumber]]_ (DC 18), _[[spells/Haste|haste]]_ (DC 17), _[[spells/Hold Person|hold person]]_ (DC 18)
2nd—_[[spells/Flaming Sphere|flaming sphere]]_ (DC 16), fox’s _[[items/Weapon Magic Abilities/Cunning|cunning]]_, _[[spells/Pyrotechnics|pyrotechnics]]_ (DC 16), _see invisibility_, _[[spells/Touch of Idiocy|touch of idiocy]]_
1st—_[[spells/Charm Person|charm person]]_ (DC 16), _[[spells/Detect Undead|detect undead]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Shield|shield]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Message|message]]_
**Opposition Schools **illusion, necromancy

### Tactics

**Before Combat **The _[[classes/Wizard|wizard]]_ casts _mage armor_ and _see invisibility_. If she has a few rounds to prepare, she casts fox’s _cunning_ on herself and uses her wand of _[[spells/Enlarge Person|enlarge person]]_ on her allies.
**During Combat **The _wizard_ casts _haste_ on her allies, _hold person_ on her most dangerous opponent, and _touch of idiocy_ on a spellcaster.
**Base Statistics **Without _mage armor_, the _wizard_’s statistics are **AC **12, touch 12, _flat-footed_ 11.

##### Statistics
**Str** 8, **Dex** 12, **Con** 14, **Int** 18, **Wis** 13, **Cha** 10
**Base Atk** +3; **CMB** +2; **CMD** 14
**Feats** _[[feats/Brew Potion|Brew Potion]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Focus|Spell Focus]]_ (enchantment)
**Skills** Diplomacy +3, _[[spells/Heal|Heal]]_ +5, Intimidate +6, Knowledge (arcana) +11, Knowledge (geography, history, local, nature) +8, Knowledge (religion) +9, Perception +7, Sense Motive +3, Spellcraft +12, Survival +3
**Languages** Auran, Common, Draconic, Dwarven, Giant, _Orc_
**SQ** arcane bond (_falchion_), forewarned, _orc_ blood, weapon familiarity
**Combat Gear** potions of cat’s _[[spells/Grace|grace]]_ (2), potions of _[[spells/Cure Light Wounds|cure light wounds]]_ (2), potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, potion of _[[spells/Protection From Arrows|protection from arrows]]_, scroll of _[[spells/Comprehend Languages|comprehend languages]]_, scrolls of _mage armor_ (2), scroll of _[[spells/Mount|mount]]_, wand of _enlarge person_ (20 charges); **Other Gear** _light crossbow_ with 20 bolts, masterwork _falchion_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Mundane/Spellbook|spellbook]]_, 239 gp

The _[[npcs/Tribal Seer|tribal seer]]_ speaks to hostile spirits and interprets omens that affect her tribe.
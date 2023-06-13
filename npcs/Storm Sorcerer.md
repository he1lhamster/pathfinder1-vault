---
cssclass: [monsters]
title1: Storm Sorcerer
title2: Storm Sorcerer
CR: 5
sources:
- name: NPC Codex
  page: 163
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 1600
race: Elf
classes:
- sorcerer 6
alignment: NE
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 6
senses:
  low-light vision: true
AC:
  AC: 18
  touch: 14
  flat_footed: 15
  components:
    armor: 4
    deflection: 1
    dex: 2
    dodge: 1
HP:
  HP: 35
  long: 6d6+12
saves:
  fort: 4
  ref: 5
  will: 7
  other: +2 vs. enchantments
immunities:
- sleep
resistances:
  electricity: 10
speeds:
  base: 30
attacks:
  melee:
  - - text: spear +2 (1d8-1/×3)
      entries:
      - - damage: 1d8-1
          crit_multiplier: 3
      attack: spear
      bonus:
      - 2
  ranged:
  - - text: mwk longbow +6 (1d8/×3)
      entries:
      - - damage: 1d8
          crit_multiplier: 3
      attack: mwk longbow
      bonus:
      - 6
spell_like_abilities:
  entries:
  - name: elemental ray
    source: default
    freq: 6/day
    other: 1d6+3 electricity
  sources:
  - name: default
    CL: 6
    concentration: 9
spells:
  entries:
  - name: lightning bolt
    source: Sorcerer
    level: 3
    DC: 17
  - name: gust of wind
    source: Sorcerer
    level: 2
    DC: 16
  - name: scorching ray
    source: Sorcerer
    level: 2
    other: electricity
  - name: spectral hand
    source: Sorcerer
    level: 2
  - name: burning hands
    source: Sorcerer
    level: 1
    other: electricity
    DC: 15
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: obscuring mist
    source: Sorcerer
    level: 1
  - name: shocking grasp
    source: Sorcerer
    level: 1
  - name: acid splash
    source: Sorcerer
    level: 0
    other: electricity
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: light
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: ray of frost
    source: Sorcerer
    level: 0
    other: electricity
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 6
    concentration: 9
    slots:
      3: 4
      2: 6
      1: 7
      0: at-will
    bloodline: elemental (air)
tactics:
  Before Combat: The sorcerer casts mage armor.
  During Combat: The sorcerer favors his electricity spells, casting lightning bolt
    or scorching ray, or using his spectral hand to deliver shocking grasp attacks.
    He prefers ranged combat, using a scroll of fly or levitate to avoid opponents
    on the ground.
  Base Statistics: Without mage armor, the sorcerer's base statistics are AC 14, touch
    14, flat-footed 11.
ability_scores:
  STR: 8
  DEX: 15
  CON: 12
  INT: 12
  WIS: 12
  CHA: 16
BAB: 3
CMB: 2
CMD: 16
feats:
- name: Dodge
- name: Eschew Materials
- name: Improved Initiative
- name: Spell Focus (evocation)
skills:
  Fly: 10
  Knowledge (arcana): 9
  Linguistics: 2
  Perception: 4
  Spellcraft: 10
    to identify magic item properties: 12
languages:
- Auran
- Common
- Draconic
- Elven
special_qualities:
- bloodline arcana (change energy damage spells to electricity)
- elven magic
- weapon familiarity
gear:
  combat:
  - scroll of fly
  - scroll of gaseous form
  - scroll of levitate
  other:
  - masterwork longbow with 20 arrows
  - spear
  - cloak of resistance +1
  - ring of protection +1
desc_long: The storm sorcerer battles his enemies with wind and lightning, reveling
  in nature's destructive power.

---

# Storm Sorcerer

**Source** NPC Codex pg. 163
**XP** 1,600
Elf _[[classes/Sorcerer|sorcerer]]_ 6

NE Medium humanoid (elf)
**Init** +6; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +4

##### Defense

**AC** 18, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 armor, +1 _[[spells/Deflection|deflection]]_, +2 Dex, +1 _[[feats/Dodge|dodge]]_)
**hp** 35 (6d6+12)
**Fort** +4, **Ref** +5, **Will** +7; +2 vs. enchantments
**Immune** sleep; **Resist** electricity 10

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Spear|spear]]_ +2 (1d8–1/×3)
**Ranged** mwk _[[items/Weapon/Longbow|longbow]]_ +6 (1d8/×3)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +9)
6/day—elemental ray (1d6+3 electricity)
**_Sorcerer_ Spells Known **(CL 6th; concentration +9)
3rd (4/day)—_[[spells/Lightning Bolt|lightning bolt]]_ (DC 17)
2nd (6/day)—_[[spells/Gust Of Wind|gust of wind]]_ (DC 16), _[[spells/Scorching Ray|scorching ray]]_ (electricity), _[[spells/Spectral Hand|spectral hand]]_
1st (7/day)—_[[spells/Burning Hands|burning hands]]_ (electricity; DC 15), _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shocking Grasp|shocking grasp]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_ (electricity), _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Ray of Frost|ray of frost]]_ (electricity), _[[spells/Read Magic|read magic]]_
**Bloodline **elemental (air)

### Tactics

**Before Combat **The _sorcerer_ casts _mage armor_.
**During Combat **The _sorcerer_ favors his electricity spells, casting _lightning bolt_ or _scorching ray_, or using his _spectral hand_ to deliver _shocking grasp_ attacks. He prefers ranged combat, using a scroll of fly or _[[spells/Levitate|levitate]]_ to avoid opponents on the ground.
**Base Statistics **Without _mage armor_, the _sorcerer_’s base statistics are **AC **14, touch 14, _flat-footed_ 11.

##### Statistics
**Str** 8, **Dex** 15, **Con** 12, **Int** 12, **Wis** 12, **Cha** 16
**Base Atk** +3; **CMB** +2; **CMD** 16
**Feats** _Dodge_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation)
**Skills** Fly +10, Knowledge (arcana) +9, Linguistics +2, Perception +4, Spellcraft +10 (+12 to _[[spells/Identify|identify]]_ magic item properties)
**Languages** Auran, Common, Draconic, Elven
**SQ** bloodline arcana (change energy damage spells to electricity), elven magic, weapon familiarity
**Combat Gear** scroll of fly, scroll of _[[spells/Gaseous Form|gaseous form]]_, scroll of _levitate_; **Other Gear** masterwork _longbow_ with 20 arrows, _spear_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_

The _[[npcs/Storm Sorcerer|storm sorcerer]]_ battles his enemies with wind and lightning, reveling in nature’s destructive power.
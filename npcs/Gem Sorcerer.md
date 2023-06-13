---
cssclass: [monsters]
title1: Gem Sorcerer
title2: Gem Sorcerer
CR: 1
sources:
- name: NPC Codex
  page: 160
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 400
race: Dwarf
classes:
- sorcerer 2
alignment: LE
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 0
senses:
  darkvision: 60
AC:
  AC: 12
  touch: 10
  flat_footed: 12
  components:
    armor: 2
HP:
  HP: 18
  long: 2d6+9
saves:
  fort: 2
  ref: 0
  will: 3
  other: +2 vs. poison, spells, and spell-like abilities
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
speeds:
  base: 20
attacks:
  melee:
  - - text: spiked gauntlet +3 (1d4+2)
      entries:
      - - damage: 1d4+2
      attack: spiked gauntlet
      bonus:
      - 3
  - - text: heavy mace +3 (1d8+2)
      entries:
      - - damage: 1d8+2
      attack: heavy mace
      bonus:
      - 3
  ranged:
  - - text: mwk heavy crossbow +2 (1d10/19-20)
      entries:
      - - damage: 1d10
          crit_range: 19-20
      attack: mwk heavy crossbow
      bonus:
      - 2
  special:
  - +1 on attack rolls vs. goblinoid and orc humanoids
spell_like_abilities:
  entries:
  - name: elemental ray
    source: default
    freq: 4/day
    other: 1d6+1 fire
  sources:
  - name: default
    CL: 2
    concentration: 3
spells:
  entries:
  - name: burning hands
    source: Sorcerer
    level: 1
    DC: 12
  - name: shocking grasp
    source: Sorcerer
    level: 1
    other: fire
  - name: acid splash
    source: Sorcerer
    level: 0
    other: fire
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: mending
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: touch of fatigue
    source: Sorcerer
    level: 0
    DC: 11
  sources:
  - name: Sorcerer
    type: known
    CL: 2
    concentration: 3
    failure_chance: 10%
    slots:
      1: 5
      0: at-will
    bloodline: elemental (fire)
tactics:
  During Combat: The sorcerer uses burning hands and shocking grasp to scorch his
    foes.
ability_scores:
  STR: 14
  DEX: 10
  CON: 15
  INT: 12
  WIS: 10
  CHA: 13
BAB: 1
CMB: 3
CMD: 13
CMD_other: 17 vs. bull rush or trip
feats:
- name: Eschew Materials
- name: Toughness
skills:
  Appraise: 5
    to assess metals or gemstones: 7
  Craft (jewelry): 5
  Perception: 2
    to notice unusual stonework: 4
  Spellcraft: 5
  Use Magic Device: 5
languages:
- Common
- Dwarven
- Giant
special_qualities:
- bloodline arcana (change energy damage spells to fire)
gear:
  combat:
  - potion of cure light wounds
  - scroll of flaming sphere
  - acid (2)
  - alchemist's fire (3)
  other:
  - leather armor
  - heavy mace
  - masterwork heavy crossbow with 20 bolts
  - spiked gauntlet
  - uncut gems (worth 100 gp)
  - 23 gp
desc_long: The gem sorcerer is unusual among dwarves, using arcane magic to satisfy
  his insatiable greed for gems.

---

# Gem Sorcerer

**Source** NPC Codex pg. 160
**XP** 400
Dwarf _[[classes/Sorcerer|sorcerer]]_ 2

LE Medium humanoid (dwarf)
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +2

##### Defense

**AC** 12, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+2 armor)
**hp** 18 (2d6+9)
**Fort** +2, **Ref** +0, **Will** +3; +2 vs. poison, spells, and _[[universal monster rules/Spell-Like Abilities|spell-like abilities]]_
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _[[feats/Dodge|dodge]]_ bonus to AC vs. giants)

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Spiked gauntlet|spiked gauntlet]]_ +3 (1d4+2) or _[[items/Weapon/Heavy mace|heavy mace]]_ +3 (1d8+2)
**Ranged** mwk _[[items/Weapon/Heavy crossbow|heavy crossbow]]_ +2 (1d10/19–20)
**Special Attacks** +1 on attack rolls vs. goblinoid and _[[monsters/Orc|orc]]_ humanoids
**_Spell-Like Abilities_** (CL 2nd; concentration +3)
4/day—elemental ray (1d6+1 fire)
**_Sorcerer_ Spells Known **(CL 2nd; concentration +3; arcane spell failure 10%)
1st (5/day)—_[[spells/Burning Hands|burning hands]]_ (DC 12), _[[spells/Shocking Grasp|shocking grasp]]_ (fire)
0 (at will)—_[[spells/Acid Splash|acid splash]]_ (fire), _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Mending|mending]]_, _[[spells/Read Magic|read magic]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 11)
**Bloodline **elemental (fire)

### Tactics

**During Combat **The _sorcerer_ uses _burning hands_ and _shocking grasp_ to scorch his foes.

##### Statistics
**Str** 14, **Dex** 10, **Con** 15, **Int** 12, **Wis** 10, **Cha** 13
**Base Atk** +1; **CMB** +3; **CMD** 13 (17 vs. bull rush or _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Toughness|Toughness]]_
**Skills** Appraise +5 (+7 to assess metals or gemstones), Craft (_[[items/Mundane/Jewelry|jewelry]]_) +5, Perception +2 (+4 to notice unusual stonework), Spellcraft +5, Use Magic Device +5
**Languages** Common, Dwarven, Giant
**SQ** bloodline arcana (change energy damage spells to fire)
**Combat Gear** potion of _[[spells/Cure Light Wounds|cure light wounds]]_, scroll of _[[spells/Flaming Sphere|flaming sphere]]_, acid (2), _[[classes/Alchemist|alchemist]]_’s fire (3); **Other Gear** _[[items/Armor/Leather armor|leather armor]]_, _heavy mace_, masterwork _heavy crossbow_ with 20 bolts, _spiked gauntlet_, uncut gems (worth 100 gp), 23 gp

The _[[npcs/Gem Sorcerer|gem sorcerer]]_ is unusual among dwarves, using arcane magic to satisfy his insatiable greed for gems.
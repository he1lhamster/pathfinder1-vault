---
cssclass: [monsters]
title1: Whiteclaw Sorcerer
title2: Whiteclaw Sorcerer
CR: 2
sources:
- name: NPC Codex
  page: 161
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 600
race: Elf
classes:
- sorcerer 3
alignment: NE
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 2
senses:
  low-light vision: true
AC:
  AC: 17
  touch: 12
  flat_footed: 15
  components:
    armor: 4
    dex: 2
    natural: 1
HP:
  HP: 19
  long: 3d6+6
saves:
  fort: 2
  ref: 5
  will: 2
  other: +2 vs. enchantments
immunities:
- sleep
resistances:
  cold: 5
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 claws +1 (1d4)
      entries:
      - - damage: 1d4
      count: 2
      attack: claws
      bonus:
      - 1
  - - text: mwk longsword +2 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: mwk longsword
      bonus:
      - 2
  ranged:
  - - text: longbow +3 (1d8/×3)
      entries:
      - - damage: 1d8
          crit_multiplier: 3
      attack: longbow
      bonus:
      - 3
  special:
  - claws (2, 1d4, 5 rounds/day)
spells:
  entries:
  - name: cause fear
    source: Sorcerer
    level: 1
    DC: 13
  - name: endure elements
    source: Sorcerer
    level: 1
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: bleed
    source: Sorcerer
    level: 0
    DC: 12
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: light
    source: Sorcerer
    level: 0
  - name: ray of frost
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 3
    concentration: 5
    slots:
      1: 6
      0: at-will
    bloodline: draconic (white)
tactics:
  Before Combat: The sorcerer casts mage armor.
  During Combat: The sorcerer casts cause fear at any dangerous-looking opponent,
    then casts magic missile at her foes. When her spells are exhausted, she casts
    bull's strength from a scroll and attacks with her claws or longsword.
  Base Statistics: Without mage armor, the sorcerer's statistics are AC 13, touch
    12, flat-footed 11.
ability_scores:
  STR: 10
  DEX: 14
  CON: 12
  INT: 15
  WIS: 8
  CHA: 15
BAB: 1
CMB: 1
CMD: 13
feats:
- name: Combat Casting
- name: Eschew Materials
- name: Lightning Reflexes
skills:
  Intimidate: 8
  Knowledge (arcana): 8
  Perception: 7
  Spellcraft: 8
    to identify magic item properties: 10
languages:
- Common
- Draconic
- Elven
- Goblin
special_qualities:
- bloodline arcana (cold spells deal +1 damage per die)
- elven magic
- weapon familiarity
gear:
  combat:
  - potion of cure light wounds
  - potion of fly
  - scrolls of bull's strength (2)
  - scroll of fog cloud
  other:
  - longbow with 20 arrows
  - masterwork longsword
  - 10 gp
desc_long: The whiteclaw sorcerer revels in her draconic blood, using her powers to
  terrify and kill enemies in her territory.

---

# Whiteclaw Sorcerer

**Source** NPC Codex pg. 161
**XP** 600
Elf _[[classes/Sorcerer|sorcerer]]_ 3

NE Medium humanoid (elf)
**Init** +2; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +7

##### Defense

**AC** 17, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 armor, +2 Dex, +1 natural)
**hp** 19 (3d6+6)
**Fort** +2, **Ref** +5, **Will** +2; +2 vs. enchantments
**Immune** sleep; **Resist** cold 5

##### Offense
**Speed** 30 ft.
**Melee** 2 claws +1 (1d4) or mwk _[[items/Weapon/Longsword|longsword]]_ +2 (1d8/19–20)
**Ranged** _[[items/Weapon/Longbow|longbow]]_ +3 (1d8/×3)
**Special Attacks** claws (2, 1d4, 5 rounds/day)
**_Sorcerer_ Spells Known **(CL 3rd; concentration +5)
1st (6/day)—_[[spells/Cause Fear|cause fear]]_ (DC 13), _[[spells/Endure Elements|endure elements]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 12), _[[spells/Detect Magic|detect magic]]_, light, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_
**Bloodline **draconic (white)

### Tactics

**Before Combat **The _sorcerer_ casts _mage armor_.
**During Combat **The _sorcerer_ casts _cause fear_ at any dangerous-looking opponent, then casts _magic missile_ at her foes. When her spells are _[[conditions/Exhausted|exhausted]]_, she casts bull’s strength from a scroll and attacks with her claws or _longsword_.
**Base Statistics **Without _mage armor_, the _sorcerer_’s statistics are **AC **13, touch 12, _flat-footed_ 11.

##### Statistics
**Str** 10, **Dex** 14, **Con** 12, **Int** 15, **Wis** 8, **Cha** 15
**Base Atk** +1; **CMB** +1; **CMD** 13
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Intimidate +8, Knowledge (arcana) +8, Perception +7, Spellcraft +8 (+10 to _[[spells/Identify|identify]]_ magic item properties)
**Languages** Common, Draconic, Elven, _[[monsters/Goblin|Goblin]]_
**SQ** bloodline arcana (cold spells deal +1 damage per die), elven magic, weapon familiarity
**Combat Gear** potion of _[[spells/Cure Light Wounds|cure light wounds]]_, potion of fly, scrolls of bull’s strength (2), scroll of _[[spells/Fog Cloud|fog cloud]]_; **Other Gear** _longbow_ with 20 arrows, masterwork _longsword_, 10 gp

The _[[npcs/Whiteclaw Sorcerer|whiteclaw sorcerer]]_ revels in her draconic blood, using her powers to terrify and kill enemies in her territory.
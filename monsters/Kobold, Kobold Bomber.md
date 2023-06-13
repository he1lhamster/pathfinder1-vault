---
cssclass: [monsters]
title1: Kobold, Kobold Bomber
title2: Kobold Bomber
CR: 1
sources:
- name: Monster Codex
  page: 133
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 400
race: Kobold
classes:
- alchemist (alchemical trapper) 2 (Pathfinder RPG Advanced Player's Guide 26, see
  page 128)
alignment: LE
size: Small
type: humanoid
subtypes:
- reptilian
initiative:
  bonus: 3
senses:
  darkvision: 60
AC:
  AC: 19
  touch: 14
  flat_footed: 16
  components:
    armor: 4
    dex: 3
    natural: 1
    size: 1
HP:
  HP: 12
  long: 2d8
saves:
  fort: 2
  ref: 6
  will: 1
  other: +2 vs. poison
weaknesses:
- light sensitivity
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk spear +2 (1d6-1/×3)
      entries:
      - - damage: 1d6-1
          crit_multiplier: 3
      attack: mwk spear
      bonus:
      - 2
  ranged:
  - - text: sling +5 (1d3-1)
      entries:
      - - damage: 1d3-1
      attack: sling
      bonus:
      - 5
  special:
  - bomb 6/day (1d6+2 fire, DC 13)
  - bomb trap
spells:
  entries:
  - superscripts:
    - UC
    name: abjuring step
    source: Alchemist
    level: 1
  - name: endure elements
    source: Alchemist
    level: 1
  - name: shield
    source: Alchemist
    level: 1
  sources:
  - name: Alchemist
    type: prepared
    CL: 2
tactics:
  During Combat: The kobold uses her mutagen and extracts to strengthen her defense,
    and throws bombs at her enemies.
ability_scores:
  STR: 8
  DEX: 16
  CON: 8
  INT: 15
  WIS: 13
  CHA: 8
BAB: 1
CMB: -1
CMD: 12
feats:
- name: Brew Potion
- superscripts:
  - APG
  name: Extra Bombs
- name: Throw Anything
skills:
  Acrobatics: 3
  Craft (trapmaking): 9
  Disable Device: 6
  Escape Artist: 3
  Knowledge (engineering): 4
  Perception: 3
  Profession (miner): 3
  Stealth: 10
  _racial_mods:
    Craft (trapmaking):
      _: 2
    Perception:
      _: 2
    Profession (miner):
      _: 2
languages:
- Common
- Draconic
- Gnome
- Goblin
special_qualities:
- alchemy (alchemy crafting +2, identify potions)
- crafty
- mutagen (+4/-2, +2 natural, 20 minutes)
- poison use
gear:
  combat:
  - potion of invisibility
  - acid
  - alchemist's fire (3)
  other:
  - chain shirt
  - mwk spear
  - sling
  - 8 gp
ecology:
  environment: temperate underground or deep forest
desc_long: Kobold tricksters are experts at crafting deadly traps-both magical and
  mundane-and at striking from concealment while their enemies are distracted by the
  traps' effects.

---

# Kobold, Kobold Bomber

**Source** Monster Codex pg. 133
**XP** 400
_[[monsters/Kobold|Kobold]]_ _[[classes/Alchemist|alchemist]]_ (alchemical trapper) 2 (Pathfinder RPG Advanced Player’s Guide 26, see page 128)

LE Small humanoid (reptilian)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +3

##### Defense

**AC** 19, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+4 armor, +3 Dex, +1 natural, +1 size)
**hp** 12 (2d8)
**Fort** +2, **Ref** +6, **Will** +1; +2 vs. poison
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Spear|spear]]_ +2 (1d6–1/×3)
**Ranged** _[[items/Weapon/Sling|sling]]_ +5 (1d3–1)
**Special Attacks** bomb 6/day (1d6+2 fire, DC 13), bomb trap
**_Alchemist_ Extracts Prepared **(CL 2nd)
1st—abjuring step, _[[spells/Endure Elements|endure elements]]_, _[[spells/Shield|shield]]_

### Tactics

**During Combat** The _kobold_ uses her mutagen and extracts to strengthen her defense, and throws bombs at her enemies.

##### Statistics
**Str** 8, **Dex** 16, **Con** 8, **Int** 15, **Wis** 13, **Cha** 8
**Base Atk** +1; **CMB** –1; **CMD** 12
**Feats** _[[feats/Brew Potion|Brew Potion]]_, _[[feats/Extra Bombs|Extra Bombs]]_, _[[feats/Throw Anything|Throw Anything]]_
**Skills** Acrobatics +3, Craft (trapmaking) +9, Disable Device +6, Escape Artist +3, Knowledge (engineering) +4, Perception +3, Profession (_[[npcs/Miner|miner]]_) +3, Stealth +10; **Racial Modifiers** +2 Craft (trapmaking), +2 Perception, +2 Profession (_miner_)
**Languages** Common, Draconic, Gnome, _[[monsters/Goblin|Goblin]]_
**SQ** alchemy (alchemy crafting +2, _[[spells/Identify|identify]]_ potions), crafty, mutagen (+4/–2, +2 natural, 20 minutes), poison use
**Combat Gear** potion of _[[spells/Invisibility|invisibility]]_, acid, _alchemist_’s fire (3); **Other Gear** _[[items/Armor/Chain shirt|chain shirt]]_, mwk _spear_, _sling_, 8 gp

##### Ecology

**Environment** temperate underground or deep forest

##### Description

_Kobold_ tricksters are experts at crafting _[[items/Weapon Magic Abilities/Deadly|deadly]]_ traps—both magical and mundane—and at striking from concealment while their enemies are distracted by the traps’ effects.
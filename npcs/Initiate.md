---
cssclass: [monsters]
title1: Initiate
title2: Initiate
CR: 1
sources:
- name: NPC Codex
  page: 245
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 400
race: Human
classes:
- adept 3
alignment: CE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 0
AC:
  AC: 12
  touch: 10
  flat_footed: 12
  other: +2 vs. good
  components:
    armor: 2
HP:
  HP: 16
  long: 3d6+6
saves:
  fort: 4
  ref: 1
  will: 4
  other: +2 vs. good
speeds:
  base: 30
attacks:
  melee:
  - - text: spear +1 (1d8/×3)
      entries:
      - - damage: 1d8
          crit_multiplier: 3
      attack: spear
      bonus:
      - 1
  - - text: mwk cold iron dagger +2 (1d4/19-20)
      entries:
      - - damage: 1d4
          crit_range: 19-20
      attack: mwk cold iron dagger
      bonus:
      - 2
  ranged:
  - - text: dart +1 (1d4)
      entries:
      - - damage: 1d4
      attack: dart
      bonus:
      - 1
spells:
  entries:
  - name: burning hands
    source: Adept
    level: 1
    DC: 12
  - name: detect good
    source: Adept
    level: 1
  - name: protection from good
    source: Adept
    level: 1
  - name: detect magic
    source: Adept
    level: 0
  - name: light
    source: Adept
    level: 0
  - name: read magic
    source: Adept
    level: 0
  sources:
  - name: Adept
    type: prepared
    CL: 3
    concentration: 4
    slots:
      0: at-will
tactics:
  Before Combat: The adept casts protection from good.
  During Combat: The adept casts burning hands whenever she can catch two or more
    foes in the area. When she runs out of spells, scrolls, and acid, she fights with
    her spear.
  Base Statistics: Without protection from good, the adept's statistics are AC no
    bonus vs. good; Saves no bonus vs. good.
ability_scores:
  STR: 10
  DEX: 11
  CON: 12
  INT: 8
  WIS: 13
  CHA: 11
BAB: 1
CMB: 1
CMD: 11
feats:
- name: Combat Casting
- name: Great Fortitude
- name: Scribe Scroll
skills:
  Knowledge (arcana): 3
  Knowledge (local): 3
  Knowledge (planes): 3
  Knowledge (religion): 5
  Spellcraft: 5
  Perception: 1
languages:
- Common
special_qualities:
- summon familiar (toad)
gear:
  combat:
  - scrolls of burning hands (2, CL 3rd)
  - scrolls of cure light wounds (2)
  - scroll of obscuring mist (CL 3rd)
  - scroll of sleep (CL 3rd)
  - acid (2)
  other:
  - leather armor
  - darts (6)
  - masterwork cold iron dagger
  - spear
  - belt pouch
  - masterwork manacles
  - scroll case
  - silver holy symbol (cracked moon)
  - spell component pouch
  - 9 gp
desc_long: The initiate never knew her true calling until strange visions opened her
  eyes to the terrors beyond reality. Now touched by madness, she tries to bring others
  into the darkness.

---

# Initiate

**Source** NPC Codex pg. 245
**XP** 400
Human adept 3
CE Medium humanoid (human)
**Init** +0; **Senses** Perception +1

##### Defense

**AC** 12, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+2 armor); +2 vs. good
**hp** 16 (3d6+6)
**Fort** +4, **Ref** +1, **Will** +4; +2 vs. good

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Spear|spear]]_ +1 (1d8/×3) or mwk cold iron _[[items/Weapon/Dagger|dagger]]_ +2 (1d4/19–20)
**Ranged** _[[items/Weapon/Dart|dart]]_ +1 (1d4)
**Adept Spells Prepared **(CL 3rd; concentration +4)
1st—_[[spells/Burning Hands|burning hands]]_ (DC 12), _[[spells/Detect Good|detect good]]_, _[[spells/Protection From Good|protection from good]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, light, _[[spells/Read Magic|read magic]]_

### Tactics

**Before Combat **The adept casts _protection from good_.
**During Combat **The adept casts _burning hands_ whenever she can catch two or more foes in the area. When she runs out of spells, scrolls, and acid, she fights with her _spear_.
**Base Statistics **Without _protection from good_, the adept’s statistics are **AC **no bonus vs. good; **Saves **no bonus vs. good.

##### Statistics
**Str** 10, **Dex** 11, **Con** 12, **Int** 8, **Wis** 13, **Cha** 11
**Base Atk** +1; **CMB** +1; **CMD** 11
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_
**Skills** Knowledge (arcana, local, planes) +3, Knowledge (religion) +5, Spellcraft +5
**Languages** Common
**SQ** _[[universal monster rules/Summon|summon]]_ familiar (toad)
**Combat Gear** scrolls of _burning hands_ (2, CL 3rd), scrolls of _[[spells/Cure Light Wounds|cure light wounds]]_ (2), scroll of _[[spells/Obscuring Mist|obscuring mist]]_ (CL 3rd), scroll of sleep (CL 3rd), acid (2); **Other Gear** _[[items/Armor/Leather armor|leather armor]]_, darts (6), masterwork cold iron _dagger_, _spear_, _[[items/Mundane/Belt pouch|belt pouch]]_, masterwork manacles, _[[items/Mundane/Scroll case|scroll case]]_, silver holy symbol (cracked moon), _[[items/Mundane/Spell component pouch|spell component pouch]]_, 9 gp

The _[[npcs/Initiate|initiate]]_ never knew her true calling until strange visions opened her eyes to the terrors beyond reality. Now touched by madness, she tries to bring others into the _[[spells/Darkness|darkness]]_.
---
cssclass: [monsters]
title1: Shoreline Cleric
title2: Shoreline Cleric
CR: 3
sources:
- name: NPC Codex
  page: 45
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 800
race: Half-elf
classes:
- cleric of Gozreh 4
alignment: N
size: Medium
type: humanoid
subtypes:
- elf
- human
initiative:
  bonus: 2
senses:
  low-light vision: true
AC:
  AC: 19
  touch: 12
  flat_footed: 17
  components:
    armor: 5
    dex: 2
    natural: 2
HP:
  HP: 25
  long: 4d8+4
saves:
  fort: 5
  ref: 3
  will: 8
  other: +2 vs. enchantments
immunities:
- sleep
speeds:
  base: 30
attacks:
  melee:
  - - text: trident +2 (1d8-1)
      entries:
      - - damage: 1d8-1
      attack: trident
      bonus:
      - 2
  ranged:
  - - text: shortbow +5 (1d6/×3)
      entries:
      - - damage: 1d6
          crit_multiplier: 3
      attack: shortbow
      bonus:
      - 5
  special:
  - channel positive energy 4/day (DC 13, 2d6)
  - wooden fist (+2, 7 rounds/day)
spell_like_abilities:
  entries:
  - name: storm burst
    source: default
    freq: 7/day
    other: 1d6+2 nonlethal damage
  sources:
  - name: default
    CL: 4
    concentration: 8
spells:
  entries:
  - name: barkskin
    source: Cleric
    level: 2
  - name: hold person
    source: Cleric
    level: 2
    count: 2
    DC: 16
  - name: summon monster II
    source: Cleric
    level: 2
  - name: cause fear
    source: Cleric
    level: 1
    DC: 15
  - name: cure light wounds
    source: Cleric
    level: 1
  - name: endure elements
    source: Cleric
    level: 1
  - name: entangle
    source: Cleric
    level: 1
    DC: 15
  - name: entropic shield
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    count: 2
    DC: 14
  - name: guidance
    source: Cleric
    level: 0
  - name: light
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 4
    concentration: 8
    slots:
      0: at-will
    domains:
    - plant
    - weather
tactics:
  Before Combat: The cleric casts barkskin.
  During Combat: The cleric casts entropic shield, then uses hold person, entangle,
    and bane arrows.
  Base Statistics: Without barkskin, her statistics are AC 17, touch 12, flat-footed
    15.
ability_scores:
  STR: 8
  DEX: 14
  CON: 13
  INT: 10
  WIS: 18
  CHA: 12
BAB: 3
CMB: 2
CMD: 14
feats:
- name: Deadly Aim
- name: Martial Weapon Proficiency (shortbow)
- name: Skill Focus (Stealth)
skills:
  Heal: 8
  Knowledge (nature): 2
  Knowledge (religion): 5
  Perception: 9
  Sense Motive: 8
  Stealth: 7
languages:
- Common
- Elven
special_qualities:
- aura
- elf blood
gear:
  combat:
  - +1 human-bane arrows (2)
  - +1 orc-bane arrow
  - potion of cure moderate wounds
  other:
  - +1 chain shirt
  - shortbow with 20 arrows
  - trident
  - anchor feather token
  - wooden holy symbol
  - 256 gp
desc_long: There is no description for this NPC.

---

# Shoreline Cleric

**Source** NPC Codex pg. 45
**XP** 800
Half-elf _[[classes/Cleric|cleric]]_ of Gozreh 4

N Medium humanoid (elf, human)
**Init** +2; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +9

##### Defense

**AC** 19, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+5 armor, +2 Dex, +2 natural)
**hp** 25 (4d8+4)
**Fort** +5, **Ref** +3, **Will** +8; +2 vs. enchantments
**Immune** sleep

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Trident|trident]]_ +2 (1d8–1)
**Ranged** _[[items/Weapon/Shortbow|shortbow]]_ +5 (1d6/×3)
**Special Attacks** channel positive energy 4/day (DC 13, 2d6), wooden fist (+2, 7 rounds/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +8)
7/day—storm burst (1d6+2 nonlethal damage)
**_Cleric_ Spells Prepared **(CL 4th; concentration +8)
2nd—_[[spells/Barkskin|barkskin]]_, _[[spells/Hold Person|hold person]]_ (2, DC 16), _[[spells/Summon Monster II|summon monster II]]_
1st—_[[spells/Cause Fear|cause fear]]_ (DC 15), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Endure Elements|endure elements]]_, _[[spells/Entangle|entangle]]_ (DC 15), _[[spells/Entropic Shield|entropic shield]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (2, DC 14), _[[spells/Guidance|guidance]]_, light
**D **Domain spell; **Domains **Plant, Weather

### Tactics

**Before Combat **The _cleric_ casts _barkskin_.
**During Combat **The _cleric_ casts _entropic shield_, then uses _hold person_, _entangle_, and _[[spells/Bane|bane]]_ arrows.
**Base Statistics **Without _barkskin_, her statistics are **AC **17, touch 12, _flat-footed_ 15.

##### Statistics
**Str** 8, **Dex** 14, **Con** 13, **Int** 10, **Wis** 18, **Cha** 12
**Base Atk** +3; **CMB** +2; **CMD** 14
**Feats** _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Martial Weapon Proficiency|Martial Weapon Proficiency]]_ (_shortbow_), _[[feats/Skill Focus|Skill Focus]]_ (Stealth)
**Skills** _[[spells/Heal|Heal]]_ +8, Knowledge (nature) +2, Knowledge (religion) +5, Perception +9, Sense Motive +8, Stealth +7
**Languages** Common, Elven
**SQ** aura, elf blood
**Combat Gear** +1 human-bane arrows (2), +1 orc-bane arrow, potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_; **Other Gear** +1 _[[items/Armor/Chain shirt|chain shirt]]_, _shortbow_ with 20 arrows, _trident_, anchor feather token, wooden holy symbol, 256 gp

There is no description for this NPC.
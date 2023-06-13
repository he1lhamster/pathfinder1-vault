---
cssclass: [monsters]
title1: Hobgoblin, Hobgoblin Bombardier
title2: Hobgoblin Bombardier
CR: 7
sources:
- name: Monster Codex
  page: 120
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 3200
race: Hobgoblin
classes:
- alchemist (grenadier) 8 (Pathfinder RPG Advanced Player's Guide 26, see page 116)
alignment: LE
size: Medium
type: humanoid
subtypes:
- goblinoid
initiative:
  bonus: 4
senses:
  darkvision: 60
AC:
  AC: 18
  touch: 14
  flat_footed: 14
  components:
    armor: 4
    dex: 4
HP:
  HP: 71
  long: 8d8+32
saves:
  fort: 9
  ref: 10
  will: 2
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk short sword +8/+3 (1d6+1/19-20)
      entries:
      - - damage: 1d6+1
          crit_range: 19-20
      attack: mwk short sword
      bonus:
      - 8
      - 3
  ranged:
  - - text: bomb +12/+7 (4d6+2 fire)
      entries:
      - - damage: 4d6+2
          type: fire
      attack: bomb
      bonus:
      - 12
      - 7
  special:
  - alchemical weapon (swift action)
  - bomb 14/day (4d6+2 fire, DC 16)
  - directed blast
spells:
  entries:
  - name: fly
    source: Alchemist
    level: 3
  - name: haste
    source: Alchemist
    level: 3
  - name: barkskin
    source: Alchemist
    level: 2
  - name: cat's grace
    source: Alchemist
    level: 2
  - name: false life
    source: Alchemist
    level: 2
  - name: invisibility
    source: Alchemist
    level: 2
  - name: resist energy
    source: Alchemist
    level: 2
  - superscripts:
    - APG
    name: bomber's eye
    source: Alchemist
    level: 1
  - name: expeditious retreat
    source: Alchemist
    level: 1
  - name: shield
    source: Alchemist
    level: 1
  - name: true strike
    source: Alchemist
    level: 1
    count: 2
  sources:
  - name: Alchemist
    type: prepared
    CL: 8
tactics:
  During Combat: The bombardier hurls bombs at enemies, or uses directed blast if
    the foes are grouped closely together. He uses unstable accelerants with the bombs
    that seem most likely to hit. He saves most of his alchemical items to use with
    the alchemical weapon ability if he gets stuck fighting in melee range. In this
    circumstance, he drinks his mutagen before attacking.
ability_scores:
  STR: 12
  DEX: 18
  CON: 16
  INT: 14
  WIS: 10
  CHA: 8
BAB: 6
CMB: 7
CMD: 21
feats:
- name: Point-Blank Shot
- name: Precise Shot
- name: Throw Anything
- name: Toughness
- name: Weapon Focus (bomb)
skills:
  Craft (alchemy): 15
  Heal: 7
  Knowledge (arcana): 11
  Knowledge (engineering): 8
  Knowledge (nature): 11
  Perception: 16
  Spellcraft: 13
  Use Magic Device: 6
languages:
- Aklo
- Common
- Goblin
- Sylvan
special_qualities:
- alchemy (alchemy crafting +8, identify potions)
- alternate racial features
- discoveries (concussive bomb [4d4+2 sonic plus deafness], fast bombs, precise bombs
  [2 squares], smoke bomb, stink bomb)
- mutagen (+4/-2, +2 natural, 80 minutes)
- swift alchemy
gear:
  combat:
  - wand of cure light wounds (40 charges)
  - acid (3)
  - alchemist's fire (4)
  - smokesticks (2)
  - tanglefoot bags (2)
  - unstable accelerant (3)
  other:
  - +2 leather armor
  - bombchucker
  - mwk short sword
  - eyes of the eagle
  - 30 gp
ecology:
  environment: temperate hills
special_abilities:
  Alternate Racial Features (Ex): The bombardier has the engineer racial trait in
    place of sneaky, granting him a +2 bonus on Craft (alchemy) and Knowledge (engineering)
    checks. He also employs the hobgoblin alternate favored class option for his alchemy
    levels, granting him four additional uses of his bomb ability each day. Both of
    these racial options can be found on page 121 of the Pathfinder RPG Advanced Race
    Guide.
desc_long: These alchemists focus their race's penchant for fire into more productive
  and efficient means of destruction than mere torches or bonfires. Instead, they
  hone the craft of concocting bombs, mutagens, and extracts. Though they possess
  the means of enhancing their physical prowess, many bombardiers forgo imbibing their
  mutagens prior to battle, believing that increasing one's weaknesses, even for potential
  gain in other areas, is a tactical mistake. When the situation calls for it, however,
  they drink mutagens to increase their physical stamina or ranged accuracy, preferring
  to decrease their perception and influence before compromising their mental faculties.

---

# Hobgoblin, Hobgoblin Bombardier

**Source** Monster Codex pg. 120
**XP** 3,200
_[[monsters/Hobgoblin|Hobgoblin]]_ _[[classes/Alchemist|alchemist]]_ (grenadier) 8 (Pathfinder RPG Advanced Player’s Guide 26, see page 116)

LE Medium humanoid (goblinoid)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +16

##### Defense

**AC** 18, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+4 armor, +4 Dex)
**hp** 71 (8d8+32)
**Fort** +9, **Ref** +10, **Will** +2

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Short sword|short sword]]_ +8/+3 (1d6+1/19–20)
**Ranged** bomb +12/+7 (4d6+2 fire)
**Special Attacks** alchemical weapon (swift action), bomb 14/day (4d6+2 fire, DC 16), directed blast
**_Alchemist_ Extracts Prepared **(CL 8th)
3rd—fly, _[[spells/Haste|haste]]_
2nd—_[[spells/Barkskin|barkskin]]_, cat’s _[[spells/Grace|grace]]_, _[[spells/False Life|false life]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Resist Energy|resist energy]]_
1st—bomber’s eye, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_ (2)

### Tactics

**During Combat** The bombardier hurls bombs at enemies, or uses directed blast if the foes are grouped closely together. He uses unstable accelerants with the bombs that seem most likely to hit. He saves most of his alchemical items to use with the alchemical weapon ability if he gets stuck fighting in melee range. In this circumstance, he drinks his mutagen before attacking.

##### Statistics
**Str** 12, **Dex** 18, **Con** 16, **Int** 14, **Wis** 10, **Cha** 8
**Base Atk** +6; **CMB** +7; **CMD** 21
**Feats** _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Throw Anything|Throw Anything]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bomb)
**Skills** Craft (alchemy) +15, _[[spells/Heal|Heal]]_ +7, Knowledge (arcana) +11, Knowledge (engineering) +8, Knowledge (nature) +11, Perception +16, Spellcraft +13, Use Magic Device +6
**Languages** Aklo, Common, _[[monsters/Goblin|Goblin]]_, Sylvan
**SQ** alchemy (alchemy crafting +8, _[[spells/Identify|identify]]_ potions), alternate racial features, discoveries (concussive bomb [4d4+2 sonic plus deafness], fast bombs, precise bombs [2 squares], _[[items/Mundane/Smoke Bomb|smoke bomb]]_, stink bomb), mutagen (+4/–2, +2 natural, 80 minutes), swift alchemy
**Combat Gear** wand of _[[spells/Cure Light Wounds|cure light wounds]]_ (40 charges), acid (3), _alchemist_’s fire (4), smokesticks (2), tanglefoot bags (2), _[[items/Mundane/Unstable accelerant|unstable accelerant]]_ (3); **Other Gear** +2 _[[items/Armor/Leather armor|leather armor]]_, _[[items/Mundane/Bombchucker|bombchucker]]_, mwk _short sword_, _[[items/Wondrous Item/Eyes of the Eagle|eyes of the eagle]]_, 30 gp

##### Ecology

**Environment** temperate hills

### Special Abilities

**Alternate Racial Features (Ex)** The bombardier has the engineer racial trait in place of _[[items/Weapon Magic Abilities/Sneaky|sneaky]]_, granting him a +2 bonus on Craft (alchemy) and Knowledge (engineering) checks. He also employs the _hobgoblin_ alternate favored class option for his alchemy levels, granting him four additional uses of his bomb ability each day. Both of these racial options can be found on page 121 of the Pathfinder RPG Advanced Race Guide.

##### Description

These alchemists focus their race’s penchant for fire into more productive and efficient means of _[[spells/Destruction|destruction]]_ than mere torches or bonfires. Instead, they hone the craft of concocting bombs, mutagens, and extracts. Though they possess the means of enhancing their physical prowess, many bombardiers forgo imbibing their mutagens prior to battle, believing that increasing one’s weaknesses, even for potential gain in other areas, is a tactical mistake. When the situation calls for it, however, they drink mutagens to increase their physical stamina or ranged accuracy, preferring to decrease their perception and influence before compromising their mental faculties.
---
cssclass: [monsters]
title1: Ratfolk, Ratfolk Chemist
title2: Ratfolk Chemist
CR: 7
sources:
- name: Monster Codex
  page: 182
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 3200
race: Ratfolk
classes:
- alchemist 8 (Pathfinder RPG Advanced Player's Guide 26)
alignment: N
size: Small
type: humanoid
subtypes:
- ratfolk
initiative:
  bonus: 9
senses:
  darkvision: 60
AC:
  AC: 26
  touch: 17
  flat_footed: 21
  components:
    armor: 4
    deflection: 1
    dex: 5
    natural: 5
    size: 1
HP:
  HP: 63
  long: 8d8+24
saves:
  fort: 9
  ref: 14
  will: 3
  other: +6 vs. poison
speeds:
  base: 20
attacks:
  melee:
  - - text: dagger +6/+1 (1d3-1/19-20)
      entries:
      - - damage: 1d3-1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 6
      - 1
  ranged:
  - - text: light crossbow +12 (1d6/19-20)
      entries:
      - - damage: 1d6
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 12
  - - text: bomb +12/+7 (4d6+4 cold or fire)
      entries:
      - - damage: 4d6+4
          type: cold or fire
      attack: bomb
      bonus:
      - 12
      - 7
  special:
  - bomb 12/day (4d6+4 cold or fire, DC 18)
  - swarming
spells:
  entries:
  - name: cure serious wounds
    source: Alchemist
    level: 3
  - name: fly
    source: Alchemist
    level: 3
  - name: heroism
    source: Alchemist
    level: 3
  - name: barkskin
    source: Alchemist
    level: 2
  - name: bull's strength
    source: Alchemist
    level: 2
  - name: invisibility
    source: Alchemist
    level: 2
  - name: resist energy
    source: Alchemist
    level: 2
  - name: see invisibility
    source: Alchemist
    level: 2
  - name: comprehend languages
    source: Alchemist
    level: 1
  - superscripts:
    - APG
    name: crafter's fortune
    source: Alchemist
    level: 1
  - superscripts:
    - APG
    name: negate aroma
    source: Alchemist
    level: 1
    DC: 15
  - name: reduce person
    source: Alchemist
    level: 1
    DC: 15
  - name: shield
    source: Alchemist
    level: 1
  sources:
  - name: Alchemist
    type: prepared
    CL: 8
tactics:
  Before Combat: The chemist imbibes her mutagen and extracts of barkskin and fly.
    She gives infusions of bull's strength and heroism to allies.
  During Combat: The chemist drops bombs while flying above the fray.
  Base Statistics: Without her mutagen and barkskin, the chemist's statistics are
    Init +7; Senses Perception +14; AC 19, touch 15, flat-footed 16; Ref +12; Ranged
    light crossbow +10 (1d6/19-20) or bomb +10/+5 (4d6+4 cold or fire); Dex 16, Wis
    12; CMD 18; Skills Heal +8, Perception +14, Profession (herbalist) +12, Survival
    +8.
ability_scores:
  STR: 8
  DEX: 20
  CON: 14
  INT: 18
  WIS: 10
  CHA: 8
BAB: 6
CMB: 4
CMD: 20
feats:
- name: Brew Potion
- name: Improved Initiative
- name: Lightning Reflexes
- name: Point-Blank Shot
- name: Precise Shot
- name: Throw Anything
skills:
  Appraise: 11
  Craft (alchemy): 17
  Disable Device: 16
  Heal: 7
  Knowledge (arcana): 15
  Knowledge (nature): 15
  Perception: 13
  Profession (herbalist): 11
  Spellcraft: 11
  Survival: 7
  Use Magic Device: 1
  _racial_mods:
    Craft (alchemy):
      _: 2
    Perception:
      _: 2
    Use Magic Device:
      _: 2
languages:
- Common
- Draconic
- Dwarven
- Gnome
- Undercommon
special_qualities:
- alchemy (alchemy crafting +8, identify potions)
- discoveries (fast bombs, frost bomb, infusion, precise bombs [4 squares])
- mutagen (+4/-2, +2 natural, 80 minutes)
- poison use
- swift alchemy
- swift poisoning
gear:
  combat:
  - potions of cure serious wounds (3)
  - potion of displacement
  - potion of invisibility
  - acid (2)
  - antitoxin (2)
  - smokesticks (2)
  - tanglefoot bags (2)
  other:
  - +1 studded leather
  - dagger
  - light crossbow with 10 bolts
  - cloak of resistance +1
  - dust of dryness
  - elixir of truth
  - ring of protection +1
  - formula book (contains prepared extracts plus displacement, disguise self, endure
    elements, enlarge person, expeditious retreat, identify, and jump)
  - tindertwigs (10)
  - 317 gp
ecology:
  environment: warm deserts or urban
desc_long: Ratfolk chemists are treasured members of ratfolk colonies. Not only do
  they provide the warren with excellent defensive capability, but their alchemical
  creations are valuable merchandise to sell or trade.

---

# Ratfolk, Ratfolk Chemist

**Source** Monster Codex pg. 182
**XP** 3,200
_[[monsters/Ratfolk|Ratfolk]]_ _[[classes/Alchemist|alchemist]]_ 8 (Pathfinder RPG Advanced Player’s Guide 26)

N Small humanoid (_ratfolk_)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +13

##### Defense

**AC** 26, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+4 armor, +1 deflection, +5 Dex, +5 natural, +1 size)
**hp** 63 (8d8+24)
**Fort** +9, **Ref** +14, **Will** +3; +6 vs. poison

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +6/+1 (1d3–1/19–20)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +12 (1d6/19–20) or bomb +12/+7 (4d6+4 cold or fire)
**Special Attacks** bomb 12/day (4d6+4 cold or fire, DC 18), swarming
**_Alchemist_ Extracts Prepared **(CL 8th)
3rd—_[[spells/Cure Serious Wounds|cure serious wounds]]_, fly, _[[spells/Heroism|heroism]]_
2nd—_[[spells/Barkskin|barkskin]]_, bull’s strength, _[[spells/Invisibility|invisibility]]_, _[[spells/Resist Energy|resist energy]]_, _[[spells/See Invisibility|see invisibility]]_
1st—_[[spells/Comprehend Languages|comprehend languages]]_, crafter’s fortune, _[[spells/Negate Aroma|negate aroma]]_ (DC 15), _[[spells/Reduce Person|reduce person]]_ (DC 15), _[[spells/Shield|shield]]_

### Tactics

**Before Combat** The chemist imbibes her mutagen and extracts of _barkskin_ and fly. She gives infusions of bull’s strength and _heroism_ to allies.
 **During Combat** The chemist drops bombs while flying above the fray.
 **Base Statistics** Without her mutagen and _barkskin_, the chemist’s statistics are **Init **+7; **Senses **Perception +14; **AC **19, touch 15, _flat-footed_ 16; **Ref **+12; **Ranged **_light crossbow_ +10 (1d6/19–20) or bomb +10/+5 (4d6+4 cold or fire); **Dex **16, **Wis **12; **CMD **18; **Skills **_[[spells/Heal|Heal]]_ +8, Perception +14, Profession (herbalist) +12, Survival +8.

##### Statistics
**Str** 8, **Dex** 20, **Con** 14, **Int** 18, **Wis** 10, **Cha** 8
**Base Atk** +6; **CMB** +4; **CMD** 20
**Feats** _[[feats/Brew Potion|Brew Potion]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Throw Anything|Throw Anything]]_
**Skills** Appraise +11, Craft (alchemy) +17, Disable Device +16, _Heal_ +7, Knowledge (arcana) +15, Knowledge (nature) +15, Perception +13, Profession (herbalist) +11, Spellcraft +11, Survival +7, Use Magic Device +1; **Racial Modifiers** +2 Craft (alchemy), +2 Perception, +2 Use Magic Device
**Languages** Common, Draconic, Dwarven, Gnome, Undercommon
**SQ** alchemy (alchemy crafting +8, _[[spells/Identify|identify]]_ potions), discoveries (fast bombs, frost bomb, infusion, precise bombs [4 squares]), mutagen (+4/–2, +2 natural, 80 minutes), poison use, swift alchemy, swift _[[items/Armor Magic Abilities/Poisoning|poisoning]]_
**Combat Gear** potions of _cure serious wounds_ (3), potion of _[[spells/Displacement|displacement]]_, potion of _invisibility_, acid (2), _[[items/Mundane/Antitoxin|antitoxin]]_ (2), smokesticks (2), tanglefoot bags (2); **Other Gear** +1 studded leather, _dagger_, _light crossbow_ with 10 bolts, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Dust of Dryness|dust of dryness]]_, _[[items/Wondrous Item/Elixir of Truth|elixir of truth]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Mundane/Formula book|formula book]]_ (contains prepared extracts plus _displacement_, _[[spells/Disguise Self|disguise self]]_, _[[spells/Endure Elements|endure elements]]_, _[[spells/Enlarge Person|enlarge person]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _identify_, and _[[spells/Jump|jump]]_), tindertwigs (10), 317 gp

##### Ecology

**Environment** warm deserts or urban

##### Description

_Ratfolk_ chemists are treasured members of _ratfolk_ colonies. Not only do they provide the warren with excellent defensive capability, but their alchemical creations are valuable merchandise to sell or trade.
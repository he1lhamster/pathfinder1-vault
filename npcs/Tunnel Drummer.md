---
cssclass: [monsters]
title1: Tunnel Drummer
title2: Tunnel Drummer
CR: 13
sources:
- name: NPC Codex
  page: 37
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 25600
race: Dwarf
classes:
- bard 14
alignment: LN
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 1
AC:
  AC: 19
  touch: 12
  flat_footed: 17
  components:
    armor: 6
    dex: 1
    dodge: 1
    natural: 1
HP:
  HP: 100
  long: 14d8+34
saves:
  fort: 6
  ref: 10
  will: 9
  other: +2 vs. poison, spells, and spell-like abilities, +4 vs. bardic performance,
    language-dependent, and sonic
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 thundering heavy mace +14/+9 (1d8+3)
      entries:
      - - damage: 1d8+3
      attack: +1 thundering heavy mace
      bonus:
      - 14
      - 9
  ranged:
  - - text: +1 heavy crossbow +12 (1d10+1/19-20)
      entries:
      - - damage: 1d10+1
          crit_range: 19-20
      attack: +1 heavy crossbow
      bonus:
      - 12
  special:
  - +1 on attack rolls against goblinoid and orc humanoids
  - bardic performance 35 rounds/day (swift action; countersong, dirge of doom, distraction,
    fascinate, frightening tune, inspire competence +4, inspire courage +3, inspire
    greatness, soothing performance, suggestion)
spells:
  entries:
  - name: greater dispel magic
    source: Bard
    level: 5
  - name: mind fog
    source: Bard
    level: 5
    DC: 20
  - name: song of discord
    source: Bard
    level: 5
    DC: 20
  - name: dimension door
    source: Bard
    level: 4
  - name: greater invisibility
    source: Bard
    level: 4
  - name: hold monster
    source: Bard
    level: 4
    DC: 19
  - name: shout
    source: Bard
    level: 4
    DC: 19
  - name: blink
    source: Bard
    level: 3
  - name: confusion
    source: Bard
    level: 3
    DC: 18
  - name: gaseous form
    source: Bard
    level: 3
  - name: haste
    source: Bard
    level: 3
    DC: 18
  - name: see invisibility
    source: Bard
    level: 3
  - name: alter self
    source: Bard
    level: 2
  - name: glitterdust
    source: Bard
    level: 2
    DC: 17
  - name: shatter
    source: Bard
    level: 2
  - name: sound burst
    source: Bard
    level: 2
    DC: 17
  - name: summon swarm
    source: Bard
    level: 2
  - name: alarm
    source: Bard
    level: 1
  - name: expeditious retreat
    source: Bard
    level: 1
  - name: feather fall
    source: Bard
    level: 1
  - name: grease
    source: Bard
    level: 1
  - name: hideous laughter
    source: Bard
    level: 1
    DC: 16
  - name: magic mouth
    source: Bard
    level: 1
  - name: detect magic
    source: Bard
    level: 0
  - name: flare
    source: Bard
    level: 0
    DC: 15
  - name: ghost sound
    source: Bard
    level: 0
    DC: 15
  - name: light
    source: Bard
    level: 0
  - name: mending
    source: Bard
    level: 0
  - name: prestidigitation
    source: Bard
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 14
    concentration: 19
    slots:
      5: 2
      4: 4
      3: 5
      2: 6
      1: 6
      0: at-will
tactics:
  Before Combat: The bard drinks a potion of eagle's splendor.
  During Combat: The bard uses mind fog and dirge of doom.
  Base Statistics: Without eagle's splendor, the bard's statistics are Bard Spells
    Known reduce spell DCs by 2; Cha 16; Skills Diplomacy +12, Perform (comedy, oratory)
    +16, Perform (percussion) +20, Perform (string) +12, Use Magic Device +14.
ability_scores:
  STR: 14
  DEX: 13
  CON: 14
  INT: 10
  WIS: 10
  CHA: 20
BAB: 10
CMB: 12
CMD: 24
CMD_other: 28 vs. bull rush or trip
feats:
- name: Cleave
- name: Dazzling Display
- name: Dodge
- name: Point-Blank Shot
- name: Power Attack
- name: Rapid Reload
- name: Weapon Focus (heavy mace)
skills:
  Acrobatics: 9
    when jumping: 5
  Diplomacy: 14
  Knowledge (dungeoneering): 13
  Knowledge (engineering): 12
  Knowledge (history): 12
  Knowledge (geography): 11
  Knowledge (nobility): 11
  Knowledge (religion): 11
  Perception: 13
    to notice unusual stonework: 15
  Perform (comedy): 18
  Perform (oratory): 18
  Perform (percussion): 22
  Perform (string): 14
  Spellcraft: 8
  Stealth: 10
  Use Magic Device: 16
languages:
- Common
- Dwarven
special_qualities:
- bardic knowledge +7
- jack-of-all-trades (use any skill)
- lore master 2/day
- versatile performance (comedy, dance, oratory, percussion)
gear:
  combat:
  - potion of eagle's splendor
  - wand of cure moderate wounds (50 charges)
  other:
  - +2 chain shirt
  - +1 heavy crossbow with 20 bolts
  - +1 thundering heavy mace
  - amulet of natural armor +1
  - lyre of building
  - drum
  - 88 gp
desc_long: Tunnel drummers keep time for acts of work and war carried out in deep
  warrens and mine tunnels.

---

# Tunnel Drummer

**Source** NPC Codex pg. 37
**XP** 25,600
Dwarf _[[classes/Bard|bard]]_ 14

LN Medium humanoid (dwarf)
**Init** +1; **Senses** Perception +13

##### Defense

**AC** 19, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+6 armor, +1 Dex, +1 _[[feats/Dodge|dodge]]_, +1 natural)
**hp** 100 (14d8+34)
**Fort** +6, **Ref** +10, **Will** +9; +2 vs. poison, spells, and _[[universal monster rules/Spell-Like Abilities|spell-like abilities]]_, +4 vs. bardic performance, language-dependent, and sonic
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _dodge_ bonus to AC vs. giants)

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon Magic Abilities/Thundering|thundering]]_ _[[items/Weapon/Heavy mace|heavy mace]]_ +14/+9 (1d8+3)
**Ranged** +1 _[[items/Weapon/Heavy crossbow|heavy crossbow]]_ +12 (1d10+1/19–20)
**Special Attacks** +1 on attack rolls against goblinoid and _[[monsters/Orc|orc]]_ humanoids, bardic performance 35 rounds/day (swift action; countersong, dirge of _[[spells/Doom|doom]]_, _[[universal monster rules/Distraction|distraction]]_, fascinate, frightening tune, inspire competence +4, inspire courage +3, inspire greatness, soothing performance, _[[spells/Suggestion|suggestion]]_)
**_Bard_ Spells Known **(CL 14th; concentration +19)
5th (2/day)—greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Mind Fog|mind fog]]_ (DC 20), _[[spells/Song of Discord|song of discord]]_ (DC 20)
4th (4/day)—_[[spells/Dimension Door|dimension door]]_, greater _[[spells/Invisibility|invisibility]]_, _[[spells/Hold Monster|hold monster]]_ (DC 19), _[[spells/Shout|shout]]_ (DC 19)
3rd (5/day)—_[[spells/Blink|blink]]_, _[[spells/Confusion|confusion]]_ (DC 18), _[[spells/Gaseous Form|gaseous form]]_, _[[spells/Haste|haste]]_ (DC 18), _[[spells/See Invisibility|see invisibility]]_
2nd (6/day)—_[[spells/Alter Self|alter self]]_, _[[spells/Glitterdust|glitterdust]]_ (DC 17), _[[spells/Shatter|shatter]]_, _[[spells/Sound Burst|sound burst]]_ (DC 17), _[[spells/Summon Swarm|summon swarm]]_
1st (6/day)—_[[spells/Alarm|alarm]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Grease|grease]]_, _[[spells/Hideous Laughter|hideous laughter]]_ (DC 16), _[[spells/Magic Mouth|magic mouth]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 15), _[[spells/Ghost Sound|ghost sound]]_ (DC 15), light, _[[spells/Mending|mending]]_, _[[spells/Prestidigitation|prestidigitation]]_

### Tactics

**Before Combat **The _bard_ drinks a potion of _[[monsters/Eagle|eagle]]_’s splendor.
**During Combat **The _bard_ uses _mind fog_ and dirge of _doom_.
**Base Statistics **Without _eagle_’s splendor, the _bard_’s statistics are **_Bard_ Spells Known **reduce spell DCs by 2; **Cha **16; **Skills **Diplomacy +12, Perform (comedy, oratory) +16, Perform (percussion) +20, Perform (string) +12, Use Magic Device +14.

##### Statistics
**Str** 14, **Dex** 13, **Con** 14, **Int** 10, **Wis** 10, **Cha** 20
**Base Atk** +10; **CMB** +12; **CMD** 24 (28 vs. bull rush or _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Dazzling Display|Dazzling Display]]_, _Dodge_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Rapid Reload|Rapid Reload]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_heavy mace_)
**Skills** Acrobatics +9 (+5 when jumping), Diplomacy +14, Knowledge (dungeoneering) +13, Knowledge (engineering, history) +12, Knowledge (geography, nobility, religion) +11, Perception +13 (+15 to notice unusual stonework), Perform (comedy, oratory) +18, Perform (percussion) +22, Perform (string) +14, Spellcraft +8, Stealth +10, Use Magic Device +16
**Languages** Common, Dwarven
**SQ** bardic knowledge +7, jack-of-all-trades (use any skill), lore master 2/day, versatile performance (comedy, dance, oratory, percussion)
**Combat Gear** potion of _eagle_’s splendor, wand of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (50 charges); **Other Gear** +2 _[[items/Armor/Chain shirt|chain shirt]]_, +1 _heavy crossbow_ with 20 bolts, +1 _thundering_ _heavy mace_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Lyre of Building|lyre of building]]_, drum, 88 gp

Tunnel drummers keep time for acts of work and war carried out in deep warrens and mine tunnels.
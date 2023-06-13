---
cssclass: [monsters]
title1: Street Artist
title2: Street Artist
CR: 7
sources:
- name: NPC Codex
  page: 31
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 3200
race: Elf
classes:
- bard 8
alignment: CN
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 3
senses:
  low-light vision: true
AC:
  AC: 18
  touch: 15
  flat_footed: 14
  components:
    armor: 3
    deflection: 1
    dex: 3
    dodge: 1
HP:
  HP: 43
  long: 8d8+4
saves:
  fort: 3
  ref: 10
  will: 7
  other: +2 vs. enchantments, +4 vs. bardic performance, language-dependent, and sonic
immunities:
- sleep
speeds:
  base: 30
attacks:
  melee:
  - - text: rapier +7/+2 (1d6+1/18-20)
      entries:
      - - damage: 1d6+1
          crit_range: 18-20
      attack: rapier
      bonus:
      - 7
      - 2
  ranged:
  - - text: +1 longbow +10/+5 (1d8+1/×3)
      entries:
      - - damage: 1d8+1
          crit_multiplier: 3
      attack: +1 longbow
      bonus:
      - 10
      - 5
  special:
  - bardic performance 21 rounds/day (move action; countersong, dirge of doom, distraction,
    fascinate, inspire competence +3, inspire courage +2, suggestion)
spells:
  entries:
  - name: haste
    source: Bard
    level: 3
    DC: 18
  - name: major image
    source: Bard
    level: 3
    DC: 18
  - name: sepia snake sigil
    source: Bard
    level: 3
    DC: 18
  - name: invisibility
    source: Bard
    level: 2
  - name: mirror image
    source: Bard
    level: 2
  - name: shatter
    source: Bard
    level: 2
  - name: sound burst
    source: Bard
    level: 2
    DC: 16
  - name: animate rope
    source: Bard
    level: 1
  - name: disguise self
    source: Bard
    level: 1
  - name: grease
    source: Bard
    level: 1
  - name: lesser confusion
    source: Bard
    level: 1
    DC: 14
  - name: silent image
    source: Bard
    level: 1
    DC: 16
  - name: daze
    source: Bard
    level: 0
    DC: 15
  - name: detect magic
    source: Bard
    level: 0
  - name: light
    source: Bard
    level: 0
  - name: mage hand
    source: Bard
    level: 0
  - name: prestidigitation
    source: Bard
    level: 0
  - name: read magic
    source: Bard
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 8
    concentration: 11
    slots:
      3: 3
      2: 5
      1: 5
      0: at-will
tactics:
  Before Combat: The bard posts political screeds in alleys, imbuing them with sepia
    snake sigils to trap those reading them. If anticipating combat, the bard drinks
    his potion of eagle's splendor.
  During Combat: The bard starts by casting haste and mirror image. He then shoots
    at opposing spellcasters or deafens them with sound burst.
  Base Statistics: Without eagle's splendor, the bard's statistics are Bard Spells
    Known reduce spell DCs by 2; Cha 17; Skills Bluff +10, Perform (dance) +14.
ability_scores:
  STR: 13
  DEX: 16
  CON: 10
  INT: 10
  WIS: 10
  CHA: 17
BAB: 6
CMB: 7
CMD: 22
feats:
- name: Dodge
- name: Mobility
- name: Point-Blank Shot
- name: Shot on the Run
skills:
  Acrobatics: 7
  Bluff: 12
  Climb: 10
  Escape Artist: 14
  Knowledge (arcane): 8
  Knowledge (local): 8
  Knowledge (nature): 8
  Knowledge (planes): 8
  Perception: 13
  Perform (dance): 16
  Sleight of Hand: 11
  Stealth: 14
languages:
- Common
- Elven
special_qualities:
- bardic knowledge +4
- elven magic
- lore master 1/day
- versatile performance (dance, comedy)
- weapon familiarity
gear:
  combat:
  - potions of cure moderate wounds (2)
  - potion of eagle's splendor
  - potion of invisibility
  other:
  - +1 leather armor
  - +1 longbow with 20 arrows
  - rapier
  - cloak of resistance +1
  - ring of protection +1
  - 45 gp
desc_long: Street artists are active in urban politics, a little crazy, or both. Their
  art and messages delight some, but annoy landowners whose buildings become the artists'
  medium.

---

# Street Artist

**Source** NPC Codex pg. 31
**XP** 3,200
Elf _[[classes/Bard|bard]]_ 8

CN Medium humanoid (elf)
**Init** +3; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +13

##### Defense

**AC** 18, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+3 armor, +1 _[[spells/Deflection|deflection]]_, +3 Dex, +1 _[[feats/Dodge|dodge]]_)
**hp** 43 (8d8+4)
**Fort** +3, **Ref** +10, **Will** +7; +2 vs. enchantments, +4 vs. bardic performance, language-dependent, and sonic
**Immune** sleep

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Rapier|rapier]]_ +7/+2 (1d6+1/18–20)
**Ranged** +1 _[[items/Weapon/Longbow|longbow]]_ +10/+5 (1d8+1/×3)
**Special Attacks** bardic performance 21 rounds/day (move action; countersong, dirge of _[[spells/Doom|doom]]_, _[[universal monster rules/Distraction|distraction]]_, fascinate, inspire competence +3, inspire courage +2, _[[spells/Suggestion|suggestion]]_)
**_Bard_ Spells Known **(CL 8th; concentration +11)
3rd (3/day)—_[[spells/Haste|haste]]_ (DC 18), _[[spells/Major Image|major image]]_ (DC 18), _[[spells/Sepia Snake Sigil|sepia snake sigil]]_ (DC 18)
2nd (5/day)—_[[spells/Invisibility|invisibility]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Shatter|shatter]]_, _[[spells/Sound Burst|sound burst]]_ (DC 16)
1st (5/day)—_[[spells/Animate Rope|animate rope]]_, _[[spells/Disguise Self|disguise self]]_, _[[spells/Grease|grease]]_, lesser _[[spells/Confusion|confusion]]_ (DC 14), _[[spells/Silent Image|silent image]]_ (DC 16)
0 (at will)—_[[spells/Daze|daze]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Read Magic|read magic]]_

### Tactics

**Before Combat **The _bard_ posts political screeds in alleys, imbuing them with sepia snake sigils to trap those reading them. If anticipating combat, the _bard_ drinks his potion of _[[monsters/Eagle|eagle]]_’s splendor.
**During Combat **The _bard_ starts by casting _haste_ and _mirror image_. He then shoots at opposing spellcasters or deafens them with _sound burst_.
**Base Statistics **Without _eagle_’s splendor, the _bard_’s statistics are **_Bard_ Spells Known **reduce spell DCs by 2; **Cha **17; **Skills **Bluff +10, Perform (dance) +14.

##### Statistics
**Str** 13, **Dex** 16, **Con** 10, **Int** 10, **Wis** 10, **Cha** 17
**Base Atk** +6; **CMB** +7; **CMD** 22
**Feats** _Dodge_, _[[feats/Mobility|Mobility]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Shot on the Run|Shot on the Run]]_
**Skills** Acrobatics +7, Bluff +12, _[[universal monster rules/Climb|Climb]]_ +10, Escape Artist +14, Knowledge (arcane, local, nature, planes) +8, Perception +13, Perform (dance) +16, Sleight of Hand +11, Stealth +14
**Languages** Common, Elven
**SQ** bardic knowledge +4, elven magic, lore master 1/day, versatile performance (dance, comedy), weapon familiarity
**Combat Gear** potions of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (2), potion of _eagle_’s splendor, potion of _invisibility_; **Other Gear** +1 _[[items/Armor/Leather armor|leather armor]]_, +1 _longbow_ with 20 arrows, _rapier_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 45 gp

Street artists are active in urban politics, a little crazy, or both. Their art and messages delight some, but annoy landowners whose buildings become the artists’ _medium_.
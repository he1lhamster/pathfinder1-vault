---
cssclass: [monsters]
title1: Tournament Champion
title2: Tournament Champion
CR: 12
sources:
- name: NPC Codex
  page: 201
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 19200
race: Half-elf
classes:
- bard 7
- sorcerer 2
- arcane archer 4
alignment: N
size: Medium
type: humanoid
subtypes:
- elf
- human
initiative:
  bonus: 7
senses:
  low-light vision: true
AC:
  AC: 21
  touch: 15
  flat_footed: 17
  components:
    armor: 6
    deflection: 1
    dex: 4
HP:
  HP: 86
  long: 7d8+2d6+4d10+22
saves:
  fort: 6
  ref: 15
  will: 11
  other: +2 vs. enchantments, +4 vs. bardic performance, language-dependent, and sonic
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk rapier +11/+6 (1d6/18-20)
      entries:
      - - damage: 1d6
          crit_range: 18-20
      attack: mwk rapier
      bonus:
      - 11
      - 6
  ranged:
  - - text: +2 longbow +21/+16 (1d8+2/×3)
      entries:
      - - damage: 1d8+2
          crit_multiplier: 3
      attack: +2 longbow
      bonus:
      - 21
      - 16
  special:
  - bardic performance 19 rounds/day (move action; countersong, distraction, fascinate,
    inspire competence +3, inspire courage +2, suggestion)
  - enhance arrows (elemental, magic)
  - imbue arrow
  - seeker arrow (1/day).
spells:
  entries:
  - name: greater invisibility
    source: Bard
    level: 4
  - name: shout
    source: Bard
    level: 4
    DC: 17
  - name: charm monster
    source: Bard
    level: 3
    DC: 16
  - name: crushing despair
    source: Bard
    level: 3
    DC: 16
  - name: cure serious wounds
    source: Bard
    level: 3
    DC: 16
  - name: deep slumber
    source: Bard
    level: 3
    DC: 16
  - name: cat's grace
    source: Bard
    level: 2
  - name: eagle's splendor
    source: Bard
    level: 2
  - name: invisibility
    source: Bard
    level: 2
  - name: shatter
    source: Bard
    level: 2
  - name: silence
    source: Bard
    level: 2
    DC: 15
  - name: charm person
    source: Bard
    level: 1
    DC: 14
  - name: feather fall
    source: Bard
    level: 1
  - name: grease
    source: Bard
    level: 1
  - name: lesser confusion
    source: Bard
    level: 1
    DC: 14
  - name: unseen servant
    source: Bard
    level: 1
  - name: dancing lights
    source: Bard
    level: 0
  - name: detect magic
    source: Bard
    level: 0
  - name: flare
    source: Bard
    level: 0
    DC: 13
  - name: mage hand
    source: Bard
    level: 0
  - name: mending
    source: Bard
    level: 0
  - name: prestidigitation
    source: Bard
    level: 0
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: true strike
    source: Sorcerer
    level: 1
  - name: arcane mark
    source: Sorcerer
    level: 0
  - name: daze
    source: Sorcerer
    level: 0
    DC: 13
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 13
  - name: open/close
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 10
    concentration: 13
    slots:
      4: 1
      3: 4
      2: 5
      1: 6
      0: at-will
  - name: Sorcerer
    type: known
    CL: 2
    concentration: 5
    failure_chance: 20%
    slots:
      1: 5
      0: at-will
    bloodline: arcane
tactics:
  Before Combat: The arcane archer casts cat's grace and drinks her potion of haste.
    She typically prepares shock arrows as her enhance arrows ability.
  During Combat: The archer's favorite tactic is to cast greater invisibility, then
    make shots from a distance using true strike.
  Base Statistics: Without cat's grace, the arcane archer's statistics are Init +5;
    Ref +13; Ranged +2 longbow +19/+14 (1d8+2/×3); Dex 20; CMD 26.
ability_scores:
  STR: 10
  DEX: 24
  CON: 13
  INT: 8
  WIS: 12
  CHA: 16
BAB: 10
CMB: 10
CMD: 28
feats:
- name: Deadly Aim
- name: Eschew Materials
- name: Far Shot
- name: Manyshot
- name: Point-Blank Shot
- name: Precise Shot
- name: Rapid Shot
- name: Skill Focus (Perception)
- name: Weapon Focus (longbow)
skills:
  Knowledge (geography): 6
  Knowledge (local): 8
  Knowledge (nobility): 8
  Perception: 25
  Perform (oratory): 19
  Perform (sing): 19
  Spellcraft: 3
  Swim: 0
  Use Magic Device: 7
languages:
- Common
- Elven
special_qualities:
- arcane bond (+2 longbow)
- bardic knowledge +3
- bloodline arcana (+1 DC for spells with metamagic feats that increase spell level)
- elf blood
- lore master 1/day
- versatile performance (oratory, sing)
gear:
  combat:
  - +1 human-bane arrow (2)
  - +1 magical beast-bane arrow (4)
  - potion of haste
  other:
  - +2 chain shirt
  - +2 longbow with 40 arrows
  - masterwork rapier
  - belt of incredible dexterity +2
  - cloak of resistance +1
  - lesser bracers of archery
  - ring of protection +1
  - 309 gp
desc_long: These half-elves travel from fair to fair, entertaining crowds with archery
  prowess, arcane flourishes, and epic ballads.

---

# Tournament Champion

**Source** NPC Codex pg. 201
**XP** 19,200
Half-elf _[[classes/Bard|bard]]_ 7/sorcerer 2/arcane archer 4

N Medium humanoid (elf, human)
**Init** +7; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +25

##### Defense

**AC** 21, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+6 armor, +1 _[[spells/Deflection|deflection]]_, +4 Dex)
**hp** 86 (7d8+2d6+4d10+22)
**Fort** +6, **Ref** +15, **Will** +11; +2 vs. enchantments, +4 vs. bardic performance, language-dependent, and sonic

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Rapier|rapier]]_ +11/+6 (1d6/18–20)
**Ranged** +2 _[[items/Weapon/Longbow|longbow]]_ +21/+16 (1d8+2/×3)
**Special Attacks** bardic performance 19 rounds/day (move action; countersong, _[[universal monster rules/Distraction|distraction]]_, fascinate, inspire competence +3, inspire courage +2, _[[spells/Suggestion|suggestion]]_), enhance arrows (elemental, magic), imbue arrow, seeker arrow (1/day).
**_Bard_ Spells Known** (CL 10th; concentration +13)
4th (1/day)—greater _[[spells/Invisibility|invisibility]]_, _[[spells/Shout|shout]]_ (DC 17)
 3rd (4/day)—_[[spells/Charm Monster|charm monster]]_ (DC 16), _[[spells/Crushing Despair|crushing despair]]_ (DC 16), _[[spells/Cure Serious Wounds|cure serious wounds]]_ (DC 16), _[[spells/Deep Slumber|deep slumber]]_ (DC 16)
 2nd (5/day)—_[[spells/Cat's Grace|cat's grace]]_, _[[spells/Eagle's Splendor|eagle's splendor]]_, _invisibility_, _[[spells/Shatter|shatter]]_, _[[spells/Silence|silence]]_ (DC 15)
 1st (6/day)—_[[spells/Charm Person|charm person]]_ (DC 14), _[[spells/Feather Fall|feather fall]]_, _[[spells/Grease|grease]]_, lesser _[[spells/Confusion|confusion]]_ (DC 14), _[[spells/Unseen Servant|unseen servant]]_
 0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 13), _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Prestidigitation|prestidigitation]]_
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known**(CL 2nd; concentration +5; arcane spell failure 20%)
1st (5/day)—_[[spells/Magic Missile|magic missile]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[spells/Daze|daze]]_ (DC 13), _[[spells/Ghost Sound|ghost sound]]_ (DC 13), open/close, _[[spells/Read Magic|read magic]]_
**Bloodline **arcane

### Tactics

**Before Combat **The arcane archer casts cat’s _[[spells/Grace|grace]]_ and drinks her potion of _[[spells/Haste|haste]]_. She typically prepares _[[items/Weapon Magic Abilities/Shock|shock]]_ arrows as her enhance arrows ability.
**During Combat **The archer’s favorite tactic is to cast greater _invisibility_, then make shots from a distance using _true strike_.
**Base Statistics **Without cat’s _grace_, the arcane archer’s statistics are **Init **+5; **Ref **+13; **Ranged** +2 _longbow_ +19/+14 (1d8+2/×3); **Dex **20; **CMD **26.

##### Statistics
**Str** 10, **Dex** 24, **Con** 13, **Int** 8, **Wis** 12, **Cha** 16
**Base Atk** +10; **CMB** +10; **CMD** 28
**Feats** _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Far Shot|Far Shot]]_, _[[feats/Manyshot|Manyshot]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Weapon Focus|Weapon Focus]]_ (_longbow_)
**Skills** Knowledge (geography) +6, Knowledge (local, nobility) +8, Perception +25, Perform (oratory, sing) +19, Spellcraft +3, Swim +0, Use Magic Device +7
**Languages** Common, Elven
**SQ** arcane bond (+2 _longbow_), bardic knowledge +3, bloodline arcana (+1 DC for spells with metamagic feats that increase spell level), elf blood, lore master 1/day, versatile performance (oratory, sing)
**Combat Gear** +1 human-bane arrow (2), +1 magical beast-bane arrow (4), potion of _haste_; **Other Gear** +2 _[[items/Armor/Chain shirt|chain shirt]]_, +2 _longbow_ with 40 arrows, masterwork _rapier_, _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, lesser bracers of archery, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 309 gp

These half-elves travel from fair to fair, entertaining crowds with archery prowess, arcane flourishes, and epic ballads.
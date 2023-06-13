---
cssclass: [monsters]
title1: Green Warden
title2: Green Warden
CR: 8
sources:
- name: NPC Codex
  page: 200
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 4800
race: Elf
classes:
- fighter 5
- conjurer 2
- arcane archer 2
alignment: N
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 5
senses:
  low-light vision: true
AC:
  AC: 19
  touch: 15
  flat_footed: 14
  components:
    armor: 4
    dex: 5
HP:
  HP: 51
  long: 5d10+2d6+2d10
saves:
  fort: 7
  ref: 9
  will: 10
  other: +2 vs. enchantments, +1 vs. fear
defensive_abilities:
- bravery +1
DR:
- amount: 10
  weakness: magic
  other: ranged weapon attack only; 30 points
immunities:
- sleep
speeds:
  base: 30
attacks:
  melee:
  - - text: +2 short sword +14/+9 (1d6+4/19-20)
      entries:
      - - damage: 1d6+4
          crit_range: 19-20
      attack: +2 short sword
      bonus:
      - 14
      - 9
  ranged:
  - - text: mwk composite longbow +18/+13 (1d8+5/×3)
      entries:
      - - damage: 1d8+5
          crit_multiplier: 3
      attack: mwk composite longbow
      bonus:
      - 18
      - 13
  special:
  - enhance arrows (magic)
  - imbue arrow
  - weapon training (bows +1)
spell_like_abilities:
  entries:
  - name: acid dart
    source: default
    freq: 4/day
  sources:
  - name: default
    CL: 3
    concentration: 4
spells:
  entries:
  - name: glitterdust
    source: Conjurer
    level: 2
    DC: 13
  - name: web
    source: Conjurer
    level: 2
    DC: 13
  - name: burning hands
    source: Conjurer
    level: 1
    count: 2
    DC: 12
  - name: color spray
    source: Conjurer
    level: 1
    count: 2
    DC: 12
  - name: bleed
    source: Conjurer
    level: 0
    DC: 11
  - name: dancing lights
    source: Conjurer
    level: 0
  - name: ghost sound
    source: Conjurer
    level: 0
    DC: 11
  - name: mage hand
    source: Conjurer
    level: 0
  sources:
  - name: Conjurer
    type: prepared
    CL: 3
    concentration: 4
    failure_chance: 15%
    slots:
      0: at-will
    opposition_schools:
    - divination
    - necromancy
tactics:
  Before Combat: The arcane archer attempts to start combat from a hard-to-reach spot,
    such as a high tree branch or steep elevation. He casts heroism and protection
    from arrows on himself from scrolls.
  During Combat: The archer keeps his distance and uses his magic arrows first. He
    casts glitterdust and web to slow down any approaching enemies, using imbue arrow
    to increase the range of such spells if needed. He uses Arcane Armor Training
    each round.
  Base Statistics: Without heroism and protection from arrows, the archer's base statistics
    are Senses Perception +12; Fort +5, Ref +7, Will +8; DR none; Melee +2 short sword
    +12/+7 (1d6+4/19-20); Ranged mwk composite longbow +16/+11 (1d8+5/×3); Skills
    Climb +8, Knowledge (arcana, nature) +7, Perception +12, Spellcraft +7 (+9 to
    identify magic item properties), Stealth +12, Swim +8.
ability_scores:
  STR: 14
  DEX: 21
  CON: 10
  INT: 12
  WIS: 13
  CHA: 8
BAB: 8
CMB: 10
CMD: 25
feats:
- name: Arcane Armor Training
- name: Iron Will
- name: Manyshot
- name: Point-Blank Shot
- name: Precise Shot
- name: Rapid Shot
- name: Scribe Scroll
- name: Weapon Focus (longbow)
- name: Weapon Specialization (longbow)
skills:
  Climb: 10
  Knowledge (arcana): 9
  Knowledge (nature): 9
  Perception: 14
  Spellcraft: 9
    to identify magic items: 11
  Stealth: 14
  Swim: 10
languages:
- Common
- Elven
- Goblin
special_qualities:
- arcane bond (masterwork composite longbow)
- armor training 1
- elven magic
- summoner's charm (1 round)
- weapon familiarity
gear:
  combat:
  - +1 frost arrows (5)
  - +1 human-bane arrows (5)
  - +1 shock arrows (5)
  - potion of cure moderate wounds
  - scroll of heroism
  - scrolls of invisibility (2)
  - scroll of protection from arrows
  other:
  - +1 studded leather
  - +2 short sword
  - masterwork composite longbow with 50 arrows
  - belt of incredible dexterity +2
  - spell component pouch
  - spellbook
  - 165 gp
desc_long: Protectors of the forest, green wardens are sworn to defend their sylvan
  homes from enemy encroachment, using magic arrows to kill from the trees' canopy.

---

# Green Warden

**Source** NPC Codex pg. 200
**XP** 4,800
Elf _[[classes/Fighter|fighter]]_ 5/conjurer 2/arcane archer 2

N Medium humanoid (elf)
**Init** +5; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +14

##### Defense

**AC** 19, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+4 armor, +5 Dex)
**hp** 51 (5d10+2d6+2d10)
**Fort** +7, **Ref** +9, **Will** +10; +2 vs. enchantments, +1 vs. _[[universal monster rules/Fear|fear]]_
**Defensive Abilities** bravery +1; **DR** 10/magic (ranged weapon attack only; 30 points); **Immune** sleep

##### Offense
**Speed** 30 ft.
**Melee** +2 _[[items/Weapon/Short sword|short sword]]_ +14/+9 (1d6+4/19–20)
**Ranged** mwk _[[items/Weapon/Composite longbow|composite longbow]]_ +18/+13 (1d8+5/×3)
**Special Attacks** enhance arrows (magic), imbue arrow, weapon _[[items/Weapon Magic Abilities/Training|training]]_ (bows +1)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd; concentration +4)
4/day—acid _[[items/Weapon/Dart|dart]]_
**Conjurer Spells Prepared **(CL 3rd; concentration +4; arcane spell failure 15%)
2nd—_[[spells/Glitterdust|glitterdust]]_ (DC 13), web (DC 13)
1st—_[[spells/Burning Hands|burning hands]]_ (2, DC 12), _[[spells/Color Spray|color spray]]_ (2, DC 12)
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 11), _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 11), _[[spells/Mage Hand|mage hand]]_
**Opposition Schools **_[[spells/Divination|divination]]_, necromancy

### Tactics

**Before Combat **The arcane archer attempts to start combat from a hard-to-reach spot, such as a high tree branch or steep elevation. He casts _[[spells/Heroism|heroism]]_ and _[[spells/Protection From Arrows|protection from arrows]]_ on himself from scrolls.
**During Combat **The archer keeps his distance and uses his magic arrows first. He casts _glitterdust_ and web to _[[spells/Slow|slow]]_ down any approaching enemies, using imbue arrow to increase the range of such spells if needed. He uses _[[feats/Arcane Armor Training|Arcane Armor Training]]_ each round.
**Base Statistics **Without _heroism_ and _protection from arrows_, the archer’s base statistics are **Senses **Perception +12; **Fort **+5, **Ref **+7, **Will **+8; **DR **none; **Melee** +2 _short sword_ +12/+7 (1d6+4/19–20); **Ranged **mwk _composite longbow_ +16/+11 (1d8+5/×3); **Skills **_[[universal monster rules/Climb|Climb]]_ +8, Knowledge (arcana, nature) +7, Perception +12, Spellcraft +7 (+9 to _[[spells/Identify|identify]]_ magic item properties), Stealth +12, Swim +8.

##### Statistics
**Str** 14, **Dex** 21, **Con** 10, **Int** 12, **Wis** 13, **Cha** 8
**Base Atk** +8; **CMB** +10; **CMD** 25
**Feats** _Arcane Armor Training_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Manyshot|Manyshot]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_[[items/Weapon/Longbow|longbow]]_), _[[feats/Weapon Specialization|Weapon Specialization]]_ (_longbow_)
**Skills** _Climb_ +10, Knowledge (arcana, nature) +9, Perception +14, Spellcraft +9 (+11 to _identify_ magic items), Stealth +14, Swim +10
**Languages** Common, Elven, _[[monsters/Goblin|Goblin]]_
**SQ** arcane bond (masterwork _composite longbow_), armor _training_ 1, elven magic, _[[classes/Summoner|summoner]]_’s charm (1 round), weapon familiarity
**Combat Gear** +1 frost arrows (5), +1 human-bane arrows (5), +1 _[[items/Weapon Magic Abilities/Shock|shock]]_ arrows (5), potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, scroll of _heroism_, scrolls of _[[spells/Invisibility|invisibility]]_ (2), scroll of _protection from arrows_; **Other Gear** +1 studded leather, +2 _short sword_, masterwork _composite longbow_ with 50 arrows, _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, _[[items/Mundane/Spellbook|spellbook]]_, 165 gp

Protectors of the forest, green wardens are sworn to defend their sylvan homes from enemy encroachment, using magic arrows to kill from the trees’ canopy.
---
cssclass: [monsters]
title1: Rider of the Steppe
title2: Rider of the Steppe
CR: 13
sources:
- name: NPC Codex
  page: 121
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 25600
race: Half-elf
classes:
- paladin 14
alignment: LG
size: Medium
type: humanoid
subtypes:
- elf
- human
initiative:
  bonus: 6
senses:
  low-light vision: true
auras:
- name: courage
  radius: 10
- name: faith
  radius: 10
- name: justice
  radius: 10
- name: resolve
  radius: 10
AC:
  AC: 23
  touch: 14
  flat_footed: 20
  components:
    armor: 8
    deflection: 1
    dex: 3
    natural: 1
HP:
  HP: 95
  long: 14d10+14
saves:
  fort: 13
  ref: 13
  will: 11
  other: +2 vs. enchantments
immunities:
- charm
- disease
- fear
- sleep
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 longsword +17/+12/+7 (1d8+3/19-20)
      entries:
      - - damage: 1d8+3
          crit_range: 19-20
      attack: +1 longsword
      bonus:
      - 17
      - 12
      - 7
  ranged:
  - - text: +2 composite longbow +22/+17/+12 (1d8+4/×3)
      entries:
      - - damage: 1d8+4
          crit_multiplier: 3
      attack: +2 composite longbow
      bonus:
      - 22
      - 17
      - 12
  special:
  - channel positive energy (DC 18, 7d6)
  - smite evil 5/day (+1 attack and AC, +14 damage)
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: At will
  sources:
  - name: default
    CL: 14
    concentration: 15
spells:
  entries:
  - name: heal mount
    source: Paladin
    level: 3
  - name: eagle's splendor
    source: Paladin
    level: 2
  - name: resist energy
    source: Paladin
    level: 2
  - name: create water
    source: Paladin
    level: 1
  - name: divine favor
    source: Paladin
    level: 1
    count: 2
  - name: endure elements
    source: Paladin
    level: 1
  sources:
  - name: Paladin
    type: prepared
    CL: 11
    concentration: 12
tactics:
  During Combat: The paladin tries to remain out of melee range and attack enemies
    with her bow.
ability_scores:
  STR: 14
  DEX: 22
  CON: 12
  INT: 10
  WIS: 8
  CHA: 13
BAB: 14
CMB: 16
CMD: 33
feats:
- name: Improved Precise Shot
- name: Manyshot
- name: Mounted Archery
- name: Mounted Combat
- name: Point-Blank Shot
- name: Precise Shot
- name: Rapid Shot
- name: Skill Focus (Perception)
skills:
  Heal: 5
  Intimidate: 6
  Knowledge (geography): 5
  Knowledge (local): 5
  Perception: 9
  Ride: 10
  Stealth: 13
  Survival: 4
languages:
- Common
- Elven
- Goblin
special_qualities:
- aura
- code of conduct
- divine bond (mount)
- elf blood
- lay on hands (7d6, 8/day)
- mercies (blinded, cursed, diseased, fatigued),
gear:
  combat:
  - +1 evil outsider-bane arrows (5)
  - +1 magical beast-bane arrows (5)
  - potion of haste
  - potion of invisibility
  other:
  - +2 mithral breastplate
  - +2 composite longbow (+2 Str) with 30 arrows
  - +1 longsword
  - amulet of natural armor +1
  - belt of incredible dexterity +2
  - cloak of resistance +2
  - ring of protection +1
  - 823 gp
desc_long: A rider of the steppe works individually or in a group to bring safety
  and law to the wild and arid flatlands, often protecting caravans and traveling
  dignitaries.

---

# Rider of the Steppe

**Source** NPC Codex pg. 121
**XP** 25,600
Half-elf _[[classes/Paladin|paladin]]_ 14

LG Medium humanoid (elf, human)
**Init** +6; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +9
**Aura** courage (10 ft.), faith (10 ft.), justice (10 ft.), resolve (10 ft.)

##### Defense

**AC** 23, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+8 armor, +1 _[[spells/Deflection|deflection]]_, +3 Dex, +1 natural)
**hp** 95 (14d10+14)
**Fort** +13, **Ref** +13, **Will** +11; +2 vs. enchantments
**Immune** charm, disease, _[[universal monster rules/Fear|fear]]_, sleep

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon/Longsword|longsword]]_ +17/+12/+7 (1d8+3/19–20)
**Ranged** +2 _[[items/Weapon/Composite longbow|composite longbow]]_ +22/+17/+12 (1d8+4/×3)
**Special Attacks** channel positive energy (DC 18, 7d6), smite evil 5/day (+1 attack and AC, +14 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +15)
At will—_[[spells/Detect Evil|detect evil]]_
**_Paladin_ Spells Prepared **(CL 11th; concentration +12)
3rd—_[[spells/Heal Mount|heal mount]]_
2nd—_[[monsters/Eagle|eagle]]_’s splendor, _[[spells/Resist Energy|resist energy]]_
1st—_[[spells/Create Water|create water]]_, _[[spells/Divine Favor|divine favor]]_ (2), _[[spells/Endure Elements|endure elements]]_

### Tactics

**During Combat **The _paladin_ tries to remain out of melee range and attack enemies with her bow.

##### Statistics
**Str** 14, **Dex** 22, **Con** 12, **Int** 10, **Wis** 8, **Cha** 13
**Base Atk** +14; **CMB** +16; **CMD** 33
**Feats** _[[feats/Improved Precise Shot|Improved Precise Shot]]_, _[[feats/Manyshot|Manyshot]]_, _[[feats/Mounted Archery|Mounted Archery]]_, _[[feats/Mounted Combat|Mounted Combat]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** _[[spells/Heal|Heal]]_ +5, Intimidate +6, Knowledge (geography, local) +5, Perception +9, Ride +10, Stealth +13, Survival +4
**Languages** Common, Elven, _[[monsters/Goblin|Goblin]]_
**SQ** aura, code of conduct, divine bond (_[[spells/Mount|mount]]_), elf blood, lay on hands (7d6, 8/day), mercies (_[[conditions/Blinded|blinded]]_, cursed, diseased, _[[conditions/Fatigued|fatigued]]_),
**Combat Gear** +1 evil outsider-bane arrows (5), +1 magical beast-bane arrows (5), potion of _[[spells/Haste|haste]]_, potion of _[[spells/Invisibility|invisibility]]_; **Other Gear** +2 mithral _[[items/Armor/Breastplate|breastplate]]_, +2 _composite longbow_ (+2 Str) with 30 arrows, +1 _longsword_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 823 gp

A _[[npcs/Rider of the Steppe|rider of the steppe]]_ works individually or in a group to bring safety and law to the wild and arid flatlands, often protecting caravans and traveling dignitaries.
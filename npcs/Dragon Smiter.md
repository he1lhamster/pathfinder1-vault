---
cssclass: [monsters]
title1: Dragon Smiter
title2: Dragon Smiter
CR: 12
sources:
- name: NPC Codex
  page: 120
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 19200
race: Human
classes:
- paladin of Iomedae 13
alignment: LG
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 1
auras:
- name: courage
  radius: 10
- name: justice
  radius: 10
- name: resolve
  radius: 10
AC:
  AC: 23
  touch: 11
  flat_footed: 22
  components:
    armor: 11
    dex: 1
    natural: 1
HP:
  HP: 115
  long: 13d10+39
saves:
  fort: 13
  ref: 10
  will: 10
immunities:
- charm
- disease
- fear
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 dragon-bane greatsword +21/+16/+11 (2d6+10/19-20)
      entries:
      - - damage: 2d6+10
          crit_range: 19-20
      attack: +1 dragon-bane greatsword
      bonus:
      - 21
      - 16
      - 11
  ranged:
  - - text: mwk heavy crossbow +15 (1d10/19-20)
      entries:
      - - damage: 1d10
          crit_range: 19-20
      attack: mwk heavy crossbow
      bonus:
      - 15
  special:
  - channel positive energy (DC 17, 7d6)
  - smite evil 5/day (+1 attack and AC, +13 damage)
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: At will
  sources:
  - name: default
    CL: 13
    concentration: 14
spells:
  entries:
  - name: prayer
    source: Paladin
    level: 3
  - name: eagle's splendor
    source: Paladin
    level: 2
  - name: resist energy
    source: Paladin
    level: 2
  - name: bless
    source: Paladin
    level: 1
    count: 2
  - name: divine favor
    source: Paladin
    level: 1
    count: 2
  sources:
  - name: Paladin
    type: prepared
    CL: 10
    concentration: 11
tactics:
  Before Combat: The paladin casts resist energy against the breath weapon energy
    type of dragons he expects to fight.
  During Combat: The paladin casts eagle's splendor to improve his smite and divine
    grace. He uses Improved Vital Strike and Lunge to land solid hits on creatures
    with reach.
ability_scores:
  STR: 22
  DEX: 12
  CON: 14
  INT: 10
  WIS: 8
  CHA: 13
BAB: 13
CMB: 19
CMD: 30
feats:
- name: Cleave
- name: Great Cleave
- name: Improved Vital Strike
- name: Lightning Reflexes
- name: Lunge
- name: Power Attack
- name: Vital Strike
- name: Weapon Focus (greatsword)
skills:
  Diplomacy: 9
  Heal: 7
  Knowledge (arcana): 8
  Knowledge (religion): 8
  Linguistics: 1
  Perception: 9
  Sense Motive: 7
languages:
- Common
- Draconic
special_qualities:
- aura
- code of conduct
- divine bond (weapon +3, 3/day)
- lay on hands (6d6, 7/day)
- mercies (frightened, paralyzed, shaken, staggered)
gear:
  combat:
  - +1 dragon-bane bolts (5)
  - potion of displacement
  other:
  - +2 full plate
  - +1 dragon-bane greatsword
  - masterwork heavy crossbow with 10 bolts
  - amulet of natural armor +1
  - belt of giant strength +2
  - cloak of resistance +2
  - silver holy symbol
  - 1,044 gp
desc_long: A dragon smiter is sworn to slay dragons.

---

# Dragon Smiter

**Source** NPC Codex pg. 120
**XP** 19,200
Human _[[classes/Paladin|paladin]]_ of Iomedae 13

LG Medium humanoid (human)
**Init** +1; **Senses** Perception +9
**Aura** courage (10 ft.), justice (10 ft.), resolve (10 ft.)

##### Defense

**AC** 23, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+11 armor, +1 Dex, +1 natural)
**hp** 115 (13d10+39)
**Fort** +13, **Ref** +10, **Will** +10
**Immune** charm, disease, _[[universal monster rules/Fear|fear]]_

##### Offense
**Speed** 20 ft.
**Melee** +1 dragon-bane _[[items/Weapon/Greatsword|greatsword]]_ +21/+16/+11 (2d6+10/19–20)
**Ranged** mwk _[[items/Weapon/Heavy crossbow|heavy crossbow]]_ +15 (1d10/19–20)
**Special Attacks** channel positive energy (DC 17, 7d6), smite evil 5/day (+1 attack and AC, +13 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +14)
At will—_[[spells/Detect Evil|detect evil]]_
**_Paladin_ Spells Prepared **(CL 10th; concentration +11)
3rd—_[[spells/Prayer|prayer]]_
2nd—_[[monsters/Eagle|eagle]]_’s splendor, _[[spells/Resist Energy|resist energy]]_
1st—_[[spells/Bless|bless]]_ (2), _[[spells/Divine Favor|divine favor]]_ (2)

### Tactics

**Before Combat **The _paladin_ casts _resist energy_ against the _[[universal monster rules/Breath Weapon|breath weapon]]_ energy type of dragons he expects to fight.
**During Combat **The _paladin_ casts _eagle_’s splendor to improve his smite and divine _[[spells/Grace|grace]]_. He uses _[[feats/Improved Vital Strike|Improved Vital Strike]]_ and _[[feats/Lunge|Lunge]]_ to land solid hits on creatures with reach.

##### Statistics
**Str** 22, **Dex** 12, **Con** 14, **Int** 10, **Wis** 8, **Cha** 13
**Base Atk** +13; **CMB** +19; **CMD** 30
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Great Cleave|Great Cleave]]_, _Improved Vital Strike_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _Lunge_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_greatsword_)
**Skills** Diplomacy +9, _[[spells/Heal|Heal]]_ +7, Knowledge (arcana, religion) +8, Linguistics +1, Perception +9, Sense Motive +7
**Languages** Common, Draconic
**SQ** aura, code of conduct, divine bond (weapon +3, 3/day), lay on hands (6d6, 7/day), mercies (_[[conditions/Frightened|frightened]]_, _[[conditions/Paralyzed|paralyzed]]_, _[[conditions/Shaken|shaken]]_, _[[conditions/Staggered|staggered]]_)
**Combat Gear** +1 dragon-bane bolts (5), potion of _[[spells/Displacement|displacement]]_; **Other Gear** +2 _[[items/Armor/Full plate|full plate]]_, +1 dragon-bane _greatsword_, masterwork _heavy crossbow_ with 10 bolts, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, silver holy symbol, 1,044 gp

A _[[npcs/Dragon Smiter|dragon smiter]]_ is sworn to slay dragons.
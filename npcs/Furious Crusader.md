---
cssclass: [monsters]
title1: Furious Crusader
title2: Furious Crusader
CR: 17
sources:
- name: NPC Codex
  page: 125
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 102400
race: Halfling
classes:
- paladin of Iomedae 18
alignment: LG
size: Small
type: humanoid
subtypes:
- halfling
initiative:
  bonus: 1
auras:
- name: courage
  radius: 10
- name: faith
  radius: 10
- name: justice
  radius: 10
- name: resolve
  radius: 10
- name: righteousness
  radius: 10
AC:
  AC: 30
  touch: 15
  flat_footed: 29
  components:
    armor: 13
    deflection: 3
    dex: 1
    natural: 2
    size: 1
HP:
  HP: 139
  long: 18d10+36
saves:
  fort: 18
  ref: 12
  will: 17
  other: +2 vs. fear
DR:
- amount: 5
  weakness: evil
immunities:
- charm
- compulsion
- disease
- fear
speeds:
  base: 30
attacks:
  melee:
  - - text: +3 flaming longspear +27/+22/+17/+12 (1d6+9/×3 plus 1d6 fire)
      entries:
      - - damage: 1d6+9
          crit_multiplier: 3
        - damage: 1d6
          type: fire
      attack: +3 flaming longspear
      bonus:
      - 27
      - 22
      - 17
      - 12
  ranged:
  - - text: +1 sling +21 (1d3+5)
      entries:
      - - damage: 1d3+5
      attack: +1 sling
      bonus:
      - 21
  special:
  - channel positive energy (DC 22, 9d6)
  - smite evil 6/day (+3 attack and AC, +18 damage)
space: 5
reach: 5
reach_other: 10 ft. with longspear
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: At will
  sources:
  - name: default
    CL: 18
    concentration: 21
spells:
  entries:
  - name: death ward
    source: Paladin
    level: 4
  - name: dispel evil
    source: Paladin
    level: 4
  - name: greater magic weapon
    source: Paladin
    level: 3
  - name: magic circle against evil
    source: Paladin
    level: 3
  - name: prayer
    source: Paladin
    level: 3
  - name: delay poison
    source: Paladin
    level: 2
    count: 2
  - name: resist energy
    source: Paladin
    level: 2
    count: 2
  - name: bless
    source: Paladin
    level: 1
    count: 2
  - name: bless weapon
    source: Paladin
    level: 1
    count: 2
  - name: divine favor
    source: Paladin
    level: 1
  sources:
  - name: Paladin
    type: prepared
    CL: 15
    concentration: 18
tactics:
  Before Combat: The paladin casts greater magic weapon on his longspear.
  During Combat: The paladin reserves most of his spells and magic items for helping
    allies against a common foe. He uses Cleave as often as possible against grouped
    opponents, and Lunge and Stand Still to control the movement of multiple enemies.
    He uses his divine bond to give his longspear the defending, holy, keen, or speed
    special ability.
  Base Statistics: Without greater magic weapon, the paladin's statistics are Melee
    +1 flaming longspear +25/+20/+15/+10 (1d6+7/×3 plus 1d6 fire).
ability_scores:
  STR: 18
  DEX: 12
  CON: 14
  INT: 8
  WIS: 12
  CHA: 16
BAB: 18
CMB: 21
CMD: 35
feats:
- name: Cleave
- name: Combat Reflexes
- name: Greater Vital Strike
- name: Improved Vital Strike
- name: Lunge
- name: Power Attack
- name: Stand Still
- name: Vital Strike
- name: Weapon Focus (longspear)
skills:
  Acrobatics: -2
    when jumping: -1
  Climb: 4
  Diplomacy: 11
  Heal: 9
  Knowledge (local): 4
  Knowledge (religion): 7
  Perception: 13
  Swim: 2
languages:
- Common
- Halfling
special_qualities:
- aura
- code of conduct
- divine bond (weapon +5, 4/day)
- lay on hands (9d6, 12/day)
- mercies (blinded, cursed, diseased, paralyzed, sickened, stunned)
gear:
  combat:
  - +1 holy bullets (10)
  - +1 undead-bane bullets (10)
  - potions of haste (2)
  - wand of cure light wounds (50 charges)
  other:
  - +4 full plate
  - +1 flaming longspear
  - +1 sling with 20 bullets
  - amulet of natural armor +2
  - belt of giant strength +2
  - boots of striding and springing
  - cloak of resistance +1
  - ring of protection +3
  - 8,735 gp
desc_long: The furious crusader is a compact bundle of holy power with a chip on his
  shoulder.

---

# Furious Crusader

**Source** NPC Codex pg. 125
**XP** 102,400
Halfling _[[classes/Paladin|paladin]]_ of Iomedae 18

LG Small humanoid (halfling)
**Init** +1; **Senses** Perception +13
**Aura** courage (10 ft.), faith (10 ft.), justice (10 ft.), resolve (10 ft.), righteousness (10 ft.)

##### Defense

**AC** 30, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 29 (+13 armor, +3 deflection, +1 Dex, +2 natural, +1 size)
**hp** 139 (18d10+36)
**Fort** +18, **Ref** +12, **Will** +17; +2 vs. _[[universal monster rules/Fear|fear]]_
**DR** 5/evil; **Immune** charm, compulsion, disease, _fear_

##### Offense
**Speed** 30 ft.
**Melee** +3 _[[items/Weapon Magic Abilities/Flaming|flaming]]_ _[[items/Weapon/Longspear|longspear]]_ +27/+22/+17/+12 (1d6+9/×3 plus 1d6 fire)
**Ranged** +1 _[[items/Weapon/Sling|sling]]_ +21 (1d3+5)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with _longspear_)
**Special Attacks** channel positive energy (DC 22, 9d6), smite evil 6/day (+3 attack and AC, +18 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +21)
At will—_[[spells/Detect Evil|detect evil]]_
**_Paladin_ Spells Prepared **(CL 15th; concentration +18)
4th—_[[spells/Death Ward|death ward]]_, _[[spells/Dispel Evil|dispel evil]]_
3rd—greater _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Magic Circle against Evil|magic circle against evil]]_, _[[spells/Prayer|prayer]]_
2nd—_[[spells/Delay Poison|delay poison]]_ (2), _[[spells/Resist Energy|resist energy]]_ (2)
1st—_[[spells/Bless|bless]]_ (2), _[[spells/Bless Weapon|bless weapon]]_ (2), _[[spells/Divine Favor|divine favor]]_

### Tactics

**Before Combat **The _paladin_ casts greater _magic weapon_ on his _longspear_.
**During Combat **The _paladin_ reserves most of his spells and magic items for helping allies against a common foe. He uses _[[feats/Cleave|Cleave]]_ as often as possible against grouped opponents, and _[[feats/Lunge|Lunge]]_ and _[[feats/Stand Still|Stand Still]]_ to control the movement of multiple enemies. He uses his divine bond to give his _longspear_ the _[[items/Weapon Magic Abilities/Defending|defending]]_, holy, _[[items/Weapon Magic Abilities/Keen|keen]]_, or speed special ability.
**Base Statistics **Without greater _magic weapon_, the _paladin_’s statistics are **Melee** +1 _flaming_ _longspear_ +25/+20/+15/+10 (1d6+7/×3 plus 1d6 fire).

##### Statistics
**Str** 18, **Dex** 12, **Con** 14, **Int** 8, **Wis** 12, **Cha** 16
**Base Atk** +18; **CMB** +21; **CMD** 35
**Feats** _Cleave_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _Lunge_, _[[feats/Power Attack|Power Attack]]_, _Stand Still_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_longspear_)
**Skills** Acrobatics –2 (–1 when jumping), _[[universal monster rules/Climb|Climb]]_ +4, Diplomacy +11, _[[spells/Heal|Heal]]_ +9, Knowledge (local) +4, Knowledge (religion) +7, Perception +13, Swim +2
**Languages** Common, Halfling
**SQ** aura, code of conduct, divine bond (weapon +5, 4/day), lay on hands (9d6, 12/day), mercies (_[[conditions/Blinded|blinded]]_, cursed, diseased, _[[conditions/Paralyzed|paralyzed]]_, _[[conditions/Sickened|sickened]]_, _[[conditions/Stunned|stunned]]_)
**Combat Gear** +1 holy bullets (10), +1 undead-bane bullets (10), potions of _[[spells/Haste|haste]]_ (2), wand of _[[spells/Cure Light Wounds|cure light wounds]]_ (50 charges); **Other Gear** +4 _[[items/Armor/Full plate|full plate]]_, +1 _flaming_ _longspear_, +1 _sling_ with 20 bullets, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, _[[items/Wondrous Item/Boots of Striding and Springing|boots of striding and springing]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +3|ring of protection +3]]_, 8,735 gp

The _[[npcs/Furious Crusader|furious crusader]]_ is a compact bundle of holy power with a chip on his shoulder.
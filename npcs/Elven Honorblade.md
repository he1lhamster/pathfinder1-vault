---
cssclass: [monsters]
title1: Elven Honorblade
title2: Elven Honorblade
CR: 10
sources:
- name: NPC Codex
  page: 118
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 9600
race: Elf
classes:
- paladin 11
alignment: LG
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 3
senses:
  low-light vision: true
auras:
- name: courage
  radius: 10
- name: justice
  radius: 10
- name: resolve
  radius: 10
AC:
  AC: 22
  touch: 15
  flat_footed: 18
  components:
    armor: 6
    deflection: 1
    dex: 3
    dodge: 1
    natural: 1
HP:
  HP: 76
  long: 11d10+11
saves:
  fort: 10
  ref: 9
  will: 9
  other: +2 vs. enchantments
immunities:
- charm
- disease
- fear
- poison
- sleep
resistances:
  fire: 20
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 elven curve blade +15/+10/+5 (1d10+5/15-20)
      entries:
      - - damage: 1d10+5
          crit_range: 15-20
      attack: +1 elven curve blade
      bonus:
      - 15
      - 10
      - 5
  ranged:
  - - text: mwk longbow +15/+10/+5 (1d8/×3)
      entries:
      - - damage: 1d8
          crit_multiplier: 3
      attack: mwk longbow
      bonus:
      - 15
      - 10
      - 5
  special:
  - channel positive energy (DC 17, 6d6)
  - smite evil 4/day (+2 attack and AC, +11 damage)
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: At will
  sources:
  - name: default
    CL: 11
    concentration: 13
spells:
  entries:
  - name: prayer
    source: Paladin
    level: 3
  - name: delay poison
    source: Paladin
    level: 2
  - name: resist energy
    source: Paladin
    level: 2
  - name: bless
    source: Paladin
    level: 1
  - name: divine favor
    source: Paladin
    level: 1
  - name: lesser restoration
    source: Paladin
    level: 1
  sources:
  - name: Paladin
    type: prepared
    CL: 8
    concentration: 10
tactics:
  Before Combat: The paladin casts delay poison and resist energy (fire).
  During Combat: The paladin uses Mobility, Spring Attack, and Whirlwind Attack to
    engage and destroy multiple opponents at once. He normally uses his divine bond
    to give his weapon the flaming and holy special abilities, but if his foes are
    spread out, he gives it speed instead.
  Base Statistics: Without resist energy, the paladin's statistics are Immune charm,
    disease, fear, sleep; Resist none.
ability_scores:
  STR: 17
  DEX: 16
  CON: 10
  INT: 13
  WIS: 8
  CHA: 14
BAB: 11
CMB: 14
CMD: 29
feats:
- name: Combat Expertise
- name: Dodge
- name: Improved Critical (elven curve blade)
- name: Mobility
- name: Spring Attack
- name: Whirlwind Attack
skills:
  Diplomacy: 10
  Heal: 3
  Knowledge (nature): 3
  Perception: 11
  Stealth: 12
  Survival: 4
languages:
- Common
- Elven
- Sylvan
special_qualities:
- aura
- code of conduct
- divine bond (weapon +3, 2/day)
- elven magic
- lay on hands (5d6, 7/day)
- mercies (poisoned, sickened, staggered)
- weapon familiarity
gear:
  gear:
  - +2 chain shirt
  - +1 elven curve blade
  - masterwork longbow with 20 arrows
  - amulet of natural armor +1
  - belt of giant strength +2
  - cloak of resistance +1
  - ring of protection +1
  - silver holy symbol
  - 319 gp
desc_long: An elven honorblade guards pristine forests and hunts evil beasts that
  would despoil nature.

---

# Elven Honorblade

**Source** NPC Codex pg. 118
**XP** 9,600
Elf _[[classes/Paladin|paladin]]_ 11

LG Medium humanoid (elf)
**Init** +3; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +11
**Aura** courage (10 ft.), justice (10 ft.), resolve (10 ft.)

##### Defense

**AC** 22, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+6 armor, +1 _[[spells/Deflection|deflection]]_, +3 Dex, +1 _[[feats/Dodge|dodge]]_, +1 natural)
**hp** 76 (11d10+11)
**Fort** +10, **Ref** +9, **Will** +9; +2 vs. enchantments
**Immune** charm, disease, _[[universal monster rules/Fear|fear]]_, poison, sleep; **Resist** fire 20

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon/Elven curve blade|elven curve blade]]_ +15/+10/+5 (1d10+5/15–20)
**Ranged** mwk _[[items/Weapon/Longbow|longbow]]_ +15/+10/+5 (1d8/×3)
**Special Attacks** channel positive energy (DC 17, 6d6), smite evil 4/day (+2 attack and AC, +11 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +13)
At will—_[[spells/Detect Evil|detect evil]]_
**_Paladin_ Spells Prepared **(CL 8th; concentration +10)
3rd—_[[spells/Prayer|prayer]]_
2nd—_[[spells/Delay Poison|delay poison]]_, _[[spells/Resist Energy|resist energy]]_
1st—_[[spells/Bless|bless]]_, _[[spells/Divine Favor|divine favor]]_, lesser _[[spells/Restoration|restoration]]_

### Tactics

**Before Combat **The _paladin_ casts _delay poison_ and _resist energy_ (fire).
**During Combat **The _paladin_ uses _[[feats/Mobility|Mobility]]_, _[[feats/Spring Attack|Spring Attack]]_, and _[[feats/Whirlwind Attack|Whirlwind Attack]]_ to engage and destroy multiple opponents at once. He normally uses his divine bond to give his weapon the _[[items/Weapon Magic Abilities/Flaming|flaming]]_ and holy special abilities, but if his foes are spread out, he gives it speed instead.
**Base Statistics **Without _resist energy_, the _paladin_’s statistics are **Immune **charm, disease, _fear_, sleep; **Resist **none.

##### Statistics
**Str** 17, **Dex** 16, **Con** 10, **Int** 13, **Wis** 8, **Cha** 14
**Base Atk** +11; **CMB** +14; **CMD** 29
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (_elven curve blade_), _Mobility_, _Spring Attack_, _Whirlwind Attack_
**Skills** Diplomacy +10, _[[spells/Heal|Heal]]_ +3, Knowledge (nature) +3, Perception +11, Stealth +12, Survival +4
**Languages** Common, Elven, Sylvan
**SQ** aura, code of conduct, divine bond (weapon +3, 2/day), elven magic, lay on hands (5d6, 7/day), mercies (poisoned, _[[conditions/Sickened|sickened]]_, _[[conditions/Staggered|staggered]]_), weapon familiarity
**Gear** +2 _[[items/Armor/Chain shirt|chain shirt]]_, +1 _elven curve blade_, masterwork _longbow_ with 20 arrows, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, silver holy symbol, 319 gp

An _[[npcs/Elven Honorblade|elven honorblade]]_ guards pristine forests and hunts evil beasts that would despoil nature.
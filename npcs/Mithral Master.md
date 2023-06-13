---
cssclass: [monsters]
title1: Mithral Master
title2: Mithral Master
CR: 18
sources:
- name: NPC Codex
  page: 126
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 153600
race: Half-elf
classes:
- paladin of Abadar 19
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
- name: righteousness
  radius: 10
AC:
  AC: 31
  touch: 16
  flat_footed: 29
  components:
    armor: 10
    deflection: 4
    dex: 2
    natural: 2
    shield: 3
HP:
  HP: 185
  long: 19d10+76
saves:
  fort: 20
  ref: 13
  will: 15
  other: +2 vs. enchantments
DR:
- amount: 5
  weakness: evil
immunities:
- charm
- compulsion
- disease
- fear
- poison
- sleep
resistances:
  fire: 30
speeds:
  base: 30
attacks:
  melee:
  - - text: +4 axiomatic longsword +29/+24/+19/+14 (1d8+9/17-20)
      entries:
      - - damage: 1d8+9
          crit_range: 17-20
      attack: +4 axiomatic longsword
      bonus:
      - 29
      - 24
      - 19
      - 14
  - - text: +1 lance +26/+21/+16/+11 (1d8+6/19-20/×3)
      entries:
      - - damage: 1d8+6
          crit_range: 19-20
          crit_multiplier: 3
      attack: +1 lance
      bonus:
      - 26
      - 21
      - 16
      - 11
  special:
  - channel positive energy (DC 22, 10d6)
  - smite evil 7/day (+3 attack and AC, +19 damage)
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: At will
  sources:
  - name: default
    CL: 19
    concentration: 22
spells:
  entries:
  - name: death ward
    source: Paladin
    level: 4
  - name: neutralize poison
    source: Paladin
    level: 4
  - name: daylight
    source: Paladin
    level: 3
  - name: greater magic weapon
    source: Paladin
    level: 3
  - name: prayer
    source: Paladin
    level: 3
  - name: remove blindness
    source: Paladin
    level: 3
  - name: delay poison
    source: Paladin
    level: 2
  - name: eagle's splendor
    source: Paladin
    level: 2
    count: 2
  - name: resist energy
    source: Paladin
    level: 2
  - name: bless
    source: Paladin
    level: 1
  - name: create water
    source: Paladin
    level: 1
  - name: divine favor
    source: Paladin
    level: 1
    count: 2
  - name: lesser restoration
    source: Paladin
    level: 1
  sources:
  - name: Paladin
    type: prepared
    CL: 16
    concentration: 19
tactics:
  Before Combat: The paladin casts delay poison and resist energy (fire) on himself
    and greater magic weapon on his longsword.
  During Combat: The paladin fights on horseback or on foot as the situation warrants.
    He casts eagle's splendor to enhance his smite evil attacks, but otherwise relies
    on standard melee tactics and healing himself with lay on hands.
  Base Statistics: Without delay poison, greater magic weapon, and resist energy the
    paladin's statistics are Immune charm, compulsion, disease, fear, sleep; Resist
    none; Melee +1 axiomatic longsword +26/+21/+16/+11 (1d8+6/17-20).
ability_scores:
  STR: 20
  DEX: 14
  CON: 14
  INT: 10
  WIS: 8
  CHA: 16
BAB: 19
CMB: 24
CMD: 40
feats:
- name: Extra Lay on Hands
- name: Great Fortitude
- name: Improved Critical (lance)
- name: Improved Critical (longsword)
- name: Improved Initiative
- name: Mounted Combat
- name: Power Attack
- name: Skill Focus (Perception)
- name: Toughness
- name: Weapon Focus (longsword)
- name: Weapon Focus (lance)
skills:
  Diplomacy: 11
  Intimidate: 6
  Knowledge (local): 5
  Knowledge (nobility): 8
  Perception: 17
  Ride: 10
    to stay in the saddle: 12
languages:
- Common
- Elven
special_qualities:
- aura
- code of conduct
- divine bond (weapon +5, 4/day)
- elf blood
- lay on hands (9d6, 14/day)
- mercies (blinded, dazed, diseased, fatigued, paralyzed, shaken)
gear:
  combat:
  - potion of haste
  other:
  - +4 mithral chainmail
  - +1 heavy steel shield
  - +1 axiomatic longsword
  - +1 lance
  - amulet of natural armor +2
  - belt of physical might +2 (Str, Con)
  - cloak of resistance +2
  - horseshoes of speed
  - ring of protection +4
  - slippers of spider climbing
  - combat-trained heavy horse
  - military saddle
  - holy symbol
  - 2,010 gp
desc_long: The mithral master is a gleaming symbol of honor.

---

# Mithral Master

**Source** NPC Codex pg. 126
**XP** 153,600
Half-elf _[[classes/Paladin|paladin]]_ of Abadar 19

LG Medium humanoid (elf, human)
**Init** +6; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +17
**Aura** courage (10 ft.), faith (10 ft.), justice (10 ft.), resolve (10 ft.), righteousness (10 ft.)

##### Defense

**AC** 31, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 29 (+10 armor, +4 _[[spells/Deflection|deflection]]_, +2 Dex, +2 natural, +3 _[[spells/Shield|shield]]_)
**hp** 185 (19d10+76)
**Fort** +20, **Ref** +13, **Will** +15; +2 vs. enchantments
**DR** 5/evil; **Immune** charm, compulsion, disease, _[[universal monster rules/Fear|fear]]_, poison, sleep; **Resist** fire 30

##### Offense
**Speed** 30 ft.
**Melee** +4 _[[items/Weapon Magic Abilities/Axiomatic|axiomatic]]_ _[[items/Weapon/Longsword|longsword]]_ +29/+24/+19/+14 (1d8+9/17–20) or +1 _[[items/Weapon/Lance|lance]]_ +26/+21/+16/+11 (1d8+6/19–20/×3)
**Special Attacks** channel positive energy (DC 22, 10d6), smite evil 7/day (+3 attack and AC, +19 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 19th; concentration +22)
At will—_[[spells/Detect Evil|detect evil]]_
**_Paladin_ Spells Prepared **(CL 16th; concentration +19)
4th—_[[spells/Death Ward|death ward]]_, _[[spells/Neutralize Poison|neutralize poison]]_
3rd—_[[spells/Daylight|daylight]]_, greater _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Prayer|prayer]]_, remove blindness
2nd—_[[spells/Delay Poison|delay poison]]_, _[[monsters/Eagle|eagle]]_’s splendor (2), _[[spells/Resist Energy|resist energy]]_
1st—_[[spells/Bless|bless]]_, _[[spells/Create Water|create water]]_, _[[spells/Divine Favor|divine favor]]_ (2), lesser _[[spells/Restoration|restoration]]_

### Tactics

**Before Combat **The _paladin_ casts _delay poison_ and _resist energy_ (fire) on himself and greater _magic weapon_ on his _longsword_.
**During Combat **The _paladin_ fights on horseback or on foot as the situation warrants. He casts _eagle_’s splendor to enhance his smite evil attacks, but otherwise relies on standard melee tactics and healing himself with lay on hands.
**Base Statistics **Without _delay poison_, greater _magic weapon_, and _resist energy_ the _paladin_’s statistics are **Immune **charm, compulsion, disease, _fear_, sleep; **Resist **none; **Melee** +1 _axiomatic_ _longsword_ +26/+21/+16/+11 (1d8+6/17–20).

##### Statistics
**Str** 20, **Dex** 14, **Con** 14, **Int** 10, **Wis** 8, **Cha** 16
**Base Atk** +19; **CMB** +24; **CMD** 40
**Feats** _[[feats/Extra Lay On Hands|Extra Lay on Hands]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Critical|Improved Critical]]_ (_lance_, _longsword_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mounted Combat|Mounted Combat]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_longsword_, _lance_)
**Skills** Diplomacy +11, Intimidate +6, Knowledge (local) +5, Knowledge (nobility) +8, Perception +17, Ride +10 (+12 to stay in the saddle)
**Languages** Common, Elven
**SQ** aura, code of conduct, divine bond (weapon +5, 4/day), elf blood, lay on hands (9d6, 14/day), mercies (_[[conditions/Blinded|blinded]]_, _[[conditions/Dazed|dazed]]_, diseased, _[[conditions/Fatigued|fatigued]]_, _[[conditions/Paralyzed|paralyzed]]_, _[[conditions/Shaken|shaken]]_)
**Combat Gear** potion of _[[spells/Haste|haste]]_; **Other Gear** +4 mithral _[[items/Armor/Chainmail|chainmail]]_, +1 _[[items/Shield/Heavy steel shield|heavy steel shield]]_, +1 _axiomatic_ _longsword_, +1 _lance_, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Belt of Physical Might +2|belt of physical might +2]]_ (Str, Con), _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Horseshoes of Speed|horseshoes of speed]]_, _[[items/Ring/Ring of Protection +4|ring of protection +4]]_, _[[items/Wondrous Item/Slippers of Spider Climbing|slippers of spider climbing]]_, combat-trained heavy _[[monsters/Horse|horse]]_, military saddle, holy symbol, 2,010 gp

The _[[npcs/Mithral Master|mithral master]]_ is a gleaming symbol of honor.
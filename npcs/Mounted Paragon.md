---
cssclass: [monsters]
title1: Mounted Paragon
title2: Mounted Paragon
CR: 15
sources:
- name: NPC Codex
  page: 123
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 51200
race: Human
classes:
- paladin 16
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
- name: faith
  radius: 10
- name: justice
  radius: 10
- name: resolve
  radius: 10
AC:
  AC: 28
  touch: 12
  flat_footed: 27
  components:
    armor: 11
    deflection: 1
    dex: 1
    natural: 1
    shield: 4
HP:
  HP: 148
  long: 16d10+56
saves:
  fort: 17
  ref: 10
  will: 13
immunities:
- charm
- disease
- fear
- poison
resistances:
  fire: 30
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 holy lance +24/+19/+14/+9 (1d8+7/19-20/×3)
      entries:
      - - damage: 1d8+7
          crit_range: 19-20
          crit_multiplier: 3
      attack: +1 holy lance
      bonus:
      - 24
      - 19
      - 14
      - 9
  - - text: +1 heavy mace +23/+18/+13/+8 (1d8+7)
      entries:
      - - damage: 1d8+7
      attack: +1 heavy mace
      bonus:
      - 23
      - 18
      - 13
      - 8
  special:
  - channel positive energy (DC 20, 8d6)
  - smite evil 6/day (+2 attack and AC, +16 damage)
space: 5
reach: 5
reach_other: 10 ft. with lance
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: At will
  sources:
  - name: default
    CL: 16
    concentration: 18
spells:
  entries:
  - name: holy sword
    source: Paladin
    level: 4
  - name: heal mount
    source: Paladin
    level: 3
  - name: prayer
    source: Paladin
    level: 3
  - name: delay poison
    source: Paladin
    level: 2
  - name: eagle's splendor
    source: Paladin
    level: 2
  - name: remove paralysis
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
    CL: 13
    concentration: 15
tactics:
  Before Combat: The paladin casts delay poison and resist energy (fire).
  During Combat: The paladin fights from horseback with his lance, positioning himself
    where he can attack the enemy leader using Spirited Charge. He uses Improved Overrun
    and Trample to pass and crush creatures in his way. If he is unhorsed and mounting
    again is dangerous or impractical, he casts holy sword on his mace and fights
    on foot.
  Base Statistics: Without delay poison and resist energy, the paladin's statistics
    are Immune charm, disease, fear; Resist none.
ability_scores:
  STR: 22
  DEX: 12
  CON: 16
  INT: 10
  WIS: 8
  CHA: 14
BAB: 16
CMB: 22
CMB_other: +24 overrun
CMD: 34
CMD_other: 36 vs. overrun
feats:
- name: Improved Critical (lance)
- name: Improved Overrun
- name: Mounted Combat
- name: Power Attack
- name: Ride-By Attack
- name: Spirited Charge
- name: Trample
- name: Vital Strike
- name: Weapon Focus (lance)
skills:
  Handle Animal: 9
  Heal: 6
  Intimidate: 10
  Perception: 15
  Ride: 15
    to stay in the saddle: 17
  Sense Motive: 10
languages:
- Common
special_qualities:
- aura
- code of conduct
- divine bond (mount)
- lay on hands (8d6, 10/day)
- mercies (fatigued, frightened, paralyzed, shaken, staggered)
desc_long: This holy warrior is a skilled rider who dispenses harsh justice at the
  point of a lance.

---

# Mounted Paragon

**Source** NPC Codex pg. 123
**XP** 51,200
Human _[[classes/Paladin|paladin]]_ 16

LG Medium humanoid (human)
**Init** +1; **Senses** Perception +15
**Aura** courage (10 ft.), faith (10 ft.), justice (10 ft.), resolve (10 ft.)

##### Defense

**AC** 28, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+11 armor, +1 _[[spells/Deflection|deflection]]_, +1 Dex, +1 natural, +4 _[[spells/Shield|shield]]_)
**hp** 148 (16d10+56)
**Fort** +17, **Ref** +10, **Will** +13
**Immune** charm, disease, _[[universal monster rules/Fear|fear]]_, poison; **Resist** fire 30

##### Offense
**Speed** 20 ft.
**Melee** +1 holy _[[items/Weapon/Lance|lance]]_ +24/+19/+14/+9 (1d8+7/19–20/×3) or +1 _[[items/Weapon/Heavy mace|heavy mace]]_ +23/+18/+13/+8 (1d8+7)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with _lance_)
**Special Attacks** channel positive energy (DC 20, 8d6), smite evil 6/day (+2 attack and AC, +16 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +18)
At will—_[[spells/Detect Evil|detect evil]]_
**_Paladin_ Spells Prepared **(CL 13th; concentration +15)
4th—_[[spells/Holy Sword|holy sword]]_
3rd—_[[spells/Heal Mount|heal mount]]_, _[[spells/Prayer|prayer]]_
2nd—_[[spells/Delay Poison|delay poison]]_, _[[monsters/Eagle|eagle]]_’s splendor, _[[spells/Remove Paralysis|remove paralysis]]_, _[[spells/Resist Energy|resist energy]]_
1st—_[[spells/Bless|bless]]_ (2), _[[spells/Divine Favor|divine favor]]_ (2)

### Tactics

**Before Combat **The _paladin_ casts _delay poison_ and _resist energy_ (fire).
**During Combat **The _paladin_ fights from horseback with his _lance_, positioning himself where he can attack the enemy leader using _[[feats/Spirited Charge|Spirited Charge]]_. He uses _[[feats/Improved Overrun|Improved Overrun]]_ and _[[universal monster rules/Trample|Trample]]_ to pass and crush creatures in his way. If he is unhorsed and mounting again is dangerous or impractical, he casts _holy sword_ on his mace and fights on foot.
**Base Statistics **Without _delay poison_ and _resist energy_, the _paladin_’s statistics are **Immune **charm, disease, _fear_; **Resist **none.

##### Statistics
**Str** 22, **Dex** 12, **Con** 16, **Int** 10, **Wis** 8, **Cha** 14
**Base Atk** +16; **CMB** +22 (+24 overrun); **CMD** 34 (36 vs. overrun)
**Feats** _[[feats/Improved Critical|Improved Critical]]_ (_lance_), _Improved Overrun_, _[[feats/Mounted Combat|Mounted Combat]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Ride-By Attack|Ride-By Attack]]_, _Spirited Charge_, _Trample_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_lance_)
**Skills** Handle Animal +9, _[[spells/Heal|Heal]]_ +6, Intimidate +10, Perception +15, Ride +15 (+17 to stay in the saddle), Sense Motive +10
**Languages** Common
**SQ** aura, code of conduct, divine bond (_[[spells/Mount|mount]]_), lay on hands (8d6, 10/day), mercies (_[[conditions/Fatigued|fatigued]]_, _[[conditions/Frightened|frightened]]_, _[[conditions/Paralyzed|paralyzed]]_, _[[conditions/Shaken|shaken]]_, _[[conditions/Staggered|staggered]]_)

This holy warrior is a skilled rider who dispenses harsh justice at the point of a _lance_.
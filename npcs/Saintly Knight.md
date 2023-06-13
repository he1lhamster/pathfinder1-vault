---
cssclass: [monsters]
title1: Saintly Knight
title2: Saintly Knight
CR: 8
sources:
- name: NPC Codex
  page: 116
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 4800
race: Half-orc
classes:
- paladin of Iomedae 9
alignment: LG
size: Medium
type: humanoid
subtypes:
- human
- orc
initiative:
  bonus: -1
senses:
  darkvision: 60
auras:
- name: courage
  radius: 10
- name: resolve
  radius: 10
AC:
  AC: 21
  touch: 9
  flat_footed: 21
  components:
    armor: 10
    dex: -1
    shield: 2
HP:
  HP: 72
  long: 9d10+18
saves:
  fort: 10
  ref: 5
  will: 12
defensive_abilities:
- orc ferocity
immunities:
- charm
- disease
- fear
resistances:
  fire: 10
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 lance +14/+9 (1d8+5/×3)
      entries:
      - - damage: 1d8+5
          crit_multiplier: 3
      attack: +1 lance
      bonus:
      - 14
      - 9
  - - text: +1 heavy mace +14/+9 (1d8+5)
      entries:
      - - damage: 1d8+5
      attack: +1 heavy mace
      bonus:
      - 14
      - 9
  ranged:
  - - text: mwk heavy crossbow +9 (1d10/19-20)
      entries:
      - - damage: 1d10
          crit_range: 19-20
      attack: mwk heavy crossbow
      bonus:
      - 9
  special:
  - channel positive energy (DC 16, 5d6)
  - smite evil 3/day (+2 attack and AC, +9 damage)
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
    CL: 9
    concentration: 11
spells:
  entries:
  - name: resist energy
    source: Paladin
    level: 2
  - name: zone of truth
    source: Paladin
    level: 2
  - name: divine favor
    source: Paladin
    level: 1
  - name: lesser restoration
    source: Paladin
    level: 1
  - name: protection from evil
    source: Paladin
    level: 1
  sources:
  - name: Paladin
    type: prepared
    CL: 6
    concentration: 8
tactics:
  Before Combat: The paladin casts resist energy (fire) unless he expects damage from
    a different energy type. He applies silversheen to his weapon if he expects to
    fight devils or lycanthropes.
  During Combat: The paladin uses Ride-By Attack and Spirited Charge, preferring to
    attack the opposing leader. When on foot, he uses his mace. If facing a powerful
    foe, he drinks his potions.
  Base Statistics: Without resist energy, the paladin's statistics are Resist none.
ability_scores:
  STR: 18
  DEX: 8
  CON: 12
  INT: 10
  WIS: 13
  CHA: 15
BAB: 9
CMB: 13
CMD: 22
feats:
- name: Iron Will
- name: Mounted Combat
- name: Ride-By Attack
- name: Skill Focus (Perception)
- name: Spirited Charge
skills:
  Handle Animal: 6
  Intimidate: 4
  Knowledge (history): 1
  Knowledge (religion): 5
  Perception: 9
  Ride: 5
    to stay in the saddle: 7
languages:
- Common
- Orc
special_qualities:
- aura
- code of conduct
- divine bond (mount)
- lay on hands (4d6, 6/day)
- mercies (frightened, shaken, staggered)
- orc blood
- weapon familiarity
gear:
  combat:
  - potion of bull's strength
  - potion of delay poison
  - potion of shield of faith
  - silversheen
  other:
  - +1 full plate
  - masterwork heavy steel shield
  - +1 heavy mace
  - +1 lance
  - masterwork heavy crossbow with 10 bolts
  - cloak of resistance +1
  - military saddle
  - 297 gp
desc_long: A saintly knight accomplishes great acts with his indomitable spirit and
  martial prowess.

---

# Saintly Knight

**Source** NPC Codex pg. 116
**XP** 4,800
Half-orc _[[classes/Paladin|paladin]]_ of Iomedae 9

LG Medium humanoid (human, _[[monsters/Orc|orc]]_)
**Init** –1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +9
**Aura** courage (10 ft.), resolve (10 ft.)

##### Defense

**AC** 21, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+10 armor, –1 Dex, +2 _[[spells/Shield|shield]]_)
**hp** 72 (9d10+18)
**Fort** +10, **Ref** +5, **Will** +12
**Defensive Abilities** _orc_ _[[universal monster rules/Ferocity|ferocity]]_; **Immune** charm, disease, _[[universal monster rules/Fear|fear]]_; **Resist** fire 10

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Lance|lance]]_ +14/+9 (1d8+5/×3) or +1 _[[items/Weapon/Heavy mace|heavy mace]]_ +14/+9 (1d8+5)
**Ranged** mwk _[[items/Weapon/Heavy crossbow|heavy crossbow]]_ +9 (1d10/19–20)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with _lance_)
**Special Attacks** channel positive energy (DC 16, 5d6), smite evil 3/day (+2 attack and AC, +9 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +11)
At will—_[[spells/Detect Evil|detect evil]]_
**_Paladin_ Spells Prepared **(CL 6th; concentration +8)
2nd—_[[spells/Resist Energy|resist energy]]_, _[[spells/Zone of Truth|zone of truth]]_
1st—_[[spells/Divine Favor|divine favor]]_, lesser _[[spells/Restoration|restoration]]_, _[[spells/Protection From Evil|protection from evil]]_

### Tactics

**Before Combat **The _paladin_ casts _resist energy_ (fire) unless he expects damage from a different energy type. He applies _[[items/Wondrous Item/Silversheen|silversheen]]_ to his weapon if he expects to fight devils or lycanthropes.
**During Combat **The _paladin_ uses _[[feats/Ride-By Attack|Ride-By Attack]]_ and _[[feats/Spirited Charge|Spirited Charge]]_, preferring to attack the opposing leader. When on foot, he uses his mace. If facing a powerful foe, he drinks his potions.
**Base Statistics **Without _resist energy_, the _paladin_’s statistics are **Resist **none.

##### Statistics
**Str** 18, **Dex** 8, **Con** 12, **Int** 10, **Wis** 13, **Cha** 15
**Base Atk** +9; **CMB** +13; **CMD** 22
**Feats** _[[feats/Iron Will|Iron Will]]_, _[[feats/Mounted Combat|Mounted Combat]]_, _Ride-By Attack_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _Spirited Charge_
**Skills** Handle Animal +6, Intimidate +4, Knowledge (history) +1, Knowledge (religion) +5, Perception +9, Ride +5 (+7 to stay in the saddle)
**Languages** Common, _Orc_
**SQ** aura, code of conduct, divine bond (_[[spells/Mount|mount]]_), lay on hands (4d6, 6/day), mercies (_[[conditions/Frightened|frightened]]_, _[[conditions/Shaken|shaken]]_, _[[conditions/Staggered|staggered]]_), _orc_ blood, weapon familiarity
**Combat Gear** potion of bull’s strength, potion of _[[spells/Delay Poison|delay poison]]_, potion of _[[spells/Shield Of Faith|shield of faith]]_, _silversheen_; **Other Gear** +1 _[[items/Armor/Full plate|full plate]]_, masterwork _[[items/Shield/Heavy steel shield|heavy steel shield]]_, +1 _heavy mace_, +1 _lance_, masterwork _heavy crossbow_ with 10 bolts, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, military saddle, 297 gp

A _[[npcs/Saintly Knight|saintly knight]]_ accomplishes great acts with his indomitable spirit and martial prowess.
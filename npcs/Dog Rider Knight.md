---
cssclass: [monsters]
title1: Dog Rider Knight
title2: Dog Rider Knight
CR: 6
sources:
- name: NPC Codex
  page: 115
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 2400
race: Halfling
classes:
- paladin of Sarenrae 7
alignment: LG
size: Small
type: humanoid
subtypes:
- halfling
initiative:
  bonus: 2
auras:
- name: courage
  radius: 10
AC:
  AC: 23
  touch: 13
  flat_footed: 21
  components:
    armor: 7
    dex: 2
    shield: 3
    size: 1
HP:
  HP: 60
  long: 7d10+17
saves:
  fort: 10
  ref: 8
  will: 8
  other: +2 vs. fear
immunities:
- disease
- fear
speeds:
  base: 15
attacks:
  melee:
  - - text: +1 lance +14/+9 (1d6+5/×3)
      entries:
      - - damage: 1d6+5
          crit_multiplier: 3
      attack: +1 lance
      bonus:
      - 14
      - 9
  - - text: mwk longsword +13/+8 (1d6+4/19-20)
      entries:
      - - damage: 1d6+4
          crit_range: 19-20
      attack: mwk longsword
      bonus:
      - 13
      - 8
  special:
  - channel positive energy (DC 16, 4d6)
  - smite evil 3/day (+3 attack and AC, +7 damage)
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
    CL: 7
    concentration: 10
spells:
  entries:
  - name: bull's strength
    source: Paladin
    level: 2
  - name: bless weapon
    source: Paladin
    level: 1
  - name: divine favor
    source: Paladin
    level: 1
  sources:
  - name: Paladin
    type: prepared
    CL: 4
    concentration: 7
tactics:
  Before Combat: The paladin casts bull's strength.
  During Combat: The paladin uses Ride-By Attack to charge his foes, and uses smite
    evil.
  Base Statistics: Without bull's strength, the paladin's statistics are Melee +1
    lance +12/+7 (1d6+3/×3) or mwk longsword +11/+6 (1d6+2/19-20); Str 14; CMB +8;
    CMD 20; Skills Climb +0.
ability_scores:
  STR: 18
  DEX: 14
  CON: 13
  INT: 10
  WIS: 8
  CHA: 16
BAB: 7
CMB: 10
CMD: 22
feats:
- name: Mounted Combat
- name: Ride-By Attack
- name: Toughness
- name: Weapon Focus (lance)
skills:
  Acrobatics: 0
    when jumping: -4
  Climb: 2
  Heal: 7
  Perception: 5
  Ride: 8
    to stay in the saddle: 10
  Survival: 1
languages:
- Common
- Halfling
special_qualities:
- aura
- code of conduct
- divine bond (mount)
- lay on hands (3d6, 6/day)
- mercies (dazed, shaken)
gear:
  combat:
  - potion of aid
  - potion of shield of faith
  other:
  - +1 breastplate
  - +1 heavy steel shield
  - +1 lance
  - masterwork longsword
  - silver holy symbol
  - exotic military saddle
  - 420 gp
desc_long: There is no description for this NPC.

---

# Dog Rider Knight

**Source** NPC Codex pg. 115
**XP** 2,400
Halfling _[[classes/Paladin|paladin]]_ of Sarenrae 7

LG Small humanoid (halfling)
**Init** +2; **Senses** Perception +5
**Aura** courage (10 ft.)

##### Defense

**AC** 23, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+7 armor, +2 Dex, +3 _[[spells/Shield|shield]]_, +1 size)
**hp** 60 (7d10+17)
**Fort** +10, **Ref** +8, **Will** +8; +2 vs. _[[universal monster rules/Fear|fear]]_
**Immune** disease, _fear_

##### Offense
**Speed** 15 ft.
**Melee** +1 _[[items/Weapon/Lance|lance]]_ +14/+9 (1d6+5/×3) or mwk _[[items/Weapon/Longsword|longsword]]_ +13/+8 (1d6+4/19–20)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with _lance_)
**Special Attacks** channel positive energy (DC 16, 4d6), smite evil 3/day (+3 attack and AC, +7 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +10)
At will—_[[spells/Detect Evil|detect evil]]_
**_Paladin_ Spells Prepared **(CL 4th; concentration +7)
2nd—bull’s strength
1st—_[[spells/Bless Weapon|bless weapon]]_, _[[spells/Divine Favor|divine favor]]_

### Tactics

**Before Combat **The _paladin_ casts bull’s strength.
**During Combat **The _paladin_ uses _[[feats/Ride-By Attack|Ride-By Attack]]_ to charge his foes, and uses smite evil.
**Base Statistics **Without bull’s strength, the _paladin_’s statistics are **Melee** +1 _lance_ +12/+7 (1d6+3/×3) or mwk _longsword_ +11/+6 (1d6+2/19–20); **Str **14; **CMB **+8; **CMD **20; **Skills **_[[universal monster rules/Climb|Climb]]_ +0.

##### Statistics
**Str** 18, **Dex** 14, **Con** 13, **Int** 10, **Wis** 8, **Cha** 16
**Base Atk** +7; **CMB** +10; **CMD** 22
**Feats** _[[feats/Mounted Combat|Mounted Combat]]_, _Ride-By Attack_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_lance_)
**Skills** Acrobatics +0 (–4 when jumping), _Climb_ +2, _[[spells/Heal|Heal]]_ +7, Perception +5, Ride +8 (+10 to stay in the saddle), Survival +1
**Languages** Common, Halfling
**SQ** aura, code of conduct, divine bond (_[[spells/Mount|mount]]_), lay on hands (3d6, 6/day), mercies (_[[conditions/Dazed|dazed]]_, _[[conditions/Shaken|shaken]]_)
**Combat Gear** potion of aid, potion of _[[spells/Shield Of Faith|shield of faith]]_; **Other Gear** +1 _[[items/Armor/Breastplate|breastplate]]_, +1 _[[items/Shield/Heavy steel shield|heavy steel shield]]_, +1 _lance_, masterwork _longsword_, silver holy symbol, exotic military saddle, 420 gp

There is no description for this NPC.
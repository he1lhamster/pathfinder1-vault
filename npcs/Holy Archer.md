---
cssclass: [monsters]
title1: Holy Archer
title2: Holy Archer
CR: 5
sources:
- name: NPC Codex
  page: 114
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 1600
race: Elf
classes:
- paladin of Erastil 6
alignment: LG
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 4
senses:
  low-light vision: true
auras:
- name: courage
  radius: 10
AC:
  AC: 18
  touch: 14
  flat_footed: 14
  components:
    armor: 4
    dex: 4
HP:
  HP: 43
  long: 6d10+6
saves:
  fort: 7
  ref: 8
  will: 8
  other: +2 vs. enchantments
immunities:
- disease
- fear
- sleep
speeds:
  base: 30
attacks:
  melee:
  - - text: longsword +6/+1 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: longsword
      bonus:
      - 6
      - 1
  ranged:
  - - text: +1 longbow +11/+6 (1d8+1/×3)
      entries:
      - - damage: 1d8+1
          crit_multiplier: 3
      attack: +1 longbow
      bonus:
      - 11
      - 6
  special:
  - channel positive energy (DC 15, 3d6)
  - smite evil 2/day (+2 attack and AC, +6 damage)
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: At will
  sources:
  - name: default
    CL: 6
    concentration: 8
spells:
  entries:
  - name: bless weapon
    source: Paladin
    level: 1
  - name: cure light wounds
    source: Paladin
    level: 1
  sources:
  - name: Paladin
    type: prepared
    CL: 3
    concentration: 5
tactics:
  During Combat: The paladin uses her bow to smite evil before it can reach her. She
    uses cover and her mobility to maintain an advantage over her opponents.
ability_scores:
  STR: 10
  DEX: 18
  CON: 11
  INT: 10
  WIS: 12
  CHA: 14
BAB: 6
CMB: 6
CMD: 20
feats:
- name: Point-Blank Shot
- name: Precise Shot
- name: Rapid Shot
skills:
  Climb: 2
  Perception: 9
  Sense Motive: 5
  Stealth: 5
languages:
- Common
- Elven
- Orc
special_qualities:
- aura
- code of conduct
- divine bond (weapon +1, 1/day)
- elven magic
- lay on hands (3d6, 5/day)
- mercies (fatigued, staggered)
- weapon familiarity
gear:
  combat:
  - +1 demon-bane arrows (5)
  - +1 undead-bane arrows (5)
  - potion of pass without trace
  - potion of shield of faith
  - alchemist's fire (2)
  other:
  - masterwork chain shirt
  - +1 longbow with 20 arrows
  - longsword
  - silver holy symbol
  - 184 gp
desc_long: Few expect honorable archers to be paladins, since they do not fit the
  typical image. Other paladins sometimes look down on these archers for shunning
  close combat, but they care only about efficiency in protecting their flocks.

---

# Holy Archer

**Source** NPC Codex pg. 114
**XP** 1,600
Elf _[[classes/Paladin|paladin]]_ of Erastil 6

LG Medium humanoid (elf)
**Init** +4; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +9
**Aura** courage (10 ft.)

##### Defense

**AC** 18, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+4 armor, +4 Dex)
**hp** 43 (6d10+6)
**Fort** +7, **Ref** +8, **Will** +8; +2 vs. enchantments
**Immune** disease, _[[universal monster rules/Fear|fear]]_, sleep

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Longsword|longsword]]_ +6/+1 (1d8/19–20)
**Ranged** +1 _[[items/Weapon/Longbow|longbow]]_ +11/+6 (1d8+1/×3)
**Special Attacks** channel positive energy (DC 15, 3d6), smite evil 2/day (+2 attack and AC, +6 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +8)
At will—_[[spells/Detect Evil|detect evil]]_
**_Paladin_ Spells Prepared **(CL 3rd; concentration +5)
1st—_[[spells/Bless Weapon|bless weapon]]_, _[[spells/Cure Light Wounds|cure light wounds]]_

### Tactics

**During Combat **The _paladin_ uses her bow to smite evil before it can reach her. She uses cover and her _[[feats/Mobility|mobility]]_ to maintain an advantage over her opponents.

##### Statistics
**Str** 10, **Dex** 18, **Con** 11, **Int** 10, **Wis** 12, **Cha** 14
**Base Atk** +6; **CMB** +6; **CMD** 20
**Feats** _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +2, Perception +9, Sense Motive +5, Stealth +5
**Languages** Common, Elven, _[[monsters/Orc|Orc]]_
**SQ** aura, code of conduct, divine bond (weapon +1, 1/day), elven magic, lay on hands (3d6, 5/day), mercies (_[[conditions/Fatigued|fatigued]]_, _[[conditions/Staggered|staggered]]_), weapon familiarity
**Combat Gear** +1 demon-bane arrows (5), +1 undead-bane arrows (5), potion of _[[spells/Pass without Trace|pass without trace]]_, potion of _[[spells/Shield Of Faith|shield of faith]]_, _[[classes/Alchemist|alchemist]]_’s fire (2); **Other Gear** masterwork _[[items/Armor/Chain shirt|chain shirt]]_, +1 _longbow_ with 20 arrows, _longsword_, silver holy symbol, 184 gp

Few expect honorable archers to be paladins, since they do not fit the typical image. Other paladins sometimes look down on these archers for shunning close combat, but they care only about efficiency in protecting their flocks.
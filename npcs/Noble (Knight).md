---
cssclass: [monsters]
title1: Noble (Knight)
title2: Noble (Knight)
CR: 7
sources:
- name: GameMastery Guide
  page: 289
  link: http://paizo.com/pathfinderRPG/v5748btpy8ffn
XP: 3200
race: Human
classes:
- aristocrat 2
- paladin 6
alignment: LG
size: Medium
type: humanoid
initiative:
  bonus: 1
auras:
- name: courage
  radius: 10
AC:
  AC: 23
  touch: 11
  flat_footed: 22
  components:
    armor: 10
    dex: 1
    shield: 2
HP:
  HP: 61
  long: 2d8+6d10+19
  HD: 8
saves:
  fort: 9
  ref: 5
  will: 9
defensive_abilities:
- divine grace +2
immunities:
- disease
- fear
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk lance +12/+7 (1d8+4/×3)
      entries:
      - - damage: 1d8+4
          crit_multiplier: 3
      attack: mwk lance
      bonus:
      - 12
      - 7
  - - text: +1 longsword +12/+7 (1d8+5/19-20)
      entries:
      - - damage: 1d8+5
          crit_range: 19-20
      attack: +1 longsword
      bonus:
      - 12
      - 7
  - - text: dagger +11/+6 (1d4+4/19-20)
      entries:
      - - damage: 1d4+4
          crit_range: 19-20
      attack: dagger
      bonus:
      - 11
      - 6
  ranged:
  - - text: dagger +8 (1d4+4/19-20)
      entries:
      - - damage: 1d4+4
          crit_range: 19-20
      attack: dagger
      bonus:
      - 8
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
  - name: cure light wounds
    source: '?'
    level: 1
  - name: divine favor
    source: '?'
    level: 1
  sources:
  - name: '?'
    type: prepared
    CL: 3
    concentration: 5
ability_scores:
  STR: 18
  DEX: 12
  CON: 14
  INT: 10
  WIS: 8
  CHA: 14
BAB: 7
CMB: 11
CMD: 22
feats:
- name: Improved Bull Rush
- name: Mounted Combat
- name: Power Attack
- name: Ride-By Attack
- name: Unseat
skills:
  Diplomacy: 10
  Handle Animal: 8
  Heal: 5
  Knowledge (history): 5
  Knowledge (nobility): 5
  Linguistics: 5
  Perception: 5
  Ride: 6
  Survival: 5
languages:
- Celestial
- Common
- Sylvan
special_qualities:
- aura of good
- divine bond (heavy horse)
- lay on hands (3d6, 5/day)
- mercies (fatigued, shaken)
gear:
  gear:
  - +1 full plate
  - masterwork heavy steel shield
  - +1 longsword
  - masterwork lance
  - dagger
  - silver holy symbol
  - heavy horse (combat trained) with chain shirt barding and military saddle
  - 420 gp
npc_boon: A knight can vouch for a PC, the knight's sterling reputation enabling the
  character to avoid or lessen a punishment. The knight can also grant a character
  entry into a tourney or a meeting with his liege with a +5 bonus on one Diplomacy
  check.
desc_long: Knights are noble warriors, proud of bearing and lineage and yet humble
  in service to their liege. Though merciful and generous of spirit, a true knight
  is always ready to level lance or bare steel in pursuit of justice and to protect
  the innocent. Knights may also serve as local lord-stewards, judges, or fortress
  commanders. Knights are usually found singly or accompanied by a squire, escorting
  a pair of pilgrims (CR 8), guarding two nobles (CR 11), or leading a lance of four
  cavalry (CR 10).

---

# Noble (Knight)

**Source** GameMastery Guide pg. 289
**XP** 3,200
Human aristocrat 2/paladin 6

LG Medium humanoid
**Init** +1; **Senses** Perception +5
**Aura** courage (10 ft.)

##### Defense

**AC** 23, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+10 armor, +1 Dex, +2 _[[spells/Shield|shield]]_)
**hp** 61 (8 HD; 2d8+6d10+19)
**Fort** +9, **Ref** +5, **Will** +9
**Defensive Abilities** divine _[[spells/Grace|grace]]_ +2; **Immune** disease, _[[universal monster rules/Fear|fear]]_

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Lance|lance]]_ +12/+7 (1d8+4/×3) or +1 _[[items/Weapon/Longsword|longsword]]_ +12/+7 (1d8+5/19–20) or _[[items/Weapon/Dagger|dagger]]_ +11/+6 (1d4+4/19–20)
**Ranged** _dagger_ +8 (1d4+4/19–20)
**Special Attacks** channel positive energy (DC 15, 3d6), smite evil 2/day (+2 attack and AC, +6 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +8)
At will—_[[spells/Detect Evil|detect evil]]_
**Spells Prepared **(CL 3rd; concentration +5)
1st—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Divine Favor|divine favor]]_

##### Statistics
**Str** 18, **Dex** 12, **Con** 14, **Int** 10, **Wis** 8, **Cha** 14
**Base Atk** +7; **CMB** +11; **CMD** 22
**Feats** _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Mounted Combat|Mounted Combat]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Ride-By Attack|Ride-By Attack]]_, _[[feats/Unseat|Unseat]]_
**Skills** Diplomacy +10, Handle Animal +8, _[[spells/Heal|Heal]]_ +5, Knowledge (history) +5, Knowledge (nobility) +5, Linguistics +5, Perception +5, Ride +6, Survival +5
**Languages** Celestial, Common, Sylvan
**SQ** aura of good, divine bond (heavy _[[monsters/Horse|horse]]_), lay on hands (3d6, 5/day), mercies (_[[conditions/Fatigued|fatigued]]_, _[[conditions/Shaken|shaken]]_)
**Gear** +1 _[[items/Armor/Full plate|full plate]]_, masterwork _[[items/Shield/Heavy steel shield|heavy steel shield]]_, +1 _longsword_, masterwork _lance_, _dagger_, silver holy symbol, heavy _horse_ (combat trained) with _[[items/Armor/Chain shirt|chain shirt]]_ barding and military saddle, 420 gp

**Boon **A _[[npcs/Knight|knight]]_ can vouch for a PC, the _knight_’s sterling reputation enabling the character to avoid or lessen a punishment. The _knight_ can also grant a character entry into a tourney or a meeting with his liege with a +5 bonus on one Diplomacy check.

Knights are noble warriors, proud of bearing and lineage and yet humble in service to their liege. Though _[[items/Weapon Magic Abilities/Merciful|merciful]]_ and generous of spirit, a true _knight_ is always ready to level _lance_ or bare steel in pursuit of justice and to protect the innocent. Knights may also serve as local lord-stewards, judges, or fortress commanders. Knights are usually found singly or accompanied by a _[[npcs/Squire|squire]]_, escorting a pair of pilgrims (CR 8), _[[items/Armor Magic Abilities/Guarding|guarding]]_ two nobles (CR 11), or leading a _lance_ of four cavalry (CR 10).
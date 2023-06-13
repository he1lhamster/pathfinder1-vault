---
cssclass: [monsters]
title1: Crusader (Holy Warrior)
title2: Crusader (Holy Warrior)
CR: 6
sources:
- name: GameMastery Guide
  page: 269
  link: http://paizo.com/pathfinderRPG/v5748btpy8ffn
XP: 2400
race: Human
classes:
- paladin 7
alignment: LG
size: Medium
type: humanoid
initiative:
  bonus: 3
auras:
- name: courage
  radius: 10
AC:
  AC: 20
  touch: 13
  flat_footed: 17
  components:
    armor: 7
    dex: 3
HP:
  HP: 51
  long: 7d10+13
saves:
  fort: 8
  ref: 7
  will: 6
defensive_abilities:
- divine grace +2
immunities:
- disease
- fear
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 greatsword +10/+5 (2d6+4/19-20)
      entries:
      - - damage: 2d6+4
          crit_range: 19-20
      attack: +1 greatsword
      bonus:
      - 10
      - 5
  - - text: lance +9/+4 (1d8+3/×3)
      entries:
      - - damage: 1d8+3
          crit_multiplier: 3
      attack: lance
      bonus:
      - 9
      - 4
  - - text: dagger +9/+4 (1d4+2/19-20)
      entries:
      - - damage: 1d4+2
          crit_range: 19-20
      attack: dagger
      bonus:
      - 9
      - 4
  ranged:
  - - text: +1 composite longbow +11/+11/+6 (1d8+3/×3)
      entries:
      - - damage: 1d8+3
          crit_multiplier: 3
      attack: +1 composite longbow
      bonus:
      - 11
      - 11
      - 6
  - - text: dagger +10 (1d4/19-20)
      entries:
      - - damage: 1d4
          crit_range: 19-20
      attack: dagger
      bonus:
      - 10
  special:
  - smite evil (3/day, +2 attack and AC, +7 damage)
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: At Will
  sources:
  - name: default
    CL: 7
    concentration: 9
spells:
  entries:
  - name: eagle's splendor
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
    concentration: 6
ability_scores:
  STR: 14
  DEX: 17
  CON: 12
  INT: 10
  WIS: 8
  CHA: 14
BAB: 7
CMB: 9
CMD: 22
feats:
- name: Deadly Aim
- name: Manyshot
- name: Point Blank Shot
- name: Power Attack
- name: Rapid Shot
skills:
  Craft (armor): 4
  Craft (weapons): 4
  Diplomacy: 6
  Handle Animal: 6
  Heal: 4
  Knowledge (nobility): 4
  Knowledge (religion): 4
  Perception: 4
  Ride: 10
  Sense Motive: 4
languages:
- Common
special_qualities:
- aura of good
- channel positive energy (DC 15, 4d6)
- divine bond (weapon +1)
- lay on hands (3d6, 5/day)
- mercies (fatigued, dazed)
gear:
  gear:
  - +1 breastplate
  - +1 greatsword
  - +1 composite longbow (+2 Str) with 20 arrows
  - 10 cold iron arrows
  - and 10 alchemical silver arrows
  - dagger
  - lance
  - silver holy symbol
  - light horse (combat trained) with military saddle
npc_boon: A holy warrior can accompany the PCs for up to 3 days on a mission consistent
  with his alignment or can send a squad of up to four temple guards (as guards) for
  1 day.
desc_long: Holy warriors are divinely sanctified and anointed warriors, raining death
  with bow and blade upon the forces of darkness and bringing hope and rescue to the
  desperate. Holy warriors are versatile combatants and could be masters of a temple
  or monastery. A holy warrior might command ten temple guards (as guards, CR 9),
  while a pair of holy warriors might escort a priest (CR 10). A half dozen could
  be a saint's honor guard (CR 13).

---

# Crusader (Holy Warrior)

**Source** GameMastery Guide pg. 269
**XP** 2,400
Human _[[classes/Paladin|paladin]]_ 7

LG Medium humanoid
**Init** +3; **Senses** Perception +4
**Aura** courage (10 ft.)

##### Defense

**AC** 20, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+7 armor, +3 Dex)
**hp** 51 (7d10+13)
**Fort** +8, **Ref** +7, **Will** +6
**Defensive Abilities** divine _[[spells/Grace|grace]]_ +2; **Immune** disease, _[[universal monster rules/Fear|fear]]_

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Greatsword|greatsword]]_ +10/+5 (2d6+4/19–20) or _[[items/Weapon/Lance|lance]]_ +9/+4 (1d8+3/×3) or _[[items/Weapon/Dagger|dagger]]_ +9/+4 (1d4+2/19–20)
**Ranged** +1 _[[items/Weapon/Composite longbow|composite longbow]]_ +11/+11/+6 (1d8+3/×3) or _dagger_ +10 (1d4/19–20)
**Special Attacks** smite evil (3/day, +2 attack and AC, +7 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +9)
At Will—_[[spells/Detect Evil|detect evil]]_
**_Paladin_ Spells Prepared **(CL 4th; concentration +6)
2nd—_[[monsters/Eagle|eagle]]_’s splendor
1st—_[[spells/Bless Weapon|bless weapon]]_, _[[spells/Divine Favor|divine favor]]_

##### Statistics
**Str** 14, **Dex** 17, **Con** 12, **Int** 10, **Wis** 8, **Cha** 14
**Base Atk** +7; **CMB** +9; **CMD** 22
**Feats** _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Manyshot|Manyshot]]_, Point Blank Shot, _[[feats/Power Attack|Power Attack]]_, _[[feats/Rapid Shot|Rapid Shot]]_
**Skills** Craft (armor) +4, Craft (weapons) +4, Diplomacy +6, Handle Animal +6, _[[spells/Heal|Heal]]_ +4, Knowledge (nobility) +4, Knowledge (religion) +4, Perception +4, Ride +10, Sense Motive +4
**Languages** Common
**SQ** aura of good, channel positive energy (DC 15, 4d6), divine bond (weapon +1), lay on hands (3d6, 5/day), mercies (_[[conditions/Fatigued|fatigued]]_, _[[conditions/Dazed|dazed]]_)
**Gear** +1 _[[items/Armor/Breastplate|breastplate]]_, +1 _greatsword_, +1 _composite longbow_ (+2 Str) with 20 arrows, 10 cold iron arrows, and 10 alchemical silver arrows, _dagger_, _lance_, silver holy symbol, light _[[monsters/Horse|horse]]_ (combat trained) with military saddle

**Boon** A holy warrior can accompany the PCs for up to 3 days on a mission consistent with his alignment or can send a squad of up to four temple guards (as guards) for 1 day.

Holy warriors are divinely sanctified and anointed warriors, raining death with bow and blade upon the forces of _[[spells/Darkness|darkness]]_ and bringing hope and rescue to the desperate. Holy warriors are versatile combatants and could be masters of a temple or monastery. A holy warrior might _[[spells/Command|command]]_ ten temple guards (as guards, CR 9), while a pair of holy warriors might escort a priest (CR 10). A half dozen could be a saint’s honor _[[npcs/Guard|guard]]_ (CR 13).
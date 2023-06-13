---
cssclass: [monsters]
title1: Gnoll, Gnoll Ravager
title2: Gnoll Ravager
CR: 11
sources:
- name: Monster Codex
  page: 97
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 12800
race: Gnoll
classes:
- antipaladin of Lamashtu 10 (Advanced Player's Guide 118)
alignment: CE
size: Medium
type: humanoid
subtypes:
- gnoll
initiative:
  bonus: 0
senses:
  darkvision: 60
auras:
- name: cowardice
  radius: 10
- name: despair
  radius: 10
AC:
  AC: 21
  touch: 10
  flat_footed: 21
  components:
    armor: 10
    natural: 1
HP:
  HP: 122
  long: 2d8+10d10+46
  HD: 12
saves:
  fort: 16
  ref: 5
  will: 12
immunities:
- disease
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 human-bane falchion +19/+14/+9 (2d4+10/15-20)
      entries:
      - - damage: 2d4+10
          crit_range: 15-20
      attack: +1 human-bane falchion
      bonus:
      - 19
      - 14
      - 9
  special:
  - channel negative energy (DC 16, 5d6)
  - smite good 4/day (+1 attack and AC, +10 damage)
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: At will
  sources:
  - name: default
    CL: 10
    concentration: 11
spells:
  entries:
  - name: bull's strength
    source: Antipaladin
    level: 2
  - name: doom
    source: Antipaladin
    level: 1
    DC: 12
  - superscripts:
    - UC
    name: litany of sloth
    source: Antipaladin
    level: 1
  - name: protection from good
    source: Antipaladin
    level: 1
  sources:
  - name: Antipaladin
    type: prepared
    CL: 7
    concentration: 8
tactics:
  Before Combat: The ravager casts bull's strength on himself.
  Base Statistics: Without bull's strength, the ravager's base statistics are Melee
    +1 human-bane falchion +17/+12/+7 (2d4+7/15-20); Str 19; CMB +15; CMD 25.
ability_scores:
  STR: 23
  DEX: 10
  CON: 18
  INT: 6
  WIS: 12
  CHA: 13
BAB: 11
CMB: 17
CMD: 27
feats:
- name: Cleave
- name: Great Cleave
- name: Improved Critical (falchion)
- name: Iron Will
- name: Power Attack
- name: Weapon Focus (falchion)
skills:
  Intimidate: 16
  Perception: 1
languages:
- Gnoll
special_qualities:
- cruelties (fatigued, nauseated, staggered)
- fiendish boon (weapon +2, 2/day)
- touch of corruption (6/day, 5d6)
gear:
  combat:
  - potion of cure moderate wounds
  other:
  - +1 full plate
  - +1 human-bane falchion
  - belt of mighty constitution +2
  - cloak of resistance +1
  - 125 gp
ecology:
  environment: warm plains or desert
desc_long: Gnolls revere Lamashtu above all other gods.

---

# Gnoll, Gnoll Ravager

**Source** Monster Codex pg. 97
**XP** 12,800
_[[monsters/Gnoll|Gnoll]]_ _[[classes/Antipaladin|antipaladin]]_ of Lamashtu 10 (Advanced Player’s Guide 118)
CE Medium humanoid (_gnoll_)
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +1
**Aura** cowardice (10 ft.), despair (10 ft.)

##### Defense

**AC** 21, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+10 armor, +1 natural)
**hp** 122 (12 HD; 2d8+10d10+46)
**Fort** +16, **Ref** +5, **Will** +12
**Immune** disease

##### Offense
**Speed** 20 ft.
**Melee** +1 human-bane _[[items/Weapon/Falchion|falchion]]_ +19/+14/+9 (2d4+10/15–20)
**Special Attacks** channel negative energy (DC 16, 5d6), smite good 4/day (+1 attack and AC, +10 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +11)
At will—_[[spells/Detect Good|detect good]]_
**_Antipaladin_ Spells Prepared **(CL 7th; concentration +8)
2nd—bull’s strength
1st—_[[spells/Doom|doom]]_ (DC 12), _[[spells/Litany of Sloth|litany of sloth]]_, _[[spells/Protection From Good|protection from good]]_

### Tactics

**Before Combat **The ravager casts bull’s strength on himself.
 **Base Statistics **Without bull’s strength, the ravager’s base statistics are Melee +1 human-bane _falchion_ +17/+12/+7 (2d4+7/15–20); **Str **19; **CMB **+15; **CMD **25.

##### Statistics
**Str** 23, **Dex** 10, **Con** 18, **Int** 6, **Wis** 12, **Cha** 13
**Base Atk** +11; **CMB** +17; **CMD** 27
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Critical|Improved Critical]]_ (_falchion_), _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_falchion_)
**Skills** Intimidate +16
**Languages** _Gnoll_
**SQ** cruelties (_[[conditions/Fatigued|fatigued]]_, _[[conditions/Nauseated|nauseated]]_, _[[conditions/Staggered|staggered]]_), fiendish boon (weapon +2, 2/day), touch of corruption (6/day, 5d6)
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_; **Other Gear** +1 _[[items/Armor/Full plate|full plate]]_, +1 human-bane _falchion_, _[[items/Wondrous Item/Belt of Mighty Constitution +2|belt of mighty constitution +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, 125 gp

##### Ecology

**Environment** warm plains or desert

##### Description

Gnolls revere Lamashtu above all other gods.
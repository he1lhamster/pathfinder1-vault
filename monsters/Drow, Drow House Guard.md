---
cssclass: [monsters]
title1: Drow, Drow House Guard
title2: Drow House Guard
CR: 2
sources:
- name: Monster Codex
  page: 35
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 600
race: Drow
classes:
- fighter 3
alignment: CE
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 3
senses:
  darkvision: 120
AC:
  AC: 17
  touch: 13
  flat_footed: 14
  components:
    armor: 4
    dex: 3
HP:
  HP: 24
  long: 3d10+3
saves:
  fort: 3
  ref: 4
  will: 2
  will_other: +1 vs. fear
  other: +2 vs. enchantment
defensive_abilities:
- bravery +1
immunities:
- sleep
SR: 9
weaknesses:
- light blindness
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk longsword +7 (1d8+2/19-20 plus poison)
      entries:
      - - damage: 1d8+2
          crit_range: 19-20
        - effect: poison
      attack: mwk longsword
      bonus:
      - 7
  ranged:
  - - text: repeating heavy crossbow +7 (1d10/19-20 plus poison)
      entries:
      - - damage: 1d10
          crit_range: 19-20
        - effect: poison
      attack: repeating heavy crossbow
      bonus:
      - 7
spell_like_abilities:
  entries:
  - name: dancing lights
    source: default
    freq: 1/day
  - name: darkness
    source: default
    freq: 1/day
  - name: faerie fire
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 3
    concentration: 3
tactics:
  During Combat: The house guard uses alchemical weapons and poison against spellcasters.
ability_scores:
  STR: 14
  DEX: 17
  CON: 11
  INT: 10
  WIS: 12
  CHA: 10
BAB: 3
CMB: 5
CMD: 18
feats:
- name: Deadly Aim
- name: Exotic Weapon Proficiency (heavy repeating crossbow)
- name: Point-Blank Shot
- name: Weapon Focus (longsword)
skills:
  Climb: 6
  Perception: 6
  Stealth: 5
languages:
- Elven
- Undercommon
special_qualities:
- armor training 1
- poison use
gear:
  combat:
  - +1 frost bolt
  - potion of cure light wounds
  - drow poison (2)
  - smokesticks (2)
  - tanglefoot bag
  - thunderstones (2)
  other:
  - mwk chain shirt
  - mwk longsword
  - repeating heavy crossbow with 20 mwk bolts
  - 47 gp
ecology:
  environment: underground
desc_long: A house guard is better trained and equipped than a common warrior defending
  a drow city or caravan.

---

# Drow, Drow House Guard

**Source** Monster Codex pg. 35
**XP** 600
_[[monsters/Drow|Drow]]_ _[[classes/Fighter|fighter]]_ 3
CE Medium humanoid (elf)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +6

##### Defense

**AC** 17, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+4 armor, +3 Dex)
**hp** 24 (3d10+3)
**Fort** +3, **Ref** +4, **Will** +2 (+1 vs. _[[universal monster rules/Fear|fear]]_); +2 vs. enchantment
**Defensive Abilities** bravery +1; **Immune** sleep; **SR** 9
**Weaknesses** _[[universal monster rules/Light Blindness|light blindness]]_

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Longsword|longsword]]_ +7 (1d8+2/19–20 plus poison)
**Ranged** _[[items/Weapon/Repeating heavy crossbow|repeating heavy crossbow]]_ +7 (1d10/19–20 plus poison)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd; concentration +3)
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Darkness|darkness]]_, _[[spells/Faerie Fire|faerie fire]]_

### Tactics

**During Combat** The house _[[npcs/Guard|guard]]_ uses alchemical weapons and poison against spellcasters.

##### Statistics
**Str** 14, **Dex** 17, **Con** 11, **Int** 10, **Wis** 12, **Cha** 10
**Base Atk** +3; **CMB** +5; **CMD** 18
**Feats** _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Exotic Weapon Proficiency|Exotic Weapon Proficiency]]_ (heavy repeating crossbow), _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_longsword_)
**Skills** _[[universal monster rules/Climb|Climb]]_ +6, Perception +6, Stealth +5
**Languages** Elven, Undercommon
**SQ** armor _[[items/Weapon Magic Abilities/Training|training]]_ 1, poison use
**Combat Gear** +1 frost bolt, potion of _[[spells/Cure Light Wounds|cure light wounds]]_, _[[poisons/Drow poison|drow poison]]_ (2), smokesticks (2), _[[items/Mundane/Tanglefoot bag|tanglefoot bag]]_, thunderstones (2); **Other Gear** mwk _[[items/Armor/Chain shirt|chain shirt]]_, mwk _longsword_, _repeating heavy crossbow_ with 20 mwk bolts, 47 gp

##### Ecology

**Environment** underground

##### Description

A house _guard_ is better trained and equipped than a common warrior _[[items/Weapon Magic Abilities/Defending|defending]]_ a _drow_ city or caravan.
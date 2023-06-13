---
cssclass: [monsters]
title1: Drow, Drow Scout
title2: Drow Scout
CR: 1
sources:
- name: Monster Codex
  page: 34
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 400
race: Drow
classes:
- rogue 2
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
  AC: 16
  touch: 13
  flat_footed: 13
  components:
    armor: 3
    dex: 3
HP:
  HP: 16
  long: 2d8+4
saves:
  fort: 1
  ref: 6
  will: 1
  other: +2 vs. enchantment
defensive_abilities:
- evasion
immunities:
- sleep
SR: 8
weaknesses:
- light blindness
speeds:
  base: 30
attacks:
  melee:
  - - text: short sword +2 (1d6+1/19-20)
      entries:
      - - damage: 1d6+1
          crit_range: 19-20
      attack: short sword
      bonus:
      - 2
  ranged:
  - - text: mwk shortbow +6 (1d6/×3 plus poison)
      entries:
      - - damage: 1d6
          crit_multiplier: 3
        - effect: poison
      attack: mwk shortbow
      bonus:
      - 6
  special:
  - sneak attack +1d6
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
    CL: 2
    concentration: 2
ability_scores:
  STR: 13
  DEX: 17
  CON: 12
  INT: 10
  WIS: 12
  CHA: 10
BAB: 1
CMB: 2
CMD: 15
feats:
- name: Weapon Focus (shortbow)
skills:
  Acrobatics: 8
  Climb: 6
  Disable Device: 7
  Knowledge (dungeoneering): 5
  Knowledge (local): 4
  Perception: 8
  Sense Motive: 5
  Stealth: 8
  Survival: 3
  Swim: 5
languages:
- Elven
- Undercommon
special_qualities:
- poison use
- trapfinding +1
gear:
  combat:
  - potion of cure light wounds
  - drow poison (2)
  - tanglefoot bag
  other:
  - mwk studded leather
  - mwk shortbow and 20 arrows
  - short sword
  - 14 gp
ecology:
  environment: underground
desc_long: Scouts are cunning and resourceful, but still must prove themselves to
  higher-ranked drow before being considered anything but expendable.

---

# Drow, Drow Scout

**Source** Monster Codex pg. 34
**XP** 400
_[[monsters/Drow|Drow]]_ _[[classes/Rogue|rogue]]_ 2
CE Medium humanoid (elf)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +8

##### Defense

**AC** 16, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+3 armor, +3 Dex)
**hp** 16 (2d8+4)
**Fort** +1, **Ref** +6, **Will** +1; +2 vs. enchantment
**Defensive Abilities** evasion; **Immune** sleep; **SR** 8
**Weaknesses** _[[universal monster rules/Light Blindness|light blindness]]_

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Short sword|short sword]]_ +2 (1d6+1/19–20)
**Ranged** mwk _[[items/Weapon/Shortbow|shortbow]]_ +6 (1d6/×3 plus poison)
**Special Attacks** sneak attack +1d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 2nd, concentration +2)
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Darkness|darkness]]_, _[[spells/Faerie Fire|faerie fire]]_

##### Statistics
**Str** 13, **Dex** 17, **Con** 12, **Int** 10, **Wis** 12, **Cha** 10
**Base Atk** +1; **CMB** +2; **CMD** 15
**Feats** _[[feats/Weapon Focus|Weapon Focus]]_ (_shortbow_)
**Skills** Acrobatics +8, _[[universal monster rules/Climb|Climb]]_ +6, Disable Device +7, Knowledge (dungeoneering) +5, Knowledge (local) +4, Perception +8, Sense Motive +5, Stealth +8, Survival +3, Swim +5
**Languages** Elven, Undercommon
**SQ** poison use, trapfinding +1
**Combat Gear** potion of _[[spells/Cure Light Wounds|cure light wounds]]_, _[[poisons/Drow poison|drow poison]]_ (2), _[[items/Mundane/Tanglefoot bag|tanglefoot bag]]_; **Other Gear** mwk studded leather, mwk _shortbow_ and 20 arrows, _short sword_, 14 gp

##### Ecology

**Environment** underground

##### Description

Scouts are _[[items/Weapon Magic Abilities/Cunning|cunning]]_ and resourceful, but still must prove themselves to higher-ranked _drow_ before being considered anything but expendable.
---
cssclass: [monsters]
title1: Tunnel Rat
title2: Tunnel Rat
CR: 5
sources:
- name: NPC Codex
  page: 130
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 1600
race: Gnome
classes:
- ranger 6
alignment: N
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 3
senses:
  low-light vision: true
AC:
  AC: 19
  touch: 15
  flat_footed: 15
  components:
    armor: 4
    dex: 3
    dodge: 1
    size: 1
HP:
  HP: 49
  long: 6d10+12
saves:
  fort: 6
  ref: 8
  will: 3
  other: +2 vs. illusions
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
immunities:
- poison
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk dagger +9/+4 (1d3+1/19-20)
      entries:
      - - damage: 1d3+1
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 9
      - 4
  ranged:
  - - text: +1 light crossbow +12 (1d6+1/19-20)
      entries:
      - - damage: 1d6+1
          crit_range: 19-20
      attack: +1 light crossbow
      bonus:
      - 12
  - - text: mwk dagger +11/+6 (1d3+1/19-20)
      entries:
      - - damage: 1d3+1
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 11
      - 6
  special:
  - +1 on attack rolls against goblinoid and reptilian humanoids
  - favored enemy (elves +2, goblinoids +4)
spells:
  entries:
  - name: alarm
    source: Ranger
    level: 1
  - name: delay poison
    source: Ranger
    level: 1
  sources:
  - name: Ranger
    type: prepared
    CL: 3
    concentration: 4
tactics:
  Before Combat: The ranger casts delay poison.
  During Combat: The ranger uses Precise Shot to help allies in melee.
  Base Statistics: Without delay poison, the ranger's statistics are Immune none.
ability_scores:
  STR: 12
  DEX: 16
  CON: 12
  INT: 12
  WIS: 13
  CHA: 10
BAB: 6
CMB: 6
CMD: 20
feats:
- name: Dodge
- name: Endurance
- name: Point-Blank Shot
- name: Precise Shot
- name: Rapid Reload
- name: Weapon Focus (light crossbow)
skills:
  Acrobatics: 8
    when jumping: 4
  Climb: 6
  Knowledge (dungeoneering): 10
  Knowledge (nature): 10
  Knowledge (engineering): 4
  Perception: 12
  Stealth: 15
  Survival: 10
languages:
- Common
- Gnome
- Sylvan
special_qualities:
- favored terrain (underground +2)
- hunter's bond (companion)
- track +3
- wild empathy +6
gear:
  combat:
  - +1 flaming arrows (6)
  - potion of barkskin
  - potion of cure moderate wounds
  - smokesticks (2)
  other:
  - masterwork chain shirt
  - +1 light crossbow with 20 bolts
  - masterwork dagger
  - 167 gp
desc_long: A tunnel rat patrols twisting passages underground.

---

# Tunnel Rat

**Source** NPC Codex pg. 130
**XP** 1,600
Gnome _[[classes/Ranger|ranger]]_ 6

N Small humanoid (gnome)
**Init** +3; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +12

##### Defense

**AC** 19, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 armor, +3 Dex, +1 dodge, +1 size)
**hp** 49 (6d10+12)
**Fort** +6, **Ref** +8, **Will** +3; +2 vs. illusions
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _dodge_ bonus to AC vs. giants); **Immune** poison

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Dagger|dagger]]_ +9/+4 (1d3+1/19–20)
**Ranged** +1 _[[items/Weapon/Light crossbow|light crossbow]]_ +12 (1d6+1/19–20) or mwk _dagger_ +11/+6 (1d3+1/19–20)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids, favored enemy (elves +2, goblinoids +4)
**_Ranger_ Spells Prepared **(CL 3rd; concentration +4)
1st—_[[spells/Alarm|alarm]]_, _[[spells/Delay Poison|delay poison]]_

### Tactics

**Before Combat **The _ranger_ casts _delay poison_.
**During Combat **The _ranger_ uses _[[feats/Precise Shot|Precise Shot]]_ to help allies in melee.
**Base Statistics **Without _delay poison_, the _ranger_’s statistics are **Immune **none.

##### Statistics
**Str** 12, **Dex** 16, **Con** 12, **Int** 12, **Wis** 13, **Cha** 10
**Base Atk** +6; **CMB** +6; **CMD** 20
**Feats** _Dodge_, _[[feats/Endurance|Endurance]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _Precise Shot_, _[[feats/Rapid Reload|Rapid Reload]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_light crossbow_)
**Skills** Acrobatics +8 (+4 when jumping), _[[universal monster rules/Climb|Climb]]_ +6, Knowledge (dungeoneering, nature) +10, Knowledge (engineering) +4, Perception +12, Stealth +15, Survival +10
**Languages** Common, Gnome, Sylvan
**SQ** favored terrain (underground +2), _[[classes/Hunter|hunter]]_’s bond (companion), track +3, wild _[[feats/Empathy|empathy]]_ +6
**Combat Gear** +1 _[[items/Weapon Magic Abilities/Flaming|flaming]]_ arrows (6), potion of _[[spells/Barkskin|barkskin]]_, potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, smokesticks (2); **Other Gear** masterwork _[[items/Armor/Chain shirt|chain shirt]]_, +1 _light crossbow_ with 20 bolts, masterwork _dagger_, 167 gp

A _[[feats/Tunnel Rat|tunnel rat]]_ patrols twisting passages underground.
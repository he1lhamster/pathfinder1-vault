---
cssclass: [monsters]
title1: Death Initiate
title2: Death Initiate
CR: 12
sources:
- name: NPC Codex
  page: 209
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 19200
race: Human
classes:
- monk 9
- assassin 4
alignment: LE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 5
AC:
  AC: 25
  touch: 21
  flat_footed: 19
  components:
    armor: 2
    deflection: 1
    dex: 5
    dodge: 1
    monk: 2
    natural: 2
    wis: 2
HP:
  HP: 88
  long: 9d8+4d8+22
saves:
  fort: 9
  ref: 14
  will: 10
  other: +2 vs. enchantments or poison
defensive_abilities:
- improved evasion
- uncanny dodge
immunities:
- disease
speeds:
  base: 60
attacks:
  melee:
  - - text: unarmed strike +15/+10 (1d10+1 plus 1d6 electricity)
      entries:
      - - damage: 1d10+1
        - damage: 1d6
          type: electricity
      attack: unarmed strike
      bonus:
      - 15
      - 10
  - - text: mwk quarterstaff +11/+6 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: mwk quarterstaff
      bonus:
      - 11
      - 6
  - - text: flurry of blows (unarmed strike) +16/+16/+11/+11/+6 (1d10+1 plus 1d6 electricity)
      entries:
      - - damage: 1d10+1
        - damage: 1d6
          type: electricity
      attack: flurry of blows (unarmed strike)
      bonus:
      - 16
      - 16
      - 11
      - 11
      - 6
  ranged:
  - - text: +1 shuriken +16/+11 (1d2+2)
      entries:
      - - damage: 1d2+2
      attack: +1 shuriken
      bonus:
      - 16
      - 11
  - - text: flurry of blows (+1 shuriken) +17/+17/+12/+12/+7 (1d2+1)
      entries:
      - - damage: 1d2+1
      attack: flurry of blows (+1 shuriken)
      bonus:
      - 17
      - 17
      - 12
      - 12
      - 7
  special:
  - death attack (DC 16)
  - flurry of blows
  - sneak attack +2d6
  - stunning fist (10/day, DC 18)
  - true death (DC 19)
tactics:
  Before Combat: The assassin drinks her potion of barkskin, attempts to study her
    victim for 3 rounds, and drinks her potion of haste.
  During Combat: Disguised as a modest pilgrim, the assassin sidles up to her mark
    and makes her death attack with a Stunning Fist attack. She then retreats to throw
    flurries of shuriken.
  Base Statistics: Without barkskin, the assassin's statistics are AC 23, touch 21,
    flat-footed 17.
ability_scores:
  STR: 12
  DEX: 21
  CON: 12
  INT: 14
  WIS: 14
  CHA: 8
BAB: 9
CMB: 13
CMD: 31
feats:
- name: Deadly Aim
- name: Deflect Arrows
- name: Dodge
- name: Extra Ki
- name: Improved Unarmed Strike
- name: Nimble Moves
- name: Point-Blank Shot
- name: Step Up
- name: Stunning Fist
- name: Weapon Finesse
- name: Weapon Focus (shuriken)
- name: Weapon Focus (unarmed strike)
skills:
  Acrobatics: 21
    when jumping: 42
  Bluff: 6
  Climb: 11
  Diplomacy: 2
  Disguise: 6
  Intimidate: 7
  Knowledge (geography): 5
  Knowledge (local): 5
  Knowledge (nature): 5
  Knowledge (history): 8
  Knowledge (religion): 6
  Perception: 18
  Sense Motive: 12
  Stealth: 21
  Swim: 7
languages:
- Auran
- Common
- Infernal
special_qualities:
- fast movement
- hidden weapons
- high jump
- ki pool (8 points, magic)
- maneuver training
- poison use
- slow fall 40 ft.
- wholeness of body
gear:
  combat:
  - potion of barkskin
  - potion of cure serious wounds
  - potion of haste
  other:
  - +1 human-bane shuriken (5)
  - +1 shuriken (20)
  - adamantine shuriken (10)
  - cold iron shuriken (10)
  - masterwork quarterstaff
  - belt of physical might +2 (Str, Dex)
  - bracers of armor +2
  - cloak of resistance +1
  - ring of protection +1
  - shock amulet of mighty fists
  - 235 gp
desc_long: These monks deal swift and dispassionate death to those who threaten or
  cross their monastery.

---

# Death Initiate

**Source** NPC Codex pg. 209
**XP** 19,200
Human _[[classes/Monk|monk]]_ 9/assassin 4

LE Medium humanoid (human)
**Init** +5; **Senses** Perception +18

##### Defense

**AC** 25, touch 21, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+2 armor, +1 _[[spells/Deflection|deflection]]_, +5 Dex, +1 _[[feats/Dodge|dodge]]_, +2 _monk_, +2 natural, +2 Wis)
**hp** 88 (9d8+4d8+22)
**Fort** +9, **Ref** +14, **Will** +10; +2 vs. enchantments or poison
**Defensive Abilities** improved evasion, uncanny _dodge_; **Immune** disease

##### Offense
**Speed** 60 ft.
**Melee** unarmed strike +15/+10 (1d10+1 plus 1d6 electricity) or mwk _[[items/Weapon/Quarterstaff|quarterstaff]]_ +11/+6 (1d6+1) or flurry of blows (unarmed strike) +16/+16/+11/+11/+6 (1d10+1 plus 1d6 electricity)
**Ranged** +1 shuriken +16/+11 (1d2+2) or flurry of blows (+1 shuriken) +17/+17/+12/+12/+7 (1d2+1)
**Special Attacks** death attack (DC 16), flurry of blows, sneak attack +2d6, _[[feats/Stunning Fist|stunning fist]]_ (10/day, DC 18), true death (DC 19)

### Tactics

**Before Combat **The assassin drinks her potion of _[[spells/Barkskin|barkskin]]_, attempts to study her victim for 3 rounds, and drinks her potion of _[[spells/Haste|haste]]_.
**During Combat **Disguised as a modest pilgrim, the assassin sidles up to her mark and makes her death attack with a _Stunning Fist_ attack. She then retreats to throw flurries of shuriken.
**Base Statistics **Without _barkskin_, the assassin’s statistics are **AC **23, touch 21, _flat-footed_ 17.

##### Statistics
**Str** 12, **Dex** 21, **Con** 12, **Int** 14, **Wis** 14, **Cha** 8
**Base Atk** +9; **CMB** +13; **CMD** 31
**Feats** _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Deflect Arrows|Deflect Arrows]]_, _Dodge_, _[[feats/Extra Ki|Extra Ki]]_, _[[feats/Improved Unarmed Strike|Improved Unarmed Strike]]_, _[[feats/Nimble Moves|Nimble Moves]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Step Up|Step Up]]_, _Stunning Fist_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (shuriken, unarmed strike)
**Skills** Acrobatics +21 (+42 when jumping), Bluff +6, _[[universal monster rules/Climb|Climb]]_ +11, Diplomacy +2, Disguise +6, Intimidate +7, Knowledge (geography, local, nature) +5, Knowledge (history) +8, Knowledge (religion) +6, Perception +18, Sense Motive +12, Stealth +21, Swim +7
**Languages** Auran, Common, Infernal
**SQ** fast movement, hidden weapons, high _[[spells/Jump|jump]]_, ki pool (8 points, magic), maneuver _[[items/Weapon Magic Abilities/Training|training]]_, poison use, _[[spells/Slow|slow]]_ fall 40 ft., wholeness of body
**Combat Gear** potion of _barkskin_, potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_, potion of _haste_; **Other Gear** +1 human-bane shuriken (5), +1 shuriken (20), adamantine shuriken (10), cold iron shuriken (10), masterwork _quarterstaff_, _[[items/Wondrous Item/Belt of Physical Might +2|belt of physical might +2]]_ (Str, Dex), _[[items/Wondrous Item/Bracers of Armor +2|bracers of armor +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Weapon Magic Abilities/Shock|shock]]_ amulet of mighty fists, 235 gp

These monks deal swift and dispassionate death to those who threaten or cross their monastery.
---
cssclass: [monsters]
title1: Giant (Frost), Frost Giant Jarl
title2: Frost Giant Jarl
CR: 18
sources:
- name: Monster Codex
  page: 75
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 153600
race: Frost
classes:
- giant ranger 9
alignment: CE
size: Large
type: humanoid
subtypes:
- cold
- giant
initiative:
  bonus: 4
senses:
  low-light vision: true
AC:
  AC: 35
  touch: 15
  flat_footed: 31
  components:
    armor: 9
    deflection: 2
    dex: 4
    natural: 11
    size: -1
HP:
  HP: 328
  long: 14d8+9d10+216
  HD: 23
saves:
  fort: 26
  ref: 17
  will: 13
defensive_abilities:
- evasion
- rock catching
immunities:
- cold
weaknesses:
- vulnerable to fire
speeds:
  base: 40
attacks:
  melee:
  - - text: +1 warhammer +27/+22/+17/+12 (2d6+12/×3)
      entries:
      - - damage: 2d6+12
          crit_multiplier: 3
      attack: +1 warhammer
      bonus:
      - 27
      - 22
      - 17
      - 12
    - text: +1 warhammer +27/+22/+17 (2d6+12/×3)
      entries:
      - - damage: 2d6+12
          crit_multiplier: 3
      attack: +1 warhammer
      bonus:
      - 27
      - 22
      - 17
  ranged:
  - - text: rock +22 (1d8+16)
      entries:
      - - damage: 1d8+16
      attack: rock
      bonus:
      - 22
  - - text: +1 warhammer +24/+19 (2d6+1/×3)
      entries:
      - - damage: 2d6+1
          crit_multiplier: 3
      attack: +1 warhammer
      bonus:
      - 24
      - 19
  special:
  - combat style (two-weapon)
  - favored enemy (giants +2, humans +4)
  - rock throwing (120 ft.)
space: 10
reach: 10
spells:
  entries:
  - superscripts:
    - UC
    name: communal returning weapon
    source: Ranger
    level: 2
  - superscripts:
    - APG
    name: call animal
    source: Ranger
    level: 1
  - name: charm animal
    source: Ranger
    level: 1
    DC: 12
  - superscripts:
    - APG
    name: lead blades
    source: Ranger
    level: 1
  sources:
  - name: Ranger
    type: prepared
    CL: 6
    concentration: 7
tactics:
  Before Combat: The jarl casts communal returning weapon on his warhammers.
  During Combat: The jarl makes full attacks with his warhammers against targets at
    any range.
ability_scores:
  STR: 32
  DEX: 19
  CON: 27
  INT: 12
  WIS: 12
  CHA: 10
BAB: 19
CMB: 31
CMD: 47
feats:
- name: Double Slice
- superscripts:
  - APG
  name: Dreadful Carnage
- name: Endurance
- superscripts:
  - APG
  name: Furious Focus
- name: Greater Two-Weapon Fighting
- name: Improved Iron Will
- name: Improved Two-Weapon Fighting
- name: Iron Will
- name: Point-Blank Shot
- name: Power Attack
- name: Precise Shot
- name: Toughness
- name: Two-Weapon Fighting
- name: Two-Weapon Rend
- name: Weapon Focus (warhammer)
skills:
  Acrobatics: 8
    when jumping: 12
  Climb: 23
  Diplomacy: 5
  Heal: 9
  Intimidate: 23
  Perception: 24
  Perform (sing): 5
  Sense Motive: 11
  Stealth: 17
    in snow: 21
  Survival: 14
  _racial_mods:
    Acrobatics:
      when jumping: 4
    Stealth:
      in snow: 4
languages:
- Common
- Giant
special_qualities:
- favored terrain (cold +4, forest +2)
- hunter's bond (companions)
- swift tracker
- track +4
- wild empathy +9
- woodland stride
gear:
  combat:
  - potions of cure serious wounds (3)
  - potion of protection from energy (fire)
  - alchemist's fire (2)
  other:
  - +4 chain shirt
  - +1 warhammer (2)
  - amulet of natural armor +2
  - belt of physical might +4 (Dex, Con)
  - boots of the winterlands
  - cloak of resistance +3
  - ring of protection +2
  - stone of alarm
  - 1,886 gp
ecology:
  environment: cold mountains
desc_long: Jarls rule their tribes and subordinates with an iron fist-or a hammer
  to the skull. Jarls take and hold their positions through force. While many might
  wish to see their stations pass on to their progeny, heredity carries little weight
  in frost giant society, and jarls understand that their children can assume power
  only by violently seizing it. As a result, frost giant jarls are hard on their children,
  encouraging sibling rivalries in hopes that one child will eventually prove strong
  enough to rule.

---

# Giant (Frost), Frost Giant Jarl

**Source** Monster Codex pg. 75
**XP** 153,600
Frost giant _[[classes/Ranger|ranger]]_ 9
CE Large humanoid (cold, giant)
**Init** +4; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +24

##### Defense

**AC** 35, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 31 (+9 armor, +2 deflection, +4 Dex, +11 natural, –1 size)
**hp** 328 (23 HD; 14d8+9d10+216)
**Fort** +26, **Ref** +17, **Will** +13
**Defensive Abilities** evasion, _[[universal monster rules/Rock Catching|rock catching]]_; **Immune** cold
**Weaknesses** vulnerable to fire

##### Offense
**Speed** 40 ft.
**Melee** +1 _[[items/Weapon/Warhammer|warhammer]]_ +27/+22/+17/+12 (2d6+12/×3), +1 _warhammer_ +27/+22/+17 (2d6+12/×3)
**Ranged** rock +22 (1d8+16) or +1 _warhammer_ +24/+19 (2d6+1/×3)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** combat style (two-weapon), favored enemy (giants +2, humans +4), _[[universal monster rules/Rock Throwing|rock throwing]]_ (120 ft.)
**_Ranger_ Spells Prepared **(CL 6th; concentration +7)
2nd—communal _[[spells/Returning Weapon|returning weapon]]_
1st—_[[spells/Call Animal|call animal]]_, _[[spells/Charm Animal|charm animal]]_ (DC 12), _[[spells/Lead Blades|lead blades]]_

### Tactics

**Before Combat** The jarl casts communal _returning weapon_ on his warhammers.
 **During Combat** The jarl makes full attacks with his warhammers against targets at any range.

##### Statistics
**Str** 32, **Dex** 19, **Con** 27, **Int** 12, **Wis** 12, **Cha** 10
**Base Atk** +19; **CMB** +31; **CMD** 47
**Feats** _[[feats/Double Slice|Double Slice]]_, _[[feats/Dreadful Carnage|Dreadful Carnage]]_, _[[feats/Endurance|Endurance]]_, _[[feats/Furious Focus|Furious Focus]]_, _[[feats/Greater Two-Weapon Fighting|Greater Two-Weapon Fighting]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Two-Weapon Fighting|Improved Two-Weapon Fighting]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, _[[feats/Two-Weapon Rend|Two-Weapon Rend]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_warhammer_)
**Skills** Acrobatics +8 (+12 when jumping), _[[universal monster rules/Climb|Climb]]_ +23, Diplomacy +5, _[[spells/Heal|Heal]]_ +9, Intimidate +23, Perception +24, Perform (sing) +5, Sense Motive +11, Stealth +17 (+21 in snow), Survival +14; **Racial Modifiers** +4 Acrobatics when jumping, +4 Stealth in snow
**Languages** Common, Giant
**SQ** favored terrain (cold +4, forest +2), _[[classes/Hunter|hunter]]_’s bond (companions), swift tracker, track +4, wild _[[feats/Empathy|empathy]]_ +9, woodland stride
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (3), potion of _[[spells/Protection from Energy|protection from energy]]_ (fire), _[[classes/Alchemist|alchemist]]_’s fire (2); **Other Gear** +4 _[[items/Armor/Chain shirt|chain shirt]]_, +1 _warhammer_ (2), _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Belt of Physical Might +4|belt of physical might +4]]_ (Dex, Con), _[[items/Wondrous Item/Boots of the Winterlands|boots of the winterlands]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +3|cloak of _resistance_ +3]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, _[[items/Wondrous Item/Stone of Alarm|stone of alarm]]_, 1,886 gp

##### Ecology

**Environment** cold mountains

##### Description

Jarls rule their tribes and subordinates with an iron fist—or a _[[items/Mundane/Hammer|hammer]]_ to the skull. Jarls take and hold their positions through force. While many might _[[spells/Wish|wish]]_ to see their stations pass on to their progeny, heredity carries little weight in frost giant society, and jarls understand that their children can assume power only by violently seizing it. As a result, frost giant jarls are hard on their children, encouraging sibling rivalries in hopes that one child will eventually prove strong enough to rule.
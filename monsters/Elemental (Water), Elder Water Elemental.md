---
cssclass: [monsters]
title1: Elemental (Water), Elder Water Elemental
title2: Mythic Elder Water Elemental
CR: 14
MR: 5
sources:
- name: Mythic Adventures
  page: 196
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 38400
alignment: N
size: Huge
type: outsider
subtypes:
- elemental
- extraplanar
- mythic
- water
initiative:
  bonus: 6
senses:
  darkvision: 60
AC:
  AC: 30
  touch: 16
  flat_footed: 22
  components:
    dex: 6
    dodge: 2
    natural: 14
    size: -2
HP:
  HP: 202
  long: 16d10+114
saves:
  fort: 14
  ref: 18
  will: 6
DR:
- amount: 10
  weakness: '-'
immunities:
- elemental traits
speeds:
  base: 20
  swim: 90
attacks:
  melee:
  - - text: 4 slams +24 (2d10+10/18-20 plus grab)
      entries:
      - - damage: 2d10+10
          crit_range: 18-20
        - effect: grab
      count: 4
      attack: slams
      bonus:
      - 24
  special:
  - drench
  - fast swallow
  - mythic power (5/day, surge +1d8)
  - pressure wave
  - smother
  - swallow whole (2d10+10 bludgeoning damage, AC 14, 20 hp, DR 10/-)
  - vortex (at will, 10-60 ft., 2d10+10 damage, DC 28)
  - water mastery
space: 15
reach: 15
ability_scores:
  STR: 30
  DEX: 22
  CON: 19
  INT: 12
  WIS: 13
  CHA: 11
BAB: 16
CMB: 28
CMB_other: +30 bull rush or sunder, +32 grapple
CMD: 48
CMD_other: 50 vs. bull rush or sunder
feats:
- name: Cleave
- is_mythic: true
  name: Dodge
- name: Great Cleave
- name: Improved Bull Rush
- is_mythic: true
  name: Improved Critical (slam)
- name: Improved Sunder
- name: Lightning Reflexes
- is_mythic: true
  name: Power Attack
skills:
  Acrobatics: 25
  Escape Artist: 25
  Knowledge (planes): 20
  Perception: 20
  Sense Motive: 20
  Stealth: 17
  Swim: 37
languages:
- Aquan
ecology:
  environment: any (Plane of Water)
  organization: solitary, pair, or gang (3-8)
  treasure_type: none
special_abilities:
  Drench (Ex): The elemental's touch puts out nonmagical flames of Large size or smaller.
    The creature can dispel magical fire it touches as dispel magic (caster level
    16th).
  Pressure Wave (Su): A mythic water elemental can expend one use of mythic power
    to create a 60-foot-radius bust of pressurized water. Creatures in the area must
    attempt a DC 22 Fort save. Success means the creature is sickened for 1d4 rounds;
    failure means the creature is nauseated for 1d4 rounds and sickened for 1d4 rounds
    after that. If the elemental expends two uses of mythic power, creatures nauseated
    by this ability also take slam damage. Creatures with the aquatic or water subtypes
    are immune to this ability. The save DC is Constitution-based.
  Swallow Whole (Ex): The elemental can use this ability on a creature it has grabbed.
    If a trapped creature cuts itself free, the hole heals itself closed at the start
    of the elemental's next turn, allowing it to use swallow whole again.
  Vortex (Su): A water elemental can create a whirlpool as a standard action, at will
    (as a whirlwind [Bestiary 306], but only underwater and cannot leave the water).
  Water Mastery (Ex): If a water elemental and its opponent are touching water, the
    elemental gains a +1 bonus on attack rolls, damage rolls, and bull rush and overrun
    combat maneuver checks. If it or the opponent are touching the ground, the elemental
    takes a -4 penalty on attack rolls, on damage rolls, and to its CMD to resist
    bull rush and overrun attempts.
desc_long: A mythic water elemental comes from the unknowable depths of its home plane,
  predating the current civilizations and gods. A witness to ancient and bizarre acts
  of life-creation, it is unconcerned about the interests of mortal creatures.

---

# Elemental (Water), Elder Water Elemental

**Source** Pathfinder RPG Bestiary pg. 127
**XP** 12,800

N Huge outsider (elemental, extraplanar, water)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +19

##### Defense

**AC** 24, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+6 Dex, +1 dodge, +9 natural, –2 size)
**hp** 152 (16d10+64)
**Fort** +14, **Ref** +18, **Will** +5
**DR** 10/—; **Immune** elemental traits

##### Offense
**Speed** 20 ft., swim 90 ft.
**Melee** 2 slams +24 (2d10+10/19–20)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _[[spells/Drench|drench]]_, _[[spells/Vortex|vortex]]_ (DC 28), water mastery

##### Statistics
**Str** 30, **Dex** 22, **Con** 19, **Int** 10, **Wis** 11, **Cha** 11
**Base Atk** +16; **CMB** +28; **CMD** 45
**Feats** _[[feats/Cleave|Cleave]]_, _Dodge_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (slam), _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Acrobatics +25, Escape Artist +25, Knowledge (planes) +19, Perception +19, Stealth +17, Swim +37

##### Ecology

**Environment** any (Plane of Water)

Water elementals are patient, relentless creatures made of living fresh or salt water. They prefer to hide or drag their opponents into the water to gain an advantage.

As with other elementals, all water elementals have their own unique shapes and appearances. Most appear as wave-like creatures with vaguely humanoid faces and smaller wave “arms” to either side. Another common form is that of any aquatic creature, such as a _[[monsters/Shark|shark]]_ or _[[monsters/Octopus|octopus]]_, but made entirely out of water.

**Elemental** **Height** **Weight** **_Vortex_ Save DC** **_Vortex_ Height** Small4 ft.34 lb.1310–20 ft. Medium8 ft.280 lbs.1510–30 ft. Large16 ft.2,250 lbs.1910–40 ft. Huge32 ft.18,000 lbs.2210–50 ft. Greater36 ft.21,000 lbs.2510–60 ft. Elder40 ft.24,000 lbs.2810–60 ft.
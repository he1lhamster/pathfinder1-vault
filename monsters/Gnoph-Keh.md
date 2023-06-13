---
cssclass: [monsters]
title1: Gnoph-Keh
desc_short: A vortex of freezing wind swirls around this six-legged, bearlike monstrosity.
  A single horn protrudes from its snarling face.
title2: Gnoph-Keh
CR: 11
sources:
- name: 'Pathfinder #46: Wake of the Watcher'
  page: 84
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderAdventurePath/carrionCrown/v5748btpy8l3e
XP: 12800
alignment: CE
size: Large
type: magical beast
subtypes:
- cold
initiative:
  bonus: 1
senses:
  darkvision: 60
  low-light vision: true
  snow vision: true
auras:
- name: cold
  radius: 30
AC:
  AC: 25
  touch: 10
  flat_footed: 24
  components:
    dex: 1
    natural: 15
    size: -1
HP:
  HP: 147
  long: 14d10+70
saves:
  fort: 14
  ref: 12
  will: 11
immunities:
- cold
weaknesses:
- heat susceptible
- vulnerable to fire
speeds:
  base: 40
attacks:
  melee:
  - - text: 4 claws +20 (1d6+7)
      entries:
      - - damage: 1d6+7
      count: 4
      attack: claws
      bonus:
      - 20
    - text: gore +20 (1d8+7/19-20/x3)
      entries:
      - - damage: 1d8+7
          crit_range: 19-20
          crit_multiplier: 3
      attack: gore
      bonus:
      - 20
  special:
  - blizzard
  - powerful charge (gore, 2d8+14/19-20/x3)
space: 10
reach: 10
ability_scores:
  STR: 24
  DEX: 13
  CON: 20
  INT: 13
  WIS: 20
  CHA: 21
BAB: 14
CMB: 22
CMD: 33
CMD_other: 41 vs. trip
feats:
- name: Bleeding Critical
- name: Critical Focus
- name: Improved Bull Rush
- name: Improved Critical (gore)
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
skills:
  Climb: 24
  Perception: 22
  Stealth: 14
    in snow or on ice: 22
  _racial_mods:
    Stealth:
      in snow or on ice: 8
languages:
- Aklo
special_qualities:
- icewalking
ecology:
  environment: any cold
  organization: solitary, pair, or gathering (3-8)
  treasure_type: standard
special_abilities:
  Blizzard (Su): Once per hour as a standard action, a gnoph-keh can create a stationary
    blizzard that fills a 20-foot-radius spread. The gnoph-keh can place the center
    of this blizzard at any point within its reach. Multiple gnoph-kehs can use the
    aid another action to help a single gnoph-keh create a much larger blizzard-every
    additional gnoph-keh who aids the first increases the area of the blizzard's radius
    by 20 feet. All gnoph-kehs wishing to aid the primary creature must be within
    the area of that gnoph-keh's cold aura. Once created, the blizzard remains active
    for 1 hour if it was created in a cold environment, or for 1 minute if created
    anywhere else. The wind in the blizzard's area blows in a clockwise circular pattern
    at windstorm speeds, restricts visibility as fog does, and makes the region count
    as difficult terrain. A gnoph-keh can move through a blizzard (either one created
    by magic or a naturally occurring blizzard) without penalty.
  Cold Aura (Su): A gnoph-keh radiates an aura of blistering cold in a 30-foot radius.
    Any creature that ends its turn within this area takes 2d6 points of cold damage.
    While in a blizzard (either one created by magic, such as the gnoph-keh's blizzard
    power, or a naturally occurring blizzard), any creature that takes damage from
    a gnoph-keh's cold aura must make a DC 22 Fortitude save to avoid being staggered
    by the numbing cold for 1 round. The save DC is Constitution-based.
  Heat Susceptible (Ex): A gnoph-keh takes a -4 penalty on all saving throws made
    to resist the effects of high temperatures (see page 444 of the Pathfinder RPG
    Core Rulebook). When a gnoph-keh takes damage from heat in this way, and the damage
    is from temperatures in excess of 90º F, the damage the creature takes is always
    lethal damage. In these conditions, the gnoph-keh's cold aura does not function
    at all.
  Icewalking (Ex): This ability works like the spider climb spell, but the surfaces
    the gnoph-keh climbs must be icy. The beast can move across icy surfaces without
    penalty and does not need to make Acrobatics checks to run or charge on ice.
  Snow Vision (Ex): A gnoph-keh can see perfectly well in snowy conditions, and does
    not take any penalties on Perception checks while in snow.
desc_long: The gnoph-keh is a six-legged horned creature vaguely akin to a polar bear
  in shape and outline, yet possessed of a cruel and creative intellect that elevates
  it from the rank of wild beast to murderous warmonger. Covered with a dense pelt
  of shaggy white fur, the gnoph-keh is equally at home walking on two, four, or six
  legs. The creature prefers to travel on all six when using its powerful charge or
  running, but rears up on its hind legs in combat to bring its four front claws to
  bear on its foes. With the gnophkeh's ability to call up and direct powerful blizzards
  matched to its ability to move and see in such conditions without any disadvantage,
  the creature is rightfully feared in the frozen realms where it dwells.

---

# Gnoph-Keh
A _[[spells/Vortex|vortex]]_ of freezing wind swirls around this six-legged, bearlike monstrosity. A single horn protrudes from its snarling face.
**Source** Pathfinder #46: Wake of the _[[monsters/Watcher|Watcher]]_ pg. 84
**XP** 12,800
CE Large magical beast (cold)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, snow _[[spells/Vision|vision]]_; Perception +22
**Aura** cold (30 ft.)

##### Defense

**AC** 25, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+1 Dex, +15 natural, -1 size)
**hp** 147 (14d10+70)
**Fort** +14, **Ref** +12, **Will** +11
**Immune** cold
**Weaknesses** _[[universal monster rules/Heat|heat]]_ susceptible, vulnerable to fire

##### Offense
**Speed** 40 ft.
**Melee** 4 claws +20 (1d6+7), gore +20 (1d8+7/19-20/x3)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** blizzard, _[[universal monster rules/Powerful Charge|powerful charge]]_ (gore, 2d8+14/19-20/x3)

##### Statistics
**Str** 24, **Dex** 13, **Con** 20, **Int** 13, **Wis** 20, **Cha** 21
**Base Atk** +14; **CMB** +22; **CMD** 33 (41 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (gore), _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +24, Perception +22, Stealth +14 (+22 in snow or on ice); **Racial Modifiers** +8 Stealth in snow or on ice
**Languages** Aklo
**SQ** icewalking

##### Ecology

**Environment** any cold
**Organization** solitary, pair, or gathering (3-8)
**Treasure** standard

### Special Abilities

**Blizzard (Su)** Once per hour as a standard action, a _[[monsters/Gnoph-Keh|gnoph-keh]]_ can create a stationary blizzard that fills a 20-foot-radius spread. The _gnoph-keh_ can place the center of this blizzard at any point within its reach. Multiple gnoph-kehs can use the aid another action to help a single _gnoph-keh_ create a much larger blizzard—every additional _gnoph-keh_ who aids the first increases the area of the blizzard’s radius by 20 feet. All gnoph-kehs wishing to aid the primary creature must be within the area of that _gnoph-keh_’s cold aura. Once created, the blizzard remains active for 1 hour if it was created in a cold environment, or for 1 minute if created anywhere else. The wind in the blizzard’s area blows in a clockwise circular pattern at windstorm speeds, restricts visibility as fog does, and makes the region count as difficult terrain. A _gnoph-keh_ can move through a blizzard (either one created by magic or a naturally occurring blizzard) without penalty.

**Cold Aura (Su)** A _gnoph-keh_ radiates an aura of blistering cold in a 30-foot radius. Any creature that ends its turn within this area takes 2d6 points of cold damage. While in a blizzard (either one created by magic, such as the _gnoph-keh_’s blizzard power, or a naturally occurring blizzard), any creature that takes damage from a _gnoph-keh_’s cold aura must make a DC 22 Fortitude save to avoid being _[[conditions/Staggered|staggered]]_ by the numbing cold for 1 round. The save DC is Constitution-based.

**_Heat_ Susceptible (Ex)** A _gnoph-keh_ takes a –4 penalty on all saving throws made to resist the effects of high temperatures (see page 444 of the Pathfinder RPG Core Rulebook). When a _gnoph-keh_ takes damage from _heat_ in this way, and the damage is from temperatures in excess of 90º F, the damage the creature takes is always lethal damage. In these conditions, the _gnoph-keh_’s cold aura does not function at all.

**Icewalking (Ex)** This ability works like the _[[spells/Spider Climb|spider climb]]_ spell, but the surfaces the _gnoph-keh_ climbs must be icy. The beast can move across icy surfaces without penalty and does not need to make Acrobatics checks to run or charge on ice.
**Snow _Vision_ (Ex)** A _gnoph-keh_ can see perfectly well in snowy conditions, and does not take any penalties on Perception checks while in snow.

##### Description

The _gnoph-keh_ is a six-legged horned creature vaguely akin to a polar bear in shape and outline, yet possessed of a _[[items/Weapon Magic Abilities/Cruel|cruel]]_ and creative intellect that elevates it from the rank of wild beast to murderous _[[feats/Warmonger|warmonger]]_. Covered with a dense pelt of shaggy white fur, the _gnoph-keh_ is equally at home walking on two, four, or six legs. The creature prefers to travel on all six when using its _powerful charge_ or running, but rears up on its hind legs in combat to bring its four front claws to bear on its foes. With the gnophkeh’s ability to call up and direct powerful blizzards matched to its ability to move and see in such conditions without any disadvantage, the creature is rightfully feared in the frozen realms where it dwells.
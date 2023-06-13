---
cssclass: [monsters]
title1: Irlgaunt
desc_short: An unwholesome abomination scuttles fluidly forth, its shape combining
  features of both spider and squid under an armor of rugged rock. While stone protuberances
  gird its upper portions, below it is a thing of angry red flesh and soft pink tendrils.
  Two gaping orifices full of tiny barbs split its lower body-a mouthlike slit surrounded
  by numerous narrow red eyes and, above that, an oozing alien aperture.
title2: Irlgaunt
CR: 13
sources:
- name: 'Pathfinder #35: War of the River Kings'
  page: 84
  link: http://paizo.com/pathfinder/adventurePath/kingmaker/v5748btpy8b7u
XP: 25600
alignment: NE
size: Large
type: aberration
initiative:
  bonus: 13
senses:
  darkvision: 60
AC:
  AC: 29
  touch: 18
  flat_footed: 20
  components:
    dex: 9
    natural: 11
    size: -1
HP:
  HP: 133
  long: 14d8+70
saves:
  fort: 9
  ref: 15
  will: 13
DR:
- amount: 10
  weakness: bludgeoning
immunities:
- acid
- cold
speeds:
  base: 40
  climb: 40
attacks:
  melee:
  - - text: 2 slams +17 (1d8+8 plus 1d6 acid)
      entries:
      - - damage: 1d8+8
        - damage: 1d6
          type: acid
      count: 2
      attack: slams
      bonus:
      - 17
    - text: bite +17 (1d8+8)
      entries:
      - - damage: 1d8+8
      attack: bite
      bonus:
      - 17
  ranged:
  - - text: 1 gastrolith +18 (2d6+8 plus 2d6 acid)
      entries:
      - - damage: 2d6+8
        - damage: 2d6
          type: acid
      count: 1
      attack: gastrolith
      bonus:
      - 18
  special:
  - gastrolith
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: stone shape
    source: default
    freq: At will
  sources:
  - name: default
    CL: 14
ability_scores:
  STR: 27
  DEX: 29
  CON: 20
  INT: 16
  WIS: 18
  CHA: 19
BAB: 10
CMB: 19
CMD: 38
CMD_other: 42 vs. trip
feats:
- name: Blind-Fight
- name: Combat Reflexes
- name: Deadly Aim
- name: Improved Initiative
- name: Improved Lightning Reflexes
- name: Lightning Reflexes
- name: Run
skills:
  Acrobatics: 26
    jump: 30
  Climb: 33
  Disguise: 18
  Fly: 0
  Perception: 21
  Stealth: 22
    in rocky terrain: 30
  Survival: 21
  Swim: 25
  _racial_mods:
    Stealth:
      in rocky terrain: 8
languages:
- Aklo
- Common
- Giant
- Terran
special_qualities:
- stone step
ecology:
  environment: any mountains or underground
  organization: solitary, pair, swarm (3-12)
  treasure_type: standard
special_abilities:
  Gastrolith (Ex): Once every 1d4 rounds, an irlgaunt can violently regurgitate a
    clot of brittle stone and digestive acids. This gastrolith is treated as a thrown
    splash weapon with a range increment of 30 feet. In addition to damaging any creature
    struck (as noted above), any creature within 10 feet of the point where the gastrolith
    strikes (whether a creature or a grid intersection) takes 1d6 points of acid damage.
    A gastrolith that misses its target hits a nearby point, just like a normal miss
    with a splash weapon, as detailed on page 202 of the Pathfinder RPG Core Rulebook.
    An irlgaunt has a separate orifice for ejecting gastroliths. Thus, it can make
    a ranged attack in addition to all its normal melee attacks.
  Stone Step (Ex): An irlgaunt can move through any sort of natural difficult terrain
    at its normal speed while in rocky or subterranean terrain. Magically altered
    terrain affects an irlgaunt as normal.
desc_long: |-
  Irlgaunts are large, spider-like aberrations that lurk in mountainous regions and vertical subterranean chasms. While large and imposing, these arachnid-like beings are deceivingly agile, their reflexes fast and movements swift, similar to the darting motions of a hunting insect. Irlgaunts are as quick-witted as they are nimble and have a strong grasp of strategy and tactics. In Iobaria, the beasts are recognized for their eerily patient predations, hiding amid jagged rocks to attack prey and ejecting crippling blasts of rock and digestive acids upon their victims. Irlgaunts typically attack travelers scaling mountain paths with steep cliff sides, using the hazardous terrain to knock unstable hikers to their death, then skittering down the sheer cliff faces to lap up the fleshy pulp below.

  Most irlgaunts stand between 11 and 13 feet tall and weigh around 3,000 pounds.

---

# Irlgaunt
An unwholesome abomination scuttles fluidly forth, its shape combining features of both spider and _[[monsters/Squid|squid]]_ under an armor of rugged rock. While stone protuberances gird its upper portions, below it is a thing of angry red flesh and soft pink tendrils. Two gaping orifices full of tiny barbs _[[universal monster rules/Split|split]]_ its lower body—a mouthlike slit surrounded by numerous narrow red eyes and, above that, an oozing alien aperture.
**Source** Pathfinder #35: War of the River Kings pg. 84
**XP** 25,600

NE Large aberration
**Init** +13; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +21

##### Defense

**AC** 29, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+9 Dex, +11 natural, -1 size)
**hp** 133 (14d8+70)
**Fort** +9, **Ref** +15, **Will** +13
**DR** 10/bludgeoning; **Immune** acid, cold

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 40 ft.
**Melee** 2 slams +17 (1d8+8 plus 1d6 acid), bite +17 (1d8+8)
**Ranged** 1 gastrolith +18 (2d6+8 plus 2d6 acid)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** gastrolith
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th)
At will - _[[spells/Stone Shape|stone shape]]_

##### Statistics
**Str** 27, **Dex** 29, **Con** 20, **Int** 16, **Wis** 18, **Cha** 19
**Base Atk** +10; **CMB** +19; **CMD** 38 (42 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Lightning Reflexes|Improved Lightning Reflexes]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, Run
**Skills** Acrobatics +26 (+30 _[[spells/Jump|jump]]_), _Climb_ +33, Disguise +18, Fly +0, Perception +21, Stealth +22 (+30 in rocky terrain), Survival +21, Swim +25; **Racial Modifiers** +8 Stealth in rocky terrain
**Languages** Aklo, Common, Giant, Terran
**SQ** stone step

##### Ecology

**Environment** any mountains or underground
**Organization** solitary, pair, swarm (3-12)
**Treasure** standard

### Special Abilities

**Gastrolith (Ex)** Once every 1d4 rounds, an _[[monsters/Irlgaunt|irlgaunt]]_ can violently regurgitate a clot of brittle stone and digestive acids. This gastrolith is treated as a thrown splash weapon with a range increment of 30 feet. In addition to damaging any creature struck (as noted above), any creature within 10 feet of the point where the gastrolith strikes (whether a creature or a grid intersection) takes 1d6 points of acid damage. A gastrolith that misses its target hits a nearby point, just like a normal miss with a splash weapon, as detailed on page 202 of the Pathfinder RPG Core Rulebook. An _irlgaunt_ has a separate orifice for ejecting gastroliths. Thus, it can make a ranged attack in addition to all its normal melee attacks.
**Stone Step (Ex)** An _irlgaunt_ can move through any sort of natural difficult terrain at its normal speed while in rocky or subterranean terrain. Magically altered terrain affects an _irlgaunt_ as normal.

##### Description

Irlgaunts are large, spider-like aberrations that lurk in mountainous regions and vertical subterranean chasms. While large and imposing, these arachnid-like beings are deceivingly _[[items/Weapon Magic Abilities/Agile|agile]]_, their reflexes fast and movements swift, similar to the darting motions of a hunting insect. Irlgaunts are as quick-witted as they are nimble and have a strong _[[spells/Grasp|grasp]]_ of strategy and tactics. In Iobaria, the beasts are recognized for their eerily patient predations, hiding amid jagged rocks to attack prey and ejecting crippling blasts of rock and digestive acids upon their victims. Irlgaunts typically attack travelers scaling mountain paths with steep cliff sides, using the hazardous terrain to _[[spells/Knock|knock]]_ unstable hikers to their death, then skittering down the sheer cliff faces to lap up the fleshy pulp below.

Most irlgaunts stand between 11 and 13 feet tall and weigh around 3,000 pounds.
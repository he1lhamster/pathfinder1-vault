---
cssclass: [monsters]
title1: Leshy, Lichen Leshy
desc_short: This miniature plant person has a body composed of lichens and a rain
  cape woven from leafy growths.
title2: Lichen Leshy
CR: 3
sources:
- name: 'Pathfinder #116: Fangs of War'
  page: 86
  link: http://paizo.com/products/btpy9npk
XP: 800
alignment: N
size: Small
type: plant
subtypes:
- leshy
- shapechanger
initiative:
  bonus: 1
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 14
  touch: 12
  flat_footed: 13
  components:
    armor: 1
    dex: 1
    natural: 1
    size: 1
HP:
  HP: 37
  long: 5d8+15
saves:
  fort: 6
  ref: 2
  will: 3
immunities:
- electricity
- plant traits
- sonic
speeds:
  base: 20
  climb: 20
attacks:
  melee:
  - - text: slam +4 (1d4 plus degradation)
      entries:
      - - damage: 1d4
        - effect: degradation
      attack: slam
      bonus:
      - 4
  ranged:
  - - text: filaments +5 (1 plus degradation)
      entries:
      - - damage: '1'
        - effect: degradation
      attack: filaments
      bonus:
      - 5
  special:
  - constrict (2d4 acid)
spell_like_abilities:
  entries:
  - name: endure elements
    source: default
    freq: Constant
  - name: pass without trace
    source: default
    freq: Constant
  sources:
  - name: default
    CL: 10
    concentration: 10
ability_scores:
  STR: 11
  DEX: 12
  CON: 15
  INT: 10
  WIS: 15
  CHA: 10
BAB: 3
CMB: 2
CMD: 13
feats:
- name: Endurance
- name: Skill Focus (Knowledge [geography])
- name: Toughness
skills:
  Climb: 8
  Knowledge (geography): 5
  Perception: 10
  Stealth: 10
    in hills and mountains: 14
  Survival: 3
    in hills and mountains: 7
  _racial_mods:
    Stealth:
      in hills and mountains: 4
    Survival:
      in hills and mountains: 4
languages:
- Druidic
- Sylvan
- plantspeech (lichens)
special_qualities:
- change shape (Small lichen; tree shape)
- expert climber
- verdant burst
- weathering
ecology:
  environment: any hills or mountains
  organization: solitary or patch (2-16)
  treasure_type: standard
special_abilities:
  Degradation (Ex): The lichen leshy's attacks envelop the target in a lattice of
    delicate digestive growths. As a standard action, a creature can tear away any
    such growths. If a creature ends its turn without having removed the growths,
    the tendrils fall away as they release acid that deals 2d4 points of acid damage,
    and the victim must succeed at a DC 14 Fortitude save or become staggered for
    1 round. The save DC is Constitution-based.
  Expert Climber (Ex): A lichen leshy can adhere to nearly any surface, as though
    constantly under a natural version of spider climb.
  Filaments (Ex): A lichen leshy can spit a tangle of filaments as a standard action.
    If it hits, this attack deals 1 point of damage (this damage is not modified by
    Strength) and affects the target with the lichen leshy's degradation ability.
    The filaments have a range increment of 20 feet and a maximum range of 100 feet.
  Weathering (Ex): A lichen leshy can release a slow-acting acid that dissolves stone
    and organic material. By remaining in contact with a 5-foot-square area for 8
    hours, the leshy can deal 3d6 points of acid damage to the surface, ignoring hardness
    less than 10.
desc_long: |-
  Like the curious plantlike organisms from which they're composed, lichen leshys are rugged creatures able to survive in unforgiving climates. Unlike most leshys, lichen leshys are rarely content to stay in one place for long, instead using their survival skills to reach the grandest vistas, harshest environs, and most daring heights. There, they rest in quiet contemplation and awe, slowly breaking down inhospitable rocks into nutrient-rich soil that can sustain new plant life.

  Lichen leshys almost always wear cozy rain cloaks that they use to blur their outlines and better camouflage their forms. They often secret away tiny mementos within their garb to remind them of their greatest achievements, and one can earn a lichen leshy's ready assistance if willing to listen to its rambling tales of how it found each trophy. This mossy clothing functions as masterwork padded armor for a lichen leshy, but not for any other creature.

---

# Leshy, Lichen Leshy
This miniature plant person has a body composed of lichens and a rain cape woven from leafy growths.
**Source** Pathfinder #116: Fangs of War pg. 86
**XP** 800

N Small plant (leshy, shapechanger)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +10

##### Defense

**AC** 14, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+1 armor, +1 Dex, +1 natural, +1 size)
**hp** 37 (5d8+15)
**Fort** +6, **Ref** +2, **Will** +3
**Immune** electricity, _[[universal monster rules/Plant Traits|plant traits]]_, sonic

##### Offense
**Speed** 20 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** slam +4 (1d4 plus degradation)
**Ranged** filaments +5 (1 plus degradation)
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (2d4 acid)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +10)
Constant—_[[spells/Endure Elements|endure elements]]_, _[[spells/Pass without Trace|pass without trace]]_

##### Statistics
**Str** 11, **Dex** 12, **Con** 15, **Int** 10, **Wis** 15, **Cha** 10
**Base Atk** +3; **CMB** +2; **CMD** 13
**Feats** _[[feats/Endurance|Endurance]]_, _[[feats/Skill Focus|Skill Focus]]_ (Knowledge [geography]), _[[feats/Toughness|Toughness]]_
**Skills** _Climb_ +8, Knowledge (geography) +5, Perception +10, Stealth +10 (+14 in hills and mountains), Survival +3 (+7 in hills and mountains); **Racial Modifiers** +4 Stealth and Survival in hills and mountains
**Languages** Druidic, Sylvan; plantspeech (lichens)
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (Small lichen; _[[spells/Tree Shape|tree shape]]_), expert climber, verdant burst, weathering

##### Ecology

**Environment** any hills or mountains
**Organization** solitary or patch (2–16)
**Treasure** standard

### Special Abilities

**Degradation (Ex)** The lichen leshy’s attacks envelop the target in a lattice of delicate digestive growths. As a standard action, a creature can tear away any such growths. If a creature ends its turn without having removed the growths, the tendrils fall away as they release acid that deals 2d4 points of acid damage, and the victim must succeed at a DC 14 Fortitude save or become _[[conditions/Staggered|staggered]]_ for 1 round. The save DC is Constitution-based.

**Expert Climber (Ex)** A lichen leshy can adhere to nearly any surface, as though constantly under a natural version of _[[spells/Spider Climb|spider climb]]_.

**Filaments (Ex)** A lichen leshy can spit a tangle of filaments as a standard action. If it hits, this attack deals 1 point of damage (this damage is not modified by Strength) and affects the target with the lichen leshy’s degradation ability. The filaments have a range increment of 20 feet and a maximum range of 100 feet.

**Weathering (Ex)** A lichen leshy can release a slow-acting acid that dissolves stone and organic material. By remaining in contact with a 5-foot-square area for 8 hours, the leshy can deal 3d6 points of acid damage to the surface, ignoring hardness less than 10.

##### Description

Like the curious plantlike organisms from which they’re composed, lichen leshys are rugged creatures able to survive in unforgiving climates. Unlike most leshys, lichen leshys are rarely content to stay in one place for long, instead using their survival skills to reach the grandest vistas, harshest environs, and most daring heights. There, they rest in quiet contemplation and awe, slowly _[[items/Weapon Magic Abilities/Breaking|breaking]]_ down inhospitable rocks into nutrient-rich soil that can sustain new plant life.

Lichen leshys almost always wear cozy rain cloaks that they use to _[[spells/Blur|blur]]_ their outlines and better camouflage their forms. They often secret away tiny mementos within their garb to remind them of their greatest achievements, and one can earn a lichen leshy’s ready assistance if willing to listen to its rambling tales of how it found each trophy. This mossy clothing functions as masterwork _[[items/Armor/Padded armor|padded armor]]_ for a lichen leshy, but not for any other creature.
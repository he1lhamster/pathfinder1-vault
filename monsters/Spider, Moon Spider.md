---
cssclass: [monsters]
title1: Spider, Moon Spider
desc_short: Pale and round-bodied, this giant spider is the size of a large dog. Its
  crimson eyes glitter with malign intelligence.
title2: Moon Spider
CR: 2
sources:
- name: The Emerald Spire Superdungeon
  page: 156
  link: http://paizo.com/products/btpy8yqx?Pathfinder-Module-The-Emerald-Spire-Superdungeon
XP: 600
alignment: NE
size: Medium
type: magical beast
initiative:
  bonus: 6
senses:
  darkvision: 60
  low-light vision: true
  tremorsense: 60
AC:
  AC: 14
  touch: 12
  flat_footed: 12
  components:
    dex: 2
    natural: 2
HP:
  HP: 22
  long: 3d10+6
saves:
  fort: 5
  ref: 5
  will: 3
speeds:
  base: 30
  climb: 30
attacks:
  melee:
  - - text: bite +4 (1d6+1 plus poison)
      entries:
      - - damage: 1d6+1
        - effect: poison
      attack: bite
      bonus:
      - 4
  special:
  - poison
  - web (+11 ranged touch, DC 19, 10 hp, DR 5/slashing)
spell_like_abilities:
  entries:
  - name: obscuring mist
    source: default
    freq: 3/day
  - name: gaseous form
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 5
    concentration: 3
ability_scores:
  STR: 12
  DEX: 15
  CON: 14
  INT: 5
  WIS: 14
  CHA: 7
BAB: 3
CMB: 4
CMD: 16
feats:
- name: Ability Focus (poison)
- name: Improved Initiative
skills:
  Climb: 21
  Perception: 10
  Stealth: 10
  _racial_mods:
    Climb:
      _: 16
    Perception:
      _: 4
    Stealth:
      _: 4
languages:
- Common (can't speak)
special_qualities:
- moon spider webs
ecology:
  environment: temperate forest
  organization: solitary, pair, or colony (3-8)
  treasure_type: standard
special_abilities:
  Moon Spider Webs (Ex): |-
    The webs created by a moon spider are especially strong and sticky, and the creatures weave net-like snares to trap their enemies. A moon spider's web attack is a ranged touch attack with a +6 racial bonus to the save DC needed to burst or escape the web. The spider also holds a trailing tether that prevents an entangled creature from moving away from the spider until it gets free.

    Moon spiders frequently set web traps throughout areas where they live. Anyone who enters a square of moon spider web must succeed at a Reflex save (DC 13) or become entangled as though it had been hit by a web attack (though the spider doesn't have a tether to it). If a creature that is already entangled enters a square of moon spider web, it must save again or become grappled. The save DC is Constitution-based.

    A moon spider's webs have 10 hit points and DR 5/slashing. A web that's set on fire takes an additional 1d6 points of fire damage each round until it's destroyed.
  Poison (Ex): Bite-injury; save Fort DC 15; frequency 1/round for 5 rounds; effect
    1d3 Str; cure 1 save.
desc_long: |-
  Moon spiders are malevolent giant spiders that haunt the Echo Wood and other forests in the western vales of the Sellen River. They are far more intelligent than most of their arachnid kin; while they aren't as smart as humans, they possess a sly cunning and magical talents that make them much more dangerous than other giant spiders-they even hunt cooperatively and share their kills.

  Moon spiders are web-weavers, and often create huge traps of sticky webbing. A creature that enters a square of moon spider webbing can easily become entangled or grappled. Typically, a moon spider uses its obscuring mist to hide the extent of its webs when prey approaches, using its tremorsense to keep track of its prey's struggles.

  Moon spiders do not speak any humanoid language, but communicate with each other in clicks and taps of their legs on the ground, and they can understand simple concepts in Common (which is useful when they're listening to prey).

---

# Spider, Moon Spider
Pale and round-bodied, this giant spider is the size of a large _[[monsters/Dog|dog]]_. Its crimson eyes glitter with malign intelligence.
**Source** The Emerald Spire Superdungeon pg. 156
**XP** 600

NE Medium magical beast
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 60 ft.; Perception +10

##### Defense

**AC** 14, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+2 Dex, +2 natural)
**hp** 22 (3d10+6)
**Fort** +5, **Ref** +5, **Will** +3

##### Offense
**Speed** 30 ft., _[[universal monster rules/Climb|climb]]_ 30 ft.
**Melee** bite +4 (1d6+1 plus poison)
**Special Attacks** poison, web (+11 ranged touch, DC 19, 10 hp, DR 5/slashing)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +3)
3/day—_[[spells/Obscuring Mist|obscuring mist]]_
1/day—_[[spells/Gaseous Form|gaseous form]]_

##### Statistics
**Str** 12, **Dex** 15, **Con** 14, **Int** 5, **Wis** 14, **Cha** 7
**Base Atk** +3; **CMB** +4; **CMD** 16
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (poison), _[[feats/Improved Initiative|Improved Initiative]]_
**Skills** _Climb_ +21, Perception +10, Stealth +10; **Racial Modifiers** +16 _Climb_, +4 Perception, +4 Stealth
**Languages** Common (can’t speak)
**SQ** moon spider webs

##### Ecology

**Environment** temperate forest
**Organization** solitary, pair, or colony (3–8)
**Treasure** standard

### Special Abilities

**Moon Spider Webs (Ex)** The webs created by a moon spider are especially strong and _[[items/Weapon Magic Abilities/Sticky|sticky]]_, and the creatures weave net-like snares to trap their enemies. A moon spider’s web attack is a ranged touch attack with a +6 racial bonus to the save DC needed to burst or escape the web. The spider also holds a trailing tether that prevents an _[[conditions/Entangled|entangled]]_ creature from moving away from the spider until it gets free.

Moon spiders frequently set web traps throughout areas where they live. Anyone who enters a square of moon spider web must succeed at a Reflex save (DC 13) or become _entangled_ as though it had been hit by a web attack (though the spider doesn’t have a tether to it). If a creature that is already _entangled_ enters a square of moon spider web, it must save again or become _[[conditions/Grappled|grappled]]_. The save DC is Constitution-based.

A moon spider’s webs have 10 hit points and DR 5/slashing. A web that’s set on fire takes an additional 1d6 points of fire damage each round until it’s destroyed.

**Poison (Ex)** Bite—injury; save Fort DC 15; frequency 1/round for 5 rounds; effect 1d3 Str; cure 1 save.

##### Description

Moon spiders are _[[items/Armor Magic Abilities/Malevolent|malevolent]]_ giant spiders that haunt the _[[spells/Echo|Echo]]_ Wood and other forests in the western vales of the Sellen River. They are far more intelligent than most of their arachnid kin; while they aren’t as smart as humans, they possess a sly _[[items/Weapon Magic Abilities/Cunning|cunning]]_ and magical talents that make them much more dangerous than other giant spiders—they even hunt cooperatively and share their kills.

Moon spiders are web-weavers, and often create huge traps of _sticky_ webbing. A creature that enters a square of moon spider webbing can easily become _entangled_ or _grappled_. Typically, a moon spider uses its _obscuring mist_ to hide the extent of its webs when prey approaches, using its _tremorsense_ to keep track of its prey’s struggles.

Moon spiders do not speak any humanoid language, but communicate with each other in clicks and taps of their legs on the ground, and they can understand simple concepts in Common (which is useful when they’re listening to prey).
---
cssclass: [monsters]
title1: Golem, Brass Golem
desc_short: This towering brass statue, built to resemble an evil horned humanoid,
  carries a gigantic curved sword in its metal fists.
title2: Brass Golem
CR: 14
sources:
- name: Bestiary 3
  page: 134
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
- name: 'Pathfinder #24: The Final Wish'
  page: 84
  link: http://paizo.com/pathfinder/adventurePath/legacyOfFire/v5748btpy89a2
XP: 38400
alignment: N
size: Huge
type: construct
initiative:
  bonus: 0
senses:
  darkvision: 60
  low-light vision: true
  see invisibility: true
AC:
  AC: 30
  touch: 8
  flat_footed: 30
  components:
    natural: 22
    size: -2
HP:
  HP: 150
  long: 20d10+40
saves:
  fort: 6
  ref: 6
  will: 7
DR:
- amount: 15
  weakness: adamantine
immunities:
- construct traits
- fire
- magic
speeds:
  base: 40
attacks:
  melee:
  - - text: brass falchion +29 (3d6+11/18-20 plus 2d6 fire)
      entries:
      - - damage: 3d6+11
          crit_range: 18-20
        - damage: 2d6
          type: fire
      attack: brass falchion
      bonus:
      - 29
    - text: slam +29 (2d6+11 plus 2d6 fire)
      entries:
      - - damage: 2d6+11
        - damage: 2d6
          type: fire
      attack: slam
      bonus:
      - 29
  special:
  - breath weapon (DC 20)
  - heat (2d6 fire)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: see invisibility
    source: default
    freq: Constant
  sources:
  - name: default
    CL: 17
    concentration: 12
ability_scores:
  STR: 32
  DEX: 11
  CON:
  INT:
  WIS: 13
  CHA: 1
BAB: 20
CMB: 33
CMD: 43
skills: {}
special_qualities:
- death throes
- brass falchion
ecology:
  environment: any
  organization: solitary or watch (2-4)
  treasure_type: none
special_abilities:
  Brass Falchion (Ex): A brass golem's falchion deals damage as a Huge falchion, but
    is actually a primary natural attack, not a manufactured weapon, and cannot be
    disarmed.
  Breath Weapon (Su): As a free action once every 1d4 rounds, a brass golem can expel
    a cloud of smoke and cinders that fills a 20-foot cube. This functions as an incendiary
    cloud that persists for 1d6 rounds, dealing 6d6 points of fire damage (DC 20 Reflex
    for half). The save DC is Constitution-based.
  Death Throes (Ex): A brass golem explodes when it is destroyed. All creatures within
    30 feet of the golem take 12d8 points of fire damage (DC 20 Reflex for half).
    The save DC is Constitution-based.
  Immunity to Magic (Ex): A brass golem is immune to any spell or spell-like ability
    that allows spell resistance. In addition, certain spells and effects function
    differently against the creature. A magical attack that deals cold damage slows
    a brass golem (as per the slow spell) for 1d6 rounds, with no saving throw.A magical
    attack that deals fire damage breaks any slow effect on the golem and heals 1
    point of damage for each 3 points of damage the attack would otherwise deal. If
    the amount of healing would cause the golem to exceed its full normal hit points,
    it gains any excess as temporary hit points. A brass golem gets no save against
    fire effects.
desc_long: Implacable automatons of elemental fire and extraplanar brass, brass golems
  stand sentinel over the palaces, treasuries, and harems of their creators. Brass
  golems are 24 feet tall and weigh 18,000 pounds.

---

# Golem, Brass Golem
This towering brass _[[spells/Statue|statue]]_, built to resemble an evil horned humanoid, carries a gigantic curved sword in its metal fists.
**Source** Bestiary 3 pg. 134, Pathfinder #24: The Final _[[spells/Wish|Wish]]_ pg. 84
**XP** 38,400

N Huge construct
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +1

##### Defense

**AC** 30, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+22 natural, –2 size)
**hp** 150 (20d10+40)
**Fort** +6, **Ref** +6, **Will** +7
**DR** 15/adamantine; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_, fire, magic

##### Offense
**Speed** 40 ft.
**Melee** brass _[[items/Weapon/Falchion|falchion]]_ +29 (3d6+11/18–20 plus 2d6 fire), slam +29 (2d6+11 plus 2d6 fire)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (DC 20), _[[universal monster rules/Heat|heat]]_ (2d6 fire)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +12)
Constant—_see invisibility_

##### Statistics
**Str** 32, **Dex** 11, **Con** —, **Int** —, **Wis** 13, **Cha** 1
**Base Atk** +20; **CMB** +33; **CMD** 43
**SQ** death throes, brass _falchion_

##### Ecology

**Environment** any
**Organization** solitary or watch (2–4)
**Treasure** none

### Special Abilities

**Brass _Falchion_ (Ex)** A brass golem’s _falchion_ deals damage as a Huge _falchion_, but is actually a primary natural attack, not a manufactured weapon, and cannot be disarmed.

**_Breath Weapon_ (Su)** As a free action once every 1d4 rounds, a brass golem can expel a cloud of smoke and cinders that fills a 20-foot cube. This functions as an _[[spells/Incendiary Cloud|incendiary cloud]]_ that persists for 1d6 rounds, dealing 6d6 points of fire damage (DC 20 Reflex for half). The save DC is Constitution-based.

**Death Throes (Ex)** A brass golem explodes when it is destroyed. All creatures within 30 feet of the golem take 12d8 points of fire damage (DC 20 Reflex for half). The save DC is Constitution-based.

**_[[universal monster rules/Immunity|Immunity]]_ to Magic (Ex)** A brass golem is immune to any spell or spell-like ability that allows _[[universal monster rules/Spell Resistance|spell resistance]]_. In addition, certain spells and effects function differently against the creature.

* A magical attack that deals cold damage slows a brass golem (as per the _[[spells/Slow|slow]]_ spell) for 1d6 rounds, with no saving throw.
* A magical attack that deals fire damage breaks any _slow_ effect on the golem and heals 1 point of damage for each 3 points of damage the attack would otherwise deal. If the amount of healing would cause the golem to exceed its full normal hit points, it gains any excess as temporary hit points. A brass golem gets no save against fire effects.

##### Description

Implacable automatons of elemental fire and extraplanar brass, brass golems stand sentinel over the palaces, treasuries, and harems of their creators. Brass golems are 24 feet tall and weigh 18,000 pounds.
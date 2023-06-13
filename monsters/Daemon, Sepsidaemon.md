---
cssclass: [monsters]
title1: Daemon, Sepsidaemon
desc_short: A long-beaked, crested head on a twisted neck rises from a formless, glowing
  mass of a body. Now and then, a grasping claw extends forth.
title2: Sepsidaemon
CR: 7
sources:
- name: Book of the Damned
  page: 243
  link: http://paizo.com/products/btpy9tok
XP: 3200
alignment: NE
size: Medium
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 8
senses:
  dakrvision: 60
  scent: true
auras:
- name: septic wounds
  radius: 30
AC:
  AC: 20
  touch: 14
  flat_footed: 16
  components:
    dex: 4
    natural: 6
HP:
  HP: 85
  long: 9d10+36
saves:
  fort: 10
  ref: 10
  will: 7
defensive_abilities:
- amorphous
DR:
- amount: 10
  weakness: good or silver
immunities:
- acid
- death effects
- disease
- poison
resistances:
  cold: 10
  electricity: 10
  fire: 10
SR: 18
speeds:
  base: 30
  swim: 30
attacks:
  melee:
  - - text: bite +13 (1d8+4 plus 1d6 acid and disease)
      entries:
      - - damage: 1d8+4
        - damage: 1d6
          type: acid
        - effect: disease
      attack: bite
      bonus:
      - 13
    - text: 2 claws +14 (1d4+4/19-20 plus 1d6 acid and disease)
      entries:
      - - damage: 1d4+4
          crit_range: 19-20
        - damage: 1d6
          type: acid
        - effect: disease
      count: 2
      attack: claws
      bonus:
      - 14
  special:
  - necrotic slough
spell_like_abilities:
  entries:
  - name: contagion
    source: default
    freq: At will
    DC: 17
  - name: dimension door
    source: default
    freq: At will
  - name: summon
    source: default
    freq: 1/day
    level: 3
    summons:
    - name: sepsidaemon
      amount: 1
      chance: 40%
  sources:
  - name: default
    CL: 7
    concentration: 10
ability_scores:
  STR: 18
  DEX: 19
  CON: 18
  INT: 13
  WIS: 14
  CHA: 17
BAB: 9
CMB: 13
CMD: 27
feats:
- name: Improved Critical (claw)
- name: Improved Initiative
- name: Iron Will
- name: Power Attack
- name: Weapon Focus (claw)
skills:
  Climb: 16
  Intimidate: 15
  Knowledge (planes): 13
  Perception: 14
  Stealth: 16
  Survival: 14
  Swim: 24
languages:
- Abyssal
- Draconic
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Abaddon)
  organization: solitary, pair, or infection (3-8)
  treasure_type: standard
special_abilities:
  Disease (Ex): 'Fleshweep: injury; save Fort DC 18; onset immediate; frequency 1/day;
    effect 1 Con damage and 1d3 Dex damage; cure 2 consecutive saves. The save DC
    is Constitution-based.'
  Necrotic Slough (Ex): As it moves, the sepsidaemon covers the ground with portions
    of its festering body, transforming any square it passes through into difficult
    terrain for 2 rounds, after which the filth evaporates. A creature that passes
    through or starts its turn in one of these squares must succeed at a DC 18 Reflex
    save or take 2d6 points of acid damage and become nauseated for 1 round; the nausea
    effect is a disease effect. A creature can be affected by this acid damage and
    nauseated condition only once per round. The save DC is Constitution-based.
  Septic Wounds Aura (Su): A sepsidaemon radiates an aura that causes wounds to fester.
    If a creature with lethal hit point damage begins its turn within 30 feet of a
    sepsidaemon, it must succeed at a DC 18 Fortitude save or become infected with
    fleshweep (see Disease above). This is a disease effect.
desc_long: Sepsidaemons embody the concept of death by gangrene, infection, and necrotic
  decay. Spawned in Abaddon from the evil souls of those who experienced horrific
  deaths under septic conditions, these daemons are most prominent in the areas of
  Apollyon's domain where the waters of the Styx intrude and leach away life and memories.
  A sepsidaemon continually hunts, feeds, and appropriates the essences of creatures.
  These fiends perpetually slough a trail of necrotic flesh and exude a fearsome aura
  that festers and corrupts wounds. A sepsidaemon fuses its victims' misappropriated
  forms to its amorphous core, where they dangle like rotting jewelry. Although sepsidaemons
  typically roam alone or in loose pairs, they are at their most fearsome when they
  form groups led by one of Apollyon's leukodaemon deacons.

---

# Daemon, Sepsidaemon
A long-beaked, crested head on a twisted neck rises from a formless, glowing mass of a body. Now and then, a grasping claw extends forth.
**Source** _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_ pg. 243
**XP** 3,200

NE Medium outsider (daemon, evil, extraplanar)
**Init** +8; **Senses** dakrvision 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +14
**Aura** septic wounds (30 ft.)

##### Defense

**AC** 20, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+4 Dex, +6 natural)
**hp** 85 (9d10+36)
**Fort** +10, **Ref** +10, **Will** +7
**Defensive Abilities** _[[universal monster rules/Amorphous|amorphous]]_; **DR** 10/good or silver; **Immune** acid, death effects, disease, poison; **Resist** cold 10, electricity 10, fire 10; **SR** 18

##### Offense
**Speed** 30 ft., swim 30 ft.
**Melee** bite +13 (1d8+4 plus 1d6 acid and disease), 2 claws +14 (1d4+4/19-20 plus 1d6 acid and disease)
**Special Attacks** necrotic _[[spells/Slough|slough]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +10)
At will—_[[spells/Contagion|contagion]]_ (DC 17), _[[spells/Dimension Door|dimension door]]_ 
1/day—_[[universal monster rules/Summon|summon]]_ (level 3, 1 sepsidaemon 40%)

##### Statistics
**Str** 18, **Dex** 19, **Con** 18, **Int** 13, **Wis** 14, **Cha** 17
**Base Atk** +9; **CMB** +13; **CMD** 27
**Feats** _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** _[[universal monster rules/Climb|Climb]]_ +16, Intimidate +15, Knowledge (planes) +13, Perception +14, Stealth +16, Survival +14, Swim +24
**Languages** Abyssal, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary, pair, or infection (3-8)
**Treasure** standard

### Special Abilities

**Disease (Ex)** Fleshweep: injury; save Fort DC 18; onset immediate; frequency 1/day; effect 1 Con damage and 1d3 Dex damage; cure 2 consecutive saves. The save DC is Constitution-based.

**Necrotic _Slough_ (Ex)** As it moves, the sepsidaemon covers the ground with portions of its festering body, transforming any square it passes through into difficult terrain for 2 rounds, after which the filth evaporates. A creature that passes through or starts its turn in one of these squares must succeed at a DC 18 Reflex save or take 2d6 points of acid damage and become _[[conditions/Nauseated|nauseated]]_ for 1 round; the nausea effect is a disease effect. A creature can be affected by this acid damage and _nauseated_ condition only once per round. The save DC is Constitution-based.
**Septic Wounds Aura (Su)** A sepsidaemon radiates an aura that causes wounds to _[[spells/Fester|fester]]_. If a creature with lethal hit point damage begins its turn within 30 feet of a sepsidaemon, it must succeed at a DC 18 Fortitude save or become infected with fleshweep (see Disease above). This is a disease effect.

##### Description

Sepsidaemons embody the concept of death by gangrene, infection, and necrotic decay. Spawned in Abaddon from the evil souls of those who experienced horrific deaths under septic conditions, these daemons are most prominent in the areas of Apollyon’s domain where the waters of the Styx intrude and leach away life and memories. A sepsidaemon continually hunts, feeds, and appropriates the essences of creatures. These fiends perpetually _slough_ a trail of necrotic flesh and exude a fearsome aura that festers and corrupts wounds. A sepsidaemon fuses its victims’ misappropriated forms to its _amorphous_ core, where they dangle like rotting _[[items/Mundane/Jewelry|jewelry]]_. Although sepsidaemons typically roam alone or in loose pairs, they are at their most fearsome when they form groups led by one of Apollyon’s leukodaemon deacons.
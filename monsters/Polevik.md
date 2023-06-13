---
cssclass: [monsters]
title1: Polevik
desc_short: Toadstools, puff balls, and other bizarre fungal growths sprout from this
  small, hunchbacked man's mold-streaked body. His beady eyes burn with paranoia and
  malice.
title2: Polevik
CR: 5
sources:
- name: 'Pathfinder #63: The Asylum Stone'
  page: 90
  link: http://paizo.com/products/btpy8sds?Pathfinder-Adventure-Path-63-The-Asylum-Stone
XP: 1600
alignment: NE
size: Small
type: fey
initiative:
  bonus: 4
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: putrefying aura
  radius: 30
  DC: 18
AC:
  AC: 17
  touch: 15
  flat_footed: 13
  components:
    dex: 4
    natural: 2
    size: 1
HP:
  HP: 60
  long: 8d6+32
saves:
  fort: 6
  ref: 10
  will: 7
DR:
- amount: 5
  weakness: cold iron
immunities:
- disease
- nausea
- poison
- sickened condition
speeds:
  base: 20
attacks:
  melee:
  - - text: bite +8 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: bite
      bonus:
      - 8
  ranged:
  - - text: puffballs +9 (1d6 plus disease)
      entries:
      - - damage: 1d6
        - effect: disease
      attack: puffballs
      bonus:
      - 9
spell_like_abilities:
  entries:
  - name: speak with plants
    source: default
    freq: Constant
    other: fungi and mold only
  sources:
  - name: default
    CL: 7
    concentration: 9
ability_scores:
  STR: 16
  DEX: 18
  CON: 19
  INT: 15
  WIS: 9
  CHA: 8
BAB: 4
CMB: 6
CMD: 20
feats:
- name: Alertness
- name: Iron Will
- name: Point-Blank Shot
- name: Precise Shot
skills:
  Acrobatics: 8
    when jumping: 4
  Craft (alchemy): 17
  Heal: 7
  Knowledge (dungeoneering): 10
  Knowledge (nature): 13
  Perception: 12
  Sense Motive: 10
  Stealth: 19
    in caves or swamps: 23
  Survival: 7
    in caves or swamps: 11
  Swim: 7
  _racial_mods:
    Craft (alchemy):
      _: 4
    Stealth:
      in caves or swamps: 4
    Survival:
      in caves or swamps: 4
languages:
- Aklo
- Common
- Sylvan
- Undercommon
special_qualities:
- fungal alchemy
ecology:
  environment: any swamp or underground
  organization: solitary
  treasure_type: standard
  treasure:
  - alchemical items
  - other treasure
special_abilities:
  Disease (Ex): |-
    Pulsing puffs is a disease characterized by small, blue-white spores sprouting within a creature's wounds. These spores quickly grow into phosphorescent, domed mounds that pulsate and throb, eating away at victims' connective tissue, severely impairing them. Additionally, once a creature takes 7 points of Dexterity damage from the pulsing puffs, the domed mounds burst, releasing a 10-foot-radius burst of diseased spores. This effect lasts for 1 round. Any creature caught within the burst radius or that moves through it is exposed to the pulsing puffs disease. The save DC is Constitution-based.

    Pulsing Puffs: Puffball-injury; save Fort DC 18; onset 1 minute; frequency 1/day; effect 1d6 Dex damage; cure 2 consecutive saves.
  Fungal Alchemy (Ex): As long as he has access to his fungus garden, a polevik can
    craft any alchemical item with a Craft DC of 25 or lower without needing to pay
    a cost in gold pieces for raw materials. Items function normally but may have
    a different appearance. For example, materials usually stored in glass jars instead
    fill rigid spheres of plant matter.
  Puffballs (Ex): Poleviks have learned how to nurture myriad species of symbiotic
    fungi upon their bodies, and the most treasured of these are their deadly puffballs.
    Each 6-inchdiameter spherical fungus has a thorny internal stalk covered by a
    thin skin of spore-laden flesh. As a standard action that does not provoke an
    attack of opportunity, a polevik can pluck and throw a puffball with a range of
    20 feet. On a successful hit, the thorns expand and pulsate on impact, bursting
    through the flesh of the puffball. This inflicts vicious wounds and releases fungal
    spores that infect the victim with pulsing puffs. As soon as a puffball has been
    plucked, another grows in its place. Once a puffball has been plucked, it decomposes
    after 1 round, becoming inert.
  Putrefying Aura (Su): All unattended nonmagical food or liquid within the radius
    of a polevik's aura instantly rots or spoils. Attended nonmagical food or liquid
    within the aura receives a saving throw to resist this effect. The save DC is
    Constitution-based.
desc_long: |-
  The secretive and suspicious poleviks cultivate gardens of fungi in deep bogs and caves far from civilization, jealously guarding the secrets of their fungal alchemy from the rest of the world. Once natives of the First World, they retain some of that plane's potent life energy, which specifically encourages the growth of fungi and molds. This enables them to turn their own spry and twisted bodies into fertile ground in which to cultivate their signature puffball weapons.

  Averaging a few inches shy of 4 feet tall and weighing approximately 115 pounds, individuals can vary in size depending on the number and size of fungal growths that they nurture upon their bodies. They rarely live beyond 300 years.

---

# Polevik
Toadstools, puff balls, and other bizarre fungal growths sprout from this small, hunchbacked man’s mold-streaked body. His beady eyes _[[universal monster rules/Burn|burn]]_ with _[[spells/Paranoia|paranoia]]_ and malice.
**Source** Pathfinder #63: The Asylum Stone pg. 90
**XP** 1,600

NE Small fey
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +12
**Aura** putrefying aura (30 ft., DC 18)

##### Defense

**AC** 17, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+4 Dex, +2 natural, +1 size)
**hp** 60 (8d6+32)
**Fort** +6, **Ref** +10, **Will** +7
**DR** 5/cold iron; **Immune** disease, nausea, poison, _[[conditions/Sickened|sickened]]_ condition

##### Offense
**Speed** 20 ft.
**Melee** bite +8 (1d6+3)
**Ranged** puffballs +9 (1d6 plus disease)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +9)
Constant—_[[spells/Speak with Plants|speak with plants]]_ (fungi and mold only)

##### Statistics
**Str** 16, **Dex** 18, **Con** 19, **Int** 15, **Wis** 9, **Cha** 8
**Base Atk** +4; **CMB** +6; **CMD** 20
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_
**Skills** Acrobatics +8 (+4 when jumping), Craft (alchemy) +17, _[[spells/Heal|Heal]]_ +7, Knowledge (dungeoneering) +10, Knowledge (nature) +13, Perception +12, Sense Motive +10, Stealth +19 (+23 in caves or swamps), Survival +7 (+11 in caves or swamps), Swim +7; **Racial Modifiers** +4 Craft (alchemy), +4 Stealth in caves or swamps, +4 Survival in caves or swamps
**Languages** Aklo, Common, Sylvan, Undercommon
**SQ** fungal alchemy

##### Ecology

**Environment** any swamp or underground
**Organization** solitary
**Treasure** standard (alchemical items, other treasure)

### Special Abilities

**Disease (Ex) **_[[diseases/Pulsing Puffs|Pulsing puffs]]_ is a disease characterized by small, blue-white spores sprouting within a creature’s wounds. These spores quickly grow into phosphorescent, domed mounds that pulsate and throb, eating away at victims’ connective tissue, severely impairing them. Additionally, once a creature takes 7 points of Dexterity damage from the _pulsing puffs_, the domed mounds burst, releasing a 10-foot-radius burst of diseased spores. This effect lasts for 1 round. Any creature caught within the burst radius or that moves through it is exposed to the _pulsing puffs_ disease. The save DC is Constitution-based.

_Pulsing Puffs_: Puffball—injury; save Fort DC 18; onset 1 minute; frequency 1/day; effect 1d6 Dex damage; cure 2 consecutive saves.

**Fungal Alchemy (Ex)** As long as he has access to his fungus garden, a _[[monsters/Polevik|polevik]]_ can craft any alchemical item with a Craft DC of 25 or lower without needing to pay a cost in gold pieces for raw materials. Items function normally but may have a different appearance. For example, materials usually stored in glass jars instead fill rigid spheres of plant matter.

**Puffballs (Ex)** Poleviks have learned how to nurture myriad species of symbiotic fungi upon their bodies, and the most treasured of these are their _[[items/Weapon Magic Abilities/Deadly|deadly]]_ puffballs. Each 6-inchdiameter spherical fungus has a thorny internal stalk covered by a thin skin of spore-laden flesh. As a standard action that does not provoke an attack of opportunity, a _polevik_ can pluck and throw a puffball with a range of 20 feet. On a successful hit, the thorns expand and pulsate on _[[items/Weapon Magic Abilities/Impact|impact]]_, bursting through the flesh of the puffball. This inflicts _[[items/Weapon Magic Abilities/Vicious|vicious]]_ wounds and releases fungal spores that infect the victim with _pulsing puffs_. As soon as a puffball has been plucked, another grows in its place. Once a puffball has been plucked, it decomposes after 1 round, becoming inert.

**Putrefying Aura (Su)** All unattended nonmagical food or liquid within the radius of a _polevik_’s aura instantly rots or spoils. Attended nonmagical food or liquid within the aura receives a saving throw to resist this effect. The save DC is Constitution-based.

##### Description

The secretive and suspicious poleviks cultivate gardens of fungi in deep bogs and caves far from civilization, jealously _[[items/Armor Magic Abilities/Guarding|guarding]]_ the secrets of their fungal alchemy from the rest of the world. Once natives of the First World, they retain some of that plane’s _[[items/Weapon Magic Abilities/Potent|potent]]_ life energy, which specifically encourages the growth of fungi and molds. This enables them to turn their own spry and twisted bodies into fertile ground in which to cultivate their signature puffball weapons.

Averaging a few inches shy of 4 feet tall and weighing approximately 115 pounds, individuals can vary in size depending on the number and size of fungal growths that they nurture upon their bodies. They rarely live beyond 300 years.
---
cssclass: [monsters]
title1: Kapre
desc_short: Roots and branches twist across this oddly proportioned creature to form
  knots of muscle. Its eyes burn like embers.
title2: Kapre
CR: 10
sources:
- name: Bestiary 4
  page: 172
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
- name: 'Pathfinder #58: Island of Empty Eyes'
  page: 86
  link: http://paizo.com/pathfinder/adventurePath/skullAndShackles/v5748btpy8mog
XP: 9600
alignment: CN
size: Huge
type: plant
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: confounding
  radius: 100
  DC: 21
AC:
  AC: 24
  touch: 10
  flat_footed: 22
  components:
    dex: 2
    natural: 14
    size: -2
HP:
  HP: 127
  long: 15d8+60
saves:
  fort: 12
  ref: 9
  will: 9
DR:
- amount: 10
  weakness: slashing
immunities:
- plant traits
speeds:
  base: 50
  climb: 30
attacks:
  melee:
  - - text: 2 slams +17 (2d6+12)
      entries:
      - - damage: 2d6+12
      count: 2
      attack: slams
      bonus:
      - 17
  special:
  - blow smoke
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: speak with plants
    source: default
    freq: Constant
  - name: invisibility
    source: default
    freq: At will
  sources:
  - name: default
    CL: 14
    concentration: 18
ability_scores:
  STR: 26
  DEX: 15
  CON: 17
  INT: 12
  WIS: 15
  CHA: 18
BAB: 11
CMB: 21
CMD: 33
feats:
- name: Alertness
- name: Combat Reflexes
- name: Diehard
- name: Endurance
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
- name: Toughness
skills:
  Climb: 20
  Disable Device: 11
  Perception: 22
  Sense Motive: 9
  Stealth: 18
  Survival: 9
  _racial_mods:
    Perception:
      _: 8
    Stealth:
      _: 8
languages:
- Common
- speak with plants
special_qualities:
- tree meld
ecology:
  environment: warm or temperate forests
  organization: solitary
  treasure_type: none
special_abilities:
  Blow Smoke (Su): Smoke constantly drifts from a kapre's mouth, and as a standard
    action it can exhale a 30-foot cone of smoke. Any creature in the area must succeed
    at a DC 20 Fortitude save or be nauseated for 1 round. This is a poison effect,
    and the save DC is Constitution-based.
  Confounding Aura (Su): A magical aura surrounds a kapre, confusing and distracting
    its foes. Within a kapre's aura, the DC of all Survival checks is increased by
    15, and creatures trained in Survival are no longer able to automatically determine
    true north. On top of this, any creature within a kapre's aura must succeed at
    a DC 21 Will saving throw when it enters the area or take a -4 penalty on concentration
    checks, initiative checks, and skill checks. A kapre can suppress this aura at
    will.
  Tree Meld (Su): A kapre can meld with any tree, similar to how the spell meld with
    stone functions. It can remain melded with a tree as long as it wishes.
desc_long: |-
  Vehement defenders of the unusual locations of the natural world, kapres have a complicated relationship with the “civilized” races. Formed of dense tree matter, they are as much part of the forest as their botanical brethren. Their intimidating physical size, territorial nature, and unusual approach to friendship often bring them into conf lict with local tribes and aggressive explorers. With slender limbs and thick, gnarled torsos, kapres are awkwardly humanoid in appearance, and if not for the soft glow of their eyes they could be mistaken for treants.

  Exceedingly secretive and wary, kapres prefer to avoid conf lict, using their imposing size and confounding auras to intimidate any would-be invaders. Leaning out of huge trees, they blow smoke onto lost explorers, persuading them to flee.

---

# Kapre
Roots and branches twist across this oddly proportioned creature to form knots of muscle. Its eyes _[[universal monster rules/Burn|burn]]_ like embers.
**Source** Bestiary 4 pg. 172, Pathfinder #58: Island of Empty Eyes pg. 86
**XP** 9,600

CN Huge plant
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +22
**Aura** _[[items/Weapon Magic Abilities/Confounding|confounding]]_ (100 ft., DC 21)

##### Defense

**AC** 24, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+2 Dex, +14 natural, –2 size)
**hp** 127 (15d8+60)
**Fort** +12, **Ref** +9, **Will** +9
**DR** 10/slashing; **Immune** _[[universal monster rules/Plant Traits|plant traits]]_

##### Offense
**Speed** 50 ft., _[[universal monster rules/Climb|climb]]_ 30 ft.
**Melee** 2 slams +17 (2d6+12)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** blow smoke
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +18)
Constant—_[[spells/Speak with Plants|speak with plants]]_
At will—_[[spells/Invisibility|invisibility]]_

##### Statistics
**Str** 26, **Dex** 15, **Con** 17, **Int** 12, **Wis** 15, **Cha** 18
**Base Atk** +11; **CMB** +21; **CMD** 33
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Diehard|Diehard]]_, _[[feats/Endurance|Endurance]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_
**Skills** _Climb_ +20, Disable Device +11, Perception +22, Sense Motive +9, Stealth +18, Survival +9; **Racial Modifiers** +8 Perception, +8 Stealth
**Languages** Common; _speak with plants_
**SQ** tree meld

##### Ecology

**Environment** warm or temperate forests
**Organization** solitary
**Treasure** none

### Special Abilities

**Blow Smoke (Su)** Smoke constantly drifts from a _[[monsters/Kapre|kapre]]_’s mouth, and as a standard action it can exhale a 30-foot cone of smoke. Any creature in the area must succeed at a DC 20 Fortitude save or be _[[conditions/Nauseated|nauseated]]_ for 1 round. This is a poison effect, and the save DC is Constitution-based.

**_Confounding_ Aura (Su)** A magical aura surrounds a _kapre_, confusing and _[[items/Weapon Magic Abilities/Distracting|distracting]]_ its foes. Within a _kapre_’s aura, the DC of all Survival checks is increased by 15, and creatures trained in Survival are no longer able to automatically determine true north. On top of this, any creature within a _kapre_’s aura must succeed at a DC 21 Will saving throw when it enters the area or take a –4 penalty on concentration checks, initiative checks, and skill checks. A _kapre_ can suppress this aura at will.

**Tree Meld (Su)** A _kapre_ can meld with any tree, similar to how the spell meld with stone functions. It can remain melded with a tree as long as it wishes.

##### Description

Vehement defenders of the unusual locations of the natural world, kapres have a complicated relationship with the “civilized” races. Formed of dense tree matter, they are as much part of the forest as their botanical brethren. Their intimidating physical size, territorial nature, and unusual approach to friendship often bring them into conf lict with local tribes and aggressive explorers. With slender limbs and thick, gnarled torsos, kapres are awkwardly humanoid in appearance, and if not for the soft glow of their eyes they could be mistaken for treants.

Exceedingly secretive and wary, kapres prefer to avoid conf lict, using their imposing size and _confounding_ auras to intimidate any would-be invaders. Leaning out of huge trees, they blow smoke onto lost explorers, persuading them to flee.
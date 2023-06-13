---
cssclass: [monsters]
title1: Leshy, Gourd Leshy
desc_short: This little plant man walks on legs like tangled vines and has a pumpkin
  carved with eyes and a mouth for a head.
title2: Gourd Leshy
CR: 1
sources:
- name: Bestiary 3
  page: 178
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 400
alignment: N
size: Small
type: plant
subtypes:
- leshy
- shapechanger
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 13
  touch: 13
  flat_footed: 11
  components:
    dex: 2
    size: 1
HP:
  HP: 9
  long: 1d8+5
saves:
  fort: 4
  ref: 2
  will: 0
immunities:
- electricity
- sonic
- plant traits
speeds:
  base: 20
attacks:
  melee:
  - - text: slam -1 (1d3-2 plus ensnare)
      entries:
      - - damage: 1d3-2
        - effect: ensnare
      attack: slam
      bonus:
      - -1
  ranged:
  - - text: seed +3 (1 plus ensnare)
      entries:
      - - damage: '1'
        - effect: ensnare
      attack: seed
      bonus:
      - 3
  special:
  - sneak attack +1d6
spell_like_abilities:
  entries:
  - name: pass without trace
    source: default
    freq: Constant
  sources:
  - name: default
    CL: 2
    concentration: 4
ability_scores:
  STR: 6
  DEX: 15
  CON: 14
  INT: 6
  WIS: 11
  CHA: 15
BAB: 0
CMB: -3
CMD: 9
feats:
- name: Toughness
skills:
  Perception: 4
  Stealth: 6
    in plains and undergrowth: 10
  Survival: 0
    in plains and undergrowth: 4
  _racial_mods:
    Stealth:
      _: 4
languages:
- Druidic
- Sylvan
- plantspeech (gourds)
special_qualities:
- change shape (Small gourd; tree shape)
- keepsake
- verdant burst
ecology:
  environment: any hills or plains
  organization: solitary or patch (2-16)
  treasure_type: standard
special_abilities:
  Ensnare (Ex): The seeds and slam attack of a gourd leshy entangle the target in
    vines for 2d4 rounds unless the target makes a DC 12 Reflex save. The target can
    attempt to burst these entangling vines before the duration expires with a DC
    12 Strength check as a full-round action. The save and burst DCs are Constitution-based.
  Keepsake (Su): Gourd leshys can pop off the top of their heads and store a single
    Fine-sized object such as a dagger or potion inside. While within the leshy's
    head, the item is warded by nondetection. In addition, after 24 hours, the item
    within is cleaned and polished, and, if damaged, repaired as if by a mending spell.
    Both spell effects have a caster level equal to twice the leshy's Hit Dice (CL
    2nd for most gourd leshys).
  Seed (Ex): A gourd leshy can hurl its seeds as a ranged attack. If it hits, this
    attack deals 1 point of damage (this damage is not modified by Strength) and affects
    the target with the gourd leshy's ensnare ability. This attack has a 10-foot range
    increment.
desc_long: |-
  With tangles of leafy vines for limbs and a carved gourd for a head, gourd leshys present a rather comical appearance. Intimately connected with the harvest season, gourd leshys see to the health and sustainable harvest of crops, especially vegetables and grains.

  Superstition and love of rituals run deep in gourd leshys. They do their best to exactly reproduce what worked before with every trivial activity, and change seemingly random details when attempting tasks they previously failed. Gourd leshys collect random odds and ends as good luck charms, ranging from polished stones to bird feathers to tarnished coins. Credulous to a fault, gourd leshys believe nearly anything they hear from those they trust. However, their admittedly hollow heads still hold memories, and a gourd leshy betrayed rarely forgets.

  As gourd leshys aren't particularly strong, they often fight dirty. One favorite trick is to wait for an enemy to come within striking distance while in gourd form so that they can assume their true form and make a sneak attack in the same round.

---

# Leshy, Gourd Leshy
This little plant man walks on legs like tangled vines and has a pumpkin carved with eyes and a mouth for a head.
**Source** Bestiary 3 pg. 178
**XP** 400

N Small plant (leshy, shapechanger)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +4

##### Defense

**AC** 13, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 11 (+2 Dex, +1 size)
**hp** 9 (1d8+5)
**Fort** +4, **Ref** +2, **Will** +0
**Immune** electricity, sonic, _[[universal monster rules/Plant Traits|plant traits]]_

##### Offense
**Speed** 20 ft.
**Melee** slam –1 (1d3–2 plus ensnare)
**Ranged** seed +3 (1 plus ensnare)
**Special Attacks** sneak attack +1d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 2nd; concentration +4)
Constant—_[[spells/Pass without Trace|pass without trace]]_

##### Statistics
**Str** 6, **Dex** 15, **Con** 14, **Int** 6, **Wis** 11, **Cha** 15
**Base Atk** +0; **CMB** –3; **CMD** 9
**Feats** _[[feats/Toughness|Toughness]]_
**Skills** Perception +4, Stealth +6 (+10 in plains and undergrowth), Survival +0 (+4 in plains and undergrowth); **Racial Modifiers** +4 Stealth 
**Languages** Druidic, Sylvan; plantspeech (gourds)
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (Small gourd; _[[spells/Tree Shape|tree shape]]_), keepsake, verdant burst

##### Ecology

**Environment** any hills or plains
**Organization** solitary or patch (2–16)
**Treasure** standard

### Special Abilities

**Ensnare (Ex) **The seeds and slam attack of a gourd leshy _[[spells/Entangle|entangle]]_ the target in vines for 2d4 rounds unless the target makes a DC 12 Reflex save. The target can attempt to burst these entangling vines before the duration expires with a DC 12 Strength check as a full-round action. The save and burst DCs are Constitution-based.

**Keepsake (Su) **Gourd leshys can pop off the top of their heads and store a single Fine-sized object such as a _[[items/Weapon/Dagger|dagger]]_ or potion inside. While within the leshy’s head, the item is warded by _[[spells/Nondetection|nondetection]]_. In addition, after 24 hours, the item within is cleaned and polished, and, if damaged, repaired as if by a _[[spells/Mending|mending]]_ spell. Both spell effects have a caster level equal to twice the leshy’s Hit Dice (CL 2nd for most gourd leshys).
**Seed (Ex)** A gourd leshy can hurl its seeds as a ranged attack. If it hits, this attack deals 1 point of damage (this damage is not modified by Strength) and affects the target with the gourd leshy’s ensnare ability. This attack has a 10-foot range increment.

##### Description

With tangles of leafy vines for limbs and a carved gourd for a head, gourd leshys present a rather comical appearance. Intimately connected with the _[[spells/Harvest Season|harvest season]]_, gourd leshys see to the health and sustainable harvest of crops, especially vegetables and grains.

Superstition and love of rituals run deep in gourd leshys. They do their best to exactly reproduce what worked before with every trivial activity, and change seemingly random details when attempting tasks they previously failed. Gourd leshys collect random odds and ends as good luck charms, ranging from polished stones to bird feathers to tarnished coins. Credulous to a fault, gourd leshys believe nearly anything they hear from those they trust. However, their admittedly hollow heads still hold memories, and a gourd leshy _[[feats/Betrayed|betrayed]]_ rarely forgets.

As gourd leshys aren’t particularly strong, they often fight dirty. One favorite trick is to wait for an enemy to come within striking distance while in gourd form so that they can assume their _[[spells/True Form|true form]]_ and make a sneak attack in the same round.
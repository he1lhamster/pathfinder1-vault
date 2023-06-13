---
cssclass: [monsters]
title1: Leshy, Flytrap Leshy
desc_short: This cluster of flytraps has a vaguely humanoid shape. The beadyeyes atop
  the largest flytrap glare menacingly.
title2: Flytrap Leshy
CR: 4
sources:
- name: Bestiary 5
  page: 156
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 1200
alignment: N
size: Small
type: plant
subtypes:
- leshy
- shapechanger
initiative:
  bonus: 6
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 17
  touch: 13
  flat_footed: 15
  components:
    dex: 2
    natural: 4
    size: 1
HP:
  HP: 39
  long: 6d8+12
saves:
  fort: 7
  ref: 4
  will: 4
immunities:
- electricity
- plant traits
- sonic
resistances:
  fire: 5
speeds:
  base: 20
attacks:
  melee:
  - - text: bite +7 (1d4+1 plus 1d4 acid and digest)
      entries:
      - - damage: 1d4+1
        - damage: 1d4
          type: acid
        - effect: digest
      attack: bite
      bonus:
      - 7
    - text: 2 flytrap hands +7(1d3+1 plus 1d3 acid and digest)
      entries:
      - - damage: 1d3+1
        - damage: 1d3
          type: acid
        - effect: digest
      count: 2
      attack: flytrap hands
      bonus:
      - 7
  ranged:
  - - text: acidic spittle +7 (1d4 acid and digest)
      entries:
      - - damage: 1d4
          type: acid
        - effect: digest
      attack: acidic spittle
      bonus:
      - 7
  special:
  - digest
  - sneak attack +1d6
spell_like_abilities:
  entries:
  - name: pass without trace
    source: default
    freq: Constant
    CL: 12
  sources:
  - name: default
    CL: 10
    concentration: 12
ability_scores:
  STR: 12
  DEX: 15
  CON: 14
  INT: 10
  WIS: 15
  CHA: 15
BAB: 4
CMB: 4
CMD: 16
feats:
- name: Combat Reflexes
- name: Improved Initiative
- name: Weapon Focus (bite)
skills:
  Intimidate: 8
  Perception: 11
  Stealth: 6
    inwetlands: 10
  Survival: 0
    in wetlands: 4
  _racial_mods:
    Stealth:
      in wetlands: 4
    Survival:
      in wetlands: 4
languages:
- Druidic
- Sylvan
- plantspeech (flytraps)
special_qualities:
- amalgam
- change shape (small flytrap; tree shape),verdant burst
ecology:
  environment: warm marshesor wetlands
  organization: solitary orcluster (4-8)
  treasure_type: standard
special_abilities:
  Amalgam (Ex): Multipleflytrap leshys can combinethemselves temporarily intoa single
    creature, to amaximum of 25 leshys.Each leshy beyond thefirst grants the amalgam
    1 Hit Die, and itgains a size category at 9, 12, 18, and 30 HitDice. The amalgam
    has a number of bite attacksequal to the number of bites of all component leshyscombined,
    but only two flytrap hands attacks. If theamalgam drops below 0 hit points, it
    dissolves, and thedamage is divided among the component leshys.
  Digest (Ex): A creature that takes acid damage from a flytrapleshy's bites or spittle
    must succeed at a DC 15 Fortitudesave or become sickened for 1d4 rounds. The save
    DCis Constitution-based.
  Flytrap Hands (Ex): In addition to the central flytrap thatserves as its head, a
    flytrap leshy has two additional,smaller flytraps that serve as its hands. These
    handsfunction as the bite of a Tiny creature.
desc_long: |-
  Most leshys are peaceful creatures that focus their effortson tending the natural region around them. While flytrapleshys do not leave their homes to pick fights, they relishthe opportunity to attack intruders. These carnivorousplants tend to attack before asking questions. While theyrarely work together with other creatures, the aggressivecreatures eagerly collaborate with others of their kind.They fight best in teams, and coordinate with each otherso seamlessly that a group of f lytrap leshys is nearlyindistinguishable from a single creature-an illusion thatthe similarity between a flytrap leshy's head and handsonly compounds. While a typical flytrap leshy has onehead and two hands, more powerful flytrap leshys existwith greater numbers of heads and hands.

  Cantankerous flytrap leshys represent the harshand seemingly cruel aspects of the natural cycle thatare ultimately needed for the greater well-being ofall creatures. When necessary to protect their homes,flytrap leshys start controlled fires, relying on their fireresistance to wade through the flames.

  Unlike most of their kind, flytrap leshys eat f lesh andare not picky about the kind of meat that they consume.They particularly savor insects, and one of the few waysto placate a flytrap leshy is to offer it a rare or unusualinsect to consume.

  A typical flytrap leshy is 2 feet talland weighs 20 pounds.

---

# Leshy, Flytrap Leshy
This cluster of flytraps has a vaguely humanoid shape. The beady

eyes atop the largest flytrap glare menacingly.
**Source** Bestiary 5 pg. 156
**XP** 1,200

N Small plant (leshy, shapechanger)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +11

##### Defense

**AC** 17, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+2 Dex, +4 natural, +1 size)
**hp** 39 (6d8+12)
**Fort** +7, **Ref** +4, **Will** +4
**Immune** electricity, _[[universal monster rules/Plant Traits|plant traits]]_, sonic; **Resist** fire 5

##### Offense
**Speed** 20 ft.
**Melee** bite +7 (1d4+1 plus 1d4 acid and digest), 2 flytrap hands +7

(1d3+1 plus 1d3 acid and digest)
**Ranged** acidic spittle +7 (1d4 acid and digest)
**Special Attacks** digest, sneak attack +1d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +12)
Constant—_[[spells/Pass without Trace|pass without trace]]_ (CL 12th)

##### Statistics
**Str** 12, **Dex** 15, **Con** 14, **Int** 10, **Wis** 15, **Cha** 15
**Base Atk** +4; **CMB** +4; **CMD** 16
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Intimidate +8, Perception +11, Stealth +6 (+10 in

wetlands), Survival +0 (+4 in wetlands); **Racial Modifiers**

+4 Stealth in wetlands, +4 Survival in wetlands
**Languages** Druidic, Sylvan; plantspeech (flytraps)
**SQ** amalgam, _[[universal monster rules/Change Shape|change shape]]_ (small flytrap; _[[spells/Tree Shape|tree shape]]_),

verdant burst

##### Ecology

**Environment** warm marshes

or wetlands
**Organization** solitary or

cluster (4–8)
**Treasure** standard

### Special Abilities

**Amalgam (Ex)** Multiple

flytrap leshys can combine

themselves temporarily into

a single creature, to a

maximum of 25 leshys.

Each leshy beyond the

first grants the amalgam 1 Hit Die, and it

gains a size category at 9, 12, 18, and 30 Hit

Dice. The amalgam has a number of bite attacks

equal to the number of bites of all component leshys

combined, but only two flytrap hands attacks. If the

amalgam drops below 0 hit points, it dissolves, and the

damage is divided among the component leshys.

**Digest (Ex)** A creature that takes acid damage from a flytrap

leshy’s bites or spittle must succeed at a DC 15 Fortitude

save or become _[[conditions/Sickened|sickened]]_ for 1d4 rounds. The save DC

is Constitution-based.

**Flytrap Hands (Ex)** In addition to the central flytrap that

serves as its head, a flytrap leshy has two additional,

smaller flytraps that serve as its hands. These hands

function as the bite of a Tiny creature.

##### Description

Most leshys are _[[items/Weapon Magic Abilities/Peaceful|peaceful]]_ creatures that focus their efforts

on tending the natural region around them. While flytrap

leshys do not leave their homes to pick fights, they relish

the opportunity to attack intruders. These carnivorous

plants tend to attack before asking questions. While they

rarely work together with other creatures, the aggressive

creatures eagerly collaborate with others of their kind.

They fight best in teams, and coordinate with each other

so seamlessly that a group of f lytrap leshys is nearly

indistinguishable from a single creature—an illusion that

the similarity between a flytrap leshy’s head and hands

only compounds. While a typical flytrap leshy has one

head and two hands, more powerful flytrap leshys exist

with greater numbers of heads and hands.

Cantankerous flytrap leshys represent the harsh

and seemingly _[[items/Weapon Magic Abilities/Cruel|cruel]]_ aspects of the natural cycle that

are ultimately needed for the greater well-being of

all creatures. When necessary to protect their homes,

flytrap leshys start controlled fires, relying on their fire

_[[universal monster rules/Resistance|resistance]]_ to wade through the flames.

Unlike most of their kind, flytrap leshys eat f lesh and

are not picky about the kind of meat that they consume.

They particularly savor insects, and one of the few ways

to placate a flytrap leshy is to offer it a rare or unusual

insect to consume.

A typical flytrap leshy is 2 feet tall

and weighs 20 pounds.
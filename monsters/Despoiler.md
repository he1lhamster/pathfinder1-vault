---
cssclass: [monsters]
title1: Despoiler
desc_short: Three spears of obsidian energy skewer this cadaverous figure.
title2: Despoiler
CR: 7
sources:
- name: Seers of the Drowned City
  page: 56
  link: http://paizo.com/products/btpy9op2?Pathfinder-Module-Seers-of-the-Drowned-City
XP: 3200
alignment: CE
size: Medium
type: undead
initiative:
  bonus: 7
senses:
  darkvision: 60
AC:
  AC: 20
  touch: 14
  flat_footed: 16
  components:
    dex: 3
    dodge: 1
    natural: 6
HP:
  HP: 85
  long: 10d8+40
saves:
  fort: 7
  ref: 8
  will: 9
immunities:
- undead traits
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 claws +13 (1d6+6 plus 1d6 negative energy and grab)
      entries:
      - - damage: 1d6+6
        - damage: 1d6
          type: negative energy
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 13
  ranged:
  - - text: black shard +10 (4d6 negative energy)
      entries:
      - - damage: 4d6
          type: negative energy
      attack: black shard
      bonus:
      - 10
  special:
  - black shards
  - embrace of darkness
ability_scores:
  STR: 23
  DEX: 17
  CON:
  INT: 12
  WIS: 14
  CHA: 19
BAB: 7
CMB: 13
CMD: 27
feats:
- name: Combat Reflexes
- name: Dodge
- name: Improved Initiative
- name: Lightning Reflexes
- name: Mobility
skills:
  Climb: 19
  Intimidate: 17
  Knowledge (religion): 14
  Perception: 15
  Stealth: 16
languages:
- Common
- Necril
ecology:
  environment: any land
  organization: solitary, pair, or cult (3-6)
  treasure_type: standard
special_abilities:
  Black Shards (Ex): As a standard action, a despoiler can remove and throw a shard
    as a bolt of negative energy to a range of 80 feet, dealing 4d6 points of negative
    energy damage on a hit. A creature that takes damage from a black shard must succeed
    at a DC 19 Fortitude save or be staggered from the pain for 1d4 rounds. A despoiler
    can impale itself on a shard in this way to heal itself of 4d6 points of damage.
    Once a shard is used, it must be replenished via the despoiler's embrace of darkness
    ability. The save DC is Charisma-based.
  Embrace of Darkness (Su): If a despoiler pins a grappled creature, it deals 4d6
    points of negative energy damage and staggers the victim for 1d3 rounds. When
    a despoiler uses this ability, it regrows a black shard (to a maximum of 3 black
    shards). A successful DC 19 Will save halves the damage and prevents the staggered
    condition and shard regrowth. The save DC is Charisma-based.
desc_long: Created from the remains of good clerics, despoilers sometimes guard desecrated
  sacred sites.

---

# Despoiler
Three spears of obsidian energy skewer this cadaverous figure.
**Source** Seers of the Drowned City pg. 56
**XP** 3,200
CE Medium undead
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +15

##### Defense

**AC** 20, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+3 Dex, +1 _[[feats/Dodge|dodge]]_, +6 natural)
**hp** 85 (10d8+40)
**Fort** +7, **Ref** +8, **Will** +9
**Immune** _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 30 ft.
**Melee** 2 claws +13 (1d6+6 plus 1d6 negative energy and _[[universal monster rules/Grab|grab]]_)
**Ranged** black shard +10 (4d6 negative energy)
**Special Attacks** black shards, embrace of _[[spells/Darkness|darkness]]_

##### Statistics
**Str** 23, **Dex** 17, **Con** —, **Int** 12, **Wis** 14, **Cha** 19
**Base Atk** +7; **CMB** +13; **CMD** 27
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +19, Intimidate +17, Knowledge (religion) +14, Perception +15, Stealth +16
**Languages** Common, Necril

##### Ecology

**Environment** any land
**Organization** solitary, pair, or cult (3–6)
**Treasure** standard

### Special Abilities

**Black Shards (Ex)** As a standard action, a _[[monsters/Despoiler|despoiler]]_ can remove and throw a shard as a bolt of negative energy to a range of 80 feet, dealing 4d6 points of negative energy damage on a hit. A creature that takes damage from a black shard must succeed at a DC 19 Fortitude save or be _[[conditions/Staggered|staggered]]_ from the pain for 1d4 rounds. A _despoiler_ can impale itself on a shard in this way to _[[spells/Heal|heal]]_ itself of 4d6 points of damage. Once a shard is used, it must be replenished via the _despoiler_’s embrace of _darkness_ ability. The save DC is Charisma-based.

**Embrace of _Darkness_ (Su)** If a _despoiler_ pins a _[[conditions/Grappled|grappled]]_ creature, it deals 4d6 points of negative energy damage and staggers the victim for 1d3 rounds. When a _despoiler_ uses this ability, it regrows a black shard (to a maximum of 3 black shards). A successful DC 19 Will save halves the damage and prevents the _staggered_ condition and shard regrowth. The save DC is Charisma-based.

##### Description

Created from the remains of good clerics, despoilers sometimes _[[npcs/Guard|guard]]_ desecrated _[[items/Weapon Magic Abilities/Sacred|sacred]]_ sites.
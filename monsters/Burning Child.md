---
cssclass: [monsters]
title1: Burning Child
desc_short: The smell of scorched flesh accompanies this small child, who appears
  to be made entirely of dust and smoldering ash.
title2: Burning Child
CR: 10
sources:
- name: Belkzen, Hold of the Orc Hordes
  page: 58
  link: http://paizo.com/products/btpy97lw?Pathfinder-Campaign-Setting-Belkzen-Hold-of-the-Orc-Hordes
XP: 9600
alignment: CN
size: Small
type: undead
subtypes:
- fire
initiative:
  bonus: 7
auras:
- name: elemental aura
  other:
  - fire
  DC: 17
- name: frightful presence
  radius: 60
  DC: 21
AC:
  AC: 17
  touch: 15
  flat_footed: 13
  components:
    dex: 3
    dodge: 1
    natural: 2
    size: 1
HP:
  HP: 150
  long: 15d8+75
saves:
  fort: 9
  ref: 12
  will: 11
defensive_abilities:
- channel resistance +4
- final embrace
immunities:
- fire
- undead traits
weaknesses:
- vulnerable to cold
speeds:
  base: 40
attacks:
  melee:
  - - text: slam +10 (1d4-2 plus burn)
      entries:
      - - damage: 1d4-2
        - effect: burn
      attack: slam
      bonus:
      - 10
  special:
  - breath weapon (60-ft. cone, 10d6 fire damage, Reflex DC 21 half)
  - burn (2d8, DC 21)
spell_like_abilities:
  entries:
  - superscripts:
    - APG
    name: elemental aura
    source: default
    freq: Constant
    other: fire only
    DC: 17
  - superscripts:
    - ARG
    name: fire trail
    source: default
    freq: Constant
    DC: 17
  - name: burning hands
    source: default
    freq: At will
    DC: 16
  - name: scorching ray
    source: default
    freq: At will
    DC: 16
  - name: quickened fireball
    source: default
    freq: 3/day
    DC: 17
  sources:
  - name: default
    CL: 11
    concentration: 15
ability_scores:
  STR: 6
  DEX: 17
  CON:
  INT: 10
  WIS: 15
  CHA: 18
BAB: 7
CMB: 14
CMD: 17
feats:
- name: Dodge
- name: Improved Initiative
- name: Lightning Reflexes
- name: Quicken Spell-Like Ability (fireball)
- name: Toughness
- name: Weapon Finesse
skills:
  Escape Artist: 18
  Intimidate: 19
  Perception: 17
  Sense Motive: 17
languages:
- Common
special_qualities:
- binary state
ecology:
  environment: temperate plains
  organization: unique
  treasure_type: none
special_abilities:
  Binary State (Su): Most of the time the Burning Child is in a passive state, during
    which he's incorporeal and invisible, though his soft sobs and the scent of burning
    flesh allow a creature to pinpoint his location with a successful DC 30 Perception
    check. If the Burning Child comes across a battle, the chance he enters his active
    state is equal to 1% per creature fighting (to a maximum of 100%). While active,
    the Burning Child is corporeal and visible. After 1d4 hours without being attacked
    or seeing conflict, the Burning Child reenters his passive state.
  Breath Weapon (Su): The Burning Child can use his breath weapon only when in his
    active state, and only once each time he becomes active.
  Final Embrace (Ex): If the Burning Child is destroyed, he reforms in 2d4 days. He
    can be permanently destroyed only when active, by a humanoid embracing and calming
    him. This requires succeeding at DC 28 Diplomacy checks for 3 consecutive rounds.
desc_long: |-
  Born from the traumatic death of an abducted human child at the hands of orc alchemists seeking to unlock the mysteries of his sorcerous bloodline and convert him into a weapon, the Burning Child has haunted a wide stretch of wasteland in eastern Belkzen for centuries.

  First seen during the battle that bears his name, the Burning Child continues to wander in an endless search for his parents, constantly reliving the terrifying experience of his first fiery death. While in his passive state, he's little more than disembodied sobbing and the scent of burning flesh. But when he happens upon the scene of a battle, the memory of his agonizing death pushes him to manifest, and he wanders into the fray crying out for rescue, all the while unintentionally sowing devastation as the uncontrollable energies coursing through him spill out of his unstable form.

---

# Burning Child
The smell of scorched flesh accompanies this small child, who appears to be made entirely of dust and smoldering ash.
**Source** Belkzen, Hold of the _[[monsters/Orc|Orc]]_ Hordes pg. 58
**XP** 9,600

CN Small undead (fire)
**Init** +7; **Senses** Perception +17
**Aura** _[[spells/Elemental Aura|elemental aura]]_ (fire, DC 17), _[[universal monster rules/Frightful Presence|frightful presence]]_ (60 ft., DC 21)

##### Defense

**AC** 17, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+3 Dex, +1 dodge, +2 natural, +1 size)
**hp** 150 (15d8+75)
**Fort** +9, **Ref** +12, **Will** +11
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4, _[[feats/Final Embrace|final embrace]]_; **Immune** fire, _[[universal monster rules/Undead Traits|undead traits]]_
**Weaknesses** vulnerable to cold

##### Offense
**Speed** 40 ft.
**Melee** slam +10 (1d4–2 plus _[[universal monster rules/Burn|burn]]_)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, 10d6 fire damage, Reflex DC 21 half), _burn_ (2d8, DC 21)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +15)
Constant—_elemental aura_ (fire only; DC 17), _[[spells/Fire Trail|fire trail]]_ (DC 17)
At will—_[[spells/Burning Hands|burning hands]]_ (DC 16), _[[spells/Scorching Ray|scorching ray]]_ (DC 16)
3/day—quickened _[[spells/Fireball|fireball]]_ (DC 17)

##### Statistics
**Str** 6, **Dex** 17, **Con** —, **Int** 10, **Wis** 15, **Cha** 18
**Base Atk** +7; **CMB** 14; **CMD** 17
**Feats** _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_fireball_), _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Escape Artist +18, Intimidate +19, Perception +17, Sense Motive +17
**Languages** Common
**SQ** binary state

##### Ecology

**Environment** temperate plains
**Organization** unique
**Treasure** none

### Special Abilities

**Binary State (Su)** Most of the time the _[[monsters/Burning Child|Burning Child]]_ is in a passive state, during which he’s _[[universal monster rules/Incorporeal|incorporeal]]_ and _[[conditions/Invisible|invisible]]_, though his soft sobs and the _[[universal monster rules/Scent|scent]]_ of _[[items/Weapon Magic Abilities/Burning|burning]]_ flesh allow a creature to pinpoint his location with a successful DC 30 Perception check. If the _Burning Child_ comes across a battle, the chance he enters his active state is equal to 1% per creature fighting (to a maximum of 100%). While active, the _Burning Child_ is corporeal and visible. After 1d4 hours without being attacked or seeing conflict, the _Burning Child_ reenters his passive state.

**_Breath Weapon_ (Su)** The _Burning Child_ can use his _breath weapon_ only when in his active state, and only once each time he becomes active.

**_Final Embrace_ (Ex)** If the _Burning Child_ is destroyed, he reforms in 2d4 days. He can be permanently destroyed only when active, by a humanoid embracing and _[[items/Armor Magic Abilities/Calming|calming]]_ him. This requires succeeding at DC 28 Diplomacy checks for 3 consecutive rounds.

##### Description

Born from the traumatic death of an abducted human child at the hands of _orc_ alchemists seeking to unlock the mysteries of his sorcerous bloodline and convert him into a weapon, the _Burning Child_ has haunted a wide stretch of wasteland in eastern Belkzen for centuries.

First seen during the battle that bears his name, the _Burning Child_ continues to wander in an endless search for his parents, constantly reliving the terrifying experience of his first fiery death. While in his passive state, he’s little more than disembodied sobbing and the _scent_ of _burning_ flesh. But when he happens upon the scene of a battle, the memory of his agonizing death pushes him to manifest, and he wanders into the fray crying out for rescue, all the while unintentionally sowing devastation as the uncontrollable energies coursing through him spill out of his unstable form.
---
cssclass: [monsters]
title1: Ragewight
desc_short: This desiccated corpse wields a greatsword, its eyes blazing with eerie
  red light.
title2: Ragewight
CR: 6
sources:
- name: Andoran, Birthplace of Freedom
  page: 58
  link: http://paizo.com/products/btpy9dz4?Pathfinder-Campaign-Setting-Andoran-Birthplace-of-Freedom
XP: 2400
alignment: CE
size: Medium
type: undead
initiative:
  bonus: 1
senses:
  darkvision: 60
AC:
  AC: 18
  touch: 10
  flat_footed: 16
  components:
    dex: 2
    natural: 8
    rage: -2
HP:
  HP: 82
  long: 11d8+33
saves:
  fort: 6
  ref: 5
  will: 10
  other: +4 morale bonus vs. spells, supernatural abilities, and spell-like abilities
immunities:
- undead traits
speeds:
  base: 40
attacks:
  melee:
  - - text: greatsword +12/+7 (2d6+6/17-20 plus energy drain)
      entries:
      - - damage: 2d6+6
          crit_range: 17-20
        - effect: energy drain
      attack: greatsword
      bonus:
      - 12
      - 7
    - text: bite +7 (1d4+2 plus energy drain)
      entries:
      - - damage: 1d4+2
        - effect: energy drain
      attack: bite
      bonus:
      - 7
  ranged:
  - - text: javelin +10 (1d6+4)
      entries:
      - - damage: 1d6+4
      attack: javelin
      bonus:
      - 10
  special:
  - create spawn
  - energy drain (1 level, DC 17)
  - rage powers (animal fury, intimidating glare, knockback, superstition, unexpected
    strike)
tactics:
  Base Statistics: When not using savage fury, the ragewight's statistics are AC 19,
    touch 11, flat-footed 18 (+1 Dex, +8 natural); hp 49 (11d8); Fort +3, Will +8;
    Melee mwk greatsword +9/+4 (2d6+1/17-20 plus energy drain); Ranged javelin +9
    (1d6+4); Str 12, Cha 11; CMB +9; CMD 21; Skills Climb +15, Intimidate +11
ability_scores:
  STR: 18
  DEX: 14
  CON:
  INT: 11
  WIS: 13
  CHA: 17
BAB: 8
CMB: 12
CMD: 24
feats:
- name: Cleave
- superscripts:
  - UC
  name: Furious Focus
- name: Great Cleave
- name: Improved Critical (greatsword)
- name: Lunge
- name: Power Attack
skills:
  Climb: 18
  Intimidate: 16
  Knowledge (religion): 7
  Perception: 15
  Stealth: 20
  _racial_mods:
    Stealth:
      _: 8
languages:
- Common
gear:
  gear:
  - greatsword
  - javelin
ecology:
  environment: temperate hills (necropolis of Nogortha)
  organization: solitary, war band (1 ragewight plus 2-5 cairn wights), or war clan
    (2-5 ragewights plus 3-10 cairn wights)
  treasure_type: standard
special_abilities:
  Create Spawn (Su): Most humanoids slain by a ragewight rise as cairn wights (though
    with chaotic evil alignments) in 1d4 rounds. However, humanoids with 6 or more
    Hit Dice and the rage class feature instead become ragewights, retaining the rage
    powers they had in life. Such spawn are under the command of their creator until
    its death, at which point they become free-willed undead.
  Savage Fury (Ex): A ragewight can trigger a savage fury as a free action. It can
    use this fury for 24 rounds each day. These rounds don't need to be consecutive.
    The ragewight gains a +6 profane bonus to its Strength and Charisma and a +3 profane
    bonus on Will saves when using this fury. When a ragewight ends its fury, it is
    staggered for 1d4 rounds and can't resume its fury during this time. This ability
    otherwise functions as the greater rage barbarian class feature, treating the
    ragewight's racial Hit Dice as its barbarian level for the purposes of rage and
    any rage powers.
desc_long: Ragewights are the spirits of savage warriors who died in a rage and have
  since had their burial places disturbed or robbed. They are most common near the
  necropolis of Nogortha, a vast graveyard that includes many barrows of barbarians
  slain in 1707 ar by the expansionist forces of Taldor. Grave robbers plundering
  such barrows occasionally unleash a ragewight, which immediately sets out to build
  an undead army of spawn and wage war against those who slew it centuries ago.

---

# Ragewight
This desiccated corpse wields a _[[items/Weapon/Greatsword|greatsword]]_, its eyes blazing with eerie red light.
**Source** Andoran, Birthplace of _[[spells/Freedom|Freedom]]_ pg. 58
**XP** 2,400
CE Medium undead
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +15

##### Defense

**AC** 18, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+2 Dex, +8 natural, –2 _[[spells/Rage|rage]]_)
**hp** 82 (11d8+33)
**Fort** +6, **Ref** +5, **Will** +10; +4 morale bonus vs. spells, supernatural abilities, and _[[universal monster rules/Spell-Like Abilities|spell-like abilities]]_
**Immune** _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 40 ft.
**Melee** _greatsword_ +12/+7 (2d6+6/17–20 plus _[[universal monster rules/Energy Drain|energy drain]]_), bite +7 (1d4+2 plus _energy drain_)
**Ranged** _[[items/Weapon/Javelin|javelin]]_ +10 (1d6+4)
**Special Attacks** create spawn, _energy drain_ (1 level, DC 17), _rage_ powers (animal fury, intimidating glare, knockback, superstition, unexpected strike)

### Tactics

**Base Statistics** When not using savage fury, the _[[monsters/Ragewight|ragewight]]_’s statistics are **AC** 19, touch 11, _flat-footed_ 18 (+1 Dex, +8 natural); **hp** 49 (11d8); **Fort **+3, **Will **+8; **Melee **mwk _greatsword_ +9/+4 (2d6+1/17–20 plus _energy drain_); **Ranged** _javelin_ +9 (1d6+4); **Str **12, **Cha **11; **CMB **+9; **CMD **21; **Skills** _[[universal monster rules/Climb|Climb]]_ +15, Intimidate +11

##### Statistics
**Str** 18, **Dex** 14, **Con** —, **Int** 11, **Wis** 13, **Cha** 17
**Base Atk** +8; **CMB** +12; **CMD** 24
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Furious Focus|Furious Focus]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Critical|Improved Critical]]_ (_greatsword_), _[[feats/Lunge|Lunge]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** _Climb_ +18, Intimidate +16, Knowledge (religion) +7, Perception +15, Stealth +20; **Racial Modifiers** +8 Stealth
**Languages** Common
**Gear** _greatsword_, _javelin_

##### Ecology

**Environment** temperate hills (necropolis of Nogortha)
**Organization** solitary, war band (1 _ragewight_ plus 2–5 cairn wights), or war clan (2–5 ragewights plus 3–10 cairn wights)
**Treasure** standard

### Special Abilities

**Create Spawn (Su)** Most humanoids slain by a _ragewight_ rise as cairn wights (though with chaotic evil alignments) in 1d4 rounds. However, humanoids with 6 or more Hit Dice and the _rage_ class feature instead become ragewights, retaining the _rage_ powers they had in life. Such spawn are under the _[[spells/Command|command]]_ of their creator until its death, at which point they become free-willed undead.
**Savage Fury (Ex)** A _ragewight_ can trigger a savage fury as a free action. It can use this fury for 24 rounds each day. These rounds don’t need to be consecutive. The _ragewight_ gains a +6 profane bonus to its Strength and Charisma and a +3 profane bonus on Will saves when using this fury. When a _ragewight_ ends its fury, it is _[[conditions/Staggered|staggered]]_ for 1d4 rounds and can’t resume its fury during this time. This ability otherwise functions as the greater _rage_ _[[classes/Barbarian|barbarian]]_ class feature, treating the _ragewight_’s racial Hit Dice as its _barbarian_ level for the purposes of _rage_ and any _rage_ powers.

##### Description

Ragewights are the spirits of savage warriors who died in a _rage_ and have since had their burial places disturbed or robbed. They are most common near the necropolis of Nogortha, a vast graveyard that includes many barrows of barbarians slain in 1707 ar by the expansionist forces of Taldor. Grave robbers plundering such barrows occasionally unleash a _ragewight_, which immediately sets out to build an undead army of spawn and wage war against those who slew it centuries ago.
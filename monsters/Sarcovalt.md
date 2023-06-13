---
cssclass: [monsters]
title1: Sarcovalt
desc_short: This horse-sized housefly has a vulture's neck growing out of its body,
  capped with a fleshless vulture skull.
title2: Sarcovalt
CR: 4
sources:
- name: Inner Sea Gods
  page: 313
  link: http://paizo.com/products/btpy94wj?Pathfinder-Campaign-Setting-Inner-Sea-Gods-Hardcover
XP: 1200
alignment: NE
size: Tiny
type: outsider
subtypes:
- evil
- extraplanar
initiative:
  bonus: 3
senses:
  darkvision: 60
  low-light vision: true
  deathwatch: true
AC:
  AC: 19
  touch: 15
  flat_footed: 16
  components:
    dex: 3
    natural: 4
    size: 2
HP:
  HP: 34
  long: 4d10+12
saves:
  fort: 6
  ref: 7
  will: 5
defensive_abilities:
- ferocity
DR:
- amount: 5
  weakness: good or silver
immunities:
- disease
resistances:
  acid: 10
  cold: 10
SR: 15
speeds:
  base: 20
  climb: 20
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +9 (1d8+1 plus bleed, disease, and grab)
      entries:
      - - damage: 1d8+1
        - effect: bleed
        - effect: disease
        - effect: grab
      attack: bite
      bonus:
      - 9
  special:
  - bleed (1d6)
  - blood drain (1d2 Constitution)
  - detach head
  - disease
space: 2.5
reach: 0
spell_like_abilities:
  entries:
  - name: deathwatch
    source: default
    freq: Constant
  - name: purify food and drink
    source: default
    freq: At will
  - name: death knell
    source: default
    freq: 3/day
    DC: 10
  - superscripts:
    - UM
    name: lesser animate dead
    source: default
    freq: 3/day
  - name: vomit swarm
    source: default
    freq: 3/day
    other: see below
  - name: acid arrow
    source: default
    freq: 1/day
  - name: contagion
    source: default
    freq: 1/day
    DC: 11
  - name: stinking cloud
    source: default
    freq: 1/day
    DC: 10
  sources:
  - name: default
    CL: 4
    concentration: 2
ability_scores:
  STR: 12
  DEX: 17
  CON: 16
  INT: 10
  WIS: 13
  CHA: 7
BAB: 4
CMB: 5
CMB_other: +9 grapple
CMD: 18
CMD_other: 26 vs. trip
feats:
- name: Great Fortitude
- name: Weapon Finesse
skills:
  Climb: 9
  Fly: 11
  Intimidate: 5
  Knowledge (nature): 7
  Knowledge (religion): 7
  Perception: 8
  Stealth: 18
  Survival: 8
languages:
- Abyssal
- Infernal
- telepathy 30 ft.
special_qualities:
- disease swarm
ecology:
  environment: any (Abaddon)
  organization: solitary, pair, or swarm (3-5)
  treasure_type: none
special_abilities:
  Detach Head (Su): A sarcovalt can survive without its head. Attacks that sever its
    head (such as those of a vorpal weapon) do not kill it. If attacked by multiple
    creatures, it grapples one opponent, detaches its head (which continues to drain
    blood), and uses its body to continue attacking with spell-like abilities. Its
    head and body share a common pool of hit points but are otherwise treated as different
    creatures while separated. The head is AC 19, touch 15, flat-footed 16 (+3 Dex,
    +4 natural, +2 size) and can fly at the creature's normal speed. The head cannot
    initiate attacks on its own, and if removed from a target, it flies back to the
    body on its next turn. The body cannot see, but it can perceive through the head's
    eye cavities if it has line of effect to the head.
  Disease Swarm (Su): |-
    A sarcovalt's vomit swarm ability summons a cloud of flies instead of spiders, which has a fly speed of 40 feet (good) and infects its target with filth fever (DC 12) instead of poison.

    Disease (Ex) Filth Fever: Bite-injury; save Fort DC 15; onset 1d3 days; frequency 1 day; effect 1d3 Dex and 1d3 Con; cure 2 consecutive saves.
desc_long: |-
  Sarcovalts are disgusting carrion-eating servants of Urgathoa that pick over the filth and the remnants of devoured souls in her planar realm. They have little personal identity and barely remember events more than a few hours old. While they are intelligent enough to converse and recognize their own kind, other servitors of the Pallid Princess, and daemons, they tend to think of other creatures as either threats or food. Sarcovalts sometimes work together to kill larger prey, but are usually content to eat scraps left behind by more powerful outsiders.

  A sarcovalt resembles an enormous fly with a vulture's neck-but instead of a fleshy head, its head is the naked skull of a vulture with glistening black eyes. When its skull is detached, its bald neck ends in a stump of tattered flesh. It savors the opportunity to drink blood, but cannot swallow it, and therefore its skull is normally painted with the life-f luid of its victims. In their eagerness to shred bodies, especially living flesh, these eager scavengers often get small treasure like amulets, rings, and other equipment worn close to the body trapped within their skulls. After letting such items rattle around in their heads for a few days, they unceremoniously vomit them up coated in the vile remains of their last several meals. Sarcovalts use their skulls similarly to how psychopomps wear masks, and the first sarcovalts might have been created in mockery of Pharasma's servants.

  Servants of Urgathoa frequently summon sarcovalts to serve either as scouts and sentinels, or as menaces to sow fear and disease in places they seek to terrorize. In the best cases, a single sarcovalt can spread disease resulting in the deaths of dozens, giving Urgathoa's priests ample bodies to raise as undead or use in more terrible plots when they reveal themselves.

  Sarcovalts measure 2 feet long and weigh 5 pounds.

---

# Sarcovalt
This horse-sized housefly has a _[[monsters/Vulture|vulture]]_’s neck _[[items/Weapon Magic Abilities/Growing|growing]]_ out of its body, capped with a fleshless _vulture_ skull.
**Source** Inner Sea Gods pg. 313
**XP** 1,200

NE Tiny outsider (evil, extraplanar)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/Deathwatch|deathwatch]]_; Perception +8

##### Defense

**AC** 19, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+3 Dex, +4 natural, +2 size)
**hp** 34 (4d10+12)
**Fort** +6, **Ref** +7, **Will** +5
**Defensive Abilities** _[[universal monster rules/Ferocity|ferocity]]_; **DR** 5/good or silver; **Immune** disease; **Resist** acid 10, cold 10; **SR** 15

##### Offense
**Speed** 20 ft., _[[universal monster rules/Climb|climb]]_ 20 ft., fly 60 ft. (good)
**Melee** bite +9 (1d8+1 plus _[[universal monster rules/Bleed|bleed]]_, disease, and _[[universal monster rules/Grab|grab]]_)
**Space** 2-1/2 ft., **Reach** 0 ft.
**Special Attacks** _bleed_ (1d6), _[[universal monster rules/Blood Drain|blood drain]]_ (1d2 Constitution), detach head, disease
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +2)
Constant—_deathwatch_
At will—_[[spells/Purify Food and Drink|purify food and drink]]_
3/day—_[[spells/Death Knell|death knell]]_ (DC 10), lesser _[[spells/Animate Dead|animate dead]]_, _[[spells/Vomit Swarm|vomit swarm]]_ (see below)
1/day—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Contagion|contagion]]_ (DC 11), _[[spells/Stinking Cloud|stinking cloud]]_ (DC 10)

##### Statistics
**Str** 12, **Dex** 17, **Con** 16, **Int** 10, **Wis** 13, **Cha** 7
**Base Atk** +4; **CMB** +5 (+9 grapple); **CMD** 18 (26 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** _Climb_ +9, Fly +11, Intimidate +5, Knowledge (nature) +7, Knowledge (religion) +7, Perception +8, Stealth +18, Survival +8
**Languages** Abyssal, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 30 ft.
**SQ** disease swarm

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary, pair, or swarm (3–5)
**Treasure** none

### Special Abilities

**Detach Head (Su)** A _[[monsters/Sarcovalt|sarcovalt]]_ can survive without its head. Attacks that sever its head (such as those of a _[[items/Weapon Magic Abilities/Vorpal|vorpal]]_ weapon) do not kill it. If attacked by multiple creatures, it grapples one opponent, detaches its head (which continues to drain blood), and uses its body to continue attacking with _spell-like abilities_. Its head and body share a common pool of hit points but are otherwise treated as different creatures while separated. The head is AC 19, touch 15, _flat-footed_ 16 (+3 Dex, +4 natural, +2 size) and can fly at the creature’s normal speed. The head cannot _[[npcs/Initiate|initiate]]_ attacks on its own, and if removed from a target, it flies back to the body on its next turn. The body cannot see, but it can perceive through the head’s eye cavities if it has line of effect to the head.

**Disease Swarm (Su)** A _sarcovalt_’s _vomit swarm_ ability summons a cloud of flies instead of spiders, which has a fly speed of 40 feet (good) and infects its target with _[[diseases/Filth Fever|filth fever]]_ (DC 12) instead of poison.

Disease (Ex) _Filth Fever_: Bite—injury; save Fort DC 15; onset 1d3 days; frequency 1 day; effect 1d3 Dex and 1d3 Con; cure 2 consecutive saves.

##### Description

Sarcovalts are disgusting carrion-eating servants of Urgathoa that pick over the filth and the remnants of devoured souls in her _[[items/Weapon Magic Abilities/Planar|planar]]_ realm. They have little personal identity and barely remember events more than a few hours old. While they are intelligent enough to converse and recognize their own kind, other servitors of the Pallid _[[npcs/Princess|Princess]]_, and daemons, they tend to think of other creatures as either threats or food. Sarcovalts sometimes work together to kill larger prey, but are usually content to eat scraps left behind by more powerful outsiders.

A _sarcovalt_ resembles an enormous fly with a _vulture_’s neck—but instead of a fleshy head, its head is the naked skull of a _vulture_ with glistening black eyes. When its skull is detached, its bald neck ends in a stump of tattered flesh. It savors the opportunity to drink blood, but cannot swallow it, and therefore its skull is normally painted with the life-f luid of its victims. In their eagerness to shred bodies, especially living flesh, these eager scavengers often get small treasure like amulets, rings, and other equipment worn close to the body trapped within their skulls. After letting such items rattle around in their heads for a few days, they unceremoniously vomit them up coated in the vile remains of their last several meals. Sarcovalts use their skulls similarly to how psychopomps wear masks, and the first sarcovalts might have been created in mockery of Pharasma’s servants.

Servants of Urgathoa frequently _[[universal monster rules/Summon|summon]]_ sarcovalts to serve either as scouts and sentinels, or as menaces to sow _[[universal monster rules/Fear|fear]]_ and disease in places they seek to terrorize. In the best cases, a single _sarcovalt_ can spread disease resulting in the deaths of dozens, giving Urgathoa’s priests ample bodies to raise as undead or use in more terrible plots when they reveal themselves.

Sarcovalts measure 2 feet long and weigh 5 pounds.
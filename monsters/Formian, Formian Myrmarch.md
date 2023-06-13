---
cssclass: [monsters]
title1: Formian, Formian Myrmarch
desc_short: This horse-sized insect has a brilliant red carapace, and its monstrous
  face ref lects great intelligence and confidence.
title2: Formian Myrmarch
CR: 10
sources:
- name: Bestiary 4
  page: 109
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 9600
alignment: LN
size: Large
type: monstrous humanoid
initiative:
  bonus: 8
  other:
    with hive mind: 12
senses:
  blindsense: 30
  darkvision: 60
  hive mind: true
AC:
  AC: 27
  touch: 16
  flat_footed: 22
  components:
    deflection: 2
    dex: 4
    dodge: 1
    natural: 11
    size: -1
HP:
  HP: 126
  long: 12d10+60
saves:
  fort: 11
  ref: 14
  will: 13
resistances:
  sonic: 10
speeds:
  base: 50
attacks:
  melee:
  - - text: sting +16 (1d8+5 plus poison)
      entries:
      - - damage: 1d8+5
        - effect: poison
      attack: sting
      bonus:
      - 16
    - text: 2 claws +16 (1d4+5/19-20)
      entries:
      - - damage: 1d4+5
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 16
    - text: bite +16 (1d6+5)
      entries:
      - - damage: 1d6+5
      attack: bite
      bonus:
      - 16
  ranged:
  - - text: javelin +15/+10/+5 (1d6+5 plus poison)
      entries:
      - - damage: 1d6+5
        - effect: poison
      attack: javelin
      bonus:
      - 15
      - 10
      - 5
  special:
  - poison
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: charm monster
    source: default
    freq: At will
    DC: 17
  - name: clairaudience/clairvoyance
    source: default
    freq: At will
  - name: detect thoughts
    source: default
    freq: At will
    DC: 15
  - name: hold monster
    source: default
    freq: 3/day
    DC: 18
  - name: feeblemind
    source: default
    freq: 1/day
    DC: 18
  sources:
  - name: default
    CL: 12
    concentration: 15
ability_scores:
  STR: 20
  DEX: 19
  CON: 20
  INT: 17
  WIS: 16
  CHA: 17
BAB: 12
CMB: 18
CMD: 35
CMD_other: 39 vs. trip
feats:
- name: Dodge
- name: Improved Initiative
- name: Mobility
- name: Quick Draw
- name: Spring Attack
- name: Vital Strike
skills:
  Climb: 20
  Diplomacy: 15
  Knowledge (arcana): 15
  Perception: 18
    with hive mind: 22
  Sense Motive: 15
  Spellcraft: 15
  Stealth: 15
languages:
- Common
- telepathy 150 ft.
special_qualities:
- formian traits
- inspire hive
- undersized weapons
ecology:
  environment: warm or temperate land or underground
  organization: Solitary, team (2-4), platoon (1 plus 7-18 warriors and 6-12 workers),
    or royal guard (4 plus 12-20 warriors)
  treasure_type: standard
  treasure:
  - 9 javelins
  - other treasure
special_abilities:
  Inspire Hive (Su): Once per day, a myrmarch can affect all warriors and workers
    in its telepathic range as if they were under the effect of a greater heroism
    spell (CL 12th).
  Poison (Ex): Javelin or sting-injury; save Fort DC 21; frequency 1/round for 6 rounds;
    effect 1d4 Dex and sickened; cure 2 saves. The save DC is Constitution-based.
desc_long: |-
  Myrmarchs are an elite caste of the formian race. They serve as direct agents for the queen, acting as advisors and generals, or administrating tasks where complexity or propriety renders taskmasters unsuitable. It is myrmarchs who answer the call when a particularly skilled diplomat or emissary is required to carry the queen's words outside of the territory of the hive to the dangerously disorganized races.

  While myrmarchs make up the aristocracy of formian society, this does not make them pampered intellectuals and bureaucrats. On the contrary, they are even more deadly than the warriors they often command, and do not hesitate to use their considerable might to aid and protect their kin. Myrmarchs facing combat apply their natural poison to their javelins, making them even more lethal.

  Like other formians, myrmarchs record their life's history upon their carapaces. Between their greater opportunities and longer lifespans (roughly as long as those of humans), myrmarchs can cover nearly every inch of their shells with great deeds accomplished, foes overcome, and service to the hive. Some myrmarchs actually run out of space for new records: some die shortly thereafter, knowing that they have served their queen to the utmost, while others add new artificial plates to their carapaces to continue their epics.

  The most accomplished, trusted, and battle-tested of their race, myrmarchs form the queen's elite bodyguard. In a small hive, these bodyguards likely have the same statistics presented above. In the oldest and largest hives, however, most possess class levels.

  A myrmarch has an enlarged thorax and abdomen, which give it the same general size and weight as a large warhorse, though its upper body is not much larger than that of a formian warrior's. Myrmarchs stand about 8 feet high and weigh about 1,200 pounds.

---

# Formian, Formian Myrmarch
This horse-sized insect has a brilliant red carapace, and its monstrous face ref lects great intelligence and confidence.
**Source** Bestiary 4 pg. 109
**XP** 9,600

LN Large monstrous humanoid
**Init** +8 (+12 with hive mind); **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 30 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., hive mind; Perception +18 (+22 with hive mind)

##### Defense

**AC** 27, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+2 deflection, +4 Dex, +1 _[[feats/Dodge|dodge]]_, +11 natural, –1 size)
**hp** 126 (12d10+60)
**Fort** +11, **Ref** +14, **Will** +13
**Resist** sonic 10

##### Offense
**Speed** 50 ft.
**Melee** sting +16 (1d8+5 plus poison), 2 claws +16 (1d4+5/19–20), bite +16 (1d6+5)
**Ranged** _[[items/Weapon/Javelin|javelin]]_ +15/+10/+5 (1d6+5 plus poison)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** poison
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +15)
At will—_[[spells/Charm Monster|charm monster]]_ (DC 17), clairaudience/clairvoyance, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 15)
3/day—_[[spells/Hold Monster|hold monster]]_ (DC 18)
1/day—_[[spells/Feeblemind|feeblemind]]_ (DC 18)

##### Statistics
**Str** 20, **Dex** 19, **Con** 20, **Int** 17, **Wis** 16, **Cha** 17
**Base Atk** +12; **CMB** +18; **CMD** 35 (39 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quick Draw|Quick Draw]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +20, Diplomacy +15, Knowledge (arcana) +15, Perception +18 (+22 with hive mind), Sense Motive +15, Spellcraft +15, Stealth +15
**Languages** Common, _[[universal monster rules/Telepathy|telepathy]]_ 150 ft.
**SQ** formian traits, inspire hive, _[[universal monster rules/Undersized Weapons|undersized weapons]]_

##### Ecology

**Environment** warm or temperate land or underground
**Organization** Solitary, team (2–4), platoon (1 plus 7–18 warriors and 6–12 workers), or royal _[[npcs/Guard|guard]]_ (4 plus 12–20 warriors)
**Treasure** standard (9 javelins, other treasure)

### Special Abilities

**Inspire Hive (Su)** Once per day, a myrmarch can affect all warriors and workers in its telepathic range as if they were under the effect of a greater _[[spells/Heroism|heroism]]_ spell (CL 12th).

**Poison (Ex)** _Javelin_ or sting—injury; save Fort DC 21; frequency 1/round for 6 rounds; effect 1d4 Dex and _[[conditions/Sickened|sickened]]_; cure 2 saves. The save DC is Constitution-based.

##### Description

Myrmarchs are an elite caste of the formian race. They serve as direct agents for the queen, acting as advisors and generals, or administrating tasks where complexity or propriety renders taskmasters unsuitable. It is myrmarchs who answer the call when a particularly skilled _[[npcs/Diplomat|diplomat]]_ or emissary is required to carry the queen’s words outside of the territory of the hive to the dangerously disorganized races.

While myrmarchs make up the aristocracy of formian society, this does not make them pampered intellectuals and bureaucrats. On the contrary, they are even more _[[items/Weapon Magic Abilities/Deadly|deadly]]_ than the warriors they often _[[spells/Command|command]]_, and do not hesitate to use their considerable might to aid and protect their kin. Myrmarchs facing combat apply their natural poison to their javelins, making them even more lethal.

Like other formians, myrmarchs record their life’s history upon their carapaces. Between their greater opportunities and longer lifespans (roughly as long as those of humans), myrmarchs can cover nearly every inch of their shells with great deeds accomplished, foes overcome, and service to the hive. Some myrmarchs actually run out of space for new records: some die shortly thereafter, knowing that they have served their queen to the utmost, while others add new artificial plates to their carapaces to continue their epics.

The most accomplished, trusted, and battle-tested of their race, myrmarchs form the queen’s elite _[[feats/Bodyguard|bodyguard]]_. In a small hive, these bodyguards likely have the same statistics presented above. In the oldest and largest hives, however, most possess class levels.

A myrmarch has an enlarged thorax and abdomen, which give it the same general size and weight as a large warhorse, though its upper body is not much larger than that of a formian warrior’s. Myrmarchs stand about 8 feet high and weigh about 1,200 pounds.
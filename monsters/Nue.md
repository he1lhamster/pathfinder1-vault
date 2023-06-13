---
cssclass: [monsters]
title1: Nue
desc_short: Materializing out of a noxious black cloud, this beast has the head of
  a fanged monkey and the body of a tiger with a viper as a tail.
title2: Nue
CR: 10
sources:
- name: Bestiary 3
  page: 204
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 9600
alignment: NE
size: Large
type: magical beast
initiative:
  bonus: 9
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 24
  touch: 15
  flat_footed: 18
  components:
    dex: 5
    dodge: 1
    natural: 9
    size: -1
HP:
  HP: 126
  long: 12d10+60
saves:
  fort: 13
  ref: 13
  will: 7
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +17 (2d6+6 plus energy drain)
      entries:
      - - damage: 2d6+6
        - effect: energy drain
      attack: bite
      bonus:
      - 17
    - text: bite +17 (1d4+6 plus poison)
      entries:
      - - damage: 1d4+6
        - effect: poison
      attack: bite
      bonus:
      - 17
    - text: 2 claws +17 (1d6+6)
      entries:
      - - damage: 1d6+6
      count: 2
      attack: claws
      bonus:
      - 17
  special:
  - energy drain (2 levels, DC 16)
  - pounce
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: contagion
    source: default
    freq: 3/day
    DC: 14
  - name: hold person
    source: default
    freq: 3/day
    DC: 13
  - name: nightmare
    source: default
    freq: 1/day
    DC: 15
  - name: shout
    source: default
    freq: 1/day
    DC: 14
  - name: waves of fatigue
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 12
    concentration: 12
ability_scores:
  STR: 22
  DEX: 21
  CON: 20
  INT: 7
  WIS: 17
  CHA: 10
BAB: 12
CMB: 19
CMD: 35
CMD_other: 39 vs. trip
feats:
- name: Combat Casting
- name: Combat Reflexes
- name: Dodge
- name: Improved Initiative
- name: Mobility
- name: Skill Focus (Stealth)
skills:
  Climb: 13
  Perception: 10
  Stealth: 11
languages:
- Common
special_qualities:
- cloud form
ecology:
  environment: warm forests or mountains
  organization: solitary, pair, or ambush (3-6)
  treasure_type: standard
special_abilities:
  Cloud Form (Su): A nue can change into the form of a 10-foot black cloud or back
    to its normal form as a standard action. A nue in cloud form is otherwise treated
    as if under the effects of gaseous form, except that it obscures vision like fog
    cloud.
  Poison (Ex): Bite-injury; save Fort DC 21; frequency 1/round for 6 rounds; effect
    1d4 Strength damage; cure 2 consecutive saves. The save DC is Constitution-based.
desc_long: |-
  This strange creature has the body of a tiger, the head of a fanged monkey, and a poisonous viper for a tail. Though some call it a chimera and treat it as an exotic specimen of that creature, it is a completely different breed of beast.

  Intelligent enough to enjoy cruelty as well as inflicting terror upon its prey, a nue delights in toying with its victim before dealing the killing blow. Often, a nue will select a target and plague it with nightmares before it even attempts an act of violence, wearing down the victim with dreadful dreams and phantasmagoric terrors. Once its prey is thoroughly exhausted, the nue will finally steal into the victim's sleeping chambers and engage in combat, paralyzing its target with its magic and infecting its prey with both disease and poison, letting the victim writhe in pain before succumbing to death.

  A nue's ghastly appearance in physical form is only made eerier by its ability to turn into an inky cloud of darkness. In this guise, a nue can hide amongst fog clouds or shadows before emerging as the destructive horror it is. By the time a nue crawls forth from the inscrutable black cloud, its prey is often too fatigued from its strange night terrors to defend itself. The dreams a nue impregnates creatures' minds with varies from victim to victim, but all share the trait of an ever-present, foreboding cloud that exudes a fierce and palpable sense of malice.

  Some legends suggest that nues are the spirits of children warped into twisted forms to spread paranoia, exhaustion, and fear among former friends and family. According to these stories, such a cursed child wreaks terror upon its friends and relatives until they are all either dead or driven mad by fear. Then, the creature moves on, seeking more challenging kills to sate its vicious hunger. The greatest joy a nue can feel is snuffing the life of a once-strong and proud target that has been brought low by its debilitating attacks.

  A nue is 9 feet long and weighs 600 pounds.

---

# Nue
Materializing out of a noxious black cloud, this beast has the head of a fanged monkey and the body of a _[[monsters/Tiger|tiger]]_ with a viper as a tail.
**Source** Bestiary 3 pg. 204
**XP** 9,600

NE Large magical beast
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +10

##### Defense

**AC** 24, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+5 Dex, +1 dodge, +9 natural, –1 size)
**hp** 126 (12d10+60)
**Fort** +13, **Ref** +13, **Will** +7

##### Offense
**Speed** 30 ft.
**Melee** bite +17 (2d6+6 plus _[[universal monster rules/Energy Drain|energy drain]]_), bite +17 (1d4+6 plus poison), 2 claws +17 (1d6+6)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _energy drain_ (2 levels, DC 16), _[[universal monster rules/Pounce|pounce]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +12)
3/day—_[[spells/Contagion|contagion]]_ (DC 14), _[[spells/Hold Person|hold person]]_ (DC 13)
1/day—_[[spells/Nightmare|nightmare]]_ (DC 15), _[[spells/Shout|shout]]_ (DC 14), _[[spells/Waves of Fatigue|waves of fatigue]]_

##### Statistics
**Str** 22, **Dex** 21, **Con** 20, **Int** 7, **Wis** 17, **Cha** 10
**Base Atk** +12; **CMB** +19; **CMD** 35 (39 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth)
**Skills** _[[universal monster rules/Climb|Climb]]_ +13, Perception +10, Stealth +11
**Languages** Common
**SQ** cloud form

##### Ecology

**Environment** warm forests or mountains
**Organization** solitary, pair, or ambush (3–6)
**Treasure** standard

### Special Abilities

**Cloud Form (Su)** A _[[monsters/Nue|nue]]_ can change into the form of a 10-foot black cloud or back to its normal form as a standard action. A _nue_ in cloud form is otherwise treated as if under the effects of _[[spells/Gaseous Form|gaseous form]]_, except that it obscures _[[spells/Vision|vision]]_ like _[[spells/Fog Cloud|fog cloud]]_.

**Poison (Ex)** Bite—injury; save Fort DC 21; frequency 1/round for 6 rounds; effect 1d4 Strength damage; cure 2 consecutive saves. The save DC is Constitution-based.

##### Description

This strange creature has the body of a _tiger_, the head of a fanged monkey, and a poisonous viper for a tail. Though some call it a _[[monsters/Chimera|chimera]]_ and treat it as an exotic specimen of that creature, it is a completely different breed of beast.

Intelligent enough to enjoy _[[feats/Cruelty|cruelty]]_ as well as inflicting terror upon its prey, a _nue_ delights in toying with its victim before dealing the killing blow. Often, a _nue_ will select a target and plague it with nightmares before it even attempts an act of violence, wearing down the victim with dreadful dreams and phantasmagoric terrors. Once its prey is thoroughly _[[conditions/Exhausted|exhausted]]_, the _nue_ will finally steal into the victim’s sleeping chambers and engage in combat, paralyzing its target with its magic and infecting its prey with both disease and poison, letting the victim writhe in pain before succumbing to death.

A _nue_’s ghastly appearance in physical form is only made eerier by its ability to turn into an inky cloud of _[[spells/Darkness|darkness]]_. In this guise, a _nue_ can hide amongst fog clouds or shadows before emerging as the destructive horror it is. By the time a _nue_ crawls forth from the inscrutable black cloud, its prey is often too _[[conditions/Fatigued|fatigued]]_ from its strange _[[spells/Night Terrors|night terrors]]_ to defend itself. The dreams a _nue_ impregnates creatures’ minds with varies from victim to victim, but all share the trait of an ever-present, foreboding cloud that exudes a fierce and palpable sense of malice.

Some legends suggest that nues are the spirits of children warped into twisted forms to spread _[[spells/Paranoia|paranoia]]_, exhaustion, and _[[universal monster rules/Fear|fear]]_ among former friends and family. According to these stories, such a cursed child wreaks terror upon its friends and relatives until they are all either dead or driven mad by _fear_. Then, the creature moves on, seeking more challenging kills to sate its _[[items/Weapon Magic Abilities/Vicious|vicious]]_ hunger. The greatest joy a _nue_ can feel is snuffing the life of a once-strong and proud target that has been brought low by its _[[items/Weapon Magic Abilities/Debilitating|debilitating]]_ attacks.

A _nue_ is 9 feet long and weighs 600 pounds.
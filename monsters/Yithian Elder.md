---
cssclass: [monsters]
title1: Yithian Elder
desc_short: 'This creature's conical body bears four rubbery appendages: two end in
  strong pincers, another ends in a cluster of four trumpetlike organs, and yet another
  is attached to a round head with three eyes that glow with ancient, forbidden power.'
title2: Yithian Elder
CR: 13
sources:
- name: Occult Bestiary
  page: 62
  link: http://paizo.com/products/btpy9g21?Pathfinder-Campaign-Setting-Occult-Bestiary
XP: 25600
alignment: LN
size: Large
type: aberration
initiative:
  bonus: 3
senses:
  all-around vision: true
  blindsense: 60
  darkvision: 60
AC:
  AC: 27
  touch: 12
  flat_footed: 24
  components:
    dex: 3
    natural: 15
    size: -1
HP:
  HP: 180
  long: 19d8+95
  fast_healing: 5
saves:
  fort: 13
  ref: 9
  will: 19
DR:
- amount: 10
  weakness: magic
resistances:
  acid: 10
  cold: 10
  fire: 10
speeds:
  base: 20
  climb: 10
attacks:
  melee:
  - - text: 2 pincers +21 (2d8+12/×3)
      entries:
      - - damage: 2d8+12
          crit_multiplier: 3
      count: 2
      attack: pincers
      bonus:
      - 21
  ranged:
  - - text: lightning gun +16 touch (10d12 electricity)
      entries:
      - - damage: 10d12
          type: electricity
      attack: lightning gun
      bonus:
      - 16
      touch: true
  special:
  - amnesia
  - deadly pincers
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: astral projection
    source: default
    freq: At will
    other: self only
  - name: detect thoughts
    source: default
    freq: At will
    DC: 18
  - name: hold monster
    source: default
    freq: At will
    DC: 21
  - name: modify memory
    source: default
    freq: At will
    DC: 21
  sources:
  - name: default
    CL: 19
    concentration: 27
psychic_magic:
  entries:
  - superscripts:
    - OA
    name: hypercognition
    PE: 2
  - superscripts:
    - OA
    name: intellect fortress III
    PE: 6
  - superscripts:
    - OA
    name: major mind swap
    PE: 9
    DC: 29
  - superscripts:
    - OA
    name: mental barrier V
    PE: 6
  - superscripts:
    - OA
    name: mind probe
    PE: 4
    DC: 24
  - superscripts:
    - OA
    name: remote viewing
    PE: 5
  - superscripts:
    - OA
    name: thought shield V
    PE: 6
  sources:
  - name: default
    CL: 19
    concentration: 27
  PE: 22
ability_scores:
  STR: 26
  DEX: 17
  CON: 21
  INT: 28
  WIS: 23
  CHA: 22
BAB: 14
CMB: 23
CMD: 36
feats:
- name: Alertness
- name: Combat Expertise
- name: Great Fortitude
- name: Improved Great Fortitude
- name: Improved Iron Will
- name: Iron Will
- name: Spell Focus (abjuration)
- name: Spell Focus (divination)
- name: Spell Focus (enchantment)
- name: Vital Strike
skills:
  Climb: 16
  Craft (sculpture): 26
  Diplomacy: 25
  Heal: 25
  Knowledge (arcana): 31
  Knowledge (dungeoneering): 31
  Knowledge (engineering): 31
  Knowledge (geography): 31
  Knowledge (history): 31
  Knowledge (planes): 31
  Linguistics: 28
  Perception: 32
  Sense Motive: 29
  Use Magic Device: 25
languages:
- Aklo
- Common
- Yithian
- 26 other languages
- telepathy 100 ft.
special_qualities:
- mental projection
ecology:
  environment: any
  organization: solitary or pair
  treasure_type: standard
  treasure:
  - lightning gun [see page 63]
  - other treasure
special_abilities:
  Amnesia (Su): Once per day as a standard action, a yithian elder can attempt to
    inflict amnesia on a target it can communicate with telepathically. The target
    can resist this attack with a successful DC 25 Will saving throw. On a failed
    save, the target takes a permanent -4 penalty on Will saving throws and skill
    checks, and loses all memories save for those the yithian chooses to leave intact.
    This effect can be cured by heal, greater restoration, or psychic surgeryOA. This
    is a mind-affecting insanity effect. The save DC is Charisma-based.
  Deadly Pincers (Ex): A yithian elder always applies 1-1/2 times its Strength modifier
    to damage dealt by its pincer attacks and deals triple damage on a critical hit.
  Mental Projection (Su): |-
    A yithian elder can cast major mind swapOA on creatures in other times and places, even if the target creature is of a different race. Before using this ability, it must first spend a week building a special device-a collection of reflective surfaces held in position with a lattice of rods- and succeed at a DC 35 Craft (sculpture) check. A yithian elder can usually gather the necessary materials with ease. This device serves as a focus in place of the spell's normal material component.

    The yithian elder can focus on its device once per day, selecting a specific location and era before entering a trance and sending its mind through time. It can use detect thoughts to locate the minds of sentient creatures in this targeted time and place. Contacted creatures have a vague sense of an otherworldly presence in their minds, even if they succeed at the Will save, but don't know its source. If the yithian elder successfully detects a sentient mind and finds it acceptable, it can target that creature with major mind swapOA. The target falls unconscious for 2d12 hours as both minds transition through space and time to their new bodies. A successful DC 29 Will saving throw prevents this unconsciousness and exchange.

    Unless the yithian elder has swapped minds with another yithian, both creatures are initially unfamiliar with the bodies they inhabit. For the first 24 hours after regaining consciousness, both take a -4 penalty on attack rolls, damage rolls and all Strength- and Dexterity-based skill checks. The mental faculties of both creatures remain intact, but the yithian elder takes a -4 penalty on Charisma-based skill checks when interacting with members of its new body's race.

    To reverse the process, the yithian elder must use its new body to create another mirror-and-rod device and return its mind to its own body. The other mind receives a new saving throw to resist the process. If either the yithian elder's body or that of its host is slain while the minds are swapped, the surviving mind remains trapped in its current body.
  Scholar (Ex): Yithian elders treat all knowledge skills as class skills.
desc_long: |-
  Yithians are beings from a galaxy far removed from Golarion across space and time. Their unusual biology is disturbing to behold. Their bodies are conical, roughly 10 feet tall and 10 feet wide at the base, and covered with a layer of rubbery flesh. Four thick appendages extend from a yithian elder's body, stretching to a length of almost 10 feet or retracting until they nearly disappear. Two of these limbs end in pincers that serve both as hands and as a means of communication via a complex system of gestures, clicks, and scraping sounds. Another appendage ends in a grouping of four tapered organs, through which yithians consume liquefied vegetable and synthetic nourishment-yithians eat no meat in this form. The fourth appendage, atop the cone, bears the creature's round head, which holds three large eyes spaced evenly around it. In addition to the eight tentacles that dangle from the bottom of all yithians' heads, a yithian elder has a “crown” of five antennae sprouting from the top of its head.

  In the distant past of their civilizations, yithians made such great advances in science and metaphysics that they learned to fling their minds across the vastness of the multiverse and inhabit the bodies of other beings, even those of creatures living millions of years in the past or future. While the yithian uses the displaced creature's body to experience alien worlds and times, the displaced mind is held in the yithian's body. Cooperative subjects who share what they know of their own worlds can move with a certain amount of freedom about the yithians' cyclopean cities. Even those who are forced to exchange their minds with yithians can, if well-behaved, learn a great deal about their hosts' culture, which is strictly organized, largely free of crime, and almost entirely focused on the exploration of science and art, though yithians possess a bizarre aesthetic in keeping with their alien natures and nearly unlimited knowledge.

  In displaced creatures' bodies, yithian elders gather information about other cultures and look for clues about what will become of their own race. Before the end of a yithian elder's time in a distant body, another elder uses its amnesia ability on the captive mind, relegating knowledge of the time spent among the great race to half-memories and strikingly realistic but vaguely terrifying dreams.

  Yithian metropolises rest atop sealed tunnels-closely guarded with powerful weapons-that contain dreaded enemies of which the yithians never speak. Yithians already know their enemies will one day burst forth from their sealed tunnels and destroy them. Before that happens, the yithians plan to send their minds forward and inhabit a new race of beings-avoiding their own destruction, even as they doom the race whose minds they displace.

  A yithian elder weighs about 4,000 pounds and can live up to 5,000 years.

---

# Yithian Elder
This creature’s conical body bears four rubbery appendages: two end in strong pincers, another ends in a cluster of four trumpetlike organs, and yet another is attached to a round head with three eyes that glow with ancient, forbidden power.
**Source** Occult Bestiary pg. 62
**XP** 25,600

LN Large aberration
**Init** +3; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[universal monster rules/Blindsense|blindsense]]_ 60 ft., _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +32

##### Defense

**AC** 27, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+3 Dex, +15 natural, –1 size)
**hp** 180 (19d8+95); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +13, **Ref** +9, **Will** +19
**DR** 10/magic; **Resist** acid 10, cold 10, fire 10

##### Offense
**Speed** 20 ft., _[[universal monster rules/Climb|climb]]_ 10 ft.
**Melee** 2 pincers +21 (2d8+12/×3)
**Ranged** _[[items/Wondrous Item/Lightning Gun|lightning gun]]_ +16 touch (10d12 electricity)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[spells/Amnesia|amnesia]]_, _[[items/Weapon Magic Abilities/Deadly|deadly]]_ pincers
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 19th; concentration +27)
At will—_[[spells/Astral Projection|astral projection]]_ (self only), _[[spells/Detect Thoughts|detect thoughts]]_ (DC 18), _[[spells/Hold Monster|hold monster]]_ (DC 21), _[[spells/Modify Memory|modify memory]]_ (DC 21)
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_ **(CL 19th; concentration +27)
22 PE—_[[spells/Hypercognition|hypercognition]]_ (2 PE), _[[spells/Intellect Fortress III|intellect fortress III]]_ (6 PE), major _[[spells/Mind Swap|mind swap]]_ (9 PE, DC 29), _[[spells/Mental Barrier V|mental barrier V]]_ (6 PE), _[[spells/Mind Probe|mind probe]]_ (4 PE, DC 24), _[[spells/Remote Viewing|remote viewing]]_ (5 PE), _[[spells/Thought _[[spells/Shield|Shield]]_ V|thought _shield_ V]]_ (6 PE)

##### Statistics
**Str** 26, **Dex** 17, **Con** 21, **Int** 28, **Wis** 23, **Cha** 22
**Base Atk** +14; **CMB** +23; **CMD** 36
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Great Fortitude|Improved Great Fortitude]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Spell Focus|Spell Focus]]_ (abjuration, _[[spells/Divination|divination]]_, enchantment), _[[feats/Vital Strike|Vital Strike]]_
**Skills** _Climb_ +16, Craft (sculpture) +26, Diplomacy +25, _[[spells/Heal|Heal]]_ +25, Knowledge (arcana, dungeoneering, engineering, geography, history, planes) +31, Linguistics +28, Perception +32, Sense Motive +29, Use Magic Device +25
**Languages** Aklo, Common, _[[monsters/Yithian|Yithian]]_, 26 other languages, _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** mental projection

##### Ecology

**Environment** any
**Organization** solitary or pair
**Treasure** standard (_lightning gun_ [see page 63], other treasure)

### Special Abilities

**_Amnesia_ (Su)** Once per day as a standard action, a _[[monsters/Yithian Elder|yithian elder]]_ can attempt to inflict _amnesia_ on a target it can communicate with telepathically. The target can resist this attack with a successful DC 25 Will saving throw. On a failed save, the target takes a permanent –4 penalty on Will saving throws and skill checks, and loses all memories save for those the _yithian_ chooses to leave intact. This effect can be cured by _heal_, greater _[[spells/Restoration|restoration]]_, or _[[spells/Psychic Surgery|psychic surgery]]_. This is a mind-affecting _[[spells/Insanity|insanity]]_ effect. The save DC is Charisma-based.

**_Deadly_ Pincers (Ex)** A _yithian elder_ always applies 1-1/2 times its Strength modifier to damage dealt by its pincer attacks and deals triple damage on a critical hit.

**Mental Projection (Su)** A _yithian elder_ can cast major _mind swap_ on creatures in other times and places, even if the target creature is of a different race. Before using this ability, it must first spend a week building a special device—a collection of reflective surfaces held in position with a lattice of rods— and succeed at a DC 35 Craft (sculpture) check. A _yithian elder_ can usually gather the necessary materials with ease. This device serves as a focus in place of the spell’s normal material component.

The _yithian elder_ can focus on its device once per day, selecting a specific location and era before entering a trance and _[[spells/Sending|sending]]_ its mind through time. It can use _detect thoughts_ to locate the minds of sentient creatures in this targeted time and place. Contacted creatures have a vague sense of an otherworldly presence in their minds, even if they succeed at the Will save, but don’t know its source. If the _yithian elder_ successfully detects a sentient mind and finds it acceptable, it can target that creature with major _mind swap_. The target falls _[[conditions/Unconscious|unconscious]]_ for 2d12 hours as both minds transition through space and time to their new bodies. A successful DC 29 Will saving throw prevents this unconsciousness and exchange.

Unless the _yithian elder_ has swapped minds with another _yithian_, both creatures are initially unfamiliar with the bodies they inhabit. For the first 24 hours after regaining consciousness, both take a –4 penalty on attack rolls, damage rolls and all Strength- and Dexterity-based skill checks. The mental faculties of both creatures remain intact, but the _yithian elder_ takes a –4 penalty on Charisma-based skill checks when interacting with members of its new body’s race.

To reverse the process, the _yithian elder_ must use its new body to create another mirror-and-rod device and return its mind to its own body. The other mind receives a new saving throw to resist the process. If either the _yithian elder_’s body or that of its host is slain while the minds are swapped, the surviving mind remains trapped in its current body.
**_[[feats/Scholar|Scholar]]_ (Ex)** _Yithian_ elders treat all knowledge skills as class skills.

##### Description

Yithians are beings from a galaxy far removed from Golarion across space and time. Their unusual biology is disturbing to behold. Their bodies are conical, roughly 10 feet tall and 10 feet wide at the base, and covered with a layer of rubbery flesh. Four thick appendages extend from a _yithian elder_’s body, stretching to a length of almost 10 feet or retracting until they nearly disappear. Two of these limbs end in pincers that serve both as hands and as a means of communication via a complex system of gestures, clicks, and scraping sounds. Another appendage ends in a grouping of four tapered organs, through which yithians consume liquefied vegetable and synthetic nourishment—yithians eat no meat in this form. The fourth appendage, atop the cone, bears the creature’s round head, which holds three large eyes spaced evenly around it. In addition to the eight tentacles that dangle from the bottom of all yithians’ heads, a _yithian elder_ has a “crown” of five antennae sprouting from the top of its head.

In the distant past of their civilizations, yithians made such great advances in science and metaphysics that they learned to _[[feats/Fling|fling]]_ their minds across the vastness of the multiverse and inhabit the bodies of other beings, even those of creatures living millions of years in the past or future. While the _yithian_ uses the displaced creature’s body to experience alien worlds and times, the displaced mind is held in the _yithian_’s body. Cooperative subjects who share what _[[spells/They Know|they know]]_ of their own worlds can move with a certain amount of _[[spells/Freedom|freedom]]_ about the yithians’ cyclopean cities. Even those who are forced to exchange their minds with yithians can, if well-behaved, learn a great deal about their hosts’ culture, which is strictly organized, largely free of crime, and almost entirely focused on the exploration of science and art, though yithians possess a bizarre aesthetic in keeping with their alien natures and nearly unlimited knowledge.

In displaced creatures’ bodies, _yithian_ elders gather information about other cultures and look for clues about what will become of their own race. Before the end of a _yithian elder_’s time in a distant body, another elder uses its _amnesia_ ability on the captive mind, relegating knowledge of the time spent among the great race to half-memories and strikingly realistic but vaguely terrifying dreams.

_Yithian_ metropolises rest atop sealed tunnels—closely guarded with powerful weapons—that contain dreaded enemies of which the yithians never speak. Yithians already know their enemies will one day burst forth from their sealed tunnels and destroy them. Before that happens, the yithians plan to send their minds forward and inhabit a new race of beings—avoiding their own _[[spells/Destruction|destruction]]_, even as they _[[spells/Doom|doom]]_ the race whose minds they displace.

A _yithian elder_ weighs about 4,000 pounds and can live up to 5,000 years.
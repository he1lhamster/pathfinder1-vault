---
cssclass: [monsters]
title1: Sphinx, Cynosphinx
desc_short: A jackal's head draped in a tattered headdress extends from a winged,
  leonine body.
title2: Cynosphinx
CR: 6
sources:
- name: 'Pathfinder #82: Secrets of the Sphinx'
  page: 84
  link: http://paizo.com/products/btpy978j?Pathfinder-Adventure-Path-82-Secrets-of-the-Sphinx
XP: 2400
alignment: NE
size: Large
type: magical beast
initiative:
  bonus: 1
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 20
  touch: 10
  flat_footed: 19
  components:
    dex: 1
    natural: 10
    size: -1
HP:
  HP: 76
  long: 9d10+27
saves:
  fort: 9
  ref: 7
  will: 5
immunities:
- disease
speeds:
  base: 30
  fly: 60
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +13 (1d8+7 plus disease and trip)
      entries:
      - - damage: 1d8+7
        - effect: disease
        - effect: trip
      attack: bite
      bonus:
      - 13
    - text: 2 claws +13 (1d6+5)
      entries:
      - - damage: 1d6+5
      count: 2
      attack: claws
      bonus:
      - 13
  special:
  - devour secret lore
  - disease
  - pounce
  - powerful bite
  - trip
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: speak with dead
    source: default
    freq: At will
    DC: 15
  - name: detect thoughts
    source: default
    freq: 3/day
    DC: 14
  - name: animate dead
    source: default
    freq: 1/day
  - superscripts:
    - APG
    name: seek thoughts
    source: default
    freq: 1/day
    DC: 15
  sources:
  - name: default
    CL: 9
    concentration: 11
ability_scores:
  STR: 20
  DEX: 13
  CON: 17
  INT: 15
  WIS: 14
  CHA: 14
BAB: 9
CMB: 15
CMB_other: +17 trip
CMD: 26
CMD_other: 32 vs. trip
feats:
- name: Cleave
- name: Combat Expertise
- name: Flyby Attack
- name: Improved Trip
- name: Power Attack
skills:
  Fly: 4
  Intimidate: 8
  Knowledge (any one): 11
  Perception: 8
  Sense Motive: 8
  Survival: 8
languages:
- Common
- Draconic
- Sphinx
ecology:
  environment: warm deserts and hills
  organization: solitary
  treasure_type: standard
special_abilities:
  Devour Secret Lore (Su): When a cynosphinx reduces a living creature below zero
    hit points, it steals some of its essence. Treat the cynosphinx as if it were
    the target of an aid spell with a caster level equal to the dying target's Hit
    Dice. A cynosphinx can only affect a single creature with this effect once in
    a 24 hour period.
  Disease (Ex): 'Carrion fever: Bite-injury; save Fort DC 17; onset 1 day; frequency
    1 day; effect 2 Con damage; cure 2 consecutive saves.'
  Powerful Bite (Ex): A cynosphinx adds 1-1/2 times its Strength bonus to its bite
    attack.
desc_long: Cynosphinxes are hoarders of secret knowledge and guardians of abandoned
  ruins. Those who intrude upon the realm of a cynosphinx and fail to offer a tribute
  of secret knowledge provoke the beast to savage anger. Whereas androsphinxes barter
  information for the sake of achieving enlightenment, cynosphinxes strive to learn
  secrets to gain power over others. Often, a cynosphinx enters a parley hoping to
  secretly learn clandestine information with its ability to read its target's thoughts,
  steering the conversation toward such topics with leading questions. Quick to anger,
  the cynosphinx kills those it feels are inferior, knowing that it still has the
  opportunity to converse with the trespasser after its death. If the knowledge it
  seeks is relayed during clever, amusing conversation, the sphinx rewards the provider
  with invaluable clues to a desired object or location, or simply safe passage through
  its territory, though the cynosphinx rarely shares any of its own secrets willingly.
  A cynosphinx stands 12 feet tall at its powerful shoulders. Built of muscular flesh
  and sinew, a cynosphinx weighs roughly 1,200 pounds.

---

# Sphinx, Cynosphinx
A _[[monsters/Jackal|jackal]]_’s head draped in a tattered headdress extends from a winged, leonine body.
**Source** Pathfinder #82: Secrets of the Sphinx pg. 84
**XP** 2,400

NE Large magical beast
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +8

##### Defense

**AC** 20, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+1 Dex, +10 natural, –1 size)
**hp** 76 (9d10+27)
**Fort** +9, **Ref** +7, **Will** +5
**Immune** disease

##### Offense
**Speed** 30 ft., fly 60 ft. (poor)
**Melee** bite +13 (1d8+7 plus disease and _[[universal monster rules/Trip|trip]]_), 2 claws +13 (1d6+5)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** devour secret lore, disease, _[[universal monster rules/Pounce|pounce]]_, powerful bite, _trip_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +11)
At will—_[[spells/Speak with Dead|speak with dead]]_ (DC 15)
3/day—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 14)
1/day—_[[spells/Animate Dead|animate dead]]_, _[[spells/Seek Thoughts|seek thoughts]]_ (DC 15)

##### Statistics
**Str** 20, **Dex** 13, **Con** 17, **Int** 15, **Wis** 14, **Cha** 14
**Base Atk** +9; **CMB** +15 (+17 _trip_); **CMD** 26 (32 vs. _trip_)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Fly +4, Intimidate +8, Knowledge (any one) +11, Perception +8, Sense Motive +8, Survival +8
**Languages** Common, Draconic, Sphinx

##### Ecology

**Environment** warm deserts and hills
**Organization** solitary
**Treasure** standard

### Special Abilities

**Devour Secret Lore (Su)** When a cynosphinx reduces a living creature below zero hit points, it steals some of its essence. Treat the cynosphinx as if it were the target of an aid spell with a caster level equal to the _[[conditions/Dying|dying]]_ target’s Hit Dice. A cynosphinx can only affect a single creature with this effect once in a 24 hour period.

**Disease (Ex)** Carrion fever: Bite—injury; save Fort DC 17; onset 1 day; frequency 1 day; effect 2 Con damage; cure 2 consecutive saves.

**Powerful Bite (Ex)** A cynosphinx adds 1-1/2 times its Strength bonus to its bite attack.

##### Description

Cynosphinxes are hoarders of secret knowledge and guardians of abandoned ruins. Those who intrude upon the realm of a cynosphinx and fail to offer a tribute of secret knowledge provoke the beast to savage anger. Whereas androsphinxes barter information for the sake of achieving enlightenment, cynosphinxes strive to learn secrets to gain power over others. Often, a cynosphinx enters a parley hoping to secretly learn clandestine information with its ability to read its target’s thoughts, steering the conversation toward such topics with leading questions. Quick to anger, the cynosphinx kills those it feels are inferior, knowing that it still has the opportunity to converse with the trespasser after its death. If the knowledge it seeks is relayed during clever, amusing conversation, the sphinx rewards the provider with invaluable clues to a desired object or location, or simply safe passage through its territory, though the cynosphinx rarely shares any of its own secrets willingly. A cynosphinx stands 12 feet tall at its powerful shoulders. Built of muscular flesh and sinew, a cynosphinx weighs roughly 1,200 pounds.
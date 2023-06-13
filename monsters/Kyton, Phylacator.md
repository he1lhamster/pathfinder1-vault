---
cssclass: [monsters]
title1: Kyton, Phylacator
desc_short: This imposing humanoid is clad in black chainmail with a featureless helm.
  It clutches a serrated dire flail in its gauntlets, and several pairs of manacles
  on its belt writhe of their own accord.
title2: Phylacator
CR: 18
sources:
- name: 'Pathfinder #132: The Six-Legend Soul'
  page: 88
  link: http://paizo.com/products/btpy9xdq?Pathfinder-Adventure-Path-The-SixLegend-Soul
XP: 153600
alignment: LE
size: Medium
type: outsider
subtypes:
- evil
- extraplanar
- kyton
- lawful
initiative:
  bonus: 4
senses:
  darkvision: 60
  true seeing: true
AC:
  AC: 32
  touch: 12
  flat_footed: 30
  components:
    armor: 6
    dex: 2
    natural: 14
HP:
  HP: 297
  long: 18d10+198
  regeneration: 15
  regeneration_weakness: good weapons and spells, silver weapons
saves:
  fort: 19
  ref: 15
  will: 16
DR:
- amount: 15
  weakness: good and silver
immunities:
- cold
- disease
SR: 29
weaknesses:
- iron chair (see text)
speeds:
  base: 20
  base_other: 30 ft. without armor
attacks:
  melee:
  - - text: +1 vicious dire flail +28/+23/+18/+13 (1d8+16 plus 2d6)
      entries:
      - - damage: 1d8+16
        - damage: 2d6
      attack: +1 vicious dire flail
      bonus:
      - 28
      - 23
      - 18
      - 13
    - text: +1 vicious dire flail +28/+23 (1d8+6 plus 2d6)
      entries:
      - - damage: 1d8+6
        - damage: 2d6
      attack: +1 vicious dire flail
      bonus:
      - 28
      - 23
  ranged:
  - - text: mwk manacles +23 (1d4+11 nonlethal plus trip)
      entries:
      - - damage: 1d4+11
          type: nonlethal
        - effect: trip
      attack: mwk manacles
      bonus:
      - 23
  special:
  - animated manacles
  - forbearance
  - unnerving gaze (30 ft., DC 26)
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: deeper darkness
    source: default
    freq: At will
  - name: detect thoughts
    source: default
    freq: At will
    DC: 19
  - name: discern lies
    source: default
    freq: At will
    DC: 21
  - name: order's wrath
    source: default
    freq: At will
    DC: 21
  - name: greater command
    source: default
    freq: 3/day
    DC: 22
  - name: greater teleport
    source: default
    freq: 3/day
  - name: imprisonment
    source: default
    freq: 1/day
    DC: 26
  - name: greater prying eyes
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 18
    concentration: 25
ability_scores:
  STR: 31
  DEX: 18
  CON: 32
  INT: 15
  WIS: 21
  CHA: 24
BAB: 18
CMB: 28
CMB_other: +32 trip
CMD: 32
CMD_other: 44 vs. trip
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: EnforcerAPG
- name: Great Fortitude
- name: Greater Trip
- name: Improved Trip
- name: Improved Two- Weapon Fighting
- name: Two-Weapon Fighting
- name: Weapon Focus (dire flail)
skills:
  Bluff: 28
  Intimidate: 28
  Knowledge (local): 23
  Knowledge (planes): 23
  Knowledge (religion): 23
  Perception: 26
  Sense Motive: 26
  Stealth: 21
languages:
- Languages Common
- Infernal
- telepathy 100 ft.
special_qualities:
- institutionalized
ecology:
  environment: any (Plane of Shadow)
  organization: solitary
  treasure_type: double
  treasure:
  - mwk chain mail
  - +1 vicious/+1 vicious dire flail
  - 4 mwk manacles
  - other treasure
special_abilities:
  Animated Manacles (Su): A phylacator can throw a set of masterwork manacles like
    a masterwork bola. A target tripped by the phylacator's manacles is also entangled
    until it slips free of the manacles or breaks them. Manacles thrown by a phylacator
    automatically expand or contract to fit creatures of any size. As a move action,
    a phylacator can move a single set of manacles within 180 feet up to 30 feet in
    any direction, but if a creature is locked in the manacles, the phylacator must
    succeed at a grapple combat maneuver check against the creature to move it. A
    phylacator can open or close any number of manacles within 180 feet as a free
    action, but it cannot open and close the same manacle in the same round.
  Forbearance (Su): As a full-round action, a phylacator can end one imprisonment
    effect it previously created. This violently rips the target through the Plane
    of Shadow to an unoccupied square adjacent to the phylacator, automatically reducing
    the target to 0 hit points in the process. This is a pain effect.
  Institutionalized (Ex): In exchange for its service, a phylacator forms a bond with
    an institution that consists of 100 or more prisoners. While inside the limits
    of this institution, it gains a +2 bonus on initiative checks and Bluff, Intimidate,
    Knowledge (local), Perception, and Sense Motive checks. It must spend 1 day familiarizing
    itself with the institution to form this bond; once selected, it loses any bond
    it had with a previous location.
  Iron Chair (Su): Each phylacator is bound to a specific metal throne covered with
    a thousand iron spikes, in which it must sit, unarmored, for 15 minutes each day.
    A phylacator that does not perform this ritual loses its regeneration and institutionalized
    abilities until it can do so. The iron chair has hardness 10 and 500 hit points;
    if destroyed, a phylacator must spend 1d12 days on the Plane of Shadow to acquire
    a replacement.
  Unnerving Gaze (Su): A creature that fails its saving throw against a phylacator's
    gaze is overcome with submissive hopelessness, taking a -4 penalty to its CMD
    for 1d4 rounds. This is a mind-affecting fear effect.
desc_long: |-
  Phylacator kytons serve as jailers, torturers, and executioners in the most terrible prisons across the planes. Although a phylacator normally relies on its intimidating presence and booming voice to quell its charges, phylacators also enjoy violence and relish opportunities to quash riots. In combat, a phylacator knocks foes to the ground with its flail and pummels them into submission, relishing the painful feedback it receives when using its weapon. Against fleeing foes, a phylacator hurls manacles it magically animates, incapacitating its foes until it can recover them at it leisure. Since a phylacator is often responsible for keeping prisoners alive, it frequently uses nonlethal tactics-but that doesn't mean it is any less brutal or efficient in its methods.

   Although a phylacator normally wears armor and draped chains to cover its flesh, its skin is midnight blue in color and has the texture of rough-hewn stone. Phylacators are hairless and their steel-gray eyes lack pupils. They are unceasingly patient and can remain utterly motionless for hours.

   Phylacators stand almost 7 feet tall and weigh approximately 350 pounds.

---

# Kyton, Phylacator
This imposing humanoid is clad in black _[[items/Armor/Chainmail|chainmail]]_ with a featureless helm. It clutches a serrated _[[items/Weapon/Dire flail|dire flail]]_ in its gauntlets, and several pairs of manacles on its belt writhe of their own accord.
**Source** Pathfinder #132: The Six-Legend Soul pg. 88
**XP** 153,600

LE Medium outsider (evil, extraplanar, _[[monsters/Kyton|kyton]]_, lawful)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +26

##### Defense

**AC** 32, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+6 armor, +2 Dex, +14 natural)
**hp** 297 (18d10+198); _[[universal monster rules/Regeneration|regeneration]]_ 15 (good weapons and spells, silver weapons)
**Fort** +19, **Ref** +15, **Will** +16
**DR** 15/good and silver; **Immune** cold, disease; **SR** 29
**Weaknesses** iron chair (see text)

##### Offense
**Speed** 20 ft. (30 ft. without armor)
**Melee** +1 _[[items/Weapon Magic Abilities/Vicious|vicious]]_ _dire flail_ +28/+23/+18/+13 (1d8+16 plus 2d6), +1 _vicious_ _dire flail_ +28/+23 (1d8+6 plus 2d6)
**Ranged** mwk manacles +23 (1d4+11 nonlethal plus _[[universal monster rules/Trip|trip]]_)
**Special Attacks** _[[items/Armor Magic Abilities/Animated|animated]]_ manacles, forbearance, unnerving _[[universal monster rules/Gaze|gaze]]_ (30 ft., DC 26)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +25)
Constant—_true seeing_ 
At will—_[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 19), _[[spells/Discern Lies|discern lies]]_ (DC 21), order’s wrath (DC 21) 
3/day—greater _[[spells/Command|command]]_ (DC 22), greater teleport 
1/day—_[[spells/Imprisonment|imprisonment]]_ (DC 26), greater _[[spells/Prying Eyes|prying eyes]]_

##### Statistics
**Str** 31, **Dex** 18, **Con** 32, **Int** 15, **Wis** 21, **Cha** 24
**Base Atk** +18; **CMB** +28 (+32 _trip_); **CMD** 32 (44 vs. _trip_)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, EnforcerAPG, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Greater Trip|Greater Trip]]_, _[[feats/Improved Trip|Improved Trip]]_, Improved Two- Weapon Fighting, _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_dire flail_)
**Skills** Bluff +28, Intimidate +28, Knowledge (local, planes, religion) +23, Perception +26, Sense Motive +26, Stealth +21
**Languages** Languages Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** institutionalized

##### Ecology

**Environment** any (Plane of _[[items/Armor Magic Abilities/Shadow|Shadow]]_)
**Organization** solitary
**Treasure** double (mwk chain mail, +1 vicious/+1 _vicious_ _dire flail_, 4 mwk manacles, other treasure)

### Special Abilities

**_Animated_ Manacles (Su)** A phylacator can throw a set of masterwork manacles like a masterwork bola. A target tripped by the phylacator’s manacles is also _[[conditions/Entangled|entangled]]_ until it slips free of the manacles or breaks them. Manacles thrown by a phylacator automatically expand or contract to fit creatures of any size. As a move action, a phylacator can move a single set of manacles within 180 feet up to 30 feet in any direction, but if a creature is locked in the manacles, the phylacator must succeed at a grapple combat maneuver check against the creature to move it. A phylacator can open or close any number of manacles within 180 feet as a free action, but it cannot open and close the same manacle in the same round.

**Forbearance (Su)** As a full-round action, a phylacator can end one _imprisonment_ effect it previously created. This violently rips the target through the Plane of _Shadow_ to an unoccupied square adjacent to the phylacator, automatically reducing the target to 0 hit points in the process. This is a pain effect.

**Institutionalized (Ex)** In exchange for its service, a phylacator forms a bond with an institution that consists of 100 or more prisoners. While inside the limits of this institution, it gains a +2 bonus on initiative checks and Bluff, Intimidate, Knowledge (local), Perception, and Sense Motive checks. It must spend 1 day familiarizing itself with the institution to form this bond; once selected, it loses any bond it had with a previous location.

**Iron Chair (Su)** Each phylacator is bound to a specific metal throne covered with a thousand iron spikes, in which it must sit, unarmored, for 15 minutes each day. A phylacator that does not perform this ritual loses its _regeneration_ and institutionalized abilities until it can do so. The iron chair has hardness 10 and 500 hit points; if destroyed, a phylacator must spend 1d12 days on the Plane of _Shadow_ to acquire a replacement.

**Unnerving _Gaze_ (Su)** A creature that fails its saving throw against a phylacator’s _gaze_ is overcome with submissive hopelessness, taking a –4 penalty to its CMD for 1d4 rounds. This is a mind-affecting _[[universal monster rules/Fear|fear]]_ effect.

##### Description

Phylacator kytons serve as jailers, torturers, and executioners in the most terrible prisons across the planes. Although a phylacator normally relies on its intimidating presence and booming voice to quell its charges, phylacators also enjoy violence and relish opportunities to quash riots. In combat, a phylacator knocks foes to the ground with its flail and pummels them into submission, relishing the painful feedback it receives when using its weapon. Against fleeing foes, a phylacator hurls manacles it magically animates, incapacitating its foes until it can recover them at it leisure. Since a phylacator is often responsible for keeping prisoners alive, it frequently uses nonlethal tactics—but that doesn’t mean it is any less brutal or efficient in its methods.

Although a phylacator normally wears armor and draped chains to cover its flesh, its skin is midnight blue in color and has the texture of rough-hewn stone. Phylacators are hairless and their steel-gray eyes lack pupils. They are unceasingly patient and can remain utterly motionless for hours.

Phylacators stand almost 7 feet tall and weigh approximately 350 pounds.
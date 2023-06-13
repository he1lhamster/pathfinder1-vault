---
cssclass: [monsters]
title1: Etheroot
desc_short: This leafy bush bears flowers of a variety of shapes and colors, one of
  which resembles a toothy mouth at the end of a long stalk.
title2: Etheroot
CR: 8
sources:
- name: Planar Adventures
  page: 233
  link: http://paizo.com/products/btpya1am
XP: 4800
alignment: N
size: Large
type: plant
subtypes:
- extraplanar
initiative:
  bonus: 10
senses:
  darkvision: 60
  low-light vision: true
  see invisibility: true
AC:
  AC: 21
  touch: 15
  flat_footed: 15
  components:
    dex: 6
    natural: 6
    size: -1
HP:
  HP: 95
  long: 10d8+50
saves:
  fort: 12
  ref: 11
  will: 7
immunities:
- plant traits
speeds:
  base: 20
attacks:
  melee:
  - - text: bite +12 (1d8+4 plus incite emotion)
      entries:
      - - damage: 1d8+4
        - effect: incite emotion
      attack: bite
      bonus:
      - 12
    - text: 6 tentacles +10 (1d4+2 plus trip)
      entries:
      - - damage: 1d4+2
        - effect: trip
      count: 6
      attack: tentacles
      bonus:
      - 10
space: 10
reach: 10
reach_other: 15 ft. with bite
spell_like_abilities:
  entries:
  - name: analyze aura
    source: default
    freq: Constant
    other: emotion only
  - name: see invisibility
    source: default
    freq: Constant
  sources:
  - name: default
    CL: 8
    concentration: 10
ability_scores:
  STR: 18
  DEX: 23
  CON: 20
  INT: 15
  WIS: 18
  CHA: 15
BAB: 7
CMB: 12
CMD: 28
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Improved Initiative
- name: Lightning Reflexes
- name: Multiattack
- name: Weapon Finesse
skills:
  Knowledge (planes): 12
  Perception: 17
  Sense Motive: 14
  Spellcraft: 12
languages:
- telepathy 100 ft.
special_qualities:
- ethereal portal
ecology:
  environment: any (Ethereal Plane)
  organization: solitary
  treasure_type: incidental
special_abilities:
  Ethereal Portal (Su): As a full-round action, an etheroot can create a portal from
    the Ethereal Plane to the corresponding location on the Material Plane in the
    4 squares beneath its body. This portal allows the etheroot's stalked bite and
    tentacles to pass through, but not the rest of its body or any other creatures.
    It also allows the etheroot‘s analyze aura ability to function across planes as
    if the plant were wholly present in the 4 affected squares. If an etheroot moves
    from its location, the portal vanishes immediately. An etheroot can be attacked
    normally by creatures on the Material Plane when its portal is active.
  Incite Emotion (Sp): If an etheroot hits with its bite, it can create the effects
    of its choice of crushing despair, fear, good hope, reckless infatuation, serenity,
    or unadulterated loathing, with the following exceptions. The effect targets only
    the touched creature, its duration is 1 minute, and the DC of the Will save to
    resist the effect is 10 + half the etheroot's Hit Dice + its Charisma modifier
    (DC 17 for a typical etheroot). An etheroot can use its incite emotion ability
    a total number of times per day equal to its Hit Dice (typically 10).
desc_long: Etheroots feed on emotions and ectoplasm. While the Ethereal Plane contains
  ample ectoplasm for their needs, etheroots typically burrow their feeding tendrils
  and roots through to the Material Plane in search of emotional energy. Depending
  upon its mood and the balance of emotions in its body, an etheroot may offer words
  of encouragement and beneficial spells, or it may evoke terror instead. Particularly
  knowledgeable planar travelers may be able to predict an etheroot's appetites by
  observing the colors and shapes of its flowers, which represent the emotional auras
  of the plant's most recent meals. One of the etheroot's favorite delicacies are
  spiritualist's phantoms, as their rare combination of ectoplasmic bodies and intense
  emotions make them uniquely flavorful and satisfying.

---

# Etheroot
This leafy bush bears flowers of a variety of shapes and colors, one of which resembles a toothy mouth at the end of a long stalk.
**Source** _[[items/Weapon Magic Abilities/Planar|Planar]]_ Adventures pg. 233
**XP** 4,800

N Large plant (extraplanar)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +17

##### Defense

**AC** 21, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+6 Dex, +6 natural, –1 size)
**hp** 95 (10d8+50)
**Fort** +12, **Ref** +11, **Will** +7
**Immune** _[[universal monster rules/Plant Traits|plant traits]]_

##### Offense
**Speed** 20 ft.
**Melee** bite +12 (1d8+4 plus incite emotion), 6 tentacles +10 (1d4+2 plus _[[universal monster rules/Trip|trip]]_)
**Space** 10 ft., **Reach** 10 ft. (15 ft. with bite)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +10)
Constant—_[[spells/Analyze Aura|analyze aura]]_ (emotion only), _see invisibility_

##### Statistics
**Str** 18, **Dex** 23, **Con** 20, **Int** 15, **Wis** 18, **Cha** 15
**Base Atk** +7; **CMB** +12; **CMD** 28 (can’t be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Knowledge (planes) +12, Perception +17, Sense Motive +14, Spellcraft +12
**Languages** _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** ethereal portal

##### Ecology

**Environment** any (Ethereal Plane)
**Organization** solitary
**Treasure** incidental

### Special Abilities

**Ethereal Portal (Su)** As a full-round action, an _[[monsters/Etheroot|etheroot]]_ can create a portal from the Ethereal Plane to the corresponding location on the Material Plane in the 4 squares beneath its body. This portal allows the _etheroot_’s stalked bite and tentacles to pass through, but not the rest of its body or any other creatures. It also allows the _etheroot_‘s _analyze aura_ ability to function across planes as if the plant were wholly present in the 4 affected squares. If an _etheroot_ moves from its location, the portal vanishes immediately. An _etheroot_ can be attacked normally by creatures on the Material Plane when its portal is active.

**Incite Emotion (Sp)** If an _etheroot_ hits with its bite, it can create the effects of its choice of _[[spells/Crushing Despair|crushing despair]]_, _[[universal monster rules/Fear|fear]]_, _[[spells/Good Hope|good hope]]_, _[[spells/Reckless Infatuation|reckless infatuation]]_, _[[spells/Serenity|serenity]]_, or _[[spells/Unadulterated Loathing|unadulterated loathing]]_, with the following exceptions. The effect targets only the touched creature, its duration is 1 minute, and the DC of the Will save to resist the effect is 10 + half the _etheroot_’s Hit Dice + its Charisma modifier (DC 17 for a typical _etheroot_). An _etheroot_ can use its incite emotion ability a total number of times per day equal to its Hit Dice (typically 10).

##### Description

Etheroots feed on emotions and ectoplasm. While the Ethereal Plane contains ample ectoplasm for their needs, etheroots typically _[[universal monster rules/Burrow|burrow]]_ their feeding tendrils and roots through to the Material Plane in search of emotional energy. Depending upon its mood and the balance of emotions in its body, an _etheroot_ may offer words of encouragement and beneficial spells, or it may evoke terror instead. Particularly knowledgeable _planar_ travelers may be able to predict an _etheroot_’s appetites by observing the colors and shapes of its flowers, which represent the emotional auras of the plant’s most recent meals. One of the _etheroot_’s favorite delicacies are _[[classes/Spiritualist|spiritualist]]_’s phantoms, as their rare combination of ectoplasmic bodies and intense emotions make them uniquely flavorful and satisfying.
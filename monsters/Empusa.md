---
cssclass: [monsters]
title1: Empusa
desc_short: This beautiful woman has red antennae, gossamer insectile wings, a wasp's
  legs, and a serpentine whip.
title2: Empusa
CR: 13
sources:
- name: Planar Adventures
  page: 232
  link: http://paizo.com/products/btpya1am
XP: 25600
alignment: CN
size: Medium
type: outsider
subtypes:
- chaotic
- extraplanar
- shapechanger
initiative:
  bonus: 8
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 28
  touch: 18
  flat_footed: 20
  components:
    dex: 8
    natural: 10
HP:
  HP: 174
  long: 12d10+108
  fast_healing: 5
saves:
  fort: 17
  ref: 16
  will: 10
DR:
- amount: 10
  weakness: lawful
immunities:
- disease
- electricity
- poison
SR: 24
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: lash +22/+17/+12 (1d6+5/×2 plus poison)
      entries:
      - - damage: 1d6+5
          crit_multiplier: 2
        - effect: poison
      attack: lash
      bonus:
      - 22
      - 17
      - 12
  special:
  - lash
  - sneak attack +3d6
space: 5
reach: 5
reach_other: 10 ft. with lash
spell_like_abilities:
  entries:
  - name: tongues
    source: default
    freq: Constant
  - name: invisibility
    source: default
    freq: At will
  - name: major image
    source: default
    freq: At will
    DC: 20
  - name: modify memory
    source: default
    freq: At will
    DC: 20
  - name: suggestion
    source: default
    freq: At will
    DC: 19
  - name: charm monster
    source: default
    freq: 3/day
    DC: 20
  - name: phantasmal vengeance
    source: default
    freq: 3/day
    DC: 20
  - name: teleport
    source: default
    freq: 3/day
    other: self plus 50 lbs. of gear only
  - name: mislead
    source: default
    freq: 1/day
    DC: 22
  - name: true seeing
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 13
    concentration: 19
ability_scores:
  STR: 17
  DEX: 26
  CON: 29
  INT: 18
  WIS: 22
  CHA: 23
BAB: 12
CMB: 20
CMD: 33
feats:
- name: Agile Maneuvers
- name: Combat Expertise
- name: Combat Reflexes
- name: Deceitful
- name: Improved Feint
- name: Weapon Finesse
skills:
  Acrobatics: 23
  Bluff: 25
  Disguise: 25
  Fly: 27
  Knowledge (planes): 13
  Knowledge (religion): 10
  Perception: 21
  Ride: 23
  Sense Motive: 21
  Sleight of Hand: 23
  Stealth: 23
languages:
- Common
- Elven
- tongues
special_qualities:
- change shape (elf, alter self)
ecology:
  environment: any (Elysium)
  organization: solitary, pair, or vengeance (3-6)
  treasure_type: standard
special_abilities:
  Lash (Su): |-
    As a move action, an empusa can manifest a whip-like weapon that appears to be a coiling serpent-once manifested, the lash exists as long as the empusa carries it. A lash vanishes if it is disarmed or the empusa drops it or is slain. An empusa's lash has a reach of 10 feet and deals 1d6 points of slashing damage on a hit. In addition, a creature damaged by the lash is affected by its toxic venom.

     Lash Venom: Lash-injury; save Fort DC 25; frequency 1/round for 6 rounds; effect 1d4 Wis damage plus confused for 1 round; cure 2 consecutive saves. The save DC is Constitution-based.
  Phantasmal Vengeance (Sp): This spell-like ability functions as phantasmal killer,
    save that the image it creates is of a creature or person who the viewer has wronged
    in their past (or of the empusa herself if there are no other appropriate options).
    If the target of a phantasmal vengeance fails his Fortitude save, the empusa can
    opt to have the victim become paralyzed for 1 hour rather than die from fear.
desc_long: |-
  The empusas are Calistria's handmaidens and elite agents. Effortlessly passing for elves, empusas move secretly through society, manipulating mortals and influencing events to achieve their missions of vengeance.

   An empusa stands 6 feet tall and weighs 120 pounds.

---

# Empusa
This beautiful woman has red antennae, gossamer insectile wings, a wasp’s legs, and a serpentine _[[items/Weapon/Whip|whip]]_.
**Source** _[[items/Weapon Magic Abilities/Planar|Planar]]_ Adventures pg. 232
**XP** 25,600

CN Medium outsider (chaotic, extraplanar, shapechanger)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +21

##### Defense

**AC** 28, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+8 Dex, +10 natural)
**hp** 174 (12d10+108); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +17, **Ref** +16, **Will** +10
**DR** 10/lawful; **Immune** disease, electricity, poison; **SR** 24

##### Offense
**Speed** 30 ft., fly 60 ft. (good)
**Melee** lash +22/+17/+12 (1d6+5/×2 plus poison)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with lash)
**Special Attacks** lash, sneak attack +3d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +19)
Constant—_[[spells/Tongues|tongues]]_
At will—_[[spells/Invisibility|invisibility]]_, _[[spells/Major Image|major image]]_ (DC 20), _[[spells/Modify Memory|modify memory]]_ (DC 20), _[[spells/Suggestion|suggestion]]_ (DC 19)
3/day—_[[spells/Charm Monster|charm monster]]_ (DC 20), _[[items/Armor Magic Abilities/Phantasmal|phantasmal]]_ _[[feats/Vengeance|vengeance]]_ (DC 20), teleport (self plus 50 lbs. of gear only)
1/day—_[[spells/Mislead|mislead]]_ (DC 22), _[[spells/True Seeing|true seeing]]_

##### Statistics
**Str** 17, **Dex** 26, **Con** 29, **Int** 18, **Wis** 22, **Cha** 23
**Base Atk** +12; **CMB** +20; **CMD** 33
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deceitful|Deceitful]]_, _[[feats/Improved Feint|Improved Feint]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +23, Bluff +25, Disguise +25, Fly +27, Knowledge (planes) +13, Knowledge (religion) +10, Perception +21, Ride +23, Sense Motive +21, Sleight of Hand +23, Stealth +23
**Languages** Common, Elven; _tongues_
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (elf, _[[spells/Alter Self|alter self]]_)

##### Ecology

**Environment** any (Elysium)
**Organization** solitary, pair, or _vengeance_ (3–6)
**Treasure** standard

### Special Abilities

**Lash (Su)** As a move action, an _[[monsters/Empusa|empusa]]_ can manifest a whip-like weapon that appears to be a coiling serpent—once manifested, the lash exists as long as the _empusa_ carries it. A lash vanishes if it is disarmed or the _empusa_ drops it or is slain. An _empusa_’s lash has a reach of 10 feet and deals 1d6 points of slashing damage on a hit. In addition, a creature damaged by the lash is affected by its _[[items/Weapon Magic Abilities/Toxic|toxic]]_ venom.

Lash Venom: Lash—injury; save Fort DC 25; frequency 1/round for 6 rounds; effect 1d4 Wis damage plus _[[conditions/Confused|confused]]_ for 1 round; cure 2 consecutive saves. The save DC is Constitution-based.

**_Phantasmal_ _Vengeance_ (Sp)** This spell-like ability functions as _[[spells/Phantasmal Killer|phantasmal killer]]_, save that the image it creates is of a creature or person who the viewer has wronged in their past (or of the _empusa_ herself if there are no other appropriate options). If the target of a _phantasmal_ _vengeance_ fails his Fortitude save, the _empusa_ can opt to have the victim become _[[conditions/Paralyzed|paralyzed]]_ for 1 hour rather than die from _[[universal monster rules/Fear|fear]]_.

##### Description

The empusas are Calistria’s handmaidens and elite agents. Effortlessly passing for elves, empusas move secretly through society, manipulating mortals and influencing events to achieve their missions of _vengeance_.

An _empusa_ stands 6 feet tall and weighs 120 pounds.
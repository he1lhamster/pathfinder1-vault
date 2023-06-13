---
cssclass: [monsters]
title1: Pukwudgie
desc_short: A merging of an emaciated man and a porcupine, this sinister creature
  smells of death and decay.
title2: Pukwudgie
CR: 7
sources:
- name: Bestiary 3
  page: 223
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 3200
alignment: NE
size: Small
type: monstrous humanoid
subtypes:
- shapechanger
initiative:
  bonus: 4
senses:
  darkvision: 60
  deathwatch: true
  detect good: true
  detect magic: true
AC:
  AC: 20
  touch: 16
  flat_footed: 15
  components:
    dex: 4
    dodge: 1
    natural: 4
    size: 1
HP:
  HP: 85
  long: 9d10+36
saves:
  fort: 7
  ref: 10
  will: 10
immunities:
- poison
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 claws +14 (1d4+2 plus poison)
      entries:
      - - damage: 1d4+2
        - effect: poison
      count: 2
      attack: claws
      bonus:
      - 14
  ranged:
  - - text: 2 quills +15 (1d4+2 plus poison)
      entries:
      - - damage: 1d4+2
        - effect: poison
      count: 2
      attack: quills
      bonus:
      - 15
  special:
  - sneak attack +3d6
  - spawn undead
spell_like_abilities:
  entries:
  - name: deathwatch
    source: default
    freq: Constant
  - name: detect good
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: command undead
    source: default
    freq: At will
    DC: 16
  - name: produce flame
    source: default
    freq: At will
  - name: animate dead
    source: default
    freq: 3/day
  - name: death knell
    source: default
    freq: 3/day
    DC: 16
  - name: invisibility
    source: default
    freq: 3/day
  - name: ray of enfeeblement
    source: default
    freq: 3/day
    DC: 15
  - name: scare
    source: default
    freq: 3/day
    DC: 16
  - name: nondetection
    source: default
    freq: 1/day
    DC: 17
  sources:
  - name: default
    CL: 10
    concentration: 14
ability_scores:
  STR: 14
  DEX: 18
  CON: 19
  INT: 15
  WIS: 14
  CHA: 19
BAB: 9
CMB: 10
CMD: 25
feats:
- name: Dodge
- name: Iron Will
- name: Mobility
- name: Weapon Finesse
- name: Weapon Focus (quill)
skills:
  Bluff: 10
  Heal: 10
  Knowledge (arcana): 11
  Knowledge (religion): 11
  Perception: 13
  Spellcraft: 11
  Stealth: 16
languages:
- Common
- Draconic
- Infernal
special_qualities:
- change shape (porcupine, beast shape II)
ecology:
  environment: temperate forests, hills, or mountains
  organization: solitary, pair, or cult (3-10)
  treasure_type: standard
special_abilities:
  Spawn Undead (Su): Any creature slain by a pukwudgie's poisonous quills rises in
    24 hours as a zombie. Undead created by this ability are not immediately under
    the control of a pukwudgie, but they receive a -4 penalty on saves against a pukwudgie's
    control undead spell-like ability.
  Poison (Su): Claw or quill-injury; save Fort DC 18; frequency 1/round for 6 rounds;
    effect 1d3 Con damage; cure 2 consecutive saves. The save DC is Constitution-based.
  Quills (Ex): A pukwudgie can fire two of its quills as a ranged attack as a standard
    action. These quills have a range increment of 40 feet. Any creature attacking
    a pukwudgie with light or one-handed melee weapons, natural weapons, or an unarmed
    strike takes 1d3 points of piercing damage. A creature that grapples a pukwudgie
    takes 2d4 points of piercing damage. Anyone who takes damage from these quills
    is also exposed to the pukwudgie's poison.
desc_long: |-
  The vile pukwudgie is a small, hunchbacked humanoid covered with long, sharp quills. These quills, like those of a porcupine, help protect the small creature but are also dangerous offensive weapons, for the quills hold a deadly poison that animates those it slays as zombies. This necromantic nature, along with their penchant for torment and sadistic ways, makes pukwudgies evil to the core. A pukwudgie stands 3-1/2 feet tall and weighs a little more than 30 pounds.

  Pukwudgies are frequently found in the company of undead. This retinue usually consists of zombies and skeletons created via their poisonous quills ability or their ability to animate dead bodies. They have a strong preference for animating the bodies of dead animals over other creatures, and often use undead animals as mounts.

  A pukwudgie usually stays away from well-traveled areas and humanoid settlements, but may sometimes slip into small villages in the night to steal children. The little horrors enjoy the tender flesh of newborn babies immensely, and are often willing to go through great personal risk to secure infantile repasts when they are available. Their delight in arson only further makes them a bane of small villages.

---

# Pukwudgie
A _[[items/Armor Magic Abilities/Merging|merging]]_ of an emaciated man and a _[[monsters/Porcupine|porcupine]]_, this sinister creature smells of death and decay.
**Source** Bestiary 3 pg. 223
**XP** 3,200

NE Small monstrous humanoid (shapechanger)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Deathwatch|deathwatch]]_, _[[spells/Detect Good|detect good]]_, _[[spells/Detect Magic|detect magic]]_; Perception +13

##### Defense

**AC** 20, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 Dex, +1 dodge, +4 natural, +1 size)
**hp** 85 (9d10+36)
**Fort** +7, **Ref** +10, **Will** +10
**Immune** poison

##### Offense
**Speed** 30 ft.
**Melee** 2 claws +14 (1d4+2 plus poison)
**Ranged** 2 quills +15 (1d4+2 plus poison)
**Special Attacks** sneak attack +3d6, spawn undead
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +14)
Constant—_deathwatch_, _detect good_, _detect magic_
At will—_[[spells/Command Undead|command undead]]_ (DC 16), _[[spells/Produce Flame|produce flame]]_
3/day—_[[spells/Animate Dead|animate dead]]_, _[[spells/Death Knell|death knell]]_ (DC 16), _[[spells/Invisibility|invisibility]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 15), _[[spells/Scare|scare]]_ (DC 16)
1/day—_[[spells/Nondetection|nondetection]]_ (DC 17)

##### Statistics
**Str** 14, **Dex** 18, **Con** 19, **Int** 15, **Wis** 14, **Cha** 19
**Base Atk** +9; **CMB** +10; **CMD** 25
**Feats** _Dodge_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (quill)
**Skills** Bluff +10, _[[spells/Heal|Heal]]_ +10, Knowledge (arcana) +11, Knowledge (religion) +11, Perception +13, Spellcraft +11, Stealth +16
**Languages** Common, Draconic, Infernal
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_porcupine_, _[[spells/Beast Shape II|beast shape II]]_)

##### Ecology

**Environment** temperate forests, hills, or mountains
**Organization** solitary, pair, or cult (3–10)
**Treasure** standard

### Special Abilities
**Spawn Undead (Su)** Any creature slain by a _[[monsters/Pukwudgie|pukwudgie]]_’s poisonous quills rises in 24 hours as a zombie. Undead created by this ability are not immediately under the control of a _pukwudgie_, but they receive a –4 penalty on saves against a _pukwudgie_’s _[[spells/Control Undead|control undead]]_ spell-like ability.

**Poison (Su) **Claw or quill—injury; save Fort DC 18; frequency 1/round for 6 rounds; effect 1d3 Con damage; cure 2 consecutive saves. The save DC is Constitution-based.

**Quills (Ex)** A _pukwudgie_ can fire two of its quills as a ranged attack as a standard action. These quills have a range increment of 40 feet. Any creature attacking a _pukwudgie_ with light or one-handed melee weapons, natural weapons, or an unarmed strike takes 1d3 points of piercing damage. A creature that grapples a _pukwudgie_ takes 2d4 points of piercing damage. Anyone who takes damage from these quills is also exposed to the _pukwudgie_’s poison.

##### Description

The vile _pukwudgie_ is a small, hunchbacked humanoid covered with long, sharp quills. These quills, like those of a _porcupine_, help protect the small creature but are also dangerous offensive weapons, for the quills hold a _[[items/Weapon Magic Abilities/Deadly|deadly]]_ poison that animates those it slays as zombies. This necromantic nature, along with their penchant for torment and sadistic ways, makes pukwudgies evil to the core. A _pukwudgie_ stands 3-1/2 feet tall and weighs a little more than 30 pounds.

Pukwudgies are frequently found in the company of undead. This retinue usually consists of zombies and skeletons created via their poisonous quills ability or their ability to _animate dead_ bodies. They have a strong preference for animating the bodies of dead animals over other creatures, and often use undead animals as mounts.

A _pukwudgie_ usually stays away from well-traveled areas and humanoid settlements, but may sometimes slip into small villages in the night to steal children. The little horrors enjoy the tender flesh of newborn babies immensely, and are often willing to go through great personal risk to secure infantile repasts when they are available. Their delight in arson only further makes them a _[[spells/Bane|bane]]_ of small villages.
---
cssclass: [monsters]
title1: Tobongo (Mwangi Treant)
desc_short: Tearing its elephantine roots free from the soil, an enormous tree unfurls
  long, tangled branches into arms ending in massive claws.
title2: Tobongo (Mwangi Treant)
CR: 12
sources:
- name: Heart of the Jungle
  page: 61
  link: http://paizo.com/store/downloads/pathfinder/pathfinderChronicles/pathfinderRPG/v5748btpy8evh
XP: 19200
alignment: N
size: Gargantuan
type: plant
initiative:
  bonus: -1
senses:
  low-light vision: true
AC:
  AC: 27
  touch: 5
  flat_footed: 27
  components:
    dex: -1
    natural: 22
    size: -4
HP:
  HP: 175
  long: 14d8+112
saves:
  fort: 17
  ref: 3
  will: 9
defensive_abilities:
- plant traits
DR:
- amount: 10
  weakness: slashing
weaknesses:
- vulnerability to fire
speeds:
  base: 40
attacks:
  melee:
  - - text: 2 slams +19 (4d6+12/19-20 plus grab)
      entries:
      - - damage: 4d6+12
          crit_range: 19-20
        - effect: grab
      count: 2
      attack: slams
      bonus:
      - 19
  ranged:
  - - text: rock +6 (4d6+18)
      entries:
      - - damage: 4d6+18
      attack: rock
      bonus:
      - 6
  special:
  - curse of barkflesh
  - rock throwing (240 ft.)
  - shake the earth
  - trample (4d6+18, DC 29)
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: entangle
    source: default
    freq: At will
    DC: 15
  sources:
  - name: default
    CL: 11
    concentration: 15
ability_scores:
  STR: 35
  DEX: 8
  CON: 26
  INT: 14
  WIS: 16
  CHA: 18
BAB: 10
CMB: 26
CMB_other: +28 to sunder
CMD: 35
CMD_other: 37 vs. sunder
feats:
- name: Alertness
- name: Improved Critical (slam)
- name: Improved Natural Attack (slam)
- name: Improved Sunder
- name: Iron Will
- name: Power Attack
- name: Weapon Focus (slam)
skills:
  Diplomacy: 14
  Intimidate: 16
  Knowledge (local): 14
  Knowledge (nature): 14
  Perception: 12
  Sense Motive: 9
  Stealth: -8
    in forests: 8
  _racial_mods:
    Stealth:
      in forests: 16
languages:
- Polyglot
- Sylvan
- Treant
- treespeech
special_qualities:
- animate trees
- double damage against objects
ecology:
  environment: warm jungles
  organization: solitary or grove (2-7)
  treasure_type: standard
special_abilities:
  Animate Trees (Sp): A tobongo can animate any trees within 180 feet at will, controlling
    up to two trees at a time. It takes 1 full round for a tree to uproot itself,
    after which it moves at a speed of 10 feet and fights as a standard treant, gaining
    the treant's vulnerability to fire (although it has only one slam attack and lacks
    the treant's animation and rock-throwing abilities). If the tobongo that animated
    it terminates the animation, moves out of range, or is incapacitated, the tree
    immediately takes root wherever it is and returns to its normal state.
  Curse of Barkflesh (Su): |-
    Following a successful grapple, a tobongo can dig its spiky branches into its victim, infecting him with a foul and potent curse. Unless he succeeds at a DC 20 Fortitude save, the victim's flesh immediately begins to harden and grow uncontrollably like tree bark, and he takes 1d4 points of Dexterity damage per day until his Dexterity reaches 0. At this point, the victim turns entirely stiff, grows roots, and transforms into a new, unintelligent tree, preventing any form of resurrection short of wish or miracle. The effect can be slowed by pruning the victim once per hour, slicing off the strange growths. Pruning inflicts 1d6 points of damage on the victim, but it negates the need to make a new Fortitude save. If the victim goes without pruning for more than an hour, the barkflesh takes over and he must immediately make the Fortitude save for the day or suffer the Dexterity damage. The save DC is Wisdom-based.

    Curse of Barkflesh: Grapple- injury; save Fort DC 20; frequency 1/ day; effect 1d4 Dex damage, when Dex reaches 0, target transforms into a tree.
  Double Damage Against Objects (Ex): A tobongo or animated tree that makes a full
    attack against an object or structure deals double damage.
  Shake the Earth (Ex): A rooted tobongo can, as a full-round action, uproot itself,
    buckling the surrounding earth in a 60-foot radius. Living creatures within the
    radius must make a DC 29 Reflex save or fall prone and take 1d6 points of damage.
    Man-made structures within the area of effect must make a DC 29 Fortitude save
    or take 4d6 points of structural damage. Once uprooted, the tobongo cannot use
    this action again until it re-roots itself. It takes the creature at least 1 hour
    to root effectively. The save DC is Strength-based.
  Treespeech (Ex): A tobongo has the ability to converse with plants as if subject
    to a continual speak with plants spell, and most plants greet it with an attitude
    of friendly or helpful.
desc_long: There is no description for this monster.

---

# Tobongo (Mwangi Treant)
Tearing its elephantine roots free from the soil, an enormous tree unfurls long, tangled branches into arms ending in massive claws.
**Source** Heart of the Jungle pg. 61
**XP** 19,200

N Gargantuan plant
**Init** -1; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +12

##### Defense

**AC** 27, touch 5, _[[conditions/Flat-Footed|flat-footed]]_ 27 (-1 Dex, +22 natural, -4 size)
**hp** 175 (14d8+112)
**Fort** +17, **Ref** +3, **Will** +9
**Defensive Abilities** _[[universal monster rules/Plant Traits|plant traits]]_; **DR** 10/slashing
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to fire

##### Offense
**Speed** 40 ft.
**Melee** 2 slams +19 (4d6+12/19-20 plus _[[universal monster rules/Grab|grab]]_)
**Ranged** rock +6 (4d6+18)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** curse of barkflesh, _[[universal monster rules/Rock Throwing|rock throwing]]_ (240 ft.), shake the earth, _[[universal monster rules/Trample|trample]]_ (4d6+18, DC 29)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th, concentration +15)
At will - _[[spells/Entangle|entangle]]_ (DC 15)

##### Statistics
**Str** 35, **Dex** 8, **Con** 26, **Int** 14, **Wis** 16, **Cha** 18
**Base Atk** +10; **CMB** +26 (+28 to sunder); **CMD** 35 (37 vs. sunder)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Improved Critical|Improved Critical]]_ (slam), _[[feats/Improved Natural Attack|Improved Natural Attack]]_ (slam), _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (slam)
**Skills** Diplomacy +14, Intimidate +16, Knowledge (local) +14, Knowledge (nature) +14, Perception +12, Sense Motive +9, Stealth –8 (+8 in forests); **Racial Modifiers** +16 Stealth in forests
**Languages** Polyglot, Sylvan, _[[monsters/Treant|Treant]]_; treespeech
**SQ** animate trees, double damage against objects

##### Ecology

**Environment** warm jungles
**Organization** solitary or grove (2-7)
**Treasure** standard

### Special Abilities

**Animate Trees (Sp)** A tobongo can animate any trees within 180 feet at will, controlling up to two trees at a time. It takes 1 full round for a tree to uproot itself, after which it moves at a speed of 10 feet and fights as a standard _treant_, gaining the _treant_’s _vulnerability_ to fire (although it has only one slam attack and lacks the _treant_’s animation and rock-throwing abilities). If the tobongo that _[[items/Armor Magic Abilities/Animated|animated]]_ it terminates the animation, moves out of range, or is incapacitated, the tree immediately takes _[[spells/Root|root]]_ wherever it is and returns to its normal state.

**Curse of Barkflesh (Su)** Following a successful grapple, a tobongo can dig its spiky branches into its victim, infecting him with a foul and _[[items/Weapon Magic Abilities/Potent|potent]]_ curse. Unless he succeeds at a DC 20 Fortitude save, the victim’s flesh immediately begins to harden and grow uncontrollably like tree bark, and he takes 1d4 points of Dexterity damage per day until his Dexterity reaches 0. At this point, the victim turns entirely stiff, grows roots, and transforms into a new, unintelligent tree, preventing any form of _[[spells/Resurrection|resurrection]]_ short of _[[spells/Wish|wish]]_ or _[[spells/Miracle|miracle]]_. The effect can be slowed by pruning the victim once per hour, slicing off the strange growths. Pruning inflicts 1d6 points of damage on the victim, but it negates the need to make a new Fortitude save. If the victim goes without pruning for more than an hour, the barkflesh takes over and he must immediately make the Fortitude save for the day or suffer the Dexterity damage. The save DC is Wisdom-based.

Curse of Barkflesh: Grapple— injury; save Fort DC 20; frequency 1/ day; effect 1d4 Dex damage, when Dex reaches 0, target transforms into a tree.

**Double Damage Against Objects (Ex)** A tobongo or _animated_ tree that makes a full attack against an object or structure deals double damage.
**Shake the Earth (Ex)** A rooted tobongo can, as a full-round action, uproot itself, buckling the surrounding earth in a 60-foot radius. Living creatures within the radius must make a DC 29 Reflex save or fall _[[conditions/Prone|prone]]_ and take 1d6 points of damage. Man-made structures within the area of effect must make a DC 29 Fortitude save or take 4d6 points of structural damage. Once uprooted, the tobongo cannot use this action again until it re-roots itself. It takes the creature at least 1 hour to _root_ effectively. The save DC is Strength-based.

**Treespeech (Ex)** A tobongo has the ability to converse with plants as if subject to a continual _[[spells/Speak with Plants|speak with plants]]_ spell, and most plants greet it with an attitude of friendly or helpful.

There is no description for this monster.
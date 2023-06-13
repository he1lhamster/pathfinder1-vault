---
cssclass: [monsters]
title1: Daemon, Nixudaemon
desc_short: This four-armed fiend has blue-green skin covered in white scars. Its
  two upper arms end in long, barbed whips of calloused flesh.
title2: Nixudaemon
CR: 7
sources:
- name: 'Pathfinder #96: Shadow of the Storm Tyrant'
  page: 88
  link: http://paizo.com/products/btpy9et9?Pathfinder-Adventure-Path-96-Shadow-of-the-Storm-Tyrant
XP: 3200
alignment: NE
size: Large
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 5
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 20
  touch: 10
  flat_footed: 19
  components:
    dex: 1
    natural: 10
    size: -1
HP:
  HP: 95
  long: 10d10+40
  fast_healing: 2
saves:
  fort: 7
  ref: 8
  will: 9
DR:
- amount: 10
  weakness: good or silver
immunities:
- acid
- daze
- death effects
- disease
- exhaustion
- fatigue
- nonlethal damage
- paralysis
- poison
- sleep
- stun
resistances:
  cold: 10
  electricity: 10
  fire: 10
SR: 18
speeds:
  base: 40
attacks:
  melee:
  - - text: 2 slams +12 (1d8+3)
      entries:
      - - damage: 1d8+3
      count: 2
      attack: slams
      bonus:
      - 12
    - text: 2 +1 deadly merciful vicious whip arms +13 (1d8+4 plus grab)
      entries:
      - - damage: 1d8+4
        - effect: grab
      count: 2
      attack: +1 deadly merciful vicious whip arms
      bonus:
      - 13
  special:
  - constrict (1d8+4)
  - damning scourge
  - dead tired
  - enslave (DC 18)
space: 10
reach: 10
reach_other: 20 ft. with whip arms
spell_like_abilities:
  entries:
  - name: deathwatch
    source: default
    freq: Constant
  - name: greater teleport
    source: default
    freq: At Will
    other: self plus 50 lbs. only
  - name: heroism
    source: default
    freq: 3/day
  - name: waves of fatigue
    source: default
    freq: 3/day
    DC: 18
  - superscripts:
    - UM
    name: temporary resurrection
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 10
    concentration: 13
ability_scores:
  STR: 17
  DEX: 13
  CON: 19
  INT: 14
  WIS: 14
  CHA: 16
BAB: 10
CMB: 14
CMB_other: +16 disarm, +16 trip, +18 grapple
CMD: 25
CMD_other: 27 vs. disarm, 27 vs. trip
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Improved Disarm
- name: Improved Initiative
- name: Improved Trip
skills:
  Acrobatics: 12
  Bluff: 16
  Diplomacy: 14
  Heal: 13
  Intimidate: 16
  Knowledge (planes): 11
  Perception: 15
  Sense Motive: 15
  Stealth: 10
languages:
- Abyssal
- Common
- Draconic
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Abaddon)
  organization: solitary, pair, or corps (3-5)
  treasure_type: standard
special_abilities:
  Damning Scourge (Su): Each of a nixudaemon's upper arms functions as a Large +1
    deadlyUE mercifulUE viciousUE whip. Attacks with these whips count as natural
    attacks for the nixudaemon, have a reach of 20 feet, and don't provoke attacks
    of opportunity. The whips can't be disarmed or sundered, nor can they be dropped
    to allow the nixudaemon to avoid being tripped because of failing a combat maneuver
    check to trip. The nixudaemon decides before each attack roll whether to apply
    the weapon's merciful special ability, its vicious special ability, both, or neither.
  Dead Tired (Su): A nixudaemon's attacks drain every bit of vitality from its victims
    when they die. Raising a creature killed by a nixudaemon (via raise dead or another
    effect that restores life) requires a successful DC 20 caster level check. The
    restored creature gains the exhausted condition, regardless of the spell used
    to raise it. The DC of this caster level check is Charisma-based, and includes
    a +2 racial bonus. A nixudaemon can use its temporary resurrection spell-like
    ability without attempting this check, even if another nixudaemon killed the subject.
  Enslave (Su): If a nixudaemon successfully uses its grab ability to grapple a foe
    with its whip attack, its tendril wraps around the victim's throat. The daemon
    can forgo its constrict damage and instead attempt to dominate the subject, as
    the spell dominate monster (Will DC 18 negates). A creature dominated by a nixudaemon
    is immune to fatigue, exhaustion, and pain effects. At the beginning of its turn,
    a dominated slave automatically receives a new saving throw to end the effect.
    The nixudaemon can dominate only one creature at a time per whip arm it possesses
    (typically two). The save DC for this ability is Charisma-based.
desc_long: |-
  Nixudaemons, or “toil daemons,” epitomize death by exploitation and extreme exertion. These fiends savor the moment when a desperate scholar collapses while putting in long, unappreciated hours, or when a galley slave finally succumbs to the lash. They drive burdened subjects before them to great effect, even resurrecting fallen servants for a brief time to complete vital tasks. Their skill for squeezing the last bit of energy from those under their supervision makes them invaluable to slavers, who pay the daemons in coin, information, and souls for their aid.

  Nixudaemons exemplify the cruelty and disdain all daemonkind display toward the living. They lash out at their subjects, whipping the life out of them slowly. If it serves the daemon's purposes, or if time allows for another game of torture, a nixudaemon will revive its subject for another day. Typically, a nixudaemon uses this ability to incite a band of slaves to work harder; it dominates the weakest members of the workers to temporarily bolster them, then saps their last ounce of strength before discarding them as spent husks.

  Most nixudaemons stand 10 feet tall and weigh 600 pounds. Sages report that the fiends grow larger and stronger as they age, absorbing the weariness of their victims over centuries. The greatest toil daemons are said to tower over their younger cousins, growing additional whip-arms and learning powerful spells that exhaust or even kill those who dare offend them.

---

# Daemon, Nixudaemon
This four-armed fiend has blue-green skin covered in white scars. Its two upper arms end in long, barbed whips of calloused flesh.
**Source** Pathfinder #96: _[[items/Armor Magic Abilities/Shadow|Shadow]]_ of the Storm Tyrant pg. 88
**XP** 3,200

NE Large outsider (daemon, evil, extraplanar)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +15

##### Defense

**AC** 20, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+1 Dex, +10 natural, –1 size)
**hp** 95 (10d10+40); _[[universal monster rules/Fast Healing|fast healing]]_ 2
**Fort** +7, **Ref** +8, **Will** +9
**DR** 10/good or silver; **Immune** acid, _[[spells/Daze|daze]]_, death effects, disease, exhaustion, fatigue, nonlethal damage, _[[universal monster rules/Paralysis|paralysis]]_, poison, sleep, stun; **Resist** cold 10, electricity 10, fire 10; **SR** 18

##### Offense
**Speed** 40 ft.
**Melee** 2 slams +12 (1d8+3), 2 +1 _[[items/Weapon Magic Abilities/Deadly|deadly]]_ _[[items/Weapon Magic Abilities/Merciful|merciful]]_ _[[items/Weapon Magic Abilities/Vicious|vicious]]_ _[[items/Weapon/Whip|whip]]_ arms +13 (1d8+4 plus _[[universal monster rules/Grab|grab]]_)
**Space** 10 ft., **Reach** 10 ft. (20 ft. with _whip_ arms)
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (1d8+4), damning scourge, dead tired, enslave (DC 18)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +13)
Constant—_[[spells/Deathwatch|deathwatch]]_
At Will—greater teleport (self plus 50 lbs. only)
3/day—_[[spells/Heroism|heroism]]_, _[[spells/Waves of Fatigue|waves of fatigue]]_ (DC 18)
1/day—_[[spells/Temporary Resurrection|temporary resurrection]]_

##### Statistics
**Str** 17, **Dex** 13, **Con** 19, **Int** 14, **Wis** 14, **Cha** 16
**Base Atk** +10; **CMB** +14 (+16 disarm, +16 _[[universal monster rules/Trip|trip]]_, +18 grapple); **CMD** 25 (27 vs. disarm, 27 vs. _trip_)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Trip|Improved Trip]]_
**Skills** Acrobatics +12, Bluff +16, Diplomacy +14, _[[spells/Heal|Heal]]_ +13, Intimidate +16, Knowledge (planes) +11, Perception +15, Sense Motive +15, Stealth +10
**Languages** Abyssal, Common, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary, pair, or corps (3–5)
**Treasure** standard

### Special Abilities

**Damning Scourge (Su)** Each of a nixudaemon’s upper arms functions as a Large +1 _deadly_ _merciful_ _vicious_ _whip_. Attacks with these whips count as _[[universal monster rules/Natural Attacks|natural attacks]]_ for the nixudaemon, have a reach of 20 feet, and don’t provoke attacks of opportunity. The whips can’t be disarmed or sundered, nor can they be dropped to allow the nixudaemon to avoid being tripped because of failing a combat maneuver check to _trip_. The nixudaemon decides before each attack roll whether to apply the weapon’s _merciful_ special ability, its _vicious_ special ability, both, or neither.

**Dead Tired (Su)** A nixudaemon’s attacks drain every bit of vitality from its victims when they die. Raising a creature killed by a nixudaemon (via _[[spells/Raise Dead|raise dead]]_ or another effect that restores life) requires a successful DC 20 caster level check. The restored creature gains the _[[conditions/Exhausted|exhausted]]_ condition, regardless of the spell used to raise it. The DC of this caster level check is Charisma-based, and includes a +2 racial bonus. A nixudaemon can use its _temporary resurrection_ spell-like ability without attempting this check, even if another nixudaemon killed the subject.

**Enslave (Su)** If a nixudaemon successfully uses its _grab_ ability to grapple a foe with its _whip_ attack, its tendril wraps around the victim’s throat. The daemon can forgo its _constrict_ damage and instead attempt to dominate the subject, as the spell _[[spells/Dominate Monster|dominate monster]]_ (Will DC 18 negates). A creature dominated by a nixudaemon is immune to fatigue, exhaustion, and pain effects. At the beginning of its turn, a dominated slave automatically receives a new saving throw to end the effect. The nixudaemon can dominate only one creature at a time per _whip_ arm it possesses (typically two). The save DC for this ability is Charisma-based.

##### Description

Nixudaemons, or “toil daemons,” epitomize death by exploitation and extreme exertion. These fiends savor the moment when a desperate _[[feats/Scholar|scholar]]_ collapses while putting in long, unappreciated hours, or when a galley _slave_ finally succumbs to the lash. They drive burdened subjects before them to great effect, even resurrecting _[[monsters/Fallen|fallen]]_ servants for a brief time to complete vital tasks. Their skill for squeezing the last bit of energy from those under their supervision makes them invaluable to slavers, who pay the daemons in coin, information, and souls for their aid.

Nixudaemons exemplify the _[[feats/Cruelty|cruelty]]_ and disdain all daemonkind display toward the living. They lash out at their subjects, whipping the life out of them slowly. If it serves the daemon’s purposes, or if time allows for another game of torture, a nixudaemon will revive its subject for another day. Typically, a nixudaemon uses this ability to incite a band of slaves to work harder; it dominates the weakest members of the workers to temporarily bolster them, then saps their last ounce of strength before discarding them as spent husks.

Most nixudaemons stand 10 feet tall and weigh 600 pounds. Sages report that the fiends grow larger and stronger as they age, absorbing the weariness of their victims over centuries. The greatest toil daemons are said to tower over their younger cousins, _[[items/Weapon Magic Abilities/Growing|growing]]_ additional whip-arms and learning powerful spells that exhaust or even kill those who dare offend them.
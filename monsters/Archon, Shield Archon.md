---
cssclass: [monsters]
title1: Archon, Shield Archon
desc_short: 'This armored giant is sheathed in metal from head to toe. One arm ends
  in a spear-like blade, the other in a massive shield. '
title2: Shield Archon
CR: 10
sources:
- name: Bestiary 2
  page: 31
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 9600
alignment: LG
size: Large
type: outsider
subtypes:
- archon
- extraplanar
- good
- lawful
initiative:
  bonus: 5
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: aura of menace
  DC: 18
- name: magic circle against evil
AC:
  AC: 29
  touch: 10
  flat_footed: 28
  other: +2 deflection vs. evil
  components:
    armor: 9
    dex: 1
    natural: 4
    shield: 6
    size: -1
HP:
  HP: 112
  long: 9d10+63
saves:
  fort: 13
  ref: 7
  will: 8
  other: +4 vs. poison
DR:
- amount: 10
  weakness: evil
immunities:
- electricity
- petrification
SR: 21
speeds:
  base: 40
  other_semicolon: 30 ft., fly 60 ft. in armor
  fly: 90
  fly_maneuverability: good
attacks:
  melee:
  - - text: +3 shortspear +16/+11 (1d8+10)
      entries:
      - - damage: 1d8+10
      attack: +3 shortspear
      bonus:
      - 16
      - 11
  special:
  - transpose ally
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: magic circle against evil
    source: default
    freq: Constant
  - name: aid
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: message
    source: default
    freq: At will
  - name: disrupting weapon
    source: default
    freq: 1/day
  - name: divine power
    source: default
    freq: 1/day
  - name: shield other
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 9
    concentration: 11
ability_scores:
  STR: 20
  DEX: 13
  CON: 25
  INT: 14
  WIS: 16
  CHA: 15
BAB: 9
CMB: 15
CMD: 26
CMD_other: 30 vs. bull rush and trip
feats:
- name: Combat Reflexes
- name: Improved Initiative
- name: Iron Will
- name: Shield Focus
- name: Stand Still
- is_bonus: true
  name: Weapon Specialization (shortspear)
skills:
  Diplomacy: 14
  Fly: 0
  Intimidate: 14
  Knowledge (religion): 14
  Perception: 15
  Sense Motive: 15
  Stealth: -6
  Survival: 15
languages:
- Celestial
- Draconic
- Infernal
- truespeech
special_qualities:
- spear and shield
- stability
ecology:
  environment: any (Heaven)
  organization: solitary, pair, or squad (3-5)
  treasure_type: standard
  treasure:
  - full plate
  - other treasure
special_abilities:
  Spear and Shield (Su): At will as a free action, a shield archon can transform his
    hands into a +1 tower shield and a +3 shortspear, or either individually, or back
    to hands again. He cannot transform both hands into shields or both into shortspears.
    A shield archon never takes the typical -2 penalty on attack rolls while wielding
    a tower shield. A shield archon's weapons cannot be disarmed, but they can be
    sundered. If a shield archon loses his spear or shield, he can manifest a new
    one as a full-round action. When a shield archon is slain, these two items fade
    away-they cannot be looted or wielded by any other creature.
  Stability (Ex): Shield archons receive a +4 racial bonus to CMD when resisting a
    bull rush or trip attempt.
  Transpose Ally (Su): Once per day as a standard action, a shield archon can teleport
    to the location of a willing (or unconscious) ally and immediately teleport that
    ally to the archon's previous position, in effect switching places with the ally.
    The archon must have line of effect to the target.
desc_long: Shield archons are the mighty rocks of celestial armies, withstanding waves
  of demons and devils without complaint. Though more than capable of tearing apart
  lesser demons and devils, their true strength lies in their ability to shrug off
  deadly attacks from superior opponents, giving their offense-oriented allies time
  to flank and overwhelm their mutual foes. Shield archons are 9 feet tall and weigh
  800 pounds.

---

# Archon, Shield Archon
This armored giant is sheathed in metal from head to toe. One arm ends in a spear-like blade, the other in a massive _[[spells/Shield|shield]]_.

**Source** Bestiary 2 pg. 31
**XP** 9,600

LG Large outsider (archon, extraplanar, good, lawful)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +15
**Aura** aura of menace (DC 18), _[[spells/Magic Circle against Evil|magic circle against evil]]_

##### Defense

**AC** 29, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+9 armor, +1 Dex, +4 natural, +6 _shield_, –1 size) (+2 deflection vs. evil)
**hp** 112 (9d10+63)
**Fort** +13, **Ref** +7, **Will** +8; +4 vs. poison
**DR** 10/evil; **Immune** electricity, petrification; **SR** 21

##### Offense
**Speed** 40 ft., fly 90 ft. (good); 30 ft., fly 60 ft. in armor
**Melee** +3 _[[items/Weapon/Shortspear|shortspear]]_ +16/+11 (1d8+10)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** transpose ally
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +11)
Constant—_magic circle against evil_
At will—aid, greater teleport (self plus 50 lbs. of objects only), _[[spells/Message|message]]_
1/day—_[[spells/Disrupting Weapon|disrupting weapon]]_, _[[spells/Divine Power|divine power]]_, _[[spells/Shield Other|shield other]]_

##### Statistics
**Str** 20, **Dex** 13, **Con** 25, **Int** 14, **Wis** 16, **Cha** 15
**Base Atk** +9; **CMB** +15; **CMD** 26 (30 vs. bull rush and _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Shield Focus|Shield Focus]]_, _[[feats/Stand Still|Stand Still]]_, _[[feats/Weapon Specialization|Weapon Specialization]]_ (_shortspear_)
**Skills** Diplomacy +14, Fly +0, Intimidate +14, Knowledge (religion) +14, Perception +15, Sense Motive +15, Stealth -6, Survival +15
**Languages** Celestial, Draconic, Infernal; truespeech
**SQ** _[[items/Weapon/Spear|spear]]_ and _shield_, stability

##### Ecology

**Environment** any (Heaven)
**Organization** solitary, pair, or squad (3–5)
**Treasure** standard (_[[items/Armor/Full plate|full plate]]_, other treasure)

### Special Abilities
**_Spear_ and _Shield_ (Su)** At will as a free action, a _shield_ archon can transform his hands into a +1 _[[items/Shield/Tower shield|tower shield]]_ and a +3 _shortspear_, or either individually, or back to hands again. He cannot transform both hands into shields or both into shortspears. A _shield_ archon never takes the typical –2 penalty on attack rolls while wielding a _tower shield_. A _shield_ archon’s weapons cannot be disarmed, but they can be sundered. If a _shield_ archon loses his _spear_ or _shield_, he can manifest a new one as a full-round action. When a _shield_ archon is slain, these two items fade away—they cannot be looted or wielded by any other creature.
**Stability (Ex)** _Shield_ archons receive a +4 racial bonus to CMD when resisting a bull rush or _trip_ attempt.

**Transpose Ally (Su)** Once per day as a standard action, a _shield_ archon can teleport to the location of a willing (or _[[conditions/Unconscious|unconscious]]_) ally and immediately teleport that ally to the archon’s previous position, in effect switching places with the ally. The archon must have line of effect to the target.

##### Description

_Shield_ archons are the mighty rocks of celestial armies, _[[items/Armor Magic Abilities/Withstanding|withstanding]]_ waves of demons and devils without complaint. Though more than capable of tearing apart lesser demons and devils, their true strength lies in their ability to shrug off _[[items/Weapon Magic Abilities/Deadly|deadly]]_ attacks from superior opponents, giving their offense-oriented allies time to flank and _[[feats/Overwhelm|overwhelm]]_ their mutual foes. _Shield_ archons are 9 feet tall and weigh 800 pounds.
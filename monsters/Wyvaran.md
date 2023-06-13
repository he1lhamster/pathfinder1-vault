---
cssclass: [monsters]
title1: Wyvaran
desc_short: This dragonlike humanoid brandishes its spear, spreads its wings, and
  shows its fangs in a angry snarl.
title2: Wyvaran
CR: 1/2
sources:
- name: Bestiary 4
  page: 281
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 200
race: Female
classes:
- wyvaran inquisitor 1
alignment: LN
size: Medium
type: dragon
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 17
  touch: 12
  flat_footed: 15
  components:
    armor: 5
    dex: 2
HP:
  HP: 10
  long: 1d8+2
saves:
  fort: 3
  ref: 2
  will: 5
immunities:
- paralysis
- sleep
speeds:
  base: 30
  fly: 30
  fly_other: clumsy) (20 ft., fly 20 ft. [clumsy] in armor
attacks:
  melee:
  - - text: shortspear +1 (1d6)
      entries:
      - - damage: 1d6
      attack: shortspear
      bonus:
      - 1
  - - text: slapping tail +0 (1d8; attacks of opportunity only)
      entries:
      - - damage: 1d8
        - effect: attacks of opportunity only
      attack: slapping tail
      bonus:
      - 0
spell_like_abilities:
  entries:
  - name: lightning arc
    source: default
    freq: 6/day
    other: 1d6 electricity
  sources:
  - name: default
    CL: 1
    concentration: 3
spells:
  entries:
  - name: cause fear
    source: Inquisitor
    level: 1
    DC: 15
  - name: shield of faith
    source: Inquisitor
    level: 1
  - name: acid splash
    source: Inquisitor
    level: 0
  - name: daze
    source: Inquisitor
    level: 0
    DC: 14
  - name: disrupt undead
    source: Inquisitor
    level: 0
  - name: guidance
    source: Inquisitor
    level: 0
  sources:
  - name: Inquisitor
    type: known
    CL: 1
    concentration: 3
    slots:
      1: 2
      0: at-will
    domains:
    - air
ability_scores:
  STR: 10
  DEX: 14
  CON: 13
  INT: 6
  WIS: 17
  CHA: 14
BAB: 0
CMB: 0
CMD: 12
feats:
- name: Weapon Focus (shortspear)
skills:
  Fly: -6
  Intimidate: 6
  Knowledge (religion): 2
  Perception: 7
languages:
- Common
- Draconic
special_qualities:
- judgment 1/day
- monster lore +3
- stern gaze
ecology:
  environment: temperate mountains
  organization: solitary, wing (2-8), or flight (4-12)
  treasure_type: NPC Gear
  treasure:
  - spear
  - scale mail
  - holy symbol
  - other treasure
desc_long: |-
  These creatures are the result of magical draconic experiments at crossbreeding wyverns and kobolds. Wyvarans are fiercely territorial creatures loyal to their kin and tribe, and allow no interlopers into their lands without good reason or proper tribute. Each defends its personal property, and seeks revenge on any who dare steal from it. Most evil and neutral wyvarans primarily concern themselves with expanding their territory and wealth.

  Many civilized races dismiss wyvarans as fast, dumb, selfish brutes. However, a creature who respects the wyvarans' rules about their property finds that they make steadfast and loyal allies. Adventuring wyvarans often view their companions as clutchmates, and are willing to take great risks to protect them.

---

# Wyvaran
This dragonlike humanoid brandishes its _[[items/Weapon/Spear|spear]]_, spreads its wings, and shows its fangs in a angry snarl.
**Source** Bestiary 4 pg. 281
**XP** 200
Female _[[monsters/Wyvaran|wyvaran]]_ _[[classes/Inquisitor|inquisitor]]_ 1

LN Medium dragon
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +7

##### Defense

**AC** 17, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+5 armor, +2 Dex)
**hp** 10 (1d8+2)
**Fort** +3, **Ref** +2, **Will** +5
**Immune** _[[universal monster rules/Paralysis|paralysis]]_, sleep

##### Offense
**Speed** 30 ft., fly 30 ft. (clumsy) (20 ft., fly 20 ft. [clumsy] in armor)
**Melee** _[[items/Weapon/Shortspear|shortspear]]_ +1 (1d6) or slapping tail +0 (1d8; attacks of opportunity only)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 1st; concentration +3)
6/day—_[[spells/Lightning Arc|lightning arc]]_ (1d6 electricity)
**_Inquisitor_ Spells Known **(CL 1st; concentration +3)
1st (2/day)—_[[spells/Cause Fear|cause fear]]_ (DC 15), _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Daze|daze]]_ (DC 14), _[[spells/Disrupt Undead|disrupt undead]]_, _[[spells/Guidance|guidance]]_
**Domain** Air

##### Statistics
**Str** 10, **Dex** 14, **Con** 13, **Int** 6, **Wis** 17, **Cha** 14
**Base Atk** +0; **CMB** +0; **CMD** 12
**Feats** _[[feats/Weapon Focus|Weapon Focus]]_ (_shortspear_)
**Skills** Fly –6, Intimidate +6, Knowledge (religion) +2, Perception +7
**Languages** Common, Draconic
**SQ** judgment 1/day, monster lore +3, stern _[[universal monster rules/Gaze|gaze]]_

##### Ecology

**Environment** temperate mountains
**Organization** solitary, wing (2–8), or _[[universal monster rules/Flight|flight]]_ (4–12)
**Treasure** NPC gear (_spear_, _[[items/Armor/Scale mail|scale mail]]_, holy symbol, other treasure)

##### Description

These creatures are the result of magical draconic experiments at crossbreeding wyverns and kobolds. Wyvarans are fiercely territorial creatures loyal to their kin and tribe, and allow no interlopers into their lands without good reason or proper tribute. Each defends its personal property, and seeks revenge on any who dare steal from it. Most evil and neutral wyvarans primarily concern themselves with expanding their territory and wealth.

Many civilized races dismiss wyvarans as fast, dumb, selfish brutes. However, a creature who respects the wyvarans’ rules about their property finds that they make steadfast and loyal allies. Adventuring wyvarans often view their companions as clutchmates, and are willing to take great risks to protect them.
---
cssclass: [monsters]
title1: Temple (Acolyte)
title2: Temple (Acolyte)
CR: 1/2
sources:
- name: GameMastery Guide
  page: 304
  link: http://paizo.com/pathfinderRPG/v5748btpy8ffn
XP: 200
race: Human
classes:
- cleric 1
alignment: LN
size: Medium
type: humanoid
initiative:
  bonus: 0
AC:
  AC: 17
  touch: 10
  flat_footed: 17
  components:
    armor: 5
    shield: 2
HP:
  HP: 5
  long: 1d8+1
saves:
  fort: 3
  ref: 0
  will: 4
speeds:
  base: 20
attacks:
  melee:
  - - text: shortspear +1 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: shortspear
      bonus:
      - 1
  ranged:
  - - text: shortspear +0 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: shortspear
      bonus:
      - 0
  special:
  - channel positive energy 7/day (DC 12, 1d6)
spell_like_abilities:
  entries:
  - name: rebuke death
    source: default
    freq: 5/day
  - name: touch of law
    source: default
    freq: 5/day
  sources:
  - name: default
    CL: 1
    concentration: 3
spells:
  entries:
  - name: bless
    source: Cleric
    level: 1
  - name: command
    source: Cleric
    level: 1
    DC: 13
  - is_domain_spell: true
    name: cure light wounds
    source: Cleric
    level: 1
  - name: guidance
    source: Cleric
    level: 0
  - name: resistance
    source: Cleric
    level: 0
  - name: virtue
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 1
    concentration: 3
    slots:
      0: at-will
    domains:
    - healing
    - law
ability_scores:
  STR: 12
  DEX: 10
  CON: 13
  INT: 10
  WIS: 15
  CHA: 14
BAB: 0
CMB: 1
CMD: 11
feats:
- name: Extra Channel
- name: Selective Channeling
skills:
  Diplomacy: 6
  Heal: 8
  Knowledge (religion): 4
  Sense Motive: 6
  Perception: 2
languages:
- Common
gear:
  combat:
  - scroll of protection from chaos
  - scroll of sanctuary
  other:
  - scale mail
  - heavy wooden shield
  - shortspears (2)
  - healer's kit
  - silver holy symbol
npc_boon: An acolyte can tend a character's wounds or provide a free wooden holy symbol
  or sacred tract (granting a +2 circumstance bonus on Knowledge [religion] checks
  about the acolyte's faith). An acolyte can also make holy water for PCs at a 20%
  discount.
desc_long: |-
  An acolyte is a priest in training, often a callow youth fresh from the cloisters, loaded with zeal but not much practiced in proselytism. They are found in temples and monasteries throughout the world, and their enthusiasm and devotion makes them eager to take up arms and armor to defend their faith and flocks.

  Acolytes of different faiths can be easily created by simply changing their domains, spells, armor, or weapons. Evil acolytes might have the Death and Evil domains, for example, and channel negative energy instead. An acolyte of nature could have the Animal and Plant domains, and wear leather armor.

  Acolytes can be temple caretakers or messengers, attendants at small roadside shrines and chapels, or assistants to more experienced priests. A pair of acolytes may accompany a temple guard (CR 3), a pilgrim (CR 4), or a medium (CR 5).

---

# Temple (Acolyte)

**Source** GameMastery Guide pg. 304
**XP** 200
Human _[[classes/Cleric|cleric]]_ 1

LN Medium humanoid
**Init** +0; **Senses** Perception +2

##### Defense

**AC** 17, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+5 armor, +2 _[[spells/Shield|shield]]_)
**hp** 5 (1d8+1)
**Fort** +3, **Ref** +0, **Will** +4

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Shortspear|shortspear]]_ +1 (1d6+1)
**Ranged** _shortspear_ +0 (1d6+1)
**Special Attacks** channel positive energy 7/day (DC 12, 1d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 1st; concentration +3)
5/day—_[[spells/Rebuke|rebuke]]_ death, touch of law
**_Cleric_ Spells Prepared **(CL 1st; concentration +3)
1st—_[[spells/Bless|bless]]_, _[[spells/Command|command]]_ (DC 13), _[[spells/Cure Light Wounds|cure light wounds]]_
0 (at will)—_[[spells/Guidance|guidance]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Virtue|virtue]]_
**D** domain spell; **Domains** Healing, Law

##### Statistics
**Str** 12, **Dex** 10, **Con** 13, **Int** 10, **Wis** 15, **Cha** 14
**Base Atk** +0; **CMB** +1; **CMD** 11
**Feats** _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Selective Channeling|Selective Channeling]]_
**Skills** Diplomacy +6, _[[spells/Heal|Heal]]_ +8, Knowledge (religion) +4, Sense Motive +6
**Languages** Common
**Combat Gear** scroll of _[[spells/Protection From Chaos|protection from chaos]]_, scroll of _[[spells/Sanctuary|sanctuary]]_; **Other Gear** _[[items/Armor/Scale mail|scale mail]]_, _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, shortspears (2), _[[npcs/Healer|healer]]_’s kit, silver holy symbol

**Boon** An _[[npcs/Acolyte|acolyte]]_ can tend a character’s wounds or provide a free wooden holy symbol or _[[items/Weapon Magic Abilities/Sacred|sacred]]_ tract (granting a +2 circumstance bonus on Knowledge [religion] checks about the _acolyte_’s faith). An _acolyte_ can also make _[[items/Mundane/Holy water|holy water]]_ for PCs at a 20% discount.

An _acolyte_ is a priest in _[[items/Weapon Magic Abilities/Training|training]]_, often a callow youth fresh from the cloisters, loaded with zeal but not much practiced in proselytism. They are found in temples and monasteries throughout the world, and their enthusiasm and devotion makes them eager to take up arms and armor to defend their faith and flocks.

Acolytes of different faiths can be easily created by simply changing their domains, spells, armor, or weapons. Evil acolytes might have the Death and Evil domains, for example, and channel negative energy instead. An _acolyte_ of nature could have the Animal and Plant domains, and wear _[[items/Armor/Leather armor|leather armor]]_.

Acolytes can be temple caretakers or messengers, attendants at small roadside shrines and chapels, or assistants to more experienced priests. A pair of acolytes may accompany a temple _[[npcs/Guard|guard]]_ (CR 3), a pilgrim (CR 4), or a _medium_ (CR 5).
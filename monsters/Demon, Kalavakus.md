---
cssclass: [monsters]
title1: Demon, Kalavakus
desc_short: 'This muscular, violet demon walks upon elephantine feet. Large, razor-sharp
  horns cover its body. '
title2: Kalavakus
CR: 10
sources:
- name: Bestiary 2
  page: 78
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 9600
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 1
senses:
  darkvision: 60
AC:
  AC: 25
  touch: 11
  flat_footed: 24
  components:
    dex: 1
    natural: 14
HP:
  HP: 125
  long: 10d10+70
saves:
  fort: 10
  ref: 8
  will: 10
DR:
- amount: 10
  weakness: good
immunities:
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 21
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +16 (1d6+6)
      entries:
      - - damage: 1d6+6
      attack: bite
      bonus:
      - 16
    - text: 2 claws +16 (1d8+6)
      entries:
      - - damage: 1d8+6
      count: 2
      attack: claws
      bonus:
      - 16
    - text: gore +16 (2d6+6)
      entries:
      - - damage: 2d6+6
      attack: gore
      bonus:
      - 16
  special:
  - enslave soul
  - horns
  - powerful charge (gore, 4d6+12)
spell_like_abilities:
  entries:
  - name: command
    source: default
    freq: At will
    DC: 14
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: telekinesis
    source: default
    freq: At will
    DC: 18
  - name: air walk
    source: default
    freq: 3/day
  - name: dominate person
    source: default
    freq: 3/day
    DC: 18
  - name: haste
    source: default
    freq: 3/day
  - name: greater command
    source: default
    freq: 1/day
    DC: 18
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: kalavakus
      amount: 1
      chance: 40%
  - name: symbol of persuasion
    source: default
    freq: 1/day
    DC: 19
  sources:
  - name: default
    CL: 12
    concentration: 15
ability_scores:
  STR: 22
  DEX: 13
  CON: 24
  INT: 15
  WIS: 17
  CHA: 16
BAB: 10
CMB: 16
CMB_other: +22 disarm
CMD: 27
feats:
- name: Combat Expertise
- name: Improved Bull Rush
- name: Improved Disarm
- name: Improved Trip
- name: Power Attack
skills:
  Acrobatics: 14
  Climb: 19
  Intimidate: 16
  Knowledge (planes): 15
  Perception: 24
  Sense Motive: 16
  Stealth: 14
  Use Magic Device: 16
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Common
- Draconic
- telepathy 100 ft.
ecology:
  environment: any (the Abyss)
  organization: solitary, pair, or slaver gang (3-6 kalavakuses plus 10-20 slaves)
  treasure_type: standard
special_abilities:
  Enslave Soul (Su): A kalavakus can attempt to enslave the soul of any mortal creature
    within 60 feet as a swift action. The kalavakus must have line of sight to the
    target. The target can resist this special attack with a DC 18 Will save, but
    is staggered for 1 round even if the save is successful. If the save is successful,
    the creature is immune to this ability for 24 hours. If the save is a failure,
    the target's soul is enslaved-this creature takes a -6 penalty on all attack rolls
    and saving throws against that kalavakus. If a creature with an enslaved soul
    is slain by that kalavakus, the soul immediately infuses the demon's body, affecting
    it with a heal spell (CL 12th). A kalavakus can have only one mortal soul enslaved
    at a time-if it enslaves a second soul, the first is released. This is a mind-affecting
    death effect. The save DC is Charisma-based.
  Horns (Ex): The kalavakus's numerous horns can easily catch weapons and yank them
    away from opponents. The demon gains a +4 racial bonus on all disarm attempts
    as a result.
desc_long: |-
  Known to some as “horned demons,” the kalavakus demons are hulking, muscled beasts. They work as slavers on the Abyss, sometimes as harem keepers or captains of the guard for a more powerful demon, and at other times as mercenaries who sell their captured victims for profit to anyone with the funds to pay. 

  A kalavakus is 7 feet tall and weighs 450 pounds. They form from the souls of evil mortals who were slavers in their mortal lives.

---

# Demon, Kalavakus
This muscular, violet demon walks upon elephantine feet. Large, razor-sharp horns cover its body.

**Source** Bestiary 2 pg. 78
**XP** 9,600
CE Medium outsider (chaotic, demon, evil, extraplanar)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +24

##### Defense

**AC** 25, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+1 Dex, +14 natural)
**hp** 125 (10d10+70)
**Fort** +10, **Ref** +8, **Will** +10
**DR** 10/good; **Immune** electricity, poison; **Resist** acid 10, cold 10, fire 10; **SR** 21

##### Offense
**Speed** 30 ft.
**Melee** bite +16 (1d6+6), 2 claws +16 (1d8+6), gore +16 (2d6+6)
**Special Attacks** enslave soul, horns, _[[universal monster rules/Powerful Charge|powerful charge]]_ (gore, 4d6+12)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +15)
At will—_[[spells/Command|command]]_ (DC 14), greater teleport (self plus 50 lbs. of objects only), _[[spells/Telekinesis|telekinesis]]_ (DC 18)
3/day—_[[spells/Air Walk|air walk]]_, _[[spells/Dominate Person|dominate person]]_ (DC 18), _[[spells/Haste|haste]]_
1/day—greater _command_ (DC 18), _[[universal monster rules/Summon|summon]]_ (level 4, 1 kalavakus 40%), _[[spells/Symbol of Persuasion|symbol of persuasion]]_ (DC 19)

##### Statistics
**Str** 22, **Dex** 13, **Con** 24, **Int** 15, **Wis** 17, **Cha** 16
**Base Atk** +10; **CMB** +16 (+22 disarm); **CMD** 27
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Acrobatics +14, _[[universal monster rules/Climb|Climb]]_ +19, Intimidate +16, Knowledge (planes) +15, Perception +24, Sense Motive +16, Stealth +14, Use Magic Device +16; **Racial Modifiers** +8 Perception
**Languages** Abyssal, Celestial, Common, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (the Abyss)
**Organization** solitary, pair, or slaver gang (3–6 kalavakuses plus 10–20 slaves)
**Treasure** standard

### Special Abilities

**Enslave Soul (Su)** A kalavakus can attempt to enslave the soul of any mortal creature within 60 feet as a swift action. The kalavakus must have line of sight to the target. The target can resist this special attack with a DC 18 Will save, but is _[[conditions/Staggered|staggered]]_ for 1 round even if the save is successful. If the save is successful, the creature is immune to this ability for 24 hours. If the save is a failure, the target’s soul is enslaved—this creature takes a –6 penalty on all attack rolls and saving throws against that kalavakus. If a creature with an enslaved soul is slain by that kalavakus, the soul immediately infuses the demon’s body, affecting it with a _[[spells/Heal|heal]]_ spell (CL 12th). A kalavakus can have only one mortal soul enslaved at a time—if it enslaves a second soul, the first is released. This is a mind-affecting death effect. The save DC is Charisma-based.

**Horns (Ex)** The kalavakus’s numerous horns can easily catch weapons and yank them away from opponents. The demon gains a +4 racial bonus on all disarm attempts as a result.

##### Description

Known to some as “horned demons,” the kalavakus demons are hulking, muscled beasts. They work as slavers on the Abyss, sometimes as harem keepers or captains of the _[[npcs/Guard|guard]]_ for a more powerful demon, and at other times as mercenaries who sell their captured victims for profit to anyone with the funds to pay.

A kalavakus is 7 feet tall and weighs 450 pounds. They form from the souls of evil mortals who were slavers in their mortal lives.
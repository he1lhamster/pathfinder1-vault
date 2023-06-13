---
cssclass: [monsters]
title1: Div, Druj Nasu
desc_short: A sickly smell of feral musk, rotting flesh, and acrid sweat surrounds
  this fly-like creature. Its wings fill the air with a dreadful drone even when the
  creature is still.
title2: Druj Nasu
CR: 8
sources:
- name: 'Pathfinder #113: What Grows Within'
  page: 84
  link: http://paizo.com/products/btpy9qcl?Pathfinder-Adventure-Path-113-What-Grows-Within
XP: 4800
alignment: NE
size: Medium
type: outsider
subtypes:
- div
- evil
- extraplanar
initiative:
  bonus: 10
senses:
  darkvision: 60
  see in darkness: true
  detect good: true
  detect magic: true
AC:
  AC: 24
  touch: 16
  flat_footed: 18
  components:
    dex: 6
    natural: 8
HP:
  HP: 105
  long: 10d10+50
saves:
  fort: 8
  ref: 13
  will: 11
DR:
- amount: 10
  weakness: cold iron and good
immunities:
- fire
- poison
resistances:
  acid: 10
  electricity: 10
SR: 19
speeds:
  base: 30
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: bite +16 (1d6+4 plus disease)
      entries:
      - - damage: 1d6+4
        - effect: disease
      attack: bite
      bonus:
      - 16
    - text: 2 claws +16 (1d4+4 plus distraction)
      entries:
      - - damage: 1d4+4
        - effect: distraction
      count: 2
      attack: claws
      bonus:
      - 16
  special:
  - disease
  - distraction (DC 20)
  - droning
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: invisibility
    source: default
    freq: At will
    other: self only
  - name: putrefy food and drink
    source: default
    freq: At will
  - name: see invisibility
    source: default
    freq: At will
  - name: summon swarm
    source: default
    freq: At will
  - name: bestow curse
    source: default
    freq: 3/day
    DC: 20
  - name: command undead
    source: default
    freq: 3/day
    DC: 18
  - name: enervation
    source: default
    freq: 3/day
  - name: animate dead
    source: default
    freq: 1/day
  - name: insect plague
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 6
    summons:
    - name: pairaka [Pathfinder RPG Bestiary 3 88]
      amount: 1
    - name: fiendish giant flies [Pathfinder RPG Bestiary 2 292, 124]
      amount: 1d6
      chance: 50%
  sources:
  - name: default
    CL: 10
    concentration: 16
ability_scores:
  STR: 18
  DEX: 23
  CON: 20
  INT: 12
  WIS: 19
  CHA: 23
BAB: 10
CMB: 14
CMD: 30
feats:
- name: Alertness
- name: Flyby Attack
- name: Hover
- name: Improved Initiative
- name: Weapon Finesse
skills:
  Acrobatics: 19
  Bluff: 19
  Fly: 22
  Knowledge (arcana): 9
  Knowledge (dungeoneering): 9
  Knowledge (planes): 9
  Knowledge (religion): 9
  Perception: 21
  Sense Motive: 14
  Stealth: 19
languages:
- Abyssal
- Celestial
- Infernal
- telepathy 100 ft.
special_qualities:
- swarmwalking
- untouched by flame
ecology:
  environment: any (Abaddon)
  organization: solitary
  treasure_type: standard
special_abilities:
  Disease (Su): Bite or claw-injury; save Fortitude DC 20; onset 1 hour; frequency
    1 day; effect 1d3 Constitution damage plus sickened and shaken; cure 2 consecutive
    saves.
  Droning (Su): As a standard action, a druj nasu can beat its wings in such a way
    that the sound they make resembles the droning of millions of buzzing flies. This
    sonic effect extends out to a 30-foot radius, though a creature can still hear
    the cacophony from a distance without being affected. Creatures in the area take
    a -4 penalty on Perception checks involving hearing, and all creatures in the
    area have a 25% chance each round of being nauseated for 1 round. Any creature
    subject to the nauseating effect of this ability can negate the nausea with a
    successful DC 20 Fortitude saving throw. In addition, any creature casting a spell
    in the area must succeed at a concentration check (DC = 15 + the level of the
    spell being cast) or lose the spell. After initiating this effect, a druj nasu
    can maintain the effect each round as a free action and can dismiss it as a move
    action.
  Swarmwalking (Su): A druj nasu is immune to damage or distraction effects caused
    by swarms.
  Untouched By Flame (Su): Any undead animated by a druj nasu or any swarm summoned
    by this div gains the druj nasu's immunity to fire.
desc_long: |-
  Foul corruptors of the dead, druj nasus are divs that haunt funeral pyres, mausoleums, and burial sites to steal corpses. They represent the uncleanness of the body and corrupting forces that can prevent a creature's proper passage into the afterlife. Some scholars claim that in ancient times these creatures' interference caused numerous cultures to alter their practices regarding burial.

  When a druj nasu was found near a body that was to be buried, the body would be considered unclean. An unclean body couldn't be buried and the sacred flames of a funeral pyre would only spread the taint to the winds, so some ancient people would then carry the corpse up the side of a cliff or mountain and have the birds and other animals clean the flesh from the bones before the deceased could be interred with the necessary rites to ensure a proper passage into the Great Beyond.

  Unlike other corpse thieves, druj nasus don't take the bodies of the deceased in order to feast upon the rotting flesh. The divs do this to spite the survivors and bring greater grief and sorrow to the family and loved ones of the dead. After pilfering the bodies, the divs watch from afar as the grieving family sinks deeper into sadness. They then animate the stolen remains and, since they have no innate ability to influence these creations, use their command undead spell-like ability to send the shambling corpse back to prey upon its former loved ones. In this way, druj nasus disrupt polite society and commit one of the ultimate cultural taboos.

  Because druj nasus, like all divs, are a scourge on humanity's accomplishments, these foul fiends are a constant target of good faiths. They are particularly hated by followers of Pharasma because of their treatment of corpses and proclivity for animating the remains they steal. Druj nasus generally ignore Pharasmins, however, and instead focus on their own mockery of the living. Because of an unknown, ancient conflict in Kelesh, druj nasus have a strong hatred for Sarenrae and her worshipers, going so far as to single them out in combat and steal away the bodies of the clergy and faithful. Sarenrae's devoted find combating these divs frustrating due to their immunity to fire.

  A druj nasu stands roughly 6 feet tall and weighs a slight 100 pounds.

---

# Div, Druj Nasu
A sickly smell of feral musk, rotting flesh, and acrid sweat surrounds this fly-like creature. Its wings fill the air with a dreadful drone even when the creature is still.
**Source** Pathfinder #113: _[[spells/What Grows Within|What Grows Within]]_ pg. 84
**XP** 4,800

NE Medium outsider (div, evil, extraplanar)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/Detect Good|detect good]]_, _[[spells/Detect Magic|detect magic]]_; Perception +21

##### Defense

**AC** 24, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+6 Dex, +8 natural)
**hp** 105 (10d10+50)
**Fort** +8, **Ref** +13, **Will** +11
**DR** 10/cold iron and good; **Immune** fire, poison; **Resist** acid 10, electricity 10; **SR** 19

##### Offense
**Speed** 30 ft., fly 60 ft. (perfect)
**Melee** bite +16 (1d6+4 plus disease), 2 claws +16 (1d4+4 plus _[[universal monster rules/Distraction|distraction]]_)
**Special Attacks** disease, _distraction_ (DC 20), droning
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +16)
Constant—_detect good_, _detect magic_
At will—_[[spells/Invisibility|invisibility]]_ (self only), _[[spells/Putrefy Food and Drink|putrefy food and drink]]_, _[[spells/See Invisibility|see invisibility]]_, _[[spells/Summon Swarm|summon swarm]]_
3/day—_[[spells/Bestow Curse|bestow curse]]_ (DC 20), _[[spells/Command Undead|command undead]]_ (DC 18), _[[spells/Enervation|enervation]]_
1/day—_[[spells/Animate Dead|animate dead]]_, _[[spells/Insect Plague|insect plague]]_, _[[universal monster rules/Summon|summon]]_ (level 6, 1 pairaka [Pathfinder RPG Bestiary 3 88] or 1d6 fiendish giant flies [Pathfinder RPG Bestiary 2 292, 124] 50%)

##### Statistics
**Str** 18, **Dex** 23, **Con** 20, **Int** 12, **Wis** 19, **Cha** 23
**Base Atk** +10; **CMB** +14; **CMD** 30
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +19, Bluff +19, Fly +22, Knowledge (arcana) +9, Knowledge (dungeoneering) +9, Knowledge (planes) +9, Knowledge (religion) +9, Perception +21, Sense Motive +14, Stealth +19
**Languages** Abyssal, Celestial, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** swarmwalking, untouched by flame

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary
**Treasure** standard

### Special Abilities

**Disease (Su)** Bite or claw—injury; save Fortitude DC 20; onset 1 hour; frequency 1 day; effect 1d3 Constitution damage plus _[[conditions/Sickened|sickened]]_ and _[[conditions/Shaken|shaken]]_; cure 2 consecutive saves.

**Droning (Su)** As a standard action, a druj nasu can beat its wings in such a way that the sound they make resembles the droning of millions of buzzing flies. This sonic effect extends out to a 30-foot radius, though a creature can still hear the cacophony from a distance without being affected. Creatures in the area take a –4 penalty on Perception checks involving hearing, and all creatures in the area have a 25% chance each round of being _[[conditions/Nauseated|nauseated]]_ for 1 round. Any creature subject to the nauseating effect of this ability can negate the nausea with a successful DC 20 Fortitude saving throw. In addition, any creature casting a spell in the area must succeed at a concentration check (DC = 15 + the level of the spell being cast) or lose the spell. After initiating this effect, a druj nasu can maintain the effect each round as a free action and can dismiss it as a move action.
**Swarmwalking (Su)** A druj nasu is immune to damage or _distraction_ effects caused by swarms.

**Untouched By Flame (Su)** Any undead _[[items/Armor Magic Abilities/Animated|animated]]_ by a druj nasu or any swarm summoned by this div gains the druj nasu’s _[[universal monster rules/Immunity|immunity]]_ to fire.

##### Description

Foul corruptors of the dead, druj nasus are divs that haunt funeral pyres, mausoleums, and burial sites to steal corpses. They represent the uncleanness of the body and corrupting forces that can prevent a creature’s proper passage into the afterlife. Some scholars claim that in ancient times these creatures’ interference caused numerous cultures to alter their practices regarding burial.

When a druj nasu was found near a body that was to be buried, the body would be considered unclean. An unclean body couldn’t be buried and the _[[items/Weapon Magic Abilities/Sacred|sacred]]_ flames of a funeral pyre would only spread the taint to the winds, so some ancient people would then carry the corpse up the side of a cliff or mountain and have the birds and other animals clean the flesh from the bones before the deceased could be interred with the necessary rites to ensure a proper passage into the Great Beyond.

Unlike other corpse thieves, druj nasus don’t take the bodies of the deceased in order to feast upon the rotting flesh. The divs do this to _[[spells/Spite|spite]]_ the survivors and bring greater grief and sorrow to the family and loved ones of the dead. After pilfering the bodies, the divs watch from afar as the grieving family sinks deeper into sadness. They then animate the stolen remains and, since they have no innate ability to influence these creations, use their _command undead_ spell-like ability to send the shambling corpse back to prey upon its former loved ones. In this way, druj nasus disrupt polite society and commit one of the ultimate cultural taboos.

Because druj nasus, like all divs, are a scourge on humanity’s accomplishments, these foul fiends are a constant target of good faiths. They are particularly hated by followers of Pharasma because of their treatment of corpses and proclivity for animating the remains they steal. Druj nasus generally ignore Pharasmins, however, and instead focus on their own mockery of the living. Because of an _[[monsters/Unknown|unknown]]_, ancient conflict in Kelesh, druj nasus have a strong hatred for Sarenrae and her worshipers, going so far as to single them out in combat and steal away the bodies of the clergy and faithful. Sarenrae’s devoted find combating these divs frustrating due to their _immunity_ to fire.

A druj nasu stands roughly 6 feet tall and weighs a slight 100 pounds.
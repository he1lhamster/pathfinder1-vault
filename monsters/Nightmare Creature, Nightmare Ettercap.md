---
cssclass: [monsters]
title1: Nightmare Creature, Nightmare Ettercap
desc_short: This strange humanoid looks like a gangly, distorted caricature of an
  ettercap, with spiderlike fingers and an enormous wicked grin.
title2: Nightmare Ettercap
CR: 4
sources:
- name: Bestiary 4
  page: 204
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 1200
alignment: NE
size: Medium
type: aberration
initiative:
  bonus: 9
senses:
  darkvision: 120
  low-light vision: true
auras:
- name: fear
  radius: 60
  DC: 13
- name: frightful presence
  radius: 30
  DC: 13
AC:
  AC: 17
  touch: 15
  flat_footed: 12
  components:
    dex: 5
    natural: 2
HP:
  HP: 30
  long: 4d8+12
  regeneration: 5
  regeneration_weakness: good spells and weapons, silver
saves:
  fort: 6
  ref: 6
  will: 6
defensive_abilities:
- illusion resistance
- protection from good
DR:
- amount: 5
  weakness: good or silver
speeds:
  base: 30
  climb: 30
  fly: 10
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: bite +5 (1d6+2 plus poison)
      entries:
      - - damage: 1d6+2
        - effect: poison
      attack: bite
      bonus:
      - 5
    - text: 2 claws +5 (1d4+2)
      entries:
      - - damage: 1d4+2
      count: 2
      attack: claws
      bonus:
      - 5
  special:
  - night terrors (DC 13)
  - poison
  - traps
  - web (+8 ranged, DC 15, 4 hp)
spell_like_abilities:
  entries:
  - name: protection from good
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: 3/day
    DC: 13
  - name: dream
    source: default
    freq: 3/day
    DC: 16
  - name: nightmare
    source: default
    freq: 3/day
    DC: 16
  - name: suggestion
    source: default
    freq: 3/day
    DC: 14
  - name: shadow walk
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 4
    concentration: 5
ability_scores:
  STR: 14
  DEX: 21
  CON: 17
  INT: 8
  WIS: 15
  CHA: 12
BAB: 3
CMB: 5
CMD: 20
feats:
- name: Great Fortitude
- name: Improved Initiative
skills:
  Climb: 14
  Craft (trapmaking): 11
  Fly: 13
  Intimidate: 5
  Perception: 9
  Stealth: 15
  _racial_mods:
    Craft (trapmaking):
      _: 8
    Intimidate:
      _: 4
    Stealth:
      _: 4
languages:
- Common
special_qualities:
- feign death (DC 13)
- spider empathy +7
ecology:
  environment: temperate forests
  organization: solitary, pair, or nests (3-6 plus 2-6 giant spiders)
  treasure_type: standard
special_abilities:
  Poison (Ex): Bite-injury; save Fort DC 15; frequency 1/round for 10 rounds; effect
    1d2 Dex; cure 2 consecutive saves. The save DC is Constitution-based.
  Spider Empathy (Ex): This ability functions as a druid's wild empathy, except that
    an ettercap can only use this ability on spiders. An ettercap gains a +4 racial
    bonus on this check. Spiders are mindless, but this empathic communication imparts
    to them a modicum of implanted intelligence, allowing ettercaps to train giant
    spiders and use them as guardians.
  Traps (Ex): An ettercap is particularly skilled at crafting cunning traps with its
    webs. Deadfalls, nooses, and spear traps are the most common traps ettercaps build
    with their webs. An ettercap doesn't require gold to build its traps, merely time.
    Rules for crafting traps can be found in Chapter 13 of the Pathfinder RPG Core
    Rulebook. Ettercap traps can be found on page 129 of the Pathfinder RPG Bestiary.
desc_long: |-
  Nightmare creatures have an unnatural link to the most terrifying parts of the Dimension of Dreams, allowing them to turn others' dreams into nightmares and sow fear even in the waking world. Corrupted by their power, they become evil and use their abilities to torment their enemies and abuse creatures weaker than themselves. Eventually this dream connection corrupts the creature's appearance into a bizarre caricature of its original form.

  A nightmare creature uses its ability to control dreams to confuse and frighten its target with horrendous imagery- visions of failure or betrayal and horrific scenes of murder and death. A nightmare creature may even allow the target to think it is in control of the dream or has awakened from a nightmare, only to snatch away that hope and send its target into a downward spiral of misery and self-doubt. The most wicked nightmare creatures tend to become ghosts if slain, returning again and again to haunt their chosen victims.

---

# Nightmare Creature, Nightmare Ettercap
This strange humanoid looks like a gangly, distorted caricature of an _[[monsters/Ettercap|ettercap]]_, with spiderlike fingers and an enormous wicked grin.
**Source** Bestiary 4 pg. 204
**XP** 1,200

NE Medium aberration
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +9
**Aura** _[[universal monster rules/Fear|fear]]_ (60 ft., DC 13), _[[universal monster rules/Frightful Presence|frightful presence]]_ (30 ft., DC 13)

##### Defense

**AC** 17, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+5 Dex, +2 natural)
**hp** 30 (4d8+12); _[[universal monster rules/Regeneration|regeneration]]_ 5 (good spells and weapons, silver)
**Fort** +6, **Ref** +6, **Will** +6
**Defensive Abilities** illusion _[[universal monster rules/Resistance|resistance]]_, _[[spells/Protection From Good|protection from good]]_; **DR** 5/good or silver

##### Offense
**Speed** 30 ft., _[[universal monster rules/Climb|climb]]_ 30 ft., fly 10 ft. (perfect)
**Melee** bite +5 (1d6+2 plus poison), 2 claws +5 (1d4+2)
**Special Attacks** _[[spells/Night Terrors|night terrors]]_ (DC 13), poison, traps, web (+8 ranged, DC 15, 4 hp)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +5)
Constant—_protection from good_
3/day—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 13), _[[spells/Dream|dream]]_ (DC 16), _[[spells/Nightmare|nightmare]]_ (DC 16), _[[spells/Suggestion|suggestion]]_ (DC 14)
1/day—_[[spells/Shadow Walk|shadow walk]]_

##### Statistics
**Str** 14, **Dex** 21, **Con** 17, **Int** 8, **Wis** 15, **Cha** 12
**Base Atk** +3; **CMB** +5; **CMD** 20
**Feats** _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_
**Skills** _Climb_ +14, Craft (trapmaking) +11, Fly +13, Intimidate +5, Perception +9, Stealth +15; **Racial Modifiers** +8 Craft (trapmaking), +4 Intimidate, +4 Stealth
**Languages** Common
**SQ** feign death (DC 13), spider _[[feats/Empathy|empathy]]_ +7

##### Ecology

**Environment** temperate forests
**Organization** solitary, pair, or nests (3–6 plus 2–6 giant spiders)
**Treasure** standard

### Special Abilities

**Poison (Ex)** Bite—injury; save Fort DC 15; frequency 1/round for 10 rounds; effect 1d2 Dex; cure 2 consecutive saves. The save DC is Constitution-based.
**Spider _Empathy_ (Ex)** This ability functions as a _[[classes/Druid|druid]]_’s wild _empathy_, except that an _ettercap_ can only use this ability on spiders. An _ettercap_ gains a +4 racial bonus on this check. Spiders are mindless, but this empathic communication imparts to them a modicum of implanted intelligence, allowing ettercaps to train giant spiders and use them as guardians.

**Traps (Ex)** An _ettercap_ is particularly skilled at crafting _[[items/Weapon Magic Abilities/Cunning|cunning]]_ traps with its webs. Deadfalls, nooses, and _[[items/Weapon/Spear|spear]]_ traps are the most common traps ettercaps build with their webs. An _ettercap_ doesn’t require gold to build its traps, merely time. Rules for crafting traps can be found in Chapter 13 of the Pathfinder RPG Core Rulebook. _Ettercap_ traps can be found on page 129 of the Pathfinder RPG Bestiary.

##### Description

_Nightmare_ creatures have an unnatural link to the most terrifying parts of the Dimension of Dreams, allowing them to turn others’ dreams into nightmares and sow _fear_ even in the waking world. Corrupted by their power, they become evil and use their abilities to torment their enemies and abuse creatures weaker than themselves. Eventually this _dream_ connection corrupts the creature’s appearance into a bizarre caricature of its original form.

A _nightmare_ creature uses its ability to control dreams to confuse and frighten its target with horrendous imagery— visions of failure or betrayal and horrific scenes of murder and death. A _nightmare_ creature may even allow the target to think it is in control of the _dream_ or has awakened from a _nightmare_, only to _[[feats/Snatch|snatch]]_ away that hope and send its target into a downward spiral of misery and self-doubt. The most wicked _nightmare_ creatures tend to become ghosts if slain, returning again and again to haunt their chosen victims.
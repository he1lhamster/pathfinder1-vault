---
cssclass: [monsters]
title1: Wendigo
desc_short: This hideous shape has the head of a feral elk with jagged teeth and sharp
  antlers. Its humanoid legs end in blackened, burnt stumps.
title2: Wendigo
CR: 17
sources:
- name: Bestiary 2
  page: 281
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
- name: 'Pathfinder #6: Spires of Xin-Shalast'
  page: 88
  link: http://paizo.com/pathfinder/adventurePath/riseOfTheRunelords/v5748btpy817c
XP: 102400
alignment: CE
size: Large
type: outsider
subtypes:
- cold
- native
initiative:
  bonus: 13
senses:
  blindsight: 60
  darkvision: 60
  low-light vision: true
AC:
  AC: 32
  touch: 18
  flat_footed: 23
  components:
    dex: 9
    natural: 14
    size: -1
HP:
  HP: 279
  long: 18d10+180
  regeneration: 15
  regeneration_weakness: fire
saves:
  fort: 21
  ref: 22
  will: 11
DR:
- amount: 15
  weakness: cold iron and magic
immunities:
- cold
- fear
SR: 28
weaknesses:
- vulnerability to fire
speeds:
  fly: 120
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: bite +26 (2d8+9/19-20 plus 4d6 cold and grab)
      entries:
      - - damage: 2d8+9
          crit_range: 19-20
        - damage: 4d6
          type: cold
        - effect: grab
      attack: bite
      bonus:
      - 26
    - text: 2 claws +26 (2d6+9/19-20 plus 4d6 cold)
      entries:
      - - damage: 2d6+9
          crit_range: 19-20
        - damage: 4d6
          type: cold
      count: 2
      attack: claws
      bonus:
      - 26
  special:
  - dream haunting
  - howl
  - rend (2 claws, 1d8+13 plus 4d6 cold plus 1d4 Cha damage)
  - wendigo psychosis
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: wind walk
    source: default
    freq: At will
    DC: 23
    other: see below
  - name: control weather
    source: default
    freq: 1/day
    other: as druid
  - name: nightmare
    source: default
    freq: 1/day
    DC: 22
  sources:
  - name: default
    CL: 18
    concentration: 25
ability_scores:
  STR: 29
  DEX: 29
  CON: 31
  INT: 26
  WIS: 20
  CHA: 24
BAB: 18
CMB: 28
CMB_other: +32 grapple
CMD: 47
feats:
- name: Ability Focus (howl)
- name: Critical Focus
- name: Flyby Attack
- name: Improved Critical (bite)
- name: Improved Critical (claws)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Persuasive
- name: Tiring Critical
skills:
  Acrobatics: 30
  Bluff: 28
  Diplomacy: 9
  Fly: 36
  Intimidate: 32
  Knowledge (arcana): 26
  Knowledge (geography): 26
  Knowledge (nature): 26
  Knowledge (religion): 26
  Knowledge (planes): 29
  Perception: 26
  Sense Motive: 26
  Spellcraft: 29
  Stealth: 26
  Survival: 26
languages:
- Aklo
- Common
- Giant
- telepathy 1 mile
special_qualities:
- no breath
ecology:
  environment: any cold
  organization: solitary
  treasure_type: none
special_abilities:
  Dream Haunting (Su): When a wendigo uses its nightmare spell-like ability, the victim
    is also exposed to wendigo psychosis.
  Howl (Ex): Three times per day as a standard action, a wendigo can emit a forlorn
    howl that can be heard up to a mile away. Any who hear the howl must make a DC
    28 Will save to avoid becoming shaken for an hour. Creatures within 120 feet become
    panicked for 1d4+4 rounds, and those within 30 feet cower with fear for 1d4 rounds.
    This is a mind-affecting fear effect. The save DC is Charisma-based.
  Wendigo Psychosis (Su): Curse-Nightmare or wind walk; save Will DC 26; onset 1 minute;
    frequency 1/day; effect 1d4 Wis drain (minimum  Wis 1); cure 3 consecutive saves.
    When a victim's Wisdom reaches 1, he seeks an individual of his race to kill and
    devour. After completing this act, the afflicted individual takes off at a run,
    and in 1d4 rounds sprints up into the sky at such a speed that his feet burn away
    into jagged stumps. The transformation into a wendigo takes 2d6 minutes as the
    victim wind walks across the sky. Once the transformation is complete, the victim
    is effectively dead, replaced by a new wendigo. True resurrection, miracle, or
    wish can restore such a victim to life, yet doing so does not harm the new wendigo.
    The save is Charisma-based.
  Wind Walk (Sp): If a wendigo pins a grappled foe, it can attempt to wind walk with
    the target by using its spell-like ability-it automatically succeeds on all concentration
    checks made to use wind walk. If the victim fails to resist the spell, the wendigo
    hurtles into the sky with him. Each round, a victim can make a new DC 23 Will
    save to turn solid again, but at this point he falls if he cannot fly. Eventually,
    the wendigo strands the victim in some rural area, usually miles from where it
    began. A creature that wind walks with a wendigo is exposed to wendigo psychosis.
    The save DC is Charisma-based.
desc_long: |-
  Beings of ancient evil, wendigos haunt the minds of mortals, driving them to desperation and, ultimately, cannibalistic madness. They enjoy whittling down prey before they strike, trailing victims for days, even weeks, while plaguing their journeys with nightmares and foul weather.

  Tribal humanoids sometimes worship wendigos as gods, bringing them live sacrifices or attempting to appease the creatures by engaging in ritual cannibalism. They mark a wendigo's territory with fetishes and dress in the furs and hides of whatever animal it most closely resembles. Wendigos take little interest in the practices of their worshipers, and view them only as an ample supply of victims.

---

# Wendigo
This hideous shape has the head of a feral elk with jagged teeth and sharp antlers. Its humanoid legs end in blackened, burnt stumps.
**Source** Bestiary 2 pg. 281, Pathfinder #6: Spires of Xin-Shalast pg. 88
**XP** 102,400
CE Large outsider (cold, native)
**Init** +13; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 60 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +26

##### Defense

**AC** 32, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+9 Dex, +14 natural, –1 size)
**hp** 279 (18d10+180); _[[universal monster rules/Regeneration|regeneration]]_ 15 (fire)
**Fort** +21, **Ref** +22, **Will** +11
**DR** 15/cold iron and magic; **Immune** cold, _[[universal monster rules/Fear|fear]]_; **SR** 28
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to fire

##### Offense
**Speed** fly 120 ft. (perfect)
**Melee** bite +26 (2d8+9/19–20 plus 4d6 cold and _[[universal monster rules/Grab|grab]]_), 2 claws +26 (2d6+9/19–20 plus 4d6 cold)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[spells/Dream|dream]]_ haunting, howl, _[[universal monster rules/Rend|rend]]_ (2 claws, 1d8+13 plus 4d6 cold plus 1d4 Cha damage), _[[monsters/Wendigo|wendigo]]_ psychosis
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +25)
At will—_[[spells/Wind Walk|wind walk]]_ (DC 23; see below)
1/day—_[[spells/Control Weather|control weather]]_ (as _[[classes/Druid|druid]]_), _[[spells/Nightmare|nightmare]]_ (DC 22)

##### Statistics
**Str** 29, **Dex** 29, **Con** 31, **Int** 26, **Wis** 20, **Cha** 24
**Base Atk** +18; **CMB** +28 (+32 grapple); **CMD** 47
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (howl), _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite, claws), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Persuasive|Persuasive]]_, _[[feats/Tiring Critical|Tiring Critical]]_
**Skills** Acrobatics +30, Bluff +28, Diplomacy +9, Fly +36, Intimidate +32, Knowledge (arcana, geography, nature, religion) +26, Knowledge (planes) +29, Perception +26, Sense Motive +26, Spellcraft +29, Stealth +26, Survival +26
**Languages** Aklo, Common, Giant; _[[universal monster rules/Telepathy|telepathy]]_ 1 mile
**SQ** _[[universal monster rules/No Breath|no breath]]_

##### Ecology

**Environment** any cold
**Organization** solitary
**Treasure** none

### Special Abilities

**_Dream_ Haunting (Su)** When a _wendigo_ uses its _nightmare_ spell-like ability, the victim is also exposed to _wendigo_ psychosis.

**Howl (Ex) **Three times per day as a standard action, a _wendigo_ can emit a forlorn howl that can be heard up to a mile away. Any who hear the howl must make a DC 28 Will save to avoid becoming _[[conditions/Shaken|shaken]]_ for an hour. Creatures within 120 feet become _[[conditions/Panicked|panicked]]_ for 1d4+4 rounds, and those within 30 feet cower with _fear_ for 1d4 rounds. This is a mind-affecting _fear_ effect. The save DC is Charisma-based.

**_Wendigo_ Psychosis (Su)** Curse—_Nightmare_ or _wind walk_; save Will DC 26; onset 1 minute; frequency 1/day; effect 1d4 Wis drain (minimum Wis 1); cure 3 consecutive saves. When a victim’s Wisdom reaches 1, he seeks an individual of his race to kill and devour. After completing this act, the afflicted individual takes off at a run, and in 1d4 rounds sprints up into the sky at such a speed that his feet _[[universal monster rules/Burn|burn]]_ away into jagged stumps. The _[[spells/Transformation|transformation]]_ into a _wendigo_ takes 2d6 minutes as the victim wind walks across the sky. Once the _transformation_ is complete, the victim is effectively dead, replaced by a new _wendigo_. _[[spells/True Resurrection|True resurrection]]_, _[[spells/Miracle|miracle]]_, or _[[spells/Wish|wish]]_ can restore such a victim to life, yet doing so does not _[[spells/Harm|harm]]_ the new _wendigo_. The save is Charisma-based.

**_Wind Walk_ (Sp)** If a _wendigo_ pins a _[[conditions/Grappled|grappled]]_ foe, it can attempt to _wind walk_ with the target by using its spell-like ability—it automatically succeeds on all concentration checks made to use _wind walk_. If the victim fails to resist the spell, the _wendigo_ hurtles into the sky with him. Each round, a victim can make a new DC 23 Will save to turn solid again, but at this point he falls if he cannot fly. Eventually, the _wendigo_ strands the victim in some rural area, usually miles from where it began. A creature that wind walks with a _wendigo_ is exposed to _wendigo_ psychosis. The save DC is Charisma-based.

##### Description

Beings of ancient evil, wendigos haunt the minds of mortals, driving them to desperation and, ultimately, cannibalistic madness. They enjoy whittling down prey before they strike, trailing victims for days, even weeks, while plaguing their journeys with nightmares and foul weather.

Tribal humanoids sometimes worship wendigos as gods, bringing them live sacrifices or attempting to appease the creatures by engaging in ritual cannibalism. They mark a _wendigo_’s territory with fetishes and dress in the _[[items/Mundane/Furs|furs]]_ and hides of whatever animal it most closely resembles. Wendigos take little interest in the practices of their worshipers, and view them only as an ample supply of victims.
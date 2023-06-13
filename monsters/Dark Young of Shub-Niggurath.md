---
cssclass: [monsters]
title1: Dark Young of Shub-Niggurath
desc_short: The lumbering bulk of a treelike monster lurches out of the mist, its
  branches tentacles, its roots ending in hooves, and its trunk decorated with numerous
  drooling maws.
title2: Dark Young of Shub-Niggurath
CR: 12
sources:
- name: 'Pathfinder #46: Wake of the Watcher'
  page: 78
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderAdventurePath/carrionCrown/v5748btpy8l3e
XP: 19200
alignment: CE
size: Huge
type: aberration
initiative:
  bonus: 7
senses:
  darkvision: 60
  tremorsense: 30
auras:
- name: frightful presence
  radius: 30
  DC: 24
AC:
  AC: 27
  touch: 11
  flat_footed: 24
  components:
    dex: 3
    natural: 16
    size: -2
HP:
  HP: 161
  long: 14d8+98
saves:
  fort: 11
  ref: 9
  will: 13
DR:
- amount: 15
  weakness: slashing
immunities:
- acid
- electricity
- fire
- poison
speeds:
  base: 30
attacks:
  melee:
  - - text: 4 tentacles +19 (1d8+10/19-20 plus grab)
      entries:
      - - damage: 1d8+10
          crit_range: 19-20
        - effect: grab
      count: 4
      attack: tentacles
      bonus:
      - 19
  special:
  - constrict (1d8+10)
  - sucking maws
  - trample (1d8+15, DC 27)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: freedom of movement
    source: default
    freq: Constant
  - name: air walk
    source: default
    freq: At will
  - name: tree shape
    source: default
    freq: At will
  - name: entangle
    source: default
    freq: 3/day
    DC: 16
  - name: command plants
    source: default
    freq: 3/day
    DC: 19
  - name: insanity
    source: default
    freq: 1/day
    DC: 22
  - name: tree stride
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 12
    concentration: 17
ability_scores:
  STR: 30
  DEX: 17
  CON: 24
  INT: 16
  WIS: 19
  CHA: 21
BAB: 10
CMB: 22
CMB_other: +26 grapple
CMD: 35
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Improved Critical (tentacles)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Power Attack
- name: Vital Strike
- name: Weapon Focus (tentacles)
skills:
  Knowledge (arcana): 17
  Knowledge (nature): 17
  Knowledge (religion): 17
  Perception: 21
  Sense Motive: 18
  Spellcraft: 20
  Stealth: 12
    in forests: 20
  _racial_mods:
    Stealth:
      in forests: 8
languages:
- Aklo
ecology:
  environment: temperate forest or swamp
  organization: solitary, pair, or grove (3-6)
  treasure_type: standard
special_abilities:
  Sucking Maws (Su): A dark young of Shub-Niggurath that successfully pins a creature
    it is grappling automatically inflicts 1d4 points of Strength drain on that creature.
    A DC 24 Fortitude save reduces this effect to 1 point of Strength drain. A creature
    drained to 0 Strength does not die, but must make a DC 24 Will save at that point
    to resist being driven mad by the experience, as the foul green waste exuded from
    the same sucking mouths that drink life implant in the emptied shells strange
    visions and horrifying certainties. If you use the GameMastery Guide in your game,
    this madness manifests as schizophrenia, but with a save DC equal to the dark
    young's Strength drain save DC listed above (DC 24 for most dark young). One common
    result of this unfortunate madness is a strange desire to return to the site of
    their original encounter in hopes of being consumed entirely by the creature that
    only drank a part of their body and mind-many of those who survive this horrific
    ordeal go on to found dark young cults of their own. If you don't use the GameMastery
    Guide in your game, treat this madness instead as an insanity spell. The madness
    element of a dark young's sucking maws is a mind-affecting effect. The save DC
    for all of the saving throws involved with this special ability is Constitution-based.
desc_long: |-
  The Elder God known in whispered circles as Shub- Niggurath is reputed to have a thousand young, when in fact her spawn are myriad. Yet some of her children are more fecund and successful than others, and the monstrosities known as her dark young are perhaps the best known of this legion of monstrosities.

  In combat, a dark young usually starts by using entangle and command plants to seize control of the surrounding terrain-its ability to constantly use freedom of movement affords it mobility through such regions, allowing it to move through the areas and select its prey with ease. Intelligent and canny, dark young know that spellcasters are more difficult to affect with insanity, and save that spell-like ability for use against rogues, fighters, and similar foes. Flight offers no guarantee of safety from the dark young, for they can pursue their foes through the air as surely as across land.

---

# Dark Young of Shub-Niggurath
The lumbering bulk of a treelike monster lurches out of the mist, its branches tentacles, its roots ending in hooves, and its trunk decorated with numerous drooling maws.
**Source** Pathfinder #46: Wake of the _[[monsters/Watcher|Watcher]]_ pg. 78
**XP** 19,200
CE Huge aberration
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Tremorsense|tremorsense]]_ 30 ft.; Perception +21
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (30 ft., DC 24)

##### Defense

**AC** 27, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+3 Dex, +16 natural, -2 size)
**hp** 161 (14d8+98)
**Fort** +11, **Ref** +9, **Will** +13
**DR** 15/slashing; **Immune** acid, electricity, fire, poison

##### Offense
**Speed** 30 ft.
**Melee** 4 tentacles +19 (1d8+10/19-20 plus _[[universal monster rules/Grab|grab]]_)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (1d8+10), sucking maws, _[[universal monster rules/Trample|trample]]_ (1d8+15, DC 27)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +17)
Constant - _[[spells/Freedom of Movement|freedom of movement]]_
At will - _[[spells/Air Walk|air walk]]_, _[[spells/Tree Shape|tree shape]]_
3/day - _[[spells/Entangle|entangle]]_ (DC 16), _[[spells/Command Plants|command plants]]_ (DC 19)
1/day - _[[spells/Insanity|insanity]]_ (DC 22), _[[spells/Tree Stride|tree stride]]_

##### Statistics
**Str** 30, **Dex** 17, **Con** 24, **Int** 16, **Wis** 19, **Cha** 21
**Base Atk** +10; **CMB** +22 (+26 grapple); **CMD** 35 (can't be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Critical|Improved Critical]]_ (tentacles), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (tentacles)
**Skills** Knowledge (arcana) +17, Knowledge (nature) +17, Knowledge (religion) +17, Perception +21, Sense Motive +18, Spellcraft +20, Stealth +12 (+20 in forests); **Racial Modifiers** +8 Stealth in forests
**Languages** Aklo

##### Ecology

**Environment** temperate forest or swamp
**Organization** solitary, pair, or grove (3-6)
**Treasure** standard

### Special Abilities
**Sucking Maws (Su)** A _[[monsters/Dark Young of Shub-Niggurath|dark young of Shub-Niggurath]]_ that successfully pins a creature it is grappling automatically inflicts 1d4 points of Strength drain on that creature. A DC 24 Fortitude save reduces this effect to 1 point of Strength drain. A creature drained to 0 Strength does not die, but must make a DC 24 Will save at that point to resist being driven mad by the experience, as the foul green waste exuded from the same sucking mouths that drink life implant in the emptied shells strange visions and horrifying certainties. If you use the GameMastery Guide in your game, this madness manifests as schizophrenia, but with a save DC equal to the dark young’s Strength drain save DC listed above (DC 24 for most dark young). One common result of this unfortunate madness is a strange desire to return to the site of their original encounter in hopes of being consumed entirely by the creature that only drank a part of their body and mind—many of those who survive this horrific ordeal go on to found dark young cults of their own. If you don’t use the GameMastery Guide in your game, treat this madness instead as an _insanity_ spell. The madness element of a dark young’s sucking maws is a mind-affecting effect. The save DC for all of the saving throws involved with this special ability is Constitution-based.

##### Description

The Elder God known in whispered circles as Shub- Niggurath is reputed to have a thousand young, when in fact her spawn are myriad. Yet some of her children are more fecund and successful than others, and the monstrosities known as her dark young are perhaps the best known of this legion of monstrosities.

In combat, a dark young usually starts by using _entangle_ and _command plants_ to seize control of the surrounding terrain—its ability to constantly use _freedom of movement_ affords it _[[feats/Mobility|mobility]]_ through such regions, allowing it to move through the areas and select its prey with ease. Intelligent and canny, dark young know that spellcasters are more difficult to affect with _insanity_, and save that spell-like ability for use against rogues, fighters, and similar foes. _[[universal monster rules/Flight|Flight]]_ offers no guarantee of safety from the dark young, for they can pursue their foes through the air as surely as across land.
---
cssclass: [monsters]
title1: Seaweed Siren
desc_short: This creature's three singing heads sway atop serpentine necks that extend
  from a bulbous body split by a wide, toothy mouth.
title2: Seaweed Siren
CR: 13
sources:
- name: Bestiary 4
  page: 235
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
- name: "Pathfinder #60: From Hell's Heart"
  page: 90
  link: http://paizo.com/pathfinder/adventurePath/skullAndShackles/v5748btpy8moi
XP: 25600
alignment: CN
size: Large
type: magical beast
subtypes:
- aquatic
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: cacophony
  radius: 100
  DC: 22
AC:
  AC: 26
  touch: 11
  flat_footed: 24
  components:
    dex: 2
    natural: 15
    size: -1
HP:
  HP: 184
  long: 16d10+96
saves:
  fort: 16
  ref: 12
  will: 8
immunities:
- mind-affecting effects
resistances:
  fire: 10
  sonic: 10
speeds:
  base: 30
  swim: 30
attacks:
  melee:
  - - text: bite +25 (4d6+15/19-20)
      entries:
      - - damage: 4d6+15
          crit_range: 19-20
      attack: bite
      bonus:
      - 25
  ranged:
  - - text: 3 sonic beams +17 (5d6 sonic)
      entries:
      - - damage: 5d6
          type: sonic
      count: 3
      attack: sonic beams
      bonus:
      - 17
  special:
  - staggering gaze
  - trample (1d10+15, DC 28)
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: shatter
    source: default
    freq: At will
    DC: 16
  - name: charm monster
    source: default
    freq: 3/day
    DC: 18
  - name: quickened confusion
    source: default
    freq: 3/day
    DC: 18
  - name: bestow curse
    source: default
    freq: 1/day
    paren_text: DC 18, ranged touch attack, 30 ft.
  sources:
  - name: default
    CL: 16
    concentration: 19
ability_scores:
  STR: 30
  DEX: 15
  CON: 22
  INT: 11
  WIS: 16
  CHA: 19
BAB: 16
CMB: 27
CMD: 39
CMD_other: 47 vs. trip
feats:
- name: Blind-Fight
- name: Critical Focus
- name: Deafening Critical
- name: Improved Critical (bite)
- name: Point-Blank Shot
- name: Power Attack
- name: Quicken Spell- Like Ability (confusion)
- name: Skill Focus (Perception)
skills:
  Bluff: 12
  Perception: 17
  Stealth: 17
    in water: 21
  Swim: 18
  _racial_mods:
    Stealth:
      in water: 4
languages:
- Aklo
- tongues
special_qualities:
- false heads
- water dependency
ecology:
  environment: any coastlines
  organization: solitary
  treasure_type: standard
special_abilities:
  Cacophony (Su): A seaweed siren's noises disrupt spellcasting; casting within 100
    feet of a seaweed siren requires a concentration check (DC 15 + the level of the
    spell being cast). All other concentration checks and Perception checks involving
    hearing made inside the aura have their DCs increased by 5. A siren can begin
    or end this ability as a free action. This is a sonic effect.
  False Heads (Ex): A seaweed siren's false heads can be severed. To sever a head,
    an opponent must make a sunder attempt with a slashing weapon targeting the head.
    A head is considered a separate weapon with hardness 0 and hit points equal to
    the siren's Hit Dice (typically 16 hp). To sever a head, an opponent must deal
    enough damage to reduce the head's hit points to 0 or fewer. Severing a head deals
    an amount of damage to the siren's body equal to the siren's Hit Dice. A siren
    can't attack with a severed head. A siren with no remaining heads can't use its
    cacophony ability or its spell-like abilities.
  Sonic Beams (Su): Each of the siren's false heads can fire a beam at a range of
    60 feet, dealing 4d6 points of sonic damage.
  Staggering Gaze (Su): Staggered 1d6 rounds, 30 feet, Will DC 22 negates. This is
    a mind-affecting effect. The save DC is Charisma-based.
  Water Dependency (Ex): A seaweed siren can survive out of the water for 1 hour per
    point of Constitution (typically 22 rounds). Beyond this limit, a seaweed siren
    begins to suffocate.
desc_long: A seaweed siren is a predator that uses false humanlike heads on its upper
  appendages in order to lure prey. The heads babble nonsense words and fragments
  of overheard sentences. If spoken to, they respond with words from a similar language.
  This behavior allows the seaweed siren to creep about under the water with only
  the heads showing, pretending to be swimming humanoids until it is ready to attack.

---

# Seaweed Siren
This creature’s three _[[items/Armor Magic Abilities/Singing|singing]]_ heads sway atop serpentine necks that extend from a bulbous body _[[universal monster rules/Split|split]]_ by a wide, toothy mouth.
**Source** Bestiary 4 pg. 235, Pathfinder #60: From Hell's Heart pg. 90
**XP** 25,600

CN Large magical beast (aquatic)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +17
**Aura** cacophony (100 ft., DC 22)

##### Defense

**AC** 26, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+2 Dex, +15 natural, –1 size)
**hp** 184 (16d10+96)
**Fort** +16, **Ref** +12, **Will** +8
**Immune** mind-affecting effects; **Resist** fire 10, sonic 10

##### Offense
**Speed** 30 ft., swim 30 ft.
**Melee** bite +25 (4d6+15/19–20)
**Ranged** 3 sonic beams +17 (5d6 sonic)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** staggering _[[universal monster rules/Gaze|gaze]]_, _[[universal monster rules/Trample|trample]]_ (1d10+15, DC 28)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +19)
At will—_[[spells/Shatter|shatter]]_ (DC 16)
3/day—_[[spells/Charm Monster|charm monster]]_ (DC 18), quickened _[[spells/Confusion|confusion]]_ (DC 18)
1/day—_[[spells/Bestow Curse|bestow curse]]_ (DC 18, ranged touch attack, 30 ft.)

##### Statistics
**Str** 30, **Dex** 15, **Con** 22, **Int** 11, **Wis** 16, **Cha** 19
**Base Atk** +16; **CMB** +27; **CMD** 39 (47 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Deafening Critical|Deafening Critical]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Power Attack|Power Attack]]_, Quicken Spell- Like Ability (_confusion_), _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** Bluff +12, Perception +17, Stealth +17 (+21 in water), Swim +18; **Racial Modifiers** +4 Stealth in water
**Languages** Aklo; _[[spells/Tongues|tongues]]_
**SQ** false heads, _[[universal monster rules/Water Dependency|water dependency]]_

##### Ecology

**Environment** any coastlines
**Organization** solitary
**Treasure** standard

### Special Abilities

**Cacophony (Su)** A _[[monsters/Seaweed Siren|seaweed siren]]_’s noises disrupt spellcasting; casting within 100 feet of a _seaweed siren_ requires a concentration check (DC 15 + the level of the spell being cast). All other concentration checks and Perception checks involving hearing made inside the aura have their DCs increased by 5. A _[[monsters/Siren|siren]]_ can begin or end this ability as a free action. This is a sonic effect.

**False Heads (Ex)** A _seaweed siren_’s false heads can be severed. To sever a head, an opponent must make a sunder attempt with a slashing weapon targeting the head. A head is considered a separate weapon with hardness 0 and hit points equal to the _siren_’s Hit Dice (typically 16 hp). To sever a head, an opponent must deal enough damage to reduce the head’s hit points to 0 or fewer. Severing a head deals an amount of damage to the _siren_’s body equal to the _siren_’s Hit Dice. A _siren_ can’t attack with a severed head. A _siren_ with no remaining heads can’t use its cacophony ability or its _spell-like abilities_.
**Sonic Beams (Su)** Each of the _siren_’s false heads can fire a beam at a range of 60 feet, dealing 4d6 points of sonic damage.
**Staggering _Gaze_ (Su)** _[[conditions/Staggered|Staggered]]_ 1d6 rounds, 30 feet, Will DC 22 negates. This is a mind-affecting effect. The save DC is Charisma-based.

**_Water Dependency_ (Ex)** A _seaweed siren_ can survive out of the water for 1 hour per point of Constitution (typically 22 rounds). Beyond this limit, a _seaweed siren_ begins to suffocate.

##### Description

A _seaweed siren_ is a predator that uses false humanlike heads on its upper appendages in order to lure prey. The heads _[[spells/Babble|babble]]_ nonsense words and fragments of overheard sentences. If spoken to, they respond with words from a similar language. This behavior allows the _seaweed siren_ to creep about under the water with only the heads showing, pretending to be swimming humanoids until it is ready to attack.
---
cssclass: [monsters]
title1: Contemplative, Enlightened Contemplative
desc_short: Resembling an enlarged brain with an atrophied humanoid body attached,
  this floating creature pulses with energy.
title2: Enlightened Contemplative
CR: 5
sources:
- name: Occult Bestiary
  page: 17
  link: http://paizo.com/products/btpy9g21?Pathfinder-Campaign-Setting-Occult-Bestiary
XP: 1600
alignment: N
size: Medium
type: monstrous humanoid
initiative:
  bonus: 5
senses:
  blindsight: 30
  darkvision: 60
  thoughtsense: 60
AC:
  AC: 16
  touch: 16
  flat_footed: 15
  components:
    deflection: 5
    dex: 1
HP:
  HP: 40
  long: 9d10-9
saves:
  fort: 4
  ref: 7
  will: 9
defensive_abilities:
- psychic buffer
speeds:
  fly: 40
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 claws +9 (1d4)
      entries:
      - - damage: 1d4
      count: 2
      attack: claws
      bonus:
      - 9
  - - text: touch +4 (phrenic disruption)
      entries:
      - - effect: phrenic disruption
      attack: touch
      bonus:
      - 4
  special:
  - phrenic disruption (DC 19)
spell_like_abilities:
  entries:
  - name: mage hand
    source: default
    freq: Constant
  - superscripts:
    - OA
    name: thought shield I
    source: default
    freq: Constant
  - superscripts:
    - OA
    name: thoughtsense
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: At will
    DC: 17
  sources:
  - name: default
    CL: 9
    concentration: 14
psychic_magic:
  entries:
  - name: detect magic
    PE: 0
  - superscripts:
    - OA
    name: hypercognition
    PE: 2
  - superscripts:
    - OA
    name: instigate psychic duel
    PE: 2
    DC: 17
  - superscripts:
    - OA
    name: mind thrust II
    PE: 2
    DC: 17
  - superscripts:
    - OA
    name: mindlink
    PE: 1
  - superscripts:
    - OA
    name: mindscape door
    PE: 3
    DC: 18
  - superscripts:
    - OA
    name: psychic asylum
    PE: 5
  - superscripts:
    - OA
    name: synaptic pulse
    PE: 3
    DC: 18
  - superscripts:
    - OA
    name: thought shield III
    PE: 4
  sources:
  - name: default
    CL: 9
    concentration: 14
  PE: 12
ability_scores:
  STR: 10
  DEX: 12
  CON: 9
  INT: 26
  WIS: 17
  CHA: 21
BAB: 9
CMB: 9
CMD: 25
feats:
- name: Alertness
- name: Combat Casting
- name: Flyby Attack
- name: Great Fortitude
- name: Improved Initiative
skills:
  Bluff: 14
  Diplomacy: 14
  Fly: 21
  Knowledge (arcana): 17
  Knowledge (geography): 17
  Knowledge (history): 17
  Knowledge (planes): 17
  Linguistics: 17
  Perception: 17
  Sense Motive: 14
  Spellcraft: 17
  Stealth: 13
languages:
- telepathy 300 ft.
- tongues
special_qualities:
- thought form
ecology:
  environment: any urban
  organization: solitary, band (2-5), or entourage (1 plus 2-4 contemplatives)
  treasure_type: standard
special_abilities:
  Phrenic Disruption (Su): An enlightened contemplative using its thought form ability
    can disrupt the thoughts of a creature as an incorporeal touch attack. The target
    must succeed at a DC 19 Will saving throw or be staggered for 1d4 rounds; multiple
    touches reset the duration but do not stack. At the start of a turn in which it
    is staggered by this ability, a creature must succeed at a second Will saving
    throw or take 1 point of Intelligence damage. This is a mind-affecting effect.
    The save DC is Charisma-based.
  Psychic Buffer (Su): An enlightened contemplative generates a field of mental interference
    that absorbs hostile attacks. Whenever the enlightened contemplative would take
    hit point damage from a mind-affecting effect, it reduces the damage taken by
    5. In addition, it adds its Charisma modifier as a deflection bonus to its Armor
    Class.
  Thought Form (Su): As a move action, an enlightened contemplative can transform
    into a translucent figure of pure thought, during which time it is incorporeal
    and can use its phrenic disruption ability. It can remain in this form for a number
    of rounds per day equal to its Hit Dice (typically 9 rounds). If the effect ends
    while the enlightened contemplative is in a space it could not otherwise occupy,
    it takes 3d6 points of damage and is shunted to the nearest open space it could
    occupy.
desc_long: |-
  Long ago, Akiton's legendary Contemplatives of Ashok (Pathfinder Campaign Setting: Distant Worlds 60) were a race of relatively ordinary humanoids. As they came into the fullness of their intelligence, however, they unlocked great psychic abilities that slowly rendered their bodies unnecessary, resulting in a quick evolutionary march toward their current forms-floating brains attached to withered, vestigial bodies.

  Now in direct control of their own evolutionary progress, most contemplatives choose to advance methodically and scientifically. Yet a small subset engaged in daring research into occultism and the Esoteric Planes favor a more reckless approach. The most impressive discoveries of these self-styled “enlightened” individuals allow them to transcend the material world's limitations for brief periods of time, much to the chagrin of more conservative contemplatives, who prefer to pursue less radical methods than their peers.

---

# Contemplative, Enlightened Contemplative
Resembling an enlarged brain with an atrophied humanoid body attached, this floating creature pulses with energy.
**Source** Occult Bestiary pg. 17
**XP** 1,600

N Medium monstrous humanoid
**Init** +5; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 30 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Thoughtsense|thoughtsense]]_ 60 ft.; Perception +17

##### Defense

**AC** 16, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+5 _[[spells/Deflection|deflection]]_, +1 Dex)
**hp** 40 (9d10–9)
**Fort** +4, **Ref** +7, **Will** +9
**Defensive Abilities** _[[classes/Psychic|psychic]]_ buffer

##### Offense
**Speed** fly 40 ft. (perfect)
**Melee** 2 claws +9 (1d4) or touch +4 (phrenic _[[items/Weapon Magic Abilities/Disruption|disruption]]_)
**Special Attacks** phrenic _disruption_ (DC 19)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +14)
Constant—_[[spells/Mage Hand|mage hand]]_, _[[spells/Thought _[[spells/Shield|Shield]]_ I|thought _shield_ I]]_, _thoughtsense_, _[[spells/Tongues|tongues]]_
At will—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 17)
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_ **(CL 9th; concentration +14)
12 PE—_[[spells/Detect Magic|detect magic]]_ (0 PE), _[[spells/Hypercognition|hypercognition]]_ (2 PE), _[[spells/Instigate _Psychic_ Duel|instigate _psychic_ duel]]_ (2 PE, DC 17), _[[spells/Mind Thrust II|mind thrust II]]_ (2 PE, DC 17), _[[spells/Mindlink|mindlink]]_ (1 PE), _[[spells/Mindscape Door|mindscape door]]_ (3 PE, DC 18), _[[spells/Psychic Asylum|psychic asylum]]_ (5 PE), _[[spells/Synaptic Pulse|synaptic pulse]]_ (3 PE, DC 18), _[[spells/Thought _Shield_ III|thought _shield_ III]]_ (4 PE)

##### Statistics
**Str** 10, **Dex** 12, **Con** 9, **Int** 26, **Wis** 17, **Cha** 21
**Base Atk** +9; **CMB** +9; **CMD** 25
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_
**Skills** Bluff +14, Diplomacy +14, Fly +21, Knowledge (arcana, geography, history, planes) +17, Linguistics +17, Perception +17, Sense Motive +14, Spellcraft +17, Stealth +13
**Languages** _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.; _tongues_
**SQ** thought form

##### Ecology

**Environment** any urban
**Organization** solitary, band (2–5), or entourage (1 plus 2–4 contemplatives)
**Treasure** standard

### Special Abilities

**Phrenic _Disruption_ (Su)** An enlightened _[[monsters/Contemplative|contemplative]]_ using its thought form ability can disrupt the thoughts of a creature as an _[[universal monster rules/Incorporeal|incorporeal]]_ touch attack. The target must succeed at a DC 19 Will saving throw or be _[[conditions/Staggered|staggered]]_ for 1d4 rounds; multiple touches reset the duration but do not stack. At the start of a turn in which it is _staggered_ by this ability, a creature must succeed at a second Will saving throw or take 1 point of Intelligence damage. This is a mind-affecting effect. The save DC is Charisma-based.

**_Psychic_ Buffer (Su)** An enlightened _contemplative_ generates a field of mental interference that absorbs hostile attacks. Whenever the enlightened _contemplative_ would take hit point damage from a mind-affecting effect, it reduces the damage taken by 5. In addition, it adds its Charisma modifier as a _deflection_ bonus to its Armor Class.

**Thought Form (Su)** As a move action, an enlightened _contemplative_ can transform into a translucent figure of pure thought, during which time it is _incorporeal_ and can use its phrenic _disruption_ ability. It can remain in this form for a number of rounds per day equal to its Hit Dice (typically 9 rounds). If the effect ends while the enlightened _contemplative_ is in a space it could not otherwise occupy, it takes 3d6 points of damage and is shunted to the nearest open space it could occupy.

##### Description

Long ago, Akiton’s legendary Contemplatives of Ashok (Pathfinder Campaign Setting: Distant Worlds 60) were a race of relatively ordinary humanoids. As they came into the fullness of their intelligence, however, they unlocked great _psychic_ abilities that slowly rendered their bodies unnecessary, resulting in a quick evolutionary march toward their current forms—floating brains attached to withered, vestigial bodies.

Now in direct control of their own evolutionary progress, most contemplatives choose to advance methodically and scientifically. Yet a small subset engaged in daring research into occultism and the Esoteric Planes favor a more reckless approach. The most impressive discoveries of these self-styled “enlightened” individuals allow them to transcend the material world’s limitations for brief periods of time, much to the chagrin of more conservative contemplatives, who prefer to pursue less radical methods than their peers.
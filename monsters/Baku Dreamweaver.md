---
cssclass: [monsters]
title1: Baku Dreamweaver
desc_short: Simple but elegant robes drape over this gray-furred, trunked quadruped,
  and its kind gaze suggests a gentle wisdom.
title2: Baku Dreamweaver
CR: 11
sources:
- name: Occult Bestiary
  page: 10
  link: http://paizo.com/products/btpy9g21?Pathfinder-Campaign-Setting-Occult-Bestiary
XP: 12800
alignment: N
size: Medium
type: magical beast
initiative:
  bonus: 11
senses:
  darkvision: 60
  low-light vision: true
  thoughtsense: 60
AC:
  AC: 25
  touch: 25
  flat_footed: 18
  components:
    dex: 7
    deflection: 8
HP:
  HP: 174
  long: 12d10+96
saves:
  fort: 16
  ref: 15
  will: 12
DR:
- amount: 15
  weakness: cold iron and magic
immunities:
- mind-affecting effects
- sleep
SR: 22
speeds:
  base: 30
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 claws +19 (2d8+4 plus mental siphon)
      entries:
      - - damage: 2d8+4
        - effect: mental siphon
      count: 2
      attack: claws
      bonus:
      - 19
    - text: gore +19 (1d8+4)
      entries:
      - - damage: 1d8+4
      attack: gore
      bonus:
      - 19
  special:
  - mental siphon
spell_like_abilities:
  entries:
  - superscripts:
    - OA
    name: ethereal fists
    source: default
    freq: Constant
  - superscripts:
    - OA
    name: dream council
    source: default
    freq: At will
  - name: invisibility
    source: default
    freq: At will
  - name: lullaby
    source: default
    freq: At will
  - name: sleep
    source: default
    freq: At will
    DC: 21
  sources:
  - name: default
    CL: 11
    concentration: 19
psychic_magic:
  entries:
  - name: deep slumber
    PE: 3
    DC: 21
  - superscripts:
    - OA
    name: dream scan
    PE: 5
    DC: 23
  - superscripts:
    - OA
    name: dream voyage
    PE: 9
  - superscripts:
    - OA
    name: incorporeal chains
    PE: 6
  - name: modify memory
    PE: 5
    DC: 23
  sources:
  - name: default
    CL: 18
    concentration: 26
  PE: 30
ability_scores:
  STR: 18
  DEX: 25
  CON: 18
  INT: 18
  WIS: 23
  CHA: 27
BAB: 12
CMB: 16
CMD: 41
feats:
- name: Alertness
- name: Flyby Attack
- name: Improved Initiative
- name: Iron Will
- superscripts:
  - OA
  name: Lucid Dreamer
- name: Weapon Finesse
skills:
  Diplomacy: 20
  Fly: 15
  Knowledge (planes): 16
  Perception: 25
  Sense Motive: 22
  Spellcraft: 16
  Stealth: 22
languages:
- Aklo
- Celestial
- Common
special_qualities:
- consume dream
- dream shepherd
- dream whispers
- dreaming grace
- oneiromancy
ecology:
  environment: any
  organization: solitary
  treasure_type: standard
special_abilities:
  Consume Dream (Su): A baku dreamweaver can consume the dreams of any sleeping creature
    within 100 feet, either preventing nightmares or causing fatigue and preventing
    all effects of rest, as per a normal baku's dream eating ability (Pathfinder RPG
    Bestiary 3 31). When it is within the Dimension of Dreams, it can use this ability
    on a creature whose lucid body is within 100 feet to cause that creature to instantly
    leave the Dimension of Dreams (removing its lucid body), with no saving throw.
  Dream Shepherd (Su): A dreamweaver can enter the Dimension of Dreams at any time
    and herd a dreamer across the dreamscape, traveling great distances in a short
    period, as per the dream travelOA spell. When the dreamweaver uses either this
    ability or its dream voyageOA psychic magic ability, reaching a destination dream
    takes 30 minutes instead of 1 hour for a creature on the same plane, and the baku
    dreamweaver gains a +5 bonus on any required Will saves.
  Dream Whispers (Su): A dreamweaver can manipulate the dreams of nearby creatures
    to cultivate particular dreams. When it encounters a dreaming creature, a dreamweaver
    can change that creature's dreamscape in any way that the greater create mindscapeOA
    spell can shape a mindscape. The dreamscape acts as an immersive and harmless
    mindscape, taking any form the baku dreamweaver desires.
  Dreaming Grace (Su): A baku dreamweaver has devoured so many insubstantial dreams
    and dream creatures that it gains a deflection bonus to its AC equal to its Charisma
    modifier and adds half its Charisma modifier to its Constitution modifier to determine
    its hit points and its bonuses on Fortitude saves and Constitution checks.
  Mental Siphon (Su): When a dreamweaver hits with a claw attack, it also deals 1d4
    points of ability damage to a mental ability score of the dreamweaver's choice.
    A successful DC 24 Will save negates this ability damage. The save DC is Charisma-based.
  Oneiromancy (Su): While within the Dimension of Dreams, a dreamweaver can predict
    that plane's strange dream logic, allowing it to reroll a single failed attack
    roll or saving throw once per round.
desc_long: Unlike normal bakus, who contentedly feed on any dreams, dreamweavers savor
  the dreams of only the most imaginative and creative beings, particularly those
  of people who are attuned to the spiritual realms or possess psychic abilities.
  The potency of such sleepers' dreams grants dreamweavers increased power. Dreamweavers
  still despise night hags and other nightmare creatures, and use their puissant abilities
  to destroy these menaces.

---

# Baku Dreamweaver
Simple but elegant robes drape over this gray-furred, trunked quadruped, and its kind _[[universal monster rules/Gaze|gaze]]_ suggests a gentle wisdom.
**Source** Occult Bestiary pg. 10
**XP** 12,800

N Medium magical beast
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Thoughtsense|thoughtsense]]_ 60 ft.; Perception +25

##### Defense

**AC** 25, touch 25, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+7 Dex, +8 _[[spells/Deflection|deflection]]_)
**hp** 174 (12d10+96)
**Fort** +16, **Ref** +15, **Will** +12
**DR** 15/cold iron and magic; **Immune** mind-affecting effects, sleep; **SR** 22

##### Offense
**Speed** 30 ft., fly 60 ft. (perfect)
**Melee** 2 claws +19 (2d8+4 plus mental siphon), gore +19 (1d8+4)
**Special Attacks** mental siphon
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +19)
Constant—_[[spells/Ethereal Fists|ethereal fists]]_
At will—_[[spells/Dream Council|dream council]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Lullaby|lullaby]]_, sleep (DC 21)
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_ **(CL 18th; concentration +26)
30 PE—_[[spells/Deep Slumber|deep slumber]]_ (3 PE, DC 21), _[[spells/Dream Scan|dream scan]]_ (5 PE, DC 23), _[[spells/Dream Voyage|dream voyage]]_ (9 PE), _[[spells/Incorporeal Chains|incorporeal chains]]_ (6 PE), _[[spells/Modify Memory|modify memory]]_ (5 PE, DC 23)

##### Statistics
**Str** 18, **Dex** 25, **Con** 18, **Int** 18, **Wis** 23, **Cha** 27
**Base Atk** +12; **CMB** +16; **CMD** 41
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lucid Dreamer|Lucid Dreamer]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Diplomacy +20, Fly +15, Knowledge (planes) +16, Perception +25, Sense Motive +22, Spellcraft +16, Stealth +22
**Languages** Aklo, Celestial, Common
**SQ** consume _[[spells/Dream|dream]]_, _dream_ shepherd, _dream_ whispers, dreaming _[[spells/Grace|grace]]_, oneiromancy

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** standard

### Special Abilities

**Consume _Dream_ (Su)** A _[[monsters/Baku Dreamweaver|baku dreamweaver]]_ can consume the dreams of any sleeping creature within 100 feet, either preventing nightmares or causing fatigue and preventing all effects of rest, as per a normal _[[monsters/Baku|baku]]_’s _dream_ eating ability (Pathfinder RPG Bestiary 3 31). When it is within the Dimension of Dreams, it can use this ability on a creature whose lucid body is within 100 feet to cause that creature to instantly leave the Dimension of Dreams (removing its lucid body), with no saving throw.

**_Dream_ Shepherd (Su)** A dreamweaver can enter the Dimension of Dreams at any time and herd a dreamer across the dreamscape, traveling great distances in a short period, as per the _[[spells/Dream Travel|dream travel]]_ spell. When the dreamweaver uses either this ability or its _dream voyage_ _psychic magic_ ability, reaching a destination _dream_ takes 30 minutes instead of 1 hour for a creature on the same plane, and the _baku dreamweaver_ gains a +5 bonus on any required Will saves.

**_Dream_ Whispers (Su)** A dreamweaver can manipulate the dreams of nearby creatures to cultivate particular dreams. When it encounters a dreaming creature, a dreamweaver can change that creature’s dreamscape in any way that the greater _[[spells/Create Mindscape|create mindscape]]_ spell can shape a mindscape. The dreamscape acts as an immersive and harmless mindscape, taking any form the _baku dreamweaver_ desires.

**Dreaming _Grace_ (Su)** A _baku dreamweaver_ has devoured so many insubstantial dreams and _dream_ creatures that it gains a _deflection_ bonus to its AC equal to its Charisma modifier and adds half its Charisma modifier to its Constitution modifier to determine its hit points and its bonuses on Fortitude saves and Constitution checks.

**Mental Siphon (Su)** When a dreamweaver hits with a claw attack, it also deals 1d4 points of ability damage to a mental ability score of the dreamweaver’s choice. A successful DC 24 Will save negates this ability damage. The save DC is Charisma-based.

**Oneiromancy (Su)** While within the Dimension of Dreams, a dreamweaver can predict that plane’s strange _dream_ logic, allowing it to reroll a single failed attack roll or saving throw once per round.

##### Description

Unlike normal bakus, who contentedly feed on any dreams, dreamweavers savor the dreams of only the most imaginative and creative beings, particularly those of people who are attuned to the spiritual realms or possess _[[classes/Psychic|psychic]]_ abilities. The potency of such sleepers’ dreams grants dreamweavers increased power. Dreamweavers still despise night hags and other _[[spells/Nightmare|nightmare]]_ creatures, and use their puissant abilities to destroy these menaces.
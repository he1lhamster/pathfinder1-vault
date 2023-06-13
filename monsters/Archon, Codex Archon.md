---
cssclass: [monsters]
title1: Archon, Codex Archon
desc_short: This enormous book has wings of glowing light and an angelic figure on
  the cover that gazes out watchfully as though alive.
title2: Codex Archon
CR: 5
sources:
- name: Monster Summoner's Handbook
  page: 24
  link: http://paizo.com/products/btpy9ela?Pathfinder-Player-Companion-Monster-Summoners-Handbook
XP: 1600
alignment: LG
size: Medium
type: outsider
subtypes:
- archon
- extraplanar
- good
- lawful
initiative:
  bonus: 3
senses:
  darkvision: 60
  detect evil: true
  detect magic: true
  low-light vision: true
auras:
- name: aura of menace
  DC: 17
- name: magic circle against evil
AC:
  AC: 20
  touch: 13
  flat_footed: 17
  other: +2 deflection vs. evil
  components:
    dex: 3
    natural: 7
HP:
  HP: 47
  long: 5d10+20
saves:
  fort: 7
  ref: 7
  will: 5
  other: +4 vs. poison, +2 vs. evil
DR:
- amount: 10
  weakness: evil
immunities:
- electricity
- petrification
SR: 16
speeds:
  fly: 30
  fly_maneuverability: good
attacks:
  melee:
  - - text: slam +7 (1d8+2)
      entries:
      - - damage: 1d8+2
      attack: slam
      bonus:
      - 7
  ranged:
  - - text: light ray +8 ranged touch (1d6)
      entries:
      - - damage: 1d6
      attack: light ray
      bonus:
      - 8
      touch: true
  special:
  - favored enemy (any one +4)
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: magic circle against evil
    source: default
    freq: Constant
  - name: aid
    source: default
    freq: At will
  - name: continual flame
    source: default
    freq: At will
  - superscripts:
    - UM
    name: forbid action
    source: default
    freq: At will
    DC: 14
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: mage hand
    source: default
    freq: At will
  - name: message
    source: default
    freq: At will
  - name: calm emotions
    source: default
    freq: 1/day
    DC: 15
  - name: clairaudience/clairvoyance
    source: default
    freq: 1/day
  - name: commune
    source: default
    freq: 1/day
    CL: 9
    other: 1 question
  - name: daylight
    source: default
    freq: 1/day
  - name: silence
    source: default
    freq: 1/day
    DC: 15
  sources:
  - name: default
    CL: 5
    concentration: 8
ability_scores:
  STR: 15
  DEX: 16
  CON: 18
  INT: 17
  WIS: 15
  CHA: 16
BAB: 5
CMB: 7
CMD: 20
feats:
- name: Iron Will
- name: Point-Blank Shot
- name: Skill Focus (Knowledge [any one])
skills:
  Craft (bookbinding): 11
  Diplomacy: 11
  Disable Device: 11
  Knowledge (any one): 14
  Linguistics: 11
  Perception: 10
  Sense Motive: 10
  Spellcraft: 11
  Survival: 10
languages:
- Celestial
- Draconic
- Infernal
- any 5 others
- truespeech
special_qualities:
- codex
ecology:
  environment: any (Heaven)
  organization: solitary, pair, or team (2-8)
  treasure_type: standard
special_abilities:
  Codex (Su): Each codex archon is also an actual codex. Within its pages, the codex
    archon details all that the archon has ever learned on its chosen topic. When
    a favored enemy of the codex archon is forced to attempt a saving throw against
    the archon's spells, the foe takes a penalty on the saving throw equal to half
    the codex archon's favored enemy bonus (-2 for most codex archons).
  Favored Enemy (Ex): A codex archon selects one favored enemy, as per the ranger
    class feature.
  Light Ray (Ex): A codex archon can fire a beam of light to damage foes. This light
    ray has a maximum range of 60 feet. This attack overcomes damage reduction of
    any type.
desc_long: |-
  A codex archon embodies Heavenly knowledge and the refinement of the mind. It serves in the libraries and archives of Heaven, and as keeper and carrier of records for Heaven's field armies. Codex archons seek out any opportunity to add to their formidable collections of information with zealous dedication, although they do not neglect to offer their insights to those they encounter who might use such knowledge for the greater good or for personal growth.

   Most codex archons specialize in a single subject, such as one plane of existence, one type of creature, or one aspect of mortal life. In general, each codex archon chooses a favored enemy and Knowledge skill closely linked to each other, such as humanoid (human) and Knowledge (local) or Knowledge (nobility). Although a codex archon's expertise allows it to more easily slay creatures of the type it studies, it usually prefers to avoid violence and uses its knowledge to coax more information out of creatures it meets. A spellcaster who calls or summons a codex archon can generally conjure one with whatever specialization she seeks unless the foe or topic is one that is little known to the forces of Heaven or an unorthodox combination (GM's discretion). Though they prefer their heavenly homes to the chaotic Material Plane, summoned codex archons may deign to serve for a time as assistants or even instructors in mortal libraries, academies, and temples.

---

# Archon, Codex Archon
This enormous book has wings of glowing light and an angelic figure on the cover that gazes out watchfully as though alive.
**Source** Monster _[[classes/Summoner|Summoner]]_'s Handbook pg. 24
**XP** 1,600

LG Medium outsider (archon, extraplanar, good, lawful)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Evil|detect evil]]_, _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +10
**Aura** aura of menace (DC 17), _[[spells/Magic Circle against Evil|magic circle against evil]]_

##### Defense

**AC** 20, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+3 Dex, +7 natural); +2 _[[spells/Deflection|deflection]]_ vs. evil
**hp** 47 (5d10+20)
**Fort** +7, **Ref** +7, **Will** +5; +4 vs. poison, +2 vs. evil
**DR** 10/evil; **Immune** electricity, petrification; **SR** 16

##### Offense
**Speed** fly 30 ft. (good)
**Melee** slam +7 (1d8+2)
**Ranged** light ray +8 ranged touch (1d6)
**Special Attacks** favored enemy (any one +4)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +8)
Constant—_detect evil_, _detect magic_, _magic circle against evil_
At will—aid, _[[spells/Continual Flame|continual flame]]_, _[[spells/Forbid Action|forbid action]]_ (DC 14), greater teleport (self plus 50 lbs. of objects only), _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_
1/day—_[[spells/Calm Emotions|calm emotions]]_ (DC 15), clairaudience/clairvoyance, _[[spells/Commune|commune]]_ (CL 9th, 1 question), _[[spells/Daylight|daylight]]_, _[[spells/Silence|silence]]_ (DC 15)

##### Statistics
**Str** 15, **Dex** 16, **Con** 18, **Int** 17, **Wis** 15, **Cha** 16
**Base Atk** +5; **CMB** +7; **CMD** 20
**Feats** _[[feats/Iron Will|Iron Will]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Skill Focus|Skill Focus]]_ (Knowledge [any one])
**Skills** Craft (bookbinding) +11, Diplomacy +11, Disable Device +11, Knowledge (any one) +14, Linguistics +11, Perception +10, Sense Motive +10, Spellcraft +11, Survival +10
**Languages** Celestial, Draconic, Infernal, any 5 others; truespeech
**SQ** codex

##### Ecology

**Environment** any (Heaven)
**Organization** solitary, pair, or team (2–8)
**Treasure** standard

### Special Abilities

**Codex (Su)** Each codex archon is also an actual codex. Within its pages, the codex archon details all that the archon has ever learned on its chosen topic. When a favored enemy of the codex archon is forced to attempt a saving throw against the archon’s spells, the foe takes a penalty on the saving throw equal to half the codex archon’s favored enemy bonus (–2 for most codex archons).

**Favored Enemy (Ex)** A codex archon selects one favored enemy, as per the _[[classes/Ranger|ranger]]_ class feature.

**Light Ray (Ex)** A codex archon can fire a beam of light to damage foes. This light ray has a maximum range of 60 feet. This attack overcomes _[[universal monster rules/Damage Reduction|damage reduction]]_ of any type.

##### Description

A codex archon embodies Heavenly knowledge and the refinement of the mind. It serves in the libraries and archives of Heaven, and as keeper and carrier of records for Heaven’s field armies. Codex archons seek out any opportunity to add to their formidable collections of information with zealous dedication, although they do not neglect to offer their insights to those they encounter who might use such knowledge for the greater good or for personal growth.

Most codex archons specialize in a single subject, such as one plane of existence, one type of creature, or one aspect of mortal life. In general, each codex archon chooses a favored enemy and Knowledge skill closely linked to each other, such as humanoid (human) and Knowledge (local) or Knowledge (nobility). Although a codex archon’s expertise allows it to more easily slay creatures of the type it studies, it usually prefers to avoid violence and uses its knowledge to coax more information out of creatures it meets. A spellcaster who calls or summons a codex archon can generally conjure one with whatever specialization she seeks unless the foe or topic is one that is little known to the forces of Heaven or an unorthodox combination (GM’s discretion). Though they prefer their heavenly homes to the chaotic Material Plane, summoned codex archons may deign to serve for a time as assistants or even instructors in mortal libraries, academies, and temples.
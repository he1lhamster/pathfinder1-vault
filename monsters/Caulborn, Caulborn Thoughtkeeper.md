---
cssclass: [monsters]
title1: Caulborn, Caulborn Thoughtkeeper
desc_short: This humanoid creature has two mouths in its eyeless head, one small and
  human, the other split into terrifying jaws.
title2: Caulborn Thoughtkeeper
CR: 9
sources:
- name: Occult Bestiary
  page: 12
  link: http://paizo.com/products/btpy9g21?Pathfinder-Campaign-Setting-Occult-Bestiary
XP: 6400
alignment: N
size: Medium
type: outsider
subtypes:
- extraplanar
initiative:
  bonus: 9
senses:
  blindsense: 60
  darkvision: 60
  thoughtsense: 60
AC:
  AC: 22
  touch: 21
  flat_footed: 17
  components:
    deflection: 6
    dex: 5
    natural: 1
HP:
  HP: 115
  long: 9d10+44
saves:
  fort: 7
  ref: 8
  will: 15
  other: +4 vs. psychic spells
defensive_abilities:
- psychic deflection
- psychic resilience
immunities:
- visual effects
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +17 (2d6+5)
      entries:
      - - damage: 2d6+5
      attack: bite
      bonus:
      - 17
    - text: 2 claws +16 (1d6+5)
      entries:
      - - damage: 1d6+5
      count: 2
      attack: claws
      bonus:
      - 16
  special:
  - consume thoughts (DC 21)
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: Constant
    DC: 18
  - name: read magic
    source: default
    freq: Constant
  - name: charm monster
    source: default
    freq: 3/day
    DC: 19
  - name: daze monster
    source: default
    freq: 3/day
    DC: 17
  - name: hold monster
    source: default
    freq: 3/day
    DC: 20
  - name: hypnotic pattern
    source: default
    freq: 3/day
    DC: 18
  - name: vampiric touch
    source: default
    freq: 3/day
  - name: plane shift
    source: default
    freq: 1/week
    other: willing targets only
  sources:
  - name: default
    CL: 9
    concentration: 15
psychic_magic:
  entries:
  - superscripts:
    - OA
    name: burst of insight
    PE: 1
  - superscripts:
    - OA
    name: emotive block
    PE: 3
    DC: 19
  - superscripts:
    - OA
    name: greater oneiric horror
    PE: 4
    DC: 20
  - superscripts:
    - OA
    name: mind thrust III
    PE: 3
    DC: 19
  - superscripts:
    - OA
    name: mindscape door
    PE: 3
    DC: 19
  - superscripts:
    - OA
    name: mindwipe
    PE: 4
    DC: 20
  - superscripts:
    - OA
    name: telekinetic maneuver
    PE: 3
  sources:
  - name: default
    CL: 9
    concentration: 15
  PE: 10
ability_scores:
  STR: 20
  DEX: 21
  CON: 18
  INT: 31
  WIS: 22
  CHA: 23
BAB: 11
CMB: 16
CMD: 37
feats:
- name: Combat Casting
- name: Combat Expertise
- name: Combat Reflexes
- name: Improved Initiative
- name: Iron Will
- name: Weapon Focus (bite)
skills:
  Acrobatics: 15
  Appraise: 20
  Bluff: 20
  Intimidate: 19
  Knowledge (all): 20
  Perception: 20
  Sense Motive: 20
  Stealth: 16
  Use Magic Device: 14
languages:
- Abyssal
- Aklo
- Aquan
- Celestial
- Common
- Draconic
- Giant
- Infernal
- Sylvan
- Terran
- Undercommon
- telepathy 100 ft.
special_qualities:
- caulborn traits
- cooperative scrying
- hive mind
ecology:
  environment: any
  organization: solitary, pair, or cabal (3-6)
  treasure_type: double
special_abilities:
  Caulborn Traits: A caulborn thoughtkeeper shares the abilities of regular caulborn
    (Pathfinder RPG Bestiary 3 48)-consume thoughts, cooperative scrying, hive mind,
    psychic deflection, and thoughtsense-which function as normal except as noted.
    If all caulborn participating in a cooperative scrying are thoughtkeepers, the
    save DC increases by 2.
desc_long: |-
  Planar scholars who subsist on the physic energy of other races, the telepathic caulborn wander the planes, storing both sustenance and information in their hives' massive brain-sacs, which are called chrestomaths. These latter entities act as living libraries, containing within them a communal racial memory spanning eons.

  While caulborn's similar appearance and hive mind lead most other intelligent races to assume all of the caulborn's humanoid individuals are identical, their race still has a certain degree of specialization. The more powerful variant known to outsiders as caulborn thoughtkeepers are a prime example of this differentiation. With their advanced psychic powers and combat abilities, these elite individuals range farthest from the hive in their search for esoteric knowledge, or directly guard and care for their hive's chrestomath. Yet while this might seem like a case of the most important jobs going to the most powerful individuals, the truth is in fact the opposite: subsisting on the best psychic energy or remaining in closest proximity to the intense volume of thoughts that constantly passes through a chrestomath empowers individual caulborn, allowing them to grow into full thoughtkeeper status. Physically, thoughtkeepers resemble other caulborn-they bear no special markings or badges of office, and in fact are treated no differently by their peers outside of their utilization, as within the hive mind they're simply seen as stronger appendages of the same greater being.

  On Golarion, caulborn thoughtkeepers are most reliably found deep beneath Kaer Maga in the city of Xavorax, communing with Anamnesis, the hive's resident chrestomath.

---

# Caulborn, Caulborn Thoughtkeeper
This humanoid creature has two mouths in its eyeless head, one small and human, the other _[[universal monster rules/Split|split]]_ into terrifying jaws.
**Source** Occult Bestiary pg. 12
**XP** 6,400

N Medium outsider (extraplanar)
**Init** +9; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 60 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Thoughtsense|thoughtsense]]_ 60 ft.; Perception +20

##### Defense

**AC** 22, touch 21, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+6 _[[spells/Deflection|deflection]]_, +5 Dex, +1 natural)
**hp** 115 (9d10+44)
**Fort** +7, **Ref** +8, **Will** +15; +4 vs. _[[classes/Psychic|psychic]]_ spells
**Defensive Abilities** _psychic_ _deflection_, _[[universal monster rules/Psychic Resilience|psychic resilience]]_; **Immune** visual effects

##### Offense
**Speed** 30 ft.
**Melee** bite +17 (2d6+5), 2 claws +16 (1d6+5)
**Special Attacks** consume thoughts (DC 21)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +15)
Constant—_[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 18), _[[spells/Read Magic|read magic]]_
3/day—_[[spells/Charm Monster|charm monster]]_ (DC 19), _[[spells/Daze Monster|daze monster]]_ (DC 17), _[[spells/Hold Monster|hold monster]]_ (DC 20), _[[spells/Hypnotic Pattern|hypnotic pattern]]_ (DC 18), _[[spells/Vampiric Touch|vampiric touch]]_
1/week—_[[spells/Plane Shift|plane shift]]_ (willing targets only)
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_ **(CL 9th; concentration +15)
10 PE—_[[spells/Burst Of Insight|burst of insight]]_ (1 PE), _[[spells/Emotive Block|emotive block]]_ (3 PE, DC 19), greater _[[spells/Oneiric Horror|oneiric horror]]_ (4 PE, DC 20), _[[spells/Mind Thrust III|mind thrust III]]_ (3 PE, DC 19), _[[spells/Mindscape Door|mindscape door]]_ (3 PE, DC 19), _[[spells/Mindwipe|mindwipe]]_ (4 PE, DC 20), _[[spells/Telekinetic Maneuver|telekinetic maneuver]]_ (3 PE)

##### Statistics
**Str** 20, **Dex** 21, **Con** 18, **Int** 31, **Wis** 22, **Cha** 23
**Base Atk** +11; **CMB** +16; **CMD** 37
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Acrobatics +15, Appraise +20, Bluff +20, Intimidate +19, Knowledge (all) +20, Perception +20, Sense Motive +20, Stealth +16, Use Magic Device +14
**Languages** Abyssal, Aklo, Aquan, Celestial, Common, Draconic, Giant, Infernal, Sylvan, Terran, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[monsters/Caulborn|caulborn]]_ traits, cooperative _[[spells/Scrying|scrying]]_, hive mind

##### Ecology

**Environment** any
**Organization** solitary, pair, or cabal (3–6)
**Treasure** double

### Special Abilities

**_Caulborn_ Traits** A _caulborn_ thoughtkeeper shares the abilities of regular _caulborn_ (Pathfinder RPG Bestiary 3 48)—consume thoughts, cooperative _scrying_, hive mind, _psychic_ _deflection_, and _thoughtsense_—which function as normal except as noted. If all _caulborn_ participating in a cooperative _scrying_ are thoughtkeepers, the save DC increases by 2.

##### Description

_[[items/Weapon Magic Abilities/Planar|Planar]]_ scholars who subsist on the physic energy of other races, the telepathic _caulborn_ wander the planes, storing both sustenance and information in their hives’ massive brain-sacs, which are _[[items/Weapon Magic Abilities/Called|called]]_ chrestomaths. These latter entities act as living libraries, containing within them a communal racial memory spanning eons.

While _caulborn_’s similar appearance and hive mind lead most other intelligent races to assume all of the _caulborn_’s humanoid individuals are identical, their race still has a certain degree of specialization. The more powerful variant known to outsiders as _caulborn_ thoughtkeepers are a prime example of this differentiation. With their advanced _psychic_ powers and combat abilities, these elite individuals range farthest from the hive in their search for esoteric knowledge, or directly _[[npcs/Guard|guard]]_ and care for their hive’s chrestomath. Yet while this might seem like a case of the most important jobs going to the most powerful individuals, the truth is in fact the opposite: subsisting on the best _psychic_ energy or remaining in closest proximity to the intense volume of thoughts that constantly passes through a chrestomath empowers individual _caulborn_, allowing them to grow into full thoughtkeeper _[[spells/Status|status]]_. Physically, thoughtkeepers resemble other _caulborn_—they bear no special markings or badges of office, and in fact are treated no differently by their peers outside of their utilization, as within the hive mind they’re simply seen as stronger appendages of the same greater being.

On Golarion, _caulborn_ thoughtkeepers are most reliably found deep beneath Kaer Maga in the city of Xavorax, communing with Anamnesis, the hive’s resident chrestomath.
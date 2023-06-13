---
cssclass: [monsters]
title1: Cervine Protector
title2: Cervine Protector
CR: 6
sources:
- name: Heaven Unleashed
  page: 44
  link: http://paizo.com/products/btpy9jbd?Pathfinder-Campaign-Setting-Heaven-Unleashed
XP: 2400
alignment: LG
size: Large
type: outsider
subtypes:
- extraplanar
- good
- lawful
initiative:
  bonus: 2
senses:
  darkvision: 60
AC:
  AC: 19
  touch: 11
  flat_footed: 17
  components:
    dex: 2
    natural: 8
    size: -1
HP:
  HP: 76
  long: 8d10+32
saves:
  fort: 10
  ref: 4
  will: 9
  other: +2 vs. poison
DR:
- amount: 5
  weakness: evil
immunities:
- electricity
- petrification
resistances:
  cold: 10
  sonic: 10
SR: 17
speeds:
  base: 40
attacks:
  melee:
  - - text: gore +14 (1d8+6 plus push)
      entries:
      - - damage: 1d8+6
        - effect: push
      attack: gore
      bonus:
      - 14
    - text: 2 hooves +8 (1d6+3)
      entries:
      - - damage: 1d6+3
      count: 2
      attack: hooves
      bonus:
      - 8
  special:
  - push (gore, 10 ft.)
  - trample (1d6+9, DC 20)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: speak with animals
    source: default
    freq: Constant
  - name: detect evil
    source: default
    freq: At will
  - name: cure moderate wounds
    source: default
    freq: 3/day
  - name: neutralize poison
    source: default
    freq: 1/day
  - name: plant growth
    source: default
    freq: 1/day
  - name: remove disease
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 8
    concentration: 8
ability_scores:
  STR: 22
  DEX: 15
  CON: 18
  INT: 12
  WIS: 13
  CHA: 11
BAB: 8
CMB: 15
CMB_other: +17 bull rush
CMD: 27
CMD_other: 29 vs. bull rush, 31 vs. trip
feats:
- name: Improved Bull Rush
- name: Iron Will
- name: Power Attack
- name: Weapon Focus (gore)
skills:
  Acrobatics: 9
    when jumping: 13
  Handle Animal: 11
  Intimidate: 8
  Knowledge (nature): 12
  Perception: 12
  Sense Motive: 12
  Stealth: 5
    in forests: 13
  Survival: 12
  _racial_mods:
    Stealth:
      in forests: 8
languages:
- Celestial
- Draconic
- Druidic
- Infernal
- speak with animals
special_qualities:
- fertile regeneration
ecology:
  environment: any (Heaven)
  organization: single, solitary, or bulwark (3-6)
  treasure_type: standard
special_abilities:
  Fertile Regeneration (Su): Once per day, if the cervine protector is in the area
    of a plant growth spell used to generate overgrowth at the time the spell is cast,
    it gains fast healing 5 for 10 minutes. The cervine protector maintains the fast
    healing even if it leaves the affected area. This effect ends immediately if the
    cervine protector is in the area of a diminish plants spell used to prune growth.
desc_long: |-
  A cervine protector might be encountered alongside the Grim White Stag, or as the companion of one of Erastil's clergy. In natural settings sacred to Erastil, solitary cervine protectors sometimes stand vigil, ensuring that no taint befalls their charge.

   Characters with the Leadership feat can take a cervine protector as a cohort at cohort level 10th or higher.

---

# Cervine Protector

**Source** Heaven Unleashed pg. 44
**XP** 2,400

LG Large outsider (extraplanar, good, lawful)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +12

##### Defense

**AC** 19, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+2 Dex, +8 natural, –1 size)
**hp** 76 (8d10+32)
**Fort** +10, **Ref** +4, **Will** +9; +2 vs. poison
**DR** 5/evil; **Immune** electricity, petrification; **Resist** cold 10, sonic 10; **SR** 17

##### Offense
**Speed** 40 ft.
**Melee** gore +14 (1d8+6 plus push), 2 hooves +8 (1d6+3)
**Space** 10 ft., **Reach** 10 ft,
**Special Attacks** push (gore, 10 ft.), _[[universal monster rules/Trample|trample]]_ (1d6+9, DC 20)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +8)
Constant—speak with animalsAt will—detect evil3/day—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_ 1/day—_[[spells/Neutralize Poison|neutralize poison]]_, _[[spells/Plant Growth|plant growth]]_, _[[spells/Remove Disease|remove disease]]_

##### Statistics
**Str** 22, **Dex** 15, **Con** 18, **Int** 12, **Wis** 13, **Cha** 11
**Base Atk** +8; **CMB** +15 (+17 bull rush); **CMD** 27 (29 vs. bull rush, 31 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (gore)
**Skills** Acrobatics +9 (+13 when jumping), Handle Animal +11, Intimidate +8, Knowledge (nature) +12, Perception +12, Sense Motive +12, Stealth +5 (+13 in forests), Survival +12; **Racial Modifiers** +8 Stealth in forests
**Languages** Celestial, Draconic, Druidic, Infernal; _[[spells/Speak with Animals|speak with animals]]_
**SQ** fertile _[[universal monster rules/Regeneration|regeneration]]_

##### Ecology

**Environment** any (Heaven)
**Organization** single, solitary, or bulwark (3–6)
**Treasure** standard

### Special Abilities

**Fertile _Regeneration_ (Su)** Once per day, if the _[[monsters/Cervine Protector|cervine protector]]_ is in the area of a _plant growth_ spell used to generate overgrowth at the time the spell is cast, it gains _[[universal monster rules/Fast Healing|fast healing]]_ 5 for 10 minutes. The _cervine protector_ maintains the _fast healing_ even if it leaves the affected area. This effect ends immediately if the _cervine protector_ is in the area of a _[[spells/Diminish Plants|diminish plants]]_ spell used to prune growth.

##### Description

A _cervine protector_ might be encountered alongside the Grim White Stag, or as the companion of one of Erastil’s clergy. In natural settings _[[items/Weapon Magic Abilities/Sacred|sacred]]_ to Erastil, solitary cervine protectors sometimes stand vigil, ensuring that no taint befalls their charge.

Characters with the _[[feats/Leadership|Leadership]]_ feat can take a _cervine protector_ as a cohort at cohort level 10th or higher.
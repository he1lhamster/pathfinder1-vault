---
cssclass: [monsters]
title1: Peri
desc_short: This beautiful albino woman is wreathed in wings of brilliant flame.
title2: Peri
CR: 14
sources:
- name: Bestiary 3
  page: 218
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 38400
alignment: NG
size: Medium
type: outsider
subtypes:
- good
- native
initiative:
  bonus: 7
senses:
  darkvision: 60
  low-light vision: true
  smoke sight: true
AC:
  AC: 30
  touch: 18
  flat_footed: 22
  components:
    dex: 7
    dodge: 1
    natural: 12
HP:
  HP: 180
  long: 19d10+76
saves:
  fort: 12
  ref: 18
  will: 17
DR:
- amount: 10
  weakness: cold iron and evil
immunities:
- electricity
- fire
resistances:
  acid: 10
  cold: 10
SR: 25
speeds:
  base: 30
  fly: 90
  fly_maneuverability: good
attacks:
  melee:
  - - text: +2 flaming burst scimitar +27/+22/+17/+12 (1d6+11/18-20 plus 1d6 fire)
      entries:
      - - damage: 1d6+11
          crit_range: 18-20
        - damage: 1d6
          type: fire
      attack: +2 flaming burst scimitar
      bonus:
      - 27
      - 22
      - 17
      - 12
    - text: 2 wings +20 (1d6+3 plus burn)
      entries:
      - - damage: 1d6+3
        - effect: burn
      count: 2
      attack: wings
      bonus:
      - 20
  special:
  - burn (2d6, DC 23)
  - whirlwind dance
spell_like_abilities:
  entries:
  - name: fire shield
    source: default
    freq: Constant
    other: warm shield
  - name: aid
    source: default
    freq: At will
  - name: flame jump
    source: default
    freq: At will
  - name: pyrotechnics
    source: default
    freq: At will
    DC: 20
  - name: scorching ray
    source: default
    freq: At will
  - name: fireball
    source: default
    freq: 3/day
    DC: 21
  - name: flame strike
    source: default
    freq: 3/day
    DC: 23
  - name: wall of fire
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 15
    concentration: 23
ability_scores:
  STR: 22
  DEX: 24
  CON: 19
  INT: 21
  WIS: 19
  CHA: 26
BAB: 19
CMB: 25
CMD: 43
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Dodge
- name: Great Fortitude
- name: Improved Disarm
- name: Iron Will
- name: Mobility
- name: Power Attack
- name: Spring Attack
- name: Whirlwind Attack
skills:
  Acrobatics: 29
  Diplomacy: 30
  Fly: 33
  Heal: 23
  Knowledge (planes): 27
  Knowledge (religion): 24
  Perception: 26
  Perform (any one): 30
  Sense Motive: 26
  Spellcraft: 27
  Stealth: 29
languages:
- Celestial
- Common
- Draconic
- Elven
- Ignan
- telepathy 100 ft.
ecology:
  environment: any good-aligned plane
  organization: solitary or pair
  treasure_type: triple
  treasure:
  - +2 flaming burst scimitar
  - other treasure
special_abilities:
  Flame Jump (Sp): A peri can enter any fire equal to the peri's size or larger and
    travel any distance to another fire in a single round, regardless of the distance
    between the two. This ability otherwise functions as greater teleport (caster
    level 14th), but the peri can transport only itself and up to 50 pounds of objects.
  Smoke Sight (Su): A peri can see through fire, fog, and smoke without penalty.
  Whirlwind Dance (Su): Once per day as a full-round action, a peri can spin in an
    ever-faster, whirling dance, transforming itself into a spinning vortex of flame
    10 to 40 feet high for up to 9 rounds. This ability functions as the whirlwind
    ability (DC 26 Reflex save), but any creature that comes in contact with the whirlwind
    or is caught inside it takes 2d6+6 points of fire damage and is subject to the
    peri's burn special attack. The save DC is Dexterity-based.
desc_long: |-
  Peris are a race of celestials native to the good-aligned Outer Planes, but they are also often found in the company of mortals on the Material Plane. Believed to be the descendants of fallen angels, peris do penance for their ancestors' sins before they can earn a place in paradise. As a result, peris work tirelessly to aid and support good heroes of the mortal realms in a never-ending battle against evil.

  Peris hate the evil fiends known as divs, who constantly seek to ruin the good works of mortals. Peris often work to repair damage wrought by the destructive divs. For their part, the divs take great pleasure in tormenting and persecuting peris, locking the fiery-winged celestials in cages of cold iron and endlessly torturing them.

---

# Peri
This beautiful albino woman is wreathed in wings of brilliant flame.
**Source** Bestiary 3 pg. 218
**XP** 38,400

NG Medium outsider (good, native)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, smoke sight; Perception +26

##### Defense

**AC** 30, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+7 Dex, +1 _[[feats/Dodge|dodge]]_, +12 natural)
**hp** 180 (19d10+76)
**Fort** +12, **Ref** +18, **Will** +17
**DR** 10/cold iron and evil; **Immune** electricity, fire; **Resist** acid 10, cold 10; **SR** 25

##### Offense
**Speed** 30 ft., fly 90 ft. (good)
**Melee** +2 _[[items/Weapon Magic Abilities/Flaming Burst|flaming burst]]_ _[[items/Weapon/Scimitar|scimitar]]_ +27/+22/+17/+12 (1d6+11/18–20 plus 1d6 fire), 2 wings +20 (1d6+3 plus _[[universal monster rules/Burn|burn]]_)
**Special Attacks** _burn_ (2d6, DC 23), _[[universal monster rules/Whirlwind|whirlwind]]_ dance
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +23)
Constant—_[[spells/Fire Shield|fire shield]]_ (warm _[[spells/Shield|shield]]_)
At will—aid, flame _[[spells/Jump|jump]]_, _[[spells/Pyrotechnics|pyrotechnics]]_ (DC 20), _[[spells/Scorching Ray|scorching ray]]_
3/day—_[[spells/Fireball|fireball]]_ (DC 21), _[[spells/Flame Strike|flame strike]]_ (DC 23), _[[spells/Wall Of Fire|wall of fire]]_

##### Statistics
**Str** 22, **Dex** 24, **Con** 19, **Int** 21, **Wis** 19, **Cha** 26
**Base Atk** +19; **CMB** +25; **CMD** 43
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Whirlwind Attack|Whirlwind Attack]]_
**Skills** Acrobatics +29, Diplomacy +30, Fly +33, _[[spells/Heal|Heal]]_ +23, Knowledge (planes) +27, Knowledge (religion) +24, Perception +26, Perform (any one) +30, Sense Motive +26, Spellcraft +27, Stealth +29
**Languages** Celestial, Common, Draconic, Elven, Ignan; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any good-aligned plane
**Organization** solitary or pair
**Treasure** triple (+2 _flaming burst_ _scimitar_, other treasure)

### Special Abilities

**Flame _Jump_ (Sp)** A _[[monsters/Peri|peri]]_ can enter any fire equal to the _peri_’s size or larger and travel any distance to another fire in a single round, regardless of the distance between the two. This ability otherwise functions as greater teleport (caster level 14th), but the _peri_ can transport only itself and up to 50 pounds of objects.
**Smoke Sight (Su)** A _peri_ can see through fire, fog, and smoke without penalty.

**_Whirlwind_ Dance (Su) **Once per day as a full-round action, a _peri_ can spin in an ever-faster, whirling dance, transforming itself into a spinning _[[spells/Vortex|vortex]]_ of flame 10 to 40 feet high for up to 9 rounds. This ability functions as the _whirlwind_ ability (DC 26 Reflex save), but any creature that comes in contact with the _whirlwind_ or is caught inside it takes 2d6+6 points of fire damage and is subject to the _peri_’s _burn_ special attack. The save DC is Dexterity-based.

##### Description

Peris are a race of celestials native to the good-aligned Outer Planes, but they are also often found in the company of mortals on the Material Plane. Believed to be the descendants of _[[monsters/Fallen|fallen]]_ angels, peris do penance for their ancestors’ sins before they can earn a place in paradise. As a result, peris work tirelessly to aid and support good heroes of the mortal realms in a never-ending battle against evil.

Peris hate the evil fiends known as divs, who constantly seek to ruin the good works of mortals. Peris often work to repair damage wrought by the destructive divs. For their part, the divs take great pleasure in tormenting and persecuting peris, locking the fiery-winged celestials in cages of cold iron and endlessly torturing them.
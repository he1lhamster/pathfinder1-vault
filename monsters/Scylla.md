---
cssclass: [monsters]
title1: Scylla
desc_short: This horrifying creature has the upper body of a beautiful woman, but
  a lower body of snapping wolf heads and writhing tentacles.
title2: Scylla
CR: 16
sources:
- name: Bestiary 2
  page: 241
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 76800
alignment: CE
size: Huge
type: aberration
subtypes:
- aquatic
initiative:
  bonus: 11
senses:
  all-around vision: true
  blindsight: 30
  darkvision: 60
  low-light vision: true
  see invisibility: true
auras:
- name: frightful presence (30 ft., DC 26),
AC:
  AC: 30
  touch: 20
  flat_footed: 18
  components:
    dex: 11
    dodge: 1
    natural: 10
    size: -2
HP:
  HP: 250
  long: 20d8+160
  fast_healing: 10
saves:
  fort: 14
  ref: 17
  will: 18
defensive_abilities:
- freedom of movement
- improved evasion
DR:
- amount: 10
  weakness: cold iron and lawful
immunities:
- cold
- charm effects
- confusion and insanity effects
resistances:
  acid: 20
  fire: 20
SR: 27
speeds:
  base: 30
  swim: 50
attacks:
  melee:
  - - text: 4 bites +25 (1d8+8/19-20 plus bleed)
      entries:
      - - damage: 1d8+8
          crit_range: 19-20
        - effect: bleed
      count: 4
      attack: bites
      bonus:
      - 25
    - text: 4 tentacles +23 (1d6+4 plus grab)
      entries:
      - - damage: 1d6+4
        - effect: grab
      count: 4
      attack: tentacles
      bonus:
      - 23
  special:
  - bleed (1d6)
  - constrict (1d6+8)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: freedom of movement
    source: default
    freq: Constant
  - name: nondetection
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: acid arrow
    source: default
    freq: At will
  - name: control water
    source: default
    freq: At will
  - name: fog cloud
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: major image
    source: default
    freq: At will
    DC: 19
  - name: black tentacles
    source: default
    freq: 3/day
  - name: charm monster
    source: default
    freq: 3/day
    DC: 20
  - name: insanity
    source: default
    freq: 3/day
    DC: 23
  - name: mirage arcana
    source: default
    freq: 3/day
    DC: 21
  - name: solid fog
    source: default
    freq: 3/day
  - name: control weather
    source: default
    freq: 1/day
  - name: power word stun
    source: default
    freq: 1/day
  - name: project image
    source: default
    freq: 1/day
    DC: 23
  - name: summon
    source: default
    freq: 1/day
    level: 8
    summons:
    - name: charybdis
      amount: 1
  sources:
  - name: default
    CL: 16
    concentration: 22
ability_scores:
  STR: 27
  DEX: 32
  CON: 27
  INT: 20
  WIS: 23
  CHA: 22
BAB: 15
CMB: 25
CMB_other: +29 grapple
CMD: 47
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Dodge
- name: Improved Critical (bite)
- name: Mobility
- name: Multiattack
- name: Power Attack
- name: Vital Strike
- name: Weapon Finesse
- name: Weapon Focus (bite)
- name: Weapon Focus (tentacles)
skills:
  Acrobatics: 34
  Bluff: 26
  Knowledge (nature): 25
  Intimidate: 29
  Perception: 29
  Sense Motive: 26
  Stealth: 26
  Swim: 39
  Use Magic Device: 26
languages:
- Abyssal
- Aquan
- Common
special_qualities:
- amphibious
- change shape (1 humanoid form, alter self)
- undersized weapons
ecology:
  environment: any water
  organization: solitary
  treasure_type: triple
desc_long: |-
  The scylla is one of the more nightmarish aberrations to blight the mortal world. Conflicting tales of her origins abound, from demonic flesh-crafting and arcane experiments to a divine curse handed down by a vengeful deity. The most popular stories cast the first scylla as the monstrous spawn of a union between a mortal and a god. Whatever the case, scyllas are fortunately quite rare, enough so that many consider them nothing more than tall tales told by sailors deep in their cups.

  Scyllas dwell along major shipping lanes, often near coastlines, where they use their spell-like abilities to lure entire ships to their doom. The hideous monsters are intelligent creatures, though half-mad with hunger and self-loathing. They normally do not use weapons, but when they do, they prefer to fight with light weapons wielded by their human-sized upper arms. However, they much prefer to keep their hands free to utilize magic items like wands, staves, and other powerful devices.

---

# Scylla
This horrifying creature has the upper body of a beautiful woman, but a lower body of snapping _[[monsters/Wolf|wolf]]_ heads and writhing tentacles.
**Source** Bestiary 2 pg. 241
**XP** 76,800
CE Huge aberration (aquatic)
**Init** +11; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[universal monster rules/Blindsight|blindsight]]_ 30 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +29
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (30 ft., DC 26),

##### Defense

**AC** 30, touch 20, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+11 Dex, +1 dodge, +10 natural, –2 size)
**hp** 250 (20d8+160); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +14, **Ref** +17, **Will** +18
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_, improved evasion; **DR** 10/cold iron and lawful; **Immune** cold, charm effects, _[[spells/Confusion|confusion]]_ and _[[spells/Insanity|insanity]]_ effects; **Resist** acid 20, fire 20; **SR** 27

##### Offense
**Speed** 30 ft., swim 50 ft.
**Melee** 4 bites +25 (1d8+8/19–20 plus _[[universal monster rules/Bleed|bleed]]_), 4 tentacles +23 (1d6+4 plus _[[universal monster rules/Grab|grab]]_)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _bleed_ (1d6), _[[universal monster rules/Constrict|constrict]]_ (1d6+8)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +22)
Constant—_freedom of movement_, _[[spells/Nondetection|nondetection]]_, _see invisibility_
At will—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Control Water|control water]]_, _[[spells/Fog Cloud|fog cloud]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Major Image|major image]]_ (DC 19)
3/day—_[[spells/Black Tentacles|black tentacles]]_, _[[spells/Charm Monster|charm monster]]_ (DC 20), _insanity_ (DC 23), _[[spells/Mirage Arcana|mirage arcana]]_ (DC 21), _[[spells/Solid Fog|solid fog]]_
1/day—_[[spells/Control Weather|control weather]]_, _[[spells/Power Word Stun|power word stun]]_, _[[spells/Project Image|project image]]_ (DC 23), _[[universal monster rules/Summon|summon]]_ (level 8, 1 _[[monsters/Charybdis|charybdis]]_)

##### Statistics
**Str** 27, **Dex** 32, **Con** 27, **Int** 20, **Wis** 23, **Cha** 22
**Base Atk** +15; **CMB** +25 (+29 grapple); **CMD** 47 (can’t be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Mobility|Mobility]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite), _Weapon Focus_ (tentacles)
**Skills** Acrobatics +34, Bluff +26, Knowledge (nature) +25, Intimidate +29, Perception +29, Sense Motive +26, Stealth +26, Swim +39, Use Magic Device +26
**Languages** Abyssal, Aquan, Common
**SQ** _[[universal monster rules/Amphibious|amphibious]]_, _[[universal monster rules/Change Shape|change shape]]_ (1 humanoid form, _[[spells/Alter Self|alter self]]_), _[[universal monster rules/Undersized Weapons|undersized weapons]]_

##### Ecology

**Environment** any water
**Organization** solitary
**Treasure** triple

##### Description

The _[[monsters/Scylla|scylla]]_ is one of the more nightmarish aberrations to _[[spells/Blight|blight]]_ the mortal world. Conflicting tales of her origins abound, from demonic flesh-crafting and arcane experiments to a divine curse handed down by a vengeful deity. The most popular stories cast the first _scylla_ as the monstrous spawn of a union between a mortal and a god. Whatever the case, scyllas are fortunately quite rare, enough so that many consider them nothing more than tall tales told by sailors deep in their cups.

Scyllas dwell along major shipping lanes, often near coastlines, where they use their _spell-like abilities_ to lure entire ships to their _[[spells/Doom|doom]]_. The hideous monsters are intelligent creatures, though half-mad with hunger and self-loathing. They normally do not use weapons, but when they do, they prefer to fight with light weapons wielded by their human-sized upper arms. However, they much prefer to keep their hands free to utilize magic items like wands, staves, and other powerful devices.
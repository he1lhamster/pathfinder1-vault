---
cssclass: [monsters]
title1: Devil, Ice Devil (Gelugon)
desc_short: A pair of frozen, multifaceted eyes coldly judge all before this towering,
  insectile monstrosity.
title2: Ice Devil (Gelugon)
CR: 13
sources:
- name: Pathfinder RPG Bestiary
  page: 77
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 25600
alignment: LE
size: Large
type: outsider
subtypes:
- devil
- evil
- extraplanar
- lawful
initiative:
  bonus: 9
senses:
  darkvision: 60
  see in darkness: true
auras:
- name: fear
  radius: 10
  DC: 22
AC:
  AC: 32
  touch: 14
  flat_footed: 27
  components:
    dex: 5
    natural: 18
    size: -1
HP:
  HP: 161
  long: 14d10+84
  regeneration: 5
  regeneration_weakness: good weapons, good spells
saves:
  fort: 15
  ref: 14
  will: 12
DR:
- amount: 10
  weakness: good
immunities:
- fire
- cold
- poison
resistances:
  acid: 10
SR: 24
speeds:
  base: 40
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: +1 frost spear +21/+16/+11 (2d6+10/×3 plus 1d6 cold plus slow)
      entries:
      - - damage: 2d6+10
          crit_multiplier: 3
        - damage: 1d6
          type: cold
        - effect: slow
      attack: +1 frost spear
      bonus:
      - 21
      - 16
      - 11
    - text: bite +14 (2d6+6)
      entries:
      - - damage: 2d6+6
      attack: bite
      bonus:
      - 14
    - text: tail +14 (3d6+3 plus slow)
      entries:
      - - damage: 3d6+3
        - effect: slow
      attack: tail
      bonus:
      - 14
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: fly
    source: default
    freq: Constant
  - name: cone of cold
    source: default
    freq: At will
    DC: 20
  - name: ice storm
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: persistent image
    source: default
    freq: At will
    DC: 20
  - name: wall of ice
    source: default
    freq: At will
    DC: 19
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: bone devils
      amount: 2
      chance: 50%
  sources:
  - name: default
    CL: 13
ability_scores:
  STR: 23
  DEX: 21
  CON: 22
  INT: 25
  WIS: 22
  CHA: 20
BAB: 14
CMB: 21
CMD: 36
feats:
- name: Alertness
- name: Cleave
- name: Combat Reflexes
- name: Improved Initiative
- name: Iron Will
- name: Power Attack
- name: Weapon Focus (spear)
skills:
  Acrobatics: 22
  Bluff: 22
  Diplomacy: 22
  Fly: 13
  Intimidate: 19
  Knowledge (planes): 24
  Knowledge (any three others): 21
  Perception: 27
  Sense Motive: 27
  Spellcraft: 21
  Stealth: 18
  Survival: 23
languages:
- Celestial
- Common
- Draconic
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Hell)
  organization: solitary, team (2-3), council (4-10), or contingent (1-3 ice devils,
    2-6 horned devils, and 1-4 bone devils)
  treasure_type: standard
  treasure:
  - +1 frost spear
  - other treasure
special_abilities:
  Slow (Su): A hit from an ice devil's tail or spear induces numbing cold. The opponent
    must succeed on a DC 23 Fortitude save or be affected as though by a slow spell
    for 1d6 rounds. This effect comes from the devil in the case of its weapon; it
    is not a quality possessed by the spear itself. The save DC is Constitution-based.
desc_long: |-
  It is said that each ice devil-known as gelugons among the ranks of devilkind-bears within its chest a stolen, frozen mortal heart, which allows it to make decisions free of all emotion. Born on the icy layer of Cocytus, Hell's seventh layer, most ice devils migrate to Caina, the eighth layer, where they plot world-damning machinations from courts of freezing steel. Although they are perhaps the most alien and monstrous in appearance of all devils, few breeds are accorded greater respect.

  In combat, a gelugon prefers to let its minions engage foes in melee so that it can hang back and appraise the foe's tactics, strengths, and weaknesses. The ice devil supports its minions with its spell-like abilities, always taking care to avoid impacting its minions in the area of effect of its spells-this not from any sense of camaraderie, only a cold and logical truth that its allies can survive longer in a fight if they are not exposed to friendly fire.

  Gelugons stand at 12 feet tall, and weigh approximately 700 pounds.

---

# Devil, Ice Devil (Gelugon)
A pair of frozen, multifaceted eyes coldly judge all before this towering, insectile monstrosity.
**Source** Pathfinder RPG Bestiary pg. 77
**XP** 25,600

LE Large outsider (devil, evil, extraplanar, lawful)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +27
**Aura** _[[universal monster rules/Fear|fear]]_ (10 ft., DC 22)

##### Defense

**AC** 32, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+5 Dex, +18 natural, –1 size)
**hp** 161 (14d10+84); _[[universal monster rules/Regeneration|regeneration]]_ 5 (good weapons, good spells)
**Fort** +15, **Ref** +14, **Will** +12
**DR** 10/good; **Immune** fire, cold, poison; **Resist** acid 10; **SR** 24

##### Offense
**Speed** 40 ft., fly 60 ft. (good)
**Melee** +1 frost _[[items/Weapon/Spear|spear]]_ +21/+16/+11 (2d6+10/×3 plus 1d6 cold plus _[[spells/Slow|slow]]_), bite +14 (2d6+6), tail +14 (3d6+3 plus _slow_)
**Space** 10 ft., **Reach** 10 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th)
Constant—fly
At will—_[[spells/Cone of Cold|cone of cold]]_ (DC 20), _[[spells/Ice Storm|ice storm]]_, greater teleport (self plus 50 lbs. of objects only), _[[spells/Persistent Image|persistent image]]_ (DC 20), _[[spells/Wall Of Ice|wall of ice]]_ (DC 19)
1/day—_[[universal monster rules/Summon|summon]]_ (level 4, 2 bone devils, 50%)

##### Statistics
**Str** 23, **Dex** 21, **Con** 22, **Int** 25, **Wis** 22, **Cha** 20
**Base Atk** +14; **CMB** +21; **CMD** 36
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_spear_)
**Skills** Acrobatics +22, Bluff +22, Diplomacy +22, Fly +13, Intimidate +19, Knowledge (planes) +24, Knowledge (any three others) +21, Perception +27, Sense Motive +27, Spellcraft +21, Stealth +18, Survival +23
**Languages** Celestial, Common, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Hell)
**Organization** solitary, team (2–3), council (4–10), or contingent (1–3 ice devils, 2–6 horned devils, and 1–4 bone devils)
**Treasure** standard (+1 frost _spear_, other treasure)

### Special Abilities
**_Slow_ (Su) **A hit from an ice devil’s tail or _spear_ induces numbing cold. The opponent must succeed on a DC 23 Fortitude save or be affected as though by a _slow_ spell for 1d6 rounds. This effect comes from the devil in the case of its weapon; it is not a quality possessed by the _spear_ itself. The save DC is Constitution-based.

##### Description

It is said that each ice devil—known as gelugons among the ranks of devilkind—bears within its chest a stolen, frozen mortal heart, which allows it to make decisions free of all emotion. Born on the icy layer of Cocytus, Hell’s seventh layer, most ice devils migrate to Caina, the eighth layer, where they plot world-damning machinations from courts of freezing steel. Although they are perhaps the most alien and monstrous in appearance of all devils, few breeds are accorded greater respect.

In combat, a gelugon prefers to let its minions engage foes in melee so that it can hang back and appraise the foe’s tactics, strengths, and weaknesses. The ice devil supports its minions with its _spell-like abilities_, always taking care to avoid impacting its minions in the area of effect of its spells—this not from any sense of camaraderie, only a cold and logical truth that its allies can survive longer in a fight if they are not exposed to _[[feats/Friendly Fire|friendly fire]]_.

Gelugons stand at 12 feet tall, and weigh approximately 700 pounds.
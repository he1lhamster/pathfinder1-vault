---
cssclass: [monsters]
title1: Demon, Painajai
desc_short: The eight spider eyes of this pale, towering humanoid glisten hungrily,
  and its mouth contains dozens of sharp teeth. It carries a barbed spear with a long,
  clinking chain attached to its end.
title2: Painajai
CR: 14
sources:
- name: Occult Bestiary
  page: 19
  link: http://paizo.com/products/btpy9g21?Pathfinder-Campaign-Setting-Occult-Bestiary
XP: 38400
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 7
senses:
  darkvision: 60
  true seeing: true
auras:
- name: mental static
  DC: 21
AC:
  AC: 28
  touch: 12
  flat_footed: 25
  components:
    dex: 3
    natural: 16
    size: -1
HP:
  HP: 203
  long: 14d10+126
saves:
  fort: 18
  ref: 12
  will: 10
DR:
- amount: 10
  weakness: good
immunities:
- electricity
- poison
- sleep
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 25
speeds:
  base: 40
  climb: 40
attacks:
  melee:
  - - text: +1 cold iron spear +23/+18/+13 (2d6+13/19-20/×3)
      entries:
      - - damage: 2d6+13
          crit_range: 19-20
          crit_multiplier: 3
      attack: +1 cold iron spear
      bonus:
      - 23
      - 18
      - 13
    - text: bite +16 (1d8+4)
      entries:
      - - damage: 1d8+4
      attack: bite
      bonus:
      - 16
  - - text: bite +21 (1d8+12)
      entries:
      - - damage: 1d8+12
      attack: bite
      bonus:
      - 21
  ranged:
  - - text: +1 cold iron spear +18 (2d6+9/19-20/×3)
      entries:
      - - damage: 2d6+9
          crit_range: 19-20
          crit_multiplier: 3
      attack: +1 cold iron spear
      bonus:
      - 18
  special:
  - chain-spear
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: summon
    source: default
    freq: 1/day
    level: 6
    summons:
    - name: painajai
      amount: 1
      chance: 35%
  sources:
  - name: default
    CL: 14
    concentration: 18
psychic_magic:
  entries:
  - superscripts:
    - OA
    name: cognitive block
    PE: 3
    DC: 17
  - name: confusion
    PE: 4
    DC: 18
  - name: fear
    PE: 4
    DC: 18
  - superscripts:
    - OA
    name: greater oneiric horror
    PE: 4
    DC: 18
  - superscripts:
    - APG
    name: hungry pit
    PE: 5
    DC: 19
  - superscripts:
    - OA
    name: mental barrier II
    PE: 3
  - name: mirage arcana
    PE: 5
    DC: 19
  - name: nightmare
    PE: 5
    DC: 19
  - name: phantasmal killer
    PE: 4
    DC: 18
  - superscripts:
    - OA
    name: synaptic pulse
    PE: 3
    DC: 17
  sources:
  - name: default
    CL: 14
    concentration: 18
  PE: 25
ability_scores:
  STR: 27
  DEX: 16
  CON: 29
  INT: 18
  WIS: 18
  CHA: 19
BAB: 14
CMB: 23
CMD: 36
feats:
- name: Combat Reflexes
- name: Improved Critical (spear)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Iron Will
- name: Vital Strike
- name: Weapon Focus (spear)
skills:
  Acrobatics: 20
    when jumping: 24
  Bluff: 21
  Climb: 33
  Intimidate: 21
  Knowledge (local): 18
  Knowledge (nature): 18
  Knowledge (planes): 21
  Perception: 21
  Stealth: 16
  Survival: 21
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
special_qualities:
- dreamwalker
ecology:
  environment: any (Abyss or Dimension of Dreams)
  organization: solitary
  treasure_type: standard
  treasure:
  - +1 cold iron spear
  - other treasure
special_abilities:
  Chain-Spear (Ex): A painajai can hurl its spear at a target within 50 feet with
    no range penalty. If the attack hits, the painajai can immediately yank the chain
    to attempt a repositionAPG or trip combat maneuver check against the target. The
    painajai is considered to have the Improved RepositionAPG and Improved Trip feats
    when performing these maneuvers with its spear only. A reposition combat maneuver
    performed in this way can only move the target closer to the painajai. The painajai
    can recover its spear as a swift action.
  Dreamwalker (Su): A painajai can travel between the Abyss and the Dimension of Dreams
    at will, as per dream travelOA, except that it cannot enter any other planes or
    take other creatures with it.
desc_long: |-
  Lamashtu created the painajai demons to haunt mortal dreams and watch their nightmares, as well as to hunt lone uinuja azatas (see page 9). Though painajais far outnumber uinujas, the demons' inability to cooperate keeps them from gaining the upper hand in their eternal struggle. These demons also indiscriminately attack anyone crossing their path, including dream travelers and other painajais, and only an overseer of overwhelming strength can prevent them from doing so. Painajais speak in a throaty and resonating voice that seems to abrade any ear upon which it falls. They grind their sharp teeth compulsively, sometimes on purpose to unnerve their opponents, and may even chew on the insides of their cheeks to produce a bloody, filthy froth.

  Painajais stand 10 feet tall and weigh about 800 pounds. These demons form from the souls of mortals whose cruel deeds have caused nightmares in other people.

---

# Demon, Painajai
The eight spider eyes of this pale, towering humanoid glisten hungrily, and its mouth contains dozens of sharp teeth. It carries a _[[items/Weapon/Barbed spear|barbed spear]]_ with a long, clinking chain attached to its end.
**Source** Occult Bestiary pg. 19
**XP** 38,400
CE Large outsider (chaotic, demon, evil, extraplanar)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +21
**Aura** mental static (DC 21)

##### Defense

**AC** 28, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+3 Dex, +16 natural, –1 size)
**hp** 203 (14d10+126)
**Fort** +18, **Ref** +12, **Will** +10
**DR** 10/good; **Immune** electricity, poison, sleep; **Resist** acid 10, cold 10, fire 10; **SR** 25

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 40 ft.
**Melee** +1 cold iron _[[items/Weapon/Spear|spear]]_ +23/+18/+13 (2d6+13/19–20/×3), bite +16 (1d8+4) or bite +21 (1d8+12)
**Ranged** +1 cold iron _spear_ +18 (2d6+9/19–20/×3)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** chain-spear
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +18)
Constant—_true seeing_
1/day—_[[universal monster rules/Summon|summon]]_ (level 6, 1 painajai 35%)
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_ **(CL 14th; concentration +18)
25 PE—_[[spells/Cognitive Block|cognitive block]]_ (3 PE, DC 17), _[[spells/Confusion|confusion]]_ (4 PE, DC 18), _[[universal monster rules/Fear|fear]]_ (4 PE, DC 18), greater _[[spells/Oneiric Horror|oneiric horror]]_ (4 PE, DC 18), _[[spells/Hungry Pit|hungry pit]]_ (5 PE, DC 19), _[[spells/Mental Barrier II|mental barrier II]]_ (3 PE), _[[spells/Mirage Arcana|mirage arcana]]_ (5 PE, DC 19), _[[spells/Nightmare|nightmare]]_ (5 PE, DC 19), _[[spells/Phantasmal Killer|phantasmal killer]]_ (4 PE, DC 18), _[[spells/Synaptic Pulse|synaptic pulse]]_ (3 PE, DC 17)

##### Statistics
**Str** 27, **Dex** 16, **Con** 29, **Int** 18, **Wis** 18, **Cha** 19
**Base Atk** +14; **CMB** +23; **CMD** 36
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Critical|Improved Critical]]_ (_spear_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_spear_)
**Skills** Acrobatics +20 (+24 when jumping), Bluff +21, _Climb_ +33, Intimidate +21, Knowledge (local) +18, Knowledge (nature) +18, Knowledge (planes) +21, Perception +21, Stealth +16, Survival +21
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[feats/Dreamwalker|dreamwalker]]_

##### Ecology

**Environment** any (Abyss or Dimension of Dreams)
**Organization** solitary
**Treasure** standard (+1 cold iron _spear_, other treasure)

### Special Abilities

**Chain-Spear (Ex)** A painajai can hurl its _spear_ at a target within 50 feet with no range penalty. If the attack hits, the painajai can immediately yank the chain to attempt a reposition or _[[universal monster rules/Trip|trip]]_ combat maneuver check against the target. The painajai is considered to have the _[[feats/Improved Reposition|Improved Reposition]]_ and _[[feats/Improved Trip|Improved Trip]]_ feats when performing these maneuvers with its _spear_ only. A reposition combat maneuver performed in this way can only move the target closer to the painajai. The painajai can recover its _spear_ as a swift action.

**_Dreamwalker_ (Su)** A painajai can travel between the Abyss and the Dimension of Dreams at will, as per _[[spells/Dream Travel|dream travel]]_, except that it cannot enter any other planes or take other creatures with it.

##### Description

Lamashtu created the painajai demons to haunt mortal dreams and watch their nightmares, as well as to hunt lone uinuja azatas (see page 9). Though painajais far outnumber uinujas, the demons’ inability to cooperate keeps them from gaining the upper hand in their eternal struggle. These demons also indiscriminately attack anyone crossing their path, including _[[spells/Dream|dream]]_ travelers and other painajais, and only an overseer of overwhelming strength can prevent them from doing so. Painajais speak in a throaty and _[[items/Armor Magic Abilities/Resonating|resonating]]_ voice that seems to abrade any ear upon which it falls. They grind their sharp teeth compulsively, sometimes on purpose to unnerve their opponents, and may even chew on the insides of their cheeks to produce a bloody, filthy froth.

Painajais stand 10 feet tall and weigh about 800 pounds. These demons form from the souls of mortals whose _[[items/Weapon Magic Abilities/Cruel|cruel]]_ deeds have caused nightmares in other people.
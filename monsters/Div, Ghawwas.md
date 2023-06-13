---
cssclass: [monsters]
title1: Div, Ghawwas
desc_short: Bristling with spiny ridges, coral horns, and needle-sharp teeth, this
  menacing biped seems to have emerged from some poisoned sea.
title2: Ghawwas
CR: 10
sources:
- name: Bestiary 3
  page: 87
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
- name: 'Pathfinder #22: The End of Eternity'
  page: 80
  link: http://paizo.com/pathfinder/adventurePath/legacyOfFire/v5748btpy87ux
XP: 9600
alignment: NE
size: Large
type: outsider
subtypes:
- aquatic
- div
- evil
- extraplanar
initiative:
  bonus: 6
senses:
  darkvision: 60
  detect good: true
  detect magic: true
  see in darkness: true
AC:
  AC: 26
  touch: 11
  flat_footed: 24
  components:
    dex: 2
    natural: 15
    size: -1
HP:
  HP: 161
  long: 14d10+84
saves:
  fort: 10
  ref: 13
  will: 11
defensive_abilities:
- rough hide
DR:
- amount: 10
  weakness: cold iron and good
immunities:
- fire
- poison
resistances:
  acid: 10
  electricity: 10
SR: 21
speeds:
  base: 30
  swim: 80
attacks:
  melee:
  - - text: bite +21 (1d8+7/19-20)
      entries:
      - - damage: 1d8+7
          crit_range: 19-20
      attack: bite
      bonus:
      - 21
    - text: 2 claws +20 (1d6+7)
      entries:
      - - damage: 1d6+7
      count: 2
      attack: claws
      bonus:
      - 20
    - text: sting +20 (1d6+7 plus poison)
      entries:
      - - damage: 1d6+7
        - effect: poison
      attack: sting
      bonus:
      - 20
  - - text: spear +20/+15/+10 (2d6+10/×3 plus poison)
      entries:
      - - damage: 2d6+10
          crit_multiplier: 3
        - effect: poison
      attack: spear
      bonus:
      - 20
      - 15
      - 10
    - text: bite +19 (1d8+3/19-20)
      entries:
      - - damage: 1d8+3
          crit_range: 19-20
      attack: bite
      bonus:
      - 19
    - text: sting +18 (1d6+3 plus poison)
      entries:
      - - damage: 1d6+3
        - effect: poison
      attack: sting
      bonus:
      - 18
  ranged:
  - - text: spear +15 (2d6+7/×3 plus poison)
      entries:
      - - damage: 2d6+7
          crit_multiplier: 3
        - effect: poison
      attack: spear
      bonus:
      - 15
  special:
  - boiling sea
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: control water
    source: default
    freq: At will
  - name: curse water
    source: default
    freq: At will
  - name: deeper darkness
    source: default
    freq: At will
  - name: dimension door
    source: default
    freq: At will
  - name: hallucinatory terrain
    source: default
    freq: 3/day
    DC: 16
  - name: stinking cloud
    source: default
    freq: 3/day
    DC: 15
  - name: summon
    source: default
    freq: 3/day
    level: 6
    summons:
    - name: pairaka
      amount: 1
      chance: 60%
  - name: quench
    source: default
    freq: 3/day
    DC: 15
  sources:
  - name: default
    CL: 12
    concentration: 14
ability_scores:
  STR: 24
  DEX: 15
  CON: 23
  INT: 12
  WIS: 15
  CHA: 14
BAB: 14
CMB: 22
CMD: 34
feats:
- name: Combat Reflexes
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Multiattack
- name: Power Attack
- name: Weapon Focus (bite)
skills:
  Bluff: 19
  Knowledge (geography): 18
  Knowledge (planes): 18
  Perception: 19
  Stealth: 15
  Survival: 19
  Swim: 32
languages:
- Abyssal
- Aquan
- Celestial
- Infernal
- telepathy 100 ft.
special_qualities:
- amphibious
ecology:
  environment: any (Abaddon)
  organization: solitary
  treasure_type: standard
special_abilities:
  Boiling Sea (Su): As a standard action, a ghawwas can cause the waters around it
    to boil. Any creature within 50 feet of the ghawwas, within the same body of water,
    and at least half submerged takes 6d6 points of fire damage (DC 23 Fortitude save
    for half). The save DC is Constitution-based.
  Poison (Ex): Sting-injury; save Fort DC 23; frequency 1/round for 6 rounds; effect
    1d6 Str; cure 2 consecutive saves.
  Rough Hide (Ex): Ghawwas have rough hides studded with jagged barbs and spiny protrusions.
    Any creature striking a ghawwas with a natural weapon or an unarmed strike takes
    1d6 points of slashing and piercing damage.
desc_long: |-
  Full of poison and treachery, ghawwas foul the seas and seek to bring ruin to those who dwell there. Ghawwas resemble a mixture of hulking humanoid, prehistoric fish, and poisonous bottom-feeder. While most ghawwas live in salt water, they sometimes teleport to oases to defile them or suck them dry. Although they see all mortals as enemies, ghawwas bear a particular grudge against peaceable, water-breathing creatures such as merfolk and locathah.

  All ghawwas find the tolling of bells insufferable, the sound filling them with rage and driving them to seek out the source and destroy either the bell or those ringing it.

  The typical ghawwas stands 12 feet tall and weighs close to 1,200 pounds.

---

# Div, Ghawwas
Bristling with spiny ridges, coral horns, and needle-sharp teeth, this _[[items/Weapon Magic Abilities/Menacing|menacing]]_ biped seems to have emerged from some poisoned sea.
**Source** Bestiary 3 pg. 87, Pathfinder #22: The End of Eternity pg. 80
**XP** 9,600

NE Large outsider (aquatic, div, evil, extraplanar)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +19

##### Defense

**AC** 26, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+2 Dex, +15 natural, –1 size)
**hp** 161 (14d10+84)
**Fort** +10, **Ref** +13, **Will** +11
**Defensive Abilities** rough hide; **DR** 10/cold iron and good; **Immune** fire, poison; **Resist** acid 10, electricity 10; **SR** 21

##### Offense
**Speed** 30 ft., swim 80 ft.
**Melee** bite +21 (1d8+7/19–20), 2 claws +20 (1d6+7), sting +20 (1d6+7 plus poison) or _[[items/Weapon/Spear|spear]]_ +20/+15/+10 (2d6+10/×3 plus poison), bite +19 (1d8+3/19-20), sting +18 (1d6+3 plus poison)
**Ranged** _spear_ +15 (2d6+7/×3 plus poison)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** boiling sea
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +14)
Constant—_detect good_, _detect magic_
At will—_[[spells/Control Water|control water]]_, _[[spells/Curse Water|curse water]]_, _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Dimension Door|dimension door]]_
3/day—_[[spells/Hallucinatory Terrain|hallucinatory terrain]]_ (DC 16), _[[spells/Stinking Cloud|stinking cloud]]_ (DC 15), _[[universal monster rules/Summon|summon]]_ (level 6, 1 pairaka 60%), _[[spells/Quench|quench]]_ (DC 15)

##### Statistics
**Str** 24, **Dex** 15, **Con** 23, **Int** 12, **Wis** 15, **Cha** 14
**Base Atk** +14; **CMB** +22; **CMD** 34
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Bluff +19, Knowledge (geography and planes) +18, Perception +19, Stealth +15, Survival +19, Swim +32
**Languages** Abyssal, Aquan, Celestial, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Amphibious|amphibious]]_

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary
**Treasure** standard

### Special Abilities

**Boiling Sea (Su)** As a standard action, a ghawwas can cause the waters around it to boil. Any creature within 50 feet of the ghawwas, within the same body of water, and at least half submerged takes 6d6 points of fire damage (DC 23 Fortitude save for half). The save DC is Constitution-based.

**Poison (Ex)** Sting—injury; save Fort DC 23; frequency 1/round for 6 rounds; effect 1d6 Str; cure 2 consecutive saves.

**Rough Hide (Ex)** Ghawwas have rough hides studded with jagged barbs and spiny protrusions. Any creature striking a ghawwas with a natural weapon or an unarmed strike takes 1d6 points of slashing and piercing damage.

##### Description

Full of poison and treachery, ghawwas foul the seas and seek to bring ruin to those who dwell there. Ghawwas resemble a mixture of hulking humanoid, prehistoric fish, and poisonous bottom-feeder. While most ghawwas live in salt water, they sometimes teleport to oases to defile them or suck them dry. Although they see all mortals as enemies, ghawwas bear a particular grudge against peaceable, water-breathing creatures such as _[[monsters/Merfolk|merfolk]]_ and _[[monsters/Locathah|locathah]]_.

All ghawwas find the tolling of bells insufferable, the sound filling them with _[[spells/Rage|rage]]_ and driving them to seek out the source and destroy either the _[[items/Mundane/Bell|bell]]_ or those ringing it.

The typical ghawwas stands 12 feet tall and weighs close to 1,200 pounds.
---
cssclass: [monsters]
title1: Xiomorn, Vault Keeper
desc_short: This towering, spindly, four-armed entity appears to be made of stone
  and crystal, yet it moves with a fluid grace.
title2: Vault Keeper
CR: 14
sources:
- name: Planar Adventures
  page: 252
  link: http://paizo.com/products/btpya1am
- name: The Emerald Spire Superdungeon
  page: 158
  link: http://paizo.com/products/btpy8yqx?Pathfinder-Module-The-Emerald-Spire-Superdungeon
XP: 38400
alignment: LN
size: Medium
type: outsider
subtypes:
- earth
- elemental
- extraplanar
initiative:
  bonus: 8
senses:
  darkvision: 60
  tremorsense: 120
AC:
  AC: 28
  touch: 19
  flat_footed: 19
  components:
    dex: 8
    dodge: 1
    natural: 9
HP:
  HP: 200
  long: 16d10+112
  fast_healing: 5
saves:
  fort: 12
  ref: 18
  will: 14
DR:
- amount: 10
  weakness: adamantine and bludgeoning
immunities:
- elemental traits
SR: 25
speeds:
  base: 40
  climb: 40
attacks:
  melee:
  - - text: 4 claws +24 (2d4+6/19-20 plus crystallization)
      entries:
      - - damage: 2d4+6
          crit_range: 19-20
        - effect: crystallization
      count: 4
      attack: claws
      bonus:
      - 24
  special:
  - crystal burst (DC 25)
  - crystallization (DC 25)
  - rend (2 claws, 2d4+9)
spell_like_abilities:
  entries:
  - name: dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: shatter
    source: default
    freq: At will
    DC: 19
  - name: statue
    source: default
    freq: At will
    DC: 24
  - name: stone shape
    source: default
    freq: At will
  - name: stone tell
    source: default
    freq: At will
  - name: command stone
    source: default
    freq: 3/day
    DC: 26
  - name: flesh to stone
    source: default
    freq: 3/day
    DC: 23
  - name: spike stones
    source: default
    freq: 3/day
    DC: 21
  - name: wall of stone
    source: default
    freq: 3/day
  - name: summon monster VII
    source: default
    freq: 1/day
    other: earth elementals only
  - name: symbol of scrying
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 16
    concentration: 23
ability_scores:
  STR: 22
  DEX: 27
  CON: 25
  INT: 27
  WIS: 18
  CHA: 24
BAB: 16
CMB: 22
CMB_other: +24 sunder
CMD: 41
CMD_other: 43 vs. sunder
feats:
- name: Combat Reflexes
- name: Dodge
- name: Improved Critical (claw)
- name: Improved Sunder
- name: Mobility
- name: Power Attack
- name: Spring Attack
- name: Weapon Finesse
skills:
  Acrobatics: 20
  Climb: 30
  Craft (sculpture): 13
  Disable Device: 22
  Heal: 20
  Knowledge (arcana): 27
  Knowledge (dungeoneering): 24
  Knowledge (geography): 24
  Knowledge (nature): 24
  Knowledge (planes): 27
  Perception: 23
  Sense Motive: 23
  Spellcraft: 27
  Stealth: 27
  Use Magic Device: 26
languages:
- Terran
- telepathy 300 ft.
special_qualities:
- item mastery
ecology:
  environment: any
  organization: solitary, pair, or cabal (3-6 plus 4-12 pechs and 2-6 earth elementals)
  treasure_type: double
special_abilities:
  Crystal Burst (Su): A Vault Keeper's crystal burst deal 12d6 points of damage.
  Crystallization (Su): A creature struck by a Vault Keeper's claw must succeed at
    a DC 25 Fortitude save or take 1 point of Dexterity drain. On a critical hit,
    a target that fails its save instead takes 4 points of Dexterity drain. This ability
    otherwise functions as the Vault Builder version.
  Item Mastery (Ex): A Vault Keeper can always activate spell trigger and spell completion
    items as if the spell were on its class list.
  Item Shaper (Ex): For the purposes of crafting magic items or constructs, a Vault
    Keeper is treated as though it had all item creation feats.
desc_long: 'Xiomorns comprise two castes: the four-legged mythic Vault Builders and
  the two-legged non-mythic Vault Keepers. Both are among the most ancient forms of
  life-primeval elemental beings who travel to raw, new worlds upon the Material Plane,
  pursuing strange ecological investigations into the nature of life. The worlds these
  enigmatic beings have visited feature strange ruins in remote regions and immense,
  vault-like caverns deep underground where ecologies that shouldn't exist flourish.
  Xiomorns have little interest in protecting a world's indigenous life, except as
  necessary for their experiments' goals, and wage war against such races when native
  empires encroach upon the xiomorns' experimental realms.'

---

# Xiomorn, Vault Keeper
This towering, spindly, four-armed entity appears to be made of stone and crystal, yet it moves with a fluid _[[spells/Grace|grace]]_.
**Source** _[[items/Weapon Magic Abilities/Planar|Planar]]_ Adventures pg. 252, The Emerald Spire Superdungeon pg. 158
**XP** 38,400

LN Medium outsider (earth, elemental, extraplanar)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Tremorsense|tremorsense]]_ 120 ft.; Perception +23

##### Defense

**AC** 28, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+8 Dex, +1 _[[feats/Dodge|dodge]]_, +9 natural)
**hp** 200 (16d10+112); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +12, **Ref** +18, **Will** +14
**DR** 10/adamantine and bludgeoning; **Immune** elemental traits; **SR** 25

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 40 ft.
**Melee** 4 claws +24 (2d4+6/19–20 plus crystallization)
**Special Attacks** crystal burst (DC 25), crystallization (DC 25), _[[universal monster rules/Rend|rend]]_ (2 claws, 2d4+9)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +23)
At will—_[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport (self plus 50 lbs. of objects only), _[[spells/Shatter|shatter]]_ (DC 19), _[[spells/Statue|statue]]_ (DC 24), _[[spells/Stone Shape|stone shape]]_, _[[spells/Stone Tell|stone tell]]_
3/day—_[[spells/Command|command]]_ stone (DC 26), _[[spells/Flesh to Stone|flesh to stone]]_ (DC 23), _[[spells/Spike Stones|spike stones]]_ (DC 21), _[[spells/Wall Of Stone|wall of stone]]_
1/day—_[[spells/Summon Monster VII|summon monster VII]]_ (earth elementals only), _[[spells/Symbol of Scrying|symbol of scrying]]_

##### Statistics
**Str** 22, **Dex** 27, **Con** 25, **Int** 27, **Wis** 18, **Cha** 24
**Base Atk** +16; **CMB** +22 (+24 sunder); **CMD** 41 (43 vs. sunder)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +20, _Climb_ +30, Craft (sculpture) +13, Disable Device +22, _[[spells/Heal|Heal]]_ +20, Knowledge (arcana) +27, Knowledge (dungeoneering) +24, Knowledge (geography) +24, Knowledge (nature) +24, Knowledge (planes) +27, Perception +23, Sense Motive +23, Spellcraft +27, Stealth +27, Use Magic Device +26
**Languages** Terran; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** item mastery

##### Ecology

**Environment** any
**Organization** solitary, pair, or cabal (3–6 plus 4–12 pechs and 2–6 earth elementals)
**Treasure** double

### Special Abilities

**Crystal Burst (Su)** A Vault Keeper’s crystal burst deal 12d6 points of damage.

**Crystallization (Su)** A creature struck by a Vault Keeper’s claw must succeed at a DC 25 Fortitude save or take 1 point of Dexterity drain. On a critical hit, a target that fails its save instead takes 4 points of Dexterity drain. This ability otherwise functions as the Vault Builder version.

**Item Mastery (Ex)** A Vault Keeper can always activate spell trigger and spell completion items as if the spell were on its class list.

**Item Shaper (Ex)** For the purposes of crafting magic items or constructs, a Vault Keeper is treated as though it had all item creation feats.

##### Description

Xiomorns comprise two castes: the four-legged mythic Vault Builders and the two-legged non-mythic Vault Keepers. Both are among the most ancient forms of life—primeval elemental beings who travel to raw, new worlds upon the Material Plane, pursuing strange ecological investigations into the nature of life. The worlds these enigmatic beings have visited feature strange ruins in remote regions and immense, vault-like caverns deep underground where ecologies that shouldn’t exist flourish. Xiomorns have little interest in protecting a world’s indigenous life, except as necessary for their experiments’ goals, and wage war against such races when native empires encroach upon the xiomorns’ experimental realms.
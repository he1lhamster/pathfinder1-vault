---
cssclass: [monsters]
title1: Soulbound Annihilator Robot
desc_short: The tip of this towering, scorpionic construct's tail thrums with otherworldly
  energy, and its body moves with unexpected speed.
title2: Soulbound Annihilator Robot
CR: 17
sources:
- name: Construct Handbook
  page: 60
  link: https://paizo.com/products/btq01vam
XP: 102400
alignment: N
size: Gargantuan
type: construct
subtypes:
- robot
initiative:
  bonus: 6
senses:
  darkvision: 120
  low-light vision: true
  tremorsense: 60
AC:
  AC: 32
  touch: 10
  flat_footed: 29
  components:
    deflection: 1
    dex: 2
    dodge: 1
    natural: 22
    size: -4
HP:
  HP: 190
  long: 20d10+80
  other: force field (80 hp, fast healing 16)
saves:
  fort: 8
  ref: 8
  will: 5
defensive_abilities:
- hardness 10
immunities:
- cold
- construct traits
resistances:
  electricity: 30
  fire: 30
weaknesses:
- susceptible to mind-affecting effects
- vulnerable to critical hits
- vulnerable to electricity
speeds:
  base: 50
  other_semicolon: booster jets
  climb: 30
attacks:
  melee:
  - - text: 2 claws +28 (2d6+12/19-20)
      entries:
      - - damage: 2d6+12
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 28
  ranged:
  - - text: 2 chain guns +19 (8d6/x4)
      entries:
      - - damage: 8d6
          crit_multiplier: 4
      count: 2
      attack: chain guns
      bonus:
      - 19
  special:
  - combined arms
  - death throes (DC 14)
  - plasma lance
  - suppressing fire
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: stinking cloud
    source: default
    freq: 3/day
    DC: 17
  - name: contagion
    source: default
    freq: 1/day
    DC: 18
  sources:
  - name: default
    CL: 10
    concentration: 14
ability_scores:
  STR: 34
  DEX: 15
  CON:
  INT: 18
  WIS: 8
  CHA: 12
BAB: 20
CMB: 36
CMD: 49
CMD_other: 57 vs. trip
feats:
- is_bonus: true
  name: Arcane Strike
- name: Combat Expertise
- name: Combat Reflexes
- is_bonus: true
  name: Craft Magic Arms and Armor
- is_bonus: true
  name: Craft Technological Arms and Armor
- is_bonus: true
  name: Craft Technological Item
- name: Deadly Aim
- name: Dodge
- is_bonus: true
  name: Exotic Weapon Proficiency (firearms)
- name: Great Fortitude
- name: Improved Critical (claw)
- name: Improved Initiative
- name: Mobility
- is_bonus: true
  name: Scribe Scroll
- name: Skill Focus (Acrobatics)
- is_bonus: true
  name: Skill Focus (Knowledge [engineering])
- is_bonus: true
  name: Technologist
- is_bonus: true
  name: Toughness
- name: Weapon Focus (chain gun)
skills:
  Acrobatics: 28
  Climb: 20
  Craft (mechanical): 15
    with technology: 19
  Intimidate: 21
  Knowledge (arcana): 17
  Knowledge (geography): 17
  Knowledge (engineering): 23
    with technology: 27
  Linguistics: 8
    with technology: 12
  Perception: 22
  Sense Motive: 22
  Spellcraft: 17
languages:
- Androffan
- Aklo
- Common
- Draconic
- Hallit
- Infernal
- Orc
special_qualities:
- bind soul
- soul focus
ecology:
  environment: any (Numeria)
  organization: solitary
  treasure_type: none
desc_long: A soulbound construct is a once-living creature that has had its soul bound
  to a construct host that serves as its new body. The creatures involved in this
  example are a Technic League captain and an annihilator robot; any abilities not
  explained here are described in those entries.

---

# Soulbound Annihilator Robot
The tip of this towering, scorpionic construct’s tail thrums with otherworldly energy, and its body moves with unexpected speed.
**Source** Construct Handbook pg. 60
**XP** 102,400

N Gargantuan construct (robot)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 60 ft.; Perception +22

##### Defense

**AC** 32, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 29 (+1 deflection, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +22 natural, -4 size)
**hp** 190 (20d10+80); force field (80 hp, _[[universal monster rules/Fast Healing|fast healing]]_ 16)
**Fort** +8, **Ref** +8, **Will** +5
**Defensive Abilities** hardness 10; **Immune** cold, _[[universal monster rules/Construct Traits|construct traits]]_; **Resist** electricity 30, fire 30
**Weaknesses** susceptible to mind-affecting effects, vulnerable to critical hits, vulnerable to electricity

##### Offense
**Speed** 50 ft., _[[universal monster rules/Climb|climb]]_ 30 ft.; booster jets
**Melee** 2 claws +28 (2d6+12/19-20)
**Ranged** 2 chain guns +19 (8d6/x4)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** combined arms, death throes (DC 14), plasma _[[items/Weapon/Lance|lance]]_, suppressing fire
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +14)
3/day—_[[spells/Stinking Cloud|stinking cloud]]_ (DC 17) 
1/day—_[[spells/Contagion|contagion]]_ (DC 18)

##### Statistics
**Str** 34, **Dex** 15, **Con** —, **Int** 18, **Wis** 8, **Cha** 12
**Base Atk** +20; **CMB** +36; **CMD** 49 (57 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Arcane Strike|Arcane Strike]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _[[feats/Craft Technological Arms And Armor|Craft Technological Arms and Armor]]_, _[[feats/Craft Technological Item|Craft Technological Item]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _Dodge_, _[[feats/Exotic Weapon Proficiency|Exotic Weapon Proficiency]]_ (firearms), _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Skill Focus|Skill Focus]]_ (Acrobatics), _Skill Focus_ (Knowledge [engineering]), _[[feats/Technologist|Technologist]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (chain gun)
**Skills** Acrobatics +28, _Climb_ +20, Craft (mechanical) +15 (+19 with technology), Intimidate +21, Knowledge (arcana, geography) +17, Knowledge (engineering) +23 (+27 with technology), Linguistics +8 (+12 with technology), Perception +22, Sense Motive +22, Spellcraft +17
**Languages** Androffan, Aklo, Common, Draconic, Hallit, Infernal, _[[monsters/Orc|Orc]]_
**SQ** bind soul, soul focus

##### Ecology

**Environment** any (Numeria)
**Organization** solitary
**Treasure** none

##### Description

A soulbound construct is a once-living creature that has had its soul bound to a construct host that serves as its new body. The creatures involved in this example are a _[[npcs/Technic League Captain|Technic League captain]]_ and an annihilator robot; any abilities not explained here are described in those entries.
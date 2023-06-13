---
cssclass: [monsters]
title1: Gnoll, Chosen of Lamashtu
title2: Chosen of Lamashtu
CR: 12
sources:
- name: Monster Codex
  page: 98
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 19200
race: Gnoll
classes:
- cleric of Lamashtu 11
alignment: CE
size: Medium
type: humanoid
subtypes:
- gnoll
initiative:
  bonus: -1
senses:
  darkvision: 60
AC:
  AC: 22
  touch: 10
  flat_footed: 22
  components:
    armor: 10
    deflection: 1
    dex: -1
    natural: 2
HP:
  HP: 95
  long: 13d8+37
saves:
  fort: 13
  ref: 3
  will: 13
DR:
- amount: 10
  weakness: adamantine
  max_absorb: 110
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 falchion +15/+10 (2d4+7/18-20)
      entries:
      - - damage: 2d4+7
          crit_range: 18-20
      attack: +1 falchion
      bonus:
      - 15
      - 10
    - text: +1 spear +14/+9 (1d8+5/×3)
      entries:
      - - damage: 1d8+5
          crit_multiplier: 3
      attack: +1 spear
      bonus:
      - 14
      - 9
  ranged:
  - - text: +1 spear +9 (1d8+5/×3)
      entries:
      - - damage: 1d8+5
          crit_multiplier: 3
      attack: +1 spear
      bonus:
      - 9
  special:
  - channel negative energy 7/day (DC 17, 6d6)
  - might of the gods (+11, 11 rounds/day)
  - scythe of evil (5 rounds, 1/day)
spell_like_abilities:
  entries:
  - name: strength surge
    source: default
    freq: 6/day
    other: '+5'
  - name: touch of evil
    source: default
    freq: 6/day
    other: 5 rounds
  sources:
  - name: default
    CL: 11
    concentration: 14
spells:
  entries:
  - is_domain_spell: true
    name: stoneskin
    source: Cleric
    level: 6
  - name: summon monster VI
    source: Cleric
    level: 6
  - name: breath of life
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: righteous might
    source: Cleric
    level: 5
  - name: slay living
    source: Cleric
    level: 5
    DC: 18
  - name: confusion
    source: Cleric
    level: 4
    DC: 17
  - name: divine power
    source: Cleric
    level: 4
  - name: freedom of movement
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: unholy blight
    source: Cleric
    level: 4
    DC: 17
  - name: bestow curse
    source: Cleric
    level: 3
    DC: 16
  - name: blindness
    source: Cleric
    level: 3
    DC: 16
  - name: cure serious wounds
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: magic vestment
    source: Cleric
    level: 3
  - superscripts:
    - UM
    name: vision of hell
    source: Cleric
    level: 3
    DC: 16
  - name: wind wall
    source: Cleric
    level: 3
  - name: aid
    source: Cleric
    level: 2
  - superscripts:
    - ARG
    name: blinding ray
    source: Cleric
    level: 2
    DC: 15
  - is_domain_spell: true
    name: bull's strength
    source: Cleric
    level: 2
  - name: death knell
    source: Cleric
    level: 2
    DC: 15
  - name: hold person
    source: Cleric
    level: 2
    DC: 15
  - name: sound burst
    source: Cleric
    level: 2
    DC: 15
  - name: cause fear
    source: Cleric
    level: 1
    DC: 14
  - name: enlarge person
    source: Cleric
    level: 1
    DC: 14
  - name: entropic shield
    source: Cleric
    level: 1
  - superscripts:
    - UM
    name: forbid action
    source: Cleric
    level: 1
    DC: 14
  - superscripts:
    - UM
    name: murderous command
    source: Cleric
    level: 1
    DC: 14
  - is_domain_spell: true
    name: protection from good
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 13
  - name: detect magic
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  - name: stabilize
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 11
    concentration: 14
    slots:
      0: at-will
    domains:
    - evil
    - strength
tactics:
  Before Combat: The gnoll casts magic vestment on an ally's armor or shield and stoneskin
    on herself.
  During Combat: The gnoll provides more allies for her pack with summon monster VI,
    then uses her spells to empower her allies as they head into combat.
ability_scores:
  STR: 18
  DEX: 8
  CON: 14
  INT: 8
  WIS: 16
  CHA: 14
BAB: 9
CMB: 13
CMD: 23
feats:
- name: Cleave
- name: Combat Casting
- name: Extra Channel
- name: Iron Will
- name: Power Attack
- name: Selective Channeling
- name: Weapon Focus (falchion)
skills:
  Perception: 8
  Spellcraft: 10
languages:
- Gnoll
gear:
  combat:
  - wand of cure moderate wounds (20 charges)
  other:
  - +2 chainmail
  - +1 falchion
  - +1 spear
  - amulet of natural armor +1
  - cloak of resistance +1
  - headband of alluring charisma +2
  - ring of protection +1
  - silver holy symbol
  - granite and diamond dust (worth 750 gp)
  - 448 gp
ecology:
  environment: warm plains or desert
desc_long: |-
  The chosen of Lamashtu are seen as the living representatives of the Mother of Monsters, and are both feared and revered by their packmates. In many cases, these powerful clerics are alphas, though even when they're not, they still hold prominent positions, typically as second-in-command.

   Gnoll religion focuses on Lamashtu. Gnoll clerics, who are almost always female, oversee gory rituals and sacrifices in the goddess's name. They believe unholy magic should not be wasted on everyday things, but that warfare is worthy of such blessings. Clerics attend the births of litters and other momentous events, as well as passing down stories to the young, though a cleric of high position might force lesser clerics to perform such duties.

---

# Gnoll, Chosen of Lamashtu

**Source** Monster Codex pg. 98
**XP** 19,200
_[[monsters/Gnoll|Gnoll]]_ _[[classes/Cleric|cleric]]_ of Lamashtu 11
CE Medium humanoid (_gnoll_)
**Init** –1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +8

##### Defense

**AC** 22, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+10 armor, +1 _[[spells/Deflection|deflection]]_, –1 Dex, +2 natural)
**hp** 95 (13d8+37)
**Fort** +13, **Ref** +3, **Will** +13
**DR** 10/adamantine (110 hp)

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Falchion|falchion]]_ +15/+10 (2d4+7/18–20), +1 _[[items/Weapon/Spear|spear]]_ +14/+9 (1d8+5/×3)
**Ranged** +1 _spear_ +9 (1d8+5/×3)
**Special Attacks** channel negative energy 7/day (DC 17, 6d6), might of the gods (+11, 11 rounds/day), _[[items/Weapon/Scythe|scythe]]_ of evil (5 rounds, 1/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +14)
6/day—strength surge (+5), _[[feats/Touch Of Evil|touch of evil]]_ (5 rounds)
**_Cleric_ Spells Prepared **(CL 11th; concentration +14)
6th—_[[spells/Stoneskin|stoneskin]]_, _[[spells/Summon Monster VI|summon monster VI]]_
5th—_[[spells/Breath Of Life|breath of life]]_, _[[spells/Righteous Might|righteous might]]_, _[[spells/Slay Living|slay living]]_ (DC 18)
4th—_[[spells/Confusion|confusion]]_ (DC 17), _[[spells/Divine Power|divine power]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 17)
3rd—_[[spells/Bestow Curse|bestow curse]]_ (DC 16), blindness (DC 16), _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Magic Vestment|magic vestment]]_, _[[spells/Vision of Hell|vision of hell]]_ (DC 16), _[[spells/Wind Wall|wind wall]]_
2nd—aid, _[[spells/Blinding Ray|blinding ray]]_ (DC 15), bull’s strength, _[[spells/Death Knell|death knell]]_ (DC 15), _[[spells/Hold Person|hold person]]_ (DC 15), _[[spells/Sound Burst|sound burst]]_ (DC 15)
1st—_[[spells/Cause Fear|cause fear]]_ (DC 14), _[[spells/Enlarge Person|enlarge person]]_ (DC 14), _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Forbid Action|forbid action]]_ (DC 14), _[[spells/Murderous Command|murderous command]]_ (DC 14), _[[spells/Protection From Good|protection from good]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, _[[spells/Read Magic|read magic]]_, stabilize
**D** domain spell; **Domains** Evil, Strength

### Tactics

**Before Combat** The _gnoll_ casts _magic vestment_ on an ally’s armor or _[[spells/Shield|shield]]_ and _stoneskin_ on herself.
 **During Combat** The _gnoll_ provides more allies for her pack with _summon monster VI_, then uses her spells to empower her allies as they head into combat.

##### Statistics
**Str** 18, **Dex** 8, **Con** 14, **Int** 8, **Wis** 16, **Cha** 14
**Base Atk** +9; **CMB** +13; **CMD** 23
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Selective Channeling|Selective Channeling]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_falchion_)
**Skills** Perception +8, Spellcraft +10
**Languages** _Gnoll_
**Combat Gear** wand of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (20 charges); **Other Gear** +2 _[[items/Armor/Chainmail|chainmail]]_, +1 _falchion_, +1 _spear_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, silver holy symbol, granite and diamond dust (worth 750 gp), 448 gp

##### Ecology

**Environment** warm plains or desert

##### Description

The chosen of Lamashtu are seen as the living representatives of the Mother of Monsters, and are both feared and revered by their packmates. In many cases, these powerful clerics are alphas, though even when they’re not, they still hold prominent positions, typically as second-in-command.

_Gnoll_ religion focuses on Lamashtu. _Gnoll_ clerics, who are almost always female, oversee _[[items/Weapon Magic Abilities/Gory|gory]]_ rituals and sacrifices in the goddess’s name. They believe _[[items/Weapon Magic Abilities/Unholy|unholy]]_ magic should not be wasted on everyday things, but that warfare is worthy of such blessings. Clerics attend the births of litters and other momentous events, as well as passing down stories to the young, though a _cleric_ of high position might force lesser clerics to perform such duties.
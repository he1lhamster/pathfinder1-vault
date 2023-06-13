---
cssclass: [monsters]
title1: Kobold, Kobold Devilspeaker
title2: Kobold Devilspeaker
CR: 7
sources:
- name: Monster Codex
  page: 134
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 3200
race: Kobold
classes:
- cleric of Asmodeus 8
alignment: LE
size: Small
type: humanoid
subtypes:
- reptilian
initiative:
  bonus: 3
senses:
  darkvision: 60
AC:
  AC: 21
  touch: 14
  flat_footed: 18
  components:
    armor: 4
    dex: 3
    natural: 1
    shield: 2
    size: 1
HP:
  HP: 47
  long: 8d8+8
saves:
  fort: 6
  ref: 5
  will: 9
weaknesses:
- light sensitivity
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk dagger +5/+0 (1d3-3/19-20)
      entries:
      - - damage: 1d3-3
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 5
      - 0
  ranged:
  - - text: dagger +10 (1d3-3/19-20)
      entries:
      - - damage: 1d3-3
          crit_range: 19-20
      attack: dagger
      bonus:
      - 10
  special:
  - channel negative energy 5/day (DC 16, 4d6)
  - staff of order (4 rounds, 1/day)
spell_like_abilities:
  entries:
  - name: copycat
    source: default
    freq: 6/day
    other: 8 rounds
  - name: touch of law
    source: default
    freq: 6/day
  - name: master's illusion
    source: default
    freq: At will
    other: 8 rounds/day
  sources:
  - name: default
    CL: 8
    concentration: 11
spells:
  entries:
  - superscripts:
    - UM
    name: aura of doom
    source: Cleric
    level: 4
    DC: 17
  - is_domain_spell: true
    name: confusion
    source: Cleric
    level: 4
    DC: 17
  - name: cure critical wounds
    source: Cleric
    level: 4
  - name: animate dead
    source: Cleric
    level: 3
  - name: blindness/deafness
    source: Cleric
    level: 3
    DC: 16
  - name: deeper darkness
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: magic circle against chaos
    source: Cleric
    level: 3
  - name: summon monster III
    source: Cleric
    level: 3
  - name: death knell
    source: Cleric
    level: 2
    DC: 15
  - name: hold person
    source: Cleric
    level: 2
    DC: 15
  - is_domain_spell: true
    name: invisibility
    source: Cleric
    level: 2
  - superscripts:
    - UM
    name: lesser animate dead
    source: Cleric
    level: 2
  - superscripts:
    - UM
    name: protective penumbra
    source: Cleric
    level: 2
  - name: bane
    source: Cleric
    level: 1
    DC: 14
  - name: bless
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: disguise self
    source: Cleric
    level: 1
  - superscripts:
    - UC
    name: moment of greatness
    source: Cleric
    level: 1
  - name: obscuring mist
    source: Cleric
    level: 1
  - name: sanctuary
    source: Cleric
    level: 1
    DC: 14
  - name: bleed
    source: Cleric
    level: 0
    DC: 13
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: mending
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 8
    concentration: 11
    slots:
      0: at-will
    domains:
    - law
    - trickery
tactics:
  Before Combat: The devilspeaker casts invisibility on herself.
  During Combat: The devilspeaker stays invisible as long as possible, casting spells
    such as animate dead, aura of doom, bless, cure critical wounds, deeper darkness,
    lesser animate dead, and summon monster III as well as using her wand of cure
    light wounds or channeling negative energy to heal undead.
ability_scores:
  STR: 4
  DEX: 16
  CON: 10
  INT: 10
  WIS: 16
  CHA: 14
BAB: 6
CMB: 2
CMD: 15
feats:
- name: Channeled Shield Wall
- name: Combat Casting
- name: Selective Channeling
- name: Toughness
skills:
  Craft (trapmaking): 2
  Heal: 14
  Perception: 5
  Profession (miner): 5
  Spellcraft: 11
  Stealth: 18
  _racial_mods:
    Craft (trapmaking):
      _: 2
    Perception:
      _: 2
    Profession (miner):
      _: 2
languages:
- Draconic
special_qualities:
- crafty
gear:
  combat:
  - feather token (whip)
  - pearl of power (2nd level)
  - wand of cure light wounds
  other:
  - +1 studded leather
  - +1 light wooden shield
  - dagger
  - mwk dagger
  - various onyx gems worth 200 gp
ecology:
  environment: temperate underground or deep forest
desc_long: Kobold priests are charged with ensuring both the spiritual and the physical
  welfare of a kobold tribe. Though some priests serve the dragon gods, many pay homage
  to Asmodeus, seeing in Hell the perfect embodiment of a lawful evil society. These
  devilspeakers believe a tribe should work like a well-oiled machine, and while kobolds'
  natural cowardice sometimes gets in the way, devilspeakers keep their warriors fighting
  bravely-whether the troops like it or not. Devilspeakers keep spells like animate
  dead handy, turning fallen kobold warriors into zombies. These kobold zombies effectively
  soften up invading adventurers, and dig tirelessly in the mines.

---

# Kobold, Kobold Devilspeaker

**Source** Monster Codex pg. 134
**XP** 3,200
_[[monsters/Kobold|Kobold]]_ _[[classes/Cleric|cleric]]_ of Asmodeus 8

LE Small humanoid (reptilian)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +5

##### Defense

**AC** 21, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+4 armor, +3 Dex, +1 natural, +2 _[[spells/Shield|shield]]_, +1 size)
**hp** 47 (8d8+8)
**Fort** +6, **Ref** +5, **Will** +9
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Dagger|dagger]]_ +5/+0 (1d3–3/19–20)
**Ranged** _dagger_ +10 (1d3–3/19–20)
**Special Attacks** channel negative energy 5/day (DC 16, 4d6), staff of order (4 rounds, 1/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +11)
6/day—copycat (8 rounds), touch of law
At will—master’s illusion (8 rounds/day)
**_Cleric_ Spells Prepared **(CL 8th; concentration +11)
4th—_[[spells/Aura of Doom|aura of doom]]_ (DC 17), _[[spells/Confusion|confusion]]_ (DC 17), _[[spells/Cure Critical Wounds|cure critical wounds]]_
3rd—_[[spells/Animate Dead|animate dead]]_, blindness/deafness (DC 16), _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Magic Circle against Chaos|magic circle against chaos]]_, _[[spells/Summon Monster III|summon monster III]]_
2nd—_[[spells/Death Knell|death knell]]_ (DC 15), _[[spells/Hold Person|hold person]]_ (DC 15), _[[spells/Invisibility|invisibility]]_, lesser _animate dead_, _[[spells/Protective Penumbra|protective penumbra]]_
1st—_[[spells/Bane|bane]]_ (DC 14), _[[spells/Bless|bless]]_, _[[spells/Disguise Self|disguise self]]_, _[[spells/Moment of Greatness|moment of greatness]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 14)
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Mending|mending]]_
**D** domain spell; **Domains** Law, Trickery

### Tactics

**Before Combat** The devilspeaker casts _invisibility_ on herself.
 **During Combat** The devilspeaker stays _[[conditions/Invisible|invisible]]_ as long as possible, casting spells such as _animate dead_, _aura of doom_, _bless_, _cure critical wounds_, _deeper darkness_, lesser _animate dead_, and _summon monster III_ as well as using her wand of _[[spells/Cure Light Wounds|cure light wounds]]_ or _[[items/Armor Magic Abilities/Channeling|channeling]]_ negative energy to _[[spells/Heal|heal]]_ undead.

##### Statistics
**Str** 4, **Dex** 16, **Con** 10, **Int** 10, **Wis** 16, **Cha** 14
**Base Atk** +6; **CMB** +2; **CMD** 15
**Feats** _[[feats/Channeled _Shield_ Wall|Channeled _Shield_ Wall]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Selective Channeling|Selective Channeling]]_, _[[feats/Toughness|Toughness]]_
**Skills** Craft (trapmaking) +2, _Heal_ +14, Perception +5, Profession (_[[npcs/Miner|miner]]_) +5, Spellcraft +11, Stealth +18; **Racial Modifiers** +2 Craft (trapmaking), +2 Perception, +2 Profession (_miner_)
**Languages** Draconic
**SQ** crafty
**Combat Gear** feather token (_[[items/Weapon/Whip|whip]]_), pearl of power (2nd level), wand of _cure light wounds_; **Other Gear** +1 studded leather, +1 _[[items/Shield/Light wooden shield|light wooden shield]]_, _dagger_, mwk _dagger_, various onyx gems worth 200 gp

##### Ecology

**Environment** temperate underground or deep forest

##### Description

_Kobold_ priests are charged with ensuring both the spiritual and the physical welfare of a _kobold_ tribe. Though some priests serve the dragon gods, many pay homage to Asmodeus, seeing in Hell the perfect embodiment of a lawful evil society. These devilspeakers believe a tribe should work like a well-oiled machine, and while kobolds’ natural cowardice sometimes gets in the way, devilspeakers keep their warriors fighting bravely—whether the troops like it or not. Devilspeakers keep spells like _animate dead_ handy, turning _[[monsters/Fallen|fallen]]_ _kobold_ warriors into zombies. These _kobold_ zombies effectively soften up invading adventurers, and dig tirelessly in the mines.
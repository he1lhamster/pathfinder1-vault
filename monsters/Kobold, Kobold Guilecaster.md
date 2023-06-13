---
cssclass: [monsters]
title1: Kobold, Kobold Guilecaster
title2: Kobold Guilecaster
CR: 5
sources:
- name: Monster Codex
  page: 131
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 1600
race: Kobold
classes:
- sorcerer 6
alignment: LE
size: Small
type: humanoid
subtypes:
- reptilian
initiative:
  bonus: 2
senses:
  darkvision: 60
AC:
  AC: 18
  touch: 13
  flat_footed: 16
  components:
    armor: 4
    dex: 2
    natural: 1
    size: 1
HP:
  HP: 35
  long: 6d6+12
saves:
  fort: 3
  ref: 4
  will: 4
weaknesses:
- light sensitivity
speeds:
  base: 30
attacks:
  melee:
  - - text: quarterstaff +2 (1d4-2)
      entries:
      - - damage: 1d4-2
      attack: quarterstaff
      bonus:
      - 2
spell_like_abilities:
  entries:
  - name: trap rune
    source: default
    freq: 6/day
    DC: 16
  sources:
  - name: default
    CL: 6
    concentration: 9
spells:
  entries:
  - name: lightning bolt
    source: Sorcerer
    level: 3
    DC: 16
  - superscripts:
    - APG
    name: create pit
    source: Sorcerer
    level: 2
  - name: mirror image
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: alarm
    source: Sorcerer
    level: 1
  - name: charm person
    source: Sorcerer
    level: 1
    DC: 14
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: ray of enfeeblement
    source: Sorcerer
    level: 1
    DC: 14
  - name: arcane mark
    source: Sorcerer
    level: 0
  - name: daze
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: open/close
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
    DC: 13
  - name: resistance
    source: Sorcerer
    level: 0
  - superscripts:
    - APG
    name: spark
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 6
    concentration: 9
    slots:
      3: 4
      2: 6
      1: 7
      0: at-will
    bloodline: kobold
ability_scores:
  STR: 6
  DEX: 14
  CON: 12
  INT: 13
  WIS: 8
  CHA: 16
BAB: 3
CMB: 0
CMD: 12
feats:
- name: Combat Expertise
- name: Eschew Materials
- name: Improved Feint
- name: Skill Focus (Craft [trapmaking])
skills:
  Bluff: 15
  Craft (trapmaking): 15
  Perception: 1
  Profession (miner): 1
  Use Magic Device: 15
  _racial_mods:
    Craft (trapmaking):
      _: 2
    Perception:
      _: 2
    Profession (miner):
      _: 2
languages:
- Draconic
- Dwarven
special_qualities:
- bloodline arcana (+2 to spell DC if target is denied Dex bonus to AC)
- crafty
- trap sense +2
gear:
  combat:
  - antitoxin
  - thunderstone
  other:
  - quarterstaff
  - circlet of persuasion
  - masterwork artisan's tools
  - 15 gp
ecology:
  environment: temperate underground or deep forest
desc_long: Kobolds see sorcery as proof of their draconic heritage.

---

# Kobold, Kobold Guilecaster

**Source** Monster Codex pg. 131
**XP** 1,600
_[[monsters/Kobold|Kobold]]_ _[[classes/Sorcerer|sorcerer]]_ 6

LE Small humanoid (reptilian)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +1

##### Defense

**AC** 18, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+4 armor, +2 Dex, +1 natural, +1 size)
**hp** 35 (6d6+12)
**Fort** +3, **Ref** +4, **Will** +4
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Quarterstaff|quarterstaff]]_ +2 (1d4–2)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +9)
6/day—trap rune (DC 16)
**_Sorcerer_ Spells Known **(CL 6th; concentration +9)
3rd (4/day)—_[[spells/Lightning Bolt|lightning bolt]]_ (DC 16)
2nd (6/day)—_[[spells/Create Pit|create pit]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Scorching Ray|scorching ray]]_
1st (7/day)—_[[spells/Alarm|alarm]]_, _[[spells/Charm Person|charm person]]_ (DC 14), _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 14)
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[spells/Daze|daze]]_, _[[spells/Detect Magic|detect magic]]_, open/close, _[[spells/Prestidigitation|prestidigitation]]_ (DC 13), _[[universal monster rules/Resistance|resistance]]_, _[[spells/Spark|spark]]_
**Bloodline** _kobold_

##### Statistics
**Str** 6, **Dex** 14, **Con** 12, **Int** 13, **Wis** 8, **Cha** 16
**Base Atk** +3; **CMB** +0; **CMD** 12
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Improved Feint|Improved Feint]]_, _[[feats/Skill Focus|Skill Focus]]_ (Craft [trapmaking])
**Skills** Bluff +15, Craft (trapmaking) +15, Perception +1, Profession (_[[npcs/Miner|miner]]_) +1, Use Magic Device +15; **Racial Modifiers** +2 Craft (trapmaking), +2 Perception, +2 Profession (_miner_)
**Languages** Draconic, Dwarven
**SQ** bloodline arcana (+2 to spell DC if target is denied Dex bonus to AC), crafty, trap sense +2
**Combat Gear** _[[items/Mundane/Antitoxin|antitoxin]]_, _[[items/Mundane/Thunderstone|thunderstone]]_; **Other Gear** _quarterstaff_, _[[items/Wondrous Item/Circlet of Persuasion|circlet of persuasion]]_, masterwork artisan’s tools, 15 gp

##### Ecology

**Environment** temperate underground or deep forest

##### Description

Kobolds see sorcery as proof of their _[[feats/Draconic Heritage|draconic heritage]]_.
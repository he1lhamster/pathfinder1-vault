---
cssclass: [monsters]
title1: Sahuagin, Sahuagin Underpriestess
title2: Sahuagin Underpriestess
CR: 5
sources:
- name: Monster Codex
  page: 193
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 1600
race: Sahuagin
classes:
- cleric 4
alignment: LE
size: Medium
type: monstrous humanoid
subtypes:
- aquatic
initiative:
  bonus: 0
senses:
  blindsense: 30
  darkvision: 60
AC:
  AC: 19
  touch: 10
  flat_footed: 19
  components:
    armor: 4
    natural: 5
HP:
  HP: 57
  long: 2d10+4d8+28
  HD: 6
saves:
  fort: 7
  ref: 4
  will: 11
  other: +2 vs. good
weaknesses:
- light blindness
speeds:
  base: 30
  swim: 60
attacks:
  melee:
  - - text: mwk trident +10 (1d8+6)
      entries:
      - - damage: 1d8+6
      attack: mwk trident
      bonus:
      - 10
    - text: bite +4 (1d4+2)
      entries:
      - - damage: 1d4+2
      attack: bite
      bonus:
      - 4
  ranged:
  - - text: mwk underwater heavy crossbow +6 (1d10/19-20)
      entries:
      - - damage: 1d10
          crit_range: 19-20
      attack: mwk underwater heavy crossbow
      bonus:
      - 6
  special:
  - blood frenzy
  - channel negative energy 3/day (DC 12, 2d6)
  - destructive smite (+2, 7/day)
spell_like_abilities:
  entries:
  - name: icicle
    source: default
    freq: 7/day
    other: 1d6+2 cold
  sources:
  - name: default
    CL: 4
    concentration: 8
spells:
  entries:
  - name: blood in the water
    source: Cleric
    level: 2
  - name: darkness
    source: Cleric
    level: 2
  - name: hold person
    source: Cleric
    level: 2
    DC: 16
  - is_domain_spell: true
    name: shatter
    source: Cleric
    level: 2
    DC: 16
  - name: bless
    source: Cleric
    level: 1
  - name: cure light wounds
    source: Cleric
    level: 1
  - name: magic weapon
    source: Cleric
    level: 1
  - name: protection from good
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: true strike
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 14
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: resistance
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 4
    concentration: 8
    slots:
      0: at-will
    domains:
    - destruction
    - water
ability_scores:
  STR: 18
  DEX: 10
  CON: 17
  INT: 14
  WIS: 18
  CHA: 11
BAB: 5
CMB: 9
CMD: 19
feats:
- name: Brew Potion
- name: Combat Casting
- name: Toughness
skills:
  Handle Animal: 3
  Knowledge (religion): 11
  Perception: 13
  Ride: 4
  Sense Motive: 13
  Spellcraft: 11
  Swim: 16
languages:
- Aklo
- Aquan
- Common
- speak with sharks
gear:
  combat:
  - potion of lesser restoration
  - wand of cure moderate wounds (11 charges)
  other:
  - +1 studded leather
  - dagger
  - mwk trident
  - mwk underwater heavy crossbow with 10 bolts
  - gold unholy symbol (worth 100 gp)
  - 317 gp
ecology:
  environment: temperate or warm ocean
desc_long: Priestesses lead ceremonies and support military actions.

---

# Sahuagin, Sahuagin Underpriestess

**Source** Monster Codex pg. 193
**XP** 1,600
_[[monsters/Sahuagin|Sahuagin]]_ _[[classes/Cleric|cleric]]_ 4

LE Medium monstrous humanoid (aquatic)
**Init** +0; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 30 ft., _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +13

##### Defense

**AC** 19, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+4 armor, +5 natural)
**hp** 57 (6 HD; 2d10+4d8+28)
**Fort** +7, **Ref** +4, **Will** +11; +2 vs. good
**Weaknesses** _[[universal monster rules/Light Blindness|light blindness]]_

##### Offense
**Speed** 30 ft., swim 60 ft.
**Melee** mwk _[[items/Weapon/Trident|trident]]_ +10 (1d8+6), bite +4 (1d4+2)
**Ranged** mwk _[[items/Weapon/Underwater heavy crossbow|underwater heavy crossbow]]_ +6 (1d10/19–20)
**Special Attacks** blood frenzy, channel negative energy 3/day (DC 12, 2d6), destructive smite (+2, 7/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +8)
7/day—icicle (1d6+2 cold)
**_Cleric_ Spells Prepared** (CL 4th; concentration +8)
2nd—_[[spells/Blood In The Water|blood in the water]]_, _[[spells/Darkness|darkness]]_, _[[spells/Hold Person|hold person]]_ (DC 16), _[[spells/Shatter|shatter]]_ (DC 16)
 1st—_[[spells/Bless|bless]]_, _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Protection From Good|protection from good]]_, _[[spells/True Strike|true strike]]_
 0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 14), _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[universal monster rules/Resistance|resistance]]_
 **D** domain spell; **Domains** _[[spells/Destruction|Destruction]]_, Water

##### Statistics
**Str** 18, **Dex** 10, **Con** 17, **Int** 14, **Wis** 18, **Cha** 11
**Base Atk** +5; **CMB** +9; **CMD** 19
**Feats** _[[feats/Brew Potion|Brew Potion]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Toughness|Toughness]]_
**Skills** Handle Animal +3, Knowledge (religion) +11, Perception +13, Ride +4, Sense Motive +13, Spellcraft +11, Swim +16
**Languages** Aklo, Aquan, Common; speak with sharks
**Combat Gear** potion of lesser _[[spells/Restoration|restoration]]_, wand of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (11 charges); **Other Gear** +1 studded leather, _[[items/Weapon/Dagger|dagger]]_, mwk _trident_, mwk _underwater heavy crossbow_ with 10 bolts, gold _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol (worth 100 gp), 317 gp

##### Ecology

**Environment** temperate or warm ocean

##### Description

Priestesses lead ceremonies and support military actions.
---
cssclass: [monsters]
title1: Drow, Drow Noble
title2: Drow Noble
CR: 3
sources:
- name: Pathfinder RPG Bestiary
  page: 115
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 800
race: Female
classes:
- drow noble cleric 3
alignment: CE
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 3
senses:
  darkvision: 120
AC:
  AC: 21
  touch: 13
  flat_footed: 18
  components:
    armor: 6
    dex: 3
    shield: 2
HP:
  HP: 20
  long: 3d8+3
saves:
  fort: 4
  ref: 4
  will: 6
  other: +2 vs. enchantment
immunities:
- sleep
SR: 14
weaknesses:
- light blindness
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk rapier +4 (1d6+1/18-20)
      entries:
      - - damage: 1d6+1
          crit_range: 18-20
      attack: mwk rapier
      bonus:
      - 4
  ranged:
  - - text: hand crossbow +5 (1d4/19-20 plus poison)
      entries:
      - - damage: 1d4
          crit_range: 19-20
        - effect: poison
      attack: hand crossbow
      bonus:
      - 5
  special:
  - bleeding touch (6/day)
  - channel negative energy (4/day, 2d6, DC 12)
  - touch of chaos (6/day)
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: dancing lights
    source: default
    freq: At will
  - name: deeper darkness
    source: default
    freq: At will
  - name: faerie fire
    source: default
    freq: At will
  - name: feather fall
    source: default
    freq: At will
  - name: levitate
    source: default
    freq: At will
  - name: divine favor
    source: default
    freq: 1/day
  - name: dispel magic
    source: default
    freq: 1/day
  - name: suggestion
    source: default
    freq: 1/day
    DC: 14
  sources:
  - name: default
    CL: 3
spells:
  entries:
  - is_domain_spell: true
    name: death knell
    source: Drow Noble Cleric
    level: 2
    DC: 15
  - name: hold person
    source: Drow Noble Cleric
    level: 2
    DC: 15
  - name: silence
    source: Drow Noble Cleric
    level: 2
    DC: 15
  - name: bless
    source: Drow Noble Cleric
    level: 1
  - name: cause fear
    source: Drow Noble Cleric
    level: 1
    DC: 14
  - name: cure light wounds
    source: Drow Noble Cleric
    level: 1
  - is_domain_spell: true
    name: protection from law
    source: Drow Noble Cleric
    level: 1
  - name: bleed
    source: Drow Noble Cleric
    level: 0
    DC: 13
  - name: detect poison
    source: Drow Noble Cleric
    level: 0
  - name: read magic
    source: Drow Noble Cleric
    level: 0
  - name: resistance
    source: Drow Noble Cleric
    level: 0
  sources:
  - name: Drow Noble Cleric
    type: prepared
    CL: 3
    domains:
    - chaos
    - death
ability_scores:
  STR: 12
  DEX: 17
  CON: 12
  INT: 10
  WIS: 17
  CHA: 12
BAB: 2
CMB: 3
CMD: 16
feats:
- name: Channel Smite
- name: Weapon Finesse
skills:
  Knowledge (religion): 6
  Sense Motive: 9
  Spellcraft: 6
  Perception: 5
  _racial_mods:
    Perception:
      _: 2
languages:
- Elven
- Undercommon
special_qualities:
- poison use
gear:
  gear:
  - masterwork breastplate
  - heavy steel shield
  - masterwork rapier
  - drow poison (4)
  - potion of invisibility
  - scroll of dispel magic
  - wand of cure light wounds (CL 1st, 20 charges)
  - 400 gp
ecology:
  environment: underground
desc_long: |-
  Although related to the elves, the drow are a vile and evil cousin at best. Sometimes called dark elves, these cunning creatures prowl the caves and tunnels of the world below, ruling vast subterranean cities through fear and might. Worshiping demons and enslaving most races they encounter, the drow are among the underworld's most feared and hated denizens.

  Drow are shorter and a bit more slender than their surface-dwelling kin, but they are otherwise physically similar. Drow have dark skin, ranging from black to a hazy purple hue. Most drow have white or silver hair and white or red eyes, but other colors are not unheard of.

  Drow society is ruled over by powerful nobility, themselves governed by sadistic and dangerous matriarchs who constantly plot and scheme against rival houses and lesser kin within their own families. The majority of drow are the common soldiers and decadent citizenry, with base stats as presented here-drow nobles are more powerful and dangerous, and are detailed below.

  In combat, drow are thoroughly ruthless, with little regard for fairness or mercy. They prefer to attack from ambush or to lure enemies into situations where they clearly have the upper hand. If things turn against them, drow are quick to flee, leaving slaves and minions to cover their escape.

---

# Drow, Drow Noble

**Source** Pathfinder RPG Bestiary pg. 115
**XP** 800
Female _[[monsters/Drow|drow]]_ noble _[[classes/Cleric|cleric]]_ 3
CE Medium humanoid (elf)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +5

##### Defense

**AC** 21, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+6 armor, +3 Dex, +2 _[[spells/Shield|shield]]_)
**hp** 20 (3d8+3)
**Fort** +4, **Ref** +4, **Will** +6; +2 vs. enchantment
**Immune** sleep; **SR** 14
**Weaknesses** _[[universal monster rules/Light Blindness|light blindness]]_

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Rapier|rapier]]_ +4 (1d6+1/18–20)
**Ranged** _[[items/Weapon/Hand crossbow|hand crossbow]]_ +5 (1d4/19–20 plus poison)
**Special Attacks** bleeding touch (6/day), channel negative energy (4/day, 2d6, DC 12), touch of chaos (6/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd)
Constant—_[[spells/Detect Magic|detect magic]]_
At will—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Faerie Fire|faerie fire]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Levitate|levitate]]_
1/day—_[[spells/Divine Favor|divine favor]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Suggestion|suggestion]]_ (DC 14)
**Spells Prepared **(CL 3rd)
2nd—_[[spells/Death Knell|death knell]]_ (DC 15), _[[spells/Hold Person|hold person]]_ (DC 15), _[[spells/Silence|silence]]_ (DC 15)
1st—_[[spells/Bless|bless]]_, _[[spells/Cause Fear|cause fear]]_ (DC 14), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Protection From Law|protection from law]]_
0—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Detect Poison|detect poison]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_
**D** domain spell; **Domains **Chaos, Death

##### Statistics
**Str** 12, **Dex** 17, **Con** 12, **Int** 10, **Wis** 17, **Cha** 12
**Base Atk** +2; **CMB** +3; **CMD** 16
**Feats** _[[feats/Channel Smite|Channel Smite]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Knowledge (religion) +6, Sense Motive +9, Spellcraft +6; **Racial Modifiers** +2 Perception
**Languages** Elven, Undercommon
**SQ** poison use
**Gear** masterwork _[[items/Armor/Breastplate|breastplate]]_, _[[items/Shield/Heavy steel shield|heavy steel shield]]_, masterwork _rapier_, _[[poisons/Drow poison|drow poison]]_ (4), potion of _[[spells/Invisibility|invisibility]]_, scroll of _dispel magic_, wand of _cure light wounds_ (CL 1st, 20 charges), 400 gp

##### Ecology

**Environment** underground

Although related to the elves, the _drow_ are a vile and evil cousin at best. Sometimes _[[items/Weapon Magic Abilities/Called|called]]_ dark elves, these _[[items/Weapon Magic Abilities/Cunning|cunning]]_ creatures prowl the caves and tunnels of the world below, ruling vast subterranean cities through _[[universal monster rules/Fear|fear]]_ and might. Worshiping demons and enslaving most races they encounter, the _drow_ are among the underworld’s most feared and hated denizens.

_Drow_ are shorter and a bit more slender than their surface-dwelling kin, but they are otherwise physically similar. _Drow_ have dark skin, ranging from black to a hazy purple hue. Most _drow_ have white or silver hair and white or red eyes, but other colors are not unheard of.

_Drow_ society is ruled over by powerful nobility, themselves governed by sadistic and dangerous matriarchs who constantly plot and scheme against _[[feats/Rival|rival]]_ houses and lesser kin within their own families. The majority of _drow_ are the common soldiers and decadent citizenry, with base stats as presented here—_drow_ nobles are more powerful and dangerous, and are detailed below.

In combat, _drow_ are thoroughly ruthless, with little regard for _[[spells/Fairness|fairness]]_ or mercy. They prefer to attack from ambush or to lure enemies into situations where they clearly have the upper hand. If things turn against them, _drow_ are quick to flee, leaving slaves and minions to cover their escape.
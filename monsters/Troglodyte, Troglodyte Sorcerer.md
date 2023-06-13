---
cssclass: [monsters]
title1: Troglodyte, Troglodyte Sorcerer
title2: Troglodyte Sorcerer
CR: 4
sources:
- name: Monster Codex
  page: 214
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 1200
race: Troglodyte
classes:
- sorcerer 4
alignment: CE
size: Medium
type: humanoid
subtypes:
- reptilian
initiative:
  bonus: 1
senses:
  darkvision: 90
auras:
- name: stench
  radius: 30
  DC: 13
  duration: 10 rounds
AC:
  AC: 17
  touch: 11
  flat_footed: 16
  components:
    dex: 1
    natural: 6
HP:
  HP: 39
  long: 2d8+4d6+16
  HD: 6
saves:
  fort: 7
  ref: 3
  will: 6
  other: +2 vs. poison
resistances:
  electricity: 5
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk club +4 (1d6)
      entries:
      - - damage: 1d6
      attack: mwk club
      bonus:
      - 4
    - text: bite -2 (1d4)
      entries:
      - - damage: 1d4
      attack: bite
      bonus:
      - -2
    - text: claw -2 (1d4)
      entries:
      - - damage: 1d4
      attack: claw
      bonus:
      - -2
  - - text: bite +3 (1d4)
      entries:
      - - damage: 1d4
      attack: bite
      bonus:
      - 3
    - text: 2 claws +3 (1d4)
      entries:
      - - damage: 1d4
      count: 2
      attack: claws
      bonus:
      - 3
  special:
  - claws (1d6, 6 rounds/day)
spells:
  entries:
  - name: acid arrow
    source: Sorcerer
    level: 2
  - name: cause fear
    source: Sorcerer
    level: 1
    DC: 15
  - superscripts:
    - UM
    name: corrosive touch
    source: Sorcerer
    level: 1
  - name: ray of enfeeblement
    source: Sorcerer
    level: 1
    DC: 15
  - name: summon monster I
    source: Sorcerer
    level: 1
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: daze
    source: Sorcerer
    level: 0
    DC: 13
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 13
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: mending
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 4
    concentration: 7
    slots:
      2: 4
      1: 7
      0: at-will
    bloodline: abyssal
ability_scores:
  STR: 10
  DEX: 13
  CON: 14
  INT: 10
  WIS: 13
  CHA: 16
BAB: 3
CMB: 3
CMD: 14
feats:
- name: Combat Casting
- name: Eschew Materials
- name: Silent Spell
- name: Spell Focus (evocation)
skills:
  Knowledge (arcana): 7
  Knowledge (planes): 4
  Spellcraft: 6
  Stealth: 9
    in rocky areas: 13
  Perception: 1
languages:
- Draconic
special_qualities:
- bloodline arcana (summoned creatures gain DR 2/good)
gear:
  combat:
  - potion of cure light wounds
  - wand of invisibility (10 charges)
  other:
  - mwk club
  - cloak of resistance +1
  - 150 gp
ecology:
  environment: any underground
desc_long: Arcane casters often become scouts, as their divine counterparts monopolize
  the positions of power within the tribe. Most troglodyte sorcerers have the Abyssal,
  Deep Earth (Pathfinder RPG Advanced Player's Guide 137), Draconic, or Undead bloodline.

---

# Troglodyte, Troglodyte Sorcerer

**Source** Monster Codex pg. 214
**XP** 1,200
_[[monsters/Troglodyte|Troglodyte]]_ _[[classes/Sorcerer|sorcerer]]_ 4
CE Medium humanoid (reptilian)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 90 ft.; Perception +1
**Aura** _[[universal monster rules/Stench|stench]]_ (30 ft., DC 13, 10 rounds)

##### Defense

**AC** 17, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+1 Dex, +6 natural)
**hp** 39 (6 HD; 2d8+4d6+16)
**Fort** +7, **Ref** +3, **Will** +6; +2 vs. poison
**Resist** electricity 5

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Club|club]]_ +4 (1d6), bite –2 (1d4), claw –2 (1d4) or bite +3 (1d4), 2 claws +3 (1d4)
**Special Attacks** claws (1d6, 6 rounds/day)
**_Sorcerer_ Spells Known **(CL 4th; concentration +7)
2nd (4/day)—_[[spells/Acid Arrow|acid arrow]]_
1st (7/day)—_[[spells/Cause Fear|cause fear]]_ (DC 15), _[[spells/Corrosive Touch|corrosive touch]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 15), _[[spells/Summon Monster I|summon monster I]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Daze|daze]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 13), _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_
**Bloodline** Abyssal

##### Statistics
**Str** 10, **Dex** 13, **Con** 14, **Int** 10, **Wis** 13, **Cha** 16
**Base Atk** +3; **CMB** +3; **CMD** 14
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Silent Spell|Silent Spell]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation)
**Skills** Knowledge (arcana) +7, Knowledge (planes) +4, Spellcraft +6, Stealth +9 (+13 in rocky areas)
**Languages** Draconic
**SQ** bloodline arcana (summoned creatures gain DR 2/good)
**Combat Gear** potion of _[[spells/Cure Light Wounds|cure light wounds]]_, wand of _[[spells/Invisibility|invisibility]]_ (10 charges); **Other Gear** mwk _club_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, 150 gp

##### Ecology

**Environment** any underground

##### Description

Arcane casters often become scouts, as their divine counterparts monopolize the positions of power within the tribe. Most _troglodyte_ sorcerers have the Abyssal, Deep Earth (Pathfinder RPG Advanced Player’s Guide 137), Draconic, or Undead bloodline.
---
cssclass: [monsters]
title1: Lizardfolk, Lizardfolk Sorcerer
title2: Lizardfolk Sorcerer
CR: 12
sources:
- name: Monster Codex
  page: 146
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 19200
race: Lizardfolk
classes:
- sorcerer 11
alignment: CN
size: Medium
type: humanoid
subtypes:
- reptilian
initiative:
  bonus: 4
AC:
  AC: 21
  touch: 11
  flat_footed: 21
  components:
    armor: 4
    deflection: 1
    natural: 6
HP:
  HP: 97
  long: 2d8+11d6+50
  HD: 13
saves:
  fort: 10
  ref: 7
  will: 10
resistances:
  acid: 10
speeds:
  base: 30
  swim: 15
attacks:
  melee:
  - - text: 2 claws +10 (1d6+3 plus 1d6 acid)
      entries:
      - - damage: 1d6+3
        - damage: 1d6
          type: acid
      count: 2
      attack: claws
      bonus:
      - 10
    - text: bite +5 (1d4+1)
      entries:
      - - damage: 1d4+1
      attack: bite
      bonus:
      - 5
  special:
  - breath weapon (60-foot line, 11d6 acid, DC 19, 1/day)
  - claws (1d4+3 plus 1d6 acid, treated as magic weapons, 7 rounds/day)
spells:
  entries:
  - superscripts:
    - UM
    name: acidic spray
    source: Sorcerer
    level: 5
    DC: 19
  - name: spell resistance
    source: Sorcerer
    level: 5
  - name: wall of stone
    source: Sorcerer
    level: 5
    DC: 19
  - name: black tentacles
    source: Sorcerer
    level: 4
  - name: fear
    source: Sorcerer
    level: 4
    DC: 18
  - name: remove curse
    source: Sorcerer
    level: 4
  - superscripts:
    - UM
    name: vitriolic mist
    source: Sorcerer
    level: 4
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: fly
    source: Sorcerer
    level: 3
  - name: haste
    source: Sorcerer
    level: 3
  - name: major image
    source: Sorcerer
    level: 3
    DC: 17
  - name: wind wall
    source: Sorcerer
    level: 3
  - name: acid arrow
    source: Sorcerer
    level: 2
  - superscripts:
    - APG
    name: create pit
    source: Sorcerer
    level: 2
    DC: 16
  - name: darkvision
    source: Sorcerer
    level: 2
  - superscripts:
    - UM
    name: frigid touch
    source: Sorcerer
    level: 2
  - name: resist energy
    source: Sorcerer
    level: 2
  - name: web
    source: Sorcerer
    level: 2
    DC: 16
  - superscripts:
    - UM
    name: corrosive touch
    source: Sorcerer
    level: 1
  - name: endure elements
    source: Sorcerer
    level: 1
  - name: grease
    source: Sorcerer
    level: 1
    DC: 15
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: ray of enfeeblement
    source: Sorcerer
    level: 1
    DC: 15
  - name: shocking grasp
    source: Sorcerer
    level: 1
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: detect poison
    source: Sorcerer
    level: 0
  - name: open/close
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: resistance
    source: Sorcerer
    level: 0
  - superscripts:
    - APG
    name: spark
    source: Sorcerer
    level: 0
  - name: mending
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 11
    concentration: 15
    slots:
      5: 4
      4: 7
      3: 7
      2: 7
      1: 7
      0: at-will
    bloodline: draconic (black)
tactics:
  Before Combat: The sorcerer casts mage armor on herself.
  During Combat: The sorcerer stays away from melee, hurling spells at foes. She usually
    begins with black tentacles or grease, the better to restrict enemy mobility in
    the already difficult swamp terrain, then follows up with ranged damage spells
    or by casting haste on the tribe's strongest warriors.
  Base Statistics: Without mage armor, the lizardfolk's statistics are AC 17, touch
    11, flat-footed 17.
ability_scores:
  STR: 17
  DEX: 10
  CON: 15
  INT: 11
  WIS: 8
  CHA: 18
BAB: 6
CMB: 9
CMD: 27
feats:
- name: Combat Casting
- superscripts:
  - APG
  name: Elemental Focus (acid)
- name: Eschew Materials
- name: Improved Initiative
- name: Iron Will
- name: Lighting Reflexes
- superscripts:
  - APG
  name: Reach Spell
- name: Toughness
- name: Weapon Focus (claw)
skills:
  Acrobatics: 6
  Climb: 7
  Intimidate: 9
  Knowledge (arcana): 5
  Knowledge (nature): 3
  Linguistics: 1
  Perception: 4
  Spellcraft: 8
  Swim: 13
  Use Magic Device: 13
  _racial_mods:
    Acrobatics:
      _: 4
languages:
- Common
- Draconic
special_qualities:
- bloodline arcana (spells that deal acid damage deal +1 damage per die)
- hold breath
gear:
  combat:
  - potion of cure moderate wounds
  - scroll of false life
  - scrolls of invisibility (2)
  - wand of fireball (12 charges)
  - wand of magic missile (50 charges)
  other:
  - amulet of natural armor +1
  - cloak of resistance +2
  - headband of alluring charisma +2
  - ring of protection +1
  - 150 gp
ecology:
  environment: temperate swamps
desc_long: Lizardfolk sorcerers can have any bloodline, but most claim (rightly or
  not) that their magic is the result of ancient interbreeding with majestic dragons.
  With the blood of dragons coursing through her veins, the sorcerer is respected
  and feared by members of her tribe. They could see her as an omen-of good or ill-and
  might send her away to live on the outskirts of tribal land if she can't quickly
  learn to control her powers. Nevertheless, though the sorcerer might stand apart
  from the rest of her tribe, she almost always comes to her kin's defense in their
  times of need.

---

# Lizardfolk, Lizardfolk Sorcerer

**Source** Monster Codex pg. 146
**XP** 19,200
_[[monsters/Lizardfolk|Lizardfolk]]_ _[[classes/Sorcerer|sorcerer]]_ 11

CN Medium humanoid (reptilian)
**Init** +4; **Senses** Perception +4

##### Defense

**AC** 21, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+4 armor, +1 _[[spells/Deflection|deflection]]_, +6 natural)
**hp** 97 (13 HD; 2d8+11d6+50)
**Fort** +10, **Ref** +7, **Will** +10
**Resist** acid 10

##### Offense
**Speed** 30 ft., swim 15 ft.
**Melee** 2 claws +10 (1d6+3 plus 1d6 acid), bite +5 (1d4+1)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-foot line, 11d6 acid, DC 19, 1/day), claws (1d4+3 plus 1d6 acid, treated as magic weapons, 7 rounds/day)
**_Sorcerer_ Spells Known **(CL 11th; concentration +15)
5th (4/day)—_[[spells/Acidic Spray|acidic spray]]_ (DC 19), _[[universal monster rules/Spell Resistance|spell resistance]]_, _[[spells/Wall Of Stone|wall of stone]]_ (DC 19)
4th (7/day)—_[[spells/Black Tentacles|black tentacles]]_, _[[universal monster rules/Fear|fear]]_ (DC 18), _[[spells/Remove Curse|remove curse]]_, _[[spells/Vitriolic Mist|vitriolic mist]]_
3rd (7/day)—_[[spells/Dispel Magic|dispel magic]]_, fly, _[[spells/Haste|haste]]_, _[[spells/Major Image|major image]]_ (DC 17), _[[spells/Wind Wall|wind wall]]_
2nd (7/day)—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Create Pit|create pit]]_ (DC 16), _[[spells/Darkvision|darkvision]]_, _[[spells/Frigid Touch|frigid touch]]_, _[[spells/Resist Energy|resist energy]]_, web (DC 16)
1st (7/day)—_[[spells/Corrosive Touch|corrosive touch]]_, _[[spells/Endure Elements|endure elements]]_, _[[spells/Grease|grease]]_ (DC 15), _[[spells/Mage Armor|mage armor]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 15), _[[spells/Shocking Grasp|shocking grasp]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, open/close, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Spark|spark]]_, _[[spells/Mending|mending]]_, _[[spells/Message|message]]_
**Bloodline **draconic (black)

### Tactics

**Before Combat** The _sorcerer_ casts _mage armor_ on herself.
 **During Combat** The _sorcerer_ stays away from melee, hurling spells at foes. She usually begins with _black tentacles_ or _grease_, the better to restrict enemy _[[feats/Mobility|mobility]]_ in the already difficult swamp terrain, then follows up with ranged damage spells or by casting _haste_ on the tribe’s strongest warriors.
 **Base Statistics** Without _mage armor_, the _lizardfolk_’s statistics are **AC** 17, touch 11, _flat-footed_ 17.

##### Statistics
**Str** 17, **Dex** 10, **Con** 15, **Int** 11, **Wis** 8, **Cha** 18
**Base Atk** +6; **CMB** +9; **CMD** 27
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Elemental Focus|Elemental Focus]]_ (acid), _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, Lighting Reflexes, _[[feats/Reach Spell|Reach Spell]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Acrobatics +6, _[[universal monster rules/Climb|Climb]]_ +7, Intimidate +9, Knowledge (arcana) +5, Knowledge (nature) +3, Linguistics +1, Perception +4, Spellcraft +8, Swim +13, Use Magic Device +13; **Racial Modifiers** +4 Acrobatics
**Languages** Common, Draconic
**SQ** bloodline arcana (spells that deal acid damage deal +1 damage per die), _[[universal monster rules/Hold Breath|hold breath]]_
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, scroll of _[[spells/False Life|false life]]_, scrolls of _[[spells/Invisibility|invisibility]]_ (2), wand of _[[spells/Fireball|fireball]]_ (12 charges), wand of _[[spells/Magic Missile|magic missile]]_ (50 charges); **Other Gear** _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 150 gp

##### Ecology

**Environment** temperate swamps

##### Description

_Lizardfolk_ sorcerers can have any bloodline, but most claim (rightly or not) that their magic is the result of ancient interbreeding with majestic dragons. With the blood of dragons coursing through her veins, the _sorcerer_ is respected and feared by members of her tribe. They could see her as an omen—of good or ill—and might send her away to live on the outskirts of tribal land if she can’t quickly learn to control her powers. Nevertheless, though the _sorcerer_ might stand apart from the rest of her tribe, she almost always comes to her kin’s defense in their times of need.
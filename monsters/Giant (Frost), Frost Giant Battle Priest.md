---
cssclass: [monsters]
title1: Giant (Frost), Frost Giant Battle Priest
title2: Frost Giant Battle Priest
CR: 13
sources:
- name: Monster Codex
  page: 73
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 25600
race: Frost
classes:
- giant cleric 8
alignment: CE
size: Large
type: humanoid
subtypes:
- cold
- giant
initiative:
  bonus: -1
senses:
  low-light vision: true
AC:
  AC: 27
  touch: 9
  flat_footed: 27
  components:
    armor: 8
    deflection: 1
    dex: -1
    natural: 10
    size: -1
HP:
  HP: 195
  long: 22d8+96
saves:
  fort: 19
  ref: 7
  will: 16
defensive_abilities:
- rock catching
immunities:
- cold
weaknesses:
- vulnerable to fire
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 battleaxe +28/+23/+18/+13 (2d6+13/×3)
      entries:
      - - damage: 2d6+13
          crit_multiplier: 3
      attack: +1 battleaxe
      bonus:
      - 28
      - 23
      - 18
      - 13
  ranged:
  - - text: rock +14 (1d8+18)
      entries:
      - - damage: 1d8+18
      attack: rock
      bonus:
      - 14
  special:
  - channel negative energy 5/day (DC 16, 4d6)
  - might of the gods (+8, 8 rounds/day)
  - rock throwing (120 ft.)
  - weapon master (8 rounds/day)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: strength surge
    source: default
    freq: 9/day
    other: '+4'
  - name: battle rage
    source: default
    freq: 9/day
    other: '+4'
  sources:
  - name: default
    CL: 8
    concentration: 14
spells:
  entries:
  - superscripts:
    - APG
    name: blessing of fervor
    source: Cleric
    level: 4
  - superscripts:
    - UC
    name: communal protection from energy
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: divine power
    source: Cleric
    level: 4
  - name: unholy blight
    source: Cleric
    level: 4
    DC: 20
  - superscripts:
    - APG
    name: enter image
    source: Cleric
    level: 3
  - name: invisibility purge
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: magic vestment
    source: Cleric
    level: 3
  - name: protection from energy
    source: Cleric
    level: 3
  - superscripts:
    - APG
    name: sacred bond
    source: Cleric
    level: 3
  - name: align weapon
    source: Cleric
    level: 2
  - name: death knell
    source: Cleric
    level: 2
    DC: 18
  - name: hold person
    source: Cleric
    level: 2
    DC: 18
  - name: magic boulder
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: spiritual weapon
    source: Cleric
    level: 2
  - superscripts:
    - APG
    name: weapon of awe
    source: Cleric
    level: 2
  - name: bane
    source: Cleric
    level: 1
    DC: 17
  - name: bless
    source: Cleric
    level: 1
  - name: command
    source: Cleric
    level: 1
    DC: 17
  - name: cure light wounds
    source: Cleric
    level: 1
  - name: divine favor
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: enlarge person
    source: Cleric
    level: 1
    DC: 17
  - name: shield of faith
    source: Cleric
    level: 1
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: mending
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 8
    concentration: 14
    slots:
      0: at-will
    domains:
    - strength
    - war
tactics:
  Before Combat: A battle priest casts bull's strength, magic vestment, and protection
    from energy (fire) before combat, and sacred bond if her jarl is present.
  During Combat: The battle priest opens combat by casting divine power, then uses
    spells like blessing of fervor to support allies and unholy blight to harm opponents.
ability_scores:
  STR: 34
  DEX: 8
  CON: 18
  INT: 13
  WIS: 23
  CHA: 14
BAB: 16
CMB: 29
CMB_other: +31 sunder
CMD: 39
CMD_other: 41 vs. sunder
feats:
- name: Brew Potion
- name: Cleave
- name: Combat Casting
- name: Craft Magic Arms and Armor
- name: Craft Wand
- name: Great Cleave
- name: Improved Sunder
- name: Lightning Reflexes
- name: Martial Weapon Proficiency (battleaxe)
- name: Power Attack
- name: Vital Strike
skills:
  Climb: 17
  Craft (armor): 10
  Intimidate: 15
  Knowledge (religion): 14
  Perception: 30
  Spellcraft: 7
  Stealth: 1
    in snow: 5
  _racial_mods:
    Stealth:
      in snow: 4
languages:
- Abyssal
- Common
- Giant
special_qualities:
- icicle 9/day (1d6+3)
gear:
  combat:
  - potions of bull's strength (2)
  - potions of cure serious wounds (4)
  - potions of protection from energy (2)
  - potion of water breathing
  - wand of cure critical wounds (15 charges)
  - wand of cure moderate wounds (15 charges)
  other:
  - mwk chainmail
  - +1 battleaxe
  - amulet of natural armor +1
  - boots of the winterlands
  - headband of inspired wisdom +2
  - ring of protection +1
  - ring of sustenance
  - golden bracelets for sacred bond (2)
  - silver unholy symbol
  - spell component pouch
  - 4,410 gp
ecology:
  environment: cold mountains
desc_long: A frost giant battle priest uses her powers seeking out those who would
  undercut her authority or that of the chief, through spying on, manipulating, and
  threatening the rest of the tribe. When needed, she's not averse to taking up her
  battleaxe and splitting a few heads.

---

# Giant (Frost), Frost Giant Battle Priest

**Source** Monster Codex pg. 73
**XP** 25,600
Frost giant _[[classes/Cleric|cleric]]_ 8
CE Large humanoid (cold, giant)
**Init** –1; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +30

##### Defense

**AC** 27, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+8 armor, +1 deflection, –1 Dex, +10 natural, –1 size)
**hp** 195 (22d8+96)
**Fort** +19, **Ref** +7, **Will** +16
**Defensive Abilities** _[[universal monster rules/Rock Catching|rock catching]]_; **Immune** cold
**Weaknesses** vulnerable to fire

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon/Battleaxe|battleaxe]]_ +28/+23/+18/+13 (2d6+13/×3)
**Ranged** rock +14 (1d8+18)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** channel negative energy 5/day (DC 16, 4d6), might of the gods (+8, 8 rounds/day), _[[universal monster rules/Rock Throwing|rock throwing]]_ (120 ft.), weapon master (8 rounds/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +14)
9/day—strength surge (+4)
9/day—battle _[[spells/Rage|rage]]_ (+4)
**_Cleric_ Spells Prepared **(CL 8th; concentration +14)
4th—_[[spells/Blessing Of Fervor|blessing of fervor]]_, communal _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Divine Power|divine power]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 20)
3rd—_[[spells/Enter Image|enter image]]_, _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Magic Vestment|magic vestment]]_, _protection from energy_, _[[spells/Sacred Bond|sacred bond]]_
2nd—_[[spells/Align Weapon|align weapon]]_, _[[spells/Death Knell|death knell]]_ (DC 18), _[[spells/Hold Person|hold person]]_ (DC 18), _[[spells/Magic Boulder|magic boulder]]_, _[[spells/Spiritual Weapon|spiritual weapon]]_, _[[spells/Weapon of Awe|weapon of awe]]_
1st—_[[spells/Bane|bane]]_ (DC 17), _[[spells/Bless|bless]]_, _[[spells/Command|command]]_ (DC 17), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Enlarge Person|enlarge person]]_ (DC 17), _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Mending|mending]]_, _[[spells/Read Magic|read magic]]_
**D** domain spell; **Domains** Strength, War

### Tactics

**Before Combat** A battle priest casts bull’s strength, _magic vestment_, and _protection from energy_ (fire) before combat, and _sacred bond_ if her jarl is present.
 **During Combat** The battle priest opens combat by casting _divine power_, then uses spells like _blessing of fervor_ to support allies and _unholy blight_ to _[[spells/Harm|harm]]_ opponents.

##### Statistics
**Str** 34, **Dex** 8, **Con** 18, **Int** 13, **Wis** 23, **Cha** 14
**Base Atk** +16; **CMB** +29 (+31 sunder); **CMD** 39 (41 vs. sunder)
**Feats** _[[feats/Brew Potion|Brew Potion]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _[[feats/Craft Wand|Craft Wand]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Martial Weapon Proficiency|Martial Weapon Proficiency]]_ (_battleaxe_), _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +17, Craft (armor) +10, Intimidate +15, Knowledge (religion) +14, Perception +30, Spellcraft +7, Stealth +1 (+5 in snow); **Racial Modifiers** +4 Stealth in snow
**Languages** Abyssal, Common, Giant
**SQ** icicle 9/day (1d6+3)
**Combat Gear** potions of bull’s strength (2), potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (4), potions of _protection from energy_ (2), potion of _[[universal monster rules/Water Breathing|water breathing]]_, wand of _[[spells/Cure Critical Wounds|cure critical wounds]]_ (15 charges), wand of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (15 charges); **Other Gear** mwk _[[items/Armor/Chainmail|chainmail]]_, +1 _battleaxe_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Boots of the Winterlands|boots of the winterlands]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Ring/Ring of Sustenance|ring of sustenance]]_, golden bracelets for _sacred bond_ (2), silver _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 4,410 gp

##### Ecology

**Environment** cold mountains

##### Description

A frost giant battle priest uses her powers seeking out those who would undercut her authority or that of the chief, through spying on, manipulating, and threatening the rest of the tribe. When needed, she’s not averse to taking up her _battleaxe_ and splitting a few heads.
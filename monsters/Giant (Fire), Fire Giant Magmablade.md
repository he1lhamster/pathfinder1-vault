---
cssclass: [monsters]
title1: Giant (Fire), Fire Giant Magmablade
title2: Fire Giant Magmablade
CR: 17
sources:
- name: Monster Codex
  page: 60
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 102400
race: Fire
classes:
- giant magus 14 (Pathfinder RPG Ultimate Magic 9)
alignment: LE
size: Large
type: humanoid
subtypes:
- fire
- giant
initiative:
  bonus: 0
senses:
  low-light vision: true
AC:
  AC: 35
  touch: 10
  flat_footed: 35
  components:
    armor: 11
    deflection: 1
    natural: 10
    shield: 4
    size: -1
HP:
  HP: 253
  long: 29d8+123
saves:
  fort: 23
  ref: 10
  will: 20
defensive_abilities:
- rock catching
DR:
- amount: 10
  weakness: adamantine
  max_absorb: 140
immunities:
- fire
- magic missile
weaknesses:
- vulnerable to cold
speeds:
  base: 40
attacks:
  melee:
  - - text: +1 dispelling keen battleaxe +35/+30/+25/+20 (2d6+16/19-20/×3)
      entries:
      - - damage: 2d6+16
          crit_range: 19-20
          crit_multiplier: 3
      attack: +1 dispelling keen battleaxe
      bonus:
      - 35
      - 30
      - 25
      - 20
  - - text: 2 slams +33 (1d8+13)
      entries:
      - - damage: 1d8+13
      count: 2
      attack: slams
      bonus:
      - 33
  ranged:
  - - text: rock +21 (1d8+19 plus 1d6 fire)
      entries:
      - - damage: 1d8+19
        - damage: 1d6
          type: fire
      attack: rock
      bonus:
      - 21
  special:
  - greater spell combat
  - heated rock
  - improved spell combat
  - rock throwing (120 ft.)
  - spell combat (-2 attack, +2 concentration, double bonus)
  - spellstrike
space: 10
reach: 10
spells:
  entries:
  - superscripts:
    - APG
    name: geyser
    source: Magus
    level: 5
    DC: 20
  - name: telekinesis
    source: Magus
    level: 5
    DC: 20
  - name: wall of stone
    source: Magus
    level: 5
    DC: 20
  - superscripts:
    - UM
    name: arcana theft
    source: Magus
    level: 4
  - superscripts:
    - APG
    name: ball lightning
    source: Magus
    level: 4
    DC: 19
  - name: black tentacles
    source: Magus
    level: 4
  - name: stoneskin
    source: Magus
    level: 4
  - name: wall of fire
    source: Magus
    level: 4
  - name: blink
    source: Magus
    level: 3
  - name: dispel magic
    source: Magus
    level: 3
  - name: fireball
    source: Magus
    level: 3
    DC: 18
  - name: flame arrow
    source: Magus
    level: 3
  - name: fly
    source: Magus
    level: 3
  - name: alter self
    source: Magus
    level: 2
  - name: blur
    source: Magus
    level: 2
  - superscripts:
    - UC
    name: effortless armor
    source: Magus
    level: 2
  - superscripts:
    - APG
    name: elemental touch
    source: Magus
    level: 2
    DC: 17
  - name: invisibility
    source: Magus
    level: 2
  - name: scorching ray
    source: Magus
    level: 2
  - name: burning hands
    source: Magus
    level: 1
    DC: 16
  - name: enlarge person
    source: Magus
    level: 1
    DC: 16
  - name: expeditious retreat
    source: Magus
    level: 1
  - superscripts:
    - APG
    name: flare burst
    source: Magus
    level: 1
    DC: 16
  - name: magic missile
    source: Magus
    level: 1
  - superscripts:
    - UC
    name: mirror strike
    source: Magus
    level: 1
  - name: reduce person
    source: Magus
    level: 1
    DC: 16
  - name: acid splash
    source: Magus
    level: 0
  - name: detect magic
    source: Magus
    level: 0
  - name: flare
    source: Magus
    level: 0
    DC: 15
  - name: light
    source: Magus
    level: 0
  - superscripts:
    - APG
    name: spark
    source: Magus
    level: 0
  sources:
  - name: Magus
    type: prepared
    CL: 14
    concentration: 19
    slots:
      0: at-will
tactics:
  Before Combat: The magmablade casts effortless armor, stoneskin, and shield from
    a scroll.
  During Combat: The magmablade wades into battle, using a mix of spellstrike, spellcasting,
    and melee prowess, causing as much havoc as possible.
  Base Statistics: Without effortless armor, stoneskin, and shield, the magmablade's
    statistics are AC 31, touch 10, flat-footed 31; DR none; Immune fire; Speed 30
    ft.; Skills Climb +39, Fly +24.
ability_scores:
  STR: 36
  DEX: 11
  CON: 19
  INT: 20
  WIS: 16
  CHA: 10
BAB: 21
CMB: 35
CMB_other: +37 overrun, +37 sunder
CMD: 46
CMD_other: 48 vs. overrun, 48 vs. sunder
feats:
- superscripts:
  - UM
  name: Burning Spell
- name: Cleave
- name: Combat Casting
- name: Critical Focus
- name: Disruptive
- name: Great Cleave
- name: Improved Critical (battleaxe)
- name: Improved Overrun
- name: Improved Sunder
- name: Iron Will
- name: Maximize Spell
- name: Power Attack
- name: Quicken Spell
- name: Staggering Critical
- name: Stunning Critical
- name: Weapon Focus (battleaxe)
- name: Weapon Specialization (battleaxe)
skills:
  Climb: 41
  Craft (weapons): 37
  Fly: 26
  Intimidate: 32
  Knowledge (arcana): 15
  Perception: 35
  Spellcraft: 37
  Use Magic Device: 32
languages:
- Common
- Draconic
- Giant
- Infernal
- Orc
special_qualities:
- arcane pool (12 points, +4)
- fighter training (fighter level 7)
- heavy armor proficiency
- improved spell recall
- knowledge pool
- magus arcana (arcane edge, critical strike, maximized magic, spell shield)
- medium armor proficiency
gear:
  combat:
  - potions of cure serious wounds (2)
  - scroll of bear's endurance
  - scroll of haste
  - scrolls of shield (2)
  - wand of true strike (50 charges)
  other:
  - +3 spell storing stone coat (scorching ray)
  - +1 dispelling keen battleaxe
  - amulet of natural armor +2
  - cloak of resistance +1
  - headband of vast intelligence +4
  - pearl of power (3rd level)
  - ring of protection +1
  - granite and diamond dust worth 250 gp
ecology:
  environment: warm mountains
desc_long: Mixing force of arms with fiery magic, a magmablade is a tornado of flame
  and carnage.

---

# Giant (Fire), Fire Giant Magmablade

**Source** Monster Codex pg. 60
**XP** 102,400
Fire giant _[[classes/Magus|magus]]_ 14 (Pathfinder RPG Ultimate Magic 9)

LE Large humanoid (fire, giant)
**Init** +0; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +35

##### Defense

**AC** 35, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 35 (+11 armor, +1 deflection, +10 natural, +4 _[[spells/Shield|shield]]_, –1 size)
**hp** 253 (29d8+123)
**Fort** +23, **Ref** +10, **Will** +20
**Defensive Abilities** _[[universal monster rules/Rock Catching|rock catching]]_; **DR** 10/adamantine (140 points); **Immune** fire, _[[spells/Magic Missile|magic missile]]_
**Weaknesses** vulnerable to cold

##### Offense
**Speed** 40 ft.
**Melee** +1 _[[items/Weapon Magic Abilities/Dispelling|dispelling]]_ _[[items/Weapon Magic Abilities/Keen|keen]]_ _[[items/Weapon/Battleaxe|battleaxe]]_ +35/+30/+25/+20 (2d6+16/19–20/×3) or 2 slams +33 (1d8+13)
**Ranged** rock +21 (1d8+19 plus 1d6 fire)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** greater spell combat, heated rock, improved spell combat, _[[universal monster rules/Rock Throwing|rock throwing]]_ (120 ft.), spell combat (–2 attack, +2 concentration, double bonus), spellstrike
**_Magus_ Spells Prepared **(CL 14th; concentration +19)
5th—_[[spells/Geyser|geyser]]_ (DC 20), _[[spells/Telekinesis|telekinesis]]_ (DC 20), _[[spells/Wall Of Stone|wall of stone]]_ (DC 20)
4th—_[[spells/Arcana Theft|arcana theft]]_, _[[spells/Ball Lightning|ball lightning]]_ (DC 19), _[[spells/Black Tentacles|black tentacles]]_, _[[spells/Stoneskin|stoneskin]]_, _[[spells/Wall Of Fire|wall of fire]]_
3rd—_[[spells/Blink|blink]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Fireball|fireball]]_ (DC 18), _[[spells/Flame Arrow|flame arrow]]_, fly
2nd—_[[spells/Alter Self|alter self]]_, _[[spells/Blur|blur]]_, _[[spells/Effortless Armor|effortless armor]]_, _[[spells/Elemental Touch|elemental touch]]_ (DC 17), _[[spells/Invisibility|invisibility]]_, _[[spells/Scorching Ray|scorching ray]]_
1st—_[[spells/Burning Hands|burning hands]]_ (DC 16), _[[spells/Enlarge Person|enlarge person]]_ (DC 16), _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Flare Burst|flare burst]]_ (DC 16), _magic missile_, _[[spells/Mirror Strike|mirror strike]]_, _[[spells/Reduce Person|reduce person]]_ (DC 16)
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 15), light, _[[spells/Spark|spark]]_

### Tactics

**Before Combat** The magmablade casts _effortless armor_, _stoneskin_, and _shield_ from a scroll.
 **During Combat** The magmablade wades into battle, using a mix of spellstrike, spellcasting, and melee prowess, causing as much havoc as possible.
 **Base Statistics** Without _effortless armor_, _stoneskin_, and _shield_, the magmablade’s statistics are **AC** 31, touch 10, _flat-footed_ 31; **DR** none; **Immune** fire; **Speed** 30 ft.; **Skills** _[[universal monster rules/Climb|Climb]]_ +39, Fly +24.

##### Statistics
**Str** 36, **Dex** 11, **Con** 19, **Int** 20, **Wis** 16, **Cha** 10
**Base Atk** +21; **CMB** +35 (+37 overrun, +37 sunder); **CMD** 46 (48 vs. overrun, 48 vs. sunder)
**Feats** _[[feats/Burning Spell|Burning Spell]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Disruptive|Disruptive]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Critical|Improved Critical]]_ (_battleaxe_), _[[feats/Improved Overrun|Improved Overrun]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Maximize Spell|Maximize Spell]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Stunning Critical|Stunning Critical]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_battleaxe_), _[[feats/Weapon Specialization|Weapon Specialization]]_ (_battleaxe_)
**Skills** _Climb_ +41, Craft (weapons) +37, Fly +26, Intimidate +32, Knowledge (arcana) +15, Perception +35, Spellcraft +37, Use Magic Device +32
**Languages** Common, Draconic, Giant, Infernal, _[[monsters/Orc|Orc]]_
**SQ** arcane pool (12 points, +4), _[[classes/Fighter|fighter]]_ _[[items/Weapon Magic Abilities/Training|training]]_ (_fighter_ level 7), _[[feats/Heavy Armor Proficiency|heavy armor proficiency]]_, improved spell recall, knowledge pool, _magus_ arcana (arcane edge, critical strike, maximized magic, spell _shield_), _[[feats/Medium Armor Proficiency|medium armor proficiency]]_
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), scroll of bear’s _[[feats/Endurance|endurance]]_, scroll of _[[spells/Haste|haste]]_, scrolls of _shield_ (2), wand of _[[spells/True Strike|true strike]]_ (50 charges); **Other Gear** +3 _[[items/Weapon Magic Abilities/Spell Storing|spell storing]]_ stone coat (_scorching ray_), +1 _dispelling_ _keen_ _battleaxe_, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of Vast Intelligence +4|headband of vast intelligence +4]]_, pearl of power (3rd level), _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, granite and diamond dust worth 250 gp

##### Ecology

**Environment** warm mountains

##### Description

Mixing force of arms with fiery magic, a magmablade is a tornado of flame and carnage.
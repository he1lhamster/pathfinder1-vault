---
cssclass: [monsters]
title1: Ghoul, Ancient Gravedigger
title2: Ancient Gravedigger
CR: 10
sources:
- name: Monster Codex
  page: 86
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 9600
race: Ghoul
classes:
- oracle 10 (Pathfinder RPG Advanced Player's Guide 42)
alignment: CE
size: Medium
type: undead
initiative:
  bonus: 4
senses:
  darkvision: 60
AC:
  AC: 22
  touch: 14
  flat_footed: 18
  components:
    armor: 4
    deflection: 1
    dex: 4
    natural: 3
HP:
  HP: 112
  long: 12d8+58
saves:
  fort: 8
  ref: 8
  will: 13
defensive_abilities:
- channel resistance +2
immunities:
- undead traits
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 bite +14 (1d6+6 plus disease and paralysis)
      entries:
      - - damage: 1d6+6
        - effect: disease
        - effect: paralysis
      attack: +1 bite
      bonus:
      - 14
    - text: 2 +1 frost claws +15 (1d6+6 plus 1d6 cold, disease, and paralysis)
      entries:
      - - damage: 1d6+6
        - damage: 1d6
          type: cold
        - effect: disease
        - effect: paralysis
      count: 2
      attack: +1 frost claws
      bonus:
      - 15
  ranged:
  - - text: rock +13/+8 (2d4+7)
      entries:
      - - damage: 2d4+7
      attack: rock
      bonus:
      - 13
      - 8
  special:
  - disease (DC 15)
  - paralysis (1d4+1 rounds, DC 15, elves are immune to this effect)
spells:
  entries:
  - name: flame strike
    source: Oracle
    level: 5
    DC: 19
  - name: mass inflict light wounds
    source: Oracle
    level: 5
  - name: stoneskin
    source: Oracle
    level: 5
  - name: divine power
    source: Oracle
    level: 4
  - name: inflict critical wounds
    source: Oracle
    level: 4
  - name: summon monster IV
    source: Oracle
    level: 4
  - name: wall of stone
    source: Oracle
    level: 4
    DC: 18
  - name: animate dead
    source: Oracle
    level: 3
  - name: blindness/deafness
    source: Oracle
    level: 3
    DC: 17
  - name: dispel magic
    source: Oracle
    level: 3
  - name: inflict serious wounds
    source: Oracle
    level: 3
  - name: meld into stone
    source: Oracle
    level: 3
  - name: darkness
    source: Oracle
    level: 2
  - name: desecrate
    source: Oracle
    level: 2
  - name: hold person
    source: Oracle
    level: 2
    DC: 16
  - name: inflict moderate wounds
    source: Oracle
    level: 2
  - name: spiritual weapon
    source: Oracle
    level: 2
  - superscripts:
    - APG
    name: stone call
    source: Oracle
    level: 2
  - name: command
    source: Oracle
    level: 1
    DC: 15
  - name: entropic shield
    source: Oracle
    level: 1
  - name: inflict light wounds
    source: Oracle
    level: 1
  - superscripts:
    - UC
    name: liberating command
    source: Oracle
    level: 1
  - name: magic stone
    source: Oracle
    level: 1
  - name: obscuring mist
    source: Oracle
    level: 1
  - name: shield of faith
    source: Oracle
    level: 1
  - name: bleed
    source: Oracle
    level: 0
    DC: 14
  - name: create water
    source: Oracle
    level: 0
  - name: detect magic
    source: Oracle
    level: 0
  - name: detect poison
    source: Oracle
    level: 0
  - name: guidance
    source: Oracle
    level: 0
  - name: mending
    source: Oracle
    level: 0
  - name: read magic
    source: Oracle
    level: 0
  - name: resistance
    source: Oracle
    level: 0
  - superscripts:
    - APG
    name: spark
    source: Oracle
    level: 0
  sources:
  - name: Oracle
    type: known
    CL: 10
    concentration: 14
    slots:
      5: 3
      4: 6
      3: 7
      2: 7
      1: 7
      0: at-will
    mystery: stone
tactics:
  Before Combat: The ancient gravedigger prepares for combat by quaffing potions of
    greater magic fang and mage armor. He uses earth glide and crystal sight to observe
    foes fighting his underlings before he attacks.
  During Combat: The ancient gravedigger prefers to fight at range, relying on summoned
    creatures, flame strike, and spiritual weapon to deal damage while he uses earth
    glide and crystal sight to take cover from the fray. If he must enter melee, the
    gravedigger fights viciously.
  Base Statistics: Without greater magic fang and mage armor, the ancient gravedigger's
    statistics are AC 18, touch 15, flat-footed 14; Melee bite +13 (1d6+5 plus disease
    and paralysis), 2 frost claws +14 (1d6+5 plus 1d6 cold, disease, and paralysis).
ability_scores:
  STR: 20
  DEX: 18
  CON:
  INT: 15
  WIS: 14
  CHA: 18
BAB: 8
CMB: 13
CMB_other: +17 trip
CMD: 27
CMD_other: 31 vs. bull rush, 33 vs. trip
feats:
- name: Combat Reflexes
- name: Extra Rage
- name: Greater Trip
- name: Improved Natural Armor
- name: Improved Trip
- name: Power Attack
- name: Quick Draw
- name: Weapon Focus (claw)
skills:
  Bluff: 16
  Diplomacy: 19
  Intimidate: 19
  Perception: 17
  Spellcraft: 17
  Stealth: 18
languages:
- Aklo
- Common
- Draconic
- Terran
- Undercommon
- tongues (understands only)
special_qualities:
- oracle's curse (tongues [Aklo])
- revelations (crystal sight, earth glide, rock throwing, stone stability)
gear:
  combat:
  - potion of greater magic fang
  - potion of mage armor
  other:
  - belt of giant strength +2
  - cloak of resistance +1
  - frost amulet of mighty fists
  - ring of protection +1
  - throwing stones (10)
  - onyx gems (worth 1,000 gp total)
  - silver dust (worth 25 gp)
ecology:
  environment: any land
desc_long: Years of digging up graves have given this ancient ghoul an affinity for
  earth magic. Powerful spellcasting ghouls usually rise to positions of leadership,
  and in his ghoul city, this gravedigger is a high-ranking member of the ruling elite.

---

# Ghoul, Ancient Gravedigger

**Source** Monster Codex pg. 86
**XP** 9,600
_[[monsters/Ghoul|Ghoul]]_ _[[classes/Oracle|oracle]]_ 10 (Pathfinder RPG Advanced Player’s Guide 42)
CE Medium undead
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +17

##### Defense

**AC** 22, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+4 armor, +1 _[[spells/Deflection|deflection]]_, +4 Dex, +3 natural)
**hp** 112 (12d8+58)
**Fort** +8, **Ref** +8, **Will** +13
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +2; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 30 ft.
**Melee** +1 bite +14 (1d6+6 plus disease and _[[universal monster rules/Paralysis|paralysis]]_), 2 +1 frost claws +15 (1d6+6 plus 1d6 cold, disease, and _paralysis_)
**Ranged** rock +13/+8 (2d4+7)
**Special Attacks** disease (DC 15), _paralysis_ (1d4+1 rounds, DC 15, elves are immune to this effect)
**_Oracle_ Spells Known **(CL 10th; concentration +14)
5th (3/day)—_[[spells/Flame Strike|flame strike]]_ (DC 19), mass _[[spells/Inflict Light Wounds|inflict light wounds]]_, _[[spells/Stoneskin|stoneskin]]_
4th (6/day)—_[[spells/Divine Power|divine power]]_, _[[spells/Inflict Critical Wounds|inflict critical wounds]]_, _[[spells/Summon Monster IV|summon monster IV]]_, _[[spells/Wall Of Stone|wall of stone]]_ (DC 18)
3rd (7/day)—_[[spells/Animate Dead|animate dead]]_, blindness/deafness (DC 17), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Inflict Serious Wounds|inflict serious wounds]]_, _[[spells/Meld into Stone|meld into stone]]_
2nd (7/day)—_[[spells/Darkness|darkness]]_, _[[spells/Desecrate|desecrate]]_, _[[spells/Hold Person|hold person]]_ (DC 16), _[[spells/Inflict Moderate Wounds|inflict moderate wounds]]_, _[[spells/Spiritual Weapon|spiritual weapon]]_, _[[spells/Stone Call|stone call]]_
1st (7/day)—_[[spells/Command|command]]_ (DC 15), _[[spells/Entropic Shield|entropic shield]]_, _inflict light wounds_, _[[spells/Liberating Command|liberating command]]_, _[[spells/Magic Stone|magic stone]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 14), _[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Guidance|guidance]]_, _[[spells/Mending|mending]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Spark|spark]]_
**Mystery** stone

### Tactics

**Before Combat** The ancient gravedigger prepares for combat by quaffing potions of greater _[[spells/Magic Fang|magic fang]]_ and _[[spells/Mage Armor|mage armor]]_. He uses _[[universal monster rules/Earth Glide|earth glide]]_ and crystal sight to observe foes fighting his underlings before he attacks.
 **During Combat** The ancient gravedigger prefers to fight at range, relying on summoned creatures, _flame strike_, and _spiritual weapon_ to deal damage while he uses _earth glide_ and crystal sight to take cover from the fray. If he must enter melee, the gravedigger fights viciously.
 **Base Statistics** Without greater _magic fang_ and _mage armor_, the ancient gravedigger’s statistics are **AC **18, touch 15, _flat-footed_ 14; **Melee **bite +13 (1d6+5 plus disease and _paralysis_), 2 frost claws +14 (1d6+5 plus 1d6 cold, disease, and _paralysis_).

##### Statistics
**Str** 20, **Dex** 18, **Con** —, **Int** 15, **Wis** 14, **Cha** 18
**Base Atk** +8; **CMB** +13 (+17 _[[universal monster rules/Trip|trip]]_); **CMD** 27 (31 vs. bull rush, 33 vs. _trip_)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Extra Rage|Extra Rage]]_, _[[feats/Greater Trip|Greater Trip]]_, _[[feats/Improved Natural Armor|Improved Natural Armor]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quick Draw|Quick Draw]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Bluff +16, Diplomacy +19, Intimidate +19, Perception +17, Spellcraft +17, Stealth +18
**Languages** Aklo, Common, Draconic, Terran, Undercommon; _[[spells/Tongues|tongues]]_ (understands only)
**SQ** _oracle_’s curse (_tongues_ [Aklo]), revelations (crystal sight, _earth glide_, _[[universal monster rules/Rock Throwing|rock throwing]]_, stone stability)
**Combat Gear** potion of greater _magic fang_, potion of _mage armor_; **Other Gear** _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, frost amulet of mighty fists, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Weapon Magic Abilities/Throwing|throwing]]_ stones (10), onyx gems (worth 1,000 gp total), silver dust (worth 25 gp)

##### Ecology

**Environment** any land

##### Description

Years of digging up graves have given this ancient _ghoul_ an affinity for _[[feats/Earth Magic|earth magic]]_. Powerful spellcasting ghouls usually rise to positions of _[[feats/Leadership|leadership]]_, and in his _ghoul_ city, this gravedigger is a high-ranking member of the ruling elite.
---
cssclass: [monsters]
title1: Giant (Fire), Fire Giant Doombringer
title2: Fire Giant Doombringer
CR: 18
sources:
- name: Monster Codex
  page: 61
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 153600
race: Fire
classes:
- giant oracle 16 (Pathfinder RPG Advanced Player's Guide 42)
alignment: LE
size: Large
type: humanoid
subtypes:
- fire
- giant
initiative:
  bonus: 6
senses:
  low-light vision: true
AC:
  AC: 32
  touch: 12
  flat_footed: 30
  components:
    armor: 9
    deflection: 1
    dex: 2
    natural: 8
    shield: 3
    size: -1
HP:
  HP: 341
  long: 31d8+202
saves:
  fort: 20
  ref: 12
  will: 20
  other: +4 vs. disease, death effects, mind-affecting effects, poison, sleep, stunning
defensive_abilities:
- rock catching
DR:
- amount: 2
  weakness: '-'
immunities:
- fire
weaknesses:
- vulnerable to cold
speeds:
  base: 30
attacks:
  melee:
  - - text: +2 conductive flail +35/+30/+25/+20 (2d6+12)
      entries:
      - - damage: 2d6+12
      attack: +2 conductive flail
      bonus:
      - 35
      - 30
      - 25
      - 20
  ranged:
  - - text: rock +25 (1d8+14 plus 1d6 fire)
      entries:
      - - damage: 1d8+14
        - damage: 1d6
          type: fire
      attack: rock
      bonus:
      - 25
  special:
  - heated rock
  - rock throwing (120 ft.)
space: 10
reach: 10
spells:
  entries:
  - name: fire storm
    source: Oracle
    level: 8
    DC: 24
  - name: incendiary cloud
    source: Oracle
    level: 8
    DC: 24
  - name: mass inflict critical wounds
    source: Oracle
    level: 8
    DC: 24
  - name: blasphemy
    source: Oracle
    level: 7
    DC: 23
  - name: destruction
    source: Oracle
    level: 7
    DC: 23
  - name: mass inflict serious wounds
    source: Oracle
    level: 7
    DC: 23
  - name: vision
    source: Oracle
    level: 7
    DC: 23
  - name: barrier blade
    source: Oracle
    level: 6
  - name: circle of death
    source: Oracle
    level: 6
    DC: 22
  - name: harm
    source: Oracle
    level: 6
    DC: 22
  - name: mass bull's strength
    source: Oracle
    level: 6
  - name: mass inflict moderate wounds
    source: Oracle
    level: 6
    DC: 22
  - name: dispel good
    source: Oracle
    level: 5
    DC: 21
  - name: greater command
    source: Oracle
    level: 5
    DC: 21
  - name: insect plague
    source: Oracle
    level: 5
    DC: 21
  - name: mass inflict light wounds
    source: Oracle
    level: 5
    DC: 21
  - name: righteous might
    source: Oracle
    level: 5
  - name: slay living
    source: Oracle
    level: 5
    DC: 21
  - superscripts:
    - APG
    name: blessing of fervor
    source: Oracle
    level: 4
  - name: greater magic weapon
    source: Oracle
    level: 4
  - name: ice storm
    source: Oracle
    level: 4
    DC: 20
  - name: imbue with spell ability
    source: Oracle
    level: 4
  - name: inflict critical wounds
    source: Oracle
    level: 4
    DC: 20
  - name: unholy blight
    source: Oracle
    level: 4
    DC: 20
  - name: dispel magic
    source: Oracle
    level: 3
  - name: inflict serious wounds
    source: Oracle
    level: 3
    DC: 19
  - name: invisibility purge
    source: Oracle
    level: 3
  - name: magic circle against good
    source: Oracle
    level: 3
  - name: stone shape
    source: Oracle
    level: 3
  - name: explosive runes
    source: Oracle
    level: 3
  - name: bear's endurance
    source: Oracle
    level: 2
  - name: darkness
    source: Oracle
    level: 2
  - name: death knell
    source: Oracle
    level: 2
    DC: 18
  - name: inflict moderate wounds
    source: Oracle
    level: 2
  - superscripts:
    - APG
    name: oracle's burden
    source: Oracle
    level: 2
    DC: 18
  - superscripts:
    - APG
    name: share language
    source: Oracle
    level: 2
  - name: summon swarm
    source: Oracle
    level: 2
  - name: bane
    source: Oracle
    level: 1
    DC: 17
  - name: cause fear
    source: Oracle
    level: 1
    DC: 17
  - name: deathwatch
    source: Oracle
    level: 1
  - name: doom
    source: Oracle
    level: 1
    DC: 17
  - name: inflict light wounds
    source: Oracle
    level: 1
    DC: 17
  - name: obscuring mist
    source: Oracle
    level: 1
  - name: shield of faith
    source: Oracle
    level: 1
  - name: bleed
    source: Oracle
    level: 0
    DC: 16
  - name: create water
    source: Oracle
    level: 0
  - name: detect magic
    source: Oracle
    level: 0
  - name: detect poison
    source: Oracle
    level: 0
  - name: purify food and drink
    source: Oracle
    level: 0
  - name: guidance
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
    CL: 16
    concentration: 22
    slots:
      8: 3
      7: 5
      6: 7
      5: 7
      4: 7
      3: 7
      2: 8
      1: 8
      0: at-will
    mystery: apocalypse
ability_scores:
  STR: 31
  DEX: 15
  CON: 23
  INT: 10
  WIS: 16
  CHA: 22
BAB: 23
CMB: 34
CMB_other: +36 overrun, +36 sunder
CMD: 47
CMD_other: 49 vs. overrun, 49 vs. sunder
feats:
- name: Cleave
- name: Combat Casting
- name: Critical Focus
- name: Empower Spell
- superscripts:
  - APG
  name: Extra Revelation
- name: Great Cleave
- name: Improved Initiative
- name: Improved Overrun
- name: Improved Sunder
- name: Iron Will
- name: Martial Weapon Proficiency (flail)
- name: Maximize Spell
- name: Power Attack
- name: Quicken Spell
- superscripts:
  - APG
  name: Selective Spell
- name: Weapon Focus (flail)
skills:
  Climb: 19
  Craft (armor): 8
  Heal: 21
  Intimidate: 17
  Perception: 32
  Spellcraft: 34
languages:
- Common
- Giant
- tongues
special_qualities:
- oracle's curse (tongues)
- revelations (doomsayer [30 ft., swift action], erosion touch [16d6, 5/day], near
  death, pass the torch [4/day, up to 8 rounds], power of the fallen [6/day], spell
  blast)
gear:
  combat:
  - potions of cure serious wounds (3)
  - scroll of mass bear's endurance
  - scroll of wall of stone
  - wand of bestow curse (15 charges)
  other:
  - +3 unrighteous adamantine breastplate
  - +2 light steel shield
  - +2 conductive flail
  - belt of physical might +2 (Str, Dex)
  - headband of alluring charisma +4
  - ring of protection +1
  - spell component pouch
  - 495 gp
ecology:
  environment: warm mountains
desc_long: With a single pronouncement from a doombringer, an entire settlement can
  be reduced to cinder and ash.

---

# Giant (Fire), Fire Giant Doombringer

**Source** Monster Codex pg. 61
**XP** 153,600
Fire giant _[[classes/Oracle|oracle]]_ 16 (Pathfinder RPG Advanced Player’s Guide 42)

LE Large humanoid (fire, giant)
**Init** +6; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +32

##### Defense

**AC** 32, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+9 armor, +1 deflection, +2 Dex, +8 natural, +3 _[[spells/Shield|shield]]_, –1 size)
**hp** 341 (31d8+202)
**Fort** +20, **Ref** +12, **Will** +20; +4 vs. disease, death effects, mind-affecting effects, poison, sleep, stunning
**Defensive Abilities** _[[universal monster rules/Rock Catching|rock catching]]_; **DR** 2/—; **Immune** fire
**Weaknesses** vulnerable to cold

##### Offense
**Speed** 30 ft.
**Melee** +2 _[[items/Weapon Magic Abilities/Conductive|conductive]]_ flail +35/+30/+25/+20 (2d6+12)
**Ranged** rock +25 (1d8+14 plus 1d6 fire)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** heated rock, _[[universal monster rules/Rock Throwing|rock throwing]]_ (120 ft.)
**_Oracle_ Spells Known **(CL 16th; concentration +22)
8th (3/day)—_[[spells/Fire Storm|fire storm]]_ (DC 24), _[[spells/Incendiary Cloud|incendiary cloud]]_ (DC 24), mass _[[spells/Inflict Critical Wounds|inflict critical wounds]]_ (DC 24)
7th (5/day)—_[[spells/Blasphemy|blasphemy]]_ (DC 23), _[[spells/Destruction|destruction]]_ (DC 23), mass _[[spells/Inflict Serious Wounds|inflict serious wounds]]_ (DC 23), _[[spells/Vision|vision]]_ (DC 23)
6th (7/day)—barrier blade, _[[spells/Circle Of Death|circle of death]]_ (DC 22), _[[spells/Harm|harm]]_ (DC 22), mass bull’s strength, mass _[[spells/Inflict Moderate Wounds|inflict moderate wounds]]_ (DC 22)
5th (7/day)—_[[spells/Dispel Good|dispel good]]_ (DC 21), greater _[[spells/Command|command]]_ (DC 21), _[[spells/Insect Plague|insect plague]]_ (DC 21), mass _[[spells/Inflict Light Wounds|inflict light wounds]]_ (DC 21), _[[spells/Righteous Might|righteous might]]_, _[[spells/Slay Living|slay living]]_ (DC 21)
4th (7/day)—_[[spells/Blessing Of Fervor|blessing of fervor]]_, greater _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Ice Storm|ice storm]]_ (DC 20), _[[spells/Imbue with Spell Ability|imbue with spell ability]]_, _inflict critical wounds_ (DC 20), _[[spells/Unholy Blight|unholy blight]]_ (DC 20)
3rd (7/day)—_[[spells/Dispel Magic|dispel magic]]_, _inflict serious wounds_ (DC 19), _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Magic Circle against Good|magic circle against good]]_, _[[spells/Stone Shape|stone shape]]_, _[[spells/Explosive Runes|explosive runes]]_
2nd (8/day)—bear’s _[[feats/Endurance|endurance]]_, _[[spells/Darkness|darkness]]_, _[[spells/Death Knell|death knell]]_ (DC 18), _inflict moderate wounds_, _oracle_’s burden (DC 18), _[[spells/Share Language|share language]]_, _[[spells/Summon Swarm|summon swarm]]_
1st (8/day)—_[[spells/Bane|bane]]_ (DC 17), _[[spells/Cause Fear|cause fear]]_ (DC 17), _[[spells/Deathwatch|deathwatch]]_, _[[spells/Doom|doom]]_ (DC 17), _inflict light wounds_ (DC 17), _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 16), _[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Purify Food and Drink|purify food and drink]]_, _[[spells/Guidance|guidance]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Spark|spark]]_
**Mystery** apocalypse

##### Statistics
**Str** 31, **Dex** 15, **Con** 23, **Int** 10, **Wis** 16, **Cha** 22
**Base Atk** +23; **CMB** +34 (+36 overrun, +36 sunder); **CMD** 47 (49 vs. overrun, 49 vs. sunder)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Extra Revelation|Extra Revelation]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Overrun|Improved Overrun]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Martial Weapon Proficiency|Martial Weapon Proficiency]]_ (flail), _[[feats/Maximize Spell|Maximize Spell]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Selective Spell|Selective Spell]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (flail)
**Skills** _[[universal monster rules/Climb|Climb]]_ +19, Craft (armor) +8, _[[spells/Heal|Heal]]_ +21, Intimidate +17, Perception +32, Spellcraft +34
**Languages** Common, Giant; _[[spells/Tongues|tongues]]_
**SQ** _oracle_’s curse (_tongues_), revelations (_[[npcs/Doomsayer|doomsayer]]_ [30 ft., swift action], erosion touch [16d6, 5/day], near death, pass the _[[items/Mundane/Torch|torch]]_ [4/day, up to 8 rounds], power of the _[[monsters/Fallen|fallen]]_ [6/day], spell blast)
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (3), scroll of mass bear’s _endurance_, scroll of _[[spells/Wall Of Stone|wall of stone]]_, wand of _[[spells/Bestow Curse|bestow curse]]_ (15 charges); **Other Gear** +3 _[[items/Armor Magic Abilities/Unrighteous|unrighteous]]_ _[[items/Armor/Adamantine Breastplate|adamantine breastplate]]_, +2 _[[items/Shield/Light steel shield|light steel shield]]_, +2 _conductive_ flail, _[[items/Wondrous Item/Belt of Physical Might +2|belt of physical might +2]]_ (Str, Dex), _[[items/Wondrous Item/Headband of Alluring Charisma +4|headband of alluring charisma +4]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 495 gp

##### Ecology

**Environment** warm mountains

##### Description

With a single pronouncement from a doombringer, an entire settlement can be reduced to cinder and ash.
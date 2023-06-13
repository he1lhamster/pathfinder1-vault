---
cssclass: [monsters]
second_statblock: true
title1: Duergar Strandrider
desc_short: This stout, gray-skinned warrior sits astride an enormous spider.
title2: Duergar Strandrider
CR: 8
sources:
- name: Tombs of Golarion
  page: 32
  link: http://paizo.com/products/btpy98yu?Pathfinder-Campaign-Setting-Tombs-of-Golarion
XP: 4800
race: Duergar
classes:
- cavalier (beast rider) 9
alignment: LE
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 6
senses:
  darkvision: 120
AC:
  AC: 20
  touch: 12
  flat_footed: 18
  components:
    armor: 8
    dex: 2
HP:
  HP: 81
  long: 9d10+27
saves:
  fort: 10
  ref: 8
  will: 6
  other: +2 vs. spells
immunities:
- paralysis
- phantasms
- poison
weaknesses:
- light sensitivity
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 lance +13/+8 (1d8+5/×3)
      entries:
      - - damage: 1d8+5
          crit_multiplier: 3
      attack: +1 lance
      bonus:
      - 13
      - 8
  - - text: mwk bardiche +13/+8 (1d10+4/19-20)
      entries:
      - - damage: 1d10+4
          crit_range: 19-20
      attack: mwk bardiche
      bonus:
      - 13
      - 8
  - - text: mwk cestus +13/+8 (1d4+3/19-20)
      entries:
      - - damage: 1d4+3
          crit_range: 19-20
      attack: mwk cestus
      bonus:
      - 13
      - 8
  ranged:
  - - text: sling +11 (1d4+3)
      entries:
      - - damage: 1d4+3
      attack: sling
      bonus:
      - 11
  special:
  - banner +2
  - cavalier's charge
  - challenge 3/day (+9 damage, +3 to hit while riding mount)
  - greater tactician 2/day (Outflank or Precise Strike, swift action, 7 rounds)
spell_like_abilities:
  entries:
  - name: enlarge person
    source: default
    freq: 1/day
    other: self only
  - name: invisibility
    source: default
    freq: 1/day
    other: self only
  sources:
  - name: default
    CL: 9
    concentration: 7
ability_scores:
  STR: 16
  DEX: 14
  CON: 16
  INT: 8
  WIS: 14
  CHA: 6
BAB: 9
CMB: 12
CMB_other: +14 overrun
CMD: 24
CMD_other: 28 vs. bull rush, 26 vs. overrun, 28 vs. trip
feats:
- superscripts:
  - APG
  name: Charge Through
- name: Cleave
- name: Improved Initiative
- name: Improved Overrun
- name: Mounted Combat
- superscripts:
  - APG
  name: Outflank
- name: Power Attack
- superscripts:
  - APG
  name: Precise Strike
- name: Ride-By Attack
skills:
  Handle Animal: 10
  Intimidate: 10
  Perception: 6
  Ride: 11
  Sense Motive: 2
    when opposing a Bluff check: 6
  Stealth: 8
  _racial_mods:
    Stealth:
      _: 4
languages:
- Common
- Dwarven
- Undercommon
special_qualities:
- mount (giant spider)
- mounted mastery
- order of the sword
gear:
  combat:
  - potion of cure serious wounds
  other:
  - +2 agile breastplate
  - +1 lance
  - mwk bardiche
  - mwk cestus
  - sling with 10 bullets
  - cloak of resistance +1
  - simple banners (2)
  - 420 gp
desc_long: ''

---

# Duergar Strandrider
This stout, gray-skinned warrior sits astride an enormous spider.
**Source** Tombs of Golarion pg. 32
**XP** 4,800
_[[monsters/Duergar|Duergar]]_ _[[classes/Cavalier|cavalier]]_ (_[[feats/Beast Rider|beast rider]]_) 9

LE Medium humanoid (dwarf)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +6

##### Defense

**AC** 20, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+8 armor, +2 Dex)
**hp** 81 (9d10+27)
**Fort** +10, **Ref** +8, **Will** +6; +2 vs. spells
**Immune** _[[universal monster rules/Paralysis|paralysis]]_, phantasms, poison
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Lance|lance]]_ +13/+8 (1d8+5/×3) or mwk _[[items/Weapon/Bardiche|bardiche]]_ +13/+8 (1d10+4/19–20) or mwk _[[items/Weapon/Cestus|cestus]]_ +13/+8 (1d4+3/19–20)
**Ranged** _[[items/Weapon/Sling|sling]]_ +11 (1d4+3)
**Special Attacks** _[[items/Mundane/Banner|banner]]_ +2, _cavalier_’s charge, challenge 3/day (+9 damage, +3 to hit while riding _[[spells/Mount|mount]]_), greater tactician 2/day (_[[feats/Outflank|Outflank]]_ or _[[feats/Precise Strike|Precise Strike]]_, swift action, 7 rounds)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +7)
1/day—_[[spells/Enlarge Person|enlarge person]]_ (self only), _[[spells/Invisibility|invisibility]]_ (self only)

##### Statistics
**Str** 16, **Dex** 14, **Con** 16, **Int** 8, **Wis** 14, **Cha** 6
**Base Atk** +9; **CMB** +12 (+14 overrun); **CMD** 24 (28 vs. bull rush, 26 vs. overrun, 28 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Charge Through|Charge Through]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Overrun|Improved Overrun]]_, _[[feats/Mounted Combat|Mounted Combat]]_, _Outflank_, _[[feats/Power Attack|Power Attack]]_, _Precise Strike_, _[[feats/Ride-By Attack|Ride-By Attack]]_
**Skills** Handle Animal +10, Intimidate +10, Perception +6, Ride +11, Sense Motive +2 (+6 when opposing a Bluff check), Stealth +8; **Racial Modifiers** +4 Stealth
**Languages** Common, Dwarven, Undercommon
**SQ** _mount_ (giant spider), mounted mastery, order of the sword
**Combat Gear** potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_; **Other Gear** +2 _[[items/Armor/Agile breastplate|agile breastplate]]_, +1 _lance_, mwk _bardiche_, mwk _cestus_, _sling_ with 10 bullets, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, simple banners (2), 420 gp

## Many-Legged _Mount_

Giant spider animal companion (Ultimate Magic 37)
 N Large vermin
 **Init **+3; **Senses **_darkvision_ 60 ft., _[[universal monster rules/Tremorsense|tremorsense]]_ 30 ft.; Perception +0

##### Defense

**AC **23, touch 12, _flat-footed_ 20 (+4 armor, +3 Dex, +7 natural, –1 size)
 **hp **60 (8d8+24)
 **Fort **+9, **Ref **+5, **Will **+2 (+6 vs. enchantments)
 **Defensive Abilities** evasion, mindless

##### Offense
**Speed **30 ft., _[[universal monster rules/Climb|climb]]_ 30 ft.
 **Melee **bite +7/+2 (1d8+3 plus poison)
 **Space **10 ft.; **Reach **10 ft.

##### Statistics
**Str **15, **Dex **16, **Con **16, **Int **—, **Wis **10, **Cha **2
 **Base Atk** +6; **CMB** +9; **CMD** 22 (34 vs. _trip_)
 **Feats **_[[feats/Endurance|Endurance]]_
 **Tricks **attack, come, defend, down, _[[npcs/Guard|guard]]_, heel
 **Skills **_Climb_ +8
 **SQ **combat riding, devotion, extra attack
 **Gear **_[[items/Armor/Chain shirt|chain shirt]]_ barding

### Special Abilities

**Poison (Ex)** Bite—injury; save Fort DC 17; frequency 1/round for 4 rounds; effect 1 Str; cure 1 save.

Where the ironclads are immovable, their counterparts— the strandriders—are swift. As a rite of passage, these _duergar_ harvest the egg sacks of giant female spiders, claiming the cluster’s strongest specimens to use as their future mounts.
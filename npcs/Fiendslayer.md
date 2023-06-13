---
cssclass: [monsters]
title1: Fiendslayer
title2: Fiendslayer
CR: 12
sources:
- name: NPC Codex
  page: 136
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 19200
race: Half-elf
classes:
- ranger 13
alignment: N
size: Medium
type: humanoid
subtypes:
- elf
- human
initiative:
  bonus: 5
senses:
  low-light vision: true
AC:
  AC: 28
  touch: 16
  flat_footed: 22
  components:
    armor: 8
    dex: 5
    dodge: 1
    natural: 4
HP:
  HP: 125
  long: 13d10+49
saves:
  fort: 12
  ref: 14
  will: 7
  other: +2 vs. enchantments
defensive_abilities:
- evasion
immunities:
- fire (120 points)
- poison
- sleep
resistances:
  electricity: 20
speeds:
  base: 40
attacks:
  melee:
  - - text: +1 cold iron rapier +17/+12/+7 (1d6+3/15-20)
      entries:
      - - damage: 1d6+3
          crit_range: 15-20
      attack: +1 cold iron rapier
      bonus:
      - 17
      - 12
      - 7
    - text: +1 silver dagger +17/+12/+7 (1d4+2/19-20)
      entries:
      - - damage: 1d4+2
          crit_range: 19-20
      attack: +1 silver dagger
      bonus:
      - 17
      - 12
      - 7
  ranged:
  - - text: +1 light crossbow +19 (1d8+1/19-20)
      entries:
      - - damage: 1d8+1
          crit_range: 19-20
      attack: +1 light crossbow
      bonus:
      - 19
  special:
  - favored enemy (evil outsiders +6, magical beasts +2, undead +2)
spells:
  entries:
  - name: cure moderate wounds
    source: Ranger
    level: 3
  - name: barkskin
    source: Ranger
    level: 2
  - name: bear's endurance
    source: Ranger
    level: 2
  - name: protection from energy
    source: Ranger
    level: 2
  - name: delay poison
    source: Ranger
    level: 1
  - name: longstrider
    source: Ranger
    level: 1
  - name: resist energy
    source: Ranger
    level: 1
    count: 2
  sources:
  - name: Ranger
    type: prepared
    CL: 10
    concentration: 12
tactics:
  Before Combat: The ranger casts barkskin, bear's endurance, delay poison, longstrider,
    protection from energy (fire), and resist energy (electricity).
  During Combat: If fighting demons or devils, the ranger applies oil of bless weapon
    to one weapon and drinks her potion of heroism.
  Base Statistics: Without barkskin, bear's endurance, delay poison, longstrider,
    protection from energy, and resist energy, the ranger's statistics are AC 24,
    touch 16, flat-footed 18; hp 99; Fort +10; Immune sleep; Resist none; Speed 30;
    Con 12; Skills Acrobatics +15.
ability_scores:
  STR: 14
  DEX: 21
  CON: 16
  INT: 10
  WIS: 14
  CHA: 8
BAB: 13
CMB: 15
CMD: 31
feats:
- name: Dodge
- name: Double Slice
- name: Endurance
- name: Greater Two-Weapon Fighting
- name: Improved Critical (rapier)
- name: Improved Two-Weapon Fighting
- name: Improved Vital Strike
- name: Skill Focus (Perception)
- name: Two-Weapon Fighting
- name: Two-Weapon Rend
- name: Vital Strike
- name: Weapon Finesse
skills:
  Acrobatics: 15
    when jumping: 19
  Knowledge (nature): 13
  Knowledge (planes): 10
  Linguistics: 3
  Perception: 26
  Ride: 12
  Stealth: 21
  Survival: 18
  Swim: 10
languages:
- Abyssal
- Celestial
- Common
- Elven
- Infernal
special_qualities:
- camouflage
- elf blood
- favored terrain (Abyss +4, underground +4, urban +2)
- hunter's bond (companions)
- quarry
- swift tracker
- track +6
- wild empathy +12
- woodland stride
gear:
  combat:
  - oil of bless weapon (2)
  - potions of cure serious wounds (2)
  - potion of heroism
  - potions of invisibility (2)
  - +1 evil outsider-bane bolts (5)
  - holy water (4)
  other:
  - +2 mithral breastplate
  - +1 cold iron rapier
  - +1 light crossbow with 15 bolts
  - +1 silver dagger
  - belt of incredible dexterity +2
  - cloak of resistance +1
  - 772 gp
desc_long: The fiendslayer's ultimate goal is to rid the mortal world of evil outsiders.

---

# Fiendslayer

**Source** NPC Codex pg. 136
**XP** 19,200
Half-elf _[[classes/Ranger|ranger]]_ 13

N Medium humanoid (elf, human)
**Init** +5; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +26

##### Defense

**AC** 28, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+8 armor, +5 Dex, +1 _[[feats/Dodge|dodge]]_, +4 natural)
**hp** 125 (13d10+49)
**Fort** +12, **Ref** +14, **Will** +7; +2 vs. enchantments
**Defensive Abilities** evasion; **Immune** fire (120 points), poison, sleep; **Resist** electricity 20

##### Offense
**Speed** 40 ft.
**Melee** +1 cold iron _[[items/Weapon/Rapier|rapier]]_ +17/+12/+7 (1d6+3/15–20), +1 silver _[[items/Weapon/Dagger|dagger]]_ +17/+12/+7 (1d4+2/19–20)
**Ranged** +1 _[[items/Weapon/Light crossbow|light crossbow]]_ +19 (1d8+1/19–20)
**Special Attacks** favored enemy (evil outsiders +6, magical beasts +2, undead +2)
**_Ranger_ Spells Prepared **(CL 10th; concentration +12)
3rd—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_
2nd—_[[spells/Barkskin|barkskin]]_, bear’s _[[feats/Endurance|endurance]]_, _[[spells/Protection from Energy|protection from energy]]_
1st—_[[spells/Delay Poison|delay poison]]_, _[[spells/Longstrider|longstrider]]_, _[[spells/Resist Energy|resist energy]]_ (2)

### Tactics

**Before Combat **The _ranger_ casts _barkskin_, bear’s _endurance_, _delay poison_, _longstrider_, _protection from energy_ (fire), and _resist energy_ (electricity).
**During Combat **If fighting demons or devils, the _ranger_ applies oil of _[[spells/Bless Weapon|bless weapon]]_ to one weapon and drinks her potion of _[[spells/Heroism|heroism]]_.
**Base Statistics **Without _barkskin_, bear’s _endurance_, _delay poison_, _longstrider_, _protection from energy_, and _resist energy_, the _ranger_’s statistics are **AC **24, touch 16, _flat-footed_ 18; **hp **99; **Fort **+10; **Immune **sleep; **Resist **none; **Speed **30; **Con **12; **Skills **Acrobatics +15.

##### Statistics
**Str** 14, **Dex** 21, **Con** 16, **Int** 10, **Wis** 14, **Cha** 8
**Base Atk** +13; **CMB** +15; **CMD** 31
**Feats** _Dodge_, _[[feats/Double Slice|Double Slice]]_, _Endurance_, _[[feats/Greater Two-Weapon Fighting|Greater Two-Weapon Fighting]]_, _[[feats/Improved Critical|Improved Critical]]_ (_rapier_), _[[feats/Improved Two-Weapon Fighting|Improved Two-Weapon Fighting]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, _[[feats/Two-Weapon Rend|Two-Weapon Rend]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +15 (+19 when jumping), Knowledge (nature) +13, Knowledge (planes) +10, Linguistics +3, Perception +26, Ride +12, Stealth +21, Survival +18, Swim +10
**Languages** Abyssal, Celestial, Common, Elven, Infernal
**SQ** camouflage, elf blood, favored terrain (Abyss +4, underground +4, urban +2), _[[classes/Hunter|hunter]]_’s bond (companions), quarry, swift tracker, track +6, wild _[[feats/Empathy|empathy]]_ +12, woodland stride
**Combat Gear** oil of _bless weapon_ (2), potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), potion of _heroism_, potions of _[[spells/Invisibility|invisibility]]_ (2), +1 evil outsider-bane bolts (5), _[[items/Mundane/Holy water|holy water]]_ (4); **Other Gear** +2 mithral _[[items/Armor/Breastplate|breastplate]]_, +1 cold iron _rapier_, +1 _light crossbow_ with 15 bolts, +1 silver _dagger_, _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, 772 gp

The _[[npcs/Fiendslayer|fiendslayer]]_’s ultimate goal is to rid the mortal world of evil outsiders.
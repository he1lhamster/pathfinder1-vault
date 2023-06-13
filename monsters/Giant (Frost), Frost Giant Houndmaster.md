---
cssclass: [monsters]
title1: Giant (Frost), Frost Giant Houndmaster
title2: Frost Giant Houndmaster
CR: 14
sources:
- name: Monster Codex
  page: 74
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 38400
race: Frost
classes:
- giant druid (arctic druid) 10 (Pathfinder RPG Advanced Player's Guide 98)
alignment: NE
size: Large
type: humanoid
subtypes:
- cold
- giant
initiative:
  bonus: 4
senses:
  low-light vision: true
  snowcaster: true
AC:
  AC: 28
  touch: 10
  flat_footed: 28
  components:
    armor: 7
    deflection: 1
    natural: 11
    size: -1
HP:
  HP: 262
  long: 24d8+154
saves:
  fort: 22
  ref: 10
  will: 18
defensive_abilities:
- rock catching
immunities:
- cold
- dazzled
weaknesses:
- vulnerable to fire
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 greataxe +27/+22/+17/+12 (3d6+14/×3)
      entries:
      - - damage: 3d6+14
          crit_multiplier: 3
      attack: +1 greataxe
      bonus:
      - 27
      - 22
      - 17
      - 12
  ranged:
  - - text: rock +16 (1d8+13)
      entries:
      - - damage: 1d8+13
      attack: rock
      bonus:
      - 16
  special:
  - rock throwing (120 ft.)
  - snowcaster
  - wild shape 3/day
space: 10
reach: 10
spells:
  entries:
  - name: animal growth
    source: Druid
    level: 5
    DC: 21
  - name: cure critical wounds
    source: Druid
    level: 5
  - name: transmute rock to mud
    source: Druid
    level: 5
    DC: 21
  - name: cure serious wounds
    source: Druid
    level: 4
  - name: flame strike
    source: Druid
    level: 4
    DC: 21
  - name: ice storm
    source: Druid
    level: 4
  - name: spike stones
    source: Druid
    level: 4
    DC: 20
  - name: call lightning
    source: Druid
    level: 3
    DC: 20
  - name: dominate animal
    source: Druid
    level: 3
    DC: 19
  - name: protection from energy
    source: Druid
    level: 3
  - name: sleet storm
    source: Druid
    level: 3
  - name: animal trance
    source: Druid
    level: 2
    DC: 18
  - name: barkskin
    source: Druid
    level: 2
  - name: bull's strength
    source: Druid
    level: 2
  - name: chill metal
    source: Druid
    level: 2
  - name: delay poison
    source: Druid
    level: 2
  - name: hold animal
    source: Druid
    level: 2
    DC: 18
  - name: charm animal
    source: Druid
    level: 1
    DC: 17
  - name: entangle
    source: Druid
    level: 1
    DC: 17
  - superscripts:
    - UM
    name: frostbite
    source: Druid
    level: 1
  - name: obscuring mist
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
    count: 2
  - name: create water
    source: Druid
    level: 0
  - name: detect magic
    source: Druid
    level: 0
  - name: light
    source: Druid
    level: 0
  - name: purify food and drink
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 10
    concentration: 16
    slots:
      0: at-will
tactics:
  Before Combat: The houndmaster casts protection from energy (fire) on herself, casts
    animal growth, barkskin, and bull's strength on her animal companion, and then
    casts call lightning.
  During Combat: The houndmaster fights with axe and magic together, directing lightning
    bolts from call lightning and miring opponents with entangle, sleet storm, and
    transmute rock to mud.
ability_scores:
  STR: 28
  DEX: 10
  CON: 20
  INT: 13
  WIS: 23
  CHA: 14
BAB: 17
CMB: 27
CMD: 38
feats:
- name: Cleave
- name: Great Cleave
- name: Improved Natural Armor
- name: Intimidating Prowess
- name: Lightning Reflexes
- name: Martial Weapon Proficiency (greataxe)
- name: Natural Spell
- name: Power Attack
- name: Scribe Scroll
- name: Spell Focus (evocation)
- name: Toughness
- name: Weapon Focus (greataxe)
skills:
  Bluff: 9
  Handle Animal: 20
  Heal: 14
  Intimidate: 29
  Knowledge (geography): 9
    in cold or icy terrain: 14
  Knowledge (nature): 16
  Perception: 29
    in cold or icy terrain: 34
  Stealth: -6
    in cold or icy terrain: 3
  Survival: 21
    in cold or icy terrain: 26
  Swim: 15
  _racial_mods:
    Stealth:
      in snow: 4
languages:
- Common
- Druidic
- Giant
- Sylvan
special_qualities:
- arctic native
- icewalking
- nature bond (animal companion)
- nature sense
- wild empathy +12
gear:
  combat:
  - pearl of power (2nd)
  - scrolls of cure serious wounds (2)
  - antitoxin (2)
  other:
  - +3 hide armor
  - +1 greataxe
  - amulet of natural armor +1
  - belt of mighty constitution +2
  - cloak of resistance +1
  - headband of inspired wisdom +2
  - manacles of cooperation (2)
  - ring of protection +1
  - 1,465 gp
ecology:
  environment: cold mountains
desc_long: A houndmaster is responsible for the care of the tribe's pets, frequently
  polar bears, wolves, and winter wolves. She is fond of pitting her charges against
  each other, allowing the packs to establish a functional hierarchy and ensuring
  that only the strongest survive to breed. Some houndmasters choose these pack leaders
  as animal companions.

---

# Giant (Frost), Frost Giant Houndmaster

**Source** Monster Codex pg. 74
**XP** 38,400
Frost giant _[[classes/Druid|druid]]_ (arctic _druid_) 10 (Pathfinder RPG Advanced Player’s Guide 98)

NE Large humanoid (cold, giant)
**Init** +4; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, snowcaster; Perception +29

##### Defense

**AC** 28, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+7 armor, +1 deflection, +11 natural, –1 size)
**hp** 262 (24d8+154)
**Fort** +22, **Ref** +10, **Will** +18
**Defensive Abilities** _[[universal monster rules/Rock Catching|rock catching]]_; **Immune** cold, _[[conditions/Dazzled|dazzled]]_
**Weaknesses** vulnerable to fire

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon/Greataxe|greataxe]]_ +27/+22/+17/+12 (3d6+14/×3)
**Ranged** rock +16 (1d8+13)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Rock Throwing|rock throwing]]_ (120 ft.), snowcaster, wild shape 3/day
**_Druid_ Spells Prepared **(CL 10th; concentration +16)
5th—_[[spells/Animal Growth|animal growth]]_ (DC 21), _[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Transmute Rock to Mud|transmute rock to mud]]_ (DC 21)
4th—_[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Flame Strike|flame strike]]_ (DC 21), _[[spells/Ice Storm|ice storm]]_, _[[spells/Spike Stones|spike stones]]_ (DC 20)
3rd—_[[spells/Call Lightning|call lightning]]_ (DC 20), _[[spells/Dominate Animal|dominate animal]]_ (DC 19), _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Sleet Storm|sleet storm]]_
2nd—_[[spells/Animal Trance|animal trance]]_ (DC 18), _[[spells/Barkskin|barkskin]]_, bull’s strength, _[[spells/Chill Metal|chill metal]]_, _[[spells/Delay Poison|delay poison]]_, _[[spells/Hold Animal|hold animal]]_ (DC 18)
1st—_[[spells/Charm Animal|charm animal]]_ (DC 17), _[[spells/Entangle|entangle]]_ (DC 17), _[[spells/Frostbite|frostbite]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Speak with Animals|speak with animals]]_ (2)
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, light, _[[spells/Purify Food and Drink|purify food and drink]]_

### Tactics

**Before Combat** The houndmaster casts _protection from energy_ (fire) on herself, casts _animal growth_, _barkskin_, and bull’s strength on her animal companion, and then casts _call lightning_.
 **During Combat** The houndmaster fights with axe and magic together, directing lightning bolts from _call lightning_ and miring opponents with _entangle_, _sleet storm_, and _transmute rock to mud_.

##### Statistics
**Str** 28, **Dex** 10, **Con** 20, **Int** 13, **Wis** 23, **Cha** 14
**Base Atk** +17; **CMB** +27; **CMD** 38
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Natural Armor|Improved Natural Armor]]_, _[[feats/Intimidating Prowess|Intimidating Prowess]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Martial Weapon Proficiency|Martial Weapon Proficiency]]_ (_greataxe_), _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation), _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_greataxe_)
**Skills** Bluff +9, Handle Animal +20, _[[spells/Heal|Heal]]_ +14, Intimidate +29, Knowledge (geography) +9 (+14 in cold or icy terrain), Knowledge (nature) +16, Perception +29 (+34 in cold or icy terrain), Stealth –6 (+3 in cold or icy terrain), Survival +21 (+26 in cold or icy terrain), Swim +15; **Racial Modifiers** +4 Stealth in snow
**Languages** Common, Druidic, Giant, Sylvan
**SQ** arctic native, icewalking, nature bond (animal companion), nature sense, wild _[[feats/Empathy|empathy]]_ +12
**Combat Gear** pearl of power (2nd), scrolls of _cure serious wounds_ (2), _[[items/Mundane/Antitoxin|antitoxin]]_ (2); **Other Gear** +3 _[[items/Armor/Hide armor|hide armor]]_, +1 _greataxe_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Mighty Constitution +2|belt of mighty constitution +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Wondrous Item/Manacles of Cooperation|manacles of cooperation]]_ (2), _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 1,465 gp

##### Ecology

**Environment** cold mountains

##### Description

A houndmaster is responsible for the care of the tribe’s pets, frequently polar bears, wolves, and winter wolves. She is fond of pitting her charges against each other, allowing the packs to establish a functional hierarchy and ensuring that only the strongest survive to breed. Some houndmasters choose these pack leaders as animal companions.
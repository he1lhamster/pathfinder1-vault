---
cssclass: [monsters]
title1: Mud Shaman
title2: Mud Shaman
CR: 8
sources:
- name: NPC Codex
  page: 68
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 4800
race: Human
classes:
- druid 9
alignment: CN
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 0
AC:
  AC: 22
  touch: 10
  flat_footed: 22
  components:
    armor: 7
    natural: 3
    shield: 2
HP:
  HP: 69
  long: 9d8+25
saves:
  fort: 8
  ref: 5
  will: 11
  other: +4 vs. fey and plant-targeted effects
immunities:
- poison
resistances:
  acid: 10
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk club +10/+5 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: mwk club
      bonus:
      - 10
      - 5
  ranged:
  - - text: mwk shortspear +7/+2 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: mwk shortspear
      bonus:
      - 7
      - 2
  special:
  - wild shape 3/day
spell_like_abilities:
  entries:
  - name: acid dart
    source: default
    freq: 8/day
  sources:
  - name: default
    CL: 9
    concentration: 14
spells:
  entries:
  - name: animal growth
    source: Druid
    level: 5
    DC: 20
  - name: stoneskin
    source: Druid
    level: 5
  - is_domain_spell: true
    name: wall of stone
    source: Druid
    level: 5
  - name: dispel magic
    source: Druid
    level: 4
  - name: freedom of movement
    source: Druid
    level: 4
  - name: giant vermin
    source: Druid
    level: 4
  - is_domain_spell: true
    name: spike stones
    source: Druid
    level: 4
    DC: 19
  - name: greater magic fang
    source: Druid
    level: 3
    count: 3
  - name: spike growth
    source: Druid
    level: 3
    DC: 18
  - is_domain_spell: true
    name: stone shape
    source: Druid
    level: 3
  - name: barkskin
    source: Druid
    level: 2
    count: 2
  - name: bull's strength
    source: Druid
    level: 2
    count: 2
  - name: fog cloud
    source: Druid
    level: 2
  - is_domain_spell: true
    name: soften earth and stone
    source: Druid
    level: 2
  - name: cure light wounds
    source: Druid
    level: 1
    count: 2
  - name: faerie fire
    source: Druid
    level: 1
    count: 2
  - is_domain_spell: true
    name: magic stone
    source: Druid
    level: 1
  - name: shillelagh
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
  - name: create water
    source: Druid
    level: 0
  - name: guidance
    source: Druid
    level: 0
  - name: know direction
    source: Druid
    level: 0
  - name: light
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 9
    concentration: 14
    slots:
      0: at-will
    domains:
    - earth
tactics:
  Before Combat: The druid casts barkskin and bull's strength.
  During Combat: The druid casts wall of stone between his opponents to separate them.
    On the following rounds, he spontaneously casts summoning spells, bolstering summoned
    creatures with greater magic fang. He eventually wild shapes into a stegosaurus
    to enter melee.
  Base Statistics: Without barkskin and bull's strength, the druid's statistics are
    AC 19, touch 10, flat-footed 19; Melee mwk club +8/+3 (1d6+1); Ranged mwk shortspear
    +7/+2 (1d6+1); Str 13; CMB +7; CMD 17; Skills Swim +4.
ability_scores:
  STR: 17
  DEX: 10
  CON: 14
  INT: 8
  WIS: 20
  CHA: 13
BAB: 6
CMB: 9
CMD: 19
feats:
- name: Augment Summoning
- name: Lightning Reflexes
- name: Lunge
- name: Power Attack
- name: Spell Focus (conjuration)
- name: Vital Strike
skills:
  Craft (woodworking): 6
  Fly: 4
  Handle Animal: 6
  Knowledge (geography): 5
  Knowledge (nature): 9
  Perception: 13
  Spellcraft: 4
  Survival: 18
  Swim: 6
languages:
- Common
special_qualities:
- nature bond (Earth domain)
- nature sense
- trackless step
- wild empathy +10
- woodland stride
gear:
  combat:
  - potion of cure serious wounds
  - scroll of lesser restoration
  - scroll of protection from energy
  - scroll of wall of fire
  other:
  - +1 dragonhide breastplate
  - masterwork heavy wooden shield
  - masterwork club
  - masterwork shortspears (3)
  - headband of inspired wisdom +2
  - holly and mistletoe
  - spell component pouch
  - 60 gp
desc_long: Stalking through boiling and sometimes acidic mud pits, these druids have
  caustic personalities and abilities.

---

# Mud Shaman

**Source** NPC Codex pg. 68
**XP** 4,800
Human _[[classes/Druid|druid]]_ 9

CN Medium humanoid (human)
**Init** +0; **Senses** Perception +13

##### Defense

**AC** 22, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+7 armor, +3 natural, +2 _[[spells/Shield|shield]]_)
**hp** 69 (9d8+25)
**Fort** +8, **Ref** +5, **Will** +11; +4 vs. fey and plant-targeted effects
**Immune** poison; **Resist** acid 10

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Club|club]]_ +10/+5 (1d6+3)
**Ranged** mwk _[[items/Weapon/Shortspear|shortspear]]_ +7/+2 (1d6+3)
**Special Attacks** wild shape 3/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +14)
8/day—acid _[[items/Weapon/Dart|dart]]_
**_Druid_ Spells Prepared **(CL 9th; concentration +14)
5th—_[[spells/Animal Growth|animal growth]]_ (DC 20), _[[spells/Stoneskin|stoneskin]]_, _[[spells/Wall Of Stone|wall of stone]]_
4th—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Giant Vermin|giant vermin]]_, _[[spells/Spike Stones|spike stones]]_ (DC 19)
3rd—greater _[[spells/Magic Fang|magic fang]]_ (3), _[[spells/Spike Growth|spike growth]]_ (DC 18), _[[spells/Stone Shape|stone shape]]_
2nd—_[[spells/Barkskin|barkskin]]_ (2), bull’s strength (2), _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Soften Earth and Stone|soften earth and stone]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_ (2), _[[spells/Faerie Fire|faerie fire]]_ (2), _[[spells/Magic Stone|magic stone]]_, _[[spells/Shillelagh|shillelagh]]_, _[[spells/Speak with Animals|speak with animals]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Guidance|guidance]]_, _[[spells/Know Direction|know direction]]_, light
**D **Domain spell; **Domain **Earth

### Tactics

**Before Combat **The _druid_ casts _barkskin_ and bull’s strength.
**During Combat **The _druid_ casts _wall of stone_ between his opponents to separate them. On the following rounds, he spontaneously casts summoning spells, _[[items/Armor Magic Abilities/Bolstering|bolstering]]_ summoned creatures with greater _magic fang_. He eventually wild shapes into a stegosaurus to enter melee.
**Base Statistics **Without _barkskin_ and bull’s strength, the _druid_’s statistics are **AC **19, touch 10, _flat-footed_ 19; **Melee **mwk _club_ +8/+3 (1d6+1); **Ranged **mwk _shortspear_ +7/+2 (1d6+1); **Str **13; **CMB **+7; **CMD **17; **Skills **Swim +4.

##### Statistics
**Str** 17, **Dex** 10, **Con** 14, **Int** 8, **Wis** 20, **Cha** 13
**Base Atk** +6; **CMB** +9; **CMD** 19
**Feats** _[[feats/Augment Summoning|Augment Summoning]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spell Focus|Spell Focus]]_ (conjuration), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Craft (woodworking) +6, Fly +4, Handle Animal +6, Knowledge (geography) +5, Knowledge (nature) +9, Perception +13, Spellcraft +4, Survival +18, Swim +6
**Languages** Common
**SQ** nature bond (Earth domain), nature sense, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, wild _[[feats/Empathy|empathy]]_ +10, woodland stride
**Combat Gear** potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_, scroll of lesser _[[spells/Restoration|restoration]]_, scroll of _[[spells/Protection from Energy|protection from energy]]_, scroll of _[[spells/Wall Of Fire|wall of fire]]_; **Other Gear** +1 dragonhide _[[items/Armor/Breastplate|breastplate]]_, masterwork _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, masterwork _club_, masterwork shortspears (3), _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 60 gp

_[[items/Weapon Magic Abilities/Stalking|Stalking]]_ through boiling and sometimes acidic mud pits, these druids have caustic personalities and abilities.
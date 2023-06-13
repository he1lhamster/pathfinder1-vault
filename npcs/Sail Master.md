---
cssclass: [monsters]
title1: Sail Master
title2: Sail Master
CR: 1
sources:
- name: NPC Codex
  page: 62
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 400
race: Human
classes:
- druid 2
alignment: NE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 1
AC:
  AC: 17
  touch: 12
  flat_footed: 15
  components:
    armor: 2
    dex: 1
    dodge: 1
    shield: 3
HP:
  HP: 18
  long: 2d8+6
saves:
  fort: 5
  ref: 1
  will: 4
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk club +5 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: mwk club
      bonus:
      - 5
  ranged:
  - - text: shortspear +2 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: shortspear
      bonus:
      - 2
spell_like_abilities:
  entries:
  - name: storm burst
    source: default
    freq: 4/day
  sources:
  - name: default
    CL: 2
    concentration: 3
spells:
  entries:
  - name: cure light wounds
    source: Druid
    level: 1
  - name: jump
    source: Druid
    level: 1
  - is_domain_spell: true
    name: obscuring mist
    source: Druid
    level: 1
  - name: shillelagh
    source: Druid
    level: 1
  - name: flare
    source: Druid
    level: 0
    DC: 11
  - name: know direction
    source: Druid
    level: 0
  - name: light
    source: Druid
    level: 0
  - name: stabilize
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 2
    concentration: 3
    slots:
      0: at-will
    domains:
    - weather
tactics:
  During Combat: The druid casts obscuring mist at the start of combat and shillelagh
    before moving into melee range.
ability_scores:
  STR: 17
  DEX: 13
  CON: 14
  INT: 8
  WIS: 12
  CHA: 10
BAB: 1
CMB: 4
CMD: 16
feats:
- name: Dodge
- name: Shield Focus
skills:
  Handle Animal: 5
  Heal: 5
  Knowledge (geography): 3
  Knowledge (nature): 1
  Perception: 5
  Profession (sailor): 5
  Survival: 7
  Swim: 5
languages:
- Common
- Druidic
special_qualities:
- nature bond (Weather domain)
- nature sense
- wild empathy +2
- woodland stride
gear:
  combat:
  - scrolls of cure light wounds (2)
  - scroll of entangle (2)
  - alchemist's fire (4)
  other:
  - masterwork leather armor
  - heavy wooden shield
  - masterwork club
  - shortspear
  - grappling hook
  - healer's kit
  - hemp rope (50 ft.)
  - holly and mistletoe
  - spell component pouch
  - amber necklace (worth 25 gp)
  - 45 gp
desc_long: Mastery of the wind and weather is a boon on any ship, and many northern
  druids thus serve as captains, navigators, and battle support.

---

# Sail Master

**Source** NPC Codex pg. 62
**XP** 400
Human _[[classes/Druid|druid]]_ 2

NE Medium humanoid (human)
**Init** +1; **Senses** Perception +5

##### Defense

**AC** 17, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+2 armor, +1 Dex, +1 _[[feats/Dodge|dodge]]_, +3 _[[spells/Shield|shield]]_)
**hp** 18 (2d8+6)
**Fort** +5, **Ref** +1, **Will** +4

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Club|club]]_ +5 (1d6+3)
**Ranged** _[[items/Weapon/Shortspear|shortspear]]_ +2 (1d6+3)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 2nd; concentration +3)
4/day—storm burst
**_Druid_ Spells Prepared **(CL 2nd; concentration +3)
1st—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Jump|jump]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shillelagh|shillelagh]]_
0 (at will)—_[[spells/Flare|flare]]_ (DC 11), _[[spells/Know Direction|know direction]]_, light, stabilize
**D **Domain spell; **Domain **Weather

### Tactics

**During Combat **The _druid_ casts _obscuring mist_ at the start of combat and _shillelagh_ before moving into melee range.

##### Statistics
**Str** 17, **Dex** 13, **Con** 14, **Int** 8, **Wis** 12, **Cha** 10
**Base Atk** +1; **CMB** +4; **CMD** 16
**Feats** _Dodge_, _[[feats/Shield Focus|Shield Focus]]_
**Skills** Handle Animal +5, _[[spells/Heal|Heal]]_ +5, Knowledge (geography) +3, Knowledge (nature) +1, Perception +5, Profession (sailor) +5, Survival +7, Swim +5
**Languages** Common, Druidic
**SQ** nature bond (Weather domain), nature sense, wild _[[feats/Empathy|empathy]]_ +2, woodland stride
**Combat Gear** scrolls of _cure light wounds_ (2), scroll of _[[spells/Entangle|entangle]]_ (2), _[[classes/Alchemist|alchemist]]_’s fire (4); **Other Gear** masterwork _[[items/Armor/Leather armor|leather armor]]_, _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, masterwork _club_, _shortspear_, _[[items/Weapon/Grappling hook|grappling hook]]_, _[[npcs/Healer|healer]]_’s kit, hemp rope (50 ft.), _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, amber necklace (worth 25 gp), 45 gp

Mastery of the wind and weather is a boon on any ship, and many northern druids thus serve as captains, navigators, and battle support.
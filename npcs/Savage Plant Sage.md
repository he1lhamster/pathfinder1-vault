---
cssclass: [monsters]
title1: Savage Plant Sage
title2: Savage Plant Sage
CR: 3
sources:
- name: NPC Codex
  page: 63
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 800
race: Half-orc
classes:
- druid 4
alignment: CN
size: Medium
type: humanoid
subtypes:
- human
- orc
initiative:
  bonus: 1
senses:
  darkvision: 60
AC:
  AC: 20
  touch: 11
  flat_footed: 19
  components:
    armor: 7
    dex: 1
    natural: 2
HP:
  HP: 32
  long: 4d8+11
saves:
  fort: 6
  ref: 2
  will: 5
  other: +4 vs. fey and plant-targeted effects
defensive_abilities:
- orc ferocity
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk club +9 (1d6+4)
      entries:
      - - damage: 1d6+4
      attack: mwk club
      bonus:
      - 9
  ranged:
  - - text: spear +4 (1d8+4/×3)
      entries:
      - - damage: 1d8+4
          crit_multiplier: 3
      attack: spear
      bonus:
      - 4
  special:
  - wild shape 1/day
spell_like_abilities:
  entries:
  - name: wooden fist
    source: default
    freq: 4/day
  sources:
  - name: default
    CL: 4
    concentration: 5
spells:
  entries:
  - is_domain_spell: true
    name: barkskin
    source: Druid
    level: 2
  - name: bull's strength
    source: Druid
    level: 2
  - name: summon swarm
    source: Druid
    level: 2
  - is_domain_spell: true
    name: entangle
    source: Druid
    level: 1
    count: 2
    DC: 12
  - name: faerie fire
    source: Druid
    level: 1
  - name: shillelagh
    source: Druid
    level: 1
    count: 2
  - name: create water
    source: Druid
    level: 0
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
    CL: 4
    concentration: 5
    slots:
      0: at-will
    domains:
    - plant
tactics:
  Before Combat: The druid casts barkskin on himself.
  During Combat: The druid casts entangle or summon swarm.
  Base Statistics: Without barkskin, the druid's statistics are AC 18, touch 11, flat-footed
    17.
ability_scores:
  STR: 18
  DEX: 12
  CON: 14
  INT: 8
  WIS: 13
  CHA: 10
BAB: 3
CMB: 7
CMD: 18
feats:
- name: Natural Spell
- name: Weapon Focus (club)
skills:
  Heal: 7
  Intimidate: 2
  Knowledge (nature): 8
  Perception: 6
  Survival: 10
languages:
- Common
- Druidic
- Orc
special_qualities:
- nature bond (Plant domain)
- nature sense
- orc blood
- trackless step
- weapon familiarity
- wild empathy +4
- woodland stride
gear:
  combat:
  - potion of cure moderate wounds
  other:
  - +1 dragonhide breastplate
  - masterwork club
  - spears (4)
  - holly and mistletoe
  - 93 gp
desc_long: There is no description for this NPC.

---

# Savage Plant Sage

**Source** NPC Codex pg. 63
**XP** 800
Half-orc _[[classes/Druid|druid]]_ 4

CN Medium humanoid (human, _[[monsters/Orc|orc]]_)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +6

##### Defense

**AC** 20, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+7 armor, +1 Dex, +2 natural)
**hp** 32 (4d8+11)
**Fort** +6, **Ref** +2, **Will** +5; +4 vs. fey and plant-targeted effects
**Defensive Abilities** _orc_ _[[universal monster rules/Ferocity|ferocity]]_

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Club|club]]_ +9 (1d6+4)
**Ranged** _[[items/Weapon/Spear|spear]]_ +4 (1d8+4/×3)
**Special Attacks** wild shape 1/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +5)
4/day—wooden fist
**_Druid_ Spells Prepared **(CL 4th; conc. +5)
2nd—_[[spells/Barkskin|barkskin]]_, bull’s strength, _[[spells/Summon Swarm|summon swarm]]_
1st—_[[spells/Entangle|entangle]]_ (2, DC 12), _[[spells/Faerie Fire|faerie fire]]_, _[[spells/Shillelagh|shillelagh]]_ (2)
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Know Direction|know direction]]_, light, stabilize
**D **Domain spell; **Domain **Plant

### Tactics

**Before Combat **The _druid_ casts _barkskin_ on himself.
**During Combat **The _druid_ casts _entangle_ or _summon swarm_.
**Base Statistics **Without _barkskin_, the _druid_’s statistics are **AC **18, touch 11, _flat-footed_ 17.

##### Statistics
**Str** 18, **Dex** 12, **Con** 14, **Int** 8, **Wis** 13, **Cha** 10
**Base Atk** +3; **CMB** +7; **CMD** 18
**Feats** _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_club_)
**Skills** _[[spells/Heal|Heal]]_ +7, Intimidate +2, Knowledge (nature) +8, Perception +6, Survival +10
**Languages** Common, Druidic, _Orc_
**SQ** nature bond (Plant domain), nature sense, _orc_ blood, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, weapon familiarity, wild _[[feats/Empathy|empathy]]_ +4, woodland stride
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_; **Other Gear** +1 dragonhide _[[items/Armor/Breastplate|breastplate]]_, masterwork _club_, spears (4), _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, 93 gp

There is no description for this NPC.
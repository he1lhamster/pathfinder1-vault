---
cssclass: [monsters]
title1: Evasive Slip
title2: Evasive Slip
CR: 5
sources:
- name: NPC Codex
  page: 65
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 1600
race: Halfling
classes:
- druid 6
alignment: NE
size: Small
type: humanoid
subtypes:
- halfling
initiative:
  bonus: 4
AC:
  AC: 22
  touch: 15
  flat_footed: 18
  components:
    armor: 5
    dex: 4
    shield: 2
    size: 1
HP:
  HP: 40
  long: 6d8+10
saves:
  fort: 7
  ref: 7
  will: 8
  other: +2 vs. fear, +4 vs. fey and plant-targeted effects
resistances:
  electricity: 10
speeds:
  base: 15
attacks:
  melee:
  - - text: mwk sickle +6 (1d4)
      entries:
      - - damage: 1d4
      attack: mwk sickle
      bonus:
      - 6
  ranged:
  - - text: mwk sling +10 (1d3)
      entries:
      - - damage: 1d3
      attack: mwk sling
      bonus:
      - 10
  special:
  - wild shape 2/day
spell_like_abilities:
  entries:
  - name: lightning arc
    source: default
    freq: 5/day
  sources:
  - name: default
    CL: 6
    concentration: 8
spells:
  entries:
  - is_domain_spell: true
    name: gaseous form
    source: Druid
    level: 3
  - name: extended summon nature's ally II
    source: Druid
    level: 3
    count: 2
  - name: barkskin
    source: Druid
    level: 2
  - name: extended summon nature's ally I
    source: Druid
    level: 2
  - name: summon swarm
    source: Druid
    level: 2
  - is_domain_spell: true
    name: wind wall
    source: Druid
    level: 2
  - name: endure elements
    source: Druid
    level: 1
  - name: faerie fire
    source: Druid
    level: 1
  - name: magic fang
    source: Druid
    level: 1
  - is_domain_spell: true
    name: obscuring mist
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
  - name: detect poison
    source: Druid
    level: 0
  - name: know direction
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
    CL: 6
    concentration: 8
    slots:
      0: at-will
    domains:
    - air
tactics:
  Before Combat: The druid casts endure elements at the start of each day. Before
    a fight he drinks his potion of invisibility.
  During Combat: Once invisible, the druid moves away from his enemies. He spends
    the next few rounds casting speak with animals and his extended summon nature's
    ally spells, followed by magic fang and barkskin, cast from his wands on the summoned
    creatures. If the summoned creatures take damage, he heals them with his wand
    of cure moderate wounds. If his invisibility is compromised, he wild shapes into
    an eagle to keep out of reach.
ability_scores:
  STR: 10
  DEX: 18
  CON: 13
  INT: 10
  WIS: 14
  CHA: 10
BAB: 4
CMB: 3
CMD: 17
feats:
- name: Augment Summoning
- name: Extend Spell
- name: Spell Focus (conjuration)
skills:
  Acrobatics: 4
    when jumping: 0
  Bluff: 2
  Heal: 6
  Knowledge (nature): 6
  Perception: 9
  Sense Motive: 4
  Spellcraft: 7
  Stealth: 12
  Survival: 13
  Swim: 3
languages:
- Common
- Druidic
- Halfling
special_qualities:
- nature bond (Air domain)
- nature sense
- trackless step
- wild empathy +6
- woodland stride
gear:
  combat:
  - potion of invisibility
  - scroll of longstrider
  - wand of barkskin (8 charges)
  - wand of cure moderate wounds (15 charges)
  - wand of magic fang (8 charges)
  other:
  - +1 hide armor
  - darkwood masterwork heavy wooden shield
  - masterwork sickle
  - masterwork sling with 20 bullets
  - antitoxin
  - holly and mistletoe
  - spell component pouch
  - 52 gp
desc_long: Evasive as the wind, these skittish druids tend to stay away from others,
  using their formidable powers to escape even the most hazardous situations.

---

# Evasive Slip

**Source** NPC Codex pg. 65
**XP** 1,600
Halfling _[[classes/Druid|druid]]_ 6

NE Small humanoid (halfling)
**Init** +4; **Senses** Perception +9

##### Defense

**AC** 22, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+5 armor, +4 Dex, +2 _[[spells/Shield|shield]]_, +1 size)
**hp** 40 (6d8+10)
**Fort** +7, **Ref** +7, **Will** +8; +2 vs. _[[universal monster rules/Fear|fear]]_, +4 vs. fey and plant-targeted effects
**Resist** electricity 10

##### Offense
**Speed** 15 ft.
**Melee** mwk _[[items/Weapon/Sickle|sickle]]_ +6 (1d4)
**Ranged** mwk _[[items/Weapon/Sling|sling]]_ +10 (1d3)
**Special Attacks** wild shape 2/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +8)
5/day—_[[spells/Lightning Arc|lightning arc]]_
**_Druid_ Spells Prepared **(CL 6th; concentration +8)
3rd—_[[spells/Gaseous Form|gaseous form]]_, extended _[[universal monster rules/Summon|summon]]_ nature’s ally II (2)
2nd—_[[spells/Barkskin|barkskin]]_, extended _summon_ nature’s ally I, _[[spells/Summon Swarm|summon swarm]]_, _[[spells/Wind Wall|wind wall]]_
1st—_[[spells/Endure Elements|endure elements]]_, _[[spells/Faerie Fire|faerie fire]]_, _[[spells/Magic Fang|magic fang]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Speak with Animals|speak with animals]]_
0 (at will)—_[[spells/Detect Poison|detect poison]]_, _[[spells/Know Direction|know direction]]_, light, _[[spells/Purify Food and Drink|purify food and drink]]_
**D **Domain spell; **Domain **Air

### Tactics

**Before Combat **The _druid_ casts _endure elements_ at the start of each day. Before a fight he drinks his potion of _[[spells/Invisibility|invisibility]]_.
**During Combat **Once _[[conditions/Invisible|invisible]]_, the _druid_ moves away from his enemies. He spends the next few rounds casting _speak with animals_ and his extended _summon_ nature’s ally spells, followed by _magic fang_ and _barkskin_, cast from his wands on the summoned creatures. If the summoned creatures take damage, he heals them with his wand of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_. If his _invisibility_ is compromised, he wild shapes into an _[[monsters/Eagle|eagle]]_ to keep out of reach.

##### Statistics
**Str** 10, **Dex** 18, **Con** 13, **Int** 10, **Wis** 14, **Cha** 10
**Base Atk** +4; **CMB** +3; **CMD** 17
**Feats** _[[feats/Augment Summoning|Augment Summoning]]_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Spell Focus|Spell Focus]]_ (conjuration)
**Skills** Acrobatics +4 (+0 when jumping), Bluff +2, _[[spells/Heal|Heal]]_ +6, Knowledge (nature) +6, Perception +9, Sense Motive +4, Spellcraft +7, Stealth +12, Survival +13, Swim +3
**Languages** Common, Druidic, Halfling
**SQ** nature bond (Air domain), nature sense, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, wild _[[feats/Empathy|empathy]]_ +6, woodland stride
**Combat Gear** potion of _invisibility_, scroll of _[[spells/Longstrider|longstrider]]_, wand of _barkskin_ (8 charges), wand of _cure moderate wounds_ (15 charges), wand of _magic fang_ (8 charges); **Other Gear** +1 _[[items/Armor/Hide armor|hide armor]]_, darkwood masterwork _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, masterwork _sickle_, masterwork _sling_ with 20 bullets, _[[items/Mundane/Antitoxin|antitoxin]]_, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 52 gp

Evasive as the wind, these skittish druids tend to stay away from others, using their formidable powers to escape even the most hazardous situations.
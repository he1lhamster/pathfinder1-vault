---
cssclass: [monsters]
title1: Taiga Stalker
title2: Taiga Stalker
CR: 15
sources:
- name: NPC Codex
  page: 75
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 51200
race: Human
classes:
- druid 16
alignment: LN
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 2
AC:
  AC: 26
  touch: 13
  flat_footed: 25
  components:
    armor: 10
    deflection: 2
    dex: 1
    shield: 3
HP:
  HP: 119
  long: 16d8+44
saves:
  fort: 14
  ref: 9
  will: 18
  other: +4 vs. fey and plant-targeted effects
immunities:
- poison
resistances:
  cold: 20
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 scimitar +15/+10/+5 (1d6+3/18-20)
      entries:
      - - damage: 1d6+3
          crit_range: 18-20
      attack: +1 scimitar
      bonus:
      - 15
      - 10
      - 5
  ranged:
  - - text: +1 sling +15/+10/+5 (1d4+3)
      entries:
      - - damage: 1d4+3
      attack: +1 sling
      bonus:
      - 15
      - 10
      - 5
  special:
  - wild shape 7/day
spell_like_abilities:
  entries:
  - name: icicle
    source: default
    freq: 9/day
  sources:
  - name: default
    CL: 16
    concentration: 22
spells:
  entries:
  - name: empowered cone of cold
    source: Druid
    level: 8
    count: 2
    DC: 22
  - is_domain_spell: true
    name: horrid wilting
    source: Druid
    level: 8
    DC: 24
  - name: elemental body IVD
    source: Druid
    level: 7
    other: water only
  - name: fire storm
    source: Druid
    level: 7
    DC: 23
  - name: heal
    source: Druid
    level: 7
  - name: true seeing
    source: Druid
    level: 7
  - name: antilife shell
    source: Druid
    level: 6
  - is_domain_spell: true
    name: cone of cold
    source: Druid
    level: 6
    DC: 22
  - name: empowered flame strike
    source: Druid
    level: 6
    DC: 20
  - name: greater dispel magic
    source: Druid
    level: 6
  - name: wall of stone
    source: Druid
    level: 6
  - name: animal growth
    source: Druid
    level: 5
    count: 2
    DC: 21
  - name: cure critical wounds
    source: Druid
    level: 5
  - name: death ward
    source: Druid
    level: 5
  - is_domain_spell: true
    name: ice storm
    source: Druid
    level: 5
  - name: stoneskin
    source: Druid
    level: 5
  - name: air walk
    source: Druid
    level: 4
  - is_domain_spell: true
    name: control weather
    source: Druid
    level: 4
  - name: dispel magic
    source: Druid
    level: 4
  - name: flame strike
    source: Druid
    level: 4
    DC: 20
  - name: freedom of movement
    source: Druid
    level: 4
  - name: spike stones
    source: Druid
    level: 4
    DC: 20
  - name: daylight
    source: Druid
    level: 3
  - name: greater magic fang
    source: Druid
    level: 3
    count: 3
  - name: protection from energy
    source: Druid
    level: 3
  - is_domain_spell: true
    name: water breathing
    source: Druid
    level: 3
  - name: barkskin
    source: Druid
    level: 2
    count: 3
  - name: bear's endurance
    source: Druid
    level: 2
  - name: bull's strength
    source: Druid
    level: 2
  - name: cat's grace
    source: Druid
    level: 2
  - is_domain_spell: true
    name: fog cloud
    source: Druid
    level: 2
  - name: cure light wounds
    source: Druid
    level: 1
    count: 3
  - name: faerie fire
    source: Druid
    level: 1
  - name: longstrider
    source: Druid
    level: 1
  - is_domain_spell: true
    name: obscuring mist
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
  - name: create water
    source: Druid
    level: 0
  - name: detect magic
    source: Druid
    level: 0
  - name: light
    source: Druid
    level: 0
  - name: mending
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 16
    concentration: 22
    slots:
      0: at-will
    domains:
    - water
tactics:
  Before Combat: Twice per month, the druid casts ironwood on her armor and also casts
    liveoak.
  During Combat: The druid casts empowered cone of cold, then begins spontaneously
    summoning creatures and casting animal growth, stoneskin, and greater magic fang
    on them. While they are fighting, she casts spells to heal them and enhance her
    abilities. When entering melee, she casts true seeing, death ward, freedom of
    movement, and barkskin on herself, and drinks her potions of haste and displacement
    before wild shaping into a Huge water elemental.
ability_scores:
  STR: 14
  DEX: 14
  CON: 14
  INT: 10
  WIS: 22
  CHA: 8
BAB: 12
CMB: 14
CMD: 28
feats:
- name: Augment Summoning
- name: Combat Casting
- name: Empower Spell
- name: Heavy Armor Proficiency
- name: Improved Vital Strike
- name: Natural Spell
- name: Power Attack
- name: Spell Focus (conjuration)
- name: Vital Strike
skills:
  Craft (woodworking): 11
  Fly: 8
  Handle Animal: 9
  Heal: 14
  Knowledge (geography): 9
  Knowledge (nature): 15
  Perception: 21
  Ride: 3
  Spellcraft: 17
  Survival: 22
languages:
- Common
special_qualities:
- a thousand faces
- nature bond (Water domain)
- nature sense
- timeless body
- trackless step
- wild empathy +15
- woodland stride
gear:
  combat:
  - potion of haste
  - potion of displacement
  - scroll of word of recall
  - wand of cure serious wounds (10 charges)
  other:
  - +1 wild ironwood full plate
  - +1 darkwood heavy wooden shield
  - +1 scimitar
  - +1 sling with 10 bullets
  - cloak of resistance +2
  - headband of inspired wisdom +4
  - ring of protection +2
  - cold weather outfit
  - healer's kit
  - holly and mistletoe
  - masterwork woodcarving tools
  - spell component pouch
  - 110 gp
desc_long: These hardy druids patrol and protect the icy reaches of northern forests,
  and command spells and abilities equally as cold and unforgiving.

---

# Taiga Stalker

**Source** NPC Codex pg. 75
**XP** 51,200
Human _[[classes/Druid|druid]]_ 16

LN Medium humanoid (human)
**Init** +2; **Senses** Perception +21

##### Defense

**AC** 26, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+10 armor, +2 _[[spells/Deflection|deflection]]_, +1 Dex, +3 _[[spells/Shield|shield]]_)
**hp** 119 (16d8+44)
**Fort** +14, **Ref** +9, **Will** +18; +4 vs. fey and plant-targeted effects
**Immune** poison; **Resist** cold 20

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Scimitar|scimitar]]_ +15/+10/+5 (1d6+3/18–20)
**Ranged** +1 _[[items/Weapon/Sling|sling]]_ +15/+10/+5 (1d4+3)
**Special Attacks** wild shape 7/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +22)
9/day—icicle
**_Druid_ Spells Prepared **(CL 16th; concentration +22)
8th—empowered _[[spells/Cone of Cold|cone of cold]]_ (2, DC 22), horrid wiltingD (DC 24)
7th—elemental body IVD (water only), _[[spells/Fire Storm|fire storm]]_ (DC 23), _[[spells/Heal|heal]]_, _[[spells/True Seeing|true seeing]]_
6th—_[[spells/Antilife Shell|antilife shell]]_, cone of coldD (DC 22), empowered _[[spells/Flame Strike|flame strike]]_ (DC 20), greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Wall Of Stone|wall of stone]]_
5th—_[[spells/Animal Growth|animal growth]]_ (2, DC 21), _[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Death Ward|death ward]]_, _[[spells/Ice Storm|ice storm]]_, _[[spells/Stoneskin|stoneskin]]_
4th—_[[spells/Air Walk|air walk]]_, _[[spells/Control Weather|control weather]]_, _dispel magic_, _flame strike_ (DC 20), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Spike Stones|spike stones]]_ (DC 20)
3rd—_[[spells/Daylight|daylight]]_, greater _[[spells/Magic Fang|magic fang]]_ (3), _[[spells/Protection from Energy|protection from energy]]_, _[[universal monster rules/Water Breathing|water breathing]]_
2nd—_[[spells/Barkskin|barkskin]]_ (3), bear’s _[[feats/Endurance|endurance]]_, bull’s strength, cat’s _[[spells/Grace|grace]]_, _[[spells/Fog Cloud|fog cloud]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_ (3), _[[spells/Faerie Fire|faerie fire]]_, _[[spells/Longstrider|longstrider]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Speak with Animals|speak with animals]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mending|mending]]_
**D **Domain spell; **Domain **Water

### Tactics

**Before Combat **Twice per month, the _druid_ casts _[[spells/Ironwood|ironwood]]_ on her armor and also casts _[[spells/Liveoak|liveoak]]_.
**During Combat **The _druid_ casts empowered _cone of cold_, then begins spontaneously summoning creatures and casting _animal growth_, _stoneskin_, and greater _magic fang_ on them. While they are fighting, she casts spells to _heal_ them and enhance her abilities. When entering melee, she casts _true seeing_, _death ward_, _freedom of movement_, and _barkskin_ on herself, and drinks her potions of _[[spells/Haste|haste]]_ and _[[spells/Displacement|displacement]]_ before wild shaping into a Huge water elemental.

##### Statistics
**Str** 14, **Dex** 14, **Con** 14, **Int** 10, **Wis** 22, **Cha** 8
**Base Atk** +12; **CMB** +14; **CMD** 28
**Feats** _[[feats/Augment Summoning|Augment Summoning]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Heavy Armor Proficiency|Heavy Armor Proficiency]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spell Focus|Spell Focus]]_ (conjuration), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Craft (woodworking) +11, Fly +8, Handle Animal +9, _Heal_ +14, Knowledge (geography) +9, Knowledge (nature) +15, Perception +21, Ride +3, Spellcraft +17, Survival +22
**Languages** Common
**SQ** a thousand faces, nature bond (Water domain), nature sense, timeless body, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, wild _[[feats/Empathy|empathy]]_ +15, woodland stride
**Combat Gear** potion of _haste_, potion of _displacement_, scroll of _[[spells/Word of Recall|word of recall]]_, wand of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (10 charges); **Other Gear** +1 wild _ironwood_ _[[items/Armor/Full plate|full plate]]_, +1 darkwood _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, +1 _scimitar_, +1 _sling_ with 10 bullets, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +4|headband of _inspired_ wisdom +4]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, cold weather outfit, _[[npcs/Healer|healer]]_’s kit, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, masterwork woodcarving tools, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 110 gp

These hardy druids patrol and protect the icy reaches of northern forests, and _[[spells/Command|command]]_ spells and abilities equally as cold and unforgiving.
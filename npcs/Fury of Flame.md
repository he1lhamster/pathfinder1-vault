---
cssclass: [monsters]
title1: Fury of Flame
title2: Fury of Flame
CR: 13
sources:
- name: NPC Codex
  page: 73
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 25600
race: Human
classes:
- druid 14
alignment: NE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 1
AC:
  AC: 28
  touch: 13
  flat_footed: 27
  components:
    armor: 7
    deflection: 2
    dex: 1
    natural: 5
    shield: 3
HP:
  HP: 120
  long: 14d8+54
saves:
  fort: 13
  ref: 7
  will: 15
  other: +4 vs. fey and plant-targeted effects
immunities:
- poison
resistances:
  fire: 20
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 club +16/+11 (1d6+6)
      entries:
      - - damage: 1d6+6
      attack: +1 club
      bonus:
      - 16
      - 11
  ranged:
  - - text: mwk shortspear +12/+7 (1d6+5)
      entries:
      - - damage: 1d6+5
      attack: mwk shortspear
      bonus:
      - 12
      - 7
  special:
  - wild shape 6/day
spell_like_abilities:
  entries:
  - name: fire bolt
    source: default
    freq: 7/day
  sources:
  - name: default
    CL: 14
    concentration: 18
spells:
  entries:
  - is_domain_spell: true
    name: elemental body IV
    source: Druid
    level: 7
    other: fire only
  - name: fire storm
    source: Druid
    level: 7
    count: 2
    DC: 23
  - is_domain_spell: true
    name: fire seeds
    source: Druid
    level: 6
  - name: empowered flame strike
    source: Druid
    level: 6
    count: 2
    DC: 20
  - name: wall of stone
    source: Druid
    level: 6
  - is_domain_spell: true
    name: fire shield
    source: Druid
    level: 5
  - name: empowered fireball
    source: Druid
    level: 5
    count: 2
    DC: 19
  - name: wall of fire
    source: Druid
    level: 5
  - name: air walk
    source: Druid
    level: 4
  - name: cure serious wounds
    source: Druid
    level: 4
  - name: dispel magic
    source: Druid
    level: 4
  - name: freedom of movement
    source: Druid
    level: 4
  - name: ice storm
    source: Druid
    level: 4
    DC: 20
  - is_domain_spell: true
    name: wall of fire
    source: Druid
    level: 4
  - name: dominate animal
    source: Druid
    level: 3
    DC: 17
  - is_domain_spell: true
    name: fireball
    source: Druid
    level: 3
    count: 2
    DC: 19
  - name: greater magic fang
    source: Druid
    level: 3
    count: 2
  - name: spike growth
    source: Druid
    level: 3
    DC: 17
  - name: barkskin
    source: Druid
    level: 2
    count: 3
  - name: bull's strength
    source: Druid
    level: 2
  - name: cat's grace
    source: Druid
    level: 2
  - is_domain_spell: true
    name: produce flame
    source: Druid
    level: 2
  - is_domain_spell: true
    name: burning hands
    source: Druid
    level: 1
    count: 2
    DC: 17
  - name: cure light wounds
    source: Druid
    level: 1
  - name: faerie fire
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
  - name: flare
    source: Druid
    level: 0
    DC: 16
  - name: light
    source: Druid
    level: 0
  - name: stabilize
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 14
    concentration: 18
    slots:
      0: at-will
    domains:
    - fire
tactics:
  Before Combat: The druid casts barkskin. He also casts ironwood on his breastplate
    twice per month, and endure elements every morning.
  During Combat: The druid wild shapes into a Huge fire elemental when casting offensive
    spells, and wild shapes into a Huge earth elemental when entering melee. He opens
    with spells such as fire storm and empowered fireball. Before entering melee,
    he casts cat's grace, freedom of movement, and greater magic fang on himself.
  Base Statistics: Without barkskin, the druid's statistics are AC 23, touch 13, flat-footed
    22.
ability_scores:
  STR: 20
  DEX: 12
  CON: 15
  INT: 10
  WIS: 18
  CHA: 8
BAB: 10
CMB: 15
CMD: 28
feats:
- name: Combat Casting
- name: Empower Spell
- name: Greater Spell Focus (evocation)
- name: Natural Spell
- name: Power Attack
- name: Spell Focus (evocation)
- name: Toughness
- name: Vital Strike
skills:
  Climb: 8
  Fly: 5
  Handle Animal: 6
  Heal: 12
  Knowledge (geography): 7
  Knowledge (nature): 11
  Perception: 15
  Perform (oratory): 5
  Ride: 7
  Spellcraft: 11
  Survival: 23
  Swim: 9
languages:
- Common
special_qualities:
- a thousand faces
- nature bond (Fire domain)
- nature sense
- trackless step
- wild empathy +13
- woodland stride
gear:
  combat:
  - potion of cure serious wounds
  - potion of haste
  other:
  - +1 ironwood breastplate
  - +1 darkwood heavy wooden shield
  - +1 club
  - masterwork shortspear
  - belt of physical might +2 (Str, Con)
  - cloak of resistance +2
  - handy haversack
  - headband of inspired wisdom +2
  - ring of protection +2
  - bedroll
  - healer's kit
  - holly and mistletoe
  - silk rope (50 ft.)
  - spell component pouch
  - 27 gp
desc_long: Controlling the power of fire and earth, these druids are natural wrath
  incarnate.

---

# Fury of Flame

**Source** NPC Codex pg. 73
**XP** 25,600
Human _[[classes/Druid|druid]]_ 14

NE Medium humanoid (human)
**Init** +1; **Senses** Perception +15

##### Defense

**AC** 28, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+7 armor, +2 _[[spells/Deflection|deflection]]_, +1 Dex, +5 natural, +3 _[[spells/Shield|shield]]_)
**hp** 120 (14d8+54)
**Fort** +13, **Ref** +7, **Will** +15; +4 vs. fey and plant-targeted effects
**Immune** poison; **Resist** fire 20

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Club|club]]_ +16/+11 (1d6+6)
**Ranged** mwk _[[items/Weapon/Shortspear|shortspear]]_ +12/+7 (1d6+5)
**Special Attacks** wild shape 6/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +18)
7/day—fire bolt
**_Druid_ Spells Prepared **(CL 14th; concentration +18)
7th—elemental body IVD (fire only), _[[spells/Fire Storm|fire storm]]_ (2, DC 23)
6th—_[[spells/Fire Seeds|fire seeds]]_, empowered _[[spells/Flame Strike|flame strike]]_ (2, DC 20), _[[spells/Wall Of Stone|wall of stone]]_
5th—_[[spells/Fire Shield|fire shield]]_, empowered _[[spells/Fireball|fireball]]_ (2, DC 19), _[[spells/Wall Of Fire|wall of fire]]_
4th—_[[spells/Air Walk|air walk]]_, _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Ice Storm|ice storm]]_ (DC 20), _wall of fire_
3rd—_[[spells/Dominate Animal|dominate animal]]_ (DC 17), _fireball_ (2, DC 19), greater _[[spells/Magic Fang|magic fang]]_ (2), _[[spells/Spike Growth|spike growth]]_ (DC 17)
2nd—_[[spells/Barkskin|barkskin]]_ (3), bull’s strength, cat’s _[[spells/Grace|grace]]_, _[[spells/Produce Flame|produce flame]]_
1st—_[[spells/Burning Hands|burning hands]]_ (2, DC 17), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Faerie Fire|faerie fire]]_, _[[spells/Shillelagh|shillelagh]]_, _[[spells/Speak with Animals|speak with animals]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Flare|flare]]_ (DC 16), light, stabilize
**D **Domain spell; **Domain **Fire

### Tactics

**Before Combat **The _druid_ casts _barkskin_. He also casts _[[spells/Ironwood|ironwood]]_ on his _[[items/Armor/Breastplate|breastplate]]_ twice per month, and _[[spells/Endure Elements|endure elements]]_ every morning.
**During Combat **The _druid_ wild shapes into a Huge fire elemental when casting offensive spells, and wild shapes into a Huge earth elemental when entering melee. He opens with spells such as _fire storm_ and empowered _fireball_. Before entering melee, he casts cat’s _grace_, _freedom of movement_, and greater _magic fang_ on himself.
**Base Statistics **Without _barkskin_, the _druid_’s statistics are **AC **23, touch 13, _flat-footed_ 22.

##### Statistics
**Str** 20, **Dex** 12, **Con** 15, **Int** 10, **Wis** 18, **Cha** 8
**Base Atk** +10; **CMB** +15; **CMD** 28
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (evocation), _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation), _[[feats/Toughness|Toughness]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +8, Fly +5, Handle Animal +6, _[[spells/Heal|Heal]]_ +12, Knowledge (geography) +7, Knowledge (nature) +11, Perception +15, Perform (oratory) +5, Ride +7, Spellcraft +11, Survival +23, Swim +9
**Languages** Common
**SQ** a thousand faces, nature bond (Fire domain), nature sense, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, wild _[[feats/Empathy|empathy]]_ +13, woodland stride
**Combat Gear** potion of _cure serious wounds_, potion of _[[spells/Haste|haste]]_; **Other Gear** +1 _ironwood_ _breastplate_, +1 darkwood _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, +1 _club_, masterwork _shortspear_, _[[items/Wondrous Item/Belt of Physical Might +2|belt of physical might +2]]_ (Str, Con), _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Handy Haversack|handy haversack]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, _[[items/Mundane/Bedroll|bedroll]]_, _[[npcs/Healer|healer]]_’s kit, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, _[[items/Mundane/Silk rope|silk rope]]_ (50 ft.), _[[items/Mundane/Spell component pouch|spell component pouch]]_, 27 gp

Controlling the power of fire and earth, these druids are natural wrath incarnate.
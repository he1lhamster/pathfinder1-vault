---
cssclass: [monsters]
title1: Rage Flame
title2: Rage Flame
CR: 18
sources:
- name: NPC Codex
  page: 78
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 153600
race: Half-orc
classes:
- druid 19
alignment: CN
size: Medium
type: humanoid
subtypes:
- human
- orc
initiative:
  bonus: 6
senses:
  darkvision: 60
AC:
  AC: 28
  touch: 16
  flat_footed: 26
  components:
    armor: 8
    deflection: 3
    dex: 2
    insight: 1
    shield: 4
HP:
  HP: 161
  long: 19d8+72
saves:
  fort: 16
  ref: 11
  will: 22
  other: +4 vs. fey and plant-targeted effects
defensive_abilities:
- orc ferocity
immunities:
- poison
resistances:
  fire: 20
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 club +17/+12/+7 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: +1 club
      bonus:
      - 17
      - 12
      - 7
  ranged:
  - - text: +1 sling +17/+12/+7 (1d4+3)
      entries:
      - - damage: 1d4+3
      attack: +1 sling
      bonus:
      - 17
      - 12
      - 7
  special:
  - wild shape 8/day
spell_like_abilities:
  entries:
  - name: fire bolt
    source: default
    freq: 11/day
  sources:
  - name: default
    CL: 19
    concentration: 27
spells:
  entries:
  - is_domain_spell: true
    name: elemental swarm
    source: Druid
    level: 9
    other: fire spell only
  - name: empowered fire storm
    source: Druid
    level: 9
    count: 3
    DC: 27
  - name: quickened cure serious wounds
    source: Druid
    level: 8
  - is_domain_spell: true
    name: incendiary cloud
    source: Druid
    level: 8
    DC: 26
  - name: reverse gravity
    source: Druid
    level: 8
  - name: sunburst
    source: Druid
    level: 8
    DC: 28
  - name: word of recall
    source: Druid
    level: 8
  - name: quickened cure moderate wounds
    source: Druid
    level: 7
  - name: fire storm
    source: Druid
    level: 7
    count: 2
    DC: 27
  - is_domain_spell: true
    name: elemental body IV
    source: Druid
    level: 7
    other: fire only
  - name: heal
    source: Druid
    level: 7
  - name: true seeing
    source: Druid
    level: 7
  - name: fire seedsD
    source: Druid
    level: 6
  - name: empowered flame strike
    source: Druid
    level: 6
    count: 3
    DC: 24
  - name: greater dispel magic
    source: Druid
    level: 6
  - name: mass cat's grace
    source: Druid
    level: 6
  - name: cure critical wounds
    source: Druid
    level: 5
    count: 2
  - is_domain_spell: true
    name: fire shield
    source: Druid
    level: 5
  - name: stoneskin
    source: Druid
    level: 5
  - name: wall of fire
    source: Druid
    level: 5
    count: 2
  - name: dispel magic
    source: Druid
    level: 4
    count: 2
  - name: flame strike
    source: Druid
    level: 4
    count: 2
    DC: 24
  - name: freedom of movement
    source: Druid
    level: 4
  - name: ice storm
    source: Druid
    level: 4
    DC: 24
  - is_domain_spell: true
    name: wall of fire
    source: Druid
    level: 4
  - is_domain_spell: true
    name: fireball
    source: Druid
    level: 3
    count: 5
    DC: 23
  - name: greater magic fang
    source: Druid
    level: 3
  - name: protection from energy
    source: Druid
    level: 3
    DC: 21
  - name: barkskin
    source: Druid
    level: 2
    count: 2
  - name: bull's strength
    source: Druid
    level: 2
    count: 2
  - name: hold animal
    source: Druid
    level: 2
    DC: 20
  - is_domain_spell: true
    name: produce flame
    source: Druid
    level: 2
  - name: lesser restoration
    source: Druid
    level: 2
  - is_domain_spell: true
    name: burning hands
    source: Druid
    level: 1
    count: 2
    DC: 21
  - name: cure light wounds
    source: Druid
    level: 1
  - name: endure elements
    source: Druid
    level: 1
  - name: faerie fire
    source: Druid
    level: 1
    count: 2
  - name: shillelagh
    source: Druid
    level: 1
  - name: create water
    source: Druid
    level: 0
  - name: flare
    source: Druid
    level: 0
    DC: 20
  - name: guidance
    source: Druid
    level: 0
  - name: resistance
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 19
    concentration: 27
    slots:
      0: at-will
    domains:
    - fire
tactics:
  Before Combat: The druid casts shambler once per week and casts ironwood on his
    armor every 19 days.
  During Combat: The druid sends shambling mounds into combat, casts mass cat's grace,
    wild shapes into a Huge fire elemental, and moves in to flank.
ability_scores:
  STR: 14
  DEX: 14
  CON: 14
  INT: 10
  WIS: 26
  CHA: 8
BAB: 14
CMB: 16
CMD: 32
feats:
- name: Blind-Fight
- name: Combat Casting
- name: Empower Spell
- name: Greater Spell Focus (evocation)
- name: Improved Initiative
- name: Natural Spell
- name: Power Attack
- name: Quicken Spell
- name: Spell Focus (evocation)
- name: Toughness
skills:
  Climb: 6
  Fly: 6
  Handle Animal: 5
  Intimidate: 1
  Knowledge (geography): 7
  Knowledge (nature): 13
  Knowledge (planes): 4
  Linguistics: 5
  Perception: 23
  Ride: 6
  Sense Motive: 16
  Spellcraft: 15
  Survival: 21
  Swim: 6
languages:
- Auran
- Common
- Draconic
- Druidic
- Giant
- Ignan
- Orc
- Terran
special_qualities:
- a thousand faces
- nature bond (Fire domain)
- nature sense
- orc blood
- timeless body
- trackless step
- weapon familiarity
- wild empathy +18
- woodland stride
gear:
  combat:
  - potions of cure serious wounds (2)
  - potion of haste
  - scroll of mass cure serious wounds
  other:
  - +2 wild ironwood breastplate
  - +2 animated darkwood heavy wooden shield
  - +1 club
  - +1 sling with 10 bullets
  - belt of mighty constitution +2
  - cloak of resistance +3
  - dusty rose prism ioun stone
  - headband of inspired wisdom +6
  - ring of protection +3
  - holly and mistletoe
  - spell component pouch
  - silver crown (worth 200 gp)
  - 63 gp
desc_long: These druids dwell in the most explosive spots in the world.

---

# Rage Flame

**Source** NPC Codex pg. 78
**XP** 153,600
Half-orc _[[classes/Druid|druid]]_ 19

CN Medium humanoid (human, _[[monsters/Orc|orc]]_)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +23

##### Defense

**AC** 28, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+8 armor, +3 _[[spells/Deflection|deflection]]_, +2 Dex, +1 insight, +4 _[[spells/Shield|shield]]_)
**hp** 161 (19d8+72)
**Fort** +16, **Ref** +11, **Will** +22; +4 vs. fey and plant-targeted effects
**Defensive Abilities** _orc_ _[[universal monster rules/Ferocity|ferocity]]_; **Immune** poison; **Resist** fire 20

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Club|club]]_ +17/+12/+7 (1d6+3)
**Ranged** +1 _[[items/Weapon/Sling|sling]]_ +17/+12/+7 (1d4+3)
**Special Attacks** wild shape 8/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 19th; concentration +27)
11/day—fire bolt
**_Druid_ Spells Prepared **(CL 19th; concentration +27)
9th—elemental swarmD (fire spell only), empowered _[[spells/Fire Storm|fire storm]]_ (3, DC 27)
8th—quickened _[[spells/Cure Serious Wounds|cure serious wounds]]_, incendiary cloudD (DC 26), _[[spells/Reverse Gravity|reverse gravity]]_, _[[spells/Sunburst|sunburst]]_ (DC 28), _[[spells/Word of Recall|word of recall]]_
7th—quickened _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _fire storm_ (2, DC 27), elemental body IVD (fire only), _[[spells/Heal|heal]]_, _[[spells/True Seeing|true seeing]]_
6th—fire seedsD, empowered _[[spells/Flame Strike|flame strike]]_ (3, DC 24), greater _[[spells/Dispel Magic|dispel magic]]_, mass _[[spells/Cat's Grace|cat's grace]]_
5th—_[[spells/Cure Critical Wounds|cure critical wounds]]_ (2), _[[spells/Fire Shield|fire shield]]_, _[[spells/Stoneskin|stoneskin]]_, _[[spells/Wall Of Fire|wall of fire]]_ (2)
4th—_dispel magic_ (2), _flame strike_ (2, DC 24), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Ice Storm|ice storm]]_ (DC 24), _wall of fire_
3rd—fireballD (5, DC 23), greater _[[spells/Magic Fang|magic fang]]_, _[[spells/Protection from Energy|protection from energy]]_ (DC 21)
2nd—_[[spells/Barkskin|barkskin]]_ (2), _[[spells/Bull's Strength|bull's strength]]_ (2), _[[spells/Hold Animal|hold animal]]_ (DC 20), _[[spells/Produce Flame|produce flame]]_, lesser _[[spells/Restoration|restoration]]_
1st—_[[items/Weapon Magic Abilities/Burning|burning]]_ handsD (2, DC 21), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Endure Elements|endure elements]]_, _[[spells/Faerie Fire|faerie fire]]_ (2), _[[spells/Shillelagh|shillelagh]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Flare|flare]]_ (DC 20), _[[spells/Guidance|guidance]]_, _[[universal monster rules/Resistance|resistance]]_
**D **Domain spell; **Domain **Fire

### Tactics

**Before Combat **The _druid_ casts _[[spells/Shambler|shambler]]_ once per week and casts _[[spells/Ironwood|ironwood]]_ on his armor every 19 days.
**During Combat **The _druid_ sends shambling mounds into combat, casts mass cat’s _[[spells/Grace|grace]]_, wild shapes into a Huge fire elemental, and moves in to flank.

##### Statistics
**Str** 14, **Dex** 14, **Con** 14, **Int** 10, **Wis** 26, **Cha** 8
**Base Atk** +14; **CMB** +16; **CMD** 32
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (evocation), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation), _[[feats/Toughness|Toughness]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +6, Fly +6, Handle Animal +5, Intimidate +1, Knowledge (geography) +7, Knowledge (nature) +13, Knowledge (planes) +4, Linguistics +5, Perception +23, Ride +6, Sense Motive +16, Spellcraft +15, Survival +21, Swim +6
**Languages** Auran, Common, Draconic, Druidic, Giant, Ignan, _Orc_, Terran
**SQ** a thousand faces, nature bond (Fire domain), nature sense, _orc_ blood, timeless body, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, weapon familiarity, wild _[[feats/Empathy|empathy]]_ +18, woodland stride
**Combat Gear** potions of _cure serious wounds_ (2), potion of _[[spells/Haste|haste]]_, scroll of mass _cure serious wounds_; **Other Gear** +2 wild _ironwood_ _[[items/Armor/Breastplate|breastplate]]_, +2 _[[items/Armor Magic Abilities/Animated|animated]]_ darkwood _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, +1 _club_, +1 _sling_ with 10 bullets, _[[items/Wondrous Item/Belt of Mighty Constitution +2|belt of mighty constitution +2]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Dusty Rose Prism Ioun Stone|dusty rose prism ioun stone]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +6|headband of _inspired_ wisdom +6]]_, _[[items/Ring/Ring of Protection +3|ring of protection +3]]_, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, silver crown (worth 200 gp), 63 gp

These druids dwell in the most explosive spots in the world.
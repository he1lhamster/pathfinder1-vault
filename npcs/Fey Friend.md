---
cssclass: [monsters]
title1: Fey Friend
title2: Fey Friend
CR: 12
sources:
- name: NPC Codex
  page: 72
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 19200
race: Gnome
classes:
- druid 13
alignment: CN
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 2
senses:
  low-light vision: true
AC:
  AC: 24
  touch: 15
  flat_footed: 21
  components:
    armor: 6
    deflection: 1
    dex: 2
    dodge: 1
    shield: 3
    size: 1
HP:
  HP: 96
  long: 13d8+34
saves:
  fort: 12
  ref: 8
  will: 15
  other: +2 vs. illusions, +4 vs. fey and plant-targeted effects
defensive_abilities:
- 25% chance to negate critical hits and sneak attacks
- defensive training (+4 dodge bonus to AC vs. giants)
immunities:
- poison
resistances:
  cold: 20
speeds:
  base: 15
attacks:
  melee:
  - - text: +1 sickle +13/+8 (1d4)
      entries:
      - - damage: 1d4
      attack: +1 sickle
      bonus:
      - 13
      - 8
  ranged:
  - - text: mwk sling +13/+8 (1d3-1)
      entries:
      - - damage: 1d3-1
      attack: mwk sling
      bonus:
      - 13
      - 8
  special:
  - +1 on attack rolls against goblinoid and reptilian humanoids
  - wild shape 5/day
spell_like_abilities:
  entries:
  - name: icicle
    source: default
    freq: 8/day
  sources:
  - name: default
    CL: 13
    concentration: 18
spells:
  entries:
  - name: creeping doom
    source: Druid
    level: 7
    DC: 23
  - is_domain_spell: true
    name: elemental body IV
    source: Druid
    level: 7
    other: water only
  - name: antilife shell
    source: Druid
    level: 6
  - is_domain_spell: true
    name: cone of cold
    source: Druid
    level: 6
    count: 2
    DC: 21
  - name: call lightning storm
    source: Druid
    level: 5
    DC: 20
  - name: cure critical wounds
    source: Druid
    level: 5
    count: 2
  - is_domain_spell: true
    name: ice storm
    source: Druid
    level: 5
  - name: stoneskin
    source: Druid
    level: 5
  - name: cure serious wounds
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
    DC: 19
  - name: freedom of movement
    source: Druid
    level: 4
  - name: spike stones
    source: Druid
    level: 4
    DC: 19
  - name: greater magic fang
    source: Druid
    level: 3
  - name: protection from energy
    source: Druid
    level: 3
  - name: quench
    source: Druid
    level: 3
  - name: sleet storm
    source: Druid
    level: 3
  - name: speak with plants
    source: Druid
    level: 3
  - is_domain_spell: true
    name: water breathing
    source: Druid
    level: 3
  - name: barkskin
    source: Druid
    level: 2
    count: 2
  - name: cat's grace
    source: Druid
    level: 2
    count: 2
  - is_domain_spell: true
    name: fog cloud
    source: Druid
    level: 2
  - name: spider climb
    source: Druid
    level: 2
  - name: cure light wounds
    source: Druid
    level: 1
  - name: endure elements
    source: Druid
    level: 1
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
  - name: pass without trace
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
  - name: flare
    source: Druid
    level: 0
    DC: 15
  - name: guidance
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
    CL: 13
    concentration: 18
    slots:
      0: at-will
    domains:
    - water
tactics:
  Before Combat: The druid casts liveoak every 13 days, and endure elements each morning.
  During Combat: The druid casts stoneskin on her treant and orders it into combat.
    She wild shapes into a bat and casts cat's grace and barkskin on herself. She
    then casts cure spells or spontaneous summon nature's ally as necessary. If entering
    melee, she casts protection from energy and greater magic fang, then wild shapes
    into a treant herself.
ability_scores:
  STR: 8
  DEX: 14
  CON: 14
  INT: 13
  WIS: 20
  CHA: 10
BAB: 9
CMB: 7
CMD: 21
feats:
- name: Augment Summoning
- name: Combat Casting
- name: Combat Expertise
- name: Dodge
- name: Natural Spell
- name: Spell Focus (conjuration)
- name: Weapon Finesse
skills:
  Craft (woodworking): 11
  Handle Animal: 6
  Heal: 12
  Knowledge (geography): 7
  Knowledge (nature): 14
  Linguistics: 6
  Perception: 20
  Ride: 7
  Spellcraft: 14
  Survival: 22
  Swim: 4
languages:
- Aquan
- Auran
- Common
- Druidic
- Giant
- Gnome
- Ignan
- Sylvan
- Terran
special_qualities:
- a thousand faces
- nature bond (Water domain)
- nature sense
- trackless step
- wild empathy +13
- woodland stride
gear:
  combat:
  - potion of cure serious wounds
  - potion of invisibility
  - scroll of heal
  other:
  - +2 glamered hide armor
  - +1 light fortification darkwood heavy wooden shield
  - +1 sickle
  - masterwork sling with 20 bullets
  - cloak of resistance +2
  - headband of inspired wisdom +2
  - ring of protection +1
  - holly and mistletoe
  - spell component pouch
  - 42 gp
desc_long: These druids see themselves not as protectors of the forest, but as part
  of it, like the fey they associate with.

---

# Fey Friend

**Source** NPC Codex pg. 72
**XP** 19,200
Gnome _[[classes/Druid|druid]]_ 13

CN Small humanoid (gnome)
**Init** +2; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +20

##### Defense

**AC** 24, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+6 armor, +1 deflection, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +3 _[[spells/Shield|shield]]_, +1 size)
**hp** 96 (13d8+34)
**Fort** +12, **Ref** +8, **Will** +15; +2 vs. illusions, +4 vs. fey and plant-targeted effects
**Defensive Abilities** 25% chance to negate critical hits and sneak attacks, defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _dodge_ bonus to AC vs. giants); **Immune** poison; **Resist** cold 20

##### Offense
**Speed** 15 ft.
**Melee** +1 _[[items/Weapon/Sickle|sickle]]_ +13/+8 (1d4)
**Ranged** mwk _[[items/Weapon/Sling|sling]]_ +13/+8 (1d3–1)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids, wild shape 5/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +18)
8/day—icicle
**_Druid_ Spells Prepared **(CL 13th; concentration +18)
7th—_[[spells/Creeping Doom|creeping doom]]_ (DC 23), elemental body IVD (water only)
6th—_[[spells/Antilife Shell|antilife shell]]_, cone of coldD (2, DC 21)
5th—_[[spells/Call Lightning Storm|call lightning storm]]_ (DC 20), _[[spells/Cure Critical Wounds|cure critical wounds]]_ (2), _[[spells/Ice Storm|ice storm]]_, _[[spells/Stoneskin|stoneskin]]_
4th—_[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Control Weather|control weather]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Flame Strike|flame strike]]_ (DC 19), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Spike Stones|spike stones]]_ (DC 19)
3rd—greater _[[spells/Magic Fang|magic fang]]_, _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Quench|quench]]_, _[[spells/Sleet Storm|sleet storm]]_, _[[spells/Speak with Plants|speak with plants]]_, _[[universal monster rules/Water Breathing|water breathing]]_
2nd—_[[spells/Barkskin|barkskin]]_ (2), cat’s _[[spells/Grace|grace]]_ (2), _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Spider Climb|spider climb]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Endure Elements|endure elements]]_, _[[spells/Faerie Fire|faerie fire]]_, _[[spells/Longstrider|longstrider]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Pass without Trace|pass without trace]]_, _[[spells/Speak with Animals|speak with animals]]_
0 (at will)—_[[spells/Flare|flare]]_ (DC 15), _[[spells/Guidance|guidance]]_, light, stabilize
**D **Domain spell; **Domain **Water

### Tactics

**Before Combat **The _druid_ casts _[[spells/Liveoak|liveoak]]_ every 13 days, and _endure elements_ each morning.
**During Combat **The _druid_ casts _stoneskin_ on her _[[monsters/Treant|treant]]_ and orders it into combat. She wild shapes into a bat and casts cat’s _grace_ and _barkskin_ on herself. She then casts cure spells or spontaneous _[[universal monster rules/Summon|summon]]_ nature’s ally as necessary. If entering melee, she casts _protection from energy_ and greater _magic fang_, then wild shapes into a _treant_ herself.

##### Statistics
**Str** 8, **Dex** 14, **Con** 14, **Int** 13, **Wis** 20, **Cha** 10
**Base Atk** +9; **CMB** +7; **CMD** 21
**Feats** _[[feats/Augment Summoning|Augment Summoning]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _Dodge_, _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Spell Focus|Spell Focus]]_ (conjuration), _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Craft (woodworking) +11, Handle Animal +6, _[[spells/Heal|Heal]]_ +12, Knowledge (geography) +7, Knowledge (nature) +14, Linguistics +6, Perception +20, Ride +7, Spellcraft +14, Survival +22, Swim +4
**Languages** Aquan, Auran, Common, Druidic, Giant, Gnome, Ignan, Sylvan, Terran
**SQ** a thousand faces, nature bond (Water domain), nature sense, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, wild _[[feats/Empathy|empathy]]_ +13, woodland stride
**Combat Gear** potion of _cure serious wounds_, potion of _[[spells/Invisibility|invisibility]]_, scroll of _heal_; **Other Gear** +2 _[[items/Weapon Magic Abilities/Glamered|glamered]]_ _[[items/Armor/Hide armor|hide armor]]_, +1 light _[[universal monster rules/Fortification|fortification]]_ darkwood _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, +1 _sickle_, masterwork _sling_ with 20 bullets, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 42 gp

These druids see themselves not as protectors of the forest, but as part of it, like the fey they _[[feats/Associate|associate]]_ with.
---
cssclass: [monsters]
title1: Mistress of High Places
title2: Mistress of High Places
CR: 10
sources:
- name: NPC Codex
  page: 70
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 9600
race: Half-elf
classes:
- druid 11
alignment: CN
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
  AC: 23
  touch: 13
  flat_footed: 21
  components:
    armor: 7
    deflection: 1
    dex: 1
    dodge: 1
    shield: 3
HP:
  HP: 84
  long: 11d8+31
saves:
  fort: 10
  ref: 5
  will: 13
  other: +2 vs. enchantments, +4 vs. fey and plant-targeted effects
immunities:
- poison
resistances:
  electricity: 10
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 sickle +10/+5 (1d6+2)
      entries:
      - - damage: 1d6+2
      attack: +1 sickle
      bonus:
      - 10
      - 5
  ranged:
  - - text: mwk shortspear +10/+5 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: mwk shortspear
      bonus:
      - 10
      - 5
  special:
  - wild shape 4/day
spell_like_abilities:
  entries:
  - name: lightning arc
    source: default
    freq: 8/day
  sources:
  - name: default
    CL: 11
    concentration: 16
spells:
  entries:
  - is_domain_spell: true
    name: chain lightning
    source: Druid
    level: 6
    DC: 22
  - name: greater dispel magic
    source: Druid
    level: 6
  - name: call lightning storm
    source: Druid
    level: 5
    DC: 21
  - is_domain_spell: true
    name: control winds
    source: Druid
    level: 5
    DC: 20
  - name: cure critical wounds
    source: Druid
    level: 5
  - name: wall of fire
    source: Druid
    level: 5
    DC: 21
  - is_domain_spell: true
    name: air walk
    source: Druid
    level: 4
  - name: cure serious wounds
    source: Druid
    level: 4
  - name: freedom of movement
    source: Druid
    level: 4
  - name: ice storm
    source: Druid
    level: 4
    DC: 20
  - name: scrying
    source: Druid
    level: 4
    DC: 19
  - is_domain_spell: true
    name: gaseous form
    source: Druid
    level: 3
  - name: greater magic fang
    source: Druid
    level: 3
    count: 2
  - name: protection from energy
    source: Druid
    level: 3
    count: 2
  - name: sleet storm
    source: Druid
    level: 3
  - name: animal messenger
    source: Druid
    level: 2
  - name: barkskin
    source: Druid
    level: 2
    count: 3
  - name: fog cloud
    source: Druid
    level: 2
  - is_domain_spell: true
    name: wind wall
    source: Druid
    level: 2
  - name: cure light wounds
    source: Druid
    level: 1
    count: 2
  - name: endure elements
    source: Druid
    level: 1
  - name: faerie fire
    source: Druid
    level: 1
    count: 2
  - is_domain_spell: true
    name: obscuring mist
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
  - name: flare
    source: Druid
    level: 0
    DC: 16
  - name: light
    source: Druid
    level: 0
  - name: mending
    source: Druid
    level: 0
  - name: stabilize
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 11
    concentration: 16
    slots:
      0: at-will
    domains:
    - air
tactics:
  Before Combat: The druid casts ironwood on her breastplate every 11 days, liveoak
    on an oak three times per month, and endure elements every morning.
  During Combat: The druid orders her treant guardian into combat, wild shapes into
    a Large earth elemental, and uses earth glide to flee underground where she casts
    beneficial spells on herself. Once prepared, she moves above ground and opens
    with chain lightning.
ability_scores:
  STR: 12
  DEX: 13
  CON: 15
  INT: 8
  WIS: 20
  CHA: 10
BAB: 8
CMB: 9
CMD: 22
feats:
- name: Dodge
- name: Improved Initiative
- name: Mobility
- name: Natural Spell
- name: Skill Focus (Survival)
- name: Spell Focus (evocation)
- name: Vital Strike
skills:
  Fly: 6
  Handle Animal: 6
  Heal: 9
  Knowledge (nature): 9
  Knowledge (planes): 3
  Linguistics: 2
  Perception: 14
  Perform (dance): 2
  Spellcraft: 5
  Survival: 18
languages:
- Aquan
- Auran
- Common
- Druidic
- Elven
- Ignan
special_qualities:
- elf blood
- nature bond (Air domain)
- nature sense
- trackless step
- wild empathy +11
- woodland stride
gear:
  combat:
  - potion of haste
  - wand of cure moderate wounds (6 charges)
  other:
  - +1 ironwood breastplate
  - +1 darkwood heavy wooden shield
  - +1 sickle
  - masterwork shortspears (3)
  - bag of holding (type I)
  - cloak of resistance +1
  - headband of inspired wisdom +2
  - ring of protection +1
  - holly and mistletoe
  - spell component pouch
  - 289 gp
desc_long: These guardians of mountain peaks traffic with air and ice elementals,
  summoning forth the spirits of the mountain storms in order to protect their sacred
  places.

---

# Mistress of High Places

**Source** NPC Codex pg. 70
**XP** 9,600
Half-elf _[[classes/Druid|druid]]_ 11

CN Medium humanoid (elf, human)
**Init** +5; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +14

##### Defense

**AC** 23, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+7 armor, +1 _[[spells/Deflection|deflection]]_, +1 Dex, +1 _[[feats/Dodge|dodge]]_, +3 _[[spells/Shield|shield]]_)
**hp** 84 (11d8+31)
**Fort** +10, **Ref** +5, **Will** +13; +2 vs. enchantments, +4 vs. fey and plant-targeted effects
**Immune** poison; **Resist** electricity 10

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Sickle|sickle]]_ +10/+5 (1d6+2)
**Ranged** mwk _[[items/Weapon/Shortspear|shortspear]]_ +10/+5 (1d6+1)
**Special Attacks** wild shape 4/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +16)
8/day—_[[spells/Lightning Arc|lightning arc]]_
**_Druid_ Spells Prepared **(CL 11th; concentration +16)
6th—_[[spells/Chain Lightning|chain lightning]]_ (DC 22), greater _[[spells/Dispel Magic|dispel magic]]_
5th—_[[spells/Call Lightning Storm|call lightning storm]]_ (DC 21), control windsD (DC 20), _[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Wall Of Fire|wall of fire]]_ (DC 21)
4th—_[[spells/Air Walk|air walk]]_, _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Ice Storm|ice storm]]_ (DC 20), _[[spells/Scrying|scrying]]_ (DC 19)
3rd—_[[spells/Gaseous Form|gaseous form]]_, greater _[[spells/Magic Fang|magic fang]]_ (2), _[[spells/Protection from Energy|protection from energy]]_ (2), _[[spells/Sleet Storm|sleet storm]]_
2nd—_[[spells/Animal Messenger|animal messenger]]_, _[[spells/Barkskin|barkskin]]_ (3), _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Wind Wall|wind wall]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_ (2), _[[spells/Endure Elements|endure elements]]_, _[[spells/Faerie Fire|faerie fire]]_ (2), _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Speak with Animals|speak with animals]]_
0 (at will)—_[[spells/Flare|flare]]_ (DC 16), light, _[[spells/Mending|mending]]_, stabilize
**D **Domain spell; **Domain **Air

### Tactics

**Before Combat **The _druid_ casts _[[spells/Ironwood|ironwood]]_ on her _[[items/Armor/Breastplate|breastplate]]_ every 11 days, _[[spells/Liveoak|liveoak]]_ on an oak three times per month, and _endure elements_ every morning.
**During Combat **The _druid_ orders her _[[monsters/Treant|treant]]_ _[[items/Weapon Magic Abilities/Guardian|guardian]]_ into combat, wild shapes into a Large earth elemental, and uses _[[universal monster rules/Earth Glide|earth glide]]_ to flee underground where she casts beneficial spells on herself. Once prepared, she moves above ground and opens with _chain lightning_.

##### Statistics
**Str** 12, **Dex** 13, **Con** 15, **Int** 8, **Wis** 20, **Cha** 10
**Base Atk** +8; **CMB** +9; **CMD** 22
**Feats** _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Skill Focus|Skill Focus]]_ (Survival), _[[feats/Spell Focus|Spell Focus]]_ (evocation), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Fly +6, Handle Animal +6, _[[spells/Heal|Heal]]_ +9, Knowledge (nature) +9, Knowledge (planes) +3, Linguistics +2, Perception +14, Perform (dance) +2, Spellcraft +5, Survival +18
**Languages** Aquan, Auran, Common, Druidic, Elven, Ignan
**SQ** elf blood, nature bond (Air domain), nature sense, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, wild _[[feats/Empathy|empathy]]_ +11, woodland stride
**Combat Gear** potion of _[[spells/Haste|haste]]_, wand of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (6 charges); **Other Gear** +1 _ironwood_ _breastplate_, +1 darkwood _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, +1 _sickle_, masterwork shortspears (3), bag of holding (type I), _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 289 gp

These guardians of mountain peaks traffic with air and ice elementals, summoning forth the spirits of the mountain storms in order to protect their _[[items/Weapon Magic Abilities/Sacred|sacred]]_ places.
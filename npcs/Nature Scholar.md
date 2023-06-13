---
cssclass: [monsters]
title1: Nature Scholar
title2: Nature Scholar
CR: 12
sources:
- name: NPC Codex
  page: 225
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 19200
race: Elf
classes:
- druid 9
- loremaster 4
alignment: N
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 3
senses:
  low-light vision: true
AC:
  AC: 23
  touch: 15
  flat_footed: 20
  components:
    armor: 4
    deflection: 2
    dex: 3
    natural: 1
    shield: 3
HP:
  HP: 106
  long: 9d8+4d6+48
saves:
  fort: 12
  ref: 8
  will: 15
  other: +2 vs. enchantments, +4 vs. fey and plant-targeted effects
defensive_abilities:
- freedom of movement
immunities:
- poison
- sleep
resistances:
  fire: 10
speeds:
  base: 40
attacks:
  melee:
  - - text: +1 sickle +9/+4 (1d6)
      entries:
      - - damage: 1d6
      attack: +1 sickle
      bonus:
      - 9
      - 4
  special:
  - wild shape 3/day
spell_like_abilities:
  entries:
  - name: speak with animals
    source: default
    freq: At will
    other: 12 rounds/day
  sources:
  - name: default
    CL: 9
    concentration: 13
spells:
  entries:
  - is_domain_spell: true
    name: animal shapes
    source: Druid
    level: 7
  - name: heal
    source: Druid
    level: 7
  - is_domain_spell: true
    name: antilife shell
    source: Druid
    level: 6
  - name: stone tell
    source: Druid
    level: 6
  - name: transport via plants
    source: Druid
    level: 6
  - name: animal growth
    source: Druid
    level: 5
    DC: 19
  - is_domain_spell: true
    name: beast shape III
    source: Druid
    level: 5
    other: animals only
  - name: call lightning storm
    source: Druid
    level: 5
    DC: 19
  - name: insect plague
    source: Druid
    level: 5
  - name: cure serious wounds
    source: Druid
    level: 4
  - name: flame strike
    source: Druid
    level: 4
    DC: 18
  - name: freedom of movement
    source: Druid
    level: 4
  - name: rusting grasp
    source: Druid
    level: 4
  - name: scrying
    source: Druid
    level: 4
    DC: 18
  - is_domain_spell: true
    name: summon nature's ally IV
    source: Druid
    level: 4
    other: animals only
  - is_domain_spell: true
    name: dominate animal
    source: Druid
    level: 3
    DC: 17
  - name: meld into stone
    source: Druid
    level: 3
  - name: poison
    source: Druid
    level: 3
    DC: 17
  - name: protection from energy
    source: Druid
    level: 3
  - name: quench
    source: Druid
    level: 3
  - name: speak with plants
    source: Druid
    level: 3
  - name: animal messenger
    source: Druid
    level: 2
  - name: fog cloud
    source: Druid
    level: 2
  - name: heat metal
    source: Druid
    level: 2
    DC: 16
  - is_domain_spell: true
    name: hold animal
    source: Druid
    level: 2
    count: 2
    DC: 16
  - name: owl's wisdom
    source: Druid
    level: 2
  - is_domain_spell: true
    name: calm animals
    source: Druid
    level: 1
    DC: 15
  - name: detect animals or plants
    source: Druid
    level: 1
  - name: entangle
    source: Druid
    level: 1
    DC: 15
  - name: faerie fire
    source: Druid
    level: 1
  - name: hide from animals
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
    CL: 13
    concentration: 17
    slots:
      0: at-will
    domains:
    - animal
tactics:
  Before Combat: The loremaster drinks her potion of resist energy (fire) and casts
    freedom of movement.
  During Combat: The loremaster casts call lightning storm and flame strike.
  Base Statistics: Without resist energy and freedom of movement, the loremaster's
    statistics are Defensive Abilities none; Resist none.
ability_scores:
  STR: 8
  DEX: 16
  CON: 14
  INT: 15
  WIS: 18
  CHA: 10
BAB: 8
CMB: 7
CMD: 22
feats:
- name: Brew Potion
- name: Craft Wondrous Item
- name: Extend Spell
- name: Iron Will
- name: Skill Focus (Knowledge [nature])
- name: Skill Focus (Stealth)
- name: Toughness
- name: Weapon Focus (sickle)
skills:
  Acrobatics: 8
    when jumping: 12
  Climb: 7
  Fly: 11
  Handle Animal: 13
  Heal: 12
  Knowledge (arcana): 6
  Knowledge (history): 6
  Knowledge (local): 6
  Knowledge (dungeoneering): 4
  Knowledge (engineering): 4
  Knowledge (nobility): 4
  Knowledge (planes): 4
  Knowledge (religion): 4
  Knowledge (geography): 14
  Knowledge (nature): 25
  Perception: 19
  Sense Motive: 9
  Stealth: 11
  Survival: 14
  Swim: 7
languages:
- Auran
- Common
- Draconic
- Druidic
- Elven
- Sylvan
special_qualities:
- animal companion (effective druid level 6th)
- elven magic
- lore +2
- nature bond (Animal domain)
- nature sense
- secrets (lore of true stamina, secret health)
- trackless step
- weapon familiarity
- wild empathy +9
- woodland stride
gear:
  combat:
  - potion of cure moderate wounds
  - potion of neutralize poison
  - potion of remove disease
  - potions of resist energy (fire) (2)
  - potion of water breathing
  other:
  - +2 leather armor
  - +2 light wooden shield
  - +1 sickle
  - amulet of natural armor +1
  - belt of mighty constitution +2
  - boots of striding and springing
  - cloak of resistance +1
  - headband of inspired wisdom +2
  - ring of protection +2
  - 2,706 gp
desc_long: More aggressive than most other loremasters, nature scholars use terrain
  and the magic of the natural world to avoid enemies while calling down destruction.

---

# Nature Scholar

**Source** NPC Codex pg. 225
**XP** 19,200
Elf _[[classes/Druid|druid]]_ 9/loremaster 4

N Medium humanoid (elf)
**Init** +3; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +19

##### Defense

**AC** 23, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+4 armor, +2 _[[spells/Deflection|deflection]]_, +3 Dex, +1 natural, +3 _[[spells/Shield|shield]]_)
**hp** 106 (9d8+4d6+48)
**Fort** +12, **Ref** +8, **Will** +15; +2 vs. enchantments, +4 vs. fey and plant-targeted effects,
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_; **Immune** poison, sleep; **Resist** fire 10

##### Offense
**Speed** 40 ft.
**Melee** +1 _[[items/Weapon/Sickle|sickle]]_ +9/+4 (1d6)
**Special Attacks** wild shape 3/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +13)
At will—_[[spells/Speak with Animals|speak with animals]]_ (12 rounds/day)
**_Druid_ Spells Prepared **(CL 13th; concentration +17)
7th—_[[spells/Animal Shapes|animal shapes]]_, _[[spells/Heal|heal]]_
6th—_[[spells/Antilife Shell|antilife shell]]_, _[[spells/Stone Tell|stone tell]]_, _[[spells/Transport via Plants|transport via plants]]_
5th—_[[spells/Animal Growth|animal growth]]_ (DC 19), _[[spells/Beast Shape III|beast shape III]]_ (animals only), _[[spells/Call Lightning Storm|call lightning storm]]_ (DC 19), _[[spells/Insect Plague|insect plague]]_
4th—_[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Flame Strike|flame strike]]_ (DC 18), _freedom of movement_, _[[spells/Rusting Grasp|rusting grasp]]_, _[[spells/Scrying|scrying]]_ (DC 18), _[[universal monster rules/Summon|summon]]_ nature’s ally IV (animals only)
3rd—_[[spells/Dominate Animal|dominate animal]]_ (DC 17), _[[spells/Meld into Stone|meld into stone]]_, poison (DC 17), _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Quench|quench]]_, _[[spells/Speak with Plants|speak with plants]]_
2nd—_[[spells/Animal Messenger|animal messenger]]_, _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Heat Metal|heat metal]]_ (DC 16), _[[spells/Hold Animal|hold animal]]_ (2, DC 16), owl’s wisdom
1st—_[[spells/Calm Animals|calm animals]]_ (DC 15), _[[spells/Detect Animals or Plants|detect animals or plants]]_, _[[spells/Entangle|entangle]]_ (DC 15), _[[spells/Faerie Fire|faerie fire]]_, _[[spells/Hide from Animals|hide from animals]]_, _speak with animals_
0 (at will)—_[[spells/Detect Poison|detect poison]]_, _[[spells/Know Direction|know direction]]_, light, _[[spells/Purify Food and Drink|purify food and drink]]_
**D **Domain spell; **Domain **Animal

### Tactics

**Before Combat **The loremaster drinks her potion of _[[spells/Resist Energy|resist energy]]_ (fire) and casts _freedom of movement_.
**During Combat **The loremaster casts _call lightning storm_ and _flame strike_.
**Base Statistics **Without _resist energy_ and _freedom of movement_, the loremaster’s statistics are **Defensive Abilities **none; **Resist **none.

##### Statistics
**Str** 8, **Dex** 16, **Con** 14, **Int** 15, **Wis** 18, **Cha** 10
**Base Atk** +8; **CMB** +7; **CMD** 22
**Feats** _[[feats/Brew Potion|Brew Potion]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Skill Focus|Skill Focus]]_ (Knowledge [nature], Stealth), _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_sickle_)
**Skills** Acrobatics +8 (+12 when jumping), _[[universal monster rules/Climb|Climb]]_ +7, Fly +11, Handle Animal +13, _Heal_ +12, Knowledge (arcana, history, local) +6, Knowledge (dungeoneering, engineering, nobility, planes, religion) +4, Knowledge (geography) +14, Knowledge (nature) +25, Perception +19, Sense Motive +9, Stealth +11, Survival +14, Swim +7
**Languages** Auran, Common, Draconic, Druidic, Elven, Sylvan
**SQ** animal companion (effective _druid_ level 6th), elven magic, lore +2, nature bond (Animal domain), nature sense, secrets (lore of true stamina, secret health), _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, weapon familiarity, wild _[[feats/Empathy|empathy]]_ +9, woodland stride
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, potion of _[[spells/Neutralize Poison|neutralize poison]]_, potion of _[[spells/Remove Disease|remove disease]]_, potions of _resist energy_ (fire) (2), potion of _[[universal monster rules/Water Breathing|water breathing]]_; **Other Gear** +2 _[[items/Armor/Leather armor|leather armor]]_, +2 _[[items/Shield/Light wooden shield|light wooden shield]]_, +1 _sickle_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Mighty Constitution +2|belt of mighty constitution +2]]_, _[[items/Wondrous Item/Boots of Striding and Springing|boots of striding and springing]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, 2,706 gp

More aggressive than most other loremasters, nature scholars use terrain and the magic of the natural world to avoid enemies while calling down _[[spells/Destruction|destruction]]_.
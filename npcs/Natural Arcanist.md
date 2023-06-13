---
cssclass: [monsters]
title1: Natural Arcanist
title2: Natural Arcanist
CR: 15
sources:
- name: NPC Codex
  page: 173
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 51200
race: Halfling
classes:
- sorcerer 16
alignment: NE
size: Small
type: humanoid
subtypes:
- halfling
initiative:
  bonus: 3
AC:
  AC: 23
  touch: 18
  flat_footed: 19
  components:
    armor: 3
    deflection: 3
    dex: 3
    dodge: 1
    natural: 2
    size: 1
HP:
  HP: 137
  long: 16d6+79
saves:
  fort: 11
  ref: 12
  will: 16
  other: +2 vs. fear
defensive_abilities:
- spell turning
DR:
- amount: 10
  weakness: adamantine
  max_absorb: 150
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk spear +8/+3 (1d6-2/×3)
      entries:
      - - damage: 1d6-2
          crit_multiplier: 3
      attack: mwk spear
      bonus:
      - 8
      - 3
  ranged:
  - - text: mwk sling +13/+8 (1d3-2)
      entries:
      - - damage: 1d3-2
      attack: mwk sling
      bonus:
      - 13
      - 8
spells:
  entries:
  - name: prismatic wall
    source: Sorcerer
    level: 8
    DC: 25
  - name: grasping hand
    source: Sorcerer
    level: 7
  - name: greater teleport
    source: Sorcerer
    level: 7
  - name: spell turning
    source: Sorcerer
    level: 7
  - name: acid fog
    source: Sorcerer
    level: 6
  - name: chain lightning
    source: Sorcerer
    level: 6
    DC: 25
  - name: globe of invulnerability
    source: Sorcerer
    level: 6
  - name: greater dispel magic
    source: Sorcerer
    level: 6
  - name: true seeing
    source: Sorcerer
    level: 6
  - name: break enchantment
    source: Sorcerer
    level: 5
  - name: cone of cold
    source: Sorcerer
    level: 5
    DC: 24
  - name: mage's faithful hound
    source: Sorcerer
    level: 5
  - name: mind fog
    source: Sorcerer
    level: 5
    DC: 22
  - name: overland flight
    source: Sorcerer
    level: 5
  - name: dimension door
    source: Sorcerer
    level: 4
  - name: enervation
    source: Sorcerer
    level: 4
  - name: phantasmal killer
    source: Sorcerer
    level: 4
    DC: 21
  - name: resilient sphere
    source: Sorcerer
    level: 4
    DC: 23
  - name: stoneskin
    source: Sorcerer
    level: 4
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: displacement
    source: Sorcerer
    level: 3
  - name: fly
    source: Sorcerer
    level: 3
  - name: hold person
    source: Sorcerer
    level: 3
    DC: 20
  - name: lightning bolt
    source: Sorcerer
    level: 3
    DC: 22
  - name: protection from energy
    source: Sorcerer
    level: 3
    DC: 20
  - name: false life
    source: Sorcerer
    level: 2
  - name: glitterdust
    source: Sorcerer
    level: 2
    DC: 19
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: knock
    source: Sorcerer
    level: 2
  - name: resist energy
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: alarm
    source: Sorcerer
    level: 1
  - name: grease
    source: Sorcerer
    level: 1
  - name: identify
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: ray of enfeeblement
    source: Sorcerer
    level: 1
    DC: 18
  - name: shield
    source: Sorcerer
    level: 1
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: arcane mark
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: detect poison
    source: Sorcerer
    level: 0
  - name: light
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: ray of frost
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: resistance
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 16
    concentration: 23
    slots:
      8: 3
      7: 6
      6: 7
      5: 7
      4: 7
      3: 8
      2: 8
      1: 8
      0: at-will
    bloodline: arcane
tactics:
  Before Combat: The sorcerer casts false life, stoneskin, and spell turning.
  During Combat: The sorcerer casts prismatic wall between himself and his enemies
    on the first round of combat, then casts displacement and globe of invulnerability.
    He attacks with area damage spells such as acid fog, chain lightning, and cone
    of cold.
  Base Statistics: Without false life, spell turning, and stoneskin, the sorcerer's
    statistics are hp 122; Defensive Abilities none; DR none.
ability_scores:
  STR: 6
  DEX: 16
  CON: 14
  INT: 12
  WIS: 10
  CHA: 24
BAB: 8
CMB: 5
CMD: 22
feats:
- name: Combat Casting
- name: Dodge
- name: Empower Spell
- name: Eschew Materials
- name: Improved Counterspell
- name: Iron Will
- name: Maximize Spell
- name: Quicken Spell
- name: Silent Spell
- name: Still Spell
- name: Toughness
skills:
  Acrobatics: 5
    when jumping: 1
  Bluff: 18
  Climb: 0
  Fly: 9
  Knowledge (arcana): 12
  Knowledge (local): 9
  Perception: 12
  Spellcraft: 12
  Use Magic Device: 18
languages:
- Common
- Dwarven
- Halfling
special_qualities:
- arcane bond (ring of protection)
- bloodline arcana (+1 DC for metamagic spells that increase spell level)
- metamagic adept (4/day)
- new arcana
- school power (+2 DC for evocation spells)
gear:
  combat:
  - potion of cure serious wounds
  - scroll of mislead
  - scroll of shadow walk
  other:
  - masterwork sling with 20 bullets
  - masterwork spear
  - amulet of natural armor +2
  - bracers of armor +3
  - cloak of resistance +3
  - headband of alluring charisma +4
  - ring of protection +3
  - diamond dust (worth 500 gp)
  - eye ointment for true seeing (worth 500 gp)
  - 1,848 gp
desc_long: The natural arcanist is a conduit for magical power, always on the brink
  of releasing too much energy.

---

# Natural Arcanist

**Source** NPC Codex pg. 173
**XP** 51,200
Halfling _[[classes/Sorcerer|sorcerer]]_ 16

NE Small humanoid (halfling)
**Init** +3; **Senses** Perception +12

##### Defense

**AC** 23, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+3 armor, +3 deflection, +3 Dex, +1 _[[feats/Dodge|dodge]]_, +2 natural, +1 size)
**hp** 137 (16d6+79)
**Fort** +11, **Ref** +12, **Will** +16; +2 vs. _[[universal monster rules/Fear|fear]]_
**Defensive Abilities** _[[spells/Spell Turning|spell turning]]_; **DR** 10/adamantine (150 points)

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Spear|spear]]_ +8/+3 (1d6–2/×3)
**Ranged** mwk _[[items/Weapon/Sling|sling]]_ +13/+8 (1d3–2)
**_Sorcerer_ Spells Known **(CL 16th; concentration +23)
8th (3/day)—_[[spells/Prismatic Wall|prismatic wall]]_ (DC 25)
7th (6/day)—_[[spells/Grasping Hand|grasping hand]]_, greater teleport, _spell turning_
6th (7/day)—_[[spells/Acid Fog|acid fog]]_, _[[spells/Chain Lightning|chain lightning]]_ (DC 25), _[[spells/Globe Of Invulnerability|globe of invulnerability]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/True Seeing|true seeing]]_
5th (7/day)—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Cone of Cold|cone of cold]]_ (DC 24), mage’s faithful hound, _[[spells/Mind Fog|mind fog]]_ (DC 22), _[[spells/Overland Flight|overland flight]]_
4th (7/day)—_[[spells/Dimension Door|dimension door]]_, _[[spells/Enervation|enervation]]_, _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 21), _[[spells/Resilient Sphere|resilient sphere]]_ (DC 23), _[[spells/Stoneskin|stoneskin]]_
3rd (8/day)—_dispel magic_, _[[spells/Displacement|displacement]]_, fly, _[[spells/Hold Person|hold person]]_ (DC 20), _[[spells/Lightning Bolt|lightning bolt]]_ (DC 22), _[[spells/Protection from Energy|protection from energy]]_ (DC 20)
2nd (8/day)—_[[spells/False Life|false life]]_, _[[spells/Glitterdust|glitterdust]]_ (DC 19), _[[spells/Invisibility|invisibility]]_, _[[spells/Knock|knock]]_, _[[spells/Resist Energy|resist energy]]_, _[[spells/Scorching Ray|scorching ray]]_
1st (8/day)—_[[spells/Alarm|alarm]]_, _[[spells/Grease|grease]]_, _[[spells/Identify|identify]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 18), _[[spells/Shield|shield]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Arcane Mark|arcane mark]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_
**Bloodline **arcane

### Tactics

**Before Combat **The _sorcerer_ casts _false life_, _stoneskin_, and _spell turning_.
**During Combat **The _sorcerer_ casts _prismatic wall_ between himself and his enemies on the first round of combat, then casts _displacement_ and _globe of invulnerability_. He attacks with area damage spells such as _acid fog_, _chain lightning_, and _cone of cold_.
**Base Statistics **Without _false life_, _spell turning_, and _stoneskin_, the _sorcerer_’s statistics are **hp **122; **Defensive Abilities **none; **DR **none.

##### Statistics
**Str** 6, **Dex** 16, **Con** 14, **Int** 12, **Wis** 10, **Cha** 24
**Base Atk** +8; **CMB** +5; **CMD** 22
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Improved Counterspell|Improved Counterspell]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Maximize Spell|Maximize Spell]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Silent Spell|Silent Spell]]_, _[[feats/Still Spell|Still Spell]]_, _[[feats/Toughness|Toughness]]_
**Skills** Acrobatics +5 (+1 when jumping), Bluff +18, _[[universal monster rules/Climb|Climb]]_ +0, Fly +9, Knowledge (arcana) +12, Knowledge (local) +9, Perception +12, Spellcraft +12, Use Magic Device +18
**Languages** Common, Dwarven, Halfling
**SQ** arcane bond (ring of protection), bloodline arcana (+1 DC for metamagic spells that increase spell level), metamagic adept (4/day), new arcana, school power (+2 DC for evocation spells)
**Combat Gear** potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_, scroll of _[[spells/Mislead|mislead]]_, scroll of _[[spells/Shadow Walk|shadow walk]]_; **Other Gear** masterwork _sling_ with 20 bullets, masterwork _spear_, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Bracers of Armor +3|bracers of armor +3]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +4|headband of alluring charisma +4]]_, _[[items/Ring/Ring of Protection +3|ring of protection +3]]_, diamond dust (worth 500 gp), eye ointment for _true seeing_ (worth 500 gp), 1,848 gp

The _[[npcs/Natural Arcanist|natural arcanist]]_ is a conduit for magical power, always on the brink of releasing too much energy.
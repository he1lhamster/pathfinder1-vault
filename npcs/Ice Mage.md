---
cssclass: [monsters]
title1: Ice Mage
title2: Ice Mage
CR: 13
sources:
- name: NPC Codex
  page: 171
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 25600
race: Half-elf
classes:
- sorcerer 14
alignment: NE
size: Medium
type: humanoid
subtypes:
- elf
- human
initiative:
  bonus: 2
senses:
  low-light vision: true
AC:
  AC: 21
  touch: 15
  flat_footed: 18
  components:
    armor: 4
    deflection: 2
    dex: 2
    dodge: 1
    natural: 2
HP:
  HP: 79
  long: 14d6+28
saves:
  fort: 6
  ref: 6
  will: 12
  other: +2 vs. enchantments
immunities:
- fire (120 points)
- sleep
resistances:
  cold: 20
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk spear +7/+2 (1d8-1/×3)
      entries:
      - - damage: 1d8-1
          crit_multiplier: 3
      attack: mwk spear
      bonus:
      - 7
      - 2
  ranged:
  - - text: mwk light crossbow +10 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: mwk light crossbow
      bonus:
      - 10
spell_like_abilities:
  entries:
  - name: elemental ray
    source: default
    freq: 9/day
    other: 1d6+7 cold
  - name: elemental blast
    source: default
    freq: 1/day
    other: 14d6 cold
    DC: 23
  sources:
  - name: default
    CL: 14
    concentration: 20
spells:
  entries:
  - name: delayed blast fireball
    source: Sorcerer
    level: 7
    other: cold
    DC: 25
  - name: chain lightning
    source: Sorcerer
    level: 6
    other: cold
    DC: 24
  - name: elemental body III
    source: Sorcerer
    level: 6
  - name: freezing sphere
    source: Sorcerer
    level: 6
    DC: 24
  - name: baleful polymorph
    source: Sorcerer
    level: 5
    DC: 21
  - name: cone of cold
    source: Sorcerer
    level: 5
    DC: 23
  - name: elemental body II
    source: Sorcerer
    level: 5
  - name: summon monster V
    source: Sorcerer
    level: 5
  - name: elemental body I
    source: Sorcerer
    level: 4
  - name: ice storm
    source: Sorcerer
    level: 4
  - name: resilient sphere
    source: Sorcerer
    level: 4
    DC: 22
  - name: solid fog
    source: Sorcerer
    level: 4
  - name: wall of ice
    source: Sorcerer
    level: 4
    DC: 22
  - name: fly
    source: Sorcerer
    level: 3
  - name: lightning bolt
    source: Sorcerer
    level: 3
    other: cold
    DC: 21
  - name: protection from energy
    source: Sorcerer
    level: 3
  - name: ray of exhaustion
    source: Sorcerer
    level: 3
    DC: 19
  - name: sleet storm
    source: Sorcerer
    level: 3
  - name: acid arrow
    source: Sorcerer
    level: 2
    other: cold
  - name: blindness/deafness
    source: Sorcerer
    level: 2
    DC: 18
  - name: fog cloud
    source: Sorcerer
    level: 2
  - name: gust of wind
    source: Sorcerer
    level: 2
    DC: 20
  - name: mirror image
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
    other: cold
  - name: burning hands
    source: Sorcerer
    level: 1
    other: cold
    DC: 19
  - name: endure elements
    source: Sorcerer
    level: 1
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: obscuring mist
    source: Sorcerer
    level: 1
  - name: shield
    source: Sorcerer
    level: 1
  - name: acid splash
    source: Sorcerer
    level: 0
    other: cold
  - name: bleed
    source: Sorcerer
    level: 0
    DC: 16
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: detect poison
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
  - name: touch of fatigue
    source: Sorcerer
    level: 0
    DC: 16
  sources:
  - name: Sorcerer
    type: known
    CL: 14
    concentration: 20
    slots:
      7: 3
      6: 6
      5: 7
      4: 7
      3: 7
      2: 8
      1: 8
      0: at-will
    bloodline: elemental (water)
tactics:
  Before Combat: The sorcerer casts mage armor and protection from energy (fire).
  During Combat: The sorcerer casts empowered area damage spells such as cone of cold,
    freezing sphere, and chain lightning. If forced into melee, she casts elemental
    body III and transforms into a Large water elemental.
  Base Statistics: Without mage armor and protection from energy, the sorcerer's statistics
    are AC 17, touch 15, flat-footed 14; Immune sleep.
ability_scores:
  STR: 8
  DEX: 15
  CON: 14
  INT: 10
  WIS: 12
  CHA: 22
BAB: 7
CMB: 6
CMD: 21
feats:
- name: Combat Casting
- name: Dodge
- name: Empower Spell
- name: Eschew Materials
- name: Greater Spell Focus (evocation)
- name: Improved Initiative
- name: Iron Will
- name: Nimble Moves
- name: Silent Spell
- name: Skill Focus (Perception)
- name: Spell Focus (evocation)
skills:
  Diplomacy: 11
  Fly: 11
  Knowledge (arcana): 8
  Knowledge (planes): 8
  Linguistics: 1
  Perception: 19
  Spellcraft: 8
  Swim: 4
languages:
- Aquan
- Common
- Elven
special_qualities:
- bloodline arcana (change energy damage spells to cold)
- elf blood
gear:
  combat:
  - potion of fly
  other:
  - masterwork light crossbow with 10 bolts
  - masterwork spear
  - amulet of natural armor +2
  - headband of alluring charisma +4
  - ring of protection +2
  - 1,413 gp
desc_long: The ice mage bends liquid and solid water to her will, killing with the
  efficiency of a sudden frost.

---

# Ice Mage

**Source** NPC Codex pg. 171
**XP** 25,600
Half-elf _[[classes/Sorcerer|sorcerer]]_ 14

NE Medium humanoid (elf, human)
**Init** +2; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +19

##### Defense

**AC** 21, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+4 armor, +2 _[[spells/Deflection|deflection]]_, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +2 natural)
**hp** 79 (14d6+28)
**Fort** +6, **Ref** +6, **Will** +12; +2 vs. enchantments
**Immune** fire (120 points), sleep; **Resist** cold 20

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Spear|spear]]_ +7/+2 (1d8–1/×3)
**Ranged** mwk _[[items/Weapon/Light crossbow|light crossbow]]_ +10 (1d8/19–20)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +20)
9/day—elemental ray (1d6+7 cold)
1/day—elemental blast (14d6 cold, DC 23)
**_Sorcerer_ Spells Known **(CL 14th, concentration +20)
7th (3/day)—_[[spells/Delayed Blast Fireball|delayed blast fireball]]_ (cold, DC 25)
6th (6/day)—_[[spells/Chain Lightning|chain lightning]]_ (cold, DC 24), _[[spells/Elemental Body III|elemental body III]]_, _[[spells/Freezing Sphere|freezing sphere]]_ (DC 24)
5th (7/day)—_[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 21), _[[spells/Cone of Cold|cone of cold]]_ (DC 23), _[[spells/Elemental Body II|elemental body II]]_, _[[spells/Summon Monster V|summon monster V]]_
4th (7/day)—_[[spells/Elemental Body I|elemental body I]]_, _[[spells/Ice Storm|ice storm]]_, _[[spells/Resilient Sphere|resilient sphere]]_ (DC 22), _[[spells/Solid Fog|solid fog]]_, _[[spells/Wall Of Ice|wall of ice]]_ (DC 22)
3rd (7/day)—fly, _[[spells/Lightning Bolt|lightning bolt]]_ (cold, DC 21), _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Ray of Exhaustion|ray of exhaustion]]_ (DC 19), _[[spells/Sleet Storm|sleet storm]]_
2nd (8/day)—_[[spells/Acid Arrow|acid arrow]]_ (cold), blindness/deafness (DC 18), _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Gust Of Wind|gust of wind]]_ (DC 20), _[[spells/Mirror Image|mirror image]]_, _[[spells/Scorching Ray|scorching ray]]_ (cold)
1st (8/day)—_[[spells/Burning Hands|burning hands]]_ (cold, DC 19), _[[spells/Endure Elements|endure elements]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shield|shield]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_ (cold), _[[universal monster rules/Bleed|bleed]]_ (DC 16), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 16)
**Bloodline **elemental (water)

### Tactics

**Before Combat **The _sorcerer_ casts _mage armor_ and _protection from energy_ (fire).
**During Combat **The _sorcerer_ casts empowered area damage spells such as _cone of cold_, _freezing sphere_, and _chain lightning_. If forced into melee, she casts _elemental body III_ and transforms into a Large water elemental.
**Base Statistics **Without _mage armor_ and _protection from energy_, the _sorcerer_’s statistics are **AC **17, touch 15, _flat-footed_ 14; **Immune **sleep.

##### Statistics
**Str** 8, **Dex** 15, **Con** 14, **Int** 10, **Wis** 12, **Cha** 22
**Base Atk** +7; **CMB** +6; **CMD** 21
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (evocation), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Nimble Moves|Nimble Moves]]_, _[[feats/Silent Spell|Silent Spell]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Spell Focus|Spell Focus]]_ (evocation)
**Skills** Diplomacy +11, Fly +11, Knowledge (arcana, planes) +8, Linguistics +1, Perception +19, Spellcraft +8, Swim +4
**Languages** Aquan, Common, Elven
**SQ** bloodline arcana (change energy damage spells to cold), elf blood
**Combat Gear** potion of fly; **Other Gear** masterwork _light crossbow_ with 10 bolts, masterwork _spear_, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +4|headband of alluring charisma +4]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, 1,413 gp

The _[[npcs/Ice Mage|ice mage]]_ bends liquid and solid water to her will, killing with the efficiency of a sudden frost.
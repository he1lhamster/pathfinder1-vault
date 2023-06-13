---
cssclass: [monsters]
title1: Fate-Bound Mage
title2: Fate-Bound Mage
CR: 18
sources:
- name: NPC Codex
  page: 176
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 153600
race: Human
classes:
- sorcerer 19
alignment: N
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 5
AC:
  AC: 24
  touch: 17
  flat_footed: 22
  other: never surprised or flat-footed
  components:
    armor: 4
    deflection: 3
    dex: 1
    dodge: 1
    insight: 2
    natural: 3
HP:
  HP: 122
  long: 19d6+53
saves:
  fort: 10
  ref: 14
  will: 18
  other: +5 vs. spells and spell-like abilities
defensive_abilities:
- fated +5
- spell turning
- within reach 1/day
DR:
- amount: 10
  weakness: adamantine
  max_absorb: 150
speeds:
  base: 30
attacks:
  melee:
  - - text: staff of fire +8/+3 (1d6-1)
      entries:
      - - damage: 1d6-1
      attack: staff of fire
      bonus:
      - 8
      - 3
  special:
  - it was meant to be (2/day)
spell_like_abilities:
  entries:
  - name: touch of destiny
    source: default
    freq: 10/day
    other: '+9'
  sources:
  - name: default
    CL: 19
    concentration: 26
spells:
  entries:
  - name: crushing hand
    source: Sorcerer
    level: 9
  - name: foresight
    source: Sorcerer
    level: 9
  - name: time stop
    source: Sorcerer
    level: 9
  - name: greater shout
    source: Sorcerer
    level: 8
    DC: 27
  - name: moment of prescience
    source: Sorcerer
    level: 8
  - name: power word stun
    source: Sorcerer
    level: 8
  - name: protection from spells
    source: Sorcerer
    level: 8
  - name: limited wish
    source: Sorcerer
    level: 7
  - name: mage's magnificent mansion
    source: Sorcerer
    level: 7
  - name: mage's sword
    source: Sorcerer
    level: 7
  - name: spell turning
    source: Sorcerer
    level: 7
  - name: chain lightning
    source: Sorcerer
    level: 6
    DC: 25
  - name: disintegrate
    source: Sorcerer
    level: 6
    DC: 23
  - name: globe of invulnerability
    source: Sorcerer
    level: 6
  - name: mislead
    source: Sorcerer
    level: 6
  - name: baleful polymorph
    source: Sorcerer
    level: 5
    DC: 22
  - name: break enchantment
    source: Sorcerer
    level: 5
  - name: cone of cold
    source: Sorcerer
    level: 5
    DC: 24
  - name: dominate person
    source: Sorcerer
    level: 5
    DC: 22
  - name: teleport
    source: Sorcerer
    level: 5
  - name: bestow curse
    source: Sorcerer
    level: 4
    DC: 21
  - name: charm monster
    source: Sorcerer
    level: 4
    DC: 21
  - name: dimension door
    source: Sorcerer
    level: 4
  - name: freedom of movement
    source: Sorcerer
    level: 4
  - name: stoneskin
    source: Sorcerer
    level: 4
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: fly
    source: Sorcerer
    level: 3
  - name: lightning bolt
    source: Sorcerer
    level: 3
    DC: 22
  - name: phantom steed
    source: Sorcerer
    level: 3
  - name: protection from energy
    source: Sorcerer
    level: 3
  - name: acid arrow
    source: Sorcerer
    level: 2
  - name: blur
    source: Sorcerer
    level: 2
  - name: false life
    source: Sorcerer
    level: 2
  - name: fog cloud
    source: Sorcerer
    level: 2
  - name: knock
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: alarm
    source: Sorcerer
    level: 1
  - name: burning hands
    source: Sorcerer
    level: 1
    DC: 20
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: shield
    source: Sorcerer
    level: 1
  - name: true strike
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
  - name: mending
    source: Sorcerer
    level: 0
  - name: open/close
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 19
    concentration: 26
    slots:
      9: 4
      8: 6
      7: 7
      6: 7
      5: 7
      4: 7
      3: 8
      2: 8
      1: 8
      0: at-will
    bloodline: destined
tactics:
  Before Combat: The sorcerer casts false life, foresight, freedom of movement, mage
    armor, moment of prescience, protection from spells, spell turning, and stoneskin.
  During Combat: The sorcerer first casts mislead and globe of invulnerability.
  Base Statistics: Without false life, foresight, mage armor, protection from spells,
    spell turning, and stoneskin, the sorcerer's statistics are AC 18, touch 15, flat-footed
    16; hp 107; Ref +12; DR none.
ability_scores:
  STR: 8
  DEX: 13
  CON: 12
  INT: 14
  WIS: 15
  CHA: 24
BAB: 9
CMB: 8
CMD: 25
feats:
- name: Combat Casting
- name: Combat Expertise
- name: Diehard
- name: Dodge
- name: Eschew Materials
- name: Greater Spell Focus (evocation)
- name: Improved Initiative
- name: Improved Lightning Reflexes
- name: Iron Will
- name: Lightning Reflexes
- name: Maximize Spell
- name: Mobility
- name: Quicken Spell
- name: Silent Spell
- name: Spell Focus (evocation)
skills:
  Bluff: 20
  Diplomacy: 17
  Fly: 11
  Intimidate: 20
  Knowledge (arcana): 15
  Knowledge (history): 15
  Perception: 21
  Spellcraft: 24
languages:
- Celestial
- Common
- Draconic
- Elven
- Infernal
special_qualities:
- bloodline arcana (gain luck bonus to saves when casting personal-range spells)
gear:
  combat:
  - potion of cure moderate wounds
  - potion of cure serious wounds
  other:
  - amulet of natural armor +3
  - cloak of resistance +3
  - glove of storing
  - headband of mental prowess +4 (Int, Wis)
  - ring of protection +3
  - staff of fire (10 charges)
  - diamond dust (worth 500 gp)
  - 7,800 gp
desc_long: Believing he's destined for greatness, this mage will do anything to succeed.

---

# Fate-Bound Mage

**Source** NPC Codex pg. 176
**XP** 153,600
Human _[[classes/Sorcerer|sorcerer]]_ 19

N Medium humanoid (human)
**Init** +5; **Senses** Perception +21

##### Defense

**AC** 24, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+4 armor, +3 _[[spells/Deflection|deflection]]_, +1 Dex, +1 _[[feats/Dodge|dodge]]_, +2 insight, +3 natural); never surprised or _flat-footed_
**hp** 122 (19d6+53)
**Fort** +10, **Ref** +14, **Will** +18; +5 vs. spells and _[[universal monster rules/Spell-Like Abilities|spell-like abilities]]_
**Defensive Abilities** fated +5, _[[spells/Spell Turning|spell turning]]_, within reach 1/day; **DR** 10/adamantine (150 points)

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Staff/Staff of Fire|staff of fire]]_ +8/+3 (1d6–1)
**Special Attacks** it was meant to be (2/day)
**_Spell-Like Abilities_** (CL 19th; concentration +26)
10/day—touch of destiny (+9)
**_Sorcerer_ Spells Known **(CL 19th; concentration +26)
9th (4/day)—_[[spells/Crushing Hand|crushing hand]]_, _[[spells/Foresight|foresight]]_, _[[spells/Time Stop|time stop]]_
8th (6/day)—greater _[[spells/Shout|shout]]_ (DC 27), _[[spells/Moment of Prescience|moment of prescience]]_, _[[spells/Power Word Stun|power word stun]]_, _[[spells/Protection from Spells|protection from spells]]_
7th (7/day)—_[[spells/Limited Wish|limited wish]]_, mage’s magnificent mansion, mage’s sword, _spell turning_
6th (7/day)—_[[spells/Chain Lightning|chain lightning]]_ (DC 25), _[[spells/Disintegrate|disintegrate]]_ (DC 23), _[[spells/Globe Of Invulnerability|globe of invulnerability]]_, _[[spells/Mislead|mislead]]_
5th (7/day)—_[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 22), _[[spells/Break Enchantment|break enchantment]]_, _[[spells/Cone of Cold|cone of cold]]_ (DC 24), _[[spells/Dominate Person|dominate person]]_ (DC 22), teleport
4th (7/day)—_[[spells/Bestow Curse|bestow curse]]_ (DC 21), _[[spells/Charm Monster|charm monster]]_ (DC 21), _[[spells/Dimension Door|dimension door]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Stoneskin|stoneskin]]_
3rd (8/day)—_[[spells/Dispel Magic|dispel magic]]_, fly, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 22), _[[spells/Phantom Steed|phantom steed]]_, _[[spells/Protection from Energy|protection from energy]]_
2nd (8/day)—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Blur|blur]]_, _[[spells/False Life|false life]]_, _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Knock|knock]]_, _[[spells/Scorching Ray|scorching ray]]_
1st (8/day)—_[[spells/Alarm|alarm]]_, _[[spells/Burning Hands|burning hands]]_ (DC 20), _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Arcane Mark|arcane mark]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, light, _[[spells/Mending|mending]]_, open/close, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Read Magic|read magic]]_
**Bloodline **destined

### Tactics

**Before Combat **The _sorcerer_ casts _false life_, _foresight_, _freedom of movement_, _mage armor_, _moment of prescience_, _protection from spells_, _spell turning_, and _stoneskin_.
**During Combat **The _sorcerer_ first casts _mislead_ and _globe of invulnerability_.
**Base Statistics **Without _false life_, _foresight_, _mage armor_, _protection from spells_, _spell turning_, and _stoneskin_, the _sorcerer_’s statistics are **AC **18, touch 15, _flat-footed_ 16; **hp **107; **Ref **+12; **DR **none.

##### Statistics
**Str** 8, **Dex** 13, **Con** 12, **Int** 14, **Wis** 15, **Cha** 24
**Base Atk** +9; **CMB** +8; **CMD** 25
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Diehard|Diehard]]_, _Dodge_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (evocation), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Lightning Reflexes|Improved Lightning Reflexes]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Maximize Spell|Maximize Spell]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Silent Spell|Silent Spell]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation)
**Skills** Bluff +20, Diplomacy +17, Fly +11, Intimidate +20, Knowledge (arcana, history) +15, Perception +21, Spellcraft +24
**Languages** Celestial, Common, Draconic, Elven, Infernal
**SQ** bloodline arcana (gain luck bonus to saves when casting personal-range spells)
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_; **Other Gear** _[[items/Wondrous Item/Amulet of Natural Armor +3|amulet of natural armor +3]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Glove of Storing|glove of storing]]_, _[[items/Wondrous Item/Headband of Mental Prowess +4|headband of mental prowess +4]]_ (Int, Wis), _[[items/Ring/Ring of Protection +3|ring of protection +3]]_, _staff of fire_ (10 charges), diamond dust (worth 500 gp), 7,800 gp

Believing he’s destined for greatness, this mage will do anything to succeed.
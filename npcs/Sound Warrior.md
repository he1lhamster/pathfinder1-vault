---
cssclass: [monsters]
title1: Sound Warrior
title2: Sound Warrior
CR: 12
sources:
- name: NPC Codex
  page: 229
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 19200
race: Halfling
classes:
- bard 5
- druid 4
- mystic theurge 4
alignment: N
size: Small
type: humanoid
subtypes:
- halfling
initiative:
  bonus: 3
AC:
  AC: 24
  touch: 17
  flat_footed: 20
  components:
    armor: 4
    deflection: 2
    dex: 3
    dodge: 1
    natural: 3
    size: 1
HP:
  HP: 76
  long: 5d8+4d8+4d6+18
saves:
  fort: 10
  ref: 11
  will: 14
  other: +2 vs. fear, +4 vs. fey and plant-targeted effects, +4 vs. bardic performance,
    language-dependent, and sonic
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk dagger +10/+5 (1d3/19-20)
      entries:
      - - damage: 1d3
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 10
      - 5
  ranged:
  - - text: mwk dagger +13/+8 (1d3/19-20)
      entries:
      - - damage: 1d3
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 13
      - 8
  special:
  - bardic performance 17 rounds/day (countersong, distraction, fascinate, inspire
    competence +2, inspire courage +2)
  - wild shape 2/day
spell_like_abilities:
  entries:
  - name: lightning arc
    source: default
    freq: 5/day
    other: 1d6+2 electricity
  sources:
  - name: default
    CL: 4
    concentration: 6
spells:
  entries:
  - name: charm monster
    source: Bard
    level: 3
    DC: 20
  - name: displacement
    source: Bard
    level: 3
  - name: haste
    source: Bard
    level: 3
  - name: sculpt sound
    source: Bard
    level: 3
  - name: hold person
    source: Bard
    level: 2
    DC: 19
  - name: scare
    source: Bard
    level: 2
    DC: 17
  - name: shatter
    source: Bard
    level: 2
  - name: sound burst
    source: Bard
    level: 2
    DC: 17
  - name: alarm
    source: Bard
    level: 1
  - name: cause fear
    source: Bard
    level: 1
    DC: 16
  - name: charm person
    source: Bard
    level: 1
    DC: 18
  - name: remove fear
    source: Bard
    level: 1
  - name: ventriloquism
    source: Bard
    level: 1
    DC: 16
  - name: ghost sound
    source: Bard
    level: 0
    DC: 15
  - name: know direction
    source: Bard
    level: 0
  - name: light
    source: Bard
    level: 0
  - name: mage hand
    source: Bard
    level: 0
  - name: message
    source: Bard
    level: 0
  - name: resistance
    source: Bard
    level: 0
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
  - name: call lightning
    source: Druid
    level: 3
    DC: 15
  - name: cure moderate wounds
    source: Druid
    level: 3
  - is_domain_spell: true
    name: gaseous form
    source: Druid
    level: 3
  - name: neutralize poison
    source: Druid
    level: 3
  - name: barkskin
    source: Druid
    level: 2
  - name: cat's grace
    source: Druid
    level: 2
  - name: delay poison
    source: Druid
    level: 2
  - name: lesser restoration
    source: Druid
    level: 2
  - is_domain_spell: true
    name: wind wall
    source: Druid
    level: 2
  - name: cure light wounds
    source: Druid
    level: 1
  - name: faerie fire
    source: Druid
    level: 1
  - name: goodberry
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
  - name: create water
    source: Druid
    level: 0
  - name: detect poison
    source: Druid
    level: 0
  - name: mending
    source: Druid
    level: 0
  - name: stabilize
    source: Druid
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 9
    concentration: 14
    slots:
      3: 4
      2: 5
      1: 7
      0: at-will
  - name: Druid
    type: prepared
    CL: 8
    concentration: 10
    slots:
      0: at-will
    domains:
    - air
tactics:
  Before Combat: The mystic theurge casts barkskin, freedom of movement, and pass
    without trace.
  During Combat: While aiding her companions with bardic performance, the mystic theurge
    harasses her opponents with call lightning, charm monster, and wind wall.
  Base Statistics: Without barkskin, the mystic theurge's statistics are AC 21, touch
    17, flat-footed 17.
ability_scores:
  STR: 10
  DEX: 16
  CON: 10
  INT: 10
  WIS: 15
  CHA: 20
BAB: 8
CMB: 7
CMD: 23
feats:
- name: Combat Casting
- name: Dodge
- name: Great Fortitude
- name: Greater Spell Focus (enchantment)
- name: Natural Spell
- name: Spell Focus (enchantment)
- name: Toughness
skills:
  Acrobatics: 5
    when jumping: 1
  Climb: 6
  Diplomacy: 9
  Fly: 9
  Heal: 6
  Knowledge (arcana): 8
  Knowledge (religion): 8
  Knowledge (geography): 9
  Knowledge (local): 9
  Knowledge (history): 10
  Knowledge (nature): 12
  Perception: 17
  Perform (oratory): 9
  Perform (sing): 9
  Sense Motive: 9
  Stealth: 20
  Survival: 12
languages:
- Common
- Druidic
- Halfling
special_qualities:
- bardic knowledge +2
- combined spells (2nd)
- lore master 1/day
- nature bond (Air domain)
- nature sense
- trackless step
- versatile performance (oratory)
- wild empathy +9
- woodland stride
gear:
  combat:
  - potion of cure serious wounds
  - smokesticks (5)
  - thunderstones (5)
  other:
  - +2 leather armor
  - masterwork daggers (2)
  - belt of mighty constitution +2
  - cloak of resistance +1
  - druid's vestment
  - headband of alluring charisma +2
  - ring of protection +2
  - 486 gp
desc_long: Using a mix of rousing oratory, song, and thunderous spells, a sound warrior
  is often heard before she's seen.

---

# Sound Warrior

**Source** NPC Codex pg. 229
**XP** 19,200
Halfling _[[classes/Bard|bard]]_ 5/druid 4/mystic theurge 4

N Small humanoid (halfling)
**Init** +3; **Senses** Perception +17

##### Defense

**AC** 24, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+4 armor, +2 deflection, +3 Dex, +1 _[[feats/Dodge|dodge]]_, +3 natural, +1 size)
**hp** 76 (5d8+4d8+4d6+18)
**Fort** +10, **Ref** +11, **Will** +14; +2 vs. _[[universal monster rules/Fear|fear]]_, +4 vs. fey and plant-targeted effects, +4 vs. bardic performance, language-dependent, and sonic

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Dagger|dagger]]_ +10/+5 (1d3/19–20)
**Ranged** mwk _dagger_ +13/+8 (1d3/19–20)
**Special Attacks** bardic performance 17 rounds/day (countersong, _[[universal monster rules/Distraction|distraction]]_, fascinate, inspire competence +2, inspire courage +2), wild shape 2/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +6)
5/day—_[[spells/Lightning Arc|lightning arc]]_ (1d6+2 electricity)
**_Bard_ Spells Known **(CL 9th; concentration +14)
3rd (4/day)—_[[spells/Charm Monster|charm monster]]_ (DC 20), _[[spells/Displacement|displacement]]_, _[[spells/Haste|haste]]_, _[[spells/Sculpt Sound|sculpt sound]]_
2nd (5/day)—_[[spells/Hold Person|hold person]]_ (DC 19), _[[spells/Scare|scare]]_ (DC 17), _[[spells/Shatter|shatter]]_, _[[spells/Sound Burst|sound burst]]_ (DC 17)
1st (7/day)—_[[spells/Alarm|alarm]]_, _[[spells/Cause Fear|cause fear]]_ (DC 16), _[[spells/Charm Person|charm person]]_ (DC 18), _[[spells/Remove Fear|remove fear]]_, _[[spells/Ventriloquism|ventriloquism]]_ (DC 16)
0 (at will)—_[[spells/Ghost Sound|ghost sound]]_ (DC 15), _[[spells/Know Direction|know direction]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[universal monster rules/Resistance|resistance]]_
**_[[classes/Druid|Druid]]_ Spells Prepared **(CL 8th; concentration +10)
4th—_[[spells/Air Walk|air walk]]_, _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Freedom of Movement|freedom of movement]]_
3rd—_[[spells/Call Lightning|call lightning]]_ (DC 15), _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Gaseous Form|gaseous form]]_, _[[spells/Neutralize Poison|neutralize poison]]_
2nd—_[[spells/Barkskin|barkskin]]_, cat’s _[[spells/Grace|grace]]_, _[[spells/Delay Poison|delay poison]]_, lesser _[[spells/Restoration|restoration]]_, _[[spells/Wind Wall|wind wall]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Faerie Fire|faerie fire]]_, _[[spells/Goodberry|goodberry]]_, _[[spells/Longstrider|longstrider]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Pass without Trace|pass without trace]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Mending|mending]]_, stabilize
**D **Domain spell; **Domains **Air

### Tactics

**Before Combat **The mystic theurge casts _barkskin_, _freedom of movement_, and _pass without trace_.
**During Combat **While aiding her companions with bardic performance, the mystic theurge harasses her opponents with _call lightning_, _charm monster_, and _wind wall_.
**Base Statistics **Without _barkskin_, the mystic theurge’s statistics are **AC **21, touch 17, _flat-footed_ 17.

##### Statistics
**Str** 10, **Dex** 16, **Con** 10, **Int** 10, **Wis** 15, **Cha** 20
**Base Atk** +8; **CMB** +7; **CMD** 23
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (enchantment), _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Spell Focus|Spell Focus]]_ (enchantment), _[[feats/Toughness|Toughness]]_
**Skills** Acrobatics +5 (+1 when jumping), _[[universal monster rules/Climb|Climb]]_ +6, Diplomacy +9, Fly +9, _[[spells/Heal|Heal]]_ +6, Knowledge (arcana, religion) +8, Knowledge (geography, local) +9, Knowledge (history) +10, Knowledge (nature) +12, Perception +17, Perform (oratory, sing) +9, Sense Motive +9, Stealth +20, Survival +12
**Languages** Common, Druidic, Halfling
**SQ** bardic knowledge +2, combined spells (2nd), lore master 1/day, nature bond (Air domain), nature sense, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, versatile performance (oratory), wild _[[feats/Empathy|empathy]]_ +9, woodland stride
**Combat Gear** potion of _cure serious wounds_, smokesticks (5), thunderstones (5); **Other Gear** +2 _[[items/Armor/Leather armor|leather armor]]_, masterwork daggers (2), _[[items/Wondrous Item/Belt of Mighty Constitution +2|belt of mighty constitution +2]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, _druid_’s vestment, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, 486 gp

Using a mix of rousing oratory, song, and thunderous spells, a _[[npcs/Sound Warrior|sound warrior]]_ is often heard before she’s seen.
---
cssclass: [monsters]
title1: Mithral Wizard
title2: Mithral Wizard
CR: 19
sources:
- name: NPC Codex
  page: 221
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 204800
race: Human
classes:
- fighter 2
- evoker 8
- eldritch knight 10
alignment: NE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 5
AC:
  AC: 34
  touch: 15
  flat_footed: 33
  components:
    armor: 14
    deflection: 4
    dex: 1
    natural: 5
HP:
  HP: 198
  long: 2d10+8d6+10d10+100
saves:
  fort: 18
  ref: 9
  will: 14
  other: +1 vs. fear
defensive_abilities:
- bravery +1
- 50% chance to negate critical hit or sneak attack
DR:
- amount: 10
  weakness: adamantine
  max_absorb: 150
speeds:
  base: 20
attacks:
  melee:
  - - text: +3 longsword +24/+19/+14/+9 (1d8+8/17-20)
      entries:
      - - damage: 1d8+8
          crit_range: 17-20
      attack: +3 longsword
      bonus:
      - 24
      - 19
      - 14
      - 9
  special:
  - intense spells (+4 damage)
  - spell critical
spell_like_abilities:
  entries:
  - name: elemental wall
    source: default
    freq: At will
    other: 8 rounds/day
  - name: force missile
    source: default
    freq: 11/day
    other: 1d4+4
  sources:
  - name: default
    CL: 17
    concentration: 25
spells:
  entries:
  - name: meteor swarm
    source: Evoker
    level: 9
  - name: time stop
    source: Evoker
    level: 9
  - name: mass charm monster
    source: Evoker
    level: 8
    DC: 26
  - name: mind blank
    source: Evoker
    level: 8
  - name: quickened phantasmal killer
    source: Evoker
    level: 8
  - name: polar ray
    source: Evoker
    level: 8
  - name: banishment
    source: Evoker
    level: 7
    DC: 25
  - name: quickened fireball
    source: Evoker
    level: 7
    count: 2
  - name: mass hold person
    source: Evoker
    level: 7
    DC: 25
  - name: reverse gravity
    source: Evoker
    level: 7
  - name: chain lightning
    source: Evoker
    level: 6
    DC: 24
  - name: disintegrate
    source: Evoker
    level: 6
    DC: 24
  - name: quickened glitterdust
    source: Evoker
    level: 6
  - name: greater dispel magic
    source: Evoker
    level: 6
  - name: stilled teleport
    source: Evoker
    level: 6
  - name: wall of iron
    source: Evoker
    level: 6
  - name: cloudkill
    source: Evoker
    level: 5
    DC: 23
  - name: stilled dimension door
    source: Evoker
    level: 5
  - name: interposing hand
    source: Evoker
    level: 5
  - name: teleport
    source: Evoker
    level: 5
  - name: wall of force
    source: Evoker
    level: 5
    count: 2
  - name: beast shape II
    source: Evoker
    level: 4
  - name: confusion
    source: Evoker
    level: 4
    DC: 22
  - name: dimension door
    source: Evoker
    level: 4
  - name: fire shield
    source: Evoker
    level: 4
  - name: stilled fireball
    source: Evoker
    level: 4
  - name: stoneskin
    source: Evoker
    level: 4
  - name: wall of ice
    source: Evoker
    level: 4
    DC: 22
  - name: dispel magic
    source: Evoker
    level: 3
    count: 2
  - name: fireball
    source: Evoker
    level: 3
    count: 2
    DC: 21
  - name: fly
    source: Evoker
    level: 3
  - name: lightning bolt
    source: Evoker
    level: 3
    count: 2
    DC: 21
  - name: acid arrow
    source: Evoker
    level: 2
    count: 2
  - name: darkvision
    source: Evoker
    level: 2
  - name: invisibility
    source: Evoker
    level: 2
  - name: mirror image
    source: Evoker
    level: 2
  - name: scorching ray
    source: Evoker
    level: 2
  - name: web
    source: Evoker
    level: 2
    DC: 20
  - name: feather fall
    source: Evoker
    level: 1
  - name: magic missile
    source: Evoker
    level: 1
    count: 4
  - name: mount
    source: Evoker
    level: 1
  - name: shield
    source: Evoker
    level: 1
  - name: detect magic
    source: Evoker
    level: 0
  - name: light
    source: Evoker
    level: 0
  - name: mage hand
    source: Evoker
    level: 0
  - name: message
    source: Evoker
    level: 0
  sources:
  - name: Evoker
    type: prepared
    CL: 17
    concentration: 25
    failure_chance: 25%
    slots:
      0: at-will
    opposition_schools:
    - divination
    - necromancy
tactics:
  Before Combat: The eldritch knight casts stoneskin.
  During Combat: The knight casts time stop, then shield, expeditious retreat, fly,
    and mirror image.
  Base Statistics: Without stoneskin, the knight's statistics are DR none.
ability_scores:
  STR: 16
  DEX: 13
  CON: 20
  INT: 26
  WIS: 10
  CHA: 8
BAB: 16
CMB: 19
CMD: 34
feats:
- name: Arcane Armor Mastery
- name: Arcane Armor Training
- name: Craft Magic Arms and Armor
- name: Craft Wand
- name: Craft Wondrous Item
- name: Disruptive
- name: Greater Weapon Focus (longsword)
- name: Improved Critical (longsword)
- name: Improved Initiative
- name: Iron Will
- name: Power Attack
- name: Quicken Spell
- name: Scribe Scroll
- name: Spell Penetration
- name: Still Spell
- name: Vital Strike
- name: Weapon Focus (longsword)
- name: Weapon Specialization (longsword)
skills:
  Bluff: 19
  Fly: 22
  Intimidate: 22
  Knowledge (arcana): 31
  Knowledge (planes): 31
  Knowledge (dungeoneering): 21
  Knowledge (engineering): 21
  Knowledge (geography): 21
  Knowledge (history): 21
  Knowledge (local): 21
  Knowledge (nobility): 21
  Perception: 20
  Ride: 17
  Spellcraft: 31
languages:
- Abyssal
- Common
- Draconic
- Dwarven
- Elven
- Giant
- Goblin
- Ignan
- Infernal
special_qualities:
- arcane bond (+2 longsword)
- diverse training
gear:
  combat:
  - wand of greater invisibility (15 charges)
  - wand of see invisibility (10 charges)
  other:
  - +5 moderate fortification mithral full plate
  - +3 longsword
  - amulet of natural armor +5
  - belt of physical might +4 (Str, Con)
  - cloak of resistance +3
  - headband of vast intelligence +6
  - ring of protection +4
  - granite and diamond dust (worth 500 gp)
  - iron sheet and gold dust (worth 50 gp)
  - 3,585 gp
desc_long: Clad in full plate, these eldritch knights mix an impenetrable defense
  with a relentless spell offense.

---

# Mithral Wizard

**Source** NPC Codex pg. 221
**XP** 204,800
Human _[[classes/Fighter|fighter]]_ 2/evoker 8/eldritch _[[npcs/Knight|knight]]_ 10

NE Medium humanoid (human)
**Init** +5; **Senses** Perception +20

##### Defense

**AC** 34, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 33 (+14 armor, +4 _[[spells/Deflection|deflection]]_, +1 Dex, +5 natural)
**hp** 198 (2d10+8d6+10d10+100)
**Fort** +18, **Ref** +9, **Will** +14; +1 vs. _[[universal monster rules/Fear|fear]]_
**Defensive Abilities** bravery +1, 50% chance to negate critical hit or sneak attack; **DR** 10/adamantine (150 points)

##### Offense
**Speed** 20 ft.
**Melee** +3 _[[items/Weapon/Longsword|longsword]]_ +24/+19/+14/+9 (1d8+8/17–20)
**Special Attacks** intense spells (+4 damage), spell critical
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +25)
At will—elemental wall (8 rounds/day)
11/day—force missile (1d4+4)
**Evoker Spells Prepared **(CL 17th; concentration +25, arcane spell failure 25%)
9th—_[[spells/Meteor Swarm|meteor swarm]]_, _[[spells/Time Stop|time stop]]_
8th—mass _[[spells/Charm Monster|charm monster]]_ (DC 26), _[[spells/Mind Blank|mind blank]]_, quickened _[[spells/Phantasmal Killer|phantasmal killer]]_, _[[spells/Polar Ray|polar ray]]_
7th—_[[spells/Banishment|banishment]]_ (DC 25), quickened _[[spells/Fireball|fireball]]_ (2), mass _[[spells/Hold Person|hold person]]_ (DC 25), _[[spells/Reverse Gravity|reverse gravity]]_
6th—_[[spells/Chain Lightning|chain lightning]]_ (DC 24), _[[spells/Disintegrate|disintegrate]]_ (DC 24), quickened _[[spells/Glitterdust|glitterdust]]_, greater _[[spells/Dispel Magic|dispel magic]]_, stilled teleport, _[[spells/Wall of Iron|wall of iron]]_
5th—_[[spells/Cloudkill|cloudkill]]_ (DC 23), stilled _[[spells/Dimension Door|dimension door]]_, _[[spells/Interposing Hand|interposing hand]]_, teleport, _[[spells/Wall Of Force|wall of force]]_ (2)
4th—_[[spells/Beast Shape II|beast shape II]]_, _[[spells/Confusion|confusion]]_ (DC 22), _dimension door_, _[[spells/Fire Shield|fire shield]]_, stilled _fireball_, _[[spells/Stoneskin|stoneskin]]_, _[[spells/Wall Of Ice|wall of ice]]_ (DC 22)
3rd—_dispel magic_ (2), _fireball_ (2, DC 21), fly, _[[spells/Lightning Bolt|lightning bolt]]_ (2, DC 21)
2nd—_[[spells/Acid Arrow|acid arrow]]_ (2), _[[spells/Darkvision|darkvision]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Scorching Ray|scorching ray]]_, web (DC 20)
1st—_[[spells/Feather Fall|feather fall]]_, _[[spells/Magic Missile|magic missile]]_ (4), _[[spells/Mount|mount]]_, _[[spells/Shield|shield]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_
**Opposition Schools **_[[spells/Divination|divination]]_, necromancy

### Tactics

**Before Combat **The eldritch _knight_ casts _stoneskin_.
**During Combat **The _knight_ casts _time stop_, then _shield_, _[[spells/Expeditious Retreat|expeditious retreat]]_, fly, and _mirror image_.
**Base Statistics **Without _stoneskin_, the _knight_’s statistics are **DR **none.

##### Statistics
**Str** 16, **Dex** 13, **Con** 20, **Int** 26, **Wis** 10, **Cha** 8
**Base Atk** +16; **CMB** +19; **CMD** 34
**Feats** _[[feats/Arcane Armor Mastery|Arcane Armor Mastery]]_, _[[feats/Arcane Armor Training|Arcane Armor Training]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _[[feats/Craft Wand|Craft Wand]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Disruptive|Disruptive]]_, _[[feats/Greater Weapon Focus|Greater Weapon Focus]]_ (_longsword_), _[[feats/Improved Critical|Improved Critical]]_ (_longsword_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Penetration|Spell Penetration]]_, _[[feats/Still Spell|Still Spell]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_longsword_), _[[feats/Weapon Specialization|Weapon Specialization]]_ (_longsword_)
**Skills** Bluff +19, Fly +22, Intimidate +22, Knowledge (arcana, planes) +31, Knowledge (dungeoneering, engineering, geography, history, local, nobility) +21, Perception +20, Ride +17, Spellcraft +31
**Languages** Abyssal, Common, Draconic, Dwarven, Elven, Giant, _[[monsters/Goblin|Goblin]]_, Ignan, Infernal
**SQ** arcane bond (+2 _longsword_), diverse _[[items/Weapon Magic Abilities/Training|training]]_
**Combat Gear** wand of greater _invisibility_ (15 charges), wand of _[[spells/See Invisibility|see invisibility]]_ (10 charges); **Other Gear** +5 moderate _[[universal monster rules/Fortification|fortification]]_ mithral _[[items/Armor/Full plate|full plate]]_, +3 _longsword_, _[[items/Wondrous Item/Amulet of Natural Armor +5|amulet of natural armor +5]]_, _[[items/Wondrous Item/Belt of Physical Might +4|belt of physical might +4]]_ (Str, Con), _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Headband of Vast Intelligence +6|headband of vast intelligence +6]]_, _[[items/Ring/Ring of Protection +4|ring of protection +4]]_, granite and diamond dust (worth 500 gp), iron sheet and gold dust (worth 50 gp), 3,585 gp

Clad in _full plate_, these eldritch knights mix an impenetrable defense with a relentless spell offense.
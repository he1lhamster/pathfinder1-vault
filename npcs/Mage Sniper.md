---
cssclass: [monsters]
title1: Mage Sniper
title2: Mage Sniper
CR: 13
sources:
- name: NPC Codex
  page: 189
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 25600
race: Half-elf
classes:
- evoker 14
alignment: LN
size: Medium
type: humanoid
subtypes:
- elf
- human
initiative:
  bonus: 4
senses:
  darkvision: 60
  low-light vision: true
  see invisibility: true
AC:
  AC: 21
  touch: 16
  flat_footed: 17
  components:
    armor: 4
    deflection: 2
    dex: 4
    natural: 1
HP:
  HP: 69
  long: 14d6+18
saves:
  fort: 7
  ref: 10
  will: 11
  other: +2 vs. enchantments
defensive_abilities:
- nondetection
- spell turning
resistances:
  electricity: 30
  fire: 30
speeds:
  base: 30
attacks:
  melee:
  - - text: dagger +8/+3 (1d4+1/19-20)
      entries:
      - - damage: 1d4+1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 8
      - 3
  ranged:
  - - text: light crossbow +11 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 11
  special:
  - intense spells (+7 damage)
spell_like_abilities:
  entries:
  - name: elemental wall
    source: default
    freq: At will
    other: 14 rounds/day
  - name: force missile
    source: default
    freq: 9/day
    other: 1d4+7
  sources:
  - name: default
    CL: 14
    concentration: 20
spells:
  entries:
  - name: enlarged maximized fireball
    source: Evoker
    level: 7
    DC: 21
  - name: prismatic spray
    source: Evoker
    level: 7
  - name: spell turning
    source: Evoker
    level: 7
  - name: disintegrate
    source: Evoker
    level: 6
    DC: 23
  - name: greater dispel magic
    source: Evoker
    level: 6
  - name: enlarged maximized scorching ray
    source: Evoker
    level: 6
    count: 2
  - name: enlarged telekinesis
    source: Evoker
    level: 6
    DC: 22
  - name: maximized acid arrow
    source: Evoker
    level: 5
  - name: enlarged black tentacles
    source: Evoker
    level: 5
  - name: maximized scorching ray
    source: Evoker
    level: 5
  - name: teleport
    source: Evoker
    level: 5
  - name: wall of force
    source: Evoker
    level: 5
  - name: arcane eye
    source: Evoker
    level: 4
  - name: dimension door
    source: Evoker
    level: 4
  - name: greater invisibility
    source: Evoker
    level: 4
  - name: enlarged lightning bolt
    source: Evoker
    level: 4
    DC: 21
  - name: maximized magic missile
    source: Evoker
    level: 4
  - name: shout
    source: Evoker
    level: 4
    DC: 22
  - name: clairaudience/clairvoyance
    source: Evoker
    level: 3
    count: 2
  - name: dispel magic
    source: Evoker
    level: 3
  - name: fly
    source: Evoker
    level: 3
  - name: nondetection
    source: Evoker
    level: 3
  - name: wind wall
    source: Evoker
    level: 3
  - name: acid arrow
    source: Evoker
    level: 2
  - name: darkness
    source: Evoker
    level: 2
  - name: darkvision
    source: Evoker
    level: 2
  - name: glitterdust
    source: Evoker
    level: 2
    DC: 18
  - name: resist energy
    source: Evoker
    level: 2
    count: 2
  - name: see invisibility
    source: Evoker
    level: 2
  - name: endure elements
    source: Evoker
    level: 1
  - name: expeditious retreat
    source: Evoker
    level: 1
  - name: mage armor
    source: Evoker
    level: 1
  - name: magic missile
    source: Evoker
    level: 1
  - name: shield
    source: Evoker
    level: 1
  - name: true strike
    source: Evoker
    level: 1
    count: 2
  - name: dancing lights
    source: Evoker
    level: 0
  - name: detect magic
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
    CL: 14
    concentration: 20
    slots:
      0: at-will
    opposition_schools:
    - enchantment
    - necromancy
tactics:
  Before Combat: The wizard casts darkvision, endure elements, mage armor, nondetection,
    resist energy (electricity, fire), see invisibility, and spell turning.
  During Combat: The wizard uses tactics specific to his quarry, choosing spells with
    saving throws that target his prey's weakest defenses. When facing a target he
    knows little about, he casts greater invisibility and then enlarged black tentacles
    to give him time to find the perfect spell. Against single targets, he casts disintegrate,
    enlarged maximized scorching ray, or maximized magic missile. He uses telekinesis
    to hurl boulders if the kill is supposed to look like an accident.
  Base Statistics: Without darkvision, mage armor, resist energy (electricity, fire),
    and see invisibility, the wizard's statistics are AC 17, touch 16, flat-footed
    13; Senses low-light vision; Defensive Abilities none; Resist none.
ability_scores:
  STR: 12
  DEX: 18
  CON: 13
  INT: 22
  WIS: 10
  CHA: 8
BAB: 7
CMB: 8
CMD: 24
feats:
- name: Craft Wondrous Item
- name: Enlarge Spell
- name: Greater Spell Focus (evocation)
- name: Maximize Spell
- name: Point-Blank Shot
- name: Precise Shot
- name: Scribe Scroll
- name: Skill Focus (Perception)
- name: Spell Focus (evocation)
- name: Spell Focus (transmutation)
- name: Spell Penetration
skills:
  Acrobatics: 9
  Climb: 11
  Fly: 17
  Handle Animal: 4
  Knowledge (arcana): 23
  Knowledge (geography): 14
  Knowledge (local): 19
  Knowledge (nature): 15
  Perception: 27
  Spellcraft: 23
  Stealth: 18
  Survival: 10
  Swim: 6
languages:
- Common
- Draconic
- Dwarven
- Elven
- Gnome
- Halfling
- Orc
special_qualities:
- arcane bond (ring of protection +2)
- elf blood
gear:
  combat:
  - potion of cure serious wounds (2)
  - potion of invisibility
  - potion of pass without trace
  - scrolls of teleport (2)
  - wand of scorching ray (CL 11th, 20 charges)
  other:
  - dagger
  - light crossbow with 10 bolts
  - amulet of natural armor +1
  - bag of holding (type II)
  - belt of incredible dexterity +2
  - cloak of resistance +2
  - eyes of the eagle
  - headband of vast intelligence +4
  - ring of protection +2
  - ring of sustenance
  - spellbook
  - 1,937 gp
desc_long: The mage sniper kills with spells at extreme range.

---

# Mage Sniper

**Source** NPC Codex pg. 189
**XP** 25,600
Half-elf evoker 14

LN Medium humanoid (elf, human)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +27

##### Defense

**AC** 21, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+4 armor, +2 _[[spells/Deflection|deflection]]_, +4 Dex, +1 natural)
**hp** 69 (14d6+18)
**Fort** +7, **Ref** +10, **Will** +11; +2 vs. enchantments
**Defensive Abilities** _[[spells/Nondetection|nondetection]]_, _[[spells/Spell Turning|spell turning]]_; **Resist** electricity 30, fire 30

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +8/+3 (1d4+1/19–20)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +11 (1d8/19–20)
**Special Attacks** intense spells (+7 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +20)
At will—elemental wall (14 rounds/day)
 9/day—force missile (1d4+7)
**Evoker Spells Prepared **(CL 14th; concentration +20)
7th—enlarged maximized _[[spells/Fireball|fireball]]_ (DC 21), _[[spells/Prismatic Spray|prismatic spray]]_, _spell turning_
6th—_[[spells/Disintegrate|disintegrate]]_ (DC 23), greater _[[spells/Dispel Magic|dispel magic]]_, enlarged maximized _[[spells/Scorching Ray|scorching ray]]_ (2), enlarged _[[spells/Telekinesis|telekinesis]]_ (DC 22)
5th—maximized _[[spells/Acid Arrow|acid arrow]]_, enlarged _[[spells/Black Tentacles|black tentacles]]_, maximized _scorching ray_, teleport, _[[spells/Wall Of Force|wall of force]]_
4th—_[[spells/Arcane Eye|arcane eye]]_, _[[spells/Dimension Door|dimension door]]_, greater _[[spells/Invisibility|invisibility]]_, enlarged _[[spells/Lightning Bolt|lightning bolt]]_ (DC 21), maximized _[[spells/Magic Missile|magic missile]]_, _[[spells/Shout|shout]]_ (DC 22)
3rd—clairaudience/clairvoyance (2), _dispel magic_, fly, _nondetection_, _[[spells/Wind Wall|wind wall]]_
2nd—_acid arrow_, _[[spells/Darkness|darkness]]_, _darkvision_, _[[spells/Glitterdust|glitterdust]]_ (DC 18), _[[spells/Resist Energy|resist energy]]_ (2), _see invisibility_
1st—_[[spells/Endure Elements|endure elements]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Mage Armor|mage armor]]_, _magic missile_, _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_ (2)
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_
**Opposition Schools **enchantment, necromancy

### Tactics

**Before Combat **The _[[classes/Wizard|wizard]]_ casts _darkvision_, _endure elements_, _mage armor_, _nondetection_, _resist energy_ (electricity, fire), _see invisibility_, and _spell turning_.
**During Combat **The _wizard_ uses tactics specific to his quarry, choosing spells with saving throws that target his prey’s weakest defenses. When facing a target he knows little about, he casts greater _invisibility_ and then enlarged _black tentacles_ to give him time to find the perfect spell. Against single targets, he casts _disintegrate_, enlarged maximized _scorching ray_, or maximized _magic missile_. He uses _telekinesis_ to hurl boulders if the kill is supposed to look like an accident.
**Base Statistics **Without _darkvision_, _mage armor_, _resist energy_ (electricity, fire), and _see invisibility_, the _wizard_’s statistics are **AC **17, touch 16, _flat-footed_ 13; **Senses **_low-light vision_; **Defensive Abilities **none; **Resist **none.

##### Statistics
**Str** 12, **Dex** 18, **Con** 13, **Int** 22, **Wis** 10, **Cha** 8
**Base Atk** +7; **CMB** +8; **CMD** 24
**Feats** _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Enlarge Spell|Enlarge Spell]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (evocation), _[[feats/Maximize Spell|Maximize Spell]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Spell Focus|Spell Focus]]_ (evocation, transmutation), _[[feats/Spell Penetration|Spell Penetration]]_
**Skills** Acrobatics +9, _[[universal monster rules/Climb|Climb]]_ +11, Fly +17, Handle Animal +4, Knowledge (arcana) +23, Knowledge (geography) +14, Knowledge (local) +19, Knowledge (nature) +15, Perception +27, Spellcraft +23, Stealth +18, Survival +10, Swim +6
**Languages** Common, Draconic, Dwarven, Elven, Gnome, Halfling, _[[monsters/Orc|Orc]]_
**SQ** arcane bond (_[[items/Ring/Ring of Protection +2|ring of protection +2]]_), elf blood
**Combat Gear** potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), potion of _invisibility_, potion of _[[spells/Pass without Trace|pass without trace]]_, scrolls of teleport (2), wand of _scorching ray_ (CL 11th, 20 charges); **Other Gear** _dagger_, _light crossbow_ with 10 bolts, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, bag of holding (type II), _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Eyes of the Eagle|eyes of the eagle]]_, _[[items/Wondrous Item/Headband of Vast Intelligence +4|headband of vast intelligence +4]]_, _ring of protection +2_, _[[items/Ring/Ring of Sustenance|ring of sustenance]]_, _[[items/Mundane/Spellbook|spellbook]]_, 1,937 gp

The _[[npcs/Mage Sniper|mage sniper]]_ kills with spells at extreme range.
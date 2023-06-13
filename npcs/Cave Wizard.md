---
cssclass: [monsters]
title1: Cave Wizard
title2: Cave Wizard
CR: 8
sources:
- name: NPC Codex
  page: 184
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 4800
race: Dwarf
classes:
- evoker 9
alignment: NE
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 3
AC:
  AC: 15
  touch: 10
  flat_footed: 15
  components:
    armor: 4
    deflection: 1
    dex: -1
    natural: 1
HP:
  HP: 92
  long: 9d6+58
saves:
  fort: 8
  ref: 2
  will: 9
  other: +2 vs. poison, spells, and spell-like abilities
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
immunities:
- fire (108 points)
speeds:
  base: 20
attacks:
  melee:
  - - text: battleaxe +5 (1d8+1/×3)
      entries:
      - - damage: 1d8+1
          crit_multiplier: 3
      attack: battleaxe
      bonus:
      - 5
  special:
  - +1 on attack rolls against goblinoid and orc humanoids
  - intense spells (+4 damage)
spell_like_abilities:
  entries:
  - name: elemental wall
    source: default
    freq: At will
    other: 9 rounds/day
  - name: force missile
    source: default
    freq: 7/day
    other: 1d4+4
  sources:
  - name: default
    CL: 9
    concentration: 13
spells:
  entries:
  - name: cone of cold
    source: Evoker
    level: 5
    DC: 20
  - name: transmute rock to mud
    source: Evoker
    level: 5
  - name: empowered acid arrow
    source: Evoker
    level: 4
  - name: greater invisibility
    source: Evoker
    level: 4
  - name: resilient sphere
    source: Evoker
    level: 4
    DC: 19
  - name: stone shape
    source: Evoker
    level: 4
  - name: dispel magic
    source: Evoker
    level: 3
  - name: fireball
    source: Evoker
    level: 3
    DC: 18
  - name: gaseous form
    source: Evoker
    level: 3
  - name: ray of exhaustion
    source: Evoker
    level: 3
    DC: 17
  - name: stinking cloud
    source: Evoker
    level: 3
    DC: 17
  - name: acid arrow
    source: Evoker
    level: 2
  - name: bear's endurance
    source: Evoker
    level: 2
  - name: protection from energy
    source: Evoker
    level: 2
  - name: scorching ray
    source: Evoker
    level: 2
  - name: spider climb
    source: Evoker
    level: 2
  - name: summon swarm
    source: Evoker
    level: 2
  - name: burning hands
    source: Evoker
    level: 1
    count: 2
    DC: 16
  - name: color spray
    source: Evoker
    level: 1
    DC: 15
  - name: feather fall
    source: Evoker
    level: 1
  - name: mage armor
    source: Evoker
    level: 1
  - name: ray of enfeeblement
    source: Evoker
    level: 1
    DC: 15
  - name: acid splash
    source: Evoker
    level: 0
  - name: dancing lights
    source: Evoker
    level: 0
  - name: detect magic
    source: Evoker
    level: 0
  - name: mage hand
    source: Evoker
    level: 0
  sources:
  - name: Evoker
    type: prepared
    CL: 9
    concentration: 13
    slots:
      0: at-will
    opposition_schools:
    - enchantment
    - necromancy
tactics:
  Before Combat: The wizard casts bear's endurance, mage armor, and protection from
    energy (fire).
  During Combat: The wizard casts greater invisibility, then uses transmute rock to
    mud to trap foes. He casts area damage spells at trapped targets and uses stinking
    cloud and resilient sphere to hinder those who escape the mud.
  Base Statistics: Without bear's endurance, mage armor, and protection from energy
    (fire), the wizard's statistics are AC 11, touch 10, flat-footed 11; hp 74; Fort
    +6; Immune none; Con 16.
ability_scores:
  STR: 12
  DEX: 8
  CON: 20
  INT: 18
  WIS: 16
  CHA: 8
BAB: 4
CMB: 5
CMD: 15
CMD_other: 19 vs. bull rush or trip
feats:
- name: Combat Casting
- name: Empower Spell
- name: Improved Initiative
- name: Scribe Scroll
- name: Spell Focus (evocation)
- name: Spell Penetration
- name: Toughness
skills:
  Appraise: 15
    to assess nonmagical metals or gemstones: 17
  Climb: 4
  Craft (alchemy): 12
  Fly: 6
  Knowledge (arcana): 16
  Knowledge (dungeoneering): 16
  Knowledge (engineering): 12
  Perception: 12
    to notice unusual stonework: 14
  Sense Motive: 4
  Spellcraft: 16
languages:
- Common
- Dwarven
- Goblin
- Terran
- Undercommon
special_qualities:
- arcane bond (bat)
gear:
  combat:
  - potion of cure moderate wounds
  - scroll of clairaudience/clairvoyance
  - scroll of solid fog
  - scroll of stinking cloud
  - scroll of stone shape
  other:
  - battleaxe
  - amulet of natural armor +1
  - headband of vast intelligence +2
  - ring of protection +1
  - spellbook
  - 665 gp
desc_long: The cave wizard manipulates the energy of deep rock.

---

# Cave Wizard

**Source** NPC Codex pg. 184
**XP** 4,800
Dwarf evoker 9

NE Medium humanoid (dwarf)
**Init** +3; **Senses** Perception +12

##### Defense

**AC** 15, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 armor, +1 _[[spells/Deflection|deflection]]_, –1 Dex, +1 natural)
**hp** 92 (9d6+58)
**Fort** +8, **Ref** +2, **Will** +9; +2 vs. poison, spells, and _[[universal monster rules/Spell-Like Abilities|spell-like abilities]]_
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _[[feats/Dodge|dodge]]_ bonus to AC vs. giants); **Immune** fire (108 points)

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Battleaxe|battleaxe]]_ +5 (1d8+1/×3)
**Special Attacks** +1 on attack rolls against goblinoid and _[[monsters/Orc|orc]]_ humanoids, intense spells (+4 damage)
**_Spell-Like Abilities_** (CL 9th; concentration +13)
At will—elemental wall (9 rounds/day)
7/day—force missile (1d4+4)
**Evoker Spells Prepared **(CL 9th; concentration +13)
5th—_[[spells/Cone of Cold|cone of cold]]_ (DC 20), _[[spells/Transmute Rock to Mud|transmute rock to mud]]_
4th—empowered _[[spells/Acid Arrow|acid arrow]]_, greater _[[spells/Invisibility|invisibility]]_, _[[spells/Resilient Sphere|resilient sphere]]_ (DC 19), _[[spells/Stone Shape|stone shape]]_
3rd—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Fireball|fireball]]_ (DC 18), _[[spells/Gaseous Form|gaseous form]]_, _[[spells/Ray of Exhaustion|ray of exhaustion]]_ (DC 17), _[[spells/Stinking Cloud|stinking cloud]]_ (DC 17)
2nd—_acid arrow_, bear’s _[[feats/Endurance|endurance]]_, _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Scorching Ray|scorching ray]]_, _[[spells/Spider Climb|spider climb]]_, _[[spells/Summon Swarm|summon swarm]]_
1st—_[[spells/Burning Hands|burning hands]]_ (2, DC 16), _[[spells/Color Spray|color spray]]_ (DC 15), _[[spells/Feather Fall|feather fall]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 15)
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_
**Opposition Schools **enchantment, necromancy

### Tactics

**Before Combat **The _[[classes/Wizard|wizard]]_ casts bear’s _endurance_, _mage armor_, and _protection from energy_ (fire).
**During Combat **The _wizard_ casts greater _invisibility_, then uses _transmute rock to mud_ to trap foes. He casts area damage spells at trapped targets and uses _stinking cloud_ and _resilient sphere_ to _[[feats/Hinder|hinder]]_ those who escape the mud.
**Base Statistics **Without bear’s _endurance_, _mage armor_, and _protection from energy_ (fire), the _wizard_’s statistics are **AC **11, touch 10, _flat-footed_ 11; **hp **74; **Fort **+6; **Immune **none; **Con **16.

##### Statistics
**Str** 12, **Dex** 8, **Con** 20, **Int** 18, **Wis** 16, **Cha** 8
**Base Atk** +4; **CMB** +5; **CMD** 15 (19 vs. bull rush or _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation), _[[feats/Spell Penetration|Spell Penetration]]_, _[[feats/Toughness|Toughness]]_
**Skills** Appraise +15 (+17 to assess nonmagical metals or gemstones), _[[universal monster rules/Climb|Climb]]_ +4, Craft (alchemy) +12, Fly +6, Knowledge (arcana, dungeoneering) +16, Knowledge (engineering) +12, Perception +12 (+14 to notice unusual stonework), Sense Motive +4, Spellcraft +16
**Languages** Common, Dwarven, _[[monsters/Goblin|Goblin]]_, Terran, Undercommon
**SQ** arcane bond (bat)
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, scroll of clairaudience/clairvoyance, scroll of _[[spells/Solid Fog|solid fog]]_, scroll of _stinking cloud_, scroll of _stone shape_; **Other Gear** _battleaxe_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Headband of Vast Intelligence +2|headband of vast intelligence +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Mundane/Spellbook|spellbook]]_, 665 gp

The _[[npcs/Cave Wizard|cave wizard]]_ manipulates the energy of deep rock.
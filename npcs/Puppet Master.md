---
cssclass: [monsters]
title1: Puppet Master
title2: Puppet Master
CR: 18
sources:
- name: NPC Codex
  page: 194
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 153600
race: Half-elf
classes:
- enchanter 19
alignment: CE
size: Medium
type: humanoid
subtypes:
- elf
- human
initiative:
  bonus: 6
senses:
  low-light vision: true
AC:
  AC: 24
  touch: 16
  flat_footed: 21
  components:
    armor: 4
    deflection: 3
    dex: 2
    dodge: 1
    natural: 4
HP:
  HP: 139
  long: 19d6+70
saves:
  fort: 13
  ref: 12
  will: 17
  other: +2 vs. enchantments, +4 vs. mind-affecting
defensive_abilities:
- mind blank
- misdirection
- spell turning
immunities:
- electricity (120 points)
- fire (120 points)
resistances:
  cold: 30
speeds:
  base: 35
attacks:
  melee:
  - - text: +1 dagger +9/+4 (1d4/19-20)
      entries:
      - - damage: 1d4
          crit_range: 19-20
      attack: +1 dagger
      bonus:
      - 9
      - 4
  special:
  - aura of despair (19 rounds/day)
spell_like_abilities:
  entries:
  - name: dazing touch
    source: default
    freq: 11/day
  sources:
  - name: default
    CL: 19
    concentration: 27
spells:
  entries:
  - name: dominate monster
    source: Enchanter
    level: 9
    DC: 29
  - name: power word kill
    source: Enchanter
    level: 9
  - name: summon monster IX
    source: Enchanter
    level: 9
  - name: weird
    source: Enchanter
    level: 9
    DC: 27
  - name: horrid wilting
    source: Enchanter
    level: 8
    DC: 26
  - name: incendiary cloud
    source: Enchanter
    level: 8
    DC: 26
  - name: irresistible dance
    source: Enchanter
    level: 8
  - name: mind blank
    source: Enchanter
    level: 8
  - name: polymorph any object
    source: Enchanter
    level: 8
    DC: 26
  - name: extended acid fog
    source: Enchanter
    level: 7
  - name: quickened hold person
    source: Enchanter
    level: 7
    count: 2
    DC: 23
  - name: mass hold person
    source: Enchanter
    level: 7
    DC: 27
  - name: project image
    source: Enchanter
    level: 7
    DC: 25
  - name: spell turning
    source: Enchanter
    level: 7
  - name: disintegrate
    source: Enchanter
    level: 6
    DC: 24
  - name: greater dispel magic
    source: Enchanter
    level: 6
  - name: greater heroism
    source: Enchanter
    level: 6
  - name: mass suggestion
    source: Enchanter
    level: 6
    DC: 26
  - name: quickened mirror image
    source: Enchanter
    level: 6
  - name: repulsion
    source: Enchanter
    level: 6
    DC: 24
  - name: cloudkill
    source: Enchanter
    level: 5
    DC: 23
  - name: dominate person
    source: Enchanter
    level: 5
    DC: 25
  - name: feeblemind
    source: Enchanter
    level: 5
    DC: 25
  - name: hold monster
    source: Enchanter
    level: 5
    DC: 25
  - name: mind fog
    source: Enchanter
    level: 5
    DC: 25
  - name: teleport
    source: Enchanter
    level: 5
  - name: bestow curse
    source: Enchanter
    level: 4
    DC: 22
  - name: charm monster
    source: Enchanter
    level: 4
    count: 2
    DC: 24
  - name: crushing despair
    source: Enchanter
    level: 4
    DC: 24
  - name: enervation
    source: Enchanter
    level: 4
  - name: greater invisibility
    source: Enchanter
    level: 4
  - name: phantasmal killer
    source: Enchanter
    level: 4
    DC: 22
  - name: displacement
    source: Enchanter
    level: 3
  - name: fly
    source: Enchanter
    level: 3
  - name: hold person
    source: Enchanter
    level: 3
    DC: 23
  - name: magic circle against good
    source: Enchanter
    level: 3
  - name: protection from energy
    source: Enchanter
    level: 3
    count: 2
  - name: slow
    source: Enchanter
    level: 3
    DC: 21
  - name: acid arrow
    source: Enchanter
    level: 2
    count: 2
  - name: ghoul touch
    source: Enchanter
    level: 2
    DC: 20
  - name: misdirection
    source: Enchanter
    level: 2
  - name: resist energy
    source: Enchanter
    level: 2
  - name: touch of idiocy
    source: Enchanter
    level: 2
  - name: web
    source: Enchanter
    level: 2
    DC: 20
  - name: charm person
    source: Enchanter
    level: 1
    DC: 21
  - name: expeditious retreat
    source: Enchanter
    level: 1
  - name: feather fall
    source: Enchanter
    level: 1
  - name: mage armor
    source: Enchanter
    level: 1
  - name: obscuring mist
    source: Enchanter
    level: 1
  - name: ray of enfeeblement
    source: Enchanter
    level: 1
    DC: 19
  - name: reduce person
    source: Enchanter
    level: 1
    DC: 19
  - name: bleed
    source: Enchanter
    level: 0
    DC: 18
  - name: daze
    source: Enchanter
    level: 0
    DC: 20
  - name: mage hand
    source: Enchanter
    level: 0
  - name: mending
    source: Enchanter
    level: 0
  sources:
  - name: Enchanter
    type: prepared
    CL: 19
    concentration: 27
    slots:
      0: at-will
    opposition_schools:
    - divination
    - evocation
tactics:
  Before Combat: The wizard casts mage armor, mind blank, misdirection, protection
    from energy (electricity, fire), resist energy (cold), and spell turning.
  During Combat: The wizard uses dominate monster, weird, and mass hold person to
    control enemies, plus incendiary cloud and horrid wilting if they resist enchantments.
    She uses polymorph any object to change the last survivor into a marionette for
    her collection.
  Base Statistics: Without mage armor, mind blank, misdirection, protection from energy,
    resist energy, and spell turning, the wizard's statistics are AC 20, touch 16,
    flat-footed 17; Defensive Abilities none; Immune none; Resist none.
ability_scores:
  STR: 8
  DEX: 14
  CON: 16
  INT: 26
  WIS: 10
  CHA: 14
BAB: 9
CMB: 8
CMD: 24
feats:
- name: Combat Casting
- name: Craft Wand
- name: Craft Wondrous Item
- name: Dodge
- name: Extend Spell
- name: Fleet
- name: Forge Ring
- name: Greater Spell Focus (enchantment)
- name: Improved Initiative
- name: Improved Iron Will
- name: Iron Will
- name: Quicken Spell
- name: Scribe Scroll
- name: Skill Focus (Perception)
- name: Spell Focus (enchantment)
skills:
  Bluff: 17
  Craft (puppets): 16
  Diplomacy: 17
  Disguise: 12
  Fly: 15
  Handle Animal: 7
  Intimidate: 17
  Knowledge (arcana): 26
  Knowledge (dungeoneering): 16
  Knowledge (engineering): 16
  Knowledge (geography): 16
  Knowledge (nature): 16
  Knowledge (nobility): 16
  Knowledge (planes): 16
  Knowledge (religion): 16
  Knowledge (history): 21
  Knowledge (local): 21
  Perception: 24
  Perform (comedy): 12
  Sense Motive: 15
  Spellcraft: 21
languages:
- Common
- Draconic
- Dwarven
- Elven
- Giant
- Goblin
- Gnome
- Halfling
- Sylvan
- Undercommon
special_qualities:
- arcane bond (ring of protection +3)
- elf blood
- enchanting smile
gear:
  combat:
  - potions of cure serious wounds (3)
  - scrolls of mage's private sanctum (2)
  - scroll of power word blind
  - scrolls of summon monster VI (2)
  - wand of displacement (20 charges)
  - wand of fly (20 charges)
  - wand of tongues (20 charges)
  other:
  - +1 dagger
  - amulet of natural armor +4
  - belt of mighty constitution +4
  - cloak of resistance +4
  - figurine of wondrous power (obsidian steed)
  - headband of vast intelligence +6
  - pearl of power (7th)
  - pearl of power (4th)
  - ring of protection +3
  - spellbook
  - 2,036 gp
desc_long: The puppet master treats living minds like a child's toys.

---

# Puppet Master

**Source** NPC Codex pg. 194
**XP** 153,600
Half-elf enchanter 19
CE Medium humanoid (elf, human)
**Init** +6; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +24

##### Defense

**AC** 24, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+4 armor, +3 _[[spells/Deflection|deflection]]_, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +4 natural)
**hp** 139 (19d6+70)
**Fort** +13, **Ref** +12, **Will** +17; +2 vs. enchantments, +4 vs. mind-affecting
**Defensive Abilities** _[[spells/Mind Blank|mind blank]]_, _[[spells/Misdirection|misdirection]]_, _[[spells/Spell Turning|spell turning]]_; **Immune** electricity (120 points), fire (120 points); **Resist** cold 30

##### Offense
**Speed** 35 ft.
**Melee** +1 _[[items/Weapon/Dagger|dagger]]_ +9/+4 (1d4/19–20)
**Special Attacks** aura of despair (19 rounds/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 19th; concentration +27)
11/day—dazing touch
**Enchanter Spells Prepared **(CL 19th; concentration +27)
9th—_[[spells/Dominate Monster|dominate monster]]_ (DC 29), _[[spells/Power Word Kill|power word kill]]_, _[[spells/Summon Monster IX|summon monster IX]]_, _[[spells/Weird|weird]]_ (DC 27)
8th—_[[spells/Horrid Wilting|horrid wilting]]_ (DC 26), _[[spells/Incendiary Cloud|incendiary cloud]]_ (DC 26), _[[spells/Irresistible Dance|irresistible dance]]_, _mind blank_, _[[spells/Polymorph Any Object|polymorph any object]]_ (DC 26)
7th—extended _[[spells/Acid Fog|acid fog]]_, quickened _[[spells/Hold Person|hold person]]_ (2, DC 23), mass _hold person_ (DC 27), _[[spells/Project Image|project image]]_ (DC 25), _spell turning_
6th—_[[spells/Disintegrate|disintegrate]]_ (DC 24), greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ _[[spells/Heroism|heroism]]_, mass _[[spells/Suggestion|suggestion]]_ (DC 26), quickened _[[spells/Mirror Image|mirror image]]_, _[[spells/Repulsion|repulsion]]_ (DC 24)
5th—_[[spells/Cloudkill|cloudkill]]_ (DC 23), _[[spells/Dominate Person|dominate person]]_ (DC 25), _[[spells/Feeblemind|feeblemind]]_ (DC 25), _[[spells/Hold Monster|hold monster]]_ (DC 25), _[[spells/Mind Fog|mind fog]]_ (DC 25), teleport
4th—_[[spells/Bestow Curse|bestow curse]]_ (DC 22), _[[spells/Charm Monster|charm monster]]_ (2, DC 24), _[[spells/Crushing Despair|crushing despair]]_ (DC 24), _[[spells/Enervation|enervation]]_, greater _[[spells/Invisibility|invisibility]]_, _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 22)
3rd—_[[spells/Displacement|displacement]]_, fly, _hold person_ (DC 23), _[[spells/Magic Circle against Good|magic circle against good]]_, _[[spells/Protection from Energy|protection from energy]]_ (2), _[[spells/Slow|slow]]_ (DC 21)
2nd—_[[spells/Acid Arrow|acid arrow]]_ (2), _[[spells/Ghoul touch|ghoul touch]]_ (DC 20), _misdirection_, _[[spells/Resist Energy|resist energy]]_, _[[spells/Touch of Idiocy|touch of idiocy]]_, web (DC 20)
1st—_[[spells/Charm Person|charm person]]_ (DC 21), _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 19), _[[spells/Reduce Person|reduce person]]_ (DC 19)
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 18), _[[spells/Daze|daze]]_ (DC 20), _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_
**Opposition Schools **_[[spells/Divination|divination]]_, evocation

### Tactics

**Before Combat **The _[[classes/Wizard|wizard]]_ casts _mage armor_, _mind blank_, _misdirection_, _protection from energy_ (electricity, fire), _resist energy_ (cold), and _spell turning_.
**During Combat **The _wizard_ uses _dominate monster_, _weird_, and mass _hold person_ to control enemies, plus _incendiary cloud_ and _horrid wilting_ if they resist enchantments. She uses _polymorph any object_ to change the last _[[feats/Survivor|survivor]]_ into a marionette for her collection.
**Base Statistics **Without _mage armor_, _mind blank_, _misdirection_, _protection from energy_, _resist energy_, and _spell turning_, the _wizard_’s statistics are **AC **20, touch 16, _flat-footed_ 17; **Defensive Abilities **none; **Immune **none; **Resist **none.

##### Statistics
**Str** 8, **Dex** 14, **Con** 16, **Int** 26, **Wis** 10, **Cha** 14
**Base Atk** +9; **CMB** +8; **CMD** 24
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Craft Wand|Craft Wand]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _Dodge_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Fleet|Fleet]]_, _[[feats/Forge Ring|Forge Ring]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (enchantment), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Spell Focus|Spell Focus]]_ (enchantment)
**Skills** Bluff +17, Craft (puppets) +16, Diplomacy +17, Disguise +12, Fly +15, Handle Animal +7, Intimidate +17, Knowledge (arcana) +26, Knowledge (dungeoneering, engineering, geography, nature, nobility, planes, religion) +16, Knowledge (history, local) +21, Perception +24, Perform (comedy) +12, Sense Motive +15, Spellcraft +21
**Languages** Common, Draconic, Dwarven, Elven, Giant, _[[monsters/Goblin|Goblin]]_, Gnome, Halfling, Sylvan, Undercommon
**SQ** arcane bond (_[[items/Ring/Ring of Protection +3|ring of protection +3]]_), elf blood, enchanting smile
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (3), scrolls of mage’s private sanctum (2), scroll of _[[spells/Power Word Blind|power word blind]]_, scrolls of _[[spells/Summon Monster VI|summon monster VI]]_ (2), wand of _displacement_ (20 charges), wand of fly (20 charges), wand of _[[spells/Tongues|tongues]]_ (20 charges); **Other Gear** +1 _dagger_, _[[items/Wondrous Item/Amulet of Natural Armor +4|amulet of natural armor +4]]_, _[[items/Wondrous Item/Belt of Mighty Constitution +4|belt of mighty constitution +4]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +4|cloak of _resistance_ +4]]_, figurine of wondrous power (obsidian steed), _[[items/Wondrous Item/Headband of Vast Intelligence +6|headband of vast intelligence +6]]_, pearl of power (7th), pearl of power (4th), _ring of protection +3_, _[[items/Mundane/Spellbook|spellbook]]_, 2,036 gp

The _[[feats/Puppet Master|puppet master]]_ treats living minds like a child’s toys.
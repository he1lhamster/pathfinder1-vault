---
cssclass: [monsters]
title1: Cruel Conjurer
title2: Cruel Conjurer
CR: 14
sources:
- name: NPC Codex
  page: 190
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 38400
race: Human
classes:
- conjurer 15
alignment: LE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 6
senses:
  see invisibility: true
AC:
  AC: 22
  touch: 15
  flat_footed: 19
  components:
    armor: 4
    deflection: 2
    dex: 2
    dodge: 1
    natural: 3
HP:
  HP: 125
  long: 15d6+70
saves:
  fort: 11
  ref: 10
  will: 12
defensive_abilities:
- magic circle against good
immunities:
- fire (120 points)
resistances:
  electricity: 30
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk quarterstaff +7/+2 (1d6-1)
      entries:
      - - damage: 1d6-1
      attack: mwk quarterstaff
      bonus:
      - 7
      - 2
spell_like_abilities:
  entries:
  - name: dimensional steps
    source: default
    freq: At will
    other: 450 feet/day
  - name: acid dart
    source: default
    freq: 9/day
    other: 1d6+7 acid
  sources:
  - name: default
    CL: 15
    concentration: 21
spells:
  entries:
  - name: incendiary cloud
    source: Conjurer
    level: 8
    DC: 26
  - name: summon monster VIII
    source: Conjurer
    level: 8
  - name: extended acid fog
    source: Conjurer
    level: 7
  - name: widened black tentacles
    source: Conjurer
    level: 7
  - name: mass hold person
    source: Conjurer
    level: 7
    DC: 23
  - name: quickened acid arrow
    source: Conjurer
    level: 6
  - name: acid fog
    source: Conjurer
    level: 6
  - name: disintegrate
    source: Conjurer
    level: 6
    DC: 22
  - name: quickened invisibility
    source: Conjurer
    level: 6
  - name: summon monster VI
    source: Conjurer
    level: 6
  - name: cloudkill
    source: Conjurer
    level: 5
    DC: 23
  - name: dismissal
    source: Conjurer
    level: 5
    DC: 21
  - name: shadow evocation
    source: Conjurer
    level: 5
    DC: 21
  - name: summon monster V
    source: Conjurer
    level: 5
  - name: teleport
    source: Conjurer
    level: 5
  - name: widened glitterdust
    source: Conjurer
    level: 5
    DC: 20
  - name: arcane eye
    source: Conjurer
    level: 4
  - name: confusion
    source: Conjurer
    level: 4
    DC: 20
  - name: dimension door
    source: Conjurer
    level: 4
  - name: greater invisibility
    source: Conjurer
    level: 4
  - name: phantasmal killer
    source: Conjurer
    level: 4
    DC: 20
  - name: solid fog
    source: Conjurer
    level: 4
  - name: displacement
    source: Conjurer
    level: 3
  - name: magic circle against good
    source: Conjurer
    level: 3
  - name: protection from energy
    source: Conjurer
    level: 3
  - name: slow
    source: Conjurer
    level: 3
    DC: 19
  - name: stinking cloud
    source: Conjurer
    level: 3
    count: 2
    DC: 21
  - name: acid arrow
    source: Conjurer
    level: 2
  - name: glitterdust
    source: Conjurer
    level: 2
    DC: 20
  - name: knock
    source: Conjurer
    level: 2
  - name: mirror image
    source: Conjurer
    level: 2
  - name: resist energy
    source: Conjurer
    level: 2
  - name: see invisibility
    source: Conjurer
    level: 2
  - name: web
    source: Conjurer
    level: 2
    DC: 20
  - name: charm person
    source: Conjurer
    level: 1
    DC: 17
  - name: color spray
    source: Conjurer
    level: 1
    DC: 17
  - name: expeditious retreat
    source: Conjurer
    level: 1
  - name: feather fall
    source: Conjurer
    level: 1
  - name: grease
    source: Conjurer
    level: 1
  - name: mage armor
    source: Conjurer
    level: 1
  - name: mount
    source: Conjurer
    level: 1
  - name: acid splash
    source: Conjurer
    level: 0
  - name: detect magic
    source: Conjurer
    level: 0
  - name: mage hand
    source: Conjurer
    level: 0
  - name: read magic
    source: Conjurer
    level: 0
  sources:
  - name: Conjurer
    type: prepared
    CL: 15
    concentration: 21
    slots:
      0: at-will
    opposition_schools:
    - evocation
    - necromancy
tactics:
  Before Combat: The wizard casts mage armor, magic circle against good, protection
    from energy (fire), resist energy (electricity), and see invisibility.
  During Combat: The wizard leads with mass hold person, followed by widened black
    tentacles or incendiary cloud if opponents are immune to enchantments. He banishes
    creatures summoned by foes, charms enemies with his staff, summons allies to protect
    him, turns uncharmed enemies against each other with confusion, and targets leaders
    with disintegrate or phantasmal killer.
  Base Statistics: Without mage armor, magic circle against good, protection from
    energy (fire), resist energy (electricity), and see invisibility, the wizard's
    statistics are Senses normal; AC 18, touch 15, flat-footed 15; Defensive Abilities
    none; Immune none; Resist none.
ability_scores:
  STR: 8
  DEX: 14
  CON: 16
  INT: 23
  WIS: 10
  CHA: 12
BAB: 7
CMB: 6
CMD: 21
feats:
- name: Augment Summoning
- name: Combat Casting
- name: Craft Wondrous Item
- name: Dodge
- name: Extend Spell
- name: Greater Spell Focus (conjuration)
- name: Improved Initiative
- name: Quicken Spell
- name: Scribe Scroll
- name: Spell Focus (Conjuration)
- name: Spell Penetration
- name: Toughness
- name: Widen Spell
skills:
  Bluff: 16
  Diplomacy: 16
  Fly: 10
  Knowledge (arcana): 24
  Knowledge (planes): 24
  Knowledge (dungeoneering): 14
  Knowledge (geography): 14
  Knowledge (nature): 19
  Knowledge (religion): 19
  Perception: 15
  Ride: 7
  Sense Motive: 10
  Spellcraft: 24
languages:
- Abyssal
- Aquan
- Auran
- Common
- Ignan
- Infernal
- Terran
special_qualities:
- arcane bond (staff)
- summoner's charm (7 rounds)
gear:
  combat:
  - potion of cure serious wounds
  - potion of invisibility
  - scroll of summon monster VIII
  - staff of charming
  other:
  - amulet of natural armor +3
  - belt of mighty constitution +2
  - cloak of resistance +3
  - headband of vast intelligence +4
  - ring of protection +2
  - spellbook
  - 2,150 gp
desc_long: A cruel conjurer directs his minions as if they were pawns in a game.

---

# Cruel Conjurer

**Source** NPC Codex pg. 190
**XP** 38,400
Human conjurer 15

LE Medium humanoid (human)
**Init** +6; **Senses** _[[spells/See Invisibility|see invisibility]]_; Perception +15

##### Defense

**AC** 22, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+4 armor, +2 _[[spells/Deflection|deflection]]_, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +3 natural)
**hp** 125 (15d6+70)
**Fort** +11, **Ref** +10, **Will** +12
**Defensive Abilities** _[[spells/Magic Circle against Good|magic circle against good]]_; **Immune** fire (120 points); **Resist** electricity 30

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Quarterstaff|quarterstaff]]_ +7/+2 (1d6–1)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +21)
At will—dimensional steps (450 feet/day)
 9/day—acid _[[items/Weapon/Dart|dart]]_ (1d6+7 acid)
**Conjurer Spells Prepared **(CL 15th; concentration +21)
8th—_[[spells/Incendiary Cloud|incendiary cloud]]_ (DC 26), _[[spells/Summon Monster VIII|summon monster VIII]]_
7th—extended _[[spells/Acid Fog|acid fog]]_, widened _[[spells/Black Tentacles|black tentacles]]_, mass _[[spells/Hold Person|hold person]]_ (DC 23)
6th—quickened _[[spells/Acid Arrow|acid arrow]]_, _acid fog_, _[[spells/Disintegrate|disintegrate]]_ (DC 22), quickened _[[spells/Invisibility|invisibility]]_, _[[spells/Summon Monster VI|summon monster VI]]_
5th—_[[spells/Cloudkill|cloudkill]]_ (DC 23), _[[spells/Dismissal|dismissal]]_ (DC 21), _[[spells/Shadow Evocation|shadow evocation]]_ (DC 21), _[[spells/Summon Monster V|summon monster V]]_, teleport, widened _[[spells/Glitterdust|glitterdust]]_ (DC 20)
4th—_[[spells/Arcane Eye|arcane eye]]_, _[[spells/Confusion|confusion]]_ (DC 20), _[[spells/Dimension Door|dimension door]]_, greater _invisibility_, _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 20), _[[spells/Solid Fog|solid fog]]_
3rd—_[[spells/Displacement|displacement]]_, _magic circle against good_, _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Slow|slow]]_ (DC 19), _[[spells/Stinking Cloud|stinking cloud]]_ (2, DC 21)
2nd—_acid arrow_, _glitterdust_ (DC 20), _[[spells/Knock|knock]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Resist Energy|resist energy]]_, _see invisibility_, web (DC 20)
1st—_[[spells/Charm Person|charm person]]_ (DC 17), _[[spells/Color Spray|color spray]]_ (DC 17), _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Grease|grease]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Mount|mount]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Read Magic|read magic]]_
**Opposition Schools **evocation, necromancy

### Tactics

**Before Combat **The _[[classes/Wizard|wizard]]_ casts _mage armor_, _magic circle against good_, _protection from energy_ (fire), _resist energy_ (electricity), and _see invisibility_.
**During Combat **The _wizard_ leads with mass _hold person_, followed by widened _black tentacles_ or _incendiary cloud_ if opponents are immune to enchantments. He banishes creatures summoned by foes, charms enemies with his staff, summons allies to protect him, turns uncharmed enemies against each other with _confusion_, and targets leaders with _disintegrate_ or _phantasmal killer_.
**Base Statistics **Without _mage armor_, _magic circle against good_, _protection from energy_ (fire), _resist energy_ (electricity), and _see invisibility_, the _wizard_’s statistics are **Senses **normal; **AC **18, touch 15, _flat-footed_ 15; **Defensive Abilities **none; **Immune **none; **Resist **none.

##### Statistics
**Str** 8, **Dex** 14, **Con** 16, **Int** 23, **Wis** 10, **Cha** 12
**Base Atk** +7; **CMB** +6; **CMD** 21
**Feats** _[[feats/Augment Summoning|Augment Summoning]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _Dodge_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (conjuration), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Focus|Spell Focus]]_ (Conjuration), _[[feats/Spell Penetration|Spell Penetration]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Widen Spell|Widen Spell]]_
**Skills** Bluff +16, Diplomacy +16, Fly +10, Knowledge (arcana, planes) +24, Knowledge (dungeoneering, geography) +14, Knowledge (nature, religion) +19, Perception +15, Ride +7, Sense Motive +10, Spellcraft +24
**Languages** Abyssal, Aquan, Auran, Common, Ignan, Infernal, Terran
**SQ** arcane bond (staff), _[[classes/Summoner|summoner]]_’s charm (7 rounds)
**Combat Gear** potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_, potion of _invisibility_, scroll of _summon monster VIII_, _[[items/Staff/Staff of Charming|staff of charming]]_; **Other Gear** _[[items/Wondrous Item/Amulet of Natural Armor +3|amulet of natural armor +3]]_, _[[items/Wondrous Item/Belt of Mighty Constitution +2|belt of mighty constitution +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Headband of Vast Intelligence +4|headband of vast intelligence +4]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, _[[items/Mundane/Spellbook|spellbook]]_, 2,150 gp

A _[[npcs/Cruel Conjurer|cruel conjurer]]_ directs his minions as if they were pawns in a game.
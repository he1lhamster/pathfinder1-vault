---
cssclass: [monsters]
title1: Arcanothief
title2: Arcanothief
CR: 12
sources:
- name: NPC Codex
  page: 205
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 19200
race: Halfling
classes:
- rogue 4
- sorcerer 5
- arcane trickster 4
alignment: N
size: Small
type: humanoid
subtypes:
- halfling
initiative:
  bonus: 4
AC:
  AC: 22
  touch: 16
  flat_footed: 18
  components:
    armor: 5
    deflection: 1
    dex: 4
    natural: 1
    size: 1
HP:
  HP: 111
  long: 4d8+5d6+4d6+44
saves:
  fort: 9
  ref: 16
  will: 10
  other: +2 vs. fear
defensive_abilities:
- evasion
- trap sense +1
- uncanny dodge
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk rapier +7/+2 (1d4-2)
      entries:
      - - damage: 1d4-2
      attack: mwk rapier
      bonus:
      - 7
      - 2
  ranged:
  - - text: +1 heavy crossbow +13 (1d8+1/19-20)
      entries:
      - - damage: 1d8+1
          crit_range: 19-20
      attack: +1 heavy crossbow
      bonus:
      - 13
  special:
  - impromptu sneak attack 1/day
  - sneak attack +4d6
spells:
  entries:
  - name: arcane eye
    source: Sorcerer
    level: 4
  - name: dimension door
    source: Sorcerer
    level: 4
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: flame arrow
    source: Sorcerer
    level: 3
  - name: gaseous form
    source: Sorcerer
    level: 3
  - name: false life
    source: Sorcerer
    level: 2
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: knock
    source: Sorcerer
    level: 2
  - name: locate object
    source: Sorcerer
    level: 2
  - name: spider climb
    source: Sorcerer
    level: 2
  - name: detect secret doors
    source: Sorcerer
    level: 1
  - name: erase
    source: Sorcerer
    level: 1
  - name: feather fall
    source: Sorcerer
    level: 1
  - name: floating disk
    source: Sorcerer
    level: 1
  - name: identify
    source: Sorcerer
    level: 1
  - name: unseen servant
    source: Sorcerer
    level: 1
  - name: acid splash
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
  - name: open/close
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  - name: ray of frost
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 9
    concentration: 12
    failure_chance: 10%
    slots:
      4: 4
      3: 7
      2: 7
      1: 7
      0: at-will
    bloodline: arcane
tactics:
  Before Combat: The arcane trickster casts false life.
  During Combat: The arcane trickster stays out of melee, using invisibility, gaseous
    form, and dimension door to keep her distance while pelting foes with crossbow
    bolts. When in dire straits, she uses her scroll of teleport to flee.
  Base Statistics: Without false life, the arcane trickster's statistics are hp 97.
ability_scores:
  STR: 6
  DEX: 18
  CON: 16
  INT: 13
  WIS: 10
  CHA: 16
BAB: 7
CMB: 4
CMD: 19
feats:
- name: Arcane Armor Training
- name: Eschew Materials
- name: Extend Spell
- name: Improved Lightning Reflexes
- name: Lightning Reflexes
- name: Nimble Moves
- name: Skill Focus (Disable Device)
- name: Still Spell
skills:
  Acrobatics: 15
    when jumping: 11
  Climb: 9
  Disable Device: 26
  Escape Artist: 11
  Knowledge (arcana): 10
  Perception: 16
  Stealth: 24
  Swim: 7
  Use Magic Device: 12
languages:
- Common
- Draconic
- Halfling
special_qualities:
- arcane bond (+1 heavy crossbow)
- bloodline arcana (+1 DC for spells with metamagic feats that increase spell level)
- metamagic adept (1/day)
- ranged legerdemain
- rogue talents (quick disable, trap spotter)
- trapfinding +2
gear:
  combat:
  - +1 construct-bane bolts (3)
  - +1 undead-bane bolts (3)
  - potions of cure serious wounds (2)
  - scroll of neutralize poison
  - scroll of remove curse
  - scroll of remove disease
  - scroll of teleport
  - wand of delay poison (10 charges)
  - antitoxin (5)
  - holy water (5)
  - tindertwigs (5)
  other:
  - +1 mithral chain shirt
  - +1 heavy crossbow with 20 bolts
  - masterwork rapier
  - amulet of natural armor +1
  - belt of incredible dexterity +2
  - cloak of resistance +2
  - gloves of arrow snaring
  - ring of protection +1
  - everburning torch
  - masterwork thieves' tools
  - spell component pouch
  - 56 gp
desc_long: Masters at breaking into wizard towers and sorcerer societies, arcanothieves
  steal magic items, supplying local fences or selling directly to visiting adventurers.

---

# Arcanothief

**Source** NPC Codex pg. 205
**XP** 19,200
Halfling _[[classes/Rogue|rogue]]_ 4/sorcerer 5/arcane trickster 4

N Small humanoid (halfling)
**Init** +4; **Senses** Perception +16

##### Defense

**AC** 22, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+5 armor, +1 deflection, +4 Dex, +1 natural, +1 size)
**hp** 111 (4d8+5d6+4d6+44)
**Fort** +9, **Ref** +16, **Will** +10; +2 vs. _[[universal monster rules/Fear|fear]]_
**Defensive Abilities** evasion, trap sense +1, uncanny _[[feats/Dodge|dodge]]_

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Rapier|rapier]]_ +7/+2 (1d4–2)
**Ranged** +1 _[[items/Weapon/Heavy crossbow|heavy crossbow]]_ +13 (1d8+1/19–20)
**Special Attacks** impromptu sneak attack 1/day, sneak attack +4d6
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 9th; concentration +12; arcane spell failure 10%)
4th (4/day)—_[[spells/Arcane Eye|arcane eye]]_, _[[spells/Dimension Door|dimension door]]_
3rd (7/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Flame Arrow|flame arrow]]_, _[[spells/Gaseous Form|gaseous form]]_
2nd (7/day)—_[[spells/False Life|false life]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Knock|knock]]_, _[[spells/Locate Object|locate object]]_, _[[spells/Spider Climb|spider climb]]_
1st (7/day)—_[[spells/Detect Secret Doors|detect secret doors]]_, _[[spells/Erase|erase]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Floating Disk|floating disk]]_, _[[spells/Identify|identify]]_, _[[spells/Unseen Servant|unseen servant]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, light, _[[spells/Mage Hand|mage hand]]_, open/close, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Ray of Frost|ray of frost]]_
**Bloodline **arcane

### Tactics

**Before Combat **The arcane trickster casts _false life_.
**During Combat **The arcane trickster stays out of melee, using _invisibility_, _gaseous form_, and _dimension door_ to keep her distance while pelting foes with crossbow bolts. When in dire straits, she uses her scroll of teleport to flee.
**Base Statistics **Without _false life_, the arcane trickster’s statistics are **hp **97.

##### Statistics
**Str** 6, **Dex** 18, **Con** 16, **Int** 13, **Wis** 10, **Cha** 16
**Base Atk** +7; **CMB** +4; **CMD** 19
**Feats** _[[feats/Arcane Armor Training|Arcane Armor Training]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Improved Lightning Reflexes|Improved Lightning Reflexes]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Nimble Moves|Nimble Moves]]_, _[[feats/Skill Focus|Skill Focus]]_ (Disable Device), _[[feats/Still Spell|Still Spell]]_
**Skills** Acrobatics +15 (+11 when jumping), _[[universal monster rules/Climb|Climb]]_ +9, Disable Device +26, Escape Artist +11, Knowledge (arcana) +10, Perception +16, Stealth +24, Swim +7, Use Magic Device +12
**Languages** Common, Draconic, Halfling
**SQ** arcane bond (+1 _heavy crossbow_), bloodline arcana (+1 DC for spells with metamagic feats that increase spell level), metamagic adept (1/day), ranged legerdemain, _rogue_ talents (quick disable, trap spotter), trapfinding +2
**Combat Gear** +1 construct-bane bolts (3), +1 undead-bane bolts (3), potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), scroll of _[[spells/Neutralize Poison|neutralize poison]]_, scroll of _[[spells/Remove Curse|remove curse]]_, scroll of _[[spells/Remove Disease|remove disease]]_, scroll of teleport, wand of _[[spells/Delay Poison|delay poison]]_ (10 charges), _[[items/Mundane/Antitoxin|antitoxin]]_ (5), _[[items/Mundane/Holy water|holy water]]_ (5), tindertwigs (5); **Other Gear** +1 mithral _[[items/Armor/Chain shirt|chain shirt]]_, +1 _heavy crossbow_ with 20 bolts, masterwork _rapier_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Gloves of Arrow Snaring|gloves of arrow snaring]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Mundane/Everburning torch|everburning torch]]_, masterwork thieves’ tools, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 56 gp

Masters at _[[items/Weapon Magic Abilities/Breaking|breaking]]_ into _[[classes/Wizard|wizard]]_ towers and _sorcerer_ societies, arcanothieves steal magic items, supplying local fences or selling directly to visiting adventurers.
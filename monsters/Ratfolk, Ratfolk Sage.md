---
cssclass: [monsters]
title1: Ratfolk, Ratfolk Sage
title2: Ratfolk Sage
CR: 6
sources:
- name: Monster Codex
  page: 181
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 2400
race: Ratfolk
classes:
- diviner 7
alignment: N
size: Small
type: humanoid
subtypes:
- ratfolk
initiative:
  bonus: 9
senses:
  darkvision: 60
AC:
  AC: 17
  touch: 13
  flat_footed: 15
  components:
    armor: 4
    dex: 2
    size: 1
HP:
  HP: 48
  long: 7d6+21
saves:
  fort: 6
  ref: 5
  will: 8
speeds:
  base: 20
  climb: 20
attacks:
  melee:
  - - text: mwk quarterstaff +3 (1d4-2)
      entries:
      - - damage: 1d4-2
      attack: mwk quarterstaff
      bonus:
      - 3
  ranged:
  - - text: light crossbow +6 (1d6/19-20)
      entries:
      - - damage: 1d6
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 6
  special:
  - swarming
spell_like_abilities:
  entries:
  - name: diviner's fortune
    source: default
    freq: 8/day
    other: '+3'
  sources:
  - name: default
    CL: 7
    concentration: 12
spells:
  entries:
  - name: arcane eye
    source: Diviner
    level: 4
  - name: dimension door
    source: Diviner
    level: 4
  - name: wall of fire
    source: Diviner
    level: 4
  - name: dispel magic
    source: Diviner
    level: 3
  - name: haste
    source: Diviner
    level: 3
  - name: lightning bolt
    source: Diviner
    level: 3
    DC: 18
  - name: tongues
    source: Diviner
    level: 3
  - name: glitterdust
    source: Diviner
    level: 2
    DC: 17
  - name: invisibility
    source: Diviner
    level: 2
  - name: scorching ray
    source: Diviner
    level: 2
  - name: see invisibility
    source: Diviner
    level: 2
  - name: spider climb
    source: Diviner
    level: 2
  - name: alarm
    source: Diviner
    level: 1
  - name: comprehend languages
    source: Diviner
    level: 1
  - name: expeditious retreat
    source: Diviner
    level: 1
  - name: grease
    source: Diviner
    level: 1
    DC: 16
  - name: mage armor
    source: Diviner
    level: 1
  - name: magic missile
    source: Diviner
    level: 1
    count: 2
  - name: acid splash
    source: Diviner
    level: 0
  - name: dancing lights
    source: Diviner
    level: 0
  - name: detect magic
    source: Diviner
    level: 0
  - name: message
    source: Diviner
    level: 0
  sources:
  - name: Diviner
    type: prepared
    CL: 7
    concentration: 12
    slots:
      0: at-will
    opposition_schools:
    - enchantment
    - necromancy
tactics:
  Before Combat: The ratfolk sage casts mage armor on himself each morning. Because
    he avoids entering direct combat, if battle is imminent, the ratfolk sage casts
    spider climb on himself and climbs to a defensible position. If he is with several
    allies, he uses his wand of blur and scrolls of magic weapon on them and their
    weapons before he does so.
  During Combat: The ratfolk sage casts wall of fire to divide up the battlefield
    and trap the ratfolk's enemies. He then casts offensive spells until he runs out,
    at which point he uses a scroll of magic weapon on his light crossbow before making
    attacks. If cornered, the sage uses dimension door to free himself.
  Base Statistics: Without mage armor and spider climb, the ratfolk sage's statistics
    are AC 13, touch 13, flat-footed 11; Speed 20 ft.; Skills Climb -2.
ability_scores:
  STR: 6
  DEX: 14
  CON: 13
  INT: 20
  WIS: 14
  CHA: 10
BAB: 3
CMB: 0
CMD: 12
feats:
- name: Craft Wondrous Item
- name: Great Fortitude
- name: Improved Initiative
- name: Scribe Scroll
- name: Spell Penetration
- name: Toughness
skills:
  Appraise: 15
  Climb: 6
  Craft (alchemy): 7
  Knowledge (arcana): 12
  Knowledge (geography): 12
  Knowledge (history): 12
  Knowledge (planes): 12
  Linguistics: 15
  Perception: 4
  Spellcraft: 15
  Stealth: 13
  _racial_mods:
    Climb:
      _: 8
    Craft (alchemy):
      _: 2
    Perception:
      _: 2
    Use Magic Device:
      _: 2
languages:
- Abyssal
- Aklo
- Common
- Dark Folk
- Draconic
- Dwarven
- Giant
- Gnoll
- Goblin
- Infernal
- Sylvan
- Terran
- Undercommon
special_qualities:
- arcane bond (staff)
- forewarned
gear:
  combat:
  - potion of cure light wounds
  - scroll of clairaudience/clairvoyance
  - scroll of locate object
  - scrolls of magic weapon (4)
  - wand of blur (13 charges)
  - wand of burning hands (CL 5th, 8 charges)
  other:
  - light crossbow with 10 bolts
  - mwk quarterstaff
  - cloak of resistance +1
  - headband of vast intelligence +2
  - spellbook (contains all prepared spells plus clairaudience/clairvoyance, floating
    disk, identify, locate object, magic weapon, minor image, and shield)
  - 92 gp
ecology:
  environment: warm deserts or urban
desc_long: Magic is most useful to the warren when it provides insight, so diviners
  are held in high regard. Though the ratfolk sage prepares some offensive spells
  in case of attack-it's always good to be ready for danger-such things can be duplicated
  with alchemy and weaponry.

---

# Ratfolk, Ratfolk Sage

**Source** Monster Codex pg. 181
**XP** 2,400
_[[monsters/Ratfolk|Ratfolk]]_ diviner 7

N Small humanoid (_ratfolk_)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +4

##### Defense

**AC** 17, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 armor, +2 Dex, +1 size)
**hp** 48 (7d6+21)
**Fort** +6, **Ref** +5, **Will** +8

##### Offense
**Speed** 20 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** mwk _[[items/Weapon/Quarterstaff|quarterstaff]]_ +3 (1d4–2)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +6 (1d6/19–20)
**Special Attacks** swarming
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +12)
8/day—diviner’s fortune (+3)
**Diviner Spells Prepared **(CL 7th; concentration +12)
4th—_[[spells/Arcane Eye|arcane eye]]_, _[[spells/Dimension Door|dimension door]]_, _[[spells/Wall Of Fire|wall of fire]]_
3rd—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Haste|haste]]_, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 18), _[[spells/Tongues|tongues]]_
2nd—_[[spells/Glitterdust|glitterdust]]_ (DC 17), _[[spells/Invisibility|invisibility]]_, _[[spells/Scorching Ray|scorching ray]]_, _[[spells/See Invisibility|see invisibility]]_, _[[spells/Spider Climb|spider climb]]_
1st—_[[spells/Alarm|alarm]]_, _[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Grease|grease]]_ (DC 16), _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_ (2)
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Message|message]]_
**Opposition Schools** enchantment, necromancy

### Tactics

**Before Combat** The _ratfolk_ sage casts _mage armor_ on himself each morning. Because he avoids entering direct combat, if battle is imminent, the _ratfolk_ sage casts _spider climb_ on himself and climbs to a defensible position. If he is with several allies, he uses his wand of _[[spells/Blur|blur]]_ and scrolls of _[[spells/Magic Weapon|magic weapon]]_ on them and their weapons before he does so.
 **During Combat** The _ratfolk_ sage casts _wall of fire_ to divide up the battlefield and trap the _ratfolk_’s enemies. He then casts offensive spells until he runs out, at which point he uses a scroll of _magic weapon_ on his _light crossbow_ before making attacks. If cornered, the sage uses _dimension door_ to free himself.
 **Base Statistics** Without _mage armor_ and _spider climb_, the _ratfolk_ sage’s statistics are **AC **13, touch 13, _flat-footed_ 11; **Speed **20 ft.; **Skills **_Climb_ –2.

##### Statistics
**Str** 6, **Dex** 14, **Con** 13, **Int** 20, **Wis** 14, **Cha** 10
**Base Atk** +3; **CMB** +0; **CMD** 12
**Feats** _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Penetration|Spell Penetration]]_, _[[feats/Toughness|Toughness]]_
**Skills** Appraise +15, _Climb_ +6, Craft (alchemy) +7, Knowledge (arcana) +12, Knowledge (geography) +12, Knowledge (history) +12, Knowledge (planes) +12, Linguistics +15, Perception +4, Spellcraft +15, Stealth +13; **Racial Modifiers** +8 _Climb_, +2 Craft (alchemy), +2 Perception, +2 Use Magic Device
**Languages** Abyssal, Aklo, Common, Dark Folk, Draconic, Dwarven, Giant, _[[monsters/Gnoll|Gnoll]]_, _[[monsters/Goblin|Goblin]]_, Infernal, Sylvan, Terran, Undercommon
**SQ** arcane bond (staff), forewarned
**Combat Gear** potion of _[[spells/Cure Light Wounds|cure light wounds]]_, scroll of clairaudience/clairvoyance, scroll of _[[spells/Locate Object|locate object]]_, scrolls of _magic weapon_ (4), wand of _blur_ (13 charges), wand of _[[spells/Burning Hands|burning hands]]_ (CL 5th, 8 charges); **Other Gear** _light crossbow_ with 10 bolts, mwk _quarterstaff_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of Vast Intelligence +2|headband of vast intelligence +2]]_, _[[items/Mundane/Spellbook|spellbook]]_ (contains all prepared spells plus clairaudience/clairvoyance, _[[spells/Floating Disk|floating disk]]_, _[[spells/Identify|identify]]_, _locate object_, _magic weapon_, _[[spells/Minor Image|minor image]]_, and _[[spells/Shield|shield]]_), 92 gp

##### Ecology

**Environment** warm deserts or urban

##### Description

Magic is most useful to the warren when it provides insight, so diviners are held in high regard. Though the _ratfolk_ sage prepares some offensive spells in case of attack—it’s always good to be ready for danger—such things can be duplicated with alchemy and weaponry.
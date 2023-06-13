---
cssclass: [monsters]
title1: Thunder Wizard
title2: Thunder Wizard
CR: 6
sources:
- name: NPC Codex
  page: 182
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 2400
race: Halfling
classes:
- evoker 7
alignment: LN
size: Small
type: humanoid
subtypes:
- halfling
initiative:
  bonus: 7
AC:
  AC: 19
  touch: 15
  flat_footed: 16
  components:
    armor: 4
    deflection: 1
    dex: 3
    size: 1
HP:
  HP: 37
  long: 7d6+10
saves:
  fort: 5
  ref: 7
  will: 10
  other: +2 vs. fear
DR:
- amount: 10
  weakness: magic
  other: ranged weapon attack only; 30 points
speeds:
  base: 20
attacks:
  melee:
  - - text: dagger +2 (1d3-2/19-20)
      entries:
      - - damage: 1d3-2
          crit_range: 19-20
      attack: dagger
      bonus:
      - 2
  - - text: quarterstaff +2 (1d4-2)
      entries:
      - - damage: 1d4-2
      attack: quarterstaff
      bonus:
      - 2
  ranged:
  - - text: dagger +7 (1d3-2/19-20)
      entries:
      - - damage: 1d3-2
          crit_range: 19-20
      attack: dagger
      bonus:
      - 7
  special:
  - intense spells (+3 damage)
spell_like_abilities:
  entries:
  - name: force missile
    source: default
    freq: 6/day
    other: 1d4+3
  sources:
  - name: default
    CL: 7
    concentration: 10
spells:
  entries:
  - name: black tentacles
    source: Evoker
    level: 4
  - name: shout
    source: Evoker
    level: 4
    DC: 17
  - name: lightning bolt
    source: Evoker
    level: 3
    count: 2
    DC: 16
  - name: protection from energy
    source: Evoker
    level: 3
  - name: empowered shocking grasp
    source: Evoker
    level: 3
  - name: darkvision
    source: Evoker
    level: 2
  - name: mirror image
    source: Evoker
    level: 2
  - name: protection from arrows
    source: Evoker
    level: 2
  - name: scorching ray
    source: Evoker
    level: 2
    count: 2
  - name: color spray
    source: Evoker
    level: 1
    DC: 14
  - name: expeditious retreat
    source: Evoker
    level: 1
  - name: feather fall
    source: Evoker
    level: 1
  - name: mage armor
    source: Evoker
    level: 1
  - name: shocking grasp
    source: Evoker
    level: 1
    count: 2
  - name: dancing lights
    source: Evoker
    level: 0
  - name: flare
    source: Evoker
    level: 0
    DC: 13
  - name: mage hand
    source: Evoker
    level: 0
  - name: mending
    source: Evoker
    level: 0
  sources:
  - name: Evoker
    type: prepared
    CL: 7
    concentration: 10
    slots:
      0: at-will
    opposition_schools:
    - divination
    - necromancy
tactics:
  Before Combat: The wizard casts mage armor and protection from arrows. If she has
    an ally who attacks in melee, she casts protection from energy (electricity) on
    that ally to protect him from her lightning bolt spells; otherwise, she casts
    it on herself (warding against fire).
  During Combat: The wizard tries to catch multiple opponents with black tentacles,
    then follows up with a lightning bolt to hit as many targets as possible. She
    uses her imp to invisibly deliver shocking grasp and empowered shocking grasp.
  Base Statistics: Without mage armor, the wizard's statistics are AC 15, touch 15,
    flat-footed 12.
ability_scores:
  STR: 6
  DEX: 16
  CON: 12
  INT: 16
  WIS: 13
  CHA: 12
BAB: 3
CMB: 0
CMD: 14
feats:
- name: Combat Casting
- name: Empower Spell
- name: Improved Familiar
- name: Improved Initiative
- name: Iron Will
- name: Scribe Scroll
skills:
  Acrobatics: 5
    when jumping: 1
  Bluff: 6
  Climb: 0
  Knowledge (arcana): 13
  Knowledge (dungeoneering): 9
  Knowledge (engineering): 7
  Knowledge (planes): 8
  Perception: 10
  Spellcraft: 13
  Stealth: 10
  Use Magic Device: 5
languages:
- Common
- Draconic
- Dwarven
- Goblin
- Halfling
- Infernal
special_qualities:
- arcane bond (imp)
gear:
  combat:
  - pearl of power (1st)
  - potion of cure moderate wounds
  - potion of lesser restoration
  - scroll of black tentacles
  - scrolls of invisibility (2)
  - scrolls of lightning bolt (2)
  - scrolls of mirror image (2)
  - scroll of protection from energy
  other:
  - dagger
  - quarterstaff
  - cloak of resistance +1
  - ring of protection +1
  - spellbook
  - 186 gp
desc_long: The thunder wizard manipulates sound and electricity to destroy her enemies.

---

# Thunder Wizard

**Source** NPC Codex pg. 182
**XP** 2,400
Halfling evoker 7

LN Small humanoid (halfling)
**Init** +7; **Senses** Perception +10

##### Defense

**AC** 19, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+4 armor, +1 deflection, +3 Dex, +1 size)
**hp** 37 (7d6+10)
**Fort** +5, **Ref** +7, **Will** +10; +2 vs. _[[universal monster rules/Fear|fear]]_
**DR** 10/magic (ranged weapon attack only; 30 points)

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +2 (1d3–2/19–20) or _[[items/Weapon/Quarterstaff|quarterstaff]]_ +2 (1d4–2)
**Ranged** _dagger_ +7 (1d3–2/19–20)
**Special Attacks** intense spells (+3 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +10)
6/day—force missile (1d4+3)
**Evoker Spells Prepared **(CL 7th; concentration +10)
4th—_[[spells/Black Tentacles|black tentacles]]_, _[[spells/Shout|shout]]_ (DC 17)
3rd—_[[spells/Lightning Bolt|lightning bolt]]_ (2, DC 16), _[[spells/Protection from Energy|protection from energy]]_, empowered _[[spells/Shocking Grasp|shocking grasp]]_
2nd—_[[spells/Darkvision|darkvision]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Protection From Arrows|protection from arrows]]_, _[[spells/Scorching Ray|scorching ray]]_ (2)
1st—_[[spells/Color Spray|color spray]]_ (DC 14), _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Mage Armor|mage armor]]_, _shocking grasp_ (2)
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Flare|flare]]_ (DC 13), _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_
**Opposition Schools **_[[spells/Divination|divination]]_, necromancy

### Tactics

**Before Combat **The _[[classes/Wizard|wizard]]_ casts _mage armor_ and _protection from arrows_. If she has an ally who attacks in melee, she casts _protection from energy_ (electricity) on that ally to protect him from her _lightning bolt_ spells; otherwise, she casts it on herself (_[[items/Armor Magic Abilities/Warding|warding]]_ against fire).
**During Combat **The _wizard_ tries to catch multiple opponents with _black tentacles_, then follows up with a _lightning bolt_ to hit as many targets as possible. She uses her imp to invisibly deliver _shocking grasp_ and empowered _shocking grasp_.
**Base Statistics **Without _mage armor_, the _wizard_’s statistics are **AC **15, touch 15, _flat-footed_ 12.

##### Statistics
**Str** 6, **Dex** 16, **Con** 12, **Int** 16, **Wis** 13, **Cha** 12
**Base Atk** +3; **CMB** +0; **CMD** 14
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Improved Familiar|Improved Familiar]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_
**Skills** Acrobatics +5 (+1 when jumping), Bluff +6, _[[universal monster rules/Climb|Climb]]_ +0, Knowledge (arcana) +13, Knowledge (dungeoneering) +9, Knowledge (engineering) +7, Knowledge (planes) +8, Perception +10, Spellcraft +13, Stealth +10, Use Magic Device +5
**Languages** Common, Draconic, Dwarven, _[[monsters/Goblin|Goblin]]_, Halfling, Infernal
**SQ** arcane bond (imp)
**Combat Gear** pearl of power (1st), potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, potion of lesser _[[spells/Restoration|restoration]]_, scroll of _black tentacles_, scrolls of _[[spells/Invisibility|invisibility]]_ (2), scrolls of _lightning bolt_ (2), scrolls of _mirror image_ (2), scroll of _protection from energy_; **Other Gear** _dagger_, _quarterstaff_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Mundane/Spellbook|spellbook]]_, 186 gp

The _[[npcs/Thunder Wizard|thunder wizard]]_ manipulates sound and electricity to destroy her enemies.
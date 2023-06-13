---
cssclass: [monsters]
title1: Troglodyte, Troglodyte Chieftain
title2: Troglodyte Chieftain
CR: 8
sources:
- name: Monster Codex
  page: 217
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 4800
race: Troglodyte
classes:
- barbarian 2
- druid (cave druid) 6 (Pathfinder RPG Advanced Player's Guide 99)
alignment: CE
size: Medium
type: humanoid
subtypes:
- reptilian
initiative:
  bonus: 4
senses:
  darkvision: 90
auras:
- name: stench
  radius: 30
  DC: 14
  duration: 10 rounds
AC:
  AC: 21
  touch: 11
  flat_footed: 21
  components:
    armor: 4
    natural: 9
    rage: -2
HP:
  HP: 100
  long: 8d8+2d12+46
  HD: 10
saves:
  fort: 14
  ref: 4
  will: 10
  other: +2 vs. abilities of aberrations and oozes
defensive_abilities:
- uncanny dodge
resistances:
  fire: 10
speeds:
  base: 50
attacks:
  melee:
  - - text: +1 greataxe +15/+10 (1d12+8/×3)
      entries:
      - - damage: 1d12+8
          crit_multiplier: 3
      attack: +1 greataxe
      bonus:
      - 15
      - 10
    - text: +1 bite +10 (1d4+4)
      entries:
      - - damage: 1d4+4
      attack: +1 bite
      bonus:
      - 10
  - - text: +1 bite +15 (1d4+8)
      entries:
      - - damage: 1d4+8
      attack: +1 bite
      bonus:
      - 15
    - text: 2 +1 claws +15 (1d4+8)
      entries:
      - - damage: 1d4+8
      count: 2
      attack: +1 claws
      bonus:
      - 15
  ranged:
  - - text: javelin +7 (1d6+7)
      entries:
      - - damage: 1d6+7
      attack: javelin
      bonus:
      - 7
  special:
  - fire bolt (1d6+3 fire, 6/day)
  - rage (7 rounds/day)
  - rage powers (moment of clarity)
  - wild shape 1/day (can adopt ooze form but not plant form)
spells:
  entries:
  - is_domain_spell: true
    name: fireball
    source: Druid
    level: 3
    DC: 16
  - name: greater magic fang
    source: Druid
    level: 3
    count: 2
  - name: swarm of fangs
    source: Druid
    level: 3
    DC: 16
  - name: barkskin
    source: Druid
    level: 2
  - name: bull's strength
    source: Druid
    level: 2
    count: 2
  - is_domain_spell: true
    name: produce flame
    source: Druid
    level: 2
  - superscripts:
    - APG
    name: stone call
    source: Druid
    level: 2
  - is_domain_spell: true
    name: burning hands
    source: Druid
    level: 1
    DC: 14
  - name: cure light wounds
    source: Druid
    level: 1
    count: 2
  - name: longstrider
    source: Druid
    level: 1
  - name: pass without trace
    source: Druid
    level: 1
  - name: create water
    source: Druid
    level: 0
  - name: detect magic
    source: Druid
    level: 0
  - name: know direction
    source: Druid
    level: 0
  - name: mending
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 6
    concentration: 9
    slots:
      0: at-will
    domains:
    - fire
tactics:
  Before Combat: The chieftain casts bull's strength and greater magic fang on both
    himself and one ally, then casts barkskin on himself.
  During Combat: While his enemies are still at range, the chieftain casts swarm of
    fangs, stone call, and other attack spells. When cornered in melee, he rages and
    attacks with his greataxe.
  Base Statistics: When he's not raging, and without barkskin, bull's strength, and
    greater magic fang, the chieftain's statistics are AC 20, touch 13, flat-footed
    20; hp 84; Fort +12, Will +8; Melee +1 greataxe +13/+8 (1d12+6/×3), bite +7 (1d4+2)
    or bite +12 (1d4+5), 2 claws +12 (1d4+5); Ranged javelin +7 (1d6+7); Str 16, Con
    13; CMB +12, CMD 22.
ability_scores:
  STR: 24
  DEX: 11
  CON: 17
  INT: 10
  WIS: 16
  CHA: 13
BAB: 7
CMB: 14
CMD: 22
feats:
- name: Combat Casting
- name: Improved Initiative
- name: Lightning Reflexes
- name: Power Attack
- name: Toughness
skills:
  Diplomacy: 7
  Intimidate: 10
  Knowledge (dungeoneering): 2
  Knowledge (religion): 6
  Perception: 12
  Sense Motive: 9
  Spellcraft: 9
  Stealth: 3
  Survival: 5
languages:
- Draconic
- Druidic
special_qualities:
- fast movement
- lightfoot
- nature bond (Fire domain)
- nature sense
- tunnelrunner
- wild empathy +7 (influence oozes, not magical beasts)
gear:
  combat:
  - potions of cure moderate wounds (2)
  - scroll of meld with stone
  other:
  - mwk chain shirt
  - +1 greataxe
  - javelins (5)
  - belt of incredible dexterity +2
  - bag of gemstones
ecology:
  environment: any underground
desc_long: Most ferocious troglodyte chieftains earn their positions by killing and
  eating their predecessors. Almost all chieftains practice some form of divine magic,
  and they must be strong-and cruel-to reign over their fractious, savage tribes.
  Troglodyte chieftains often wear fine metal items claimed from other creatures that
  they or their subjects have killed.

---

# Troglodyte, Troglodyte Chieftain

**Source** Monster Codex pg. 217
**XP** 4,800
_[[monsters/Troglodyte|Troglodyte]]_ _[[classes/Barbarian|barbarian]]_ 2/druid (cave _[[classes/Druid|druid]]_) 6 (Pathfinder RPG Advanced Player’s Guide 99)
CE Medium humanoid (reptilian)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 90 ft.; Perception +12
**Aura** _[[universal monster rules/Stench|stench]]_ (30 ft., DC 14, 10 rounds)

##### Defense

**AC** 21, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+4 armor, +9 natural, –2 _[[spells/Rage|rage]]_)
**hp** 100 (10 HD; 8d8+2d12+46)
**Fort** +14, **Ref** +4, **Will** +10; +2 vs. abilities of aberrations and oozes
**Defensive Abilities** uncanny _[[feats/Dodge|dodge]]_; **Resist** fire 10

##### Offense
**Speed** 50 ft.
**Melee** +1 _[[items/Weapon/Greataxe|greataxe]]_ +15/+10 (1d12+8/×3), +1 bite +10 (1d4+4) or +1 bite +15 (1d4+8), 2 +1 claws +15 (1d4+8)
**Ranged** _[[items/Weapon/Javelin|javelin]]_ +7 (1d6+7)
**Special Attacks** fire bolt (1d6+3 fire, 6/day), _rage_ (7 rounds/day), _rage_ powers (moment of _[[items/Weapon/Clarity|clarity]]_), wild shape 1/day (can adopt ooze form but not plant form)
**_Druid_ Spells Prepared **(CL 6th; concentration +9)
3rd—_[[spells/Fireball|fireball]]_ (DC 16), greater _[[spells/Magic Fang|magic fang]]_ (2), _[[spells/Swarm Of Fangs|swarm of fangs]]_ (DC 16)
2nd—_[[spells/Barkskin|barkskin]]_, bull’s strength (2), _[[spells/Produce Flame|produce flame]]_, _[[spells/Stone Call|stone call]]_
1st—_[[spells/Burning Hands|burning hands]]_ (DC 14), _[[spells/Cure Light Wounds|cure light wounds]]_ (2), _[[spells/Longstrider|longstrider]]_, _[[spells/Pass without Trace|pass without trace]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Know Direction|know direction]]_, _[[spells/Mending|mending]]_
**D** domain spell; **Domain** Fire

### Tactics

**Before Combat** The chieftain casts bull’s strength and greater _magic fang_ on both himself and one ally, then casts _barkskin_ on himself.
 **During Combat** While his enemies are still at range, the chieftain casts _swarm of fangs_, _stone call_, and other attack spells. When cornered in melee, he rages and attacks with his _greataxe_.
 **Base Statistics** When he’s not raging, and without _barkskin_, bull’s strength, and greater _magic fang_, the chieftain’s statistics are **AC** 20, touch 13, _flat-footed_ 20; **hp** 84; **Fort** +12, **Will** +8; **Melee** +1 _greataxe_ +13/+8 (1d12+6/×3), bite +7 (1d4+2) or bite +12 (1d4+5), 2 claws +12 (1d4+5); **Ranged** _javelin_ +7 (1d6+7); **Str **16, **Con **13; **CMB **+12, **CMD **22.

##### Statistics
**Str** 24, **Dex** 11, **Con** 17, **Int** 10, **Wis** 16, **Cha** 13
**Base Atk** +7; **CMB** +14; **CMD** 22
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_
**Skills** Diplomacy +7, Intimidate +10, Knowledge (dungeoneering) +2, Knowledge (religion) +6, Perception +12, Sense Motive +9, Spellcraft +9, Stealth +3, Survival +5
**Languages** Draconic, Druidic
**SQ** fast movement, lightfoot, nature bond (Fire domain), nature sense, tunnelrunner, wild _[[feats/Empathy|empathy]]_ +7 (influence oozes, not magical beasts)
**Combat Gear** potions of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (2), scroll of meld with stone; **Other Gear** mwk _[[items/Armor/Chain shirt|chain shirt]]_, +1 _greataxe_, javelins (5), _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, bag of gemstones

##### Ecology

**Environment** any underground

##### Description

Most ferocious _troglodyte_ chieftains earn their positions by killing and eating their predecessors. Almost all chieftains practice some form of divine magic, and they must be strong—and _[[items/Weapon Magic Abilities/Cruel|cruel]]_—to reign over their fractious, savage tribes. _Troglodyte_ chieftains often wear fine metal items claimed from other creatures that they or their subjects have killed.
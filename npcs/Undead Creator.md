---
cssclass: [monsters]
title1: Undead Creator
title2: Undead Creator
CR: 10
sources:
- name: NPC Codex
  page: 186
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 9600
race: Human
classes:
- necromancer 11
alignment: LN
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 5
senses:
  darkvision: 60
  see invisibility: true
AC:
  AC: 16
  touch: 11
  flat_footed: 15
  components:
    armor: 4
    dex: 1
    natural: 1
HP:
  HP: 100
  long: 11d6+59
saves:
  fort: 10
  ref: 6
  will: 10
resistances:
  fire: 30
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk dagger +6 (1d4/19-20)
      entries:
      - - damage: 1d4
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 6
  special:
  - channel negative energy (DC 17, 8/day)
spell_like_abilities:
  entries:
  - name: grave touch
    source: default
    freq: 8/day
    other: 5 rounds
  sources:
  - name: default
    CL: 11
    concentration: 16
spells:
  entries:
  - name: create undead
    source: Necromancer
    level: 6
  - name: eyebite
    source: Necromancer
    level: 6
    DC: 23
  - name: baleful polymorph
    source: Necromancer
    level: 5
    DC: 20
  - name: magic jar
    source: Necromancer
    level: 5
    DC: 22
  - name: teleport
    source: Necromancer
    level: 5
  - name: waves of fatigue
    source: Necromancer
    level: 5
  - name: animate dead
    source: Necromancer
    level: 4
  - name: enervation
    source: Necromancer
    level: 4
  - name: fear
    source: Necromancer
    level: 4
    DC: 21
  - name: solid fog
    source: Necromancer
    level: 4
  - name: wall of fire
    source: Necromancer
    level: 4
  - name: blink
    source: Necromancer
    level: 3
  - name: fireball
    source: Necromancer
    level: 3
    DC: 18
  - name: fly
    source: Necromancer
    level: 3
  - name: ray of exhaustion
    source: Necromancer
    level: 3
    DC: 20
  - name: vampiric touch
    source: Necromancer
    level: 3
    count: 2
  - name: blindness/deafness
    source: Necromancer
    level: 2
    DC: 19
  - name: false life
    source: Necromancer
    level: 2
  - name: resist energy
    source: Necromancer
    level: 2
  - name: see invisibility
    source: Necromancer
    level: 2
  - name: scare
    source: Necromancer
    level: 2
    DC: 19
  - name: scorching ray
    source: Necromancer
    level: 2
  - name: alarm
    source: Necromancer
    level: 1
  - name: burning hands
    source: Necromancer
    level: 1
    DC: 16
  - name: cause fear
    source: Necromancer
    level: 1
    DC: 18
  - name: detect undead
    source: Necromancer
    level: 1
  - name: expeditious retreat
    source: Necromancer
    level: 1
  - name: mage armor
    source: Necromancer
    level: 1
  - name: magic missile
    source: Necromancer
    level: 1
  - name: bleed
    source: Necromancer
    level: 0
    DC: 17
  - name: detect magic
    source: Necromancer
    level: 0
  - name: read magic
    source: Necromancer
    level: 0
  - name: touch of fatigue
    source: Necromancer
    level: 0
    DC: 17
  sources:
  - name: Necromancer
    type: prepared
    CL: 11
    concentration: 16
    slots:
      0: at-will
    opposition_schools:
    - enchantment
    - illusion
tactics:
  Before Combat: The wizard casts mage armor, false life, resist energy (fire), and
    see invisibility.
  During Combat: The wizard casts solid fog on a group of enemies, then casts wall
    of fire in a circle (focused inward) around the solid fog. As opponents leave
    the fog, he attacks them directly with eyebite and enervation. He might cast fear
    to drive opponents through the wall of fire, or cast fireball on a group of opponents
    grouped together.
  Base Statistics: Without false life, mage armor, resist energy, and see invisibility,
    the wizard's statistics are Senses darkvision 60 ft.; AC 12, touch 11, flat-footed
    11; hp 85; Resist none.
ability_scores:
  STR: 10
  DEX: 12
  CON: 16
  INT: 20
  WIS: 8
  CHA: 14
BAB: 5
CMB: 5
CMD: 16
feats:
- name: Brew Potion
- name: Combat Casting
- name: Command Undead
- name: Craft Wondrous Item
- name: Greater Spell Focus (necromancy)
- name: Improved Channel
- name: Improved Initiative
- name: Iron Will
- name: Scribe Scroll
- name: Spell Focus (necromancy)
- name: Toughness
skills:
  Craft (alchemy): 19
  Fly: 5
  Heal: 4
  Intimidate: 7
  Knowledge (arcana): 19
  Knowledge (dungeoneering): 13
  Knowledge (engineering): 13
  Knowledge (geography): 13
  Knowledge (history): 13
  Knowledge (local): 13
  Knowledge (nature): 13
  Knowledge (nobility): 13
  Knowledge (planes): 13
  Knowledge (religion): 18
  Perception: 4
  Spellcraft: 19
languages:
- Aklo
- Common
- Dwarven
- Elven
- Goblin
- Infernal
special_qualities:
- arcane bond (rat)
- life sight (10 feet, 11 rounds/day)
gear:
  combat:
  - potions of cure moderate wounds (2)
  - potion of displacement
  - potion of invisibility
  - robe of bones
  other:
  - masterwork dagger
  - amulet of natural armor +1
  - belt of mighty constitution +2
  - cloak of resistance +2
  - goggles of night
  - headband of vast intelligence +2
  - spellbook
  - crystal for magic jar (worth 100 gp)
  - onyx gems (worth 300 gp)
  - 623 gp
desc_long: The undead creator dispassionately crafts unlife out of dead flesh and
  bone.

---

# Undead Creator

**Source** NPC Codex pg. 186
**XP** 9,600
Human necromancer 11

LN Medium humanoid (human)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/See Invisibility|see invisibility]]_; Perception +4

##### Defense

**AC** 16, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 armor, +1 Dex, +1 natural)
**hp** 100 (11d6+59)
**Fort** +10, **Ref** +6, **Will** +10
**Resist** fire 30

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Dagger|dagger]]_ +6 (1d4/19–20)
**Special Attacks** channel negative energy (DC 17, 8/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +16)
8/day—grave touch (5 rounds)
**Necromancer Spells Prepared **(CL 11th; concentration +16)
6th—_[[spells/Create Undead|create undead]]_, _[[spells/Eyebite|eyebite]]_ (DC 23)
5th—_[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 20), _[[spells/Magic Jar|magic jar]]_ (DC 22), teleport, _[[spells/Waves of Fatigue|waves of fatigue]]_
4th—_[[spells/Animate Dead|animate dead]]_, _[[spells/Enervation|enervation]]_, _[[universal monster rules/Fear|fear]]_ (DC 21), _[[spells/Solid Fog|solid fog]]_, _[[spells/Wall Of Fire|wall of fire]]_
3rd—_[[spells/Blink|blink]]_, _[[spells/Fireball|fireball]]_ (DC 18), fly, _[[spells/Ray of Exhaustion|ray of exhaustion]]_ (DC 20), _[[spells/Vampiric Touch|vampiric touch]]_ (2)
2nd—blindness/deafness (DC 19), _[[spells/False Life|false life]]_, _[[spells/Resist Energy|resist energy]]_, _see invisibility_, _[[spells/Scare|scare]]_ (DC 19), _[[spells/Scorching Ray|scorching ray]]_
1st—_[[spells/Alarm|alarm]]_, _[[spells/Burning Hands|burning hands]]_ (DC 16), _[[spells/Cause Fear|cause fear]]_ (DC 18), _[[spells/Detect Undead|detect undead]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 17), _[[spells/Detect Magic|detect magic]]_, _[[spells/Read Magic|read magic]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 17)
**Opposition Schools **enchantment, illusion

### Tactics

**Before Combat **The _[[classes/Wizard|wizard]]_ casts _mage armor_, _false life_, _resist energy_ (fire), and _see invisibility_.
**During Combat **The _wizard_ casts _solid fog_ on a group of enemies, then casts _wall of fire_ in a circle (focused inward) around the _solid fog_. As opponents leave the fog, he attacks them directly with _eyebite_ and _enervation_. He might cast _fear_ to drive opponents through the _wall of fire_, or cast _fireball_ on a group of opponents grouped together.
**Base Statistics **Without _false life_, _mage armor_, _resist energy_, and _see invisibility_, the _wizard_’s statistics are **Senses **_darkvision_ 60 ft.; **AC **12, touch 11, _flat-footed_ 11; **hp **85; **Resist **none.

##### Statistics
**Str** 10, **Dex** 12, **Con** 16, **Int** 20, **Wis** 8, **Cha** 14
**Base Atk** +5; **CMB** +5; **CMD** 16
**Feats** _[[feats/Brew Potion|Brew Potion]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[spells/Command Undead|Command Undead]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (necromancy), _[[feats/Improved Channel|Improved Channel]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Focus|Spell Focus]]_ (necromancy), _[[feats/Toughness|Toughness]]_
**Skills** Craft (alchemy) +19, Fly +5, _[[spells/Heal|Heal]]_ +4, Intimidate +7, Knowledge (arcana) +19, Knowledge (dungeoneering, engineering, geography, history, local, nature, nobility, planes) +13, Knowledge (religion) +18, Perception +4, Spellcraft +19
**Languages** Aklo, Common, Dwarven, Elven, _[[monsters/Goblin|Goblin]]_, Infernal
**SQ** arcane bond (rat), life sight (10 feet, 11 rounds/day)
**Combat Gear** potions of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (2), potion of _[[spells/Displacement|displacement]]_, potion of _[[spells/Invisibility|invisibility]]_, _[[items/Wondrous Item/Robe of Bones|robe of bones]]_; **Other Gear** masterwork _dagger_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Mighty Constitution +2|belt of mighty constitution +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Goggles of Night|goggles of night]]_, _[[items/Wondrous Item/Headband of Vast Intelligence +2|headband of vast intelligence +2]]_, _[[items/Mundane/Spellbook|spellbook]]_, crystal for _magic jar_ (worth 100 gp), onyx gems (worth 300 gp), 623 gp

The _[[npcs/Undead Creator|undead creator]]_ dispassionately crafts unlife out of dead flesh and bone.
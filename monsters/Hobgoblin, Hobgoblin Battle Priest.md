---
cssclass: [monsters]
title1: Hobgoblin, Hobgoblin Battle Priest
title2: Hobgoblin Battle Priest
CR: 8
sources:
- name: Monster Codex
  page: 121
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 4800
race: Hobgoblin
classes:
- cleric 9
alignment: LE
size: Medium
type: humanoid
subtypes:
- goblinoid
initiative:
  bonus: 0
senses:
  darkvision: 60
AC:
  AC: 18
  touch: 10
  flat_footed: 18
  components:
    armor: 8
HP:
  HP: 71
  long: 9d8+27
saves:
  fort: 9
  ref: 4
  will: 10
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 morningstar +9/+4 (1d8+3)
      entries:
      - - damage: 1d8+3
      attack: +1 morningstar
      bonus:
      - 9
      - 4
  ranged:
  - - text: mwk heavy crossbow +7 (1d10/19-20)
      entries:
      - - damage: 1d10
          crit_range: 19-20
      attack: mwk heavy crossbow
      bonus:
      - 7
  special:
  - channel negative energy 6/day (DC 19, 5d6)
  - staff of order (4 rounds, 1/day)
  - weapon master (9 rounds/day)
spell_like_abilities:
  entries:
  - name: battle rage
    source: default
    freq: 6/day
    other: '+4'
  - name: touch of law
    source: default
    freq: 6/day
  sources:
  - name: default
    CL: 9
    concentration: 12
spells:
  entries:
  - is_domain_spell: true
    name: flame strike
    source: Cleric
    level: 5
    DC: 18
  - name: righteous might
    source: Cleric
    level: 5
  - superscripts:
    - APG
    name: blessing of fervor
    source: Cleric
    level: 4
  - name: cure critical wounds
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: divine power
    source: Cleric
    level: 4
  - name: blindness/deafness
    source: Cleric
    level: 3
    DC: 16
  - name: cure serious wounds
    source: Cleric
    level: 3
  - name: dispel magic
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: magic circle against chaos
    source: Cleric
    level: 3
  - name: prayer
    source: Cleric
    level: 3
  - name: aid
    source: Cleric
    level: 2
  - name: bear's endurance
    source: Cleric
    level: 2
  - name: death knell
    source: Cleric
    level: 2
    DC: 15
  - name: lesser restoration
    source: Cleric
    level: 2
  - name: sound burst
    source: Cleric
    level: 2
    DC: 15
  - is_domain_spell: true
    name: spiritual weapon
    source: Cleric
    level: 2
  - name: bless
    source: Cleric
    level: 1
  - name: entropic shield
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: magic weapon
    source: Cleric
    level: 1
  - name: remove fear
    source: Cleric
    level: 1
    count: 2
  - name: shield of faith
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 13
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: stabilize
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 9
    concentration: 12
    slots:
      0: at-will
    domains:
    - law
    - war
tactics:
  During Combat: The battle priest casts righteous might immediately, trusting that
    it will protect her and make her a beacon for her allies, then casts blessing
    of fervor to bolster her allies. After that, she begins to antagonize her foes,
    typically starting by casting blindness/deafness against an enemy commander.
ability_scores:
  STR: 14
  DEX: 10
  CON: 14
  INT: 10
  WIS: 16
  CHA: 16
BAB: 6
CMB: 8
CMD: 18
feats:
- name: Combat Casting
- name: Heavy Armor Proficiency
- name: Improved Channel
- name: Selective Channeling
- name: Toughness
skills:
  Heal: 15
  Knowledge (religion): 12
  Spellcraft: 12
  Stealth: -2
  Perception: 3
languages:
- Common
- Goblin
gear:
  combat:
  - wand of cure moderate wounds (10 charges)
  - acid (2)
  - alchemist's fire (2)
  - antitoxin
  other:
  - +1 splint mail
  - +1 morningstar
  - mwk heavy crossbow with 20 bolts
  - cloak of resistance +1
  - headband of alluring charisma +2
  - spell component pouch
  - unholy symbol
  - 24 gp
ecology:
  environment: temperate hills
desc_long: |-
  Battle priests' augmentations to their allies' strength, stamina, precision, and speed are vital to many hobgoblin tactics, and as such the clerics often serve as trusted advisors to commanders, consulting to determine what magical support would best serve the tactical situation.

   Like all hobgoblins, battle priests live for the adrenaline rush of open warfare, and during the heat of a skirmish they often turn their attention away from their allies-it is the task of the soldier to survive and drive his enemy before him, and a battle priest sees it as coddling weakness to tend to wounds among those soldiers not strong enough to grasp their own victory. Rather, battle priests employ their magic to debilitate their foes, channeling the wrath of their gods of war upon those who oppose them.

---

# Hobgoblin, Hobgoblin Battle Priest

**Source** Monster Codex pg. 121
**XP** 4,800
_[[monsters/Hobgoblin|Hobgoblin]]_ _[[classes/Cleric|cleric]]_ 9

LE Medium humanoid (goblinoid)
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +3

##### Defense

**AC** 18, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+8 armor)
**hp** 71 (9d8+27)
**Fort** +9, **Ref** +4, **Will** +10

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Morningstar|morningstar]]_ +9/+4 (1d8+3)
**Ranged** mwk _[[items/Weapon/Heavy crossbow|heavy crossbow]]_ +7 (1d10/19–20)
**Special Attacks** channel negative energy 6/day (DC 19, 5d6), staff of order (4 rounds, 1/day), weapon master (9 rounds/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +12)
6/day—battle _[[spells/Rage|rage]]_ (+4), touch of law
**_Cleric_ Spells Prepared **(CL 9th; concentration +12)
5th—_[[spells/Flame Strike|flame strike]]_ (DC 18), _[[spells/Righteous Might|righteous might]]_
4th—_[[spells/Blessing Of Fervor|blessing of fervor]]_, _[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Divine Power|divine power]]_
3rd—blindness/deafness (DC 16), _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Magic Circle against Chaos|magic circle against chaos]]_, _[[spells/Prayer|prayer]]_
2nd—aid, bear’s _[[feats/Endurance|endurance]]_, _[[spells/Death Knell|death knell]]_ (DC 15), lesser _[[spells/Restoration|restoration]]_, _[[spells/Sound Burst|sound burst]]_ (DC 15), _[[spells/Spiritual Weapon|spiritual weapon]]_
1st—_[[spells/Bless|bless]]_, _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Remove Fear|remove fear]]_ (2), _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, stabilize
**D** domain spell; **Domains** Law, War

### Tactics

**During Combat** The battle priest casts _righteous might_ immediately, trusting that it will protect her and make her a beacon for her allies, then casts _blessing of fervor_ to bolster her allies. After that, she begins to _[[feats/Antagonize|antagonize]]_ her foes, typically starting by casting blindness/deafness against an enemy commander.

##### Statistics
**Str** 14, **Dex** 10, **Con** 14, **Int** 10, **Wis** 16, **Cha** 16
**Base Atk** +6; **CMB** +8; **CMD** 18
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Heavy Armor Proficiency|Heavy Armor Proficiency]]_, _[[feats/Improved Channel|Improved Channel]]_, _[[feats/Selective Channeling|Selective Channeling]]_, _[[feats/Toughness|Toughness]]_
**Skills** _[[spells/Heal|Heal]]_ +15, Knowledge (religion) +12, Spellcraft +12, Stealth –2
**Languages** Common, _[[monsters/Goblin|Goblin]]_
**Combat Gear** wand of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (10 charges), acid (2), _[[classes/Alchemist|alchemist]]_’s fire (2), _[[items/Mundane/Antitoxin|antitoxin]]_; **Other Gear** +1 _[[items/Armor/Splint mail|splint mail]]_, +1 _morningstar_, mwk _heavy crossbow_ with 20 bolts, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol, 24 gp

##### Ecology

**Environment** temperate hills

##### Description

Battle priests’ augmentations to their allies’ strength, stamina, precision, and speed are vital to many _hobgoblin_ tactics, and as such the clerics often serve as trusted advisors to commanders, consulting to determine what magical support would best serve the tactical situation.

Like all hobgoblins, battle priests live for the adrenaline rush of open warfare, and during the _[[universal monster rules/Heat|heat]]_ of a skirmish they often turn their attention away from their allies—it is the task of the soldier to survive and drive his enemy before him, and a battle priest sees it as coddling weakness to tend to wounds among those soldiers not strong enough to _[[spells/Grasp|grasp]]_ their own victory. Rather, battle priests employ their magic to debilitate their foes, _[[items/Armor Magic Abilities/Channeling|channeling]]_ the wrath of their gods of war upon those who oppose them.
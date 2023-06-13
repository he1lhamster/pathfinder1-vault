---
cssclass: [monsters]
title1: Ghoul, Ghoul Monarch
title2: Ghoul Monarch
CR: 12
sources:
- name: Monster Codex
  page: 87
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 19200
race: Ghoul
classes:
- sorcerer 12
alignment: CE
size: Medium
type: undead
initiative:
  bonus: 10
senses:
  darkvision: 60
AC:
  AC: 23
  touch: 17
  flat_footed: 17
  components:
    armor: 4
    deflection: 1
    dex: 6
    natural: 2
HP:
  HP: 176
  long: 2d8+12d6+125
  HD: 14
saves:
  fort: 10
  ref: 12
  will: 14
defensive_abilities:
- channel resistance +2
- nondetection
immunities:
- undead traits
resistances:
  cold: 10
speeds:
  base: 30
  burrow: 10
attacks:
  melee:
  - - text: bite +13 (1d6+1 plus disease and paralysis)
      entries:
      - - damage: 1d6+1
        - effect: disease
        - effect: paralysis
      attack: bite
      bonus:
      - 13
    - text: 2 claws +13 (1d6+1 plus paralysis)
      entries:
      - - damage: 1d6+1
        - effect: paralysis
      count: 2
      attack: claws
      bonus:
      - 13
  special:
  - disease (DC 23)
  - paralysis (1d4+1 rounds, DC 23, elves are immune to this effect)
  - ravenous frenzy (12/day)
spells:
  entries:
  - name: mislead
    source: Sorcerer
    level: 6
    DC: 22
  - name: move earth
    source: Sorcerer
    level: 6
  - name: dominate person
    source: Sorcerer
    level: 5
    DC: 21
  - name: hungry earth
    source: Sorcerer
    level: 5
    DC: 21
  - superscripts:
    - APG
    name: suffocation
    source: Sorcerer
    level: 5
    DC: 21
  - name: beast shape II
    source: Sorcerer
    level: 4
  - name: black tentacles
    source: Sorcerer
    level: 4
  - name: dimension door
    source: Sorcerer
    level: 4
  - name: fear
    source: Sorcerer
    level: 4
  - name: gaseous form
    source: Sorcerer
    level: 3
  - name: lightning bolt
    source: Sorcerer
    level: 3
    DC: 19
  - name: nondetection
    source: Sorcerer
    level: 3
  - name: stinking cloud
    source: Sorcerer
    level: 3
    DC: 19
  - name: vampiric touch
    source: Sorcerer
    level: 3
  - name: alter self
    source: Sorcerer
    level: 2
  - name: command undead
    source: Sorcerer
    level: 2
    DC: 18
  - name: false life
    source: Sorcerer
    level: 2
  - superscripts:
    - APG
    name: feast of ashes
    source: Sorcerer
    level: 2
    DC: 18
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: mirror image
    source: Sorcerer
    level: 2
  - name: burning hands
    source: Sorcerer
    level: 1
    DC: 17
  - name: grease
    source: Sorcerer
    level: 1
    DC: 17
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: obscuring mist
    source: Sorcerer
    level: 1
  - name: ray of enfeeblement
    source: Sorcerer
    level: 1
    DC: 17
  - name: silent image
    source: Sorcerer
    level: 1
  - name: arcane mark
    source: Sorcerer
    level: 0
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: daze
    source: Sorcerer
    level: 0
    DC: 16
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: light
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
    DC: 16
  - name: ray of frost
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 12
    concentration: 18
    slots:
      6: 4
      5: 6
      4: 7
      3: 7
      2: 8
      1: 8
      0: at-will
    bloodline: ghoul
tactics:
  Before Combat: Before combat, the monarch casts false life, mage armor, and nondetection
    on herself.
  During Combat: A ghoul monarch avoids direct confrontation unless she can fight
    using dominate person or magic jar. The ghoul monarch starts combat by casting
    quickened grease and hungry earth, trapping as many spellcasters as she can in
    the effect. If the monarch has minions, she focuses on disabling and keeping enemies
    off guard rather than using direct damage spells. She targets powerful spellcasters
    with suffocation or black tentacles.
  Morale: A ghoul monarch flees to a safe haven or attempts to flee by burrowing underground
    at the first sign she is in serious danger.
  Base Statistics: Without false life, mage armor, and nondetection, the monarch's
    statistics are AC 19, touch 17, flat-footed 13; hp 161; Defensive Abilities channel
    resistance +2.
ability_scores:
  STR: 13
  DEX: 22
  CON:
  INT: 15
  WIS: 16
  CHA: 22
BAB: 7
CMB: 8
CMD: 25
feats:
- name: Eschew Materials
- name: Improved Initiative
- name: Lightning Reflexes
- name: Old as Dirt
- name: Quicken Spell
- name: Sleeper
- name: Toughness
- name: Warren Digger
- name: Weapon Finesse
skills:
  Bluff: 13
  Intimidate: 23
  Perception: 20
  Spellcraft: 19
  Stealth: 28
languages:
- Common
- Draconic
- Undercommon
special_qualities:
- bloodline arcana (heal when casting necromancy spells)
gear:
  combat:
  - potions of inflict moderate wounds (2)
  - scroll of magic jar
  - scroll of teleport
  other:
  - +2 silken ceremonial armor
  - belt of incredible dexterity +2
  - headband of alluring charisma +2
  - ring of protection +1
  - stalker's mask
  - 470 gp
ecology:
  environment: any land
desc_long: These ancient sorcerers have attained their power by using those around
  them as puppets. They command mortals and undead using both their magic and force
  of personality.

---

# Ghoul, Ghoul Monarch

**Source** Monster Codex pg. 87
**XP** 19,200
_[[monsters/Ghoul|Ghoul]]_ _[[classes/Sorcerer|sorcerer]]_ 12
CE Medium undead
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +20

##### Defense

**AC** 23, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+4 armor, +1 _[[spells/Deflection|deflection]]_, +6 Dex, +2 natural)
**hp** 176 (14 HD; 2d8+12d6+125)
**Fort** +10, **Ref** +12, **Will** +14
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +2, _[[spells/Nondetection|nondetection]]_; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** cold 10

##### Offense
**Speed** 30 ft., _[[universal monster rules/Burrow|burrow]]_ 10 ft.
**Melee** bite +13 (1d6+1 plus disease and _[[universal monster rules/Paralysis|paralysis]]_), 2 claws +13 (1d6+1 plus _paralysis_)
**Special Attacks** disease (DC 23), _paralysis_ (1d4+1 rounds, DC 23, elves are immune to this effect), _[[curses/Ravenous|ravenous]]_ frenzy (12/day)
**_Sorcerer_ Spells Known **(CL 12th; concentration +18)
6th (4/day)—_[[spells/Mislead|mislead]]_ (DC 22), _[[spells/Move Earth|move earth]]_
5th (6/day)—_[[spells/Dominate Person|dominate person]]_ (DC 21), _[[spells/Hungry Earth|hungry earth]]_ (DC 21), _[[spells/Suffocation|suffocation]]_ (DC 21)
4th (7/day)—_[[spells/Beast Shape II|beast shape II]]_, _[[spells/Black Tentacles|black tentacles]]_, _[[spells/Dimension Door|dimension door]]_, _[[universal monster rules/Fear|fear]]_
3rd (7/day)—_[[spells/Gaseous Form|gaseous form]]_, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 19), _nondetection_, _[[spells/Stinking Cloud|stinking cloud]]_ (DC 19), _[[spells/Vampiric Touch|vampiric touch]]_
2nd (8/day)—_[[spells/Alter Self|alter self]]_, _[[spells/Command Undead|command undead]]_ (DC 18), _[[spells/False Life|false life]]_, _[[spells/Feast Of Ashes|feast of ashes]]_ (DC 18), _[[spells/Invisibility|invisibility]]_, _[[spells/Mirror Image|mirror image]]_
1st (8/day)—_[[spells/Burning Hands|burning hands]]_ (DC 17), _[[spells/Grease|grease]]_ (DC 17), _[[spells/Mage Armor|mage armor]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 17), _[[spells/Silent Image|silent image]]_
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 16), _[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Prestidigitation|prestidigitation]]_ (DC 16), _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_
**Bloodline** _ghoul_

### Tactics

**Before Combat** Before combat, the monarch casts _false life_, _mage armor_, and _nondetection_ on herself.
 **During Combat** A _ghoul_ monarch avoids direct confrontation unless she can fight using _dominate person_ or _[[spells/Magic Jar|magic jar]]_. The _ghoul_ monarch starts combat by casting quickened _grease_ and _hungry earth_, trapping as many spellcasters as she can in the effect. If the monarch has minions, she focuses on disabling and keeping enemies off _[[npcs/Guard|guard]]_ rather than using direct damage spells. She targets powerful spellcasters with _suffocation_ or _black tentacles_.
 **Morale** A _ghoul_ monarch flees to a safe haven or attempts to flee by burrowing underground at the first sign she is in serious danger.
 **Base Statistics** Without _false life_, _mage armor_, and _nondetection_, the monarch’s statistics are **AC **19, touch 17, _flat-footed_ 13; **hp **161; **Defensive Abilities** _channel resistance_ +2.

##### Statistics
**Str** 13, **Dex** 22, **Con** —, **Int** 15, **Wis** 16, **Cha** 22
**Base Atk** +7; **CMB** +8; **CMD** 25
**Feats** _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, Old as Dirt, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Sleeper|Sleeper]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Warren Digger|Warren Digger]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +13, Intimidate +23, Perception +20, Spellcraft +19, Stealth +28
**Languages** Common, Draconic, Undercommon
**SQ** bloodline arcana (_[[spells/Heal|heal]]_ when casting necromancy spells)
**Combat Gear** potions of _[[spells/Inflict Moderate Wounds|inflict moderate wounds]]_ (2), scroll of _magic jar_, scroll of teleport; **Other Gear** +2 _[[items/Armor/Silken ceremonial armor|silken ceremonial armor]]_, _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, stalker’s _[[items/Mundane/Mask|mask]]_, 470 gp

##### Ecology

**Environment** any land

##### Description

These ancient sorcerers have attained their power by using those around them as puppets. They _[[spells/Command|command]]_ mortals and undead using both their magic and force of personality.
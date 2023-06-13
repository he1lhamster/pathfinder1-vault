---
cssclass: [monsters]
title1: Spirit Avenger
title2: Spirit Avenger
CR: 16
sources:
- name: NPC Codex
  page: 223
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 76800
race: Half-orc
classes:
- barbarian 4
- sorcerer 6
- eldritch knight 7
alignment: N
size: Medium
type: humanoid
subtypes:
- human
- orc
initiative:
  bonus: 4
senses:
  darkvision: 60
AC:
  AC: 25
  touch: 18
  flat_footed: 20
  components:
    armor: 5
    deflection: 3
    dex: 4
    dodge: 1
    natural: 2
HP:
  HP: 139
  long: 4d12+6d6+7d10+48
saves:
  fort: 17
  ref: 12
  will: 16
defensive_abilities:
- orc ferocity
- trap sense +1
- uncanny dodge
resistances:
  acid: 5
  cold: 5
speeds:
  base: 40
attacks:
  melee:
  - - text: +1 spear +15/+10/+5 (1d8+1/×3)
      entries:
      - - damage: 1d8+1
          crit_multiplier: 3
      attack: +1 spear
      bonus:
      - 15
      - 10
      - 5
  ranged:
  - - text: +1 shortbow +20/+15/+10 (1d6+3/×3)
      entries:
      - - damage: 1d6+3
          crit_multiplier: 3
      attack: +1 shortbow
      bonus:
      - 20
      - 15
      - 10
  special:
  - rage (12 rounds/day)
  - rage powers (no escape, superstition +3)
spell_like_abilities:
  entries:
  - name: heavenly fire
    source: default
    freq: 6/day
    other: 1d4+3 divine energy
  sources:
  - name: default
    CL: 12
    concentration: 15
spells:
  entries:
  - name: disintegrate
    source: Sorcerer
    level: 6
    DC: 19
  - name: dismissal
    source: Sorcerer
    level: 5
    DC: 18
  - name: summon monster V
    source: Sorcerer
    level: 5
  - name: dimensional anchor
    source: Sorcerer
    level: 4
  - name: locate creature
    source: Sorcerer
    level: 4
  - name: resilient sphere
    source: Sorcerer
    level: 4
    DC: 17
  - name: halt undead
    source: Sorcerer
    level: 3
    DC: 16
  - name: haste
    source: Sorcerer
    level: 3
  - name: lightning bolt
    source: Sorcerer
    level: 3
    DC: 16
  - name: magic circle against evil
    source: Sorcerer
    level: 3
  - name: summon monster III
    source: Sorcerer
    level: 3
  - name: blindness/deafness
    source: Sorcerer
    level: 2
    DC: 15
  - name: false life
    source: Sorcerer
    level: 2
  - name: mirror image
    source: Sorcerer
    level: 2
  - name: resist energy
    source: Sorcerer
    level: 2
  - name: rope trick
    source: Sorcerer
    level: 2
  - name: see invisibility
    source: Sorcerer
    level: 2
  - name: bless
    source: Sorcerer
    level: 1
  - name: cause fear
    source: Sorcerer
    level: 1
    DC: 14
  - name: detect undead
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: shield
    source: Sorcerer
    level: 1
  - name: unseen servant
    source: Sorcerer
    level: 1
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: disrupt undead
    source: Sorcerer
    level: 0
  - name: flare
    source: Sorcerer
    level: 0
    DC: 13
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: open/close
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  - name: resistance
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 12
    concentration: 15
    slots:
      6: 3
      5: 5
      4: 6
      3: 7
      2: 7
      1: 7
      0: at-will
    bloodline: celestial
tactics:
  Before Combat: The eldritch knight casts false life.
  During Combat: The knight starts combat with shield and summoning spells, letting
    conjured allies run interference while he contains or damages his foes.
  Base Statistics: Without false life, the eldritch knight's statistics are hp 125.
ability_scores:
  STR: 10
  DEX: 18
  CON: 14
  INT: 10
  WIS: 16
  CHA: 16
BAB: 14
CMB: 14
CMD: 32
feats:
- name: Arcane Armor Mastery
- name: Arcane Armor Training
- name: Blind-Fight
- name: Combat Casting
- name: Dodge
- name: Eschew Materials
- name: Great Fortitude
- name: Iron Will
- name: Point-Blank Shot
- name: Rapid Shot
- name: Weapon Focus (shortbow)
- name: Weapon Specialization (shortbow)
skills:
  Climb: 8
  Diplomacy: 5
  Handle Animal: 11
  Intimidate: 5
  Knowledge (nature): 8
  Knowledge (planes): 5
  Knowledge (religion): 5
  Linguistics: 1
  Perception: 16
  Survival: 11
  Swim: 8
languages:
- Celestial
- Common
- Giant
- Orc
special_qualities:
- bloodline arcana (summoned creatures gain DR 3/evil)
- diverse training
- fast movement
- orc blood
- weapon familiarity
gear:
  combat:
  - +1 ghost touch arrows (10)
  - +1 undead-bane arrows (10)
  - scroll of neutralize poison
  - scroll of remove disease
  - scrolls of restoration (2)
  other:
  - +1 shortbow with 20 arrows
  - +1 spear
  - amulet of natural armor +2
  - belt of incredible dexterity +2
  - bracers of armor +5
  - cloak of resistance +3
  - headband of mental prowess +2 (Wis, Cha)
  - ring of protection +3
  - 246 gp
desc_long: Dedicated to protecting the world from evil outsiders and undead, spirit
  avengers realize it's better to contain an enemy than to destroy it.

---

# Spirit Avenger

**Source** NPC Codex pg. 223
**XP** 76,800
Half-orc _[[classes/Barbarian|barbarian]]_ 4/sorcerer 6/eldritch _[[npcs/Knight|knight]]_ 7

N Medium humanoid (human, _[[monsters/Orc|orc]]_)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +16

##### Defense

**AC** 25, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+5 armor, +3 _[[spells/Deflection|deflection]]_, +4 Dex, +1 _[[feats/Dodge|dodge]]_, +2 natural)
**hp** 139 (4d12+6d6+7d10+48)
**Fort** +17, **Ref** +12, **Will** +16
**Defensive Abilities** _orc_ _[[universal monster rules/Ferocity|ferocity]]_, trap sense +1, uncanny _dodge_; **Resist** acid 5, cold 5

##### Offense
**Speed** 40 ft.
**Melee** +1 _[[items/Weapon/Spear|spear]]_ +15/+10/+5 (1d8+1/×3)
**Ranged** +1 _[[items/Weapon/Shortbow|shortbow]]_ +20/+15/+10 (1d6+3/×3)
**Special Attacks** _[[spells/Rage|rage]]_ (12 rounds/day), _rage_ powers (no escape, superstition +3)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +15)
6/day—heavenly fire (1d4+3 divine energy)
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 12th; concentration +15)
6th (3/day)—_[[spells/Disintegrate|disintegrate]]_ (DC 19)
5th (5/day)—_[[spells/Dismissal|dismissal]]_ (DC 18), _[[spells/Summon Monster V|summon monster V]]_
4th (6/day)—_[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Locate Creature|locate creature]]_, _[[spells/Resilient Sphere|resilient sphere]]_ (DC 17)
3rd (7/day)—_[[spells/Halt Undead|halt undead]]_ (DC 16), _[[spells/Haste|haste]]_, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 16), _[[spells/Magic Circle against Evil|magic circle against evil]]_, _[[spells/Summon Monster III|summon monster III]]_
2nd (7/day)—blindness/deafness (DC 15), _[[spells/False Life|false life]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Resist Energy|resist energy]]_, _[[spells/Rope Trick|rope trick]]_, _[[spells/See Invisibility|see invisibility]]_
1st (7/day)—_[[spells/Bless|bless]]_, _[[spells/Cause Fear|cause fear]]_ (DC 14), _[[spells/Detect Undead|detect undead]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Shield|shield]]_, _[[spells/Unseen Servant|unseen servant]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Disrupt Undead|disrupt undead]]_, _[[spells/Flare|flare]]_ (DC 13), _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, open/close, _[[spells/Prestidigitation|prestidigitation]]_, _[[universal monster rules/Resistance|resistance]]_
**Bloodline **celestial

### Tactics

**Before Combat **The eldritch _knight_ casts _false life_.
**During Combat **The _knight_ starts combat with _shield_ and summoning spells, letting conjured allies run interference while he contains or damages his foes.
**Base Statistics **Without _false life_, the eldritch _knight_’s statistics are **hp **125.

##### Statistics
**Str** 10, **Dex** 18, **Con** 14, **Int** 10, **Wis** 16, **Cha** 16
**Base Atk** +14; **CMB** +14; **CMD** 32
**Feats** _[[feats/Arcane Armor Mastery|Arcane Armor Mastery]]_, _[[feats/Arcane Armor Training|Arcane Armor Training]]_, _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_shortbow_), _[[feats/Weapon Specialization|Weapon Specialization]]_ (_shortbow_)
**Skills** _[[universal monster rules/Climb|Climb]]_ +8, Diplomacy +5, Handle Animal +11, Intimidate +5, Knowledge (nature) +8, Knowledge (planes, religion) +5, Linguistics +1, Perception +16, Survival +11, Swim +8
**Languages** Celestial, Common, Giant, _Orc_
**SQ** bloodline arcana (summoned creatures gain DR 3/evil), diverse _[[items/Weapon Magic Abilities/Training|training]]_, fast movement, _orc_ blood, weapon familiarity
**Combat Gear** +1 _[[items/Weapon Magic Abilities/Ghost Touch|ghost touch]]_ arrows (10), +1 undead-bane arrows (10), scroll of _[[spells/Neutralize Poison|neutralize poison]]_, scroll of _[[spells/Remove Disease|remove disease]]_, scrolls of _[[spells/Restoration|restoration]]_ (2); **Other Gear** +1 _shortbow_ with 20 arrows, +1 _spear_, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, _[[items/Wondrous Item/Bracers of Armor +5|bracers of armor +5]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Headband of Mental Prowess +2|headband of mental prowess +2]]_ (Wis, Cha), _[[items/Ring/Ring of Protection +3|ring of protection +3]]_, 246 gp

Dedicated to protecting the world from evil outsiders and undead, spirit avengers realize it’s better to contain an enemy than to destroy it.
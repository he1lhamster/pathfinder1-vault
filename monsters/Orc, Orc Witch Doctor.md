---
cssclass: [monsters]
title1: Orc, Orc Witch Doctor
title2: Orc Witch Doctor
CR: 8
sources:
- name: Monster Codex
  page: 171
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 4800
race: Orc
classes:
- witch (scarred witch doctor) 9 (Pathfinder RPG Advanced Player's Guide 42, Pathfinder
  RPG Advanced Race Guide 140)
alignment: CE
size: Medium
type: humanoid
subtypes:
- orc
initiative:
  bonus: 2
senses:
  darkvision: 60
AC:
  AC: 17
  touch: 13
  flat_footed: 15
  components:
    armor: 4
    deflection: 1
    dex: 2
HP:
  HP: 94
  long: 9d6+60
saves:
  fort: 7
  ref: 6
  will: 10
  other: +2 vs. pain
defensive_abilities:
- ferocity
weaknesses:
- light sensitivity
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk dagger +6 (1d4+1/19-20)
      entries:
      - - damage: 1d4+1
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 6
  ranged:
  - - text: sling +6 (1d4+1)
      entries:
      - - damage: 1d4+1
      attack: sling
      bonus:
      - 6
  special:
  - hexes (blight [90 feet], cackle, evil eye [-4, 4 rounds], misfortune [2 rounds],
    slumber [9 rounds])
spells:
  entries:
  - name: cloudkill
    source: Witch
    level: 5
    DC: 16
  - name: enervation
    source: Witch
    level: 4
  - name: shout
    source: Witch
    level: 4
    DC: 15
  - name: fly
    source: Witch
    level: 3
  - name: lightning bolt
    source: Witch
    level: 3
    DC: 14
  - superscripts:
    - APG
    name: pain strike
    source: Witch
    level: 3
    DC: 14
  - superscripts:
    - APG
    name: screech
    source: Witch
    level: 3
    DC: 14
  - name: blindness/deafness
    source: Witch
    level: 2
    DC: 13
  - superscripts:
    - ARG
    name: blood blaze
    source: Witch
    level: 2
  - name: false life
    source: Witch
    level: 2
  - superscripts:
    - ARG
    name: sentry skull
    source: Witch
    level: 2
  - name: touch of idiocy
    source: Witch
    level: 2
  - name: burning hands
    source: Witch
    level: 1
    DC: 12
  - name: chill touch
    source: Witch
    level: 1
    DC: 12
  - name: enlarge person
    source: Witch
    level: 1
    DC: 12
  - name: mage armor
    source: Witch
    level: 1
  - name: ray of enfeeblement
    source: Witch
    level: 1
    DC: 12
  - name: arcane mark
    source: Witch
    level: 0
  - name: detect magic
    source: Witch
    level: 0
  - name: read magic
    source: Witch
    level: 0
  - superscripts:
    - APG
    name: spark
    source: Witch
    level: 0
  sources:
  - name: Witch
    type: prepared
    CL: 9
    concentration: 10
    slots:
      0: at-will
    patron: vengeance
tactics:
  Before Combat: The witch doctor casts false life and mage armor on herself before
    combat.
  During Combat: Before enemies reach the orcs, the witch doctor casts cloudkill in
    their midst. She then casts fly on herself so she can cast additional spells and
    uses hexes from above her enemies' melee reach. The witch doctor typically spends
    a couple of rounds weakening her strongest foes using enervation and ray of exhaustion,
    then begins blasting with evocation spells.
  Base Statistics: Without false life and mage armor, the witch doctor's statistics
    are AC 13, touch 13, flat-footed 11; hp 79.
ability_scores:
  STR: 12
  DEX: 14
  CON: 16
  INT: 12
  WIS: 12
  CHA: 8
BAB: 4
CMB: 5
CMD: 18
feats:
- superscripts:
  - APG
  name: Accursed Hex
- name: Combat Casting
- superscripts:
  - APG
  name: Extra Hex
- name: Iron Will
- name: Toughness
skills:
  Heal: 7
  Intimidate: 12
  Perception: 10
  Spellcraft: 13
languages:
- Common
- Orc
special_qualities:
- constitution dependent
- fetish mask
- hex scar
- scarshield (+4, 9 min./day)
- weapon familiarity
gear:
  combat:
  - potion of cure serious wounds
  - wand of ray of exhaustion (4 charges)
  other:
  - mwk dagger
  - sling with 20 stones
  - belt of incredible dexterity +2
  - bracers of armor +1
  - cloak of resistance +1
  - ring of protection +1
  - 98 gp
ecology:
  environment: temperate hills, mountains, or underground
desc_long: |-
  This witch doctor scars herself to get spells from her patron, a common practice among orc witches but one that's rarely practiced by non-orcs. The witch doctor draws her power from the enduring pain of these ritualistic scars, which also give her some measure of physical protection.

   The ferocious fetish mask she wears is carved from wood and is adorned with grisly remnants of people and animals, typically blood and gristle. Most witch doctors wear their masks anytime they perform magic or interact with other orcs, but some prefer to wear them only when going into battle or communing with their patrons through the masks to prepare spells.

   Because most orc tribes hold divine magic in high regard, many witch doctors learn to practice a small amount of divine magic in addition to their arcane magic-or at least pretend their spells come from the gods. Feuds between mystics and witch doctors create conf lict within many tribes, and most orcs side with the mystics. Often, these feuds turn into duels for supremacy.

---

# Orc, Orc Witch Doctor

**Source** Monster Codex pg. 171
**XP** 4,800
_[[monsters/Orc|Orc]]_ _[[classes/Witch|witch]]_ (scarred _witch_ doctor) 9 (Pathfinder RPG Advanced Player’s Guide 42, Pathfinder RPG Advanced Race Guide 140)
CE Medium humanoid (_orc_)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +10

##### Defense

**AC** 17, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 armor, +1 _[[spells/Deflection|deflection]]_, +2 Dex)
**hp** 94 (9d6+60)
**Fort** +7, **Ref** +6, **Will** +10; +2 vs. pain
**Defensive Abilities** _[[universal monster rules/Ferocity|ferocity]]_
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Dagger|dagger]]_ +6 (1d4+1/19–20)
**Ranged** _[[items/Weapon/Sling|sling]]_ +6 (1d4+1)
**Special Attacks** hexes (_[[spells/Blight|blight]]_ [90 feet], cackle, evil eye [–4, 4 rounds], misfortune [2 rounds], slumber [9 rounds])
**_Witch_ Spells Prepared **(CL 9th; concentration +10)
5th—_[[spells/Cloudkill|cloudkill]]_ (DC 16)
4th—_[[spells/Enervation|enervation]]_, _[[spells/Shout|shout]]_ (DC 15)
3rd—fly, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 14), _[[spells/Pain Strike|pain strike]]_ (DC 14), _[[spells/Screech|screech]]_ (DC 14)
2nd—blindness/deafness (DC 13), _[[spells/Blood Blaze|blood blaze]]_, _[[spells/False Life|false life]]_, _[[spells/Sentry Skull|sentry skull]]_, _[[spells/Touch of Idiocy|touch of idiocy]]_
1st—_[[spells/Burning Hands|burning hands]]_ (DC 12), _[[spells/Chill Touch|chill touch]]_ (DC 12), _[[spells/Enlarge Person|enlarge person]]_ (DC 12), _[[spells/Mage Armor|mage armor]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 12)
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Read Magic|read magic]]_, _[[spells/Spark|spark]]_
**Patron **_[[feats/Vengeance|vengeance]]_

### Tactics

**Before Combat** The _witch_ doctor casts _false life_ and _mage armor_ on herself before combat.
 **During Combat** Before enemies reach the orcs, the _witch_ doctor casts _cloudkill_ in their midst. She then casts fly on herself so she can cast additional spells and uses hexes from above her enemies’ melee reach. The _witch_ doctor typically spends a couple of rounds weakening her strongest foes using _enervation_ and _[[spells/Ray of Exhaustion|ray of exhaustion]]_, then begins blasting with evocation spells.
 **Base Statistics** Without _false life_ and _mage armor_, the _witch_ doctor’s statistics are **AC **13, touch 13, _flat-footed_ 11; **hp **79.

##### Statistics
**Str** 12, **Dex** 14, **Con** 16, **Int** 12, **Wis** 12, **Cha** 8
**Base Atk** +4; **CMB** +5; **CMD** 18
**Feats** _[[feats/Accursed Hex|Accursed Hex]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Extra Hex|Extra Hex]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Toughness|Toughness]]_
**Skills** _[[spells/Heal|Heal]]_ +7, Intimidate +12, Perception +10, Spellcraft +13
**Languages** Common, _Orc_
**SQ** constitution dependent, fetish _[[items/Mundane/Mask|mask]]_, hex scar, scarshield (+4, 9 min./day), weapon familiarity
**Combat Gear** potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_, wand of _ray of exhaustion_ (4 charges); **Other Gear** mwk _dagger_, _sling_ with 20 stones, _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, _[[items/Wondrous Item/Bracers of Armor +1|bracers of armor +1]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 98 gp

##### Ecology

**Environment** temperate hills, mountains, or underground

##### Description

This _witch_ doctor scars herself to get spells from her patron, a common practice among _orc_ witches but one that’s rarely practiced by non-orcs. The _witch_ doctor draws her power from the enduring pain of these ritualistic scars, which also give her some measure of physical protection.

The ferocious fetish _mask_ she wears is carved from wood and is adorned with grisly remnants of people and animals, typically blood and gristle. Most _witch_ doctors wear their masks anytime they perform magic or interact with other orcs, but some prefer to wear them only when going into battle or communing with their patrons through the masks to prepare spells.

Because most _orc_ tribes hold divine magic in high regard, many _witch_ doctors learn to practice a small amount of divine magic in addition to their arcane magic—or at least pretend their spells come from the gods. Feuds between mystics and _witch_ doctors create conf lict within many tribes, and most orcs side with the mystics. Often, these feuds turn into duels for supremacy.
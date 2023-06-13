---
cssclass: [monsters]
title1: Vampire, Vampire Savage
title2: Vampire Savage
CR: 10
sources:
- name: Monster Codex
  page: 241
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 9600
race: Half-orc
classes:
- vampire barbarian 9
alignment: CE
size: Medium
type: undead
subtypes:
- augmented humanoid
- human
- orc
initiative:
  bonus: 8
senses:
  darkvision: 60
AC:
  AC: 21
  touch: 14
  flat_footed: 16
  components:
    deflection: 1
    dex: 4
    dodge: 1
    natural: 7
    rage: -2
HP:
  HP: 136
  long: 9d12+72
  fast_healing: 5
saves:
  fort: 13
  ref: 10
  will: 8
defensive_abilities:
- channel resistance +4
- improved uncanny dodge
- orc ferocity
- trap sense +3
DR:
- amount: 10
  weakness: magic and silver
- amount: 1
  weakness: '-'
immunities:
- undead traits
resistances:
  cold: 10
  electricity: 10
weaknesses:
- vampire weaknesses
speeds:
  base: 40
attacks:
  melee:
  - - text: +1 greataxe +20/+15 (1d12+16/×3)
      entries:
      - - damage: 1d12+16
          crit_multiplier: 3
      attack: +1 greataxe
      bonus:
      - 20
      - 15
    - text: bite +14 (1d4+5 plus energy drain)
      entries:
      - - damage: 1d4+5
        - effect: energy drain
      attack: bite
      bonus:
      - 14
    - text: slam +15 (1d4+5 plus energy drain)
      entries:
      - - damage: 1d4+5
        - effect: energy drain
      attack: slam
      bonus:
      - 15
  special:
  - blood drain
  - children of the night
  - create spawn
  - dominate (DC 20)
  - energy drain (2 levels, DC 20)
  - rage (24 rounds/day)
  - rage powers (animal fury, bleeding blow, no escape, powerful blow +3)
tactics:
  Before Combat: The vampire savage drinks one or more of his potions as appropriate
    to the upcoming battle.
  During Combat: The vampire savage rages and makes full attacks against his opponents,
    grappling an opponent and draining blood if he has an opportunity to do so.
  Base Statistics: When he's not raging, the savage's statistics are AC 23, touch
    16, flat-footed 18; hp 118; Fort +11, Will +6; Melee +1 greataxe +18/+13 (1d12+13/×3),
    slam +13 (1d4+4 plus energy drain), bite +12 (1d4+4 plus energy drain); Str 26,
    Cha 18; CMB +17 (+21 bull rush); CMD 33 (33 vs. bull rush).
ability_scores:
  STR: 30
  DEX: 18
  CON:
  INT: 10
  WIS: 14
  CHA: 22
BAB: 9
CMB: 19
CMB_other: +23 bull rush
CMD: 33
CMD_other: 35 vs. bull rush
feats:
- is_bonus: true
  name: Alertness
- name: Cleave
- is_bonus: true
  name: Dodge
- name: Greater Bull Rush
- name: Improved Bull Rush
- is_bonus: true
  name: Improved Initiative
- is_bonus: true
  name: Lightning Reflexes
- name: Power Attack
- is_bonus: true
  name: Toughness
- name: Weapon Focus (slam)
skills:
  Acrobatics: 16
    when jumping: 20
  Intimidate: 20
  Knowledge (nature): 12
  Perception: 24
  Sense Motive: 12
  _racial_mods:
    Bluff:
      _: 8
    Perception:
      _: 8
    Sense Motive:
      _: 8
    Stealth:
      _: 8
languages:
- Common
- Orc
special_qualities:
- change shape (dire bat or wolf, beast shape II)
- fast movement
- gaseous form
- orc blood
- shadowless
- spider climb
gear:
  combat:
  - potion of blur
  - potion of haste
  - potion of resist energy (fire)
  other:
  - +1 greataxe
  - amulet of natural armor +1
  - belt of giant strength +2
  - cloak of resistance +1
  - ring of protection +1
  - 80 gp
ecology:
  environment: any
special_abilities:
  Undead Barbarian: An undead creature with the ability to enter a rage gains the
    morale bonuses from rage despite being immune to morale effects. The bonus to
    Constitution from the rage applies to an undead creature's Charisma instead.
desc_long: |-
  With razor-sharp fangs and the ability to drain the life out of his opponents, a vampire savage is a frightening sight to behold. This vampire tears his victims apart even as he bleeds them dry-savoring every scream he causes, enjoys the last heartbeat of each victim, and laughs at adventurers who dare to try stopping his murderous rampage. Because the vampire savage mangles the bodies of his victims so badly, many believe that his killings are the work of a wild animal. The carnage he leaves in his wake stands as an easy trail for a hunter to follow, but those would-be vampire slayers who get too close are not usually seen again.

   This sort of vampire often takes control of a violent tribe of orcs, gnolls, and similar creatures, driving them into a frenzy and demanding blood sacrifices from them to appease his appetite.

---

# Vampire, Vampire Savage

**Source** Monster Codex pg. 241
**XP** 9,600
Half-orc _[[monsters/Vampire|vampire]]_ _[[classes/Barbarian|barbarian]]_ 9
CE Medium undead (augmented humanoid, human, _[[monsters/Orc|orc]]_)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +24

##### Defense

**AC** 21, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+1 _[[spells/Deflection|deflection]]_, +4 Dex, +1 _[[feats/Dodge|dodge]]_, +7 natural, –2 _[[spells/Rage|rage]]_)
**hp** 136 (9d12+72); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +13, **Ref** +10, **Will** +8
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4, improved uncanny _dodge_, _orc_ _[[universal monster rules/Ferocity|ferocity]]_, trap sense +3; **DR** 10/magic and silver and DR 1/—; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** cold 10, electricity 10
**Weaknesses** _vampire_ weaknesses

##### Offense
**Speed** 40 ft.
**Melee** +1 _[[items/Weapon/Greataxe|greataxe]]_ +20/+15 (1d12+16/×3), bite +14 (1d4+5 plus _[[universal monster rules/Energy Drain|energy drain]]_), slam +15 (1d4+5 plus _energy drain_)
**Special Attacks** _[[universal monster rules/Blood Drain|blood drain]]_, children of the night, create spawn, dominate (DC 20), _energy drain_ (2 levels, DC 20), _rage_ (24 rounds/day), _rage_ powers (animal fury, bleeding blow, no escape, powerful blow +3)

### Tactics

**Before Combat** The _vampire_ savage drinks one or more of his potions as appropriate to the upcoming battle.
 **During Combat** The _vampire_ savage rages and makes full attacks against his opponents, grappling an opponent and draining blood if he has an opportunity to do so.
 **Base Statistics** When he’s not raging, the savage’s statistics are **AC **23, touch 16, _flat-footed_ 18; **hp **118; **Fort **+11, **Will **+6; **Melee **+1 _greataxe_ +18/+13 (1d12+13/×3), slam +13 (1d4+4 plus _energy drain_), bite +12 (1d4+4 plus _energy drain_); **Str **26, **Cha **18; **CMB **+17 (+21 bull rush); **CMD **33 (33 vs. bull rush).

##### Statistics
**Str** 30, **Dex** 18, **Con** —, **Int** 10, **Wis** 14, **Cha** 22
**Base Atk** +9; **CMB** +19 (+23 bull rush); **CMD** 33 (35 vs. bull rush)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Cleave|Cleave]]_, _Dodge_, _[[feats/Greater Bull Rush|Greater Bull Rush]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (slam)
**Skills** Acrobatics +16 (+20 when jumping), Intimidate +20, Knowledge (nature) +12, Perception +24, Sense Motive +12; **Racial Modifiers** +8 Bluff, +8 Perception, +8 Sense Motive, +8 Stealth
**Languages** Common, _Orc_
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (dire bat or _[[monsters/Wolf|wolf]]_, _[[spells/Beast Shape II|beast shape II]]_), fast movement, _[[spells/Gaseous Form|gaseous form]]_, _orc_ blood, shadowless, _[[spells/Spider Climb|spider climb]]_
**Combat Gear** potion of _[[spells/Blur|blur]]_, potion of _[[spells/Haste|haste]]_, potion of _[[spells/Resist Energy|resist energy]]_ (fire); **Other Gear** +1 _greataxe_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 80 gp

##### Ecology

**Environment** any

### Special Abilities

**Undead _Barbarian_** An undead creature with the ability to enter a _rage_ gains the morale bonuses from _rage_ despite being immune to morale effects. The bonus to Constitution from the _rage_ applies to an undead creature’s Charisma instead.

##### Description

With razor-sharp fangs and the ability to drain the life out of his opponents, a _vampire_ savage is a frightening sight to behold. This _vampire_ tears his victims apart even as he bleeds them dry—savoring every scream he causes, enjoys the last heartbeat of each victim, and laughs at adventurers who dare to try stopping his murderous rampage. Because the _vampire_ savage mangles the bodies of his victims so badly, many believe that his killings are the work of a wild animal. The carnage he leaves in his wake stands as an easy trail for a _[[classes/Hunter|hunter]]_ to follow, but those would-be _vampire_ slayers who get too close are not usually seen again.

This sort of _vampire_ often takes control of a violent tribe of orcs, gnolls, and similar creatures, driving them into a frenzy and demanding blood sacrifices from them to appease his appetite.
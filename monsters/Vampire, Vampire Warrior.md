﻿---
cssclass: [monsters]
title1: Vampire, Vampire Warrior
title2: Vampire Warrior
CR: 8
sources:
- name: Monster Codex
  page: 240
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 4800
race: Vishkanya
classes:
- jiang-shi vampire fighter 7 (Pathfinder RPG Bestiary 3 278, 281)
alignment: LE
size: Medium
type: undead
subtypes:
- augmented humanoid
- vishkanya
initiative:
  bonus: 9
senses:
  blindsight: 60
  blindsight_other: breathing creatures only
  darkvision: 60
  low-light vision: true
AC:
  AC: 25
  touch: 15
  flat_footed: 20
  components:
    armor: 8
    dex: 4
    dodge: 1
    natural: 2
HP:
  HP: 78
  long: 7d10+35
  fast_healing: 5
saves:
  fort: 9
  ref: 7
  will: 4
  will_other: +2 vs. fear
  other: +2 vs. poison
defensive_abilities:
- bravery +2
- channel resistance +4
- prayer scroll
DR:
- amount: 10
  weakness: magic and slashing
immunities:
- undead traits
resistances:
  cold: 20
weaknesses:
- jiang-shi weaknesses
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk katana +15/+10 (1d8+8/15-20 plus poison)
      entries:
      - - damage: 1d8+8
          crit_range: 15-20
        - effect: poison
      attack: mwk katana
      bonus:
      - 15
      - 10
  - - text: bite +12 (1d6+5)
      entries:
      - - damage: 1d6+5
      attack: bite
      bonus:
      - 12
    - text: 2 claws +12 (1d8+5/19-20 plus grab)
      entries:
      - - damage: 1d8+5
          crit_range: 19-20
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 12
  ranged:
  - - text: shuriken +12/+7 (1d2+5)
      entries:
      - - damage: 1d2+5
      attack: shuriken
      bonus:
      - 12
      - 7
  special:
  - drain chi (DC 17)
  - poison
  - weapon training (heavy blades +1)
tactics:
  Before Combat: The warrior vampire uses her oil of keen edge on her katana and applies
    a dose of her racial poison to it.
  During Combat: The warrior vampire uses her scabbard of vigor to grant her katana
    a +3 enhancement bonus for 3 rounds. Once that expires, or if her katana attacks
    are ineffective, she resorts to natural attacks, grappling, and her drain chi
    ability.
ability_scores:
  STR: 20
  DEX: 20
  CON:
  INT: 10
  WIS: 15
  CHA: 18
BAB: 7
CMB: 12
CMD: 28
feats:
- is_bonus: true
  name: Alertness
- name: Cleave
- name: Combat Reflexes
- is_bonus: true
  name: Dodge
- name: Exotic Weapon Proficiency (katana)
- name: Improved Initiative
- is_bonus: true
  name: Mobility
- name: Power Attack
- name: Quick Draw
- is_bonus: true
  name: Skill Focus (Acrobatics)
- is_bonus: true
  name: Spring Attack
- name: Weapon Focus (katana)
- name: Weapon Specialization (katana)
skills:
  Acrobatics: 12
  Craft (calligraphy): 4
  Craft (paintings): 4
  Escape Artist: 3
  Knowledge (local): 2
  Knowledge (nobility): 2
  Perception: 21
  Sense Motive: 4
  Stealth: 12
  _racial_mods:
    Acrobatics:
      _: 8
    Perception:
      _: 8
    Stealth:
      _: 10
languages:
- Common
- Vishkanya
special_qualities:
- armor training 2
- poison use
- toxic (4/day)
gear:
  combat:
  - oil of keen edge
  - potion of bull's strength
  - potion of fly
  - potion of haste
  - potion of inflict moderate wounds
  - potion of invisibility
  other:
  - o-yoroi
  - mwk katana
  - shuriken (20)
  - brooch of shielding (50 points)
  - scabbard of vigor
  - 46 gp
ecology:
  environment: any
special_abilities:
  Drain Chi (Su): Instead of draining blood, a jiang-shi vampire drains “chi,” or
    life energy, from a victim's breath. When a jiang-shi makes a successful grapple
    check (in addition to any other effects caused by a successful check, including
    additional damage), the jiang-shi can attempt to drain chi by drinking the victim's
    breath. The victim can resist this attack by succeeding at a DC 17 Fortitude save.
    On a failed save, the victim gains 1 negative level and is staggered for 1d4 rounds.
  Poison (Ex): 'Vishkanya Venom: Weapon-injury; save Fort DC 17; frequency 1/round
    for 6 rounds; effect 1d2 Dex; cure 1 save.'
  Prayer Scroll (Su): The scroll attached to the brow of a jiang-shi grants immunity
    to any effects generated by spell-completion or spelltrigger magic items, such
    as scrolls and wands. Such magical effects treat the jiang-shi as if she had unbeatable
    spell resistance. A jiang-shi's prayer scroll can be removed with a successful
    steal combat maneuver (Pathfinder RPG Advanced Player's Guide 322), which immediately
    ends the jiang-shi's immunity to these effects. If a jiang-shi's prayer scroll
    is destroyed (a standard action), the vampire also loses her fast healing ability.
    A jiangshi can create a replacement prayer scroll by using any strip of parchment
    and a writing instrument, but doing so requires 10 minutes of uninterrupted work.
  Toxic (Ex): Four times per day as a swift action, a vishkanya can envenom a weapon
    that she wields with her toxic saliva or blood.
desc_long: When this vishkanya was alive, she pursued the path of the samurai, but
  wasn't allowed to join their honorable ranks. Her restless spirit remained trapped
  in her flesh after death, and eventually she animated her own rotting body and sought
  out those who had wronged her.

---

# Vampire, Vampire Warrior

**Source** Monster Codex pg. 240
**XP** 4,800
_[[monsters/Vishkanya|Vishkanya]]_ jiang-shi _[[monsters/Vampire|vampire]]_ _[[classes/Fighter|fighter]]_ 7 (Pathfinder RPG Bestiary 3 278, 281)

LE Medium undead (augmented humanoid, _vishkanya_)
**Init** +9; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 60 ft. (breathing creatures only), _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +21

##### Defense

**AC** 25, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+8 armor, +4 Dex, +1 _[[feats/Dodge|dodge]]_, +2 natural)
**hp** 78 (7d10+35); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +9, **Ref** +7, **Will** +4 (+2 vs. _[[universal monster rules/Fear|fear]]_); +2 vs. poison
**Defensive Abilities** bravery +2, _[[universal monster rules/Channel Resistance|channel resistance]]_ +4, _[[spells/Prayer|prayer]]_ scroll; **DR** 10/magic and slashing; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** cold 20
**Weaknesses** jiang-shi weaknesses

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Katana|katana]]_ +15/+10 (1d8+8/15–20 plus poison) or bite +12 (1d6+5), 2 claws +12 (1d8+5/19–20 plus _[[universal monster rules/Grab|grab]]_)
**Ranged** shuriken +12/+7 (1d2+5)
**Special Attacks** drain chi (DC 17), poison, weapon _[[items/Weapon Magic Abilities/Training|training]]_ (heavy blades +1)

### Tactics

**Before Combat** The warrior _vampire_ uses her oil of _[[spells/Keen Edge|keen edge]]_ on her _katana_ and applies a dose of her racial poison to it.
 **During Combat** The warrior _vampire_ uses her _[[items/Wondrous Item/Scabbard of Vigor|scabbard of vigor]]_ to grant her _katana_ a +3 enhancement bonus for 3 rounds. Once that expires, or if her _katana_ attacks are ineffective, she resorts to _[[universal monster rules/Natural Attacks|natural attacks]]_, grappling, and her drain chi ability.

##### Statistics
**Str** 20, **Dex** 20, **Con** —, **Int** 10, **Wis** 15, **Cha** 18
**Base Atk** +7; **CMB** +12; **CMD** 28
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Exotic Weapon Proficiency|Exotic Weapon Proficiency]]_ (_katana_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quick Draw|Quick Draw]]_, _[[feats/Skill Focus|Skill Focus]]_ (Acrobatics), _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_katana_), _[[feats/Weapon Specialization|Weapon Specialization]]_ (_katana_)
**Skills** Acrobatics +12, Craft (calligraphy) +4, Craft (paintings) +4, Escape Artist +3, Knowledge (local) +2, Knowledge (nobility) +2, Perception +21, Sense Motive +4, Stealth +12; **Racial Modifiers** +8 Acrobatics, +8 Perception, +10 Stealth
**Languages** Common, _Vishkanya_
**SQ** armor _training_ 2, poison use, _[[items/Weapon Magic Abilities/Toxic|toxic]]_ (4/day)
**Combat Gear** oil of _keen edge_, potion of bull’s strength, potion of fly, potion of _[[spells/Haste|haste]]_, potion of _[[spells/Inflict Moderate Wounds|inflict moderate wounds]]_, potion of _[[spells/Invisibility|invisibility]]_; **Other Gear** _[[items/Armor/O-yoroi|o-yoroi]]_, mwk _katana_, shuriken (20), _[[items/Wondrous Item/Brooch of Shielding|brooch of shielding]]_ (50 points), _scabbard of vigor_, 46 gp

##### Ecology

**Environment** any

### Special Abilities

**Drain Chi (Su)** Instead of draining blood, a jiang-shi _vampire_ drains “chi,” or life energy, from a victim’s breath. When a jiang-shi makes a successful grapple check (in addition to any other effects caused by a successful check, including additional damage), the jiang-shi can attempt to drain chi by drinking the victim’s breath. The victim can resist this attack by succeeding at a DC 17 Fortitude save. On a failed save, the victim gains 1 negative level and is _[[conditions/Staggered|staggered]]_ for 1d4 rounds.

**Poison (Ex)** _Vishkanya_ Venom: Weapon—injury; save Fort DC 17; frequency 1/round for 6 rounds; effect 1d2 Dex; cure 1 save.

**_Prayer_ Scroll (Su)** The scroll attached to the brow of a jiang-shi grants _[[universal monster rules/Immunity|immunity]]_ to any effects generated by spell-completion or spelltrigger magic items, such as scrolls and wands. Such magical effects treat the jiang-shi as if she had unbeatable _[[universal monster rules/Spell Resistance|spell resistance]]_. A jiang-shi’s _prayer_ scroll can be removed with a successful steal combat maneuver (Pathfinder RPG Advanced Player’s Guide 322), which immediately ends the jiang-shi’s _immunity_ to these effects. If a jiang-shi’s _prayer_ scroll is destroyed (a standard action), the _vampire_ also loses her _fast healing_ ability. A jiangshi can create a replacement _prayer_ scroll by using any strip of parchment and a writing instrument, but doing so requires 10 minutes of uninterrupted work.

**_Toxic_ (Ex)** Four times per day as a swift action, a _vishkanya_ can envenom a weapon that she wields with her _toxic_ saliva or blood.

##### Description

When this _vishkanya_ was alive, she pursued the path of the _[[classes/Samurai|samurai]]_, but wasn’t allowed to join their honorable ranks. Her restless spirit remained trapped in her flesh after death, and eventually she _[[items/Armor Magic Abilities/Animated|animated]]_ her own rotting body and sought out those who had wronged her.
---
cssclass: [monsters]
title1: Asura, Hishandura
desc_short: This muscular fiend has two vertically mirrored faces, four arms, and
  a quartet of sinister punching daggers
title2: Hishandura
CR: 15
sources:
- name: 'Pathfinder #136: Temple of the Peacock Spirit'
  page: 82
  link: https://paizo.com/products/btpya0b5
XP: 51200
alignment: LE
size: Large
type: outsider
subtypes:
- asura
- evil
- extraplanar
- lawful
initiative:
  bonus: 7
senses:
  darkvision: 60
  scent: true
  scent of carnage: true
  smoke sight: true
auras:
- name: elusive
  radius: 75
AC:
  AC: 30
  touch: 12
  flat_footed: 27
  components:
    dex: 3
    natural: 18
    size: -1
HP:
  HP: 207
  long: 18d10+108
  regeneration: 10
  regeneration_weakness: good spells, good weapons
saves:
  fort: 17
  ref: 11
  will: 15
  other: +2 vs. enchantment spells
DR:
- amount: 10
  weakness: good
immunities:
- curse effects
- disease
- poison
resistances:
  acid: 10
  electricity: 10
SR: 26
speeds:
  base: 50
attacks:
  melee:
  - - text: +1 punching dagger +23/+18/+13/+8 (1d6+8/19-20/×3)
      entries:
      - - damage: 1d6+8
          crit_range: 19-20
          crit_multiplier: 3
      attack: +1 punching dagger
      bonus:
      - 23
      - 18
      - 13
      - 8
    - text: 3 +1 punching daggers +23 (1d6+4/19-20/×3)
      entries:
      - - damage: 1d6+4
          crit_range: 19-20
          crit_multiplier: 3
      count: 3
      attack: +1 punching daggers
      bonus:
      - 23
    - text: bite +19 (2d6+3)
      entries:
      - - damage: 2d6+3
      attack: bite
      bonus:
      - 19
  - - text: bite +24 (2d6+7)
      entries:
      - - damage: 2d6+7
      attack: bite
      bonus:
      - 24
    - text: 4 slams +24 (1d6+7)
      entries:
      - - damage: 1d6+7
      count: 4
      attack: slams
      bonus:
      - 24
  special:
  - destructive blades
  - punitive penance
  - rend (2 slams or 2 punching daggers, 4d6 bleed and punitive penance)
  - repentant rain
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: gaseous form
    source: default
    freq: At will
  - name: chain lightning
    source: default
    freq: 3/day
    DC: 22
  - name: cloudkill
    source: default
    freq: 3/day
    DC: 21
  - name: cone of cold
    source: default
    freq: 3/day
    DC: 21
  - name: dimension door
    source: default
    freq: 3/day
  - name: fire snake
    source: default
    freq: 3/day
    DC: 21
  - name: greater dispel magic
    source: default
    freq: 3/day
  - name: wall of fire
    source: default
    freq: 3/day
  - name: control water
    source: default
    freq: 1/day
  - name: control weather
    source: default
    freq: 1/day
  - name: greater shout
    source: default
    freq: 1/day
    DC: 24
  - name: summon
    source: default
    freq: 1/day
    level: 6
    summons:
    - name: aghasuras
      amount: 1d3
      chance: 40%
  sources:
  - name: default
    CL: 18
    concentration: 24
ability_scores:
  STR: 25
  DEX: 16
  CON: 23
  INT: 13
  WIS: 18
  CHA: 22
BAB: 18
CMB: 26
CMD: 39
feats:
- name: Combat Reflexes
- name: Critical Focus
- name: Improved Critical (punching dagger)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Multiweapon Fighting
- name: Nimble Moves
- name: Power Attack
- name: Staggering Critical
skills:
  Escape Artist: 9
  Intimidate: 27
  Knowledge (local): 13
  Knowledge (planes): 13
  Knowledge (religion): 22
  Perception: 29
  Sense Motive: 25
  Spellcraft: 19
  Use Magic Device: 27
  _racial_mods:
    Escape Artist:
      _: 6
    Perception:
      _: 4
languages:
- Common
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Hell)
  organization: solitary
  treasure_type: standard
  treasure:
  - 4 +1 punching daggers
  - other treasure
special_abilities:
  Destructive Blades (Su): A hishandura's melee attacks ignore hardness of less than
    20 and damage reduction, except for damage reduction bypassed by epic weapons
    and damage reduction without a type (such as DR 10/-). Whenever a hishandura makes
    a full attack against an object or a structure, its attacks deal double damage.
  Punitive Penance (Su): When a hishandura rends a target, that creature must succeed
    at a DC 25 Will save or experience overwhelming grief for its past actions, as
    per terrible remorse. The save DC is Charisma-based.
  Repentant Rain (Su): Once per round after confirming a critical hit with a melee
    weapon, a hishandura can spray gore from the wound in a 30-foot cone originating
    from any square occupied by its target. Each non-asura in the area is blinded
    for 1d3 rounds unless it succeeds at a DC 26 Reflex save. A blinded creature can
    wipe the gore from its eyes as a standard action, removing the blindness; alternatively,
    another creature adjacent to a blinded creature can wipe away the gore as a standard
    action. Jumping into a body of water or being subject to an effect that creates
    a lot of water (such as create water or hydraulic push) also removes the blindness.
    The save DC is Strength-based.
  Scent of Carnage (Ex): A hishandura's sense of smell is especially sensitive to
    blood and fresh injuries. The asura gains blindsense with a range of 60 feet but
    can sense only corpses, badly wounded creatures (those with half their total hit
    points or fewer), those suffering from bleed damage, and those affected by the
    asura's repentant rain ability.
  Smoke Sight (Ex): A hishandura can see through fire, fog, and smoke as if they were
    perfectly clear, ignoring the miss chance for these obstructions, up to its normal
    range of its vision.
desc_long: |-
  Ages ago, a short-sighted god sought to punish his flock for a perceived slight, infusing a champion with a fragment of his power and sending it to wreak havoc. The champion did as commanded, tearing apart the faithful and showering their city with blood. The deity heard the tearful cries of the mortals, pleading for mercy and insisting that any kindly god would never visit such hatred upon his people. The god felt an upwelling of shame for having engineered such violence, but rather than accept responsibility or undo the damage, the god appeared before the city and forsook the divine champion, insisting that it was a raving beast sent by some less caring patron than himself. Empowered by their lying god's words and magic, the people praised him, rallied, and killed the champion. From this act of betrayal-and the remains of the slaughtered champion-rose the first hishandura.

   Hishanduras are 13 feet tall and weigh 1,800 pounds.

---

# Asura, Hishandura
This muscular fiend has two vertically _[[items/Armor Magic Abilities/Mirrored|mirrored]]_ faces, four arms, and a quartet of sinister punching daggers
**Source** Pathfinder #136: Temple of the Peacock Spirit pg. 82
**XP** 51,200

LE Large outsider (asura, evil, extraplanar, lawful)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_, _scent_ of carnage, smoke sight; Perception +29
**Aura** elusive (75 ft.)

##### Defense

**AC** 30, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+3 Dex, +18 natural, –1 size)
**hp** 207 (18d10+108); _[[universal monster rules/Regeneration|regeneration]]_ 10 (good spells, good weapons)
**Fort** +17, **Ref** +11, **Will** +15; +2 vs. enchantment spells
**DR** 10/good; **Immune** curse effects, disease, poison; **Resist** acid 10, electricity 10; **SR** 26

##### Offense
**Speed** 50 ft.
**Melee** +1 _[[items/Weapon/Punching dagger|punching dagger]]_ +23/+18/+13/+8 (1d6+8/19–20/×3), 3 +1 punching daggers +23 (1d6+4/19–20/×3), bite +19 (2d6+3) or bite +24 (2d6+7), 4 slams +24 (1d6+7)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** destructive blades, punitive penance, _[[universal monster rules/Rend|rend]]_ (2 slams or 2 punching daggers, 4d6 _[[universal monster rules/Bleed|bleed]]_ and punitive penance), repentant rain
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +24)
At will—_[[spells/Gaseous Form|gaseous form]]_ 
3/day—_[[spells/Chain Lightning|chain lightning]]_ (DC 22), _[[spells/Cloudkill|cloudkill]]_ (DC 21), _[[spells/Cone of Cold|cone of cold]]_ (DC 21), _[[spells/Dimension Door|dimension door]]_, _[[spells/Fire Snake|fire snake]]_ (DC 21), greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Wall Of Fire|wall of fire]]_ 
1/day—_[[spells/Control Water|control water]]_, _[[spells/Control Weather|control weather]]_, greater _[[spells/Shout|shout]]_ (DC 24), _[[universal monster rules/Summon|summon]]_ (level 6, 1d3 aghasuras, 40%)

##### Statistics
**Str** 25, **Dex** 16, **Con** 23, **Int** 13, **Wis** 18, **Cha** 22
**Base Atk** +18; **CMB** +26; **CMD** 39
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (_punching dagger_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiweapon Fighting|Multiweapon Fighting]]_, _[[feats/Nimble Moves|Nimble Moves]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_
**Skills** Escape Artist +9, Intimidate +27, Knowledge (local) +13, Knowledge (planes) +13, Knowledge (religion) +22, Perception +29, Sense Motive +25, Spellcraft +19, Use Magic Device +27; **Racial Modifiers** +6 Escape Artist, +4 Perception
**Languages** Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Hell)
**Organization** solitary
**Treasure** standard (4 +1 punching daggers, other treasure)

### Special Abilities

**Destructive Blades (Su)** A hishandura’s melee attacks ignore hardness of less than 20 and _[[universal monster rules/Damage Reduction|damage reduction]]_, except for _damage reduction_ bypassed by epic weapons and _damage reduction_ without a type (such as DR 10/—). Whenever a hishandura makes a full attack against an object or a structure, its attacks deal double damage.

**Punitive Penance (Su)** When a hishandura rends a target, that creature must succeed at a DC 25 Will save or experience _[[spells/Overwhelming Grief|overwhelming grief]]_ for its past actions, as per _[[spells/Terrible Remorse|terrible remorse]]_. The save DC is Charisma-based.

**Repentant Rain (Su)** Once per round after confirming a critical hit with a melee weapon, a hishandura can spray gore from the wound in a 30-foot cone originating from any square occupied by its target. Each non-asura in the area is _[[conditions/Blinded|blinded]]_ for 1d3 rounds unless it succeeds at a DC 26 Reflex save. A _blinded_ creature can wipe the gore from its eyes as a standard action, removing the blindness; alternatively, another creature adjacent to a _blinded_ creature can wipe away the gore as a standard action. Jumping into a body of water or being subject to an effect that creates a lot of water (such as _[[spells/Create Water|create water]]_ or _[[spells/Hydraulic Push|hydraulic push]]_) also removes the blindness. The save DC is Strength-based.
**_Scent_ of Carnage (Ex)** A hishandura’s sense of smell is especially sensitive to blood and fresh injuries. The asura gains _[[universal monster rules/Blindsense|blindsense]]_ with a range of 60 feet but can sense only corpses, badly wounded creatures (those with half their total hit points or fewer), those suffering from _bleed_ damage, and those affected by the asura’s repentant rain ability.
**Smoke Sight (Ex)** A hishandura can see through fire, fog, and smoke as if they were perfectly clear, ignoring the miss chance for these obstructions, up to its normal range of its _[[spells/Vision|vision]]_.

##### Description

Ages ago, a short-sighted god sought to punish his flock for a perceived slight, infusing a _[[items/Armor Magic Abilities/Champion|champion]]_ with a fragment of his power and _[[spells/Sending|sending]]_ it to wreak havoc. The _champion_ did as commanded, tearing apart the faithful and showering their city with blood. The deity heard the tearful cries of the mortals, pleading for mercy and insisting that any kindly god would never visit such hatred upon his people. The god felt an upwelling of shame for having engineered such violence, but rather than accept responsibility or undo the damage, the god appeared before the city and forsook the divine _champion_, insisting that it was a raving beast sent by some less caring patron than himself. Empowered by their lying god’s words and magic, the people praised him, rallied, and killed the _champion_. From this act of betrayal—and the remains of the slaughtered _champion_—rose the first hishandura.

Hishanduras are 13 feet tall and weigh 1,800 pounds.
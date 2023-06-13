---
cssclass: [monsters]
title1: Devil, Warmonger Devil (Levaloch)
desc_short: Armored like an infernal knight upon some monstrous steed, this fiend
  of iron and nails scuttles upon six bladed, beetle-like legs.
title2: Warmonger Devil (Levaloch)
CR: 7
sources:
- name: Bestiary 5
  page: 81
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
- name: 'Book of the Damned - Volume 1: Princes of Darkness'
  page: 60
  link: http://paizo.com/store/downloads/pathfinder/pathfinderChronicles/pathfinderRPG/v5748btpy8a6f
XP: 3200
alignment: LE
size: Large
type: outsider
subtypes:
- devil
- evil
- extraplanar
- lawful
initiative:
  bonus: 7
senses:
  darkvision: 60
  see in darkness: true
AC:
  AC: 22
  touch: 12
  flat_footed: 19
  components:
    dex: 3
    natural: 10
    size: -1
HP:
  HP: 84
  long: 8d10+40
saves:
  fort: 10
  ref: 9
  will: 5
defensive_abilities:
- construct form
DR:
- amount: 5
  weakness: good
immunities:
- fire
- poison
resistances:
  acid: 10
  cold: 10
SR: 12
speeds:
  base: 40
  climb: 40
attacks:
  melee:
  - - text: mwk trident +13/+8 (2d6+7)
      entries:
      - - damage: 2d6+7
      attack: mwk trident
      bonus:
      - 13
      - 8
    - text: 2 legs +7 (1d8+2) or
      entries: []
      count: 2
      attack: legs +7 (1d8+2) or
  ranged:
  - - text: mwk trident +10 (2d6+7)
      entries:
      - - damage: 2d6+7
      attack: mwk trident
      bonus:
      - 10
  - - text: net +10 ranged touch (entangle)
      entries:
      - - effect: entangle
      attack: net
      bonus:
      - 10
      touch: true
  special:
  - merciless blow
  - Trample (1d8+7, DC 19)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: lemure
      amount: 1d4
    - name: bearded devil
      amount: 1
      chance: 40%
  sources:
  - name: default
    CL: 12
    concentration: 14
ability_scores:
  STR: 20
  DEX: 17
  CON: 19
  INT: 14
  WIS: 16
  CHA: 15
BAB: 8
CMB: 14
CMD: 27
CMD_other: 31 vs. bull rush and trip
feats:
- name: Combat Reflexes
- name: Improved Initiative
- name: Power Attack
- name: Toughness
skills:
  Acrobatics: 14
  Bluff: 13
  Climb: 17
  Craft (weapons): 9
  Intimidate: 13
  Knowledge (dungeoneering): 9
  Knowledge (engineering): 9
  Knowledge (planes): 13
  Perception: 16
  Stealth: 12
    among metal objects or debris: 18
  _racial_mods:
    Perception:
      _: 2
    Stealth:
      _: 2
      among metal objects or debris: 8
languages:
- Celestial
- Draconic
- Infernal
- telepathy 100 ft.
special_qualities:
- hellstrider
- phalanx
- stability
ecology:
  environment: any (Hell)
  organization: solitary, pair, or troop (3-18)
  treasure_type: standard
  treasure:
  - masterwork trident
  - other treasure
special_abilities:
  Construct Form: Despite being true devils, levalochs possess a number of immunities
    common to constructs, including immunity to ability damage, ability drain, death
    effects, death from massive damage, disease, energy drain, exhaustion, fatigue,
    necromancy effects, nonlethal damage, paralysis, sleep effects, and stunning.
    Upon being reduced to 0 hit points, they are immediately destroyed.
  Hellstrider (Su): A levaloch is not impeded by difficult terrain, and can move or
    Charge Through such squares as normal. It can also cross areas covered with dangerous
    impediments (such as caltrops or thorns) without being damaged or hindered. The
    creature's legs are immune to acid and cold, allowing it to cross even rivers
    of acid without being damaged or hindered as long as the hazard is fewer than
    4 feet deep. This ability does not protect a levaloch against magical hindrances
    like black tentacles, web, or similar spells.
  Merciless Blow (Su): Any trident attack a levaloch makes against entangled creatures
    deals an Extra 2d6 points of damage.
  Phalanx (Ex): All devils adjacent to a levaloch gain a +1 morale bonus on attack
    rolls and to AC.
  Stability (Ex): A levaloch gains a +4 bonus to CMD against bull rush and trip.
desc_long: Fearsome giants of steel and blades, levalochs serve the armies of Hell
  as potent warriors and tenacious hunters. They stand just over 10 feet tall and
  weigh 1 ton.

---

# Devil, Warmonger Devil (Levaloch)
Armored like an infernal _[[npcs/Knight|knight]]_ upon some monstrous steed, this fiend of iron and nails scuttles upon six bladed, beetle-like legs.
**Source** Bestiary 5 pg. 81, _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_ - Volume 1: Princes of _[[spells/Darkness|Darkness]]_ pg. 60
**XP** 3,200

LE Large outsider (devil, evil, extraplanar, lawful)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +16

##### Defense

**AC** 22, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+3 Dex, +10 natural, -1 size)
**hp** 84 (8d10+40)
**Fort** +10, **Ref** +9, **Will** +5
**Defensive Abilities** construct form; **DR** 5/good; **Immune** fire, poison; **Resist** acid 10, cold 10; **SR** 12

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 40 ft.
**Melee** mwk _[[items/Weapon/Trident|trident]]_ +13/+8 (2d6+7), 2 legs +7 (1d8+2) or
**Ranged** mwk _trident_ +10 (2d6+7) or _[[items/Mundane/Net|net]]_ +10 ranged touch (_[[spells/Entangle|entangle]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** merciless blow, _[[universal monster rules/Trample|Trample]]_ (1d8+7, DC 19)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +14)
At will—greater teleport (self plus 50 lbs. of objects only)
1/day—_[[universal monster rules/Summon|summon]]_ (level 4, 1d4 lemure or 1 bearded devil 40%)

##### Statistics
**Str** 20, **Dex** 17, **Con** 19, **Int** 14, **Wis** 16, **Cha** 15
**Base Atk** +8; **CMB** +14; **CMD** 27 (31 vs. bull rush and _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_
**Skills** Acrobatics +14, Bluff +13, _Climb_ +17, Craft (weapons) +9, Intimidate +13, Knowledge (dungeoneering, engineering) +9, Knowledge (planes) +13, Perception +16, Stealth +12 (+18 among metal objects or debris); **Racial Modifiers** +2 Perception, +2 Stealth (+8 Stealth among metal objects or debris)
**Languages** Celestial, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** hellstrider, phalanx, stability

##### Ecology

**Environment** any (Hell)
**Organization** solitary, pair, or troop (3-18)
**Treasure** standard (masterwork _trident_, other treasure)

### Special Abilities

**Construct Form** Despite being true devils, levalochs possess a number of immunities common to constructs, including _[[universal monster rules/Immunity|immunity]]_ to ability damage, ability drain, death effects, death from massive damage, disease, _[[universal monster rules/Energy Drain|energy drain]]_, exhaustion, fatigue, necromancy effects, nonlethal damage, _[[universal monster rules/Paralysis|paralysis]]_, sleep effects, and stunning. Upon being reduced to 0 hit points, they are immediately destroyed.

**Hellstrider (Su)** A levaloch is not impeded by difficult terrain, and can move or _[[feats/Charge Through|Charge Through]]_ such squares as normal. It can also cross areas covered with dangerous impediments (such as _[[items/Mundane/Caltrops|caltrops]]_ or thorns) without being damaged or hindered. The creature’s legs are immune to acid and cold, allowing it to cross even rivers of acid without being damaged or hindered as long as the hazard is fewer than 4 feet deep. This ability does not protect a levaloch against magical hindrances like _[[spells/Black Tentacles|black tentacles]]_, web, or similar spells.

**Merciless Blow (Su)** Any _trident_ attack a levaloch makes against _[[conditions/Entangled|entangled]]_ creatures deals an Extra 2d6 points of damage.

**Phalanx (Ex)** All devils adjacent to a levaloch gain a +1 morale bonus on attack rolls and to AC.
**Stability (Ex)** A levaloch gains a +4 bonus to CMD against bull rush and _trip_.

##### Description

Fearsome giants of steel and blades, levalochs serve the armies of Hell as _[[items/Weapon Magic Abilities/Potent|potent]]_ warriors and tenacious hunters. They stand just over 10 feet tall and weigh 1 ton.
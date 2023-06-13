---
cssclass: [monsters]
title1: Asura, Aghasura
desc_short: This immense creature looks like a horned rattlesnake, save for its two
  muscular arms, each of which wields a scimitar.
title2: Aghasura
CR: 11
sources:
- name: Bestiary 3
  page: 22
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 12800
alignment: LE
size: Huge
type: outsider
subtypes:
- asura
- evil
- extraplanar
- lawful
initiative:
  bonus: 3
senses:
  darkvision: 60
  scent: true
auras:
- name: attraction
  radius: 50
- name: elusive
  radius: 75
AC:
  AC: 23
  touch: 11
  flat_footed: 20
  components:
    armor: 6
    dex: 3
    natural: 6
    size: -2
HP:
  HP: 161
  long: 14d10+84
  regeneration: 5
  regeneration_weakness: good weapons, good spells
saves:
  fort: 15
  ref: 9
  will: 11
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
SR: 22
speeds:
  base: 50
  swim: 30
  swim_other: 35 ft., swim 20 ft. in armor
attacks:
  melee:
  - - text: mwk scimitar +26/+21/+16 (2d6+12/15-20 plus poison)
      entries:
      - - damage: 2d6+12
          crit_range: 15-20
        - effect: poison
      attack: mwk scimitar
      bonus:
      - 26
      - 21
      - 16
    - text: mwk scimitar +26 (2d6+12/15-20 plus poison)
      entries:
      - - damage: 2d6+12
          crit_range: 15-20
        - effect: poison
      attack: mwk scimitar
      bonus:
      - 26
    - text: bite +19 (2d8+6 plus grab and poison)
      entries:
      - - damage: 2d8+6
        - effect: grab
        - effect: poison
      attack: bite
      bonus:
      - 19
  special:
  - dual wielder
  - infused weapons
  - swallow whole (2d6+12 acid damage, AC 13, 16 hp)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: deeper darkness
    source: default
    freq: 3/day
  - name: cloudkill
    source: default
    freq: 1/day
    DC: 19
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: 1d4+1 adhukaits
      chance: 20%
    - name: 45%
      chance: 20%
    - name: aghasura
      amount: 1
      chance: 20%
  sources:
  - name: default
    CL: 11
    concentration: 15
ability_scores:
  STR: 34
  DEX: 17
  CON: 23
  INT: 11
  WIS: 14
  CHA: 18
BAB: 14
CMB: 28
CMB_other: +32 grapple
CMD: 41
CMD_other: can't be tripped
feats:
- name: Cleave
- name: Critical Focus
- name: Great Cleave
- name: Improved Critical (scimitar)
- name: Lightning Reflexes
- name: Power Attack
- name: Weapon Focus (scimitar)
skills:
  Acrobatics: 17
  Bluff: 19
  Escape Artist: 6
  Intimidate: 17
  Knowledge (planes): 13
  Perception: 19
  Sense Motive: 19
  Stealth: 9
  Swim: 17
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
  organization: solitary or troop (2-9)
  treasure:
  - standard (masterwork breastplate,
special_abilities:
  Attraction Aura (Su): An aghasura exudes a 50-foot aura whenever it remains motionless
    for at least 1 round. All nonevil creatures that enter this area must make a DC
    21 Will save to avoid being compelled to move toward the aghasura's location.
    If the aghasura moves, the effect ends for all currently affected creatures. This
    is a mind-affecting compulsion. The save DC is Charisma-based.
  Dual Wielder (Ex): An aghasura does not take a penalty on attack or damage rolls
    when attacking with two weapons.
  Infused Weapons (Su): Weapons an aghasura wields are considered to be magic for
    the purposes of overcoming damage reduction. In addition, such weapons gain the
    ability to deliver the aghasura's poison on a successful attack.
  Poison (Ex): Bite or weapon-injury; save Fort DC 23; frequency 1/round for 6 rounds;
    effect 1d4 Con damage; cure 2 consecutive saves.
desc_long: |-
  Aghasuras, or the poison ones, are massive fiends who have perfected the art of ambush and hold to duties of guardianship and butchery. It is said that these frightful ophidian monsters came into being when a deity granted free will to her favorite serpent pets, but when these pets were left to their own devices, they slipped into the deity's favored temple and slew all of her greatest priests. The serpents who survived the deity's wrath became the first aghasuras.

  An aghasura is 30 feet long and weighs nearly 7 tons.

---

# Asura, Aghasura
This immense creature looks like a horned rattlesnake, save for its two muscular arms, each of which wields a _[[items/Weapon/Scimitar|scimitar]]_.
**Source** Bestiary 3 pg. 22
**XP** 12,800

LE Huge outsider (asura, evil, extraplanar, lawful)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +19
**Aura** attraction (50 ft.), elusive (75 ft.)

##### Defense

**AC** 23, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+6 armor, +3 Dex, +6 natural, –2 size)
**hp** 161 (14d10+84); _[[universal monster rules/Regeneration|regeneration]]_ 5 (good weapons, good spells)
**Fort** +15, **Ref** +9, **Will** +11; +2 vs. enchantment spells
**DR** 10/good; **Immune** curse effects, disease, poison; **Resist** acid 10, electricity 10; **SR** 22

##### Offense
**Speed** 50 ft., swim 30 ft. (35 ft., swim 20 ft. in armor)
**Melee** mwk _scimitar_ +26/+21/+16 (2d6+12/15-20 plus poison), mwk _scimitar_ +26 (2d6+12/15-20 plus poison), bite +19 (2d8+6 plus _[[universal monster rules/Grab|grab]]_ and poison)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** dual wielder, infused weapons, _[[universal monster rules/Swallow Whole|swallow whole]]_ (2d6+12 acid damage, AC 13, 16 hp)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +15)
At will—greater teleport (self plus 50 lbs. of objects only)
3/day—_[[spells/Deeper Darkness|deeper darkness]]_
1/day—_[[spells/Cloudkill|cloudkill]]_ (DC 19), _[[universal monster rules/Summon|summon]]_ (level 4, 1d4+1 adhukaits, 45%, or 1 aghasura, 20%)

##### Statistics
**Str** 34, **Dex** 17, **Con** 23, **Int** 11, **Wis** 14, **Cha** 18
**Base Atk** +14; **CMB** +28 (+32 grapple); **CMD** 41 (can’t be tripped)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Critical|Improved Critical]]_ (_scimitar_), _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_scimitar_)
**Skills** Acrobatics +17, Bluff +19, Escape Artist +6, Intimidate +17, Knowledge (planes) +13, Perception +19, Sense Motive +19, Stealth +9, Swim +17; **Racial Modifiers** +6 Escape Artist, +4 Perception
**Languages** Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Hell)
**Organization** solitary or troop (2–9)
**Treasure** standard (masterwork _[[items/Armor/Breastplate|breastplate]]_,

### Special Abilities

**Attraction Aura (Su)** An aghasura exudes a 50-foot aura whenever it remains motionless for at least 1 round. All nonevil creatures that enter this area must make a DC 21 Will save to avoid being compelled to move toward the aghasura’s location. If the aghasura moves, the effect ends for all currently affected creatures. This is a mind-affecting compulsion. The save DC is Charisma-based.

**Dual Wielder (Ex) **An aghasura does not take a penalty on attack or damage rolls when attacking with two weapons.

**Infused Weapons (Su)** Weapons an aghasura wields are considered to be magic for the purposes of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_. In addition, such weapons gain the ability to deliver the aghasura’s poison on a successful attack.

**Poison (Ex)** Bite or weapon—injury; save Fort DC 23; frequency 1/round for 6 rounds; effect 1d4 Con damage; cure 2 consecutive saves.

##### Description

Aghasuras, or the poison ones, are massive fiends who have perfected the art of ambush and hold to duties of guardianship and butchery. It is said that these frightful ophidian monsters came into being when a deity granted free will to her favorite serpent pets, but when these pets were left to their own devices, they slipped into the deity’s favored temple and slew all of her greatest priests. The serpents who survived the deity’s wrath became the first aghasuras.

An aghasura is 30 feet long and weighs nearly 7 tons.
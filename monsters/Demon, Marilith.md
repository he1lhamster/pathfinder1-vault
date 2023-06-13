---
cssclass: [monsters]
title1: Demon, Marilith
desc_short: This snake-bodied woman has six arms, yet her cruel weapons float in the
  air, glistening with poison.
title2: Mythic Marilith
CR: 21
MR: 8
sources:
- name: Mythic Adventures
  page: 182
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 409600
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
- mythic
initiative:
  bonus: 4
senses:
  darkvision: 60
  true seeing: true
auras:
- name: unholy aura
  DC: 26
AC:
  AC: 40
  touch: 17
  flat_footed: 36
  components:
    deflection: 4
    dex: 4
    natural: 23
    size: -1
HP:
  HP: 344
  long: 16d10+256
  fast_healing: 5
saves:
  fort: 25
  ref: 18
  will: 13
DR:
- amount: 10
  weakness: cold iron and epic and good
immunities:
- cold
- fire
- electricity
- poison
resistances:
  acid: 10
SR: 32
speeds:
  base: 40
attacks:
  melee:
  - - text: +2 longsword +28/+23/+18/+13 (2d6+12/16-20 plus poison)
      entries:
      - - damage: 2d6+12
          crit_range: 16-20
        - effect: poison
      attack: +2 longsword
      bonus:
      - 28
      - 23
      - 18
      - 13
    - text: 5 +2 longswords +28 (2d6+7/16-20 plus poison)
      entries:
      - - damage: 2d6+7
          crit_range: 16-20
        - effect: poison
      count: 5
      attack: +2 longswords
      bonus:
      - 28
    - text: tail slap +20 (2d6+5 plus grab)
      entries:
      - - damage: 2d6+5
        - effect: grab
      attack: tail slap
      bonus:
      - 20
  special:
  - constrict (tail slap, 2d6+15 plus crushing coils)
  - greater infuse weapon
  - multiweapon mastery
  - mythic power (8/day, surge +1d10)
  - poisoned weapons
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 26
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: project image
    source: default
    freq: At will
    DC: 25
  - name: telekinesis
    source: default
    freq: At will
    DC: 23
  - name: blade barrier
    source: default
    freq: 3/day
    DC: 24
  - name: fly
    source: default
    freq: 3/day
  - name: heal
    source: default
    freq: 3/day
    other: self only
  - name: summon
    source: default
    freq: 1/day
    level: 5
    summons:
    - name: marilith
      amount: 1
      chance: 20%
    - name: nalfeshnee
      amount: 1
      chance: 35%
    - name: hezrous
      amount: 1d4
      chance: 60%
  sources:
  - name: default
    CL: 16
    concentration: 24
ability_scores:
  STR: 31
  DEX: 19
  CON: 32
  INT: 18
  WIS: 18
  CHA: 27 Base Atk +16; CMB +27 (+29 disarm
BAB: ''
CMB:
CMD:
feats:
- is_mythic: true
  name: Bleeding Critical
- is_mythic: true
  name: Combat Expertise
- name: Combat Reflexes
- is_mythic: true
  name: Critical Focus
- is_mythic: true
  name: Improved Critical (longsword)
- name: Improved Disarm
- name: Power Attack
- name: Weapon Focus (longsword)
skills:
  Acrobatics: 23
  Bluff: 27
  Diplomacy: 27
  Fly: 18
  Intimidate: 27
  Knowledge (engineering): 20
  Perception: 31
  Sense Motive: 23
  Stealth: 19
  Use Magic Device: 27
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
special_qualities:
- change shape (any animal, humanoid, or giant; shapechange)
ecology:
  environment: any (Abyss)
  organization: solitary, pair, or platoon (1 marilith, 1-3 glabrezus, and 3-14 babaus)
  treasure_type: double
  treasure:
  - 6 mwk longswords
  - other treasure
special_abilities:
  Crushing Coils (Ex): A constricted creature must succeed at a DC 28 Fortitude save
    or lose consciousness for 1d8 rounds. The save DC is Strength-based.
  Greater Infuse Weapon (Su): Any weapon a mythic marilith wields gains a +2 enhancement
    bonus and counts as a chaotic and evil cold iron weapon. She can expend two uses
    of mythic power as an immediate action to add the dancing special ability to all
    her manufactured weapons for 4 rounds.
  Poisoned Weapons (Ex): As a swift action, a mythic marilith can lick one of her
    manufactured weapons to coat it with deathblade poison (Pathfinder RPG Core Rulebook
    558).
desc_long: A mythic marilith is a queen of chaos and evil, controlling a large territory
  in the Abyss and commanding a legion of demons.

---

# Demon, Marilith
This snake-bodied fiend has a six-armed woman’s torso, pointed ears, and glittering, otherworldly eyes.
**Source** Pathfinder RPG Bestiary pg. 63
**XP** 102,400
CE Large outsider (chaotic, demon, evil, extraplanar)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +31
**Aura** _[[spells/Unholy Aura|unholy aura]]_ (DC 25)

##### Defense

**AC** 32, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+4 deflection, +4 Dex, +15 natural, –1 size)
**hp** 264 (16d10+176)
**Fort** +25, **Ref** +18, **Will** +13
**DR** 10/cold iron and good; **Immune** electricity and poison; **Resist** acid 10, cold 10, fire 10; **SR** 28

##### Offense
**Speed** 40 ft.
**Melee** +1 _[[items/Weapon/Longsword|longsword]]_ +24/+19/+14/+9 (2d6+8/17–20), 5 +1 longswords +24 (2d6+4/17–20), tail slap +17 (2d6+3 plus _[[universal monster rules/Grab|grab]]_) or 6 slams +22 (1d8+7), tail slap +17 (2d6+3 plus _grab_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (tail slap, 2d6+10 plus crushing coils), infuse weapon, _[[universal monster rules/Multiweapon Mastery|multiweapon mastery]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th)
Constant—_true seeing_, _unholy aura_ (DC 25)
At will—greater teleport (self plus 50 lbs. of objects only), _[[spells/Project Image|project image]]_ (DC 24), _[[spells/Telekinesis|telekinesis]]_ (DC 22)
3/day—_[[spells/Blade Barrier|blade barrier]]_ (DC 23), fly
1/day—_[[universal monster rules/Summon|summon]]_ (level 5, 1 marilith 20%, 1 nalfeshnee at 35%, or 1d4 hezrous at 60%)

##### Statistics
**Str** 25, **Dex** 19, **Con** 32, **Int** 18, **Wis** 18, **Cha** 25
**Base Atk** +16; **CMB** +24 (+28 grapple); **CMD** 42 (can’t be tripped)
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (_longsword_), _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_longsword_)
**Skills** Acrobatics +23, Bluff +26, Diplomacy +26, Fly +18, Intimidate +26, Knowledge (engineering) +20, Perception +31, Sense Motive +23, Stealth +19, Use Magic Device +26; **Racial Modifiers** +8 Perception
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abyss)
**Organization** solitary, pair, or platoon (1 marilith, 1–3 glabrezus, and 3–14 babaus)
**Treasure** double (6 mwk longswords, other treasure)

### Special Abilities

**Crushing Coils (Ex)** A creature that takes damage from a marilith’s _constrict_ attack must succeed on a DC 25 Fortitude save or lose consciousness for 1d8 rounds. The save DC is Strength-based.

**Infuse Weapon (Su)** Any weapon a marilith wields gains a +1 enhancement bonus to attack and damage, and strikes as if it were a chaotic and evil cold iron weapon (in addition to retaining the qualities of its actual composition).

**_Multiweapon Mastery_ (Ex)** A marilith never takes penalties to her attack roll when fighting with multiple weapons.

##### Description

The leaders of Abyssal hordes and queens of Abyssal nations, the dreaded mariliths serve demon lords as governesses, advisors, and even lovers, yet their brilliance as tacticians makes them most sought after as generals and commanders of armies. The most powerful mariliths serve no one, and instead _[[spells/Command|command]]_ _[[curses/Ravenous|ravenous]]_ fiendish legions.

A marilith is 6 to 9 feet tall and measures 20 feet from head to tail tip. It weighs 4,000 pounds. Only the most arrogant and proud evil souls, typically those of _[[items/Weapon Magic Abilities/Cruel|cruel]]_ kings, sadistic generals, and exceptionally violent warlords, can trigger the manifestation of a marilith.
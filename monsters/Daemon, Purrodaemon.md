---
cssclass: [monsters]
title1: Daemon, Purrodaemon
desc_short: 'Dozens of weapons pierce this massive monster's body. Red eyes glow with
  wickedness in its vulture-like head. '
title2: Purrodaemon
CR: 18
sources:
- name: Bestiary 2
  page: 73
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 153600
alignment: NE
size: Large
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 10
senses:
  darkvision: 60
  true seeing: true
auras:
- name: fear
  radius: 15
  DC: 24
- name: unholy aura
AC:
  AC: 35
  touch: 19
  flat_footed: 29
  components:
    deflection: 4
    dex: 6
    natural: 16
    size: -1
HP:
  HP: 294
  long: 19d10+190
saves:
  fort: 25
  ref: 21
  will: 14
DR:
- amount: 10
  weakness: good and silver
immunities:
- acid
- death effects
- disease
- poison
resistances:
  cold: 10
  electricity: 10
  fire: 10
SR: 29
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: +2 wounding halberd (2d8+18/19-20/x3)
      entries:
      - - damage: 2d8+18
          crit_range: 19-20
          crit_multiplier: 3
      attack: +2 wounding halberd
    - text: bite +24 (1d8+5)
      entries:
      - - damage: 1d8+5
      attack: bite
      bonus:
      - 24
  special:
  - weapon steep
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
    DC: 23
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: chain lightning
    source: default
    freq: 3/day
    DC: 21
  - name: cone of cold
    source: default
    freq: 3/day
    DC: 20
  - name: flame strike
    source: default
    freq: 3/day
    DC: 20
  - name: summon
    source: default
    freq: 1/day
    level: 5
    summons:
    - name: derghodaemons
      amount: 2
      chance: 50%
  sources:
  - name: default
    CL: 18
    concentration: 23
ability_scores:
  STR: 32
  DEX: 23
  CON: 30
  INT: 17
  WIS: 18
  CHA: 21
BAB: 19
CMB: 31
CMD: 51
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Greater Vital Strike
- is_bonus: true
  name: Improved Critical (halberd)
- name: Improved Initiative
- name: Improved Sunder
- name: Improved Vital Strike
- name: Lunge
- name: Power Attack
- name: Quick Draw
- name: Vital Strike
- is_bonus: true
  name: Weapon Focus (halberd)
skills:
  Acrobatics: 28
  Bluff: 21
  Diplomacy: 17
  Fly: 16
  Intimidate: 27
  Knowledge (planes): 25
  Perception: 26
  Sense Motive: 26
  Spellcraft: 23
  Stealth: 24
  Survival: 17
languages:
- Abyssal
- Draconic
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Abaddon)
  organization: solitary, patrol (2-5), or unit (6-12)
  treasure_type: standard
special_abilities:
  Weapon Steep (Su): A purrodaemon can sheathe a weapon in its flesh as a swift action.
    This does no damage to the daemon. If a weapon remains sheathed in its body for
    at least 24 hours, the weapon absorbs some of its essence and gains magical enhancements.
    A purrodaemon can have up to a dozen weapons lodged in its body at a time, but
    only one can possess magical enhancements at a time. The total enhancements cannot
    exceed a +4 effective enhancement-most purrodaemons opt to create +2 wounding
    weapons in this manner. A weapon's enhancements vanish as soon as the purrodaemon
    dies or releases the weapon. A purrodaemon gains Weapon Focus and Improved Critical
    as bonus feats as long as it wields a weapon benefiting from its weapon steep
    ability.
desc_long: Deacons of War, purrodaemons ravage the planes as generals of massive battles.
  They employ creative tactics and never launch an assault without carefully looking
  over the plans or surveying the battlefield themselves. A purrodaemon is 12 feet
  tall and weighs 1,300 pounds.

---

# Daemon, Purrodaemon
Dozens of weapons pierce this massive monster’s body. Red eyes glow with wickedness in its vulture-like head.

**Source** Bestiary 2 pg. 73
**XP** 153,600

NE Large outsider (daemon, evil, extraplanar)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +26
**Aura** _[[universal monster rules/Fear|fear]]_ (15 ft., DC 24), _[[spells/Unholy Aura|unholy aura]]_

##### Defense

**AC** 35, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 29 (+4 deflection, +6 Dex, +16 natural, –1 size)
**hp** 294 (19d10+190)
**Fort** +25, **Ref** +21, **Will** +14
**DR** 10/good and silver; **Immune** acid, death effects, disease, poison; **Resist** cold 10, electricity 10, fire 10; **SR** 29

##### Offense
**Speed** 30 ft., fly 60 ft. (good)
**Melee** +2 _[[items/Weapon Magic Abilities/Wounding|wounding]]_ _[[items/Weapon/Halberd|halberd]]_ (2d8+18/19-20/x3), bite +24 (1d8+5)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** weapon steep
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +23)
Constant—_true seeing_, _unholy aura_ (DC 23)
At will—greater teleport (self plus 50 lbs. of objects only)
3/day—_[[spells/Chain Lightning|chain lightning]]_ (DC 21), _[[spells/Cone of Cold|cone of cold]]_ (DC 20), _[[spells/Flame Strike|flame strike]]_ (DC 20)
1/day—_[[universal monster rules/Summon|summon]]_ (level 5, 2 derghodaemons 50%)

##### Statistics
**Str** 32, **Dex** 23, **Con** 30, **Int** 17, **Wis** 18, **Cha** 21
**Base Atk** +19; **CMB** +31; **CMD** 51
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (_halberd_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quick Draw|Quick Draw]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_halberd_)
**Skills** Acrobatics +28, Bluff +21, Diplomacy +17, Fly +16, Intimidate +27, Knowledge (planes) +25, Perception +26, Sense Motive +26, Spellcraft +23, Stealth +24, Survival +17
**Languages** Abyssal, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary, patrol (2–5), or unit (6–12)
**Treasure** standard

### Special Abilities

**Weapon Steep (Su)** A purrodaemon can sheathe a weapon in its flesh as a swift action. This does no damage to the daemon. If a weapon remains sheathed in its body for at least 24 hours, the weapon absorbs some of its essence and gains magical enhancements. A purrodaemon can have up to a dozen weapons lodged in its body at a time, but only one can possess magical enhancements at a time. The total enhancements cannot exceed a +4 effective enhancement—most purrodaemons opt to create +2 _wounding_ weapons in this manner. A weapon’s enhancements _[[spells/Vanish|vanish]]_ as soon as the purrodaemon dies or releases the weapon. A purrodaemon gains _Weapon Focus_ and _Improved Critical_ as bonus feats as long as it wields a weapon benefiting from its weapon steep ability.

##### Description

Deacons of War, purrodaemons ravage the planes as generals of massive battles. They employ creative tactics and never launch an assault without carefully looking over the plans or surveying the battlefield themselves. A purrodaemon is 12 feet tall and weighs 1,300 pounds.
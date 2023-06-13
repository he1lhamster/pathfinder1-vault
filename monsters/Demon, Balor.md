---
cssclass: [monsters]
title1: Demon, Balor
desc_short: This winged fiend's horned head and fanged visage present the perfection
  of the demonic form, fire spurting from its flesh.
title2: Balor
CR: 20
sources:
- name: Pathfinder RPG Bestiary
  page: 58
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 307200
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 11
senses:
  darkvision: 60
  low-light vision: true
  true seeing: true
auras:
- name: flaming body
- name: unholy aura
  DC: 26
AC:
  AC: 36
  touch: 20
  flat_footed: 29
  components:
    deflection: 4
    dex: 7
    natural: 16
    size: -1
HP:
  HP: 370
  long: 20d10+260
saves:
  fort: 29
  ref: 17
  will: 25
DR:
- amount: 15
  weakness: cold iron and good
immunities:
- electricity
- fire
- poison
resistances:
  acid: 10
  cold: 10
SR: 31
speeds:
  base: 40
  fly: 90
  fly_maneuverability: good
attacks:
  melee:
  - - text: +1 vorpal unholy longsword +31/+26/+21/+16 (2d6+13)
      entries:
      - - damage: 2d6+13
      attack: +1 vorpal unholy longsword
      bonus:
      - 31
      - 26
      - 21
      - 16
    - text: +1 vorpal flaming whip +30/+25/+20 (1d4+7 plus 1d6 fire and entangle)
      entries:
      - - damage: 1d4+7
        - damage: 1d6
          type: fire
        - effect: entangle
      attack: +1 vorpal flaming whip
      bonus:
      - 30
      - 25
      - 20
  - - text: 2 slams +31 (1d10+12)
      entries:
      - - damage: 1d10+12
      count: 2
      attack: slams
      bonus:
      - 31
space: 10
reach: 10
reach_other: 20 ft. with whip
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 26
  - name: dominate monster
    source: default
    freq: At will
    DC: 27
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: power word stun
    source: default
    freq: At will
  - name: telekinesis
    source: default
    freq: At will
    DC: 23
  - name: quickened telekinesis
    source: default
    freq: 3/day
    DC: 23
  - name: blasphemy
    source: default
    freq: 1/day
    DC: 25
  - name: fire storm
    source: default
    freq: 1/day
    DC: 26
  - name: implosion
    source: default
    freq: 1/day
    DC: 27
  - name: summon
    source: default
    freq: 1/day
    level: 9
    summons:
    - name: any 1 CR 19
    - name: lower demon
      chance: 100%
  sources:
  - name: default
    CL: 20
ability_scores:
  STR: 35
  DEX: 25
  CON: 36
  INT: 24
  WIS: 24
  CHA: 27
BAB: 20
CMB: 33
CMD: 54
feats:
- name: Cleave
- name: Combat Reflexes
- name: Greater Two-Weapon Fighting
- name: Improved Initiative
- name: Improved Two-Weapon Fighting
- name: Iron Will
- name: Power Attack
- name: Quicken Spell-Like Ability (telekinesis)
- name: Two-Weapon Fighting
- name: Weapon Focus (longsword)
skills:
  Acrobatics: 27
  Bluff: 31
  Diplomacy: 31
  Fly: 32
  Intimidate: 31
  Knowledge (history): 27
  Knowledge (nobility): 27
  Knowledge (planes): 30
  Knowledge (religion): 27
  Perception: 38
  Sense Motive: 30
  Stealth: 26
  Use Magic Device: 31
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
special_qualities:
- death throes
- vorpal strike
- whip mastery
ecology:
  environment: any (Abyss)
  organization: solitary or warband (1 balor and 2-5 glabrezus)
  treasure_type: standard
  treasure:
  - +1 unholy longsword
  - +1 flaming whip
  - other treasure
special_abilities:
  Death Throes (Su): When killed, a balor explodes in a blinding flash of fire that
    deals 100 points of damage (half fire, half unholy damage) to anything within
    100 feet (Reflex DC 33 halves). The save DC is Constitution-based.
  Entangle (Ex): If a balor strikes a Medium or smaller foe with its whip, the balor
    can immediately attempt a grapple check without provoking an attack of opportunity.
    If the balor wins the check, it draws the foe into an adjacent square. The foe
    gains the grappled condition, but the balor does not.
  Flaming Body (Su): A balor's body is covered in dancing flames. Anyone striking
    a balor with a natural weapon or unarmed strike takes 1d6 points of fire damage.
    A creature that grapples a balor or is grappled by one takes 6d6 points of fire
    damage each round the grapple persists.
  Vorpal Strike (Su): Any slashing weapon a balor wields (including its standard longsword
    and whip) gains the vorpal weapon quality. Weapons retain this quality for one
    hour after the balor releases the weapon, but after this the weapon reverts to
    its standard magical qualities, if any.
  Whip Mastery (Ex): A balor treats a whip as a light weapon for the purposes of two-weapon
    fighting, and can inflict lethal damage on a foe regardless of the foe's armor.
desc_long: |-
  When folk whisper frightened tales of the demonic, what most envision is a towering figure of fire and flesh, a horned nightmare armed with flaming whip and sword flying through the night in search of its latest victim. The demon these folk fear is the balor, and that fear is justly placed, for few demons can match the mighty balor in strength or brutality.

  On the Abyss, most balors serve demon lords as generals or captains (those balors who don't are even more potent, and are known as balor lords-see below). A balor typically commands vast legions of demons, and while it often lets these slavering and eager minions fight its battles, the balor is far from a coward. If presented with an opportunity to join a fight, few balors choose to resist.

  In combat, a balor relies upon its spell-like abilities to fight foes wise enough to avoid melee range, favoring destructive powers like fire storm or implosion and saving dominate monster for use against the rare foe it would prefer to capture alive. A balor usually uses telekinesis to disarm ranged weapons or pull foes into melee-with the use of a quickened telekinesis, a balor can use the latter tactic and still inflict a full-round attack on a hapless foe. A balor reduced to fewer than 50 hit points almost always seeks to flee via teleportation, but if that and flight prove impossible it seeks to position itself such that, if it is slain, its death throes are as devastating as possible to the enemy host.

  A balor stands 14 feet in height and weighs 4,500 pounds. Only the cruelest mortal souls can fuel the creation of a balor-unlike in the cases of most other demons, it often takes multiple souls of powerful villains to trigger the birthing of a new balor.

---

# Demon, Balor
This winged fiend’s horned head and fanged visage present the perfection of the demonic form, fire spurting from its flesh.
**Source** Pathfinder RPG Bestiary pg. 58
**XP** 307,200
CE Large outsider (chaotic, demon, evil, extraplanar)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/True Seeing|true seeing]]_; Perception +38
**Aura** _[[items/Weapon Magic Abilities/Flaming|flaming]]_ body, _[[spells/Unholy Aura|unholy aura]]_ (DC 26)

##### Defense

**AC** 36, touch 20, _[[conditions/Flat-Footed|flat-footed]]_ 29 (+4 deflection, +7 Dex, +16 natural, –1 size)
**hp** 370 (20d10+260)
**Fort** +29, **Ref** +17, **Will** +25
**DR** 15/cold iron and good; **Immune** electricity, fire, poison; **Resist** acid 10, cold 10; **SR** 31

##### Offense
**Speed** 40 ft., fly 90 ft. (good)
**Melee** +1 _[[items/Weapon Magic Abilities/Vorpal|vorpal]]_ _[[items/Weapon Magic Abilities/Unholy|unholy]]_ _[[items/Weapon/Longsword|longsword]]_ +31/+26/+21/+16 (2d6+13), +1 _vorpal_ _flaming_ _[[items/Weapon/Whip|whip]]_ +30/+25/+20 (1d4+7 plus 1d6 fire and _[[spells/Entangle|entangle]]_) or 2 slams +31 (1d10+12)
**Space** 10 ft., **Reach** 10 ft. (20 ft. with _whip_)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th)
Constant—_true seeing_, _unholy aura_ (DC 26)
At will—_[[spells/Dominate Monster|dominate monster]]_ (DC 27), greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport (self plus 50 lbs. of objects only), _[[spells/Power Word Stun|power word stun]]_, _[[spells/Telekinesis|telekinesis]]_ (DC 23)
3/day—quickened _telekinesis_ (DC 23)
1/day—_[[spells/Blasphemy|blasphemy]]_ (DC 25), _[[spells/Fire Storm|fire storm]]_ (DC 26), _[[spells/Implosion|implosion]]_ (DC 27), _[[universal monster rules/Summon|summon]]_ (level 9, any 1 CR 19 or lower demon 100%)

##### Statistics
**Str** 35, **Dex** 25, **Con** 36, **Int** 24, **Wis** 24, **Cha** 27
**Base Atk** +20; **CMB** +33; **CMD** 54
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Greater Two-Weapon Fighting|Greater Two-Weapon Fighting]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Two-Weapon Fighting|Improved Two-Weapon Fighting]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_telekinesis_), _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_longsword_)
**Skills** Acrobatics +27, Bluff +31, Diplomacy +31, Fly +32, Intimidate +31, Knowledge (history) +27, Knowledge (nobility) +27, Knowledge (planes) +30, Knowledge (religion) +27, Perception +38, Sense Motive +30, Stealth +26, Use Magic Device +31; **Racial Modifiers** +8 Perception
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** death throes, _vorpal_ strike, _[[feats/Whip Mastery|whip mastery]]_

##### Ecology

**Environment** any (Abyss)
**Organization** solitary or warband (1 balor and 2–5 glabrezus)
**Treasure** standard (+1 _unholy_ _longsword_, +1 _flaming_ _whip_, other treasure)

### Special Abilities

**Death Throes (Su) **When killed, a balor explodes in a _[[feats/Blinding Flash|blinding flash]]_ of fire that deals 100 points of damage (half fire, half _unholy_ damage) to anything within 100 feet (Reflex DC 33 halves). The save DC is Constitution-based.

**_Entangle_ (Ex) **If a balor strikes a _[[classes/Medium|Medium]]_ or smaller foe with its _whip_, the balor can immediately attempt a grapple check without provoking an attack of opportunity. If the balor wins the check, it draws the foe into an adjacent square. The foe gains the _[[conditions/Grappled|grappled]]_ condition, but the balor does not.

**_Flaming_ Body (Su)** A balor’s body is covered in _[[items/Weapon Magic Abilities/Dancing|dancing]]_ flames. Anyone striking a balor with a natural weapon or unarmed strike takes 1d6 points of fire damage. A creature that grapples a balor or is _grappled_ by one takes 6d6 points of fire damage each round the grapple persists.

**_Vorpal_ Strike (Su)** Any slashing weapon a balor wields (including its standard _longsword_ and _whip_) gains the _vorpal_ weapon quality. Weapons retain this quality for one hour after the balor releases the weapon, but after this the weapon reverts to its standard magical qualities, if any.

**_Whip Mastery_ (Ex)** A balor treats a _whip_ as a light weapon for the purposes of _two-weapon fighting_, and can inflict lethal damage on a foe regardless of the foe’s armor.

##### Description

When folk whisper _[[conditions/Frightened|frightened]]_ tales of the demonic, what most envision is a towering figure of fire and flesh, a horned _[[spells/Nightmare|nightmare]]_ armed with _flaming_ _whip_ and sword flying through the night in search of its latest victim. The demon these folk _[[universal monster rules/Fear|fear]]_ is the balor, and that _fear_ is justly placed, for few demons can match the mighty balor in strength or brutality.

On the Abyss, most balors serve demon lords as generals or captains (those balors who don’t are even more _[[items/Weapon Magic Abilities/Potent|potent]]_, and are known as balor lords—see below). A balor typically commands vast legions of demons, and while it often lets these slavering and eager minions fight its battles, the balor is far from a coward. If presented with an opportunity to join a fight, few balors choose to resist.

In combat, a balor relies upon its _spell-like abilities_ to fight foes wise enough to avoid melee range, favoring destructive powers like _fire storm_ or _implosion_ and saving _dominate monster_ for use against the rare foe it would prefer to capture alive. A balor usually uses _telekinesis_ to disarm ranged weapons or _[[universal monster rules/Pull|pull]]_ foes into melee—with the use of a quickened _telekinesis_, a balor can use the latter tactic and still inflict a full-round attack on a hapless foe. A balor reduced to fewer than 50 hit points almost always seeks to flee via teleportation, but if that and _[[universal monster rules/Flight|flight]]_ prove impossible it seeks to position itself such that, if it is slain, its death throes are as devastating as possible to the enemy host.

A balor stands 14 feet in height and weighs 4,500 pounds. Only the cruelest mortal souls can fuel the creation of a balor—unlike in the cases of most other demons, it often takes multiple souls of powerful villains to trigger the birthing of a new balor.
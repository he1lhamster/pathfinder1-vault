---
cssclass: [monsters]
title1: Demon Lord, Xoveron
desc_short: This hulking, four-armed, four-headed, sting-tailed gargoyle stands as
  tall as a house.
title2: Xoveron
CR: 27
sources:
- name: 'Pathfinder #73: The Worldwound Incursion'
  page: 84
  link: http://paizo.com/products/btpy90q9?Pathfinder-Adventure-Path-73-The-Worldwound-Incursion
XP: 3276800
alignment: CE
size: Huge
type: outsider
initiative:
  bonus: 6
senses:
  darkvision: 60
  detect good: true
  detect law: true
  true seeing: true
auras:
- name: frightful presence
  radius: 120
  DC: 35
- name: unholy aura
  DC: 27
AC:
  AC: 45
  touch: 30
  flat_footed: 39
  components:
    deflection: 4
    dex: 6
    natural: 15
    profane: 12
    size: -2
HP:
  HP: 643
  long: 33d10+462
  regeneration: 30
  regeneration_weakness: mythic or deific
saves:
  fort: 36
  ref: 23
  will: 33
defensive_abilities:
- Abyssal resurrection
- freedom of movement
DR:
- amount: 20
  weakness: cold iron, good, and epic
immunities:
- ability damage and drain
- acid
- charm and compulsion effects
- death effects
- electricity
- level drain
- petrification
- poison
resistances:
  cold: 30
  fire: 30
SR: 38
speeds:
  base: 50
  fly: 80
  fly_maneuverability: good
attacks:
  melee:
  - - text: 4 claws +48 (1d8+17/19-20)
      entries:
      - - damage: 1d8+17
          crit_range: 19-20
      count: 4
      attack: claws
      bonus:
      - 48
    - text: 4 bites +48 (2d6+17/19-20)
      entries:
      - - damage: 2d6+17
          crit_range: 19-20
      count: 4
      attack: bites
      bonus:
      - 48
    - text: sting +48 (1d8+17/19-20 plus poison)
      entries:
      - - damage: 1d8+17
          crit_range: 19-20
        - effect: poison
      attack: sting
      bonus:
      - 48
  special:
  - devastating blow
  - feed
  - poison
  - rend (2 claws, 2d8+25)
  - roar
  - shatter petrification
  - shockwave
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 27
  - name: astral projection
    source: default
    freq: At will
  - name: blasphemy
    source: default
    freq: At will
    DC: 26
  - name: desecrate
    source: default
    freq: At will
  - name: flesh to stone
    source: default
    freq: At will
    DC: 25
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
  - name: shapechange
    source: default
    freq: At will
  - name: stone shape
    source: default
    freq: At will
  - name: telekinesis
    source: default
    freq: At will
    DC: 24
  - name: unhallow
    source: default
    freq: At will
  - name: unholy blight
    source: default
    freq: At will
    DC: 23
  - name: earthquake
    source: default
    freq: 3/day
  - name: quickened flesh to stone
    source: default
    freq: 3/day
    DC: 25
  - name: reverse gravity
    source: default
    freq: 3/day
  - name: symbol of weakness
    source: default
    freq: 3/day
    DC: 26
  - name: implosion
    source: default
    freq: 1/day
    DC: 28
  - name: imprisonment
    source: default
    freq: 1/day
    DC: 28
  - name: time stop
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 27
    concentration: 36
ability_scores:
  STR: 44
  DEX: 23
  CON: 38
  INT: 24
  WIS: 32
  CHA: 28
BAB: 33
CMB: 52
CMB_other: +56 bull rush, +56 sunder
CMD: 86
CMD_other: 88 vs. bull rush, 88 vs. sunder
feats:
- name: Awesome Blow
- name: Bleeding Critical
- name: Craft Construct
- name: Craft Magic Arms and Armor
- name: Craft Wondrous Item
- name: Critical Focus
- name: Greater Bull Rush
- name: Greater Sunder
- name: Improved Bull Rush
- name: Improved Critical (claw)
- name: Improved Critical (bite)
- name: Improved Critical (sting)
- name: Improved Lightning Reflexes
- name: Improved Sunder
- name: Lightning Reflexes
- name: Power Attack
- name: Quicken Spell-Like Ability (flesh to stone)
skills:
  Acrobatics: 39
    when jumping: 47
  Disable Device: 42
  Fly: 42
  Intimidate: 45
  Knowledge (arcana): 40
  Knowledge (religion): 40
  Knowledge (engineering): 43
  Knowledge (planes): 43
  Perception: 55
  Sense Motive: 47
  Spellcraft: 43
  Stealth: 34
  Use Magic Device: 42
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Common
- Draconic
- Terran
- telepathy 300 ft.
ecology:
  environment: any (Ghahazi, Abyss)
  organization: solitary (unique)
  treasure_type: triple
special_abilities:
  Devastating Blow (Su): As a standard action, Xoveron can bring all four of his claws
    to bear upon a single target. It this attack hits, he deals 8d8+68 points of bludgeoning
    damage. If the target is a creature, it must make a successful DC 43 Fortitude
    save or be knocked prone and staggered for 1d4 rounds. If the target is an object,
    the attack ignores all hardness possessed by the object. The save DC is Strength-based.
  Feed (Su): Xoveron can consume the corpse of a Large or smaller creature that has
    been dead no longer than a day as a full-round action. Doing so destroys the creature's
    body and leaves its gear scattered on the ground. All armor and gear worn in the
    body slot must make a successful DC 43 Fortitude save to avoid becoming broken
    by this swift and violent consumption. When Xoveron feeds on a creature, he immediately
    learns all of that creature's memories and knowledge. In addition, he gains the
    effects of a heal spell and a haste spell (both at CL 27th). The save DC is Strength-based.
  Poison (Ex): Sting-injury; save Fort DC 40; frequency 1/round for 6 rounds; effect
    1d6 Dexterity drain; cure 3 consecutive saves. If a creature's Dexterity is drained
    to 0, the creature is immediately petrified. The save DC is Constitution-based.
  Roar (Su): Xoveron can unleash a devastating roar as a standard action once per
    hour. When he roars, all creatures and unattended objects within 60 feet take
    30d10 points of sonic damage and become stunned for 1d6 rounds. Xoveron does not
    take this damage, and he can exclude any number of creatures or objects from this
    effect as he wills. A successful DC 40 Reflex save halves the damage and negates
    the stun effect. The save DC is Constitution-based.
  Shatter Petrification (Su): Xoveron can strike a petrified creature with any one
    of his natural weapon attacks to cause it to shatter. The petrified creature can
    resist this with a successful DC 43 Fortitude save. If the creature fails to resist,
    the blow smashes it apart into an explosion of razor sharp stone fragments. Any
    creature within 10 feet of a shattering petrified creature takes 10d6 points of
    piercing and slashing damage from these flying fragments of once-living flesh
    (Reflex DC 43 half). Xoveron is never damaged by these flying shards of stone.
    The save DC is Strength-based.
  Shockwave (Su): When Xoveron makes a charge attack while flying and lands at the
    end of the charge, the force of his landing creates a powerful shockwave. All
    creatures standing on the ground within 30 feet of Xoveron when he lands at the
    end of a charge attack must make a successful DC 40 Reflex save to avoid being
    knocked prone by the force of the impact. The save DC is Constitution-based.
desc_long: |-
  Xoveron, the Horned Prince, is the demon lord of gargoyles, gluttony, and ruins. It is said that he can look out through the eyes of all stone gargoyles perched on roofs throughout the world, watching and waiting for cities to fall, that he might visit and feed on those left behind. Xoveron himself towers at a height of 25 feet, with a wingspan of just over 50 feet. When the Horned Prince moves, the sound of stone grinding on stone can be heard, as if the demon lord himself were composed not of flesh but of some unholy stone come to demonic life.

  Xoveron is often accompanied by numerous vrolikai and ulkreth demons (see page 82). Gargoyles of tremendous size often serve at the Horned Prince's whim, as do monsters with a reputation for hunger and gluttony, such as purple worms or man-eating animals. His realm on the Abyss is an immense, ruined city called Ghahazi, said to have been constructed over the eons by the Horned Prince, who plucked decaying districts and crumbling structures from dead cities across countless worlds.

---

# Demon Lord, Xoveron
This hulking, four-armed, four-headed, sting-tailed _[[monsters/Gargoyle|gargoyle]]_ stands as tall as a house.
**Source** Pathfinder #73: The Worldwound Incursion pg. 84
**XP** 3,276,800
CE Huge outsider
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_, _[[spells/True Seeing|true seeing]]_; Perception +55
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (120 ft., DC 35), _[[spells/Unholy Aura|unholy aura]]_ (DC 27)

##### Defense

**AC** 45, touch 30, _[[conditions/Flat-Footed|flat-footed]]_ 39 (+4 deflection, +6 Dex, +15 natural, +12 profane, –2 size)
**hp** 643 (33d10+462); _[[universal monster rules/Regeneration|regeneration]]_ 30 (mythic or deific)
**Fort** +36, **Ref** +23, **Will** +33
**Defensive Abilities** Abyssal _[[spells/Resurrection|resurrection]]_, _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 20/cold iron, good, and epic; **Immune** _[[universal monster rules/Ability Damage and Drain|ability damage and drain]]_, acid, charm and compulsion effects, death effects, electricity, level drain, petrification, poison; **Resist** cold 30, fire 30; **SR** 38

##### Offense
**Speed** 50 ft., fly 80 ft. (good)
**Melee** 4 claws +48 (1d8+17/19–20), 4 bites +48 (2d6+17/19–20), sting +48 (1d8+17/19–20 plus poison)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** devastating blow, feed, poison, _[[universal monster rules/Rend|rend]]_ (2 claws, 2d8+25), roar, _[[spells/Shatter|shatter]]_ petrification, shockwave
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 27th; concentration +36)
Constant—_detect good_, _detect law_, _freedom of movement_, _true seeing_, _unholy aura_ (DC 27)
At will—_[[spells/Astral Projection|astral projection]]_, _[[spells/Blasphemy|blasphemy]]_ (DC 26), _[[spells/Desecrate|desecrate]]_, _[[spells/Flesh to Stone|flesh to stone]]_ (DC 25), greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport, _[[spells/Shapechange|shapechange]]_, _[[spells/Stone Shape|stone shape]]_, _[[spells/Telekinesis|telekinesis]]_ (DC 24), _[[spells/Unhallow|unhallow]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 23)
3/day—_[[spells/Earthquake|earthquake]]_, quickened _flesh to stone_ (DC 25), _[[spells/Reverse Gravity|reverse gravity]]_, _[[spells/Symbol Of Weakness|symbol of weakness]]_ (DC 26)
1/day—_[[spells/Implosion|implosion]]_ (DC 28), _[[spells/Imprisonment|imprisonment]]_ (DC 28), _[[spells/Time Stop|time stop]]_

##### Statistics
**Str** 44, **Dex** 23, **Con** 38, **Int** 24, **Wis** 32, **Cha** 28
**Base Atk** +33; **CMB** +52 (+56 bull rush, +56 sunder); **CMD** 86 (88 vs. bull rush, 88 vs. sunder)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Craft Construct|Craft Construct]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Bull Rush|Greater Bull Rush]]_, _[[feats/Greater Sunder|Greater Sunder]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw, bite, sting), _[[feats/Improved Lightning Reflexes|Improved Lightning Reflexes]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_flesh to stone_)
**Skills** Acrobatics +39 (+47 when jumping), Disable Device +42, Fly +42, Intimidate +45, Knowledge (arcana) +40, Knowledge (religion) +40, Knowledge (engineering) +43, Knowledge (planes) +43, Perception +55, Sense Motive +47, Spellcraft +43, Stealth +34, Use Magic Device +42; **Racial Modifiers** +8 Perception
**Languages** Abyssal, Celestial, Common, Draconic, Terran; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.

##### Ecology

**Environment** any (Ghahazi, Abyss)
**Organization** solitary (unique)
**Treasure** triple

### Special Abilities

**Devastating Blow (Su)** As a standard action, Xoveron can bring all four of his claws to bear upon a single target. It this attack hits, he deals 8d8+68 points of bludgeoning damage. If the target is a creature, it must make a successful DC 43 Fortitude save or be knocked _[[conditions/Prone|prone]]_ and _[[conditions/Staggered|staggered]]_ for 1d4 rounds. If the target is an object, the attack ignores all hardness possessed by the object. The save DC is Strength-based.

**Feed (Su)** Xoveron can consume the corpse of a Large or smaller creature that has been dead no longer than a day as a full-round action. Doing so destroys the creature’s body and leaves its gear scattered on the ground. All armor and gear worn in the body slot must make a successful DC 43 Fortitude save to avoid becoming _[[conditions/Broken|broken]]_ by this swift and violent _[[feats/Consumption|consumption]]_. When Xoveron feeds on a creature, he immediately learns all of that creature’s memories and knowledge. In addition, he gains the effects of a _[[spells/Heal|heal]]_ spell and a _[[spells/Haste|haste]]_ spell (both at CL 27th). The save DC is Strength-based.

**Poison (Ex)** Sting—injury; save Fort DC 40; frequency 1/round for 6 rounds; effect 1d6 Dexterity drain; cure 3 consecutive saves. If a creature’s Dexterity is drained to 0, the creature is immediately _[[conditions/Petrified|petrified]]_. The save DC is Constitution-based.

**Roar (Su)** Xoveron can unleash a devastating roar as a standard action once per hour. When he roars, all creatures and unattended objects within 60 feet take 30d10 points of sonic damage and become _[[conditions/Stunned|stunned]]_ for 1d6 rounds. Xoveron does not take this damage, and he can exclude any number of creatures or objects from this effect as he wills. A successful DC 40 Reflex save halves the damage and negates the stun effect. The save DC is Constitution-based.
**_Shatter_ Petrification (Su)** Xoveron can strike a _petrified_ creature with any one of his natural weapon attacks to cause it to _shatter_. The _petrified_ creature can resist this with a successful DC 43 Fortitude save. If the creature fails to resist, the blow smashes it apart into an explosion of razor sharp stone fragments. Any creature within 10 feet of a _[[items/Weapon Magic Abilities/Shattering|shattering]]_ _petrified_ creature takes 10d6 points of piercing and slashing damage from these flying fragments of once-living flesh (Reflex DC 43 half). Xoveron is never damaged by these flying shards of stone. The save DC is Strength-based.
**Shockwave (Su)** When Xoveron makes a charge attack while flying and lands at the end of the charge, the force of his landing creates a powerful shockwave. All creatures standing on the ground within 30 feet of Xoveron when he lands at the end of a charge attack must make a successful DC 40 Reflex save to avoid being knocked _prone_ by the force of the _[[items/Weapon Magic Abilities/Impact|impact]]_. The save DC is Constitution-based.

##### Description

Xoveron, the Horned Prince, is the demon lord of gargoyles, gluttony, and ruins. It is said that he can look out through the eyes of all stone gargoyles perched on roofs throughout the world, watching and waiting for cities to fall, that he might visit and feed on those left behind. Xoveron himself towers at a height of 25 feet, with a wingspan of just over 50 feet. When the Horned Prince moves, the sound of stone _[[items/Armor Magic Abilities/Grinding|grinding]]_ on stone can be heard, as if the demon lord himself were composed not of flesh but of some _[[items/Weapon Magic Abilities/Unholy|unholy]]_ stone come to demonic life.

Xoveron is often accompanied by numerous vrolikai and ulkreth demons (see page 82). Gargoyles of tremendous size often serve at the Horned Prince’s whim, as do monsters with a reputation for hunger and gluttony, such as purple worms or man-eating animals. His realm on the Abyss is an immense, ruined city _[[items/Weapon Magic Abilities/Called|called]]_ Ghahazi, said to have been constructed over the eons by the Horned Prince, who plucked decaying districts and crumbling structures from dead cities across countless worlds.
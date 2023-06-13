---
cssclass: [monsters]
title1: Devil, Drowning Devil (Sarglagon)
desc_short: This serpentine creature has finlike wings, ram horns, four eyes, and
  arms that end in masses of tentacles.
title2: Drowning Devil (Sarglagon)
CR: 8
sources:
- name: Bestiary 4
  page: 52
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
- name: "Pathfinder #60: From Hell's Heart"
  page: 80
  link: http://paizo.com/pathfinder/adventurePath/skullAndShackles/v5748btpy8moi
XP: 4800
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
  see invisibility: true
auras:
- name: heavy aura
  radius: 10
  DC: 18
AC:
  AC: 21
  touch: 17
  flat_footed: 13
  components:
    dex: 7
    dodge: 1
    natural: 4
    size: -1
HP:
  HP: 103
  long: 9d10+54
saves:
  fort: 12
  ref: 10
  will: 11
DR:
- amount: 5
  weakness: good
immunities:
- fire
- poison
resistances:
  acid: 10
  cold: 10
SR: 19
speeds:
  base: 30
  fly: 30
  fly_maneuverability: average
  swim: 40
attacks:
  melee:
  - - text: bite +15 (2d6+5)
      entries:
      - - damage: 2d6+5
      attack: bite
      bonus:
      - 15
    - text: 2 slams +15 (1d8+5 plus poison)
      entries:
      - - damage: 1d8+5
        - effect: poison
      count: 2
      attack: slams
      bonus:
      - 15
  special:
  - drown
  - poison
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: see invisibility
    source: default
    freq: Constant
  - name: water breathing
    source: default
    freq: Constant
  - name: control water
    source: default
    freq: At will
  - name: curse water
    source: default
    freq: At will
  - name: discern lies
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - superscripts:
    - APG
    name: hydraulic push
    source: default
    freq: At will
  - superscripts:
    - APG
    name: hydraulic torrent
    source: default
    freq: 3/day
  - name: poison
    source: default
    freq: 3/day
    DC: 18
  - name: protection from good
    source: default
    freq: 3/day
  - name: freedom of movement
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: drowning devil
      amount: 1
      chance: 35%
  sources:
  - name: default
    CL: 12
    concentration: 16
ability_scores:
  STR: 20
  DEX: 25
  CON: 23
  INT: 16
  WIS: 20
  CHA: 19
BAB: 9
CMB: 17
CMD: 33
CMD_other: can't be tripped
feats:
- name: Agile Maneuvers
- name: Combat Reflexes
- name: Dodge
- name: Weapon Finesse
- name: Wind Stance
skills:
  Bluff: 16
  Diplomacy: 16
  Fly: 5
  Intimidate: 16
  Knowledge (nature): 15
  Knowledge (planes): 15
  Perception: 17
  Sense Motive: 17
  Stealth: 15
  Swim: 25
languages:
- Celestial
- Common
- Draconic
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Hell)
  organization: solitary, pair, or guard (3-10)
  treasure_type: standard
special_abilities:
  Drown (Su): As a full-round action, a drowning devil can summon murky water into
    the lungs of a single target within 30 feet. If the target can't breathe water,
    it's unable hold its breath and immediately begins to drown. At the start of its
    next turn, the target must succeed at a DC 18 Fortitude save to cough up this
    water or it falls unconscious and is brought to 0 hit points. On the next round,
    the target must save successfully again or drop to -1 hit point and start dying;
    on the third round it must save successfully again or die. The save DC is Charisma-based.
  Heavy Aura (Su): Whenever a creature enters the drowning devil's heavy aura, it
    must succeed at a DC 18 Will save or reduce its speed as if carrying a load one
    step higher or wearing armor one category heavier (whichever is worse), and its
    armor check penalty increases by 2. A creature already carrying a heavy load or
    wearing heavy armor that fails its save can't move as long as it remains in the
    affected area. A creature that saves against a drowning devil's heavy aura is
    immune to that devil's aura for 24 hours. The save DC is Charisma-based.
  Poison (Ex): Slam-injury; save Fort DC 20; frequency 1/round for 6 rounds; effect
    1d4 Str; cure 2 consecutive saves.
desc_long: Called sarglagons in their Infernal tongue, drowning devils take great
  pride in being the best-adapted guardians of Hell's waterways, and are among the
  few fiends who travel the seas and rivers of the multiverse as part of larger infernal
  plots. Even in the air or on the ground, a drowning devil moves with a haunting
  litheness as though it were swimming. A typical drowning devil weighs 600 pounds,
  and can exceed 15 feet from head to tail.

---

# Devil, Drowning Devil (Sarglagon)
This serpentine creature has finlike wings, ram horns, four eyes, and arms that end in masses of tentacles.
**Source** Bestiary 4 pg. 52, Pathfinder #60: From Hell's Heart pg. 80
**XP** 4,800

LE Large outsider (devil, evil, extraplanar, lawful)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +17
**Aura** heavy aura (10 ft., DC 18)

##### Defense

**AC** 21, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+7 Dex, +1 dodge, +4 natural, –1 size)
**hp** 103 (9d10+54)
**Fort** +12, **Ref** +10, **Will** +11
**DR** 5/good; **Immune** fire, poison; **Resist** acid 10, cold 10; **SR** 19

##### Offense
**Speed** 30 ft., fly 30 ft. (average), swim 40 ft.
**Melee** bite +15 (2d6+5), 2 slams +15 (1d8+5 plus poison)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** drown, poison
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +16)
Constant—_see invisibility_, _[[universal monster rules/Water Breathing|water breathing]]_
At will—_[[spells/Control Water|control water]]_, _[[spells/Curse Water|curse water]]_, _[[spells/Discern Lies|discern lies]]_, greater teleport (self plus 50 lbs. of objects only), _[[spells/Hydraulic Push|hydraulic push]]_
3/day—_[[spells/Hydraulic Torrent|hydraulic torrent]]_, poison (DC 18), _[[spells/Protection From Good|protection from good]]_
1/day—_[[spells/Freedom of Movement|freedom of movement]]_, _[[universal monster rules/Summon|summon]]_ (level 4, 1 drowning devil 35%)

##### Statistics
**Str** 20, **Dex** 25, **Con** 23, **Int** 16, **Wis** 20, **Cha** 19
**Base Atk** +9; **CMB** +17; **CMD** 33 (can’t be tripped)
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Wind Stance|Wind Stance]]_
**Skills** Bluff +16, Diplomacy +16, Fly +5, Intimidate +16, Knowledge (nature) +15, Knowledge (planes) +15, Perception +17, Sense Motive +17, Stealth +15, Swim +25
**Languages** Celestial, Common, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Hell)
**Organization** solitary, pair, or _[[npcs/Guard|guard]]_ (3–10)
**Treasure** standard

### Special Abilities

**Drown (Su)** As a full-round action, a drowning devil can _summon_ murky water into the lungs of a single target within 30 feet. If the target can’t breathe water, it’s unable hold its breath and immediately begins to drown. At the start of its next turn, the target must succeed at a DC 18 Fortitude save to cough up this water or it falls _[[conditions/Unconscious|unconscious]]_ and is brought to 0 hit points. On the next round, the target must save successfully again or drop to –1 hit point and start _[[conditions/Dying|dying]]_; on the third round it must save successfully again or die. The save DC is Charisma-based.

**Heavy Aura (Su)** Whenever a creature enters the drowning devil’s heavy aura, it must succeed at a DC 18 Will save or reduce its speed as if carrying a load one step higher or wearing armor one category heavier (whichever is worse), and its armor check penalty increases by 2. A creature already carrying a heavy load or wearing heavy armor that fails its save can’t move as long as it remains in the affected area. A creature that saves against a drowning devil’s heavy aura is immune to that devil’s aura for 24 hours. The save DC is Charisma-based.

**Poison (Ex)** Slam—injury; save Fort DC 20; frequency 1/round for 6 rounds; effect 1d4 Str; cure 2 consecutive saves.

##### Description

_[[items/Weapon Magic Abilities/Called|Called]]_ sarglagons in their Infernal tongue, drowning devils take great pride in being the best-adapted guardians of Hell’s waterways, and are among the few fiends who travel the seas and rivers of the multiverse as part of larger infernal plots. Even in the air or on the ground, a drowning devil moves with a haunting litheness as though it were swimming. A typical drowning devil weighs 600 pounds, and can exceed 15 feet from head to tail.
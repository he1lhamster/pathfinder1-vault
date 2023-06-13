---
cssclass: [monsters]
title1: Hallowed Lynx
desc_short: Within a halo of brilliant, glowing orbs are the distinctive features
  of a compact feline with tufted ears, a short tail, and keen, piercing eyes.
title2: Hallowed Lynx
CR: 17
sources:
- name: 'Pathfinder #138: Rise of New Thassilon'
  page: 88
  link: https://paizo.com/products/btq01w1w
XP: 102400
alignment: NE
size: Small
type: magical beast
initiative:
  bonus: 5
senses:
  arcane sight: true
  darkvision: 60
  low-light vision: true
  scent: true
auras:
- name: hallowed lights
  radius: 60
  DC: 26
AC:
  AC: 29
  touch: 17
  flat_footed: 23
  components:
    dex: 5
    dodge: 1
    natural: 12
    size: 1
HP:
  HP: 241
  long: 23d10+115
saves:
  fort: 17
  ref: 20
  will: 14
immunities:
- blindness
- fire
- light effects
speeds:
  base: 40
  climb: 20
attacks:
  melee:
  - - text: bite +29 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: bite
      bonus:
      - 29
    - text: 2 claws +29 (1d6+1)
      entries:
      - - damage: 1d6+1
      count: 2
      attack: claws
      bonus:
      - 29
  ranged:
  - - text: blinding orb +24 touch (10d8 plus blindness)
      entries:
      - - damage: 10d8
        - effect: blindness
      attack: blinding orb
      bonus:
      - 24
      touch: true
  special:
  - blinding orb (DC 26)
  - pounce
  - rake (2 claws +29, 1d6+1)
  - release shining child
  - sneak attack +6d6
spell_like_abilities:
  entries:
  - name: arcane sight
    source: default
    freq: Constant
  - name: daylight
    source: default
    freq: At will
  - name: major image
    source: default
    freq: At will
    DC: 18
  - name: mirror image
    source: default
    freq: At will
  - name: rainbow pattern
    source: default
    freq: At will
    DC: 19
  - name: quickened dispel magic
    source: default
    freq: 3/day
  - name: prismatic spray
    source: default
    freq: 3/day
    DC: 22
  - name: scintillating pattern
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 23
    concentration: 28
ability_scores:
  STR: 12
  DEX: 21
  CON: 19
  INT: 4
  WIS: 10
  CHA: 21
BAB: 23
CMB: 23
CMD: 39
CMD_other: 43 vs. trip
feats:
- name: Dodge
- name: Following Step
- name: Iron Will
- name: Lightning Reflexes
- name: Mobility
- name: Quicken Spell-Like Ability (dispel magic)
- name: Skill Focus (Acrobatics)
- name: Spring Attack
- name: Step Up
- name: Step Up And StrikeAPG
- name: Toughness
- name: Weapon Finesse
skills:
  Acrobatics: 37
    when jumping: 41
  Climb: 9
  Perception: 0
languages:
- Azlanti
- Thassilonian (can't speak)
ecology:
  environment: any
  organization: solitary or pair
  treasure_type: standard
special_abilities:
  Blinding Orb (Su): A hallowed lynx has a halo of seven orbs of brilliant light.
    It can hurl an orb as a ranged touch attack with a range of 120 feet. A creature
    hit by the hallowed lynx's blinding orb takes 10d8 points of fire damage and must
    succeed at a DC 26 Fortitude save or be permanently blinded. Once hurled, an orb
    loses its innate brilliance and cannot be used again until 24 hours have passed,
    after which time its energy refreshes and it resumes glowing. The save DC is Charisma-based.
  Hallowed Lights (Su): The glowing orbs surrounding a hallowed lynx radiate light
    out to a distance of 60 feet. This light counters and is countered by darkness
    as though it were an 8th-level spell. Allies in this light, including the hallowed
    lynx, gain an insight bonus on Charisma-based skill checks and Will saving throws
    equal to the lynx's Charisma modifier. Enemies in the light at the start of the
    lynx's turn must succeed at a DC 26 Will save or become blinded for 1 round. If
    the hallowed lynx has expended all seven of its orbs through its blinding orb
    or release shining child ability, the hallowed lights cease until at least one
    of the hallowed lynx's orbs has refreshed. The save DC is Charisma-based.
  Release Shining Child (Su): As a standard action, a hallowed lynx can release the
    shining child encapsulated within any one of its glowing orbs. This functions
    as if the shining child had been summoned using a summon monster IX spell (CL
    23rd). Once an orb has been used in this manner, it loses its innate brilliance
    and cannot be used again until 24 hours have passed, after which time its energy
    refreshes and it resumes glowing.
desc_long: 'A mid-sized feline adorned with a halo of blinding orbs of light, the
  hallowed lynx is a creature widely thought to be mere myth or long extinct. Only
  a handful of hallowed lynxes exist, most held in stasis within long-buried Thassilonian
  ruins, though rumored sightings of the blindingly bright cats suggest that small
  populations may have survived to the present day. Created from keen hunters and
  imbued with potent light-based magic distilled from powerful outsiders, hallowed
  lynxes are deadly predators whose mere presence bolsters their allies. Aside from
  the brilliant orbs that surround them, a hallowed lynx resembles its mundane kin,
  having a short tail, large paws, spotted tawny fur, and distinctive tufts of fur
  extending from its ears. It is the same size as an ordinary lynx: just over 2 feet
  tall, around 3 feet long, and weighing about 35 pounds.'

---

# Hallowed Lynx
Within a halo of brilliant, glowing orbs are the distinctive features of a compact feline with tufted ears, a short tail, and _[[items/Weapon Magic Abilities/Keen|keen]]_, piercing eyes.
**Source** Pathfinder #138: Rise of New Thassilon pg. 88
**XP** 102,400

NE Small magical beast
**Init** +5; **Senses** _[[spells/Arcane Sight|arcane sight]]_, _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +0
**Aura** hallowed lights (60 ft., DC 26)

##### Defense

**AC** 29, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+5 Dex, +1 dodge, +12 natural, +1 size)
**hp** 241 (23d10+115)
**Fort** +17, **Ref** +20, **Will** +14
**Immune** blindness, fire, light effects

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** bite +29 (1d6+1), 2 claws +29 (1d6+1)
**Ranged** _[[items/Armor Magic Abilities/Blinding|blinding]]_ orb +24 touch (10d8 plus blindness)
**Special Attacks** _blinding_ orb (DC 26), _[[universal monster rules/Pounce|pounce]]_, _[[universal monster rules/Rake|rake]]_ (2 claws +29, 1d6+1), release _[[monsters/Shining Child|shining child]]_, sneak attack +6d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 23rd; concentration +28)
Constant—_arcane sight_ 
At will—_[[spells/Daylight|daylight]]_, _[[spells/Major Image|major image]]_ (DC 18), _[[spells/Mirror Image|mirror image]]_, _[[spells/Rainbow Pattern|rainbow pattern]]_ (DC 19) 
3/day—quickened _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Prismatic Spray|prismatic spray]]_ (DC 22), _[[spells/Scintillating Pattern|scintillating pattern]]_

##### Statistics
**Str** 12, **Dex** 21, **Con** 19, **Int** 4, **Wis** 10, **Cha** 21
**Base Atk** +23; **CMB** +23; **CMD** 39 (43 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _Dodge_, _[[feats/Following Step|Following Step]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_dispel magic_), _[[feats/Skill Focus|Skill Focus]]_ (Acrobatics), _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Step Up|Step Up]]_, _Step Up_ And StrikeAPG, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +37 (+41 when jumping), _Climb_ +9
**Languages** Azlanti, Thassilonian (can’t speak)

##### Ecology

**Environment** any
**Organization** solitary or pair
**Treasure** standard

### Special Abilities

**_Blinding_ Orb (Su)** A _[[monsters/Hallowed Lynx|hallowed lynx]]_ has a halo of seven orbs of brilliant light. It can hurl an orb as a ranged touch attack with a range of 120 feet. A creature hit by the _hallowed lynx_’s _blinding_ orb takes 10d8 points of fire damage and must succeed at a DC 26 Fortitude save or be permanently _[[conditions/Blinded|blinded]]_. Once hurled, an orb loses its innate brilliance and cannot be used again until 24 hours have passed, after which time its energy refreshes and it resumes glowing. The save DC is Charisma-based.

**Hallowed Lights (Su)** The glowing orbs surrounding a _hallowed lynx_ radiate light out to a distance of 60 feet. This light counters and is countered by _[[spells/Darkness|darkness]]_ as though it were an 8th-level spell. Allies in this light, including the _hallowed lynx_, gain an insight bonus on Charisma-based skill checks and Will saving throws equal to the lynx’s Charisma modifier. Enemies in the light at the start of the lynx’s turn must succeed at a DC 26 Will save or become _blinded_ for 1 round. If the _hallowed lynx_ has expended all seven of its orbs through its _blinding_ orb or release _shining child_ ability, the hallowed lights cease until at least one of the _hallowed lynx_’s orbs has refreshed. The save DC is Charisma-based.

**Release _Shining Child_ (Su)** As a standard action, a _hallowed lynx_ can release the _shining child_ encapsulated within any one of its glowing orbs. This functions as if the _shining child_ had been summoned using a _[[spells/Summon Monster IX|summon monster IX]]_ spell (CL 23rd). Once an orb has been used in this manner, it loses its innate brilliance and cannot be used again until 24 hours have passed, after which time its energy refreshes and it resumes glowing.

##### Description

A mid-sized feline adorned with a halo of _blinding_ orbs of light, the _hallowed lynx_ is a creature widely thought to be mere myth or long extinct. Only a handful of hallowed lynxes exist, most held in stasis within long-buried Thassilonian ruins, though rumored sightings of the blindingly bright cats suggest that small populations may have survived to the present day. Created from _keen_ hunters and imbued with _[[items/Weapon Magic Abilities/Potent|potent]]_ light-based magic distilled from powerful outsiders, hallowed lynxes are _[[items/Weapon Magic Abilities/Deadly|deadly]]_ predators whose mere presence bolsters their allies. Aside from the brilliant orbs that surround them, a _hallowed lynx_ resembles its mundane kin, having a short tail, large paws, spotted tawny fur, and distinctive tufts of fur extending from its ears. It is the same size as an ordinary lynx: just over 2 feet tall, around 3 feet long, and weighing about 35 pounds.
---
cssclass: [monsters]
title1: Emperor of Scales
desc_short: The air fills with the sound of hissing snakes as a giant, severed snake's
  head floats into view, with a gaping mouth and twin fangs dripping virulent poison.
  Its eyes are milky and blind, but its forked tongue constantly tests the air for
  fresh scents. Below the head, where a body should be, numerous hissing serpents
  thrash like tendrils of torn flesh. Blood drips from the severed head, sizzling
  as it burns like acid through anything it touches.
title2: Emperor of Scales
CR: 15
sources:
- name: 'Pathfinder #42: Sanctum of the Serpent God'
  page: 82
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderAdventurePath/serpentsSkull/v5748btpy8ihw
XP: 51200
alignment: CE
size: Huge
type: outsider
subtypes:
- chaotic
- evil
- native
initiative:
  bonus: 11
senses:
  all-around vision: true
  darkvision: 60
  scent: true
auras:
- name: frightful presence
  radius: 60
  DC: 25
- name: maddening hiss
  radius: 100
  DC: 25
AC:
  AC: 30
  touch: 15
  flat_footed: 23
  components:
    dex: 7
    natural: 15
    size: -2
HP:
  HP: 225
  long: 18d10+126
  regeneration: 5
  regeneration_weakness: electricity
saves:
  fort: 19
  ref: 13
  will: 15
DR:
- amount: 15
  weakness: good and silver
immunities:
- acid
- fire
- mind-affecting effects
- paralysis
- poison
- vorpal weapons
SR: 26
speeds:
  base: 30
  climb: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +24 (2d8+8/19-20 plus poison and grab)
      entries:
      - - damage: 2d8+8
          crit_range: 19-20
        - effect: poison
        - effect: grab
      attack: bite
      bonus:
      - 24
    - text: 8 snakebites +22 (1d6+4 plus poison)
      entries:
      - - damage: 1d6+4
        - effect: poison
      count: 8
      attack: snakebites
      bonus:
      - 22
  special:
  - acidic gore
  - poison
  - swallow whole (2d8+12 plus poison, AC 17, 22 hp)
space: 15
reach: 10
reach_other: 15 ft. with snakebites
spell_like_abilities:
  entries:
  - name: fly
    source: default
    freq: Constant
  - name: poison
    source: default
    freq: At will
    DC: 20
  - name: teleport
    source: default
    freq: At will
  - name: accelerate poison
    source: default
    freq: 3/day
    DC: 18
  - name: blindness/deafness
    source: default
    freq: 3/day
    DC: 18
  - name: blur
    source: default
    freq: 3/day
  - name: dominate person
    source: default
    freq: 3/day
    DC: 21
  - name: major image
    source: default
    freq: 3/day
    DC: 19
  - name: mirror image
    source: default
    freq: 3/day
  - name: suggestion
    source: default
    freq: 3/day
    DC: 19
  - name: chaos hammer
    source: default
    freq: 1/day
    DC: 20
  - name: dream
    source: default
    freq: 1/day
  - name: mass suggestion
    source: default
    freq: 1/day
    DC: 22
  - name: nightmare
    source: default
    freq: 1/day
    DC: 21
  - name: unholy blight
    source: default
    freq: 1/day
    DC: 20
  sources:
  - name: default
    CL: 15
    concentration: 21
ability_scores:
  STR: 26
  DEX: 24
  CON: 23
  INT: 13
  WIS: 19
  CHA: 22
BAB: 18
CMB: 28
CMB_other: +32 grapple
CMD: 45
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Great Fortitude
- name: Hover
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Multiattack
- name: Power Attack
- name: Snatch
- name: Toughness
skills:
  Bluff: 27
  Climb: 16
  Escape Artist: 22
  Fly: 20
  Knowledge (history): 12
  Knowledge (planes): 12
  Knowledge (religion): 12
  Perception: 26
  Sense Motive: 22
  Spellcraft: 19
  Stealth: 16
  Use Magic Device: 21
  _racial_mods:
    Escape Artist:
      _: 4
    Perception:
      _: 4
    Stealth:
      _: 4
    Use Magic Device:
      _: 4
languages:
- Abyssal
- Aklo
- Azlanti (does not speak)
- telepathy 100 ft.
special_qualities:
- command snakes
ecology:
  environment: any
  organization: solitary
  treasure_type: standard
special_abilities:
  Acidic Gore (Su): The Emperor of Scales' giant severed head continually drips blood
    and gore that burn like acid. Any creature within 10 feet of the Emperor of Scales
    must make a DC 25 Reflex save or be sprayed by droplets of acidic blood, taking
    2d6 points of acid damage. The save DC is Constitution-based.
  Command Snakes (Ex): As a free action, the Emperor of Scales can command any snake
    or serpent with the animal or magical beast type, as the dominate animal spell.
    The target can resist the command with a DC 25 Will save.
  Immunity to Vorpal Weapons (Ex): The Emperor of Scales is essentially a giant head
    with no body. As a result, its head cannot be severed, and vorpal weapons have
    no additional effect on it.
  Maddening Hiss (Su): The Emperor of Scales' numerous snake heads constantly hiss
    in a maddening cacophony as a free action. Any creature within 100 feet of the
    Emperor of Scales must make a DC 25 Will save or be confused for 1 round. This
    is a mind-affecting compulsion insanity effect. A creature that saves cannot be
    affected by the Emperor of Scales' maddening hiss for 24 hours. The save DC is
    Charisma-based.
  Poison (Ex): Bite or swallow-injury; save Fort DC 25; frequency 1/round for 10 rounds;
    effect 2d6 acid and 1d4 Str; cure 2 consecutive saves; snakebite-injury; save
    Fort DC 20; frequency 1/round for 6 rounds; effect 1d2 Con; cure 2 consecutive
    saves.
desc_long: |-
  In the earliest days of the Age of Serpents, when the great serpentfolk empire was young, the serpentfolk were ruled by a single, powerful priest-king. When Ydersius took his rightful place as god of the serpentfolk, he exalted this priest-king above all others, raising the king up to become his foremost servant and herald. With his original name long lost to memory, the first king of the serpentfolk empire became known as the Emperor of Scales.

  With Ydersius's still-living head entombed beneath the earth and his mindless body endlessly wandering the Darklands, the Emperor of Scales is the snake-god's primary representative on Golarion. Unable to take direct action on his own, Ydersius relies upon his herald to enact his will on the Material Plane. The Emperor of Scales embodies the fall of the mighty serpentfolk empire from its previous heights, and personifies the rage of Ydersius himself, trapped and sundered into two lesser parts. But he also represents the god's immortality, for even in defeat Ydersius was not slain, and even without a body, the Emperor of Scales still serves.

  The Emperor of Scales does not speak, but it can communicate telepathically. Snakes and serpents of all kinds and sizes f lock to the Emperor of Scales, who can enslave them to his will. The Emperor of Scales appears as a giant snake's head about 20 feet long, and weighs close to 5 tons. His serpentine tendrils extend another 15 feet behind and around his head.

---

# Emperor of Scales
The air fills with the sound of hissing snakes as a giant, severed snake’s head floats into view, with a gaping mouth and twin fangs dripping _[[feats/Virulent Poison|virulent poison]]_. Its eyes are milky and blind, but its forked tongue constantly tests the air for fresh scents. Below the head, where a body should be, numerous hissing serpents thrash like tendrils of torn flesh. Blood drips from the severed head, sizzling as it burns like acid through anything it touches.
**Source** Pathfinder #42: Sanctum of the Serpent God pg. 82
**XP** 51,200
CE Huge outsider (chaotic, evil, native)
**Init** +11; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +26
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (60 ft., DC 25), maddening hiss (100 ft., DC 25)

##### Defense

**AC** 30, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+7 Dex, +15 natural, -2 size)
**hp** 225 (18d10+126); _[[universal monster rules/Regeneration|regeneration]]_ 5 (electricity)
**Fort** +19, **Ref** +13, **Will** +15
**DR** 15/good and silver; **Immune** acid, fire, mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, poison, _[[items/Weapon Magic Abilities/Vorpal|vorpal]]_ weapons; **SR** 26

##### Offense
**Speed** 30 ft., _[[universal monster rules/Climb|climb]]_ 30 ft., fly 60 ft. (good)
**Melee** bite +24 (2d8+8/19-20 plus poison and _[[universal monster rules/Grab|grab]]_), 8 snakebites +22 (1d6+4 plus poison)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with snakebites)
**Special Attacks** acidic gore, poison, _[[universal monster rules/Swallow Whole|swallow whole]]_ (2d8+12 plus poison, AC 17, 22 hp)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +21)
Constant — fly
At will — poison (DC 20), teleport
3/day — _[[spells/Accelerate Poison|accelerate poison]]_* (DC 18), blindness/deafness (DC 18), _[[spells/Blur|blur]]_, _[[spells/Dominate Person|dominate person]]_ (DC 21), _[[spells/Major Image|major image]]_ (DC 19), _[[spells/Mirror Image|mirror image]]_, _[[spells/Suggestion|suggestion]]_ (DC 19)
1/day — _[[spells/Chaos Hammer|chaos hammer]]_ (DC 20), _[[spells/Dream|dream]]_, mass _suggestion_ (DC 22), _[[spells/Nightmare|nightmare]]_ (DC 21), _[[spells/Unholy Blight|unholy blight]]_ (DC 20)

##### Statistics
**Str** 26, **Dex** 24, **Con** 23, **Int** 13, **Wis** 19, **Cha** 22
**Base Atk** +18; **CMB** +28 (+32 grapple); **CMD** 45 (can't be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Snatch|Snatch]]_, _[[feats/Toughness|Toughness]]_
**Skills** Bluff +27, _Climb_ +16, Escape Artist +22, Fly +20, Knowledge (history) +12, Knowledge (planes) +12, Knowledge (religion) +12, Perception +26, Sense Motive +22, Spellcraft +19, Stealth +16, Use Magic Device +21; **Racial Modifiers** +4 Escape Artist, +4 Perception, +4 Stealth, +4 Use Magic Device
**Languages** Abyssal, Aklo, Azlanti (does not speak), _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[spells/Command|command]]_ snakes

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** standard

### Special Abilities

**Acidic Gore (Su)** The _[[monsters/Emperor of Scales|Emperor of Scales]]_’ giant severed head continually drips blood and gore that _[[universal monster rules/Burn|burn]]_ like acid. Any creature within 10 feet of the _Emperor of Scales_ must make a DC 25 Reflex save or be sprayed by droplets of acidic blood, taking 2d6 points of acid damage. The save DC is Constitution-based.

**_Command_ Snakes (Ex)** As a free action, the _Emperor of Scales_ can _command_ any snake or serpent with the animal or magical beast type, as the _[[spells/Dominate Animal|dominate animal]]_ spell. The target can resist the _command_ with a DC 25 Will save.

**_[[universal monster rules/Immunity|Immunity]]_ to _Vorpal_ Weapons (Ex)** The _Emperor of Scales_ is essentially a giant head with no body. As a result, its head cannot be severed, and _vorpal_ weapons have no additional effect on it.

**Maddening Hiss (Su)** The _Emperor of Scales_’ numerous snake heads constantly hiss in a maddening cacophony as a free action. Any creature within 100 feet of the _Emperor of Scales_ must make a DC 25 Will save or be _[[conditions/Confused|confused]]_ for 1 round. This is a mind-affecting compulsion _[[spells/Insanity|insanity]]_ effect. A creature that saves cannot be affected by the _Emperor of Scales_’ maddening hiss for 24 hours. The save DC is Charisma-based.

**Poison (Ex)** Bite or swallow—injury; save Fort DC 25; frequency 1/round for 10 rounds; effect 2d6 acid and 1d4 Str; cure 2 consecutive saves; _[[items/Weapon/Snakebite|snakebite]]_—injury; save Fort DC 20; frequency 1/round for 6 rounds; effect 1d2 Con; cure 2 consecutive saves.
* See Pathfinder RPG Advanced Player’s Guide.

##### Description

In the earliest days of the Age of Serpents, when the great _[[monsters/Serpentfolk|serpentfolk]]_ empire was young, the _serpentfolk_ were ruled by a single, powerful priest-king. When Ydersius took his rightful place as god of the _serpentfolk_, he exalted this priest-king above all others, raising the _[[npcs/King|king]]_ up to become his foremost servant and herald. With his original name long lost to memory, the first _king_ of the _serpentfolk_ empire became known as the _Emperor of Scales_.

With Ydersius’s still-living head entombed beneath the earth and his mindless body endlessly wandering the Darklands, the _Emperor of Scales_ is the snake-god’s primary representative on Golarion. Unable to take direct action on his own, Ydersius relies upon his herald to enact his will on the Material Plane. The _Emperor of Scales_ embodies the fall of the mighty _serpentfolk_ empire from its previous heights, and personifies the _[[spells/Rage|rage]]_ of Ydersius himself, trapped and sundered into two lesser parts. But he also represents the god’s immortality, for even in defeat Ydersius was not slain, and even without a body, the _Emperor of Scales_ still serves.

The _Emperor of Scales_ does not speak, but it can communicate telepathically. Snakes and serpents of all kinds and sizes f lock to the _Emperor of Scales_, who can enslave them to his will. The _Emperor of Scales_ appears as a giant snake’s head about 20 feet long, and weighs close to 5 tons. His serpentine tendrils extend another 15 feet behind and around his head.
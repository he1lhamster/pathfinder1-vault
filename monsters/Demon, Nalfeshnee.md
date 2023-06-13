---
cssclass: [monsters]
title1: Demon, Nalfeshnee
desc_short: This porcine demon has huge tusks and tiny wings, and its furred flesh
  oozes with greasy black-and-purple energy.
title2: Mythic Nalfeshnee
CR: 17
MR: 7
sources:
- name: Mythic Adventures
  page: 183
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 102400
alignment: CE
size: Huge
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
- mythic
initiative:
  bonus: 12
senses:
  darkvision: 60
  true seeing: true
auras:
- name: unholy aura
  DC: 25
AC:
  AC: 36
  touch: 13
  flat_footed: 35
  components:
    deflection: 4
    dex: 1
    natural: 23
    size: -2
HP:
  HP: 287
  long: 15d10+205
  fast_healing: 5
saves:
  fort: 22
  ref: 10
  will: 21
DR:
- amount: 10
  weakness: epic and good
immunities:
- fire
- electricity
- poison
resistances:
  acid: 10
  cold: 10
SR: 28
speeds:
  base: 30
  fly: 40
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +28 (3d8+15/18-20)
      entries:
      - - damage: 3d8+15
          crit_range: 18-20
      attack: bite
      bonus:
      - 28
    - text: 2 claws +28 (2d6+15/19-20 plus steal)
      entries:
      - - damage: 2d6+15
          crit_range: 19-20
        - effect: steal
      count: 2
      attack: claws
      bonus:
      - 28
  special:
  - demonic knowledge
  - mythic power (7/day, surge +1d10)
  - touch of chaos
  - unholy nimbus
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: detect thoughts
    source: default
    freq: Constant
    DC: 19
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 25
  - name: call lightning
    source: default
    freq: At will
    DC: 20
  - name: feeblemind
    source: default
    freq: At will
    DC: 22
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: move earth
    source: default
    freq: At will
  - name: slow
    source: default
    freq: At will
    DC: 20
  - name: stone shape
    source: default
    freq: At will
  - name: stone tell
    source: default
    freq: At will
  - name: scrying
    source: default
    freq: 3/day
  - name: contact other plane
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 5
    summons:
    - name: nalfeshnee
      amount: 1
      chance: 20%
    - name: hezrous
      amount: 1d4
      chance: 40%
    - name: vrocks
      amount: 1d4
      chance: 50%
  sources:
  - name: default
    CL: 12
    concentration: 19
ability_scores:
  STR: 40
  DEX: 13
  CON: 29
  INT: 23
  WIS: 22
  CHA: 24
BAB: 15
CMB: 32
CMB_other: +34 bull rush
CMD: 47
CMD_other: 49 vs. bull rush
feats:
- name: Awesome Blow
- name: Cleave
- name: Improved Bull Rush
- is_mythic: true
  name: Improved Critical (bite)
- name: Improved Critical (claws)
- is_mythic: true
  name: Improved Initiative
- is_mythic: true
  name: Iron Will
- is_mythic: true
  name: Power Attack
skills:
  Bluff: 25
  Diplomacy: 25
  Fly: 11
  Intimidate: 22
  Knowledge (arcana): 24
  Knowledge (planes): 24
  Knowledge (any one other): 21
  Perception: 32
  Sense Motive: 24
  Spellcraft: 24
  Stealth: 11
  Use Magic Device: 25
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
ecology:
  environment: any (Abyss)
  organization: solitary or warband (1 nalfeshnee, 1 hezrou, and 2-5 vrocks)
  treasure_type: standard
special_abilities:
  Demonic Knowledge (Su): By expending one use of mythic power as a free action, the
    demon learns one weakness, vulnerability, or special defense of an opponent within
    reach.
  Touch of Chaos (Sp): This functions like the Chaos domain granted power (Core Rulebook
    42), except the demon can expend one use of mythic power as a free action to use
    this ability when it hits with a natural attack.
  Unholy Nimbus (Su): Three times per day as a free action, the demon can create writhing
    colored lights on its body. One round later, the light bursts in a 60-foot radius.
    Any non-demon caught within this area must succeed at a DC 24 Will save or be
    dazed for 1d10 rounds as visions of madness hound it. The save DC is Charisma-based.
desc_long: A mythic nalfeshnee gains its power by tricking or forcing other mythic
  beings to imbue it. It hoards its many valuable secrets as a dragon hoards gold.

---

# Demon, Nalfeshnee
A towering, corpulent beast, this fiend has the hideous head of a _[[monsters/Boar|boar]]_ and arms ending in fatty, four-fingered hands.
**Source** Pathfinder RPG Bestiary pg. 65
**XP** 38,400
CE Huge outsider (chaotic, demon, evil, extraplanar)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +31
**Aura** _[[spells/Unholy Aura|unholy aura]]_ (DC 23)

##### Defense

**AC** 29, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+4 deflection, +1 Dex, +16 natural, –2 size)
**hp** 203 (14d10+126)
**Fort** +22, **Ref** +9, **Will** +21
**DR** 10/good; **Immune** electricity, poison; **Resist** acid 10, cold 10, fire 10; **SR** 25

##### Offense
**Speed** 30 ft., fly 40 ft. (poor)
**Melee** bite +23 (3d8+11/19–20), 2 claws +23 (2d6+11)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _[[items/Weapon Magic Abilities/Unholy|unholy]]_ nimbus
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th)
Constant—_true seeing_, _unholy aura_ (DC 23)
At will—_[[spells/Call Lightning|call lightning]]_ (DC 18), _[[spells/Feeblemind|feeblemind]]_ (DC 20), greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Slow|slow]]_ (DC 18), greater teleport (self plus 50 lbs. of objects only)
1/day—_[[universal monster rules/Summon|summon]]_ (level 5, 1 nalfeshnee 20%, 1d4 hezrous 40%, or 1d4 vrocks 50%)

##### Statistics
**Str** 32, **Dex** 13, **Con** 29, **Int** 23, **Wis** 22, **Cha** 20
**Base Atk** +14; **CMB** +27; **CMD** 42
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Bluff +22, Diplomacy +22, Fly +10, Intimidate +19, Knowledge (arcana) +23, Knowledge (planes) +23, Knowledge (any one other) +20, Perception +31, Sense Motive +23, Spellcraft +23, Stealth +10, Use Magic Device +22; Racial Modifier +8 on Perception
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abyss)
**Organization** solitary or warband (1 nalfeshnee, 1 hezrou, and 2–5 vrocks)
**Treasure** standard

### Special Abilities

**_Unholy_ Nimbus (Su)** Three times per day as a free action a nalfeshnee can create a nimbus of _unholy_ light, causing nauseating beams of writhing color to play around its body. One round later, the light bursts in a 60-foot radius. Any non-demon creature caught within this area must succeed on a DC 22 Will save or be _[[conditions/Dazed|dazed]]_ for 1d10 rounds as visions of madness hound it. The save DC is Charisma-based.

##### Description

Few demons understand the inner workings of the Abyss like the nalfeshnee, and it is not unusual to see a nalfeshnee _[[spells/Seeming|seeming]]_ to serve the Abyss itself rather than a demon lord. Some claim stewardship over the fleshy realms that birth new demons, while others _[[npcs/Guard|guard]]_ sites of particular significance deep in the plane’s secret reaches. Often, a nalfeshnee’s realm in the Abyss surpasses the strength and size of the largest of mortal kingdoms, for nalfeshnees display a singular gift for managing and ordering the chaos of the Abyss. Mortal summoners often seek them out for their unparalleled yet mad intellects, ever taking care to comb through bargains with such demons for hidden and unwanted consequences, for there is little a nalfeshnee will agree to do that does not, in some sinister way, advance the needs and desires of the Abyss.

Nalfeshnees stand 20 feet tall and weigh 8,000 pounds. They form from the souls of greedy or avaricious evil mortals, particularly those who ruled over empires of slavery, theft, banditry, and more violent vices.
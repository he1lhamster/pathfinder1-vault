---
cssclass: [monsters]
title1: Lamia Matriarch
desc_short: This creature looks like a beautiful human woman from the waist up, but
  below is the body and tail of an immense snake.
title2: Lamia Matriarch
CR: 8
sources:
- name: Bestiary 2
  page: 175
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
- name: 'Pathfinder #2: The Skinsaw Murders'
  page: 92
  link: http://paizo.com/pathfinder/adventurePath/riseOfTheRunelords/v5748btpy8029
XP: 4800
alignment: CE
size: Large
type: monstrous humanoid
subtypes:
- shapechanger
initiative:
  bonus: 4
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 21
  touch: 13
  flat_footed: 17
  components:
    dex: 4
    natural: 8
    size: -1
HP:
  HP: 102
  long: 12d10+36
saves:
  fort: 7
  ref: 12
  will: 11
immunities:
- mind-affecting effects
SR: 19
speeds:
  base: 40
  climb: 40
  swim: 40
attacks:
  melee:
  - - text: +1 scimitars +14/+14/+9/+9/+4 (1d6+6/15-20 plus 1 Wisdom drain on first
        hit each round)
      entries:
      - - damage: 1d6+6
          crit_range: 15-20
        - damage: '1'
          type: Wisdom drain on first hit each round
      attack: +1 scimitars
      bonus:
      - 14
      - 14
      - 9
      - 9
      - 4
  - - text: touch +16 (1d4 Wisdom drain)
      entries:
      - - damage: 1d4
          type: Wisdom drain
      attack: touch
      bonus:
      - 16
  special:
  - Wisdom drain
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: charm monster
    source: default
    freq: At will
    DC: 19
  - name: ventriloquism
    source: default
    freq: At will
    DC: 16
  - name: deep slumber
    source: default
    freq: 3/day
    DC: 18
  - name: dream
    source: default
    freq: 3/day
  - name: major image
    source: default
    freq: 3/day
    DC: 18
  - name: mirror image
    source: default
    freq: 3/day
  - name: suggestion
    source: default
    freq: 3/day
    DC: 18
  sources:
  - name: default
    CL: 12
    concentration: 17
spells:
  entries:
  - name: haste
    source: '?'
    level: 3
  - name: death knell
    source: '?'
    level: 2
    DC: 17
  - name: invisibility
    source: '?'
    level: 2
  - name: cure light wounds
    source: '?'
    level: 1
  - name: divine favor
    source: '?'
    level: 1
  - name: mage armor
    source: '?'
    level: 1
  - name: magic missile
    source: '?'
    level: 1
  - name: dancing lights
    source: '?'
    level: 0
  - name: daze
    source: '?'
    level: 0
    DC: 15
  - name: detect magic
    source: '?'
    level: 0
  - name: ghost sound
    source: '?'
    level: 0
    DC: 15
  - name: mage hand
    source: '?'
    level: 0
  - name: mending
    source: '?'
    level: 0
  - name: prestidigitation
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 6
    concentration: 11
    slots:
      3: 4
      2: 6
      1: 8
      0: at-will
ability_scores:
  STR: 20
  DEX: 19
  CON: 17
  INT: 16
  WIS: 16
  CHA: 21
BAB: 12
CMB: 18
CMD: 32
CMD_other: can't be tripped
feats:
- name: Double Slice
- name: Extend Spell
- name: Improved Critical (scimitar)
- name: Improved Two-Weapon Fighting
- name: Two-Weapon Fighting
- name: Weapon Focus (scimitar)
skills:
  Acrobatics: 8
    jump: 12
  Bluff: 21
  Climb: 13
  Diplomacy: 11
  Disguise: 11
  Intimidate: 20
  Knowledge (any one): 15
  Knowledge (arcana): 15
  Spellcraft: 15
  Swim: 13
  Use Magic Device: 21
  Perception: 3
  _racial_mods:
    Acrobatics:
      _: 4
    Bluff:
      _: 4
    Use Magic Device:
      _: 4
languages:
- Abyssal
- Common
- Draconic
special_qualities:
- change shape (fixed Medium humanoid form, alter self)
- undersized weapons
ecology:
  environment: any land
  organization: solitary, pair, or cult (3-6)
  treasure_type: double
  treasure:
  - two +1 scimitars
  - other treasure
special_abilities:
  Spells: A lamia matriarch casts spells as a 6th-level sorcerer, and can cast spells
    from the cleric list as well as those normally available to a sorcerer. Cleric
    spells are considered arcane spells for a lamia matriarch.
  Wisdom Drain (Su): A lamia matriarch drains 1d4 points of Wisdom each time she hits
    with her melee touch attack. The first time each round that she strikes a foe
    with a melee weapon, she also drains 1 point of Wisdom. A DC 21 Will save negates
    the Wisdom drain. Unlike with other kinds of ability drain attacks, a lamia matriarch
    does not heal damage when she uses her Wisdom drain. The save DC is Charisma-based.
desc_long: The queens of a race consumed by bitterness and predatory instinct, lamia
  matriarchs mastermind all manner of foul plots in hopes of breaking the bestial
  curse that afflicts their race. They move with shocking ease from silken-tongued
  temptresses to dervishes, striking with all the deadly precision of vipers. Quick
  to covet, enslave, and overindulge, lamia matriarchs luxuriate in gory feasts, violent
  trysts, and bloody entertainments, reveling until their playthings are broken or
  until they tire and move on.

---

# Lamia Matriarch
This creature looks like a beautiful human woman from the waist up, but below is the body and tail of an immense snake.
**Source** Bestiary 2 pg. 175, Pathfinder #2: The Skinsaw Murders pg. 92
**XP** 4,800
CE Large monstrous humanoid (shapechanger)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +3

##### Defense

**AC** 21, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+4 Dex, +8 natural, –1 size)
**hp** 102 (12d10+36)
**Fort** +7, **Ref** +12, **Will** +11
**Immune** mind-affecting effects; **SR** 19

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 40 ft., swim 40 ft.
**Melee** +1 scimitars +14/+14/+9/+9/+4 (1d6+6/15–20 plus 1 Wisdom drain on first hit each round) or touch +16 (1d4 Wisdom drain)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** Wisdom drain
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +17)
At will—_[[spells/Charm Monster|charm monster]]_ (DC 19), _[[spells/Ventriloquism|ventriloquism]]_ (DC 16)
3/day—_[[spells/Deep Slumber|deep slumber]]_ (DC 18), _[[spells/Dream|dream]]_, _[[spells/Major Image|major image]]_ (DC 18), _[[spells/Mirror Image|mirror image]]_, _[[spells/Suggestion|suggestion]]_ (DC 18)
**Spells Known **(CL 6th; concentration +11)
3rd (4/day)—_[[spells/Haste|haste]]_
2nd (6/day)—_[[spells/Death Knell|death knell]]_ (DC 17), _[[spells/Invisibility|invisibility]]_
1st (8/day)—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 15), _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Prestidigitation|prestidigitation]]_

##### Statistics
**Str** 20, **Dex** 19, **Con** 17, **Int** 16, **Wis** 16, **Cha** 21
**Base Atk** +12; **CMB** +18; **CMD** 32 (can’t be tripped)
**Feats** _[[feats/Double Slice|Double Slice]]_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Improved Critical|Improved Critical]]_ (_[[items/Weapon/Scimitar|scimitar]]_), _[[feats/Improved Two-Weapon Fighting|Improved Two-Weapon Fighting]]_, _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_scimitar_)
**Skills** Acrobatics +8 (+12 _[[spells/Jump|jump]]_), Bluff +21, _Climb_ +13, Diplomacy +11, Disguise +11, Intimidate +20, Knowledge (any one) +15, Knowledge (arcana) +15, Spellcraft +15, Swim +13, Use Magic Device +21; **Racial Modifiers** +4 Acrobatics, +4 Bluff, +4 Use Magic Device
**Languages** Abyssal, Common, Draconic
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (fixed Medium humanoid form, _[[spells/Alter Self|alter self]]_), _[[universal monster rules/Undersized Weapons|undersized weapons]]_

##### Ecology

**Environment** any land
**Organization** solitary, pair, or cult (3–6)
**Treasure** double (two +1 scimitars, other treasure)

### Special Abilities
**Spells **A _[[monsters/Lamia Matriarch|lamia matriarch]]_ casts spells as a 6th-level _[[classes/Sorcerer|sorcerer]]_, and can cast spells from the _[[classes/Cleric|cleric]]_ list as well as those normally available to a _sorcerer_. _Cleric_ spells are considered arcane spells for a _lamia matriarch_.

**Wisdom Drain (Su)** A _lamia matriarch_ drains 1d4 points of Wisdom each time she hits with her melee touch attack. The first time each round that she strikes a foe with a melee weapon, she also drains 1 point of Wisdom. A DC 21 Will save negates the Wisdom drain. Unlike with other kinds of ability drain attacks, a _lamia matriarch_ does not _[[spells/Heal|heal]]_ damage when she uses her Wisdom drain. The save DC is Charisma-based.

##### Description

The queens of a race consumed by bitterness and predatory instinct, _[[monsters/Lamia|lamia]]_ matriarchs mastermind all manner of foul plots in hopes of _[[items/Weapon Magic Abilities/Breaking|breaking]]_ the bestial curse that afflicts their race. They move with shocking ease from silken-tongued temptresses to dervishes, striking with all the _[[items/Weapon Magic Abilities/Deadly|deadly]]_ precision of vipers. Quick to covet, enslave, and overindulge, _lamia_ matriarchs luxuriate in _[[items/Weapon Magic Abilities/Gory|gory]]_ feasts, violent trysts, and bloody entertainments, reveling until their playthings are _[[conditions/Broken|broken]]_ or until they tire and move on.
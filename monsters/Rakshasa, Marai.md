---
cssclass: [monsters]
title1: Rakshasa, Marai
desc_short: This finely robed and nimble fiend has six colorful vipers in place of
  arms, and a long, forked tongue in its fanged mouth.
title2: Marai
CR: 8
sources:
- name: Bestiary 3
  page: 228
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 4800
alignment: LE
size: Medium
type: outsider
subtypes:
- native
- rakshasa
- shapechanger
initiative:
  bonus: 5
senses:
  darkvision: 60
AC:
  AC: 21
  touch: 16
  flat_footed: 15
  components:
    dex: 5
    dodge: 1
    natural: 5
HP:
  HP: 94
  long: 9d10+45
saves:
  fort: 8
  ref: 11
  will: 9
DR:
- amount: 10
  weakness: good and piercing
SR: 23
speeds:
  base: 40
attacks:
  melee:
  - - text: 7 bites +14 (1d4+2 plus confusion)
      entries:
      - - damage: 1d4+2
        - effect: confusion
      count: 7
      attack: bites
      bonus:
      - 14
  ranged:
  - - text: 6 energy bolts +14 touch (1d8 plus special)
      entries:
      - - damage: 1d8
        - effect: special
      count: 6
      attack: energy bolts
      bonus:
      - 14
      touch: true
  special:
  - detect thoughts (DC 18)
  - energy bolts
spells:
  entries:
  - name: invisibility
    source: '?'
    level: 2
  - name: scorching ray
    source: '?'
    level: 2
  - name: charm person
    source: '?'
    level: 1
    DC: 15
  - name: jump
    source: '?'
    level: 1
  - name: mage armor
    source: '?'
    level: 1
  - name: magic missile
    source: '?'
    level: 1
  - name: bleed
    source: '?'
    level: 0
    DC: 14
  - name: detect magic
    source: '?'
    level: 0
  - name: ghost sound
    source: '?'
    level: 0
    DC: 14
  - name: mage hand
    source: '?'
    level: 0
  - name: open/close
    source: '?'
    level: 0
  - name: read magic
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 5
    concentration: 9
    slots:
      2: 5
      1: 7
      0: at-will
ability_scores:
  STR: 14
  DEX: 21
  CON: 20
  INT: 11
  WIS: 13
  CHA: 18
BAB: 9
CMB: 11
CMD: 27
feats:
- name: Dodge
- name: Iron Will
- name: Silent Spell
- name: Still Spell
- name: Weapon Finesse
skills:
  Acrobatics: 14
    when jumping: 18
  Bluff: 20
  Climb: 7
  Disguise: 16
  Knowledge (arcana): 8
  Perception: 10
  Sense Motive: 12
  Spellcraft: 8
  _racial_mods:
    Bluff:
      _: 4
    Disguise:
      _: 8
languages:
- Common
- Infernal
- Undercommon
special_qualities:
- change shape (any humanoid; alter self)
ecology:
  environment: any
  organization: solitary, pair, cult (3-12)
  treasure_type: standard
special_abilities:
  Confusion (Su): A creature bitten by a marai's bite (from either its actual mouth
    or the snakes it has for hands) must succeed at a DC 19 Will save or become confused
    for 1 round. The save DC is Constitution-based.
  Energy Bolts (Ex): |-
    Once every 1d4 rounds as a standard action that provokes an attack of opportunity, a marai's six snake arms can each spit a bolt of energy to a maximum range of 60 feet. Each bolt deals 1d8 points of damage and has an additional effect if the target fails to resist it with a DC 19 Fortitude save, as summarized below. The save DC is Constitution-based.

     Amethyst Viper: Cold damage plus sickened for 1d4 rounds.
     Crimson Viper: Fire damage plus burn (1d4, DC 19).
     Emerald Viper: Acid damage plus nauseated for 1 round.
     Magenta Viper: Electricity damage plus staggered for 1 round.
     Turquoise Viper: Sonic damage plus stunned for 1 round.
     Violet Viper: Force damage plus knocked prone.
  Spells: A marai casts arcane spells as a 5th-level sorcerer.
desc_long: |-
  Marai are deviant spellcasters first and fiendish corruptors second. If allowed to indulge in their desire for perverse mystical study, most marai are content to serve as part of another rakshasa's cabal. A solitary marai might pose as a neophyte magician to infiltrate another spellcaster's abode. If the marai is successful, the master soon becomes either the servant or a corpse.

  The possibility of new magical discoveries drives a marai. Morality and compassion never constrain the fiend's experiments. A marai prefers to torment and exploit mortals who have no idea of the rakshasa's true nature, and it takes great pleasure in using magical might to bring would-be heroes, especially those who invade its lair, to their knees. Such a game offers a marai enjoyment, however, only if subjects are unaware of the danger or at least unable to oppose it.

  A marai is 6 feet tall and weighs 160 pounds. Its serpentine arms render fine manipulation or wielding weapons unfeasible, and so it typically assumes humanoid form when working on experiments that require manual dexterity. A marai unable to do so must rely upon cantrips like mage hand for such tasks-or perhaps the aid of a slave or charmed ally.

---

# Rakshasa, Marai
This finely robed and nimble fiend has six colorful vipers in place of arms, and a long, forked tongue in its fanged mouth.
**Source** Bestiary 3 pg. 228
**XP** 4,800

LE Medium outsider (native, _[[monsters/Rakshasa|rakshasa]]_, shapechanger)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +10

##### Defense

**AC** 21, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+5 Dex, +1 _[[feats/Dodge|dodge]]_, +5 natural)
**hp** 94 (9d10+45)
**Fort** +8, **Ref** +11, **Will** +9
**DR** 10/good and piercing; **SR** 23

##### Offense
**Speed** 40 ft.
**Melee** 7 bites +14 (1d4+2 plus _[[spells/Confusion|confusion]]_)
**Ranged** 6 energy bolts +14 touch (1d8 plus special)
**Special Attacks** _[[spells/Detect Thoughts|detect thoughts]]_ (DC 18), energy bolts
**Spells Known **(CL 5th; concentration +9)
2nd (5/day)—_[[spells/Invisibility|invisibility]]_, _[[spells/Scorching Ray|scorching ray]]_
1st (7/day)—_[[spells/Charm Person|charm person]]_ (DC 15), _[[spells/Jump|jump]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 14), _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 14), _[[spells/Mage Hand|mage hand]]_, open/close, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 14, **Dex** 21, **Con** 20, **Int** 11, **Wis** 13, **Cha** 18
**Base Atk** +9; **CMB** +11; **CMD** 27
**Feats** _Dodge_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Silent Spell|Silent Spell]]_, _[[feats/Still Spell|Still Spell]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +14 (+18 when jumping), Bluff +20, _[[universal monster rules/Climb|Climb]]_ +7, Disguise +16, Knowledge (arcana) +8, Perception +10, Sense Motive +12, Spellcraft +8; **Racial Modifiers** +4 Bluff, +8 Disguise
**Languages** Common, Infernal, Undercommon
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (any humanoid; _[[spells/Alter Self|alter self]]_)

##### Ecology

**Environment** any
**Organization** solitary, pair, cult (3–12)
**Treasure** standard

### Special Abilities

**_Confusion_ (Su) **A creature bitten by a marai’s bite (from either its actual mouth or the snakes it has for hands) must succeed at a DC 19 Will save or become _[[conditions/Confused|confused]]_ for 1 round. The save DC is Constitution-based.

**Energy Bolts (Ex)** Once every 1d4 rounds as a standard action that provokes an attack of opportunity, a marai’s six snake arms can each spit a bolt of energy to a maximum range of 60 feet. Each bolt deals 1d8 points of damage and has an additional effect if the target fails to resist it with a DC 19 Fortitude save, as summarized below. The save DC is Constitution-based.

Amethyst Viper: Cold damage plus _[[conditions/Sickened|sickened]]_ for 1d4 rounds.
 Crimson Viper: Fire damage plus _[[universal monster rules/Burn|burn]]_ (1d4, DC 19).
 Emerald Viper: Acid damage plus _[[conditions/Nauseated|nauseated]]_ for 1 round.
 Magenta Viper: Electricity damage plus _[[conditions/Staggered|staggered]]_ for 1 round.
 Turquoise Viper: Sonic damage plus _[[conditions/Stunned|stunned]]_ for 1 round.
 Violet Viper: Force damage plus knocked _[[conditions/Prone|prone]]_.
**Spells **A marai casts arcane spells as a 5th-level _[[classes/Sorcerer|sorcerer]]_.

##### Description

Marai are deviant spellcasters first and fiendish corruptors second. If allowed to indulge in their desire for perverse mystical study, most marai are content to serve as part of another _rakshasa_’s cabal. A solitary marai might pose as a neophyte magician to infiltrate another spellcaster’s abode. If the marai is successful, the master soon becomes either the servant or a corpse.

The possibility of new magical discoveries drives a marai. Morality and compassion never constrain the fiend’s experiments. A marai prefers to torment and exploit mortals who have no idea of the _rakshasa_’s true nature, and it takes great pleasure in using magical might to bring would-be heroes, especially those who invade its lair, to their knees. Such a game offers a marai enjoyment, however, only if subjects are unaware of the danger or at least unable to oppose it.

A marai is 6 feet tall and weighs 160 pounds. Its serpentine arms render fine manipulation or wielding weapons unfeasible, and so it typically assumes humanoid form when working on experiments that require manual dexterity. A marai unable to do so must rely upon cantrips like _mage hand_ for such tasks—or perhaps the aid of a _[[items/Mundane/Slave|slave]]_ or charmed ally.
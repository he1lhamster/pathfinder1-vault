---
cssclass: [monsters]
title1: Devil, Cabal Devil (Uniila)
desc_short: The curves of a shapely maiden define the outline of a mysterious figure
  wrapped in mist and strips of ancient robes. From beneath the rune-embroidered tatters
  stretch four, corpse-pale arms, each bearing either a blade or some mysterious arcane
  device. Hidden within the cowl of its hood shimmer the faintest outlines of a veiled
  face and a pair of eyes flickering with barely restrained energy.
title2: Cabal Devil (Uniila)
CR: 10
sources:
- name: 'Pathfinder #28: The Infernal Syndrome'
  page: 86
  link: http://paizo.com/pathfinder/adventurePath/councilOfThieves/v5748btpy8b9h
XP: 9600
alignment: LE
size: Medium
type: outsider
subtypes:
- devil
- evil
- extraplanar
- incorporeal
- lawful
initiative:
  bonus: 6
senses:
  darkvision: 60
  see in darkness: true
AC:
  AC: 22
  touch: 22
  flat_footed: 15
  components:
    deflection: 5
    dex: 6
    dodge: 1
HP:
  HP: 95
  long: 10d10+40
saves:
  fort: 11
  ref: 15
  will: 7
DR:
- amount: 10
  weakness: good
immunities:
- fire
- poison
resistances:
  acid: 10
  cold: 10
SR: 21
speeds:
  fly: 40
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 4 +1 daggers +17 (1d4+1/19-20)
      entries:
      - - damage: 1d4+1
          crit_range: 19-20
      count: 4
      attack: +1 daggers
      bonus:
      - 17
  ranged:
  - - text: 4 +1 daggers +17 (1d4+1/19-20)
      entries:
      - - damage: 1d4+1
          crit_range: 19-20
      count: 4
      attack: +1 daggers
      bonus:
      - 17
  special:
  - dread magic
spell_like_abilities:
  entries:
  - name: augury
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: true seeing
    source: default
    freq: At will
  - name: unseen servant
    source: default
    freq: At will
  - name: bestow curse
    source: default
    freq: 3/day
    DC: 19
  - name: blink
    source: default
    freq: 3/day
  - name: detect thoughts
    source: default
    freq: 3/day
    DC: 17
  - name: dispel magic
    source: default
    freq: 3/day
  - name: invisibility
    source: default
    freq: 3/day
  - name: blasphemy
    source: default
    freq: 1/day
    DC: 22
  - name: mark of justice
    source: default
    freq: 1/day
  - name: summon devil
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: imps
      amount: 2d4
      chance: 55%
  sources:
  - name: default
    CL: 8
spells:
  entries:
  - name: summon monster IV
    source: '?'
    level: 4
  - name: fireball
    source: '?'
    level: 3
    DC: 18
  - name: gaseous form
    source: '?'
    level: 3
  - name: fog cloud
    source: '?'
    level: 2
  - name: glitterdust
    source: '?'
    level: 2
    DC: 17
  - name: mirror image
    source: '?'
    level: 2
    DC: 17
  - name: disguise self
    source: '?'
    level: 1
  - name: identify
    source: '?'
    level: 1
  - name: magic missile
    source: '?'
    level: 1
  - name: ray of enfeeblement
    source: '?'
    level: 1
    DC: 16
  - name: shield
    source: '?'
    level: 1
  - name: arcane mark
    source: '?'
    level: 0
  - name: bleed
    source: '?'
    level: 0
    DC: 15
  - name: dancing lights
    source: '?'
    level: 0
  - name: detect magic
    source: '?'
    level: 0
  - name: disrupt undead
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: prestidigitation
    source: '?'
    level: 0
  - name: touch of fatigue
    source: '?'
    level: 0
    DC: 15
  sources:
  - name: '?'
    type: known
    CL: 8
    slots:
      4: 3
      3: 5
      2: 6
      1: 6
ability_scores:
  STR: 11
  DEX: 22
  CON: 19
  INT: 22
  WIS: 18
  CHA: 21
BAB: 10
CMB: 10
CMD: 32
feats:
- name: Dodge
- name: Lightning Reflexes
- name: Mobility
- name: Scribe ScrollB
- name: Weapon Finesse
- name: Wind Stance
skills:
  Appraise: 16
  Bluff: 18
  Diplomacy: 18
  Disguise: 18
  Fly: 14
  Knowledge (arcana): 19
  Knowledge (planes): 19
  Knowledge (religion): 19
  Perception: 17
  Sense Motive: 17
  Sleight of Hand: 16
  Spellcraft: 16
  Stealth: 19
languages:
- Aklo
- Celestial
- Common
- Draconic
- Infernal
- Undercommon
- telepathy 100 ft.
special_qualities:
- infernal arcana
- scroll mastery
- witch token
ecology:
  environment: any (Hell)
  organization: solitary, pair or cabal (3-9)
  treasure_type: double
  treasure:
  - 4 +1 daggers
  - other treasure as magic scrolls and writings
special_abilities:
  Dread Magic (Su): All spells an uniila casts draw upon terrible infernal eddies
    and the torment of damned souls. As such, all of an uniila's spells (not her spell-like
    abilities) are strange and terrible to behold. This increases the Spellcraft DC
    required to identify an uniila's spell as it is being cast by +5. In addition,
    at will, an uniila can choose to make a spell she casts particularly frightening.
    Any creature forced to make a saving throw to resist a spell cast by an uniila
    must make an additional Will save at the same DC or be shaken for 1 round. This
    effect can potentially increase the severity of other fear effects. This is a
    mind-affecting fear effect.
  Infernal Arcana (Su): |-
    Once per day, after spending a minute whispering strange formulas and cosmic truths, an uniila can grant an adjacent mortal spellcaster additional profane insight into the ways of magic. This counts as a bonus spell prepared or spell per day of 6th level or lower, which is immediately accessible by the target in addition to all its regular spells. The uniila chooses what spell to grant the target. It need not be a spell already known by the target, though it must be of 6th level or lower and of a level he can cast or from his class's spell list. This spell remains available to the target for 24 hours. The spell can be any arcane or divine spell. An uniila can never use this ability on herself or non-mortal targets.

    Once a target chooses to make use of this spell, it is cast at the uniila's caster level (typically 8th) and is treated as having the evil subtype. In addition, as the uniila chooses, she may spontaneously add the effects of any metamagic feat to the spell (without the spell being treated as though it were of an increased spell level). Typically, uniilas use this ability to compel magic users to rely on them for more powerful magic, though they might also use effects like Widen Spell to affect unintended targets.
  Scroll Mastery (Su): All uniilas possess Scribe Scroll as a bonus feat. An uniila
    is treated as knowing all spells of 6th level or lower in the Pathfinder RPG Core
    Rulebook and can create scrolls of any of those spells. Whether an uniila knows
    rarer magic is decided by the GM.
  Summon Devil (Su): Once per day, an uniila can attempt to summon 2d4 imps with a
    55% chance of success. This ability is the equivalent of a 4th-level spell.
  Witch Token (Su): |-
    By spending an hour in concentration, an uniila can create a token of arcane power. This token may take any form that takes up an item slot, and typically appears as a subtly fiendish ring, amulet, or similar piece of jewelry. While it is worn by a mortal, all of the DCs of any spells the wearer casts increase by +1 (this effect stacks with Spell Focus). However, while wearing a witch token, the bearer takes a -5 penalty on all saves made to resist spells and effects cast by the token's creation. Also, while the token is being worn, the uniila can effectively scry through the token at will and without the wearer's knowledge as long as he remains on the same plane. Spells and effects that typically bar or confound scry also affect the witch token.

    As a standard action, an uniila can cause her witch token to erupt in a burst of destructive magic that deals 10d6 points of damage to the wearer. An uniila can only ever have one witch token in existence at a time and must destroy a previously created token before creating a new one. The damage of this effect is based on the uniila's Hit Dice.

    All witch tokens are also under effects similar to magic aura, and are detected as possessing auras of moderate universal magic. Those who use identify or a similar spell must succeed at a DC 20 Will save to receive correct information (that the token sheds an aura of strong divination). Detect evil reveals no aura from a witch token. The saving throw is Charisma-based.
desc_long: 'The tools devils use to ensnare the minds and ultimately the souls of
  their victims vary incredibly, from the most blatant of infernal corruptions to
  enticements that seem not like temptations at all. The elusive cabal devils, or
  uniilas as they are known by diabolists, employ one of the most seductive drugs
  in existence in their snares: magic. Mistresses of the arcane with an understanding
  of the cultic arts-both arcane and divine-that rivals even that of many greater
  fiends, these mysterious and aloof sages haunt the most ancient ruins and moldering
  depths of Stygia, the fifth layer of Hell, researching arcana and puzzling over
  formulae destined to shake the cosmos. When conjured forth or left to their own
  devices upon the Material Plane, uniilas make no untoward offers or forceful demands
  of their mortal hosts; they merely offer greater magical power in any of the various
  ways they might do so. Should the ease with which such might is granted pollute
  a mortal's ambitions or lead him to rely upon a devil for his power, such ultimately
  proves the student's fault, not the eager teacher's. So too does the resulting damnation
  at the end of the mortal's short life prove more of his own doing than any overt
  diabolical trap, making uniilas' methods all the more sinister for their subtlety.'

---

# Devil, Cabal Devil (Uniila)
The curves of a shapely maiden define the outline of a mysterious figure wrapped in mist and strips of ancient robes. From beneath the rune-embroidered tatters stretch four, corpse-pale arms, each bearing either a blade or some mysterious arcane device. Hidden within the cowl of its hood shimmer the faintest outlines of a veiled face and a pair of eyes flickering with barely restrained energy.
**Source** Pathfinder #28: The Infernal Syndrome pg. 86
**XP** 9,600

LE Medium outsider (devil, evil, extraplanar, _[[universal monster rules/Incorporeal|incorporeal]]_, lawful)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +17

##### Defense

**AC** 22, touch 22, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+5 _[[spells/Deflection|deflection]]_, +6 Dex, +1 _[[feats/Dodge|dodge]]_)
**hp** 95 (10d10+40)
**Fort** +11, **Ref** +15, **Will** +7
**DR** 10/good; **Immune** fire, poison; **Resist** acid 10, cold 10; **SR** 21

##### Offense
**Speed** fly 40 ft. (perfect)
**Melee** 4 +1 daggers +17 (1d4+1/19-20)
**Ranged** 4 +1 daggers +17 (1d4+1/19-20)
**Special Attacks** dread magic
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th)
At will — _[[spells/Augury|augury]]_, greater teleport (self plus 50 lbs. of objects only), _[[spells/True Seeing|true seeing]]_, _[[spells/Unseen Servant|unseen servant]]_
3/day — _[[spells/Bestow Curse|bestow curse]]_ (DC 19), _[[spells/Blink|blink]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 17), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Invisibility|invisibility]]_
1/day — _[[spells/Blasphemy|blasphemy]]_ (DC 22), _[[spells/Mark of Justice|mark of justice]]_, _[[universal monster rules/Summon|summon]]_ devil (level 4, 2d4 imps 55%)
**Spells Known** (CL 8th)
4th (3/day) — _[[spells/Summon Monster IV|summon monster IV]]_
3rd (5/day) — _[[spells/Fireball|fireball]]_ (DC 18), _[[spells/Gaseous Form|gaseous form]]_
2nd (6/day) — _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Glitterdust|glitterdust]]_ (DC 17), _[[spells/Mirror Image|mirror image]]_ (DC 17)
1st (6/day) — _[[spells/Disguise Self|disguise self]]_, _[[spells/Identify|identify]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 16), _[[spells/Shield|shield]]_
0 — _[[spells/Arcane Mark|arcane mark]]_, _[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Disrupt Undead|disrupt undead]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 15)

##### Statistics
**Str** 11, **Dex** 22, **Con** 19, **Int** 22, **Wis** 18, **Cha** 21
**Base Atk** +10; **CMB** +10; **CMD** 32
**Feats** _Dodge_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, Scribe ScrollB, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Wind Stance|Wind Stance]]_
**Skills** Appraise +16, Bluff +18, Diplomacy +18, Disguise +18, Fly +14, Knowledge (arcana) +19, Knowledge (planes) +19, Knowledge (religion) +19, Perception +17, Sense Motive +17, Sleight of Hand +16, Spellcraft +16, Stealth +19
**Languages** Aklo, Celestial, Common, Draconic, Infernal, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** infernal arcana, scroll mastery, _[[classes/Witch|witch]]_ token

##### Ecology

**Environment** any (Hell)
**Organization** solitary, pair or cabal (3-9)
**Treasure** double (4 +1 daggers, other treasure as magic scrolls and writings)

### Special Abilities

**Dread Magic (Su)** All spells an uniila casts draw upon terrible infernal eddies and the torment of _[[feats/Damned|damned]]_ souls. As such, all of an uniila’s spells (not her _spell-like abilities_) are strange and terrible to behold. This increases the Spellcraft DC required to _identify_ an uniila’s spell as it is being cast by +5. In addition, at will, an uniila can choose to make a spell she casts particularly frightening. Any creature forced to make a saving throw to resist a spell cast by an uniila must make an additional Will save at the same DC or be _[[conditions/Shaken|shaken]]_ for 1 round. This effect can potentially increase the severity of other _[[universal monster rules/Fear|fear]]_ effects. This is a mind-affecting _fear_ effect.

**Infernal Arcana (Su)** Once per day, after spending a minute whispering strange formulas and cosmic truths, an uniila can grant an adjacent mortal spellcaster additional profane insight into the ways of magic. This counts as a bonus spell prepared or spell per day of 6th level or lower, which is immediately accessible by the target in addition to all its regular spells. The uniila chooses what spell to grant the target. It need not be a spell already known by the target, though it must be of 6th level or lower and of a level he can cast or from his class’s spell list. This spell remains available to the target for 24 hours. The spell can be any arcane or divine spell. An uniila can never use this ability on herself or non-mortal targets.

Once a target chooses to make use of this spell, it is cast at the uniila’s caster level (typically 8th) and is treated as having the evil subtype. In addition, as the uniila chooses, she may spontaneously add the effects of any metamagic feat to the spell (without the spell being treated as though it were of an increased spell level). Typically, uniilas use this ability to compel magic users to rely on them for more powerful magic, though they might also use effects like _[[feats/Widen Spell|Widen Spell]]_ to affect unintended targets.
**Scroll Mastery (Su)** All uniilas possess _[[feats/Scribe Scroll|Scribe Scroll]]_ as a bonus feat. An uniila is treated as knowing all spells of 6th level or lower in the Pathfinder RPG Core Rulebook and can create scrolls of any of those spells. Whether an uniila knows rarer magic is decided by the GM.
**_Summon_ Devil (Su)** Once per day, an uniila can attempt to _summon_ 2d4 imps with a 55% chance of success. This ability is the equivalent of a 4th-level spell.

**_Witch_ Token (Su)** By spending an hour in concentration, an uniila can create a token of arcane power. This token may take any form that takes up an item slot, and typically appears as a subtly fiendish ring, amulet, or similar piece of _[[items/Mundane/Jewelry|jewelry]]_. While it is worn by a mortal, all of the DCs of any spells the wearer casts increase by +1 (this effect stacks with _[[feats/Spell Focus|Spell Focus]]_). However, while wearing a _witch_ token, the bearer takes a –5 penalty on all saves made to resist spells and effects cast by the token’s creation. Also, while the token is being worn, the uniila can effectively scry through the token at will and without the wearer’s knowledge as long as he remains on the same plane. Spells and effects that typically bar or confound scry also affect the _witch_ token.

As a standard action, an uniila can cause her _witch_ token to erupt in a burst of destructive magic that deals 10d6 points of damage to the wearer. An uniila can only ever have one _witch_ token in existence at a time and must destroy a previously created token before creating a new one. The damage of this effect is based on the uniila’s Hit Dice.

All _witch_ tokens are also under effects similar to _[[spells/Magic Aura|magic aura]]_, and are detected as possessing auras of moderate universal magic. Those who use _identify_ or a similar spell must succeed at a DC 20 Will save to receive correct information (that the token sheds an aura of strong _[[spells/Divination|divination]]_). _[[spells/Detect Evil|Detect evil]]_ reveals no aura from a _witch_ token. The saving throw is Charisma-based.

##### Description

The tools devils use to ensnare the minds and ultimately the souls of their victims vary incredibly, from the most blatant of infernal corruptions to enticements that seem not like temptations at all. The elusive cabal devils, or uniilas as they are known by diabolists, employ one of the most seductive drugs in existence in their snares: magic. Mistresses of the arcane with an understanding of the cultic arts—both arcane and divine—that rivals even that of many greater fiends, these mysterious and aloof sages haunt the most ancient ruins and moldering depths of Stygia, the fifth layer of Hell, researching arcana and puzzling over formulae destined to shake the cosmos. When conjured forth or left to their own devices upon the Material Plane, uniilas make no untoward offers or forceful demands of their mortal hosts; they merely offer greater magical power in any of the various ways they might do so. Should the ease with which such might is granted pollute a mortal’s ambitions or lead him to rely upon a devil for his power, such ultimately proves the student’s fault, not the eager teacher’s. So too does the resulting _[[spells/Damnation|damnation]]_ at the end of the mortal’s short life prove more of his own doing than any overt diabolical trap, making uniilas’ methods all the more sinister for their subtlety.
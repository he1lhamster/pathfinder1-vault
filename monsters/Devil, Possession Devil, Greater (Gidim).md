---
cssclass: [monsters]
title1: Devil, Possession Devil, Greater (Gidim)
title2: Possession Devil, Greater (Gidim)
CR: 15
sources:
- name: 'Pathfinder #29: Mother of Flies'
  page: 83
  link: http://paizo.com/pathfinder/adventurePath/councilOfThieves/v5748btpy8bc1
XP: 51200
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
  bonus: 8
senses:
  darkvision: 60
  see in darkness: true
AC:
  AC: 24
  touch: 24
  flat_footed: 15
  components:
    deflection: 5
    dex: 8
    dodge: 1
HP:
  HP: 187
  long: 15d10+105
saves:
  fort: 16
  ref: 19
  will: 12
DR:
- amount: 10
  weakness: good
resistances:
  acid: 10
  cold: 10
SR: 26
speeds:
  base: 30
  fly: 40
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 claws +19 (1d4+5)
      entries:
      - - damage: 1d4+5
      count: 2
      attack: claws
      bonus:
      - 19
    - text: bite +19 (1d6+5)
      entries:
      - - damage: 1d6+5
      attack: bite
      bonus:
      - 19
  special:
  - dread
  - malevolence
spell_like_abilities:
  entries:
  - name: greater invisibility
    source: default
    freq: Constant
  - name: bleed
    source: default
    freq: At will
    DC: 15
  - name: ghost sound
    source: default
    freq: At will
    DC: 15
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: knock
    source: default
    freq: At will
    DC: 17
  - name: levitate
    source: default
    freq: At will
    DC: 17
  - name: major image
    source: default
    freq: At will
    DC: 18
  - name: prestidigitation
    source: default
    freq: At will
    DC: 15
  - name: unseen servant
    source: default
    freq: At will
    DC: 16
  - name: animate dead
    source: default
    freq: 3/day
  - name: animate rope
    source: default
    freq: 3/day
    DC: 16
  - name: bestow curse
    source: default
    freq: 3/day
    DC: 19
  - name: contagion
    source: default
    freq: 3/day
    DC: 19
  - name: dancing lights
    source: default
    freq: 3/day
    DC: 15
  - name: ethereal jaunt
    source: default
    freq: 3/day
    other: Ethereal Plane to Material Plane and vice versa
  - name: gust of wind
    source: default
    freq: 3/day
    DC: 17
  - name: major creation
    source: default
    freq: 3/day
  - name: plane shift
    source: default
    freq: 3/day
    paren_text: self only; to Ethereal Plane, Hell, or Material Plane only
  - name: produce flame
    source: default
    freq: 3/day
    DC: 16
  - name: stinking cloud
    source: default
    freq: 3/day
    DC: 18
  - name: suggestion
    source: default
    freq: 3/day
    DC: 18
  - name: summon
    source: default
    freq: 1/day
    level: 5
    summons:
    - name: lesser possession devils
      amount: 1d4
      chance: 40%
  sources:
  - name: default
    CL: 12
ability_scores:
  STR:
  DEX: 26
  CON: 24
  INT: 17
  WIS: 20
  CHA: 20
BAB: 15
CMB: 23
CMD: 39
feats:
- name: Alertness
- name: Combat Reflexes
- name: Dodge
- name: Improved Iron Will
- name: Iron Will
- name: Lightning Reflexes
- name: Mobility
- name: Stand Still
skills:
  Acrobatics: 26
  Bluff: 23
  Diplomacy: 23
  Disable Device: 26
  Fly: 16
  Intimidate: 23
  Knowledge (planes): 21
  Perception: 27
  Sense Motive: 27
  Stealth: 26
languages:
- Aklo
- Common
- Infernal
special_qualities:
- nourished by negativity
- otherworldly
ecology:
  environment: any (Hell or Ethereal Plane)
  organization: solitary
  treasure_type: none
special_abilities:
  Claws (Su): A gidim's natural attacks inflict real wounds when they rake against
    physical objects they strike. A gidim's natural weapon damage is modified by its
    Charisma bonus.
  Dread (Su): Gidims are adept at using their spell-like abilities to terrifying effect.
    At will, and while remaining invisible, a gidim can choose to make any of the
    spell-like abilities noted in its stat block particularly frightening. Any creature
    that witnesses and is within 10 feet of the effect of one of these spell-like
    abilities must make a saving throw or be shaken for 1 minute. This effect can
    potentially increase the severity of other fear effects. This is a mind-affecting
    fear effect.
  Malevolence (Su): Once per day, a gidim on the Material Plane can merge its body
    with another creature's. This ability is similar to a magic jar spell (CL 10th
    or the devil's HD, whichever is higher), except that it does not require a receptacle.
    To use this ability, the devil must be adjacent to the target. The target can
    resist the attack with a successful DC 16 Will save. A creature that successfully
    saves is immune to that same devil's malevolence for 24 hours. While using this
    ability, the gidim is not affected by its otherworldly ability. The save DC is
    Charisma-based.
  Nourished by Negativity (Su): Gidims seek out volatile mortals to aid them in entering
    the Material Plane. At the most basic level, negative emotions occur when a creature
    is dying, raging, or subject to a fear effect. At the GM's discretion, negative
    emotions might also include non-rules-related effects, such as extreme feelings
    of anger, betrayal, frustration, hate, or sorrow. Anytime a gidim witnesses a
    creature affected by negative emotions, it may choose to gain a +1 bonus on its
    next Will save made to enter the Material Plane, so long as it attempts to enter
    the plane within 30 feet of that creature and within 24 hours. If within 12 to
    24 hours of gaining this bonus the gidim witness the same creature again being
    affected by negative emotions, it gains an additional +1 bonus on its Will save
    which stacks with the original and increases the duration of the bonus by an additional
    24 hours. Thus, a gidim may gain a stacking +1 bonus to its Will save in this
    manner once every 12 hours. The devil loses its entire accumulated bonus if it
    attempts and fails to enter the Material Plane, if 24 hours pass without it witnessing
    its target creature being affected by negative emotions, or if it takes a bonus
    from another creature affected by negative emotions. Once on the Material Plane,
    this bonus applies to a gidim's Will saves made to resist being expelled from
    the plane. The bonus decreases by 1 every minute until it reaches 0. A gidim that
    leaves the Material Plane before this bonus reaches 0 retains any remaining bonus.
  Otherworldly (Ex): Gidims find it difficult to enter the Material Plane. To do so
    by any means, a lesser possession devil must make a DC 30 Will save, failure meaning
    it is barred from entry and cannot access the plane again for 12 hours. In addition,
    after every minute of being on the Material Plane, the devil must make a DC 30
    Will save or be expelled, returning to the plane it traveled from. Additionally,
    as a free action a number of times per day equal to the gidim's Charisma modifier,
    the devil can empower one of its spell-like abilities to extend out from the Ethereal
    Plane and affect a target on the Material Plane.
  Sunlight Weakness (Ex): Gidims' powers are weakened in natural sunlight (not merely
    a daylight spell), reducing the DCs of their special abilities by -4. In addition,
    gidims attempting to enter the Material Plane into an area of sunlight take a
    -4 penalty on their Will save.
desc_long: |-
  Diabolically clever and immortally creative, the legions of Hell use all the tools at their disposal to undermine and corrupt the souls of mortalkind. Among these tools are the souls of unabashedly depraved and hateful mortals sentenced to Hell in punishment for lives of sin. The foulest of these souls occasionally find themselves plucked from their torments and reforged in infernal crucibles, etched with bindings of hellish magic, then set loose upon the living. These evil souls bear many of the powers of devils, but fall outside the normal infernal hierarchies, not being considered true devils by their fiendish peers. Rather, they are gidims, Hell-bound souls made weapons of the Pit. 

   More than mere souls yet less than fiends, gidims find themselves barred from the mortal plane by the laws of existence. Their minds and memories linger on half-forgotten lives, however, and upon emotions and sensations long lost to fiends. Thus, they endlessly seek ways to infiltrate the paths of the living. Traveling to the Ethereal Plane, they peer into the Material Plane, seeking out hapless mortals and drawing power from their hatred, their violence, their sorrow, and especially their fears. Continued feeding upon and encouragement of such emotions grants them greater ability to invade the mortal realm and potentially steal new bodies, through which their foulness might live again.

   Two breeds of gidim exist, lesser possession devils and greater. Both appear nearly identical, but greater possession devils are created from spirits of extraordinary, near-legendary evil beings. These foulest of souls are granted even more powerful diabolical abilities and are often loosed by their infernal masters to torment, unhinge, and ultimately destroy the mortal enemies of Hell. Lesser possession devils are typically left to their own devices, using their abilities to sow fear, torment innocents, spread mistrust, and ruin lives.

---

# Devil, Possession Devil, Greater (Gidim)

**Source** Pathfinder #29: Mother of Flies pg. 83
**XP** 51,200

LE Medium outsider (devil, evil, extraplanar, _[[universal monster rules/Incorporeal|incorporeal]]_, lawful)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +27

##### Defense

**AC** 24, touch 24, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+5 _[[spells/Deflection|deflection]]_, +8 Dex, +1 _[[feats/Dodge|dodge]]_)
**hp** 187 (15d10+105)
**Fort** +16, **Ref** +19, **Will** +12
**DR** 10/good; **Resist** acid 10, cold 10; **SR** 26

##### Offense
**Speed** 30 ft., fly 40 ft. (perfect)
**Melee** 2 claws +19 (1d4+5), bite +19 (1d6+5)
**Special Attacks** dread, malevolence
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th)
Constant — greater _[[spells/Invisibility|invisibility]]_
At will — _[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Ghost Sound|ghost sound]]_* (DC 15), greater teleport (self plus 50 lbs. of objects only), _[[spells/Knock|knock]]_* (DC 17), _[[spells/Levitate|levitate]]_* (DC 17), _[[spells/Major Image|major image]]_* (DC 18), _[[spells/Prestidigitation|prestidigitation]]_* (DC 15), _[[spells/Unseen Servant|unseen servant]]_* (DC 16)
3/day — _[[spells/Animate Dead|animate dead]]_, _[[spells/Animate Rope|animate rope]]_* (DC 16), _[[spells/Bestow Curse|bestow curse]]_ (DC 19), _[[spells/Contagion|contagion]]_ (DC 19), _[[spells/Dancing Lights|dancing lights]]_* (DC 15), _[[spells/Ethereal Jaunt|ethereal jaunt]]_ (Ethereal Plane to Material Plane and vice versa), _[[spells/Gust Of Wind|gust of wind]]_* (DC 17), _[[spells/Major Creation|major creation]]_, _[[spells/Plane Shift|plane shift]]_ (self only; to Ethereal Plane, Hell, or Material Plane only), _[[spells/Produce Flame|produce flame]]_* (DC 16), _[[spells/Stinking Cloud|stinking cloud]]_ (DC 18), _[[spells/Suggestion|suggestion]]_ (DC 18)
1/day — _[[universal monster rules/Summon|summon]]_ (level 5, 1d4 lesser _[[spells/Possession|possession]]_ devils, 40%)
* causes dread

##### Statistics
**Str** —, **Dex** 26, **Con** 24, **Int** 17, **Wis** 20, **Cha** 20
**Base Atk** +15; **CMB** +23; **CMD** 39
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Stand Still|Stand Still]]_
**Skills** Acrobatics +26, Bluff +23, Diplomacy +23, Disable Device +26, Fly +16, Intimidate +23, Knowledge (planes) +21, Perception +27, Sense Motive +27, Stealth +26
**Languages** Aklo, Common, Infernal
**SQ** nourished by negativity, otherworldly

##### Ecology

**Environment** any (Hell or Ethereal Plane)
**Organization** solitary
**Treasure** none

### Special Abilities

**Claws (Su)** A gidim’s _[[universal monster rules/Natural Attacks|natural attacks]]_ inflict real wounds when they _[[universal monster rules/Rake|rake]]_ against physical objects they strike. A gidim’s natural weapon damage is modified by its Charisma bonus.

**Dread (Su)** Gidims are adept at using their _spell-like abilities_ to terrifying effect. At will, and while remaining _[[conditions/Invisible|invisible]]_, a gidim can choose to make any of the _spell-like abilities_ noted in its stat block particularly frightening. Any creature that witnesses and is within 10 feet of the effect of one of these _spell-like abilities_ must make a saving throw or be _[[conditions/Shaken|shaken]]_ for 1 minute. This effect can potentially increase the severity of other _[[universal monster rules/Fear|fear]]_ effects. This is a mind-affecting _fear_ effect.

**Malevolence (Su)** Once per day, a gidim on the Material Plane can merge its body with another creature’s. This ability is similar to a _[[spells/Magic Jar|magic jar]]_ spell (CL 10th or the devil’s HD, whichever is higher), except that it does not require a receptacle. To use this ability, the devil must be adjacent to the target. The target can resist the attack with a successful DC 16 Will save. A creature that successfully saves is immune to that same devil’s malevolence for 24 hours. While using this ability, the gidim is not affected by its otherworldly ability. The save DC is Charisma-based.

**Nourished by Negativity (Su)** Gidims seek out volatile mortals to aid them in entering the Material Plane. At the most basic level, negative emotions occur when a creature is _[[conditions/Dying|dying]]_, raging, or subject to a _fear_ effect. At the GM’s discretion, negative emotions might also include non-rules-related effects, such as extreme feelings of anger, betrayal, frustration, hate, or sorrow. Anytime a gidim witnesses a creature affected by negative emotions, it may choose to gain a +1 bonus on its next Will save made to enter the Material Plane, so long as it attempts to enter the plane within 30 feet of that creature and within 24 hours. If within 12 to 24 hours of gaining this bonus the gidim _[[spells/Witness|witness]]_ the same creature again being affected by negative emotions, it gains an additional +1 bonus on its Will save which stacks with the original and increases the duration of the bonus by an additional 24 hours. Thus, a gidim may gain a stacking +1 bonus to its Will save in this manner once every 12 hours. The devil loses its entire accumulated bonus if it attempts and fails to enter the Material Plane, if 24 hours pass without it witnessing its target creature being affected by negative emotions, or if it takes a bonus from another creature affected by negative emotions. Once on the Material Plane, this bonus applies to a gidim’s Will saves made to resist being expelled from the plane. The bonus decreases by 1 every minute until it reaches 0. A gidim that leaves the Material Plane before this bonus reaches 0 retains any remaining bonus.

**Otherworldly (Ex)** Gidims find it difficult to enter the Material Plane. To do so by any means, a lesser _possession_ devil must make a DC 30 Will save, failure meaning it is barred from entry and cannot access the plane again for 12 hours. In addition, after every minute of being on the Material Plane, the devil must make a DC 30 Will save or be expelled, returning to the plane it traveled from. Additionally, as a free action a number of times per day equal to the gidim’s Charisma modifier, the devil can empower one of its _spell-like abilities_ to extend out from the Ethereal Plane and affect a target on the Material Plane.
**Sunlight Weakness (Ex)** Gidims’ powers are weakened in natural sunlight (not merely a _[[spells/Daylight|daylight]]_ spell), reducing the DCs of their special abilities by –4. In addition, gidims attempting to enter the Material Plane into an area of sunlight take a –4 penalty on their Will save.

##### Description

Diabolically clever and immortally creative, the legions of Hell use all the tools at their disposal to _[[feats/Undermine|undermine]]_ and corrupt the souls of mortalkind. Among these tools are the souls of unabashedly depraved and hateful mortals sentenced to Hell in punishment for lives of sin. The foulest of these souls occasionally find themselves plucked from their torments and reforged in infernal crucibles, etched with bindings of hellish magic, then set loose upon the living. These evil souls bear many of the powers of devils, but fall outside the normal infernal hierarchies, not being considered true devils by their fiendish peers. Rather, they are gidims, Hell-bound souls made weapons of the Pit.

More than mere souls yet less than fiends, gidims find themselves barred from the mortal plane by the laws of existence. Their minds and memories linger on half-forgotten lives, however, and upon emotions and sensations long lost to fiends. Thus, they endlessly seek ways to infiltrate the paths of the living. Traveling to the Ethereal Plane, they peer into the Material Plane, seeking out hapless mortals and drawing power from their hatred, their violence, their sorrow, and especially their fears. Continued feeding upon and encouragement of such emotions grants them greater ability to invade the mortal realm and potentially steal new bodies, through which their foulness might live again.

Two breeds of gidim exist, lesser _possession_ devils and greater. Both appear nearly identical, but greater _possession_ devils are created from spirits of extraordinary, near-legendary evil beings. These foulest of souls are granted even more powerful diabolical abilities and are often loosed by their infernal masters to torment, unhinge, and ultimately destroy the mortal enemies of Hell. Lesser _possession_ devils are typically left to their own devices, using their abilities to sow _fear_, torment innocents, spread mistrust, and ruin lives.
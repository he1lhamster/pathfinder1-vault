---
cssclass: [monsters]
title1: Devil, Possession Devil, Lesser (Gidim)
desc_short: An impression of unmistakable malice pervades the area, the vague yet
  undeniable sensation of looming malevolence and faint foul breath.
title2: Possession Devil, Lesser (Gidim)
CR: 6
sources:
- name: 'Pathfinder #29: Mother of Flies'
  page: 82
  link: http://paizo.com/pathfinder/adventurePath/councilOfThieves/v5748btpy8bc1
XP: 2400
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
  bonus: 3
senses:
  darkvision: 60
  see in darkness: true
AC:
  AC: 17
  touch: 17
  flat_footed: 13
  components:
    deflection: 3
    dex: 3
    dodge: 1
HP:
  HP: 59
  long: 7d10+21
saves:
  fort: 8
  ref: 10
  will: 7
defensive_abilities:
- incorporeal
DR:
- amount: 5
  weakness: good
resistances:
  acid: 10
  cold: 10
SR: 17
weaknesses:
- sunlight weakness
speeds:
  base: 30
  fly: 30
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 claws +10 touch (1d4+3)
      entries:
      - - damage: 1d4+3
      count: 2
      attack: claws
      bonus:
      - 10
      touch: true
    - text: bite +10 touch (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: bite
      bonus:
      - 10
      touch: true
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
    DC: 13
  - name: ghost sound
    source: default
    freq: At will
    DC: 13
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: knock
    source: default
    freq: At will
    DC: 15
  - name: levitate
    source: default
    freq: At will
    DC: 15
  - name: open/close
    source: default
    freq: At will
    DC: 13
  - name: prestidigitation
    source: default
    freq: At will
    DC: 13
  - name: mage hand
    source: default
    freq: At will
    DC: 13
  - name: animate rope
    source: default
    freq: 3/day
    DC: 14
  - name: dancing lights
    source: default
    freq: 3/day
    DC: 13
  - name: ethereal jaunt
    source: default
    freq: 3/day
    other: Ethereal Plane to Material Plane and vice versa
  - name: minor creation
    source: default
    freq: 3/day
  - name: plane shift
    source: default
    freq: 3/day
    paren_text: self only; to Ethereal Plane, Hell, or Material Plane only
  - name: produce flame
    source: default
    freq: 3/day
    DC: 14
  - name: silent image
    source: default
    freq: 3/day
    DC: 14
  - name: suggestion
    source: default
    freq: 3/day
    DC: 16
  - name: unseen servant
    source: default
    freq: 3/day
    DC: 14
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: lesser possession devil
      amount: 1
      chance: 40%
  sources:
  - name: default
    CL: 12
ability_scores:
  STR:
  DEX: 16
  CON: 16
  INT: 15
  WIS: 17
  CHA: 17
BAB: 7
CMB: 10
CMD: 24
feats:
- name: Alertness
- name: Dodge
- name: Iron Will
- name: Lightning Reflexes
skills:
  Acrobatics: 13
  Bluff: 13
  Disable Device: 13
  Fly: 11
  Intimidate: 13
  Knowledge (planes): 12
  Perception: 15
  Sense Motive: 15
  Stealth: 13
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

# Devil, Possession Devil, Lesser (Gidim)
An impression of unmistakable malice pervades the area, the vague yet undeniable sensation of looming malevolence and faint foul breath.
**Source** Pathfinder #29: Mother of Flies pg. 82
**XP** 2,400

LE Medium outsider (devil, evil, extraplanar, _[[universal monster rules/Incorporeal|incorporeal]]_, lawful)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +15

##### Defense

**AC** 17, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+3 _[[spells/Deflection|deflection]]_, +3 Dex, +1 _[[feats/Dodge|dodge]]_)
**hp** 59 (7d10+21)
**Fort** +8, **Ref** +10, **Will** +7
**Defensive Abilities** _incorporeal_; **DR** 5/good; **Resist** acid 10, cold 10; **SR** 17
**Weaknesses** sunlight weakness

##### Offense
**Speed** 30 ft., fly 30 ft. (perfect)
**Melee** 2 claws +10 touch (1d4+3), bite +10 touch (1d6+3)
**Special Attacks** dread, malevolence
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th)
Constant — greater _[[spells/Invisibility|invisibility]]_
At will — _[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Ghost Sound|ghost sound]]_* (DC 13), greater teleport (self plus 50 lbs. of objects only), _[[spells/Knock|knock]]_* (DC 15), _[[spells/Levitate|levitate]]_* (DC 15), open/close* (DC 13), _[[spells/Prestidigitation|prestidigitation]]_* (DC 13), _[[spells/Mage Hand|mage hand]]_* (DC 13)
3/day — _[[spells/Animate Rope|animate rope]]_* (DC 14), _[[spells/Dancing Lights|dancing lights]]_* (DC 13), _[[spells/Ethereal Jaunt|ethereal jaunt]]_ (Ethereal Plane to Material Plane and vice versa), _[[spells/Minor Creation|minor creation]]_, _[[spells/Plane Shift|plane shift]]_ (self only; to Ethereal Plane, Hell, or Material Plane only), _[[spells/Produce Flame|produce flame]]_* (DC 14), _[[spells/Silent Image|silent image]]_* (DC 14), _[[spells/Suggestion|suggestion]]_ (DC 16), _[[spells/Unseen Servant|unseen servant]]_* (DC 14)
1/day — _[[universal monster rules/Summon|summon]]_ (level 4, 1 lesser _[[spells/Possession|possession]]_ devil, 40%)
* causes dread

##### Statistics
**Str** —, **Dex** 16, **Con** 16, **Int** 15, **Wis** 17, **Cha** 17
**Base Atk** +7; **CMB** +10; **CMD** 24
**Feats** _[[feats/Alertness|Alertness]]_, _Dodge_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Acrobatics +13, Bluff +13, Disable Device +13, Fly +11, Intimidate +13, Knowledge (planes) +12, Perception +15, Sense Motive +15, Stealth +13
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
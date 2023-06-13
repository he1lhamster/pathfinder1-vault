---
cssclass: [monsters]
title1: Watcher
desc_short: This enormous black insectile creature moves with an almost nauseating
  grace as it watches with its single red eye.
title2: Watcher
CR: 22
sources:
- name: Planar Adventures
  page: 246
  link: http://paizo.com/products/btpya1am
XP: 614400
alignment: LN
size: Gargantuan
type: outsider
initiative:
  bonus: 12
senses:
  blindsight: 120
  see in darkness: true
  true seeing: true
AC:
  AC: 41
  touch: 26
  flat_footed: 32
  components:
    dex: 8
    dodge: 1
    wis: 11
    natural: 15
    size: -4
HP:
  HP: 429
  long: 26d10+286
  regeneration: 15
  regeneration_weakness: chaotic spells and effects
saves:
  fort: 19
  ref: 23
  will: 27
defensive_abilities:
- evasion
- freedom of movement
DR:
- amount: 15
  weakness: chaotic
immunities:
- blindness
- daze
- divination effects
- force effects
- mind-affecting effects
SR: 33
speeds:
  base: 60
  other_semicolon: air walk
attacks:
  melee:
  - - text: 6 talons +32 (2d8+10/19-20 plus stasis)
      entries:
      - - damage: 2d8+10
          crit_range: 19-20
        - effect: stasis
      count: 6
      attack: talons
      bonus:
      - 32
space: 20
reach: 30
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: control weather
    source: default
    freq: At will
  - name: plane shift
    source: default
    freq: At will
    DC: 22
  - name: telekinesis
    source: default
    freq: At will
    DC: 20
  - name: call lightning storm
    source: default
    freq: 3/day
    DC: 21
  - name: earthquake
    source: default
    freq: 3/day
    DC: 22
  - name: quickened teleport
    source: default
    freq: 3/day
  - name: sirocco
    source: default
    freq: 3/day
    DC: 21
  - name: vortex
    source: default
    freq: 3/day
    DC: 22
  - name: whirlwind
    source: default
    freq: 3/day
    DC: 23
  - name: meteor swarm
    source: default
    freq: 1/day
    DC: 24
  - name: storm of vengeance
    source: default
    freq: 1/day
    DC: 24
  - name: time stop
    source: default
    freq: 1/day
  - name: tsunami
    source: default
    freq: 1/day
    DC: 24
  sources:
  - name: default
    CL: 20
    concentration: 25
ability_scores:
  STR: 30
  DEX: 27
  CON: 32
  INT: 29
  WIS: 34
  CHA: 21
BAB: 26
CMB: 40
CMD: 70
CMD_other: can't be tripped
feats:
- name: Alertness
- name: Combat Expertise
- name: Combat Reflexes
- name: Critical Focus
- name: Dodge
- name: Improved Critical (talons)
- name: Improved Initiative
- name: Mobility
- name: Quicken Spell-Like Ability (teleport)
- name: Skill Focus (Perception)
- name: Spring Attack
- name: Staggering Critical
- name: Whirlwind Attack
skills:
  Acrobatics: 37
  Craft (any one): 38
  Knowledge (arcana): 35
  Knowledge (dungeoneering): 35
  Knowledge (engineering): 35
  Knowledge (geography): 35
  Knowledge (history): 35
  Knowledge (planes): 38
  Knowledge (religion): 35
  Perception: 51
  Sense Motive: 45
  Spellcraft: 38
  Stealth: 25
  Survival: 41
  Use Magic Device: 34
languages:
- telepathy 200 ft.
- truespeech
special_qualities:
- beacon of Jandelay
- inconspicuous
- perfect observation
- phase shift
ecology:
  environment: any (Jandelay)
  organization: solitary or council (2-5)
  treasure_type: standard
special_abilities:
  Beacon of Jandelay (Su): Watchers can plant a beacon of Jandelay-a six-foot-tall
    glowing spire of pale yellow force energy-by spending 1 minute of uninterrupted
    activity. When planted on a world shortly to experience an apocalypse, these beacons
    designate the surrounding environs as important and guarantee that the area around
    the beacon will be incorporated into Jandelay upon the world's destruction. Beacons
    of Jandelay function properly even when constructed out of phase (see phase shift
    below), so watchers typically place them in such a manner to prevent denizens
    of the doomed world from removing or otherwise tampering with them. A beacon of
    Jandelay has hardness 30 and 440 hit points. A watcher immediately senses if a
    beacon of Jandelay it created takes damage, and when a watcher plane shifts or
    teleports to a site that contains a beacon of Jandelay, it always arrives on target.
  Inconspicuous (Su): Despite their enormous size, watchers have an unnerving ability
    to fade into the background, causing other creatures to overlook or ignore them.
    When a creature would first perceive a watcher (see it, hear its movements, or
    notice it with any other sense, be it natural or supernatural), it must succeed
    at a DC 28 Will save or it simply doesn't perceive the watcher for 24 hours, treating
    it as if it were invisible and silenced from the observer's perspective. On a
    successful save, the creature perceives the watcher and is immune to that watcher's
    inconspicuous ability for 24 hours. If the watcher attacks a creature that failed
    its save, it breaks the inconspicuous effect for that creature automatically for
    24 hours. The Oliphaunt of Jandelay automatically fails its save against the inconspicuous
    ability, allowing the watchers to share their home with the beast while staying
    beneath its notice. This is a mind-affecting effect that automatically bypasses
    the Oliphaunt of Jandelay's ward against command ability. The save DC is Charisma-based.
  Perfect Observation (Su): Watchers see and remember every sensation around them
    with perfect clarity, and their memory never fades. They are always assumed to
    have rolled a 20 on vision-based Perception checks (resulting in a 71 for a typical
    watcher). Further, they gain a bonus to their AC equal to their Wisdom modifier
    as a result of this supernatural ability to perceive threats and danger.
  Phase Shift (Su): Once per day, a watcher can shift itself out of phase with reality
    as a standard action; shifting back into phase is a free action. When out of phase
    with reality, a watcher can't be affected by effects from the plane it is watching,
    but it also can't affect that plane with its abilities (except for with beacon
    of Jandelay). However, the watcher can still observe the plane, and denizens of
    the plane can observe it if they overcome the watcher's inconspicuous ability.
    Watchers often use phase shift to observe events leading up to an apocalypse without
    succumbing to the cataclysm destined to destroy the world in question. Dimensional
    anchor or similar effects that bar dimensional travel not only prevent a watcher
    from using phase shift but can also force a watcher back into reality if they
    successfully target and affect a phase-shifted watcher. A watcher forced into
    reality against its will in this manner becomes staggered for 1d3 rounds.
  Stasis (Su): A creature damaged by a watcher's talon must succeed at a DC 28 Will
    save or be slowed for 1 round, as per slow. A slowed creature (be it a creature
    affected by the spell of the same name, by a watcher's talon, or by another slow-inducing
    effect) that takes damage from a watcher's talon must succeed at a DC 28 Fortitude
    save or become permanently trapped in a state of stasis, as per temporal stasis.
    This effect ends if the watcher who created the effect is slain or is no longer
    on the same plane as the victim. The save DC is Charisma-based.
desc_long: |-
  The watchers of Jandelay are bizarre and enigmatic creatures, inscrutable to most mortals, particularly since Jandelay itself is so unknown. Watchers lurk in worlds on the brink of destruction in order to observe events as they unfold and to catalogue and prepare a piece of the worlds for eternal enshrinement in Jandelay. Watchers mostly perform this work unseen, regularly setting beacons and, rarely, putting objects or beings into stasis in order to bring them along to Jandelay. Watchers have no desire to accelerate apocalypses before their appointed times, but they are drawn to action when would-be heroes or saviors take extreme measures to prevent a calamity.

  On Jandelay, watchers move from region to region, building alabaster spires and creating other objects and edifices upon the interstitial fields, depending on their favored crafts. Left alone, a watcher might spend centuries crafting a single object, only to lose interest in its work immediately after completing the task.

  When faced with a particular threat or curiosity, watchers naturally organize into councils of up to five individuals. When such a council forms, one watcher is selected as an observer, and this watcher is bolstered by the presence of the others. Councils often take quite a while to come to a decision as to how to proceed, but once they do, they pursue their task with an eerie single-mindedness and efficiency that has led some observers to incorrectly infer that the speechless watchers were operating as a hive mind-in truth, they are simply obsessed with perfection and elegance of action.

  Prehensile filaments nestled amid the sharp talons at the tip of each leg allow watchers to perform precision motions as necessary. A watcher's peculiar brand of air walk keeps its main body upright even if all of its legs are occupied, allowing it to attack with all six legs and protecting it from attempts to trip it.

  Watchers stand 30 feet tall atop their insectile legs, and weigh 6 tons.

---

# Watcher
This enormous black insectile creature moves with an almost nauseating _[[spells/Grace|grace]]_ as it watches with its single red eye.
**Source** _[[items/Weapon Magic Abilities/Planar|Planar]]_ Adventures pg. 246
**XP** 614,400

LN Gargantuan outsider
**Init** +12; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 120 ft., _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/True Seeing|true seeing]]_; Perception +51

##### Defense

**AC** 41, touch 26, _[[conditions/Flat-Footed|flat-footed]]_ 32 (+8 Dex, +1 dodge, +11 Wis, +15 natural, –4 size)
**hp** 429 (26d10+286); _[[universal monster rules/Regeneration|regeneration]]_ 15 (chaotic spells and effects)
**Fort** +19, **Ref** +23, **Will** +27
**Defensive Abilities** evasion, _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 15/chaotic; **Immune** blindness, _[[spells/Daze|daze]]_, _[[spells/Divination|divination]]_ effects, force effects, mind-affecting effects; **SR** 33

##### Offense
**Speed** 60 ft.; _[[spells/Air Walk|air walk]]_
**Melee** 6 talons +32 (2d8+10/19–20 plus stasis)
**Space** 20 ft., **Reach** 30 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +25)
Constant—_air walk_, _freedom of movement_, _true seeing_
At will—_[[spells/Control Weather|control weather]]_, _[[spells/Plane Shift|plane shift]]_ (DC 22), _[[spells/Telekinesis|telekinesis]]_ (DC 20)
3/day—_[[spells/Call Lightning Storm|call lightning storm]]_ (DC 21), _[[spells/Earthquake|earthquake]]_ (DC 22), quickened teleport, _[[spells/Sirocco|sirocco]]_ (DC 21), _[[spells/Vortex|vortex]]_ (DC 22), _[[universal monster rules/Whirlwind|whirlwind]]_ (DC 23)
1/day—_[[spells/Meteor Swarm|meteor swarm]]_ (DC 24), _[[spells/Storm Of Vengeance|storm of vengeance]]_ (DC 24), _[[spells/Time Stop|time stop]]_, _[[spells/Tsunami|tsunami]]_ (DC 24)

##### Statistics
**Str** 30, **Dex** 27, **Con** 32, **Int** 29, **Wis** 34, **Cha** 21
**Base Atk** +26; **CMB** +40; **CMD** 70 (can’t be tripped)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (talons), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (teleport), _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Whirlwind Attack|Whirlwind Attack]]_
**Skills** Acrobatics +37, Craft (any one) +38, Knowledge (arcana) +35, Knowledge (dungeoneering) +35, Knowledge (engineering) +35, Knowledge (geography) +35, Knowledge (history) +35, Knowledge (planes) +38, Knowledge (religion) +35, Perception +51, Sense Motive +45, Spellcraft +38, Stealth +25, Survival +41, Use Magic Device +34
**Languages** _[[universal monster rules/Telepathy|telepathy]]_ 200 ft.; truespeech
**SQ** beacon of Jandelay, inconspicuous, perfect observation, phase shift

##### Ecology

**Environment** any (Jandelay)
**Organization** solitary or council (2–5)
**Treasure** standard

### Special Abilities

**Beacon of Jandelay (Su)** Watchers can plant a beacon of Jandelay—a six-foot-tall glowing spire of pale yellow force energy—by spending 1 minute of uninterrupted activity. When planted on a world shortly to experience an apocalypse, these beacons designate the surrounding environs as important and guarantee that the area around the beacon will be incorporated into Jandelay upon the world’s _[[spells/Destruction|destruction]]_. Beacons of Jandelay function properly even when constructed out of phase (see phase shift below), so watchers typically place them in such a manner to prevent denizens of the doomed world from removing or otherwise tampering with them. A beacon of Jandelay has hardness 30 and 440 hit points. A _[[monsters/Watcher|watcher]]_ immediately senses if a beacon of Jandelay it created takes damage, and when a _watcher_ plane shifts or teleports to a site that contains a beacon of Jandelay, it always arrives on target.

**Inconspicuous (Su)** Despite their enormous size, watchers have an unnerving ability to fade into the background, causing other creatures to _[[spells/Overlook|overlook]]_ or ignore them. When a creature would first perceive a _watcher_ (see it, hear its movements, or notice it with any other sense, be it natural or supernatural), it must succeed at a DC 28 Will save or it simply doesn’t perceive the _watcher_ for 24 hours, treating it as if it were _[[conditions/Invisible|invisible]]_ and silenced from the observer’s perspective. On a successful save, the creature perceives the _watcher_ and is immune to that _watcher_’s inconspicuous ability for 24 hours. If the _watcher_ attacks a creature that failed its save, it breaks the inconspicuous effect for that creature automatically for 24 hours. The _[[monsters/Oliphaunt of Jandelay|Oliphaunt of Jandelay]]_ automatically fails its save against the inconspicuous ability, allowing the watchers to share their home with the beast while staying beneath its notice. This is a mind-affecting effect that automatically bypasses the _Oliphaunt of Jandelay_’s ward against _[[spells/Command|command]]_ ability. The save DC is Charisma-based.

**Perfect Observation (Su)** Watchers see and remember every sensation around them with perfect _[[items/Weapon/Clarity|clarity]]_, and their memory never fades. They are always assumed to have rolled a 20 on vision-based Perception checks (resulting in a 71 for a typical _watcher_). Further, they gain a bonus to their AC equal to their Wisdom modifier as a result of this supernatural ability to perceive threats and danger.

**Phase Shift (Su)** Once per day, a _watcher_ can shift itself out of phase with reality as a standard action; shifting back into phase is a free action. When out of phase with reality, a _watcher_ can’t be affected by effects from the plane it is watching, but it also can’t affect that plane with its abilities (except for with beacon of Jandelay). However, the _watcher_ can still observe the plane, and denizens of the plane can observe it if they overcome the _watcher_’s inconspicuous ability. Watchers often use phase shift to observe events leading up to an apocalypse without succumbing to the cataclysm destined to destroy the world in question. _[[spells/Dimensional Anchor|Dimensional anchor]]_ or similar effects that bar dimensional travel not only prevent a _watcher_ from using phase shift but can also force a _watcher_ back into reality if they successfully target and affect a phase-shifted _watcher_. A _watcher_ forced into reality against its will in this manner becomes _[[conditions/Staggered|staggered]]_ for 1d3 rounds.
**Stasis (Su)** A creature damaged by a _watcher_’s talon must succeed at a DC 28 Will save or be slowed for 1 round, as per _[[spells/Slow|slow]]_. A slowed creature (be it a creature affected by the spell of the same name, by a _watcher_’s talon, or by another slow-inducing effect) that takes damage from a _watcher_’s talon must succeed at a DC 28 Fortitude save or become permanently trapped in a state of stasis, as per _[[spells/Temporal Stasis|temporal stasis]]_. This effect ends if the _watcher_ who created the effect is slain or is no longer on the same plane as the victim. The save DC is Charisma-based.

##### Description

The watchers of Jandelay are bizarre and enigmatic creatures, inscrutable to most mortals, particularly since Jandelay itself is so _[[monsters/Unknown|unknown]]_. Watchers lurk in worlds on the brink of _destruction_ in order to observe events as they unfold and to catalogue and prepare a piece of the worlds for eternal enshrinement in Jandelay. Watchers mostly perform this work _[[items/Weapon Magic Abilities/Unseen|unseen]]_, regularly setting beacons and, rarely, putting objects or beings into stasis in order to bring them along to Jandelay. Watchers have no desire to accelerate apocalypses before their appointed times, but they are drawn to action when would-be heroes or saviors take extreme measures to prevent a calamity.

On Jandelay, watchers move from region to region, building alabaster spires and creating other objects and edifices upon the interstitial fields, depending on their favored crafts. Left alone, a _watcher_ might spend centuries crafting a single object, only to lose interest in its work immediately after completing the task.

When faced with a particular threat or curiosity, watchers naturally organize into councils of up to five individuals. When such a council forms, one _watcher_ is selected as an observer, and this _watcher_ is bolstered by the presence of the others. Councils often take quite a while to come to a decision as to how to proceed, but once they do, they pursue their task with an eerie single-mindedness and efficiency that has led some observers to incorrectly infer that the speechless watchers were operating as a hive mind—in truth, they are simply obsessed with perfection and elegance of action.

_[[items/Weapon Magic Abilities/Prehensile|Prehensile]]_ filaments nestled amid the sharp talons at the tip of each leg allow watchers to perform precision motions as necessary. A _watcher_’s peculiar _[[spells/Brand|brand]]_ of _air walk_ keeps its main body upright even if all of its legs are occupied, allowing it to attack with all six legs and protecting it from attempts to _[[universal monster rules/Trip|trip]]_ it.

Watchers stand 30 feet tall atop their insectile legs, and weigh 6 tons.
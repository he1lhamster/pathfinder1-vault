---
cssclass: [monsters]
title1: Great Old One, Bokrug
desc_short: This great reptilian monster is an aquatic lizard with a beard of tentacles
  and a sting-tipped tail.
title2: Bokrug
CR: 27
sources:
- name: Bestiary 4
  page: 136
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 3276800
alignment: CN
size: Large
type: magical beast
subtypes:
- aquatic
- chaotic
- extraplanar
- Great Old One
initiative:
  bonus: 22
senses:
  blindsight: 120
  darkvision: 60
  low-light vision: true
auras:
- name: toxic breath
  radius: 30
  DC: 41
- name: unspeakable presence
  radius: 300
  DC: 33
AC:
  AC: 45
  touch: 27
  flat_footed: 37
  components:
    dex: 8
    insight: 10
    natural: 18
    size: -1
HP:
  HP: 645
  long: 30d10+480
  fast_healing: 20
saves:
  fort: 33
  ref: 25
  will: 22
defensive_abilities:
- immortality
- insanity (DC 41)
- spines
DR:
- amount: 15
  weakness: epic and lawful
immunities:
- ability damage
- ability drain
- aging
- cold
- death effects
- disease
- energy drain
- mind-affecting effects
- paralysis
- petrification
- poison
resistances:
  acid: 30
  fire: 30
SR: 38
speeds:
  base: 50
  swim: 120
  other:
  - air walk
attacks:
  melee:
  - - text: bite +44 (4d8+22/19-20)
      entries:
      - - damage: 4d8+22
          crit_range: 19-20
      attack: bite
      bonus:
      - 44
    - text: 2 claws +44 (2d8+22/19-20)
      entries:
      - - damage: 2d8+22
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 44
    - text: sting +44 (3d6+22/19-20 plus poison)
      entries:
      - - damage: 3d6+22
          crit_range: 19-20
        - effect: poison
      attack: sting
      bonus:
      - 44
    - text: tentacle beard +39 (4d6+22 plus grab)
      entries:
      - - damage: 4d6+22
        - effect: grab
      attack: tentacle beard
      bonus:
      - 39
  special:
  - constrict (4d6+22)
  - critical poisoning
  - mythic power (10/day, surge +1d12)
  - poison
  - powerful blows (bite, claws, sting, tentacle beard)
  - vengeful dreams
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - is_mythic_spell: true
    name: cloudkill
    source: default
    freq: At will
    DC: 23
  - is_mythic_spell: true
    name: dimension door
    source: default
    freq: At will
  - is_mythic_spell: true
    name: dream
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: hallucinatory terrain
    source: default
    freq: At will
  - is_mythic_spell: true
    name: nightmare
    source: default
    freq: At will
    DC: 23
  - is_mythic_spell: true
    name: plane shift
    source: default
    freq: At will
  - name: transmute rock to mud
    source: default
    freq: At will
  - name: wind walk
    source: default
    freq: At will
  - name: demand
    source: default
    freq: 3/day
  - name: quickened feeblemind
    source: default
    freq: 3/day
    DC: 23
  - name: horrid wilting
    source: default
    freq: 3/day
    DC: 26
  - is_mythic_spell: true
    name: control weather
    source: default
    freq: 1/day
  - name: symbol of insanity
    source: default
    freq: 1/day
    DC: 26
  - is_mythic_spell: true
    superscripts:
    - APG
    name: tsunami
    source: default
    freq: 1/day
    DC: 26
  sources:
  - name: default
    CL: 27
    concentration: 35
ability_scores:
  STR: 40
  DEX: 27
  CON: 42
  INT: 22
  WIS: 30
  CHA: 27
BAB: 30
CMB: 46
CMB_other: +50 bull rush, grapple, or overrun
CMD: 74
CMD_other: 76 vs. bull rush or overrun, 78 vs. trip
feats:
- name: Bleeding Critical
- name: Combat Reflexes
- name: Critical Focus
- name: Greater Bull Rush
- name: Greater Overrun
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Improved Critical (claw)
- name: Improved Critical (sting)
- name: Improved Initiative
- name: Improved Iron Will
- name: Improved Overrun
- name: Iron Will
- name: Power Attack
- name: Quicken Spell- Like Ability (feeblemind)
skills:
  Knowledge (arcana): 36
  Knowledge (history): 36
  Knowledge (nature): 36
  Knowledge (religion): 36
  Perception: 43
  Spellcraft: 36
  Stealth: 37
  Swim: 56
languages:
- Aklo
- Aquan
- Draconic
- telepathy 100 ft.
special_qualities:
- amphibious
- otherworldly insight
ecology:
  environment: any water
  organization: solitary (unique)
  treasure_type: triple
special_abilities:
  Critical Poisoning (Su): If Bokrug confirms a critical hit with his sting, he injects
    his foe with 3 doses of poison (this increases the save DC by 4). A foe that is
    normally immune to poison can be affected by Bokrug's poison in this way, but
    treats the poisoning as if it had been injected with only 1 dose.
  Immortality (Ex): |-
    If Bokrug is killed, his body immediately begins to thrash and writhe spasmodically, continuing to do so for 1d4 rounds. During this time, he makes a single sting attack against one random target in reach. At the end of this time, his body grows still, then melts into water and evaporates away. Bokrug reforms in dormancy back in his realm in the Dimension of Dreams soon thereafter, remaining in a comatose state for hundreds of years unless he is awoken earlier via complex rituals.

    Any effect that destroys Bokrug's body (such as disintegrate) merely reduces his remains to water that then evaporates away as described above, but such measures do prevent his body from thrashing and stinging prior to this supernatural evaporation.
  Poison (Ex): Sting-injury; save Fort DC 41; frequency 1/round for 6 rounds; effect
    2d4 Wisdom damage; cure 3 consecutive saves. A creature whose Wisdom damage equals
    its Wisdom score automatically becomes afflicted by a random insanity (Pathfinder
    RPG GameMastery Guide 250). The save DC is Constitution-based.
  Spines (Ex): Any creature that makes a melee attack against Bokrug must succeed
    at a DC 33 Reflex save or be struck by the numerous swiftly reacting spines that
    cover the Great Old One, taking 2d6+15 points of damage. Using a reach weapon
    does not endanger the attacker in this way. The save DC is Dexterity-based.
  Toxic Breath (Su): Bokrug's breath is toxic. Whenever the Great Old One is above
    water, he is surrounded by a 30-foot-radius cloud of invisible poison gas that
    causes temporary madness and hallucinations. Any creature that begins its turn
    in this area must succeed at a DC 41 Will save or be confused for 1 round. A creature
    that holds its breath or doesn't have to breathe gains a +4 bonus on this saving
    throw. This is a mind-affecting poison effect. The save DC is Constitution-based.
  Unspeakable Presence (Su): Failing a DC 33 Will save against Bokrug's unspeakable
    presence causes the victim to become overwhelmed with hopelessness and doom-it
    takes a -4 penalty on all attack rolls, saving throws, ability checks, skill checks,
    and weapon damage rolls as long as it remains within the area of affect. The save
    DC is Charisma-based.
  Vengeful Dreams (Su): Any creature that has ever damaged Bokrug or has slain one
    of his clerics can be targeted by the Great Old One's vengeful dreams regardless
    of the distance between the creature and Bokrug, even across planar boundaries.
    In order to use vengeful dreams against a target, Bokrug must successfully affect
    the target with his nightmare spell-like ability; the target is always treated
    as familiar to Bokrug, and as if Bokrug possessed a body part of the victim, resulting
    in a -15 penalty on the saving throw against the nightmare. If the victim fails
    its save against the nightmare, the horrific dream unfolds as a vision of Bokrug
    consuming the victim alive. The victim then remains alive, conscious, and aware
    as the Great Old One digests it, and as Bokrug destroys all that remains of the
    victim's lifelong friends, home, belongings, and family. When the victim awakens
    from the nightmare, it must succeed at a DC 33 Will save or take 3d6 points of
    Wisdom drain from the vengeful dreams. If this drains the target's Wisdom to 0,
    it automatically gains a random insanity (GameMastery Guide 250). Once Bokrug
    uses this ability against a creature, he can't do so again until that creature
    again damages him or slays one of his clerics. This is a mind-affecting effect.
    The save DC is Charisma-based.
desc_long: |-
  Bokrug, the Water Lizard, dwells in a distant and forsaken corner of the Dimension of Dreams, in a land that was once heavily populated but is now a desolate and barren realm surrounding a nameless lake-a realm once ruled by mighty human empires, but now ruled only by the hideous amphibian minions of the Water Lizard. Bokrug himself is a vast creature, a vaguely iguana-shaped monster with a beard of writhing tendrils and a long tail tipped with a stinger. The scales that cover his body hide long spines that Bokrug can extend or retract with near lightning speed.

  Bokrug spends the majority of his time slumbering far down in the depths of his submerged lair. No rivers feed the lake, nor does it drain into the sea. Yet the still, ominous waters are neither stale nor brackish, implying that they connect somewhere deep underground, and. By way of these dark, secret waterways, Bokgrug has access to the lakes and rivers of the Dimension of Dreams, and his ability to plane shift allows him access to other realms as he wills.

---

# Great Old One, Bokrug
This great reptilian monster is an aquatic lizard with a beard of tentacles and a sting-tipped tail.
**Source** Bestiary 4 pg. 136
**XP** 3,276,800

CN Large magical beast (aquatic, chaotic, extraplanar, Great Old One)
**Init** +22; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 120 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +43
**Aura** _[[items/Weapon Magic Abilities/Toxic|toxic]]_ breath (30 ft., DC 41), unspeakable presence (300 ft., DC 33)

##### Defense

**AC** 45, touch 27, _[[conditions/Flat-Footed|flat-footed]]_ 37 (+8 Dex, +10 insight, +18 natural, –1 size)
**hp** 645 (30d10+480); _[[universal monster rules/Fast Healing|fast healing]]_ 20
**Fort** +33, **Ref** +25, **Will** +22
**Defensive Abilities** immortality, _[[spells/Insanity|insanity]]_ (DC 41), spines; **DR** 15/epic and lawful; **Immune** ability damage, ability drain, aging, cold, death effects, disease, _[[universal monster rules/Energy Drain|energy drain]]_, mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, petrification, poison; **Resist** acid 30, fire 30; **SR** 38

##### Offense
**Speed** 50 ft., swim 120 ft., _[[spells/Air Walk|air walk]]_
**Melee** bite +44 (4d8+22/19–20), 2 claws +44 (2d8+22/19–20), sting +44 (3d6+22/19–20 plus poison), tentacle beard +39 (4d6+22 plus _[[universal monster rules/Grab|grab]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (4d6+22), critical _[[items/Armor Magic Abilities/Poisoning|poisoning]]_, mythic power (10/day, surge +1d12), poison, powerful blows (bite, claws, sting, tentacle beard), vengeful dreams
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 27th; concentration +35)
Constant—_air walk_
At will—_[[spells/Cloudkill|cloudkill]]_ (DC 23), _[[spells/Dimension Door|dimension door]]_, _[[spells/Dream|dream]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Hallucinatory Terrain|hallucinatory terrain]]_, _[[spells/Nightmare|nightmare]]_ (DC 23), _[[spells/Plane Shift|plane shift]]_, _[[spells/Transmute Rock to Mud|transmute rock to mud]]_, _[[spells/Wind Walk|wind walk]]_
3/day—_[[spells/Demand|demand]]_, quickened _[[spells/Feeblemind|feeblemind]]_ (DC 23), _[[spells/Horrid Wilting|horrid wilting]]_ (DC 26)
1/day—_[[spells/Control Weather|control weather]]_, _[[spells/Symbol of Insanity|symbol of insanity]]_ (DC 26), tsunamiAPG, M (DC 26)

##### Statistics
**Str** 40, **Dex** 27, **Con** 42, **Int** 22, **Wis** 30, **Cha** 27
**Base Atk** +30; **CMB** +46 (+50 bull rush, grapple, or overrun); **CMD** 74 (76 vs. bull rush or overrun, 78 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Bull Rush|Greater Bull Rush]]_, _[[feats/Greater Overrun|Greater Overrun]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _Improved Critical_ (claw), _Improved Critical_ (sting), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Overrun|Improved Overrun]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, Quicken Spell- Like Ability (_feeblemind_)
**Skills** Knowledge (arcana, history, nature, religion) +36, Perception +43, Spellcraft +36, Stealth +37, Swim +56
**Languages** Aklo, Aquan, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Amphibious|amphibious]]_, otherworldly insight

##### Ecology

**Environment** any water
**Organization** solitary (unique)
**Treasure** triple

### Special Abilities

**Critical _Poisoning_ (Su)** If Bokrug confirms a critical hit with his sting, he injects his foe with 3 doses of poison (this increases the save DC by 4). A foe that is normally immune to poison can be affected by Bokrug’s poison in this way, but treats the _poisoning_ as if it had been injected with only 1 dose.

**Immortality (Ex)** If Bokrug is killed, his body immediately begins to thrash and writhe spasmodically, continuing to do so for 1d4 rounds. During this time, he makes a single sting attack against one random target in reach. At the end of this time, his body grows still, then melts into water and evaporates away. Bokrug reforms in dormancy back in his realm in the Dimension of Dreams soon thereafter, remaining in a comatose state for hundreds of years unless he is awoken earlier via complex rituals.

Any effect that destroys Bokrug’s body (such as _[[spells/Disintegrate|disintegrate]]_) merely reduces his remains to water that then evaporates away as described above, but such measures do prevent his body from thrashing and stinging prior to this supernatural evaporation.

**Poison (Ex)** Sting—injury; save Fort DC 41; frequency 1/round for 6 rounds; effect 2d4 Wisdom damage; cure 3 consecutive saves. A creature whose Wisdom damage equals its Wisdom score automatically becomes afflicted by a random _insanity_ (Pathfinder RPG GameMastery Guide 250). The save DC is Constitution-based.
**Spines (Ex)** Any creature that makes a melee attack against Bokrug must succeed at a DC 33 Reflex save or be struck by the numerous swiftly reacting spines that cover the Great Old One, taking 2d6+15 points of damage. Using a reach weapon does not endanger the attacker in this way. The save DC is Dexterity-based.

**_Toxic_ Breath (Su)** Bokrug’s breath is _toxic_. Whenever the Great Old One is above water, he is surrounded by a 30-foot-radius cloud of _[[conditions/Invisible|invisible]]_ poison gas that causes temporary madness and hallucinations. Any creature that begins its turn in this area must succeed at a DC 41 Will save or be _[[conditions/Confused|confused]]_ for 1 round. A creature that holds its breath or doesn’t have to breathe gains a +4 bonus on this saving throw. This is a mind-affecting poison effect. The save DC is Constitution-based.

**Unspeakable Presence (Su)** Failing a DC 33 Will save against Bokrug’s unspeakable presence causes the victim to become overwhelmed with hopelessness and _[[spells/Doom|doom]]_—it takes a –4 penalty on all attack rolls, saving throws, ability checks, skill checks, and weapon damage rolls as long as it remains within the area of affect. The save DC is Charisma-based.

**Vengeful Dreams (Su)** Any creature that has ever damaged Bokrug or has slain one of his clerics can be targeted by the Great Old One’s vengeful dreams regardless of the distance between the creature and Bokrug, even across _[[items/Weapon Magic Abilities/Planar|planar]]_ boundaries. In order to use vengeful dreams against a target, Bokrug must successfully affect the target with his _nightmare_ spell-like ability; the target is always treated as familiar to Bokrug, and as if Bokrug possessed a body part of the victim, resulting in a –15 penalty on the saving throw against the _nightmare_. If the victim fails its save against the _nightmare_, the horrific _dream_ unfolds as a _[[spells/Vision|vision]]_ of Bokrug consuming the victim alive. The victim then remains alive, conscious, and aware as the Great Old One digests it, and as Bokrug destroys all that remains of the victim’s lifelong friends, home, belongings, and family. When the victim awakens from the _nightmare_, it must succeed at a DC 33 Will save or take 3d6 points of Wisdom drain from the vengeful dreams. If this drains the target’s Wisdom to 0, it automatically gains a random _insanity_ (GameMastery Guide 250). Once Bokrug uses this ability against a creature, he can’t do so again until that creature again damages him or slays one of his clerics. This is a mind-affecting effect. The save DC is Charisma-based.

##### Description

Bokrug, the Water Lizard, dwells in a distant and forsaken corner of the Dimension of Dreams, in a land that was once heavily populated but is now a desolate and barren realm surrounding a nameless lake—a realm once ruled by mighty human empires, but now ruled only by the hideous amphibian minions of the Water Lizard. Bokrug himself is a vast creature, a vaguely iguana-shaped monster with a beard of writhing tendrils and a long tail tipped with a stinger. _[[diseases/The Scales|The scales]]_ that cover his body hide long spines that Bokrug can extend or retract with near lightning speed.

Bokrug spends the majority of his time slumbering far down in the depths of his submerged lair. No rivers feed the lake, nor does it drain into the sea. Yet the still, _[[items/Weapon Magic Abilities/Ominous|ominous]]_ waters are neither stale nor brackish, implying that they connect somewhere deep underground, and. By way of these dark, secret waterways, Bokgrug has access to the lakes and rivers of the Dimension of Dreams, and his ability to _plane shift_ allows him access to other realms as he wills.
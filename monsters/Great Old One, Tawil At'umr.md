---
cssclass: [monsters]
title1: Great Old One, Tawil At'umr
desc_short: A gray robe and veil obscure this humanoid's form, save for afoaming mass
  of bubbles and tentacles extending from below.
title2: Tawil At'umr
CR: 30
sources:
- name: Bestiary 6
  page: 148
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 9830400
alignment: CN
size: Large
type: outsider
subtypes:
- chaotic
- extraplanar
- Great Old One
initiative:
  bonus: 27
senses:
  darkvision: 60
  see in darkness: true
  true seeing: true
auras:
- name: cloak of chaos
  DC: 30
- name: unspeakable presence
  radius: 300
  DC: 39
AC:
  AC: 49
  touch: 37
  flat_footed: 35
  components:
    deflection: 4
    dex: 13
    dodge,+10 insight: 1
    natural: 12
    size: -1
HP:
  HP: 752
  long: 35d10+560
  fast_healing: 30
saves:
  fort: 31
  ref: 36
  will: 34
defensive_abilities:
- amorphous
- dimensional fortification,freedom of movement
- immortality
- insanity (DC 39)
immunities:
- ability damage
- ability drain
- aging
- cold
- deatheffects
- disease
- energy drain
- mind-affecting effects,paralysis
- petrification
- sonic
resistances:
  acid: 30
  electricity: 30
  fire: 30
SR: 41
speeds:
  base: 60
  fly: 120
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 slams +51 (2d8+17 plus temporal displacement)
      entries:
      - - damage: 2d8+17
        - effect: temporal displacement
      count: 2
      attack: slams
      bonus:
      - 51
    - text: 4 tentacles +49 (6d6+8/19-20 plus grab)
      entries:
      - - damage: 6d6+8
          crit_range: 19-20
        - effect: grab
      count: 4
      attack: tentacles
      bonus:
      - 49
  special:
  - command the ancient ones
  - constrict (6d6+25),dimensional dreams
  - merge lives
  - mythic power (10/day,surge +1d12)
  - portal mastery
space: 10
reach: 10
reach_other: 30 ft. with tentacles
spell_like_abilities:
  entries:
  - name: cloak of chaos
    source: default
    freq: Constant
    DC: 30
  - name: freedom of movement
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: astral projection
    source: default
    freq: At will
  - is_mythic_spell: true
    name: dimensional lock
    source: default
    freq: At will
  - is_mythic_spell: true
    name: dream
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: interplanetary teleport
    source: default
    freq: At will
  - is_mythic_spell: true
    name: nightmare
    source: default
    freq: At will
  - is_mythic_spell: true
    name: plane shift
    source: default
    freq: At will
    DC: 29
  - is_mythic_spell: true
    name: sending
    source: default
    freq: At will
  - name: teleport object
    source: default
    freq: At will
    DC: 29
  - name: demand
    source: default
    freq: 3/day
    DC: 30
  - is_mythic_spell: true
    name: quickened disintegrate
    source: default
    freq: 3/day
    DC: 28
  - name: quickened feeblemind
    source: default
    freq: 3/day
    DC: 27
  - is_mythic_spell: true
    name: quickened mislead
    source: default
    freq: 3/day
    DC: 28
  - name: gate
    source: default
    freq: 1/day
  - name: microcosm
    source: default
    freq: 1/day
    DC: 31
  - name: summon
    source: default
    freq: 1/day
    level: 9
    summons:
    - name: ancient ones
      amount: 2
      chance: 100%
  - is_mythic_spell: true
    name: time stop
    source: default
    freq: 1/day
  - is_mythic_spell: true
    name: wish
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 30
    concentration: 42
ability_scores:
  STR: 44
  DEX: 36
  CON: 43
  INT: 35
  WIS: 32
  CHA: 35
BAB: 35
CMB: 53
CMD: 91
CMD_other: can't be tripped
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Critical Focus
- name: Dodge
- name: Flyby Attack
- name: Greater Disarm
- name: Greater Sunder
- name: Improved Critical (tentacle)
- name: Improved Disarm
- name: ImprovedInitiative
- name: Improved Sunder
- name: Mobility
- name: Multiattack
- name: PowerAttack
- name: Quicken Spell-Like Ability (disintegrate)
- name: Quicken Spell-Like Ability (feeblemind)
- name: Quicken Spell-Like Ability (mislead)
- name: Staggering Critical
skills:
  Acrobatics: 48
  Bluff: 50
  Diplomacy: 47
  Disguise: 47
  Fly: 57
  Intimidate: 47
  Knowledge (arcana,engineering): 47
  Knowledge (geography): 47
  Knowledge (history): 47
  Knowledge (nature): 47
  Knowledge (religion): 47
  Knowledge (planes): 50
  Perception: 49
  Sense Motive: 49
  Spellcraft: 47
  Stealth: 47
  Use Magic Device: 47
languages:
- Aklo
- telepathy 1 mile
- tongues
special_qualities:
- otherworldly insight
ecology:
  environment: any
  organization: solitary (unique)
  treasure_type: triple
special_abilities:
  Command the Ancient Ones (Su): Tawil at'Umr commands the obedience of a race of
    lesser immortals known as the ancient ones, creatures akin to itself but of inferior
    power. An ancient one is a hundun with the invincible mythic simple template that
    is native to the Material Plane. In addition to Tawil at'Umr being able to summon
    ancient ones to its side, any command spoken or telepathically sent from it to
    an ancient one (but not to a normal hundun) must be obeyed without question (and
    with no save).
  Dimensional Dreams (Su): When Tawil at'Umr uses its nightmare spell-like ability,
    it can target any creature it has affected with its spell-like or supernatural
    abilities, or any creature that has ever traveled via a gate spell, regardless
    of distance. In addition to the effects of nightmare, the target must succeed
    at a DC 39 Will save or die, only to be reincarnated a moment later into a new
    body on another world. This is a mind-affecting death effect. The save DC is Charisma-based.
  Dimensional Fortification (Ex): Tawil at'Umr cannot be forced to travel via teleportation
    effects unless it so chooses.
  Immortality (Ex): If Tawil at'Umr is killed, Yog-Sothoth can create a new avatar
    immediately. The replacement Tawil at'Umr typically does not reappear where it
    was killed, and it usually does not seek revenge against those who slew its predecessor.
    Usually.
  Merge Lives (Su): Once per day as a full-round action, Tawil at'Umr can cause a
    touched creature's mind (the target) to merge with any other creature (the host)
    that Tawil at'Umr has affected via dimensional dreams. The target can resist this
    effect with a successful DC 39 Will save. If the creature fails its save, its
    body vanishes (leaving behind any gear it may have carried) and its mind becomes
    trapped in the host creature's mind. The target can observe the world through
    the host creature but cannot control the host creature's actions. In time, or
    under certain conditions, the target can eventually take control of the host's
    actions, but these developments are rare and require hundreds of years to occur
    (usually, the host creature dies long before the target can exert such influence).
    To others, it is rarely apparent which body throughout the countless worlds Tawil
    at'Umr has seen was chosen as a host for the target's mind. This is a mindaffecting
    curse effect. The save DC is Charisma-based.
  Portal Mastery (Su): Tawil at'Umr senses when a creature is about to teleport into
    its vicinity (within range of its unspeakable presence), or when a portal is about
    to open in that same area. If it wishes, Tawil at'Umr can block the teleportation
    or portal effect from occurring as an immediate action. The creator of the effect
    must succeed at a caster level check against Tawil at'Umr's spell resistance or
    the effect is countered.
  Temporal Displacement (Su): A creature struck by one of Tawil at'Umr's slam attacks
    must succeed at a DC 39 Fortitude save or enter a state of suspended animation
    like that created by temporal stasis. This condition cannot be removed via dispel
    magic, nor does freedom of movement offer protection. Freedom can immediately
    end this effect, as can Tawil at'Umr's touch. Once every 24 hours, a displaced
    creature can attempt a new DC 39 Fortitude save to end the effect, but otherwise
    this effect is permanent. The save DCs are Charisma-based.
  Unspeakable Presence (Su): As long as it remains shrouded in its cloak, Tawil at'Umr's
    unspeakable presence is suppressed, but as soon as it attacks or otherwise reveals
    its true form, any creature within range that fails a DC 39 Will save is placed
    in its own subjective reality, as if under the effects of a microcosm spell. A
    creature immune to mind-affecting effects that fails its save against this effect
    is instead staggered for 1d6 rounds. This is a mind-affecting phantasm effect.
    The save DC is Charisma-based.
desc_long: |-
  Tawil at'Umr is unusual among the Great Old Ones, for it is a physical projection of the will of one of the most powerful of the Outer Gods-Yog-Sothoth. As a sort of avatar of this deity, Tawil at'Umr pursues its own goals throughout the Material Plane and dimensions that intersect it in ways mortals can never fully understand. Tawil at'Umr is just as likely to react to attacks against it with its formidable combat prowess as it is to ignore its attackers or simply relocate to another point in the multiverse-its reasons for doing so are as inscrutable as its plans for reality. Some scholars theorize that Tawil at'Umr is little more than a side effect of Yog-Sothoth's presence upon reality when the Outer God brushes up against this universe. Even if this is the case, Tawil at'Umr's knowledge of reality is vast, and many have sought the avatar out to learn its secrets. 

  Tawil at'Umr appears as a cloaked figure of approximately the same shape as the observer, yet larger- when viewed by a humanoid, it stands 12 feet tall. When it casts its cloak aside, it is revealed as a seething mass of protoplasm capable of taking many shapes and forms, several of which should not be able to exist.

---

# Great Old One, Tawil At'umr
A _[[monsters/Gray|gray]]_ robe and _[[spells/Veil|veil]]_ obscure this humanoid’s form, save for a

foaming mass of bubbles and tentacles extending from below.
**Source** Bestiary 6 pg. 148
**XP** 9,830,400

CN Large outsider (chaotic, extraplanar, Great Old One)
**Init** +27; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/True Seeing|true seeing]]_;

Perception +49
**Aura** _[[spells/Cloak of Chaos|cloak of chaos]]_ (DC 30), unspeakable presence (300 ft., DC 39)

##### Defense

**AC** 49, touch 37, _[[conditions/Flat-Footed|flat-footed]]_ 35 (+4 deflection, +13 Dex, +1 _[[feats/Dodge|dodge]]_,

+10 insight, +12 natural, –1 size)
**hp** 752 (35d10+560); _[[universal monster rules/Fast Healing|fast healing]]_ 30
**Fort** +31, **Ref** +36, **Will** +34
**Defensive Abilities** _[[universal monster rules/Amorphous|amorphous]]_, dimensional _[[universal monster rules/Fortification|fortification]]_,

_[[spells/Freedom of Movement|freedom of movement]]_, immortality, _[[spells/Insanity|insanity]]_ (DC 39); **Immune** ability damage, ability drain, aging, cold, death

effects, disease, _[[universal monster rules/Energy Drain|energy drain]]_, mind-affecting effects,

_[[universal monster rules/Paralysis|paralysis]]_, petrification, sonic; **Resist** acid 30, electricity 30,

fire 30; **SR** 41

##### Offense
**Speed** 60 ft., fly 120 ft. (perfect)
**Melee** 2 slams +51 (2d8+17 plus temporal _[[spells/Displacement|displacement]]_),

4 tentacles +49 (6d6+8/19–20 plus _[[universal monster rules/Grab|grab]]_)
**Space** 10 ft., **Reach** 10 ft. (30 ft. with tentacles)
**Special Attacks** _[[spells/Command|command]]_ the ancient ones, _[[universal monster rules/Constrict|constrict]]_ (6d6+25),

dimensional dreams, merge lives, mythic power (10/day,

surge +1d12), portal mastery
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 30th; concentration +42)
Constant—_cloak of chaos_ (DC 30), _freedom of movement_, _[[spells/Tongues|tongues]]_, _true seeing_ 
At will—_[[spells/Astral Projection|astral projection]]_, _[[spells/Dimensional Lock|dimensional lock]]_, _[[spells/Dream|dream]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Interplanetary Teleport|interplanetary teleport]]_, _[[spells/Nightmare|nightmare]]_, _[[spells/Plane Shift|plane shift]]_ (DC 29), _[[spells/Sending|sending]]_, _[[spells/Teleport Object|teleport object]]_ (DC 29) 
3/day—_[[spells/Demand|demand]]_ (DC 30), quickened _[[spells/Disintegrate|disintegrate]]_ (DC 28), quickened _[[spells/Feeblemind|feeblemind]]_ (DC 27), quickened _[[spells/Mislead|mislead]]_ (DC 28) 
1/day—_[[spells/Gate|gate]]_, _[[spells/Microcosm|microcosm]]_ (DC 31), _[[universal monster rules/Summon|summon]]_ (level 9, 2 ancient ones 100%), _[[spells/Time Stop|time stop]]_, _[[spells/Wish|wish]]_ 
**M** mythic spell

##### Statistics
**Str** 44, **Dex** 36, **Con** 43, **Int** 35, **Wis** 32, **Cha** 35
**Base Atk** +35; **CMB** +53; **CMD** 91 (can’t be tripped)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Greater Disarm|Greater Disarm]]_, _[[feats/Greater Sunder|Greater Sunder]]_, _[[feats/Improved Critical|Improved Critical]]_ (tentacle), _[[feats/Improved Disarm|Improved Disarm]]_, Improved

Initiative, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Multiattack|Multiattack]]_, Power

Attack, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_disintegrate_, _feeblemind_, _mislead_), _[[feats/Staggering Critical|Staggering Critical]]_
**Skills** Acrobatics +48, Bluff +50, Diplomacy +47,

Disguise +47, Fly +57, Intimidate +47, Knowledge (arcana,

engineering, geography, history, nature, religion) +47,

Knowledge (planes) +50, Perception +49, Sense Motive +49,

Spellcraft +47, Stealth +47, Use Magic Device +47
**Languages** Aklo; _[[universal monster rules/Telepathy|telepathy]]_ 1 mile; _tongues_
**SQ** otherworldly insight

##### Ecology

**Environment** any
**Organization** solitary (unique)
**Treasure** triple

### Special Abilities

**_Command_ the Ancient Ones (Su)** Tawil at’Umr commands the obedience of a race of lesser immortals known as the ancient ones, creatures akin to itself but of inferior power. An ancient one is a _[[monsters/Hundun|hundun]]_ with the invincible mythic simple template that is native to the Material Plane. In addition to Tawil at’Umr being able to _summon_ ancient ones to its side, any _command_ spoken or telepathically sent from it to an ancient one (but not to a normal _hundun_) must be obeyed without question (and with no save).

**Dimensional Dreams (Su)** When Tawil at’Umr uses its _nightmare_ spell-like ability, it can target any creature it has affected with its spell-like or supernatural abilities, or any creature that has ever traveled via a _gate_ spell, regardless of distance. In addition to the effects of _nightmare_, the target must succeed at a DC 39 Will save or die, only to be reincarnated a moment later into a new body on another world. This is a mind-affecting death effect. The save DC is Charisma-based.

**Dimensional _Fortification_ (Ex)** Tawil at’Umr cannot be forced to travel via teleportation effects unless it so chooses.

**Immortality (Ex)** If Tawil at’Umr is killed, Yog-Sothoth can create a new avatar immediately. The replacement Tawil at’Umr typically does not reappear where it was killed, and it usually does not seek revenge against those who slew its predecessor. Usually.

**Merge Lives (Su)** Once per day as a full-round action, Tawil at’Umr can cause a touched creature’s mind (the target) to merge with any other creature (the host) that Tawil at’Umr has affected via dimensional dreams. The target can resist this effect with a successful DC 39 Will save. If the creature fails its save, its body vanishes (leaving behind any gear it may have carried) and its mind becomes trapped in the host creature’s mind. The target can observe the world through the host creature but cannot control the host creature’s actions. In time, or under certain conditions, the target can eventually take control of the host’s actions, but these developments are rare and require hundreds of years to occur (usually, the host creature dies long before the target can exert such influence). To others, it is rarely apparent which body throughout the countless worlds Tawil at’Umr has seen was chosen as a host for the target’s mind. This is a mindaffecting curse effect. The save DC is Charisma-based.

**Portal Mastery (Su)** Tawil at’Umr senses when a creature is about to teleport into its vicinity (within range of its unspeakable presence), or when a portal is about to open in that same area. If it wishes, Tawil at’Umr can block the teleportation or portal effect from occurring as an immediate action. The creator of the effect must succeed at a caster level check against Tawil at’Umr’s _[[universal monster rules/Spell Resistance|spell resistance]]_ or the effect is countered.

**Temporal _Displacement_ (Su)** A creature struck by one of Tawil at’Umr’s slam attacks must succeed at a DC 39 Fortitude save or enter a state of suspended animation like that created by _[[spells/Temporal Stasis|temporal stasis]]_. This condition cannot be removed via _dispel magic_, nor does _freedom of movement_ offer protection. _[[spells/Freedom|Freedom]]_ can immediately end this effect, as can Tawil at’Umr’s touch. Once every 24 hours, a displaced creature can attempt a new DC 39 Fortitude save to end the effect, but otherwise this effect is permanent. The save DCs are Charisma-based.

**Unspeakable Presence (Su)** As long as it remains shrouded in its cloak, Tawil at’Umr’s unspeakable presence is suppressed, but as soon as it attacks or otherwise reveals its _[[spells/True Form|true form]]_, any creature within range that fails a DC 39 Will save is placed in its own _[[spells/Subjective Reality|subjective reality]]_, as if under the effects of a _microcosm_ spell. A creature immune to mind-affecting effects that fails its save against this effect is instead _[[conditions/Staggered|staggered]]_ for 1d6 rounds. This is a mind-affecting phantasm effect. The save DC is Charisma-based.

##### Description

Tawil at’Umr is unusual among the Great Old Ones, for it is a physical projection of the will of one of the most powerful of the Outer Gods—Yog-Sothoth. As a sort of avatar of this deity, Tawil at’Umr pursues its own goals throughout the Material Plane and dimensions that intersect it in ways mortals can never fully understand. Tawil at’Umr is just as likely to react to attacks against it with its formidable combat prowess as it is to ignore its attackers or simply relocate to another point in the multiverse—its reasons for doing so are as inscrutable as its plans for reality. Some scholars theorize that Tawil at’Umr is little more than a side effect of Yog-Sothoth’s presence upon reality when the Outer God brushes up against this universe. Even if this is the case, Tawil at’Umr’s knowledge of reality is vast, and many have sought the avatar out to learn its secrets.

Tawil at’Umr appears as a cloaked figure of approximately the same shape as the observer, yet larger— when viewed by a humanoid, it stands 12 feet tall. When it casts its cloak aside, it is revealed as a seething mass of protoplasm capable of taking many shapes and forms, several of which should not be able to exist.
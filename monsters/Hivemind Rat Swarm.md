---
cssclass: [monsters]
title1: Hivemind Rat Swarm
desc_short: A swarm of rats groups around a barrel, every pair of red eyesstaring
  intently at one rat in the center of the mass.
title2: Hivemind Rat Swarm
CR: 8
sources:
- name: Bestiary 6
  page: 156
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 4800
alignment: N
size: Tiny
type: magical beast
subtypes:
- swarm
initiative:
  bonus: 6
senses:
  darkvision: 60
  low-light vision: true
  scent: true
  thoughtsense: 60
AC:
  AC: 20
  touch: 20
  flat_footed: 18
  components:
    dex: 2
    insight: 6
    size: 2
HP:
  HP: 76
  long: 9d10+27
saves:
  fort: 8
  ref: 10
  will: 4
defensive_abilities:
- swarm traits
speeds:
  base: 15
  climb: 15
  swim: 15
attacks:
  melee:
  - - text: swarm (2d6 plus disease and distraction)
      entries:
      - - damage: 2d6
        - effect: disease
        - effect: distraction
      attack: swarm
  special:
  - disease
  - distraction (DC 16)
  - psychic spellcasting
space: 10
reach: 0
spell_like_abilities:
  entries:
  - name: synaptic pulse
    source: default
    freq: 3rd (4/day)
    DC: 16
  - name: paranoia
    source: default
    freq: 2nd (6/day)
    DC: 15
  - name: spontaneous immolation
    source: default
    freq: 2nd (6/day)
    DC: 16
  - name: charm animal
    source: default
    freq: 1st (7/day)
    DC: 14
  - name: charm person
    source: default
    freq: 1st (7/day)
    DC: 14
  - name: mind thrust I
    source: default
    freq: 1st (7/day)
    DC: 14
  - name: unseen servant
    source: default
    freq: 1st (7/day)
  - name: bleed
    source: default
    freq: 0 (at will)
    DC: 13
  - name: daze
    source: default
    freq: 0 (at will)
    DC: 13
  - name: ghost sound
    source: default
    freq: 0 (at will)
    DC: 13
  - name: haunted fey aspect
    source: default
    freq: 0 (at will)
    DC: 13
  - name: mage hand
    source: default
    freq: 0 (at will)
  - name: open/close
    source: default
    freq: 0 (at will)
  - name: telekinetic projectile
    source: default
    freq: 0 (at will)
    DC: 13
  sources:
  - name: default
    CL: 6
    concentration: 9
ability_scores:
  STR: 2
  DEX: 15
  CON: 14
  INT: 17
  WIS: 13
  CHA: 10
BAB: 9
CMB:
CMD:
feats:
- name: Combat Casting
- name: Improved Initiative
- name: Lightning Reflexes
- name: Skill Focus (Perception)
- name: Toughness
skills:
  Acrobatics: 14
  Climb: 14
  Knowledge (arcana): 15
  Perception: 16
  Stealth: 22
    when hiding the nexus: 32
  Swim: 10
  _racial_mods:
    Stealth:
      when hiding the nexus: 10
languages:
- Aklo
- Common
- Goblin
- Halfling
- telepathy 100 ft.
special_qualities:
- hivemind nexus
ecology:
  environment: any
  organization: solitary or infestation (2-5 swarms)
  treasure_type: none
special_abilities:
  Disease (Su): Swarm-injury; save Fort DC 16; onset 1d3 days; frequency 1/day; effect
    1d3 Dex damage and 1d3 Con damage; cure 2 consecutive saves.
desc_long: |-
  A hivemind consists of a swarm of smaller creatures whose individual minds have supernaturally bonded into one to become a single, collective intelligence. Hiveminds often occur in swarms that have existed for generations and that have dwelled in areas of potent magical influence, particularly areas of strong psychic magic. Over time, the swarm learns to work together in more intelligent ways to achieve its goals, and it eventually evolves a cohesive mind. Of course, this evolution can be hastened by direct intervention of potent magic (typically something on the level of a miracle or wish), or as an unintended side effect of esoteric rituals, the use or destruction of artifacts, or the deaths of powerful minds. 

  A hivemind swarm learns from its surroundings, which in turn shape its choices in the languages it learns and the psychic spells it develops a penchant for casting. An urban swarm may pick up Common, Dwarven, Elven, or Halfling from snippets of conversations overheard through sewer grates, whereas an underground swarm may learn Dwarven or Undercommon. A hivemind may begin to exert its psychic abilities by compelling animals or people to bring it food or protect it from larger creatures, and it slowly graduates to defending itself and actively attacking as it gains experience. 

  Eventually, the hivemind's mental network takes on more complex tasks as a collective mind. At this point, the hivemind creates a nexus, a single individual in the swarm through which the collective routes all thought. While the nexus is often fairly inconspicuous within the teeming mass of the swarm, it is possible for a highly perceptive observer to notice its decisive movements, spellcasting gestures, or intense gaze. The death of the nexus does not eliminate the shared intelligence of a hivemind, but it is disruptive, forcing the collective to focus inward to regroup and form a new nexus.

---

# Hivemind Rat Swarm
A swarm of rats groups around a _[[items/Mundane/Barrel|barrel]]_, every pair of red eyes

staring intently at one rat in the center of the mass.
**Source** Bestiary 6 pg. 156
**XP** 4,800

N Tiny magical beast (swarm)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_,

_[[universal monster rules/Thoughtsense|thoughtsense]]_ 60 ft.; Perception +16

##### Defense

**AC** 20, touch 20, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+2 Dex, +6 insight, +2 size)
**hp** 76 (9d10+27)
**Fort** +8, **Ref** +10, **Will** +4
**Defensive Abilities** swarm traits

##### Offense
**Speed** 15 ft., _[[universal monster rules/Climb|climb]]_ 15 ft., swim 15 ft.
**Melee** swarm (2d6 plus disease and _[[universal monster rules/Distraction|distraction]]_)
**Space** 10 ft., **Reach** 0 ft.
**Special Attacks** disease, _distraction_ (DC 16), _[[classes/Psychic|psychic]]_ spellcasting
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +9)
3rd (4/day)—_[[spells/Synaptic Pulse|synaptic pulse]]_ (DC 16) 
2nd (6/day)—_[[spells/Paranoia|paranoia]]_ (DC 15), _[[spells/Spontaneous Immolation|spontaneous immolation]]_ (DC 16) 
1st (7/day)—_[[spells/Charm Animal|charm animal]]_ (DC 14), _[[spells/Charm Person|charm person]]_ (DC 14), _[[spells/Mind Thrust I|mind thrust I]]_ (DC 14), _[[spells/Unseen Servant|unseen servant]]_ 
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Daze|daze]]_ (DC 13), _[[spells/Ghost Sound|ghost sound]]_ (DC 13), _[[spells/Haunted Fey Aspect|haunted fey aspect]]_ (DC 13), _[[spells/Mage Hand|mage hand]]_, open/close, _[[spells/Telekinetic Projectile|telekinetic projectile]]_ (DC 13)

##### Statistics
**Str** 2, **Dex** 15, **Con** 14, **Int** 17, **Wis** 13, **Cha** 10
**Base Atk** +9; **CMB** —; **CMD** —
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Toughness|Toughness]]_
**Skills** Acrobatics +14, _Climb_ +14, Knowledge (arcana) +15,

Perception +16, Stealth +22 (+32 when hiding the nexus),

Swim +10; **Racial Modifiers** +10 Stealth when hiding the nexus
**Languages** Aklo, Common, _[[monsters/Goblin|Goblin]]_, Halfling; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** hivemind nexus

##### Ecology

**Environment** any
**Organization** solitary or infestation (2–5 swarms)
**Treasure** none

### Special Abilities

**Disease (Su)** Swarm—injury; save Fort DC 16; onset 1d3 days; frequency 1/day; effect 1d3 Dex damage and 1d3 Con damage; cure 2 consecutive saves.

##### Description

A hivemind consists of a swarm of smaller creatures whose individual minds have supernaturally bonded into one to become a single, collective intelligence. Hiveminds often occur in swarms that have existed for generations and that have dwelled in areas of _[[items/Weapon Magic Abilities/Potent|potent]]_ magical influence, particularly areas of strong _[[universal monster rules/Psychic Magic|psychic magic]]_. Over time, the swarm learns to work together in more intelligent ways to achieve its goals, and it eventually evolves a cohesive mind. Of course, this evolution can be hastened by direct intervention of _potent_ magic (typically something on the level of a _[[spells/Miracle|miracle]]_ or _[[spells/Wish|wish]]_), or as an unintended side effect of esoteric rituals, the use or _[[spells/Destruction|destruction]]_ of artifacts, or the deaths of powerful minds.

A hivemind swarm learns from its surroundings, which in turn shape its choices in the languages it learns and the _psychic_ spells it develops a penchant for casting. An urban swarm may pick up Common, Dwarven, Elven, or Halfling from snippets of conversations overheard through sewer grates, whereas an underground swarm may learn Dwarven or Undercommon. A hivemind may begin to exert its _psychic_ abilities by compelling animals or people to bring it food or protect it from larger creatures, and it slowly graduates to _[[items/Weapon Magic Abilities/Defending|defending]]_ itself and actively attacking as it gains experience.

Eventually, the hivemind’s mental network takes on more complex tasks as a collective mind. At this point, the hivemind creates a nexus, a single individual in the swarm through which the collective routes all thought. While the nexus is often fairly inconspicuous within the teeming mass of the swarm, it is possible for a highly perceptive observer to notice its decisive movements, spellcasting gestures, or intense _[[universal monster rules/Gaze|gaze]]_. The death of the nexus does not eliminate the shared intelligence of a hivemind, but it is _[[feats/Disruptive|disruptive]]_, forcing the collective to focus inward to regroup and form a new nexus.
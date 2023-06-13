---
cssclass: [monsters]
title1: Automaton, Master Automaton
desc_short: This construct is covered with elaborate markings. Its arms end in tremendous
  hooks, and the core in its head glows with light.
title2: Master Automaton
CR: 20
sources:
- name: Construct Handbook
  page: 26
  link: https://paizo.com/products/btq01vam
XP: 307200
alignment: LN
size: Huge
type: construct
subtypes:
- automaton
- extraplanar
initiative:
  bonus: 3
senses:
  automaton sense: true
  darkvision: 60
  low-light vision: true
  true seeing: true
AC:
  AC: 38
  touch: 20
  flat_footed: 34
  components:
    dex: 3
    dodge: 1
    insight: 8
    natural: 18
    size: -2
HP:
  HP: 377
  long: 25d10+240
  fast_healing: 20
saves:
  fort: 16
  ref: 19
  will: 23
defensive_abilities:
- powerful core
- reconstruction
immunities:
- construct traits
- electricity
resistances:
  cold: 30
  sonic: 30
SR: 31
weaknesses:
- vulnerable mind
speeds:
  base: 60
  climb: 30
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: 2 arcane hooks +33 (4d10+18/19-20)
      entries:
      - - damage: 4d10+18
          crit_range: 19-20
      count: 2
      attack: arcane hooks
      bonus:
      - 33
  special:
  - energy beam (90-ft. line or 60-ft. cone, DC 30, 20d6, usable every 1d3 rounds)
  - rend (2 arcane hooks, 4d10+18)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: tongues
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: cloudkill
    source: default
    freq: At will
    DC: 23
  - name: fireball
    source: default
    freq: At will
    DC: 21
  - name: lightning bolt
    source: default
    freq: At will
    DC: 21
  - name: teleport
    source: default
    freq: At will
  - name: banishment
    source: default
    freq: 3/day
    DC: 25
  - name: blade barrier
    source: default
    freq: 3/day
    DC: 24
  - name: plane shift
    source: default
    freq: 3/day
  - name: power word stun
    source: default
    freq: 3/day
    DC: 26
  - name: reverse gravity
    source: default
    freq: 1/day
  - name: prismatic wall
    source: default
    freq: 1/day
  - name: time stop
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 25
    concentration: 33
ability_scores:
  STR: 28
  DEX: 16
  CON:
  INT: 20
  WIS: 21
  CHA: 27
BAB: 25
CMB: 36
CMD: 58
feats:
- name: Alertness
- name: Combat Expertise
- name: Combat Reflexes
- name: Dodge
- name: Flyby Attack
- name: Hover
- name: Improved Critical (arcane hook)
- name: Iron Will
- name: Mobility
- name: Power Attack
- name: Spring Attack
- name: Vital Strike
- name: Weapon Focus (arcane hook)
skills:
  Climb: 32
  Diplomacy: 23
  Fly: 27
  Intimidate: 23
  Knowledge (arcana): 30
  Knowledge (planes): 30
  Perception: 34
  Sense Motive: 7
  Spellcraft: 20
  Use Magic Device: 23
languages:
- Abyssal
- Celestial
- Common
- Ignan
- Jistka
- telepathy 100 ft.
- tongues
ecology:
  environment: any (Axis)
  organization: solitary
  treasure_type: none
special_abilities:
  Arcane Hooks (Ex): A master automaton's hooks are treated as having the ghost touch
    property and as epic weapons for the purpose of overcoming damage reduction. A
    master automaton applies twice its Strength as a bonus on damage rolls with its
    hooks. When a master automaton hits with a hook, it can attempt a reposition combat
    maneuver as a free action. With a successful combat maneuver check, the master
    automaton can move its target to any square within its reach. If both hook attacks
    hit the target, the master automaton gains a +5 bonus on the combat maneuver check.
  Automaton Sense (Ex): A master automaton can sense and locate other automatons within
    500 feet as if it had blindsense, and it can detect automatons within 60 feet
    as if it had blindsight.
  Consume Core (Ex): A master automaton can consume the life energy found within an
    automaton core as a standard action. Consuming a core in this manner destroys
    the automaton core and grants the master a +1 bonus to natural armor and on attack
    rolls, skill checks, and saving throws for 24 hours. Consuming a second automaton
    core within this 24 hour period causes the bonuses to become permanent. A master
    automaton can never gain more than a +10 bonus by consuming automaton cores. If
    a master automaton consumes the automaton core of another master automaton, it
    gains that master automaton's permanent bonuses gained by the consume core ability,
    if any, and add these bonuses to its own permanent bonuses.
  Energy Beam (Ex): A master automaton can focus the energy in its core to fire either
    a 90-foot line or a 60-foot cone of energy as a standard action. The beam deals
    20d6 points of damage to each creature caught in the area (Reflex DC 30 half).
    Half of the damage is fire damage and half is force damage. A master automaton
    can use its energy beam once every 1d3 rounds. A master automaton can use its
    energy beam when it is grappling or being grappled. The save DC is Wisdom-based.
  Powerful Core (Ex): A master automaton's automaton core is filled with extremely
    potent life energy, granting the master an insight bonus to AC and on saving throws
    equal to the master automaton's Charisma bonus (if any). Additionally, this energy
    grants the master automaton a number of bonus hit points per Hit Die equal to
    its Charisma bonus (if any).
  Reconstruction (Ex): A master automaton is able to reconstruct itself if its body
    is destroyed. The master automaton's automaton core uses its energy to rebuild
    the automaton's body over the span of 1d10 days. If the core is located in Axis,
    the reconstruction requires only 1d10 hours. Once reconstructed, the master automaton
    reactivates with full hit points and any bonuses it had gained from the consume
    core ability. Only destroying a master automaton's automaton core prevents this
    reconstruction.
desc_long: |+
  Master automatons are the most powerful among their kind. The highest-ranking leaders of the Artificer Conclave reserved these frames for themselves, intent on using their power to keep the rest of the automatons, and the other masters, in check. Most master automatons did not enter combat, instead choosing to serve as strategists and advisors.

   While every master automaton is customized to serve the needs of the Conclave, they all command the same basic abilities. Most notable is their ability to detect and destroy automaton cores, an ability developed in case it became necessary to stop rogue automatons. Each master's frame is created with an arcane resonance that matches that found in automaton cores, allowing a master automaton to destroy and consume a core with ease. An unexpected side effect of this destruction process, however, is that a master absorbs the destroyed core's energy, which empowers the master.

   This knowledge soon led to an arms race among the masters as they sought more automatons that they deemed as deserving of destruction. A large number of automatons were destroyed and consumed before this arms race eventually reached a deadlock, when the masters intentionally destroyed the means of creating new automaton cores in an attempt to cut off their rivals. This marked the end of the Artificer Conclave, and the masters soon went into hiding.

   Today, the masters hide among the planes, mostly in especially remote or dangerous areas. Very few masters remain on Golarion. These masters resurface only when they find leads on a large collection of automaton cores or a particularly powerful automaton, biding their time until the perfect moment to strike. A few masters did not fall prey to avarice, though, and instead serve as advisors to particularly powerful beings, such as great rulers or powerful mages, hoping to steer them away from Jistka's past mistakes. Others still continue their search for knowledge, exploring the multiverse at their leisure to collect new knowledge and meet new personalities. Of particular note is the master automaton Anquira, who makes it very public that she is on a quest to speak with the other masters in the hopes of piecing together the lost knowledge of automaton creation to help restore the automatons to their original forms.

...

---

# Automaton, Master Automaton
This construct is covered with elaborate markings. Its arms end in tremendous hooks, and the core in its head glows with light.
**Source** Construct Handbook pg. 26
**XP** 307,200

LN Huge construct (automaton, extraplanar)
**Init** +3; **Senses** automaton sense, _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/True Seeing|true seeing]]_; Perception +34

##### Defense

**AC** 38, touch 20, _[[conditions/Flat-Footed|flat-footed]]_ 34 (+3 Dex, +1 dodge, +8 insight, +18 natural, -2 size)
**hp** 377 (25d10+240); _[[universal monster rules/Fast Healing|fast healing]]_ 20
**Fort** +16, **Ref** +19, **Will** +23
**Defensive Abilities** powerful core, reconstruction; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_, electricity; **Resist** cold 30, sonic 30; **SR** 31
**Weaknesses** vulnerable mind

##### Offense
**Speed** 60 ft., _[[universal monster rules/Climb|climb]]_ 30 ft., fly 60 ft. (average)
**Melee** 2 arcane hooks +33 (4d10+18/19-20)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** energy beam (90-ft. line or 60-ft. cone, DC 30, 20d6, usable every 1d3 rounds), _[[universal monster rules/Rend|rend]]_ (2 arcane hooks, 4d10+18)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 25th; concentration +33)
Constant—_[[spells/Tongues|tongues]]_, _true seeing_ 
At will—_[[spells/Cloudkill|cloudkill]]_ (DC 23), _[[spells/Fireball|fireball]]_ (DC 21), _[[spells/Lightning Bolt|lightning bolt]]_ (DC 21), teleport 
3/day—_[[spells/Banishment|banishment]]_ (DC 25), _[[spells/Blade Barrier|blade barrier]]_ (DC 24), _[[spells/Plane Shift|plane shift]]_, _[[spells/Power Word Stun|power word stun]]_ (DC 26) 
1/day—_[[spells/Reverse Gravity|reverse gravity]]_, _[[spells/Prismatic Wall|prismatic wall]]_, _[[spells/Time Stop|time stop]]_

##### Statistics
**Str** 28, **Dex** 16, **Con** —, **Int** 20, **Wis** 21, **Cha** 27
**Base Atk** +25; **CMB** +36; **CMD** 58
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (arcane hook), _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (arcane hook)
**Skills** _Climb_ +32, Diplomacy +23, Fly +27, Intimidate +23, Knowledge (arcana) +30, Knowledge (planes) +30, Perception +34, Sense Motive +7, Spellcraft +20, Use Magic Device +23
**Languages** Abyssal, Celestial, Common, Ignan, Jistka; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft., _tongues_

##### Ecology

**Environment** any (Axis)
**Organization** solitary
**Treasure** none

### Special Abilities

**Arcane Hooks (Ex)** A master automaton’s hooks are treated as having the _[[items/Weapon Magic Abilities/Ghost Touch|ghost touch]]_ property and as epic weapons for the purpose of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_. A master automaton applies twice its Strength as a bonus on damage rolls with its hooks. When a master automaton hits with a hook, it can attempt a reposition combat maneuver as a free action. With a successful combat maneuver check, the master automaton can move its target to any square within its reach. If both hook attacks hit the target, the master automaton gains a +5 bonus on the combat maneuver check.

**Automaton Sense (Ex)** A master automaton can sense and locate other automatons within 500 feet as if it had _[[universal monster rules/Blindsense|blindsense]]_, and it can detect automatons within 60 feet as if it had _[[universal monster rules/Blindsight|blindsight]]_.

**Consume Core (Ex)** A master automaton can consume the life energy found within an _[[items/Wondrous Item/Automaton Core|automaton core]]_ as a standard action. Consuming a core in this manner destroys the _automaton core_ and grants the master a +1 bonus to natural armor and on attack rolls, skill checks, and saving throws for 24 hours. Consuming a second _automaton core_ within this 24 hour period causes the bonuses to become permanent. A master automaton can never gain more than a +10 bonus by consuming automaton cores. If a master automaton consumes the _automaton core_ of another master automaton, it gains that master automaton’s permanent bonuses gained by the consume core ability, if any, and add these bonuses to its own permanent bonuses.

**Energy Beam (Ex)** A master automaton can focus the energy in its core to fire either a 90-foot line or a 60-foot cone of energy as a standard action. The beam deals 20d6 points of damage to each creature caught in the area (Reflex DC 30 half). Half of the damage is fire damage and half is force damage. A master automaton can use its energy beam once every 1d3 rounds. A master automaton can use its energy beam when it is grappling or being _[[conditions/Grappled|grappled]]_. The save DC is Wisdom-based.

**Powerful Core (Ex)** A master automaton’s _automaton core_ is filled with extremely _[[items/Weapon Magic Abilities/Potent|potent]]_ life energy, granting the master an insight bonus to AC and on saving throws equal to the master automaton’s Charisma bonus (if any). Additionally, this energy grants the master automaton a number of bonus hit points per Hit Die equal to its Charisma bonus (if any).

**Reconstruction (Ex)** A master automaton is able to reconstruct itself if its body is destroyed. The master automaton’s _automaton core_ uses its energy to rebuild the automaton’s body over the span of 1d10 days. If the core is located in Axis, the reconstruction requires only 1d10 hours. Once reconstructed, the master automaton reactivates with full hit points and any bonuses it had gained from the consume core ability. Only destroying a master automaton’s _automaton core_ prevents this reconstruction.

##### Description

Master automatons are the most powerful among their kind. The highest-ranking leaders of the Artificer Conclave reserved these frames for themselves, intent on using their power to keep the rest of the automatons, and the other masters, in check. Most master automatons did not enter combat, instead choosing to serve as strategists and advisors.

While every master automaton is customized to serve the needs of the Conclave, they all _[[spells/Command|command]]_ the same basic abilities. Most notable is their ability to detect and destroy automaton cores, an ability developed in case it became necessary to stop _[[classes/Rogue|rogue]]_ automatons. Each master’s frame is created with an arcane resonance that matches that found in automaton cores, allowing a master automaton to destroy and consume a core with ease. An unexpected side effect of this _[[spells/Destruction|destruction]]_ process, however, is that a master absorbs the destroyed core’s energy, which empowers the master.

This knowledge soon led to an arms race among the masters as they sought more automatons that they deemed as deserving of _destruction_. A large number of automatons were destroyed and consumed before this arms race eventually reached a deadlock, when the masters intentionally destroyed the means of creating new automaton cores in an attempt to cut off their rivals. This marked the end of the Artificer Conclave, and the masters soon went into hiding.

Today, the masters hide among the planes, mostly in especially remote or dangerous areas. Very few masters remain on Golarion. These masters resurface only when they find leads on a large collection of automaton cores or a particularly powerful automaton, biding their time until the perfect moment to strike. A few masters did not fall prey to avarice, though, and instead serve as advisors to particularly powerful beings, such as great rulers or powerful mages, hoping to steer them away from Jistka’s past mistakes. Others still continue their search for knowledge, exploring the multiverse at their leisure to collect new knowledge and meet new personalities. Of particular note is the master automaton Anquira, who makes it very public that she is on a quest to speak with the other masters in the hopes of piecing together the lost knowledge of automaton creation to help restore the automatons to their original forms.
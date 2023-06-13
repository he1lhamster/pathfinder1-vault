---
cssclass: [monsters]
title1: Clockwork, Clockwork Overseer
desc_short: One arm of this six-limbed clockwork construct ends in a broad fist, and
  the other extends into an articulated metal lash.
title2: Clockwork Overseer
CR: 7
sources:
- name: 'Pathfinder #123: The Flooded Cathedral'
  page: 86
  link: http://paizo.com/products/btpy9uk2?Pathfinder-Adventure-Path-123-The-Flooded-Cathedral
XP: 3200
alignment: N
size: Medium
type: construct
subtypes:
- clockwork
initiative:
  bonus: 6
senses:
  all-around vision: true
  darkvision: 60
  low-light vision: true
auras:
- name: aura of command
  radius: 30
AC:
  AC: 21
  touch: 14
  flat_footed: 17
  components:
    dex: 2
    dodge: 2
    natural: 7
HP:
  HP: 75
  long: 10d10+20
saves:
  fort: 4
  ref: 8
  will: 5
DR:
- amount: 5
  weakness: adamantine
immunities:
- construct traits
weaknesses:
- vulnerable to electricity
speeds:
  base: 30
  climb: 30
attacks:
  melee:
  - - text: lash +15 (1d4+5 plus trip)
      entries:
      - - damage: 1d4+5
        - effect: trip
      attack: lash
      bonus:
      - 15
    - text: slam +15 (1d6+5 plus push)
      entries:
      - - damage: 1d6+5
        - effect: push
      attack: slam
      bonus:
      - 15
  special:
  - overclock
  - push (slam, 10 ft.)
space: 5
reach: 5
reach_other: 10 ft. with lash
ability_scores:
  STR: 19
  DEX: 14
  CON:
  INT:
  WIS: 13
  CHA: 1
BAB: 10
CMB: 15
CMD: 29
feats:
- is_bonus: true
  name: Improved Initiative
- is_bonus: true
  name: Lightning Reflexes
skills:
  Climb: 12
  Perception: 1
special_qualities:
- swift reactions
- tactical calculus
- winding
ecology:
  environment: any land
  organization: solitary, crew (1 plus 2-5 clockwork servants), or deployment (1-2
    plus 2-5 clockwork soldiers)
  treasure_type: none
special_abilities:
  Aura of Command (Ex): A clockwork overseer broadcasts subtle commands in a 30-foot
    radius, granting heightened combat abilities to all clockwork creatures in the
    area. Affected clockwork creatures, including the clockwork overseer, gain a +1
    competence bonus on saving throws, attack rolls, and weapon damage rolls; these
    bonuses are already calculated into the clockwork overseer's statistics. As a
    standard action, a clockwork overseer can intensify the aura until the beginning
    of its next turn, increasing the competence bonus to +2.
  Lash (Ex): A clockwork overseer's lash is a primary natural attack that deals bludgeoning
    damage.
  Overclock (Ex): In place of making a lash attack on its turn, a clockwork overseer
    can overclock another clockwork creature within its reach, impelling it to exceed
    its performance limitations. At the beginning of its turn, an overclocked creature
    takes an amount of damage equal to half its Hit Dice (minimum 1), expends 1 full
    day of activity stored by its winding ability, and gains one of the following
    benefits, selected by the clockwork overseer. The overclocked creature gains the
    benefits of haste. The overclocked creature's natural attacks and attacks with
    metal melee weapons deal an additional 1d6 points of fire damage. If the creature
    already deals fire damage, including with a breath weapon or the swallow whole
    ability, that special attack's fire damage increases by 2d6. The overclocked creature
    gains Combat Reflexes as a bonus feat and gains a +2 bonus on attack rolls when
    making attacks of opportunity. A clockwork overseer can end this effect on a clockwork
    creature affected by its aura of command as a free action. The overclocked condition
    otherwise continues until the clockwork creature expends its stored days of activity
    or is destroyed.
  Tactical Calculus (Ex): A clockwork overseer can store hundreds of commands and
    scripts, allowing it to perform modest feats of problem-solving and strategic
    command as though it had an Intelligence score of 10. In practice, this enables
    a clockwork overseer to make tactical decisions, such as exploiting terrain or
    flanking targets, as well as convey simple tactical commands to other clockwork
    creatures in its aura of command. If the clockwork overseer takes electricity
    damage, it must succeed at a Fortitude save (DC = the electricity damage dealt)
    or lose both its aura of command and tactical calculus abilities for 1d4 rounds.
desc_long: What clockwork creatures boast in both strength and resilience, they often
  lack in nuance and strategy. Most machinists are content to command their constructs
  directly when seeking tactical precision, but only a few artificers have the technical
  expertise needed to create a mechanical lieutenant capable of reasoning and adapting
  in its master's absence. Known as clockwork overseers, these constructs boast extraordinarily
  complex programming that far exceeds the basic command vocabulary of other clockwork
  creatures. This allows clockwork overseers to store hundreds or even thousands of
  commands, which they can parse and sort quickly enough to simulate an intelligent
  creature's adaptive thinking-at least regarding combat strategy and moderately complex
  tasks of coordinating construct laborers. These functions fall short of true thought,
  and clockwork overseers are incapable of language, emotion, higher thinking, or
  symbolic reasoning beyond specific sounds and statements they might parrot on command.

---

# Clockwork, Clockwork Overseer
One arm of this six-limbed clockwork construct ends in a broad fist, and the other extends into an articulated metal lash.
**Source** Pathfinder #123: The Flooded Cathedral pg. 86
**XP** 3,200

N Medium construct (clockwork)
**Init** +6; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +1
**Aura** aura of _[[spells/Command|command]]_ (30 ft.)

##### Defense

**AC** 21, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+2 Dex, +2 _[[feats/Dodge|dodge]]_, +7 natural)
**hp** 75 (10d10+20)
**Fort** +4, **Ref** +8, **Will** +5
**DR** 5/adamantine; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_
**Weaknesses** vulnerable to electricity

##### Offense
**Speed** 30 ft., _[[universal monster rules/Climb|climb]]_ 30 ft.
**Melee** lash +15 (1d4+5 plus _[[universal monster rules/Trip|trip]]_), slam +15 (1d6+5 plus push)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with lash)
**Special Attacks** overclock, push (slam, 10 ft.)

##### Statistics
**Str** 19, **Dex** 14, **Con** —, **Int** —, **Wis** 13, **Cha** 1
**Base Atk** +10; **CMB** +15; **CMD** 29
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** _Climb_ +12
**SQ** swift reactions, tactical calculus, winding

##### Ecology

**Environment** any land
**Organization** solitary, crew (1 plus 2–5 clockwork servants), or deployment (1–2 plus 2–5 clockwork soldiers)
**Treasure** none

### Special Abilities

**Aura of _Command_ (Ex)** A clockwork overseer broadcasts subtle commands in a 30-foot radius, granting heightened combat abilities to all clockwork creatures in the area. Affected clockwork creatures, including the clockwork overseer, gain a +1 competence bonus on saving throws, attack rolls, and weapon damage rolls; these bonuses are already calculated into the clockwork overseer’s statistics. As a standard action, a clockwork overseer can intensify the aura until the beginning of its next turn, increasing the competence bonus to +2.

**Lash (Ex)** A clockwork overseer’s lash is a primary natural attack that deals bludgeoning damage.

**Overclock (Ex)** In place of making a lash attack on its turn, a clockwork overseer can overclock another clockwork creature within its reach, impelling it to exceed its performance limitations. At the beginning of its turn, an overclocked creature takes an amount of damage equal to half its Hit Dice (minimum 1), expends 1 full day of activity stored by its winding ability, and gains one of the following benefits, selected by the clockwork overseer.

* The overclocked creature gains the benefits of _[[spells/Haste|haste]]_. 
* The overclocked creature’s _[[universal monster rules/Natural Attacks|natural attacks]]_ and attacks with metal melee weapons deal an additional 1d6 points of fire damage. If the creature already deals fire damage, including with a _[[universal monster rules/Breath Weapon|breath weapon]]_ or the _[[universal monster rules/Swallow Whole|swallow whole]]_ ability, that special attack’s fire damage increases by 2d6. 
* The overclocked creature gains _[[feats/Combat Reflexes|Combat Reflexes]]_ as a bonus feat and gains a +2 bonus on attack rolls when making attacks of opportunity.

A clockwork overseer can end this effect on a clockwork creature affected by its aura of _command_ as a free action. The overclocked condition otherwise continues until the clockwork creature expends its stored days of activity or is destroyed.

**Tactical Calculus (Ex)** A clockwork overseer can store hundreds of commands and scripts, allowing it to perform modest feats of problem-solving and strategic _command_ as though it had an Intelligence score of 10. In practice, this enables a clockwork overseer to make tactical decisions, such as exploiting terrain or flanking targets, as well as convey simple tactical commands to other clockwork creatures in its aura of _command_. If the clockwork overseer takes electricity damage, it must succeed at a Fortitude save (DC = the electricity damage dealt) or lose both its aura of _command_ and tactical calculus abilities for 1d4 rounds.

##### Description

What clockwork creatures boast in both strength and resilience, they often lack in nuance and strategy. Most machinists are content to _command_ their constructs directly when seeking tactical precision, but only a few artificers have the technical expertise needed to create a mechanical lieutenant capable of reasoning and adapting in its master’s absence. Known as clockwork overseers, these constructs boast extraordinarily complex programming that far exceeds the basic _command_ vocabulary of other clockwork creatures. This allows clockwork overseers to store hundreds or even thousands of commands, which they can parse and sort quickly enough to simulate an intelligent creature’s adaptive thinking—at least regarding combat strategy and moderately complex tasks of coordinating construct laborers. These functions fall short of true thought, and clockwork overseers are incapable of language, emotion, higher thinking, or symbolic reasoning beyond specific sounds and statements they might parrot on _command_.
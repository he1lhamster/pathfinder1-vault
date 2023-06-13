---
cssclass: [monsters]
title1: Drekavac
desc_short: Dressed in graveyard rags, this pitiful creature cries out like a sick
  child. An oversized, bestial head perches atop its spindly, child-sized body, and
  its eyes are nothing but sunken pools of shadow with no trace of life in them. A
  cloying mist wreathes its frail form, accompanied by the stench of death and disease.
title2: Drekavac
CR: 3
sources:
- name: 'Pathfinder #31: Stolen Land'
  page: 78
  link: http://paizo.com/pathfinder/adventurePath/kingmaker/v5748btpy8dhc
XP: 800
alignment: NE
size: Small
type: undead
initiative:
  bonus: 1
senses:
  darkvision: 60
auras:
- name: unnatural aura
  radius: 30
AC:
  AC: 15
  touch: 12
  flat_footed: 14
  components:
    dex: 1
    natural: 3
    size: 1
HP:
  HP: 30
  long: 4d8+12
saves:
  fort: 4
  ref: 2
  will: 7
DR:
- amount: 5
  weakness: silver
immunities:
- undead traits
weaknesses:
- sunlight aversion
- vulnerability to magic
- vulnerability to salt
speeds:
  base: 20
attacks:
  melee:
  - - text: chilling grasp +5 touch (1d6 cold plus disease)
      entries:
      - - damage: 1d6
          type: cold
        - effect: disease
      attack: chilling grasp
      bonus:
      - 5
      touch: true
  - - text: shadow +5 touch (disease)
      entries:
      - - effect: disease
      attack: shadow
      bonus:
      - 5
      touch: true
  special:
  - create spawn
  - disease
  - diseased shadow
spell_like_abilities:
  entries:
  - name: gaseous form
    source: default
    freq: At will
  sources:
  - name: default
    CL: 5
    concentration: 8
ability_scores:
  STR: 10
  DEX: 12
  CON:
  INT: 9
  WIS: 12
  CHA: 17
BAB: 3
CMB: 2
CMD: 13
feats:
- name: Iron Will
- name: Weapon Finesse
skills:
  Intimidate: 10
  Perception: 8
  Stealth: 12
languages:
- Common
ecology:
  environment: any
  organization: solitary or pack (2-5)
  treasure_type: none
special_abilities:
  Create Spawn (Su): A child slain by a drekavac's disease has a 1-in- 6 chance of
    rising as another drekavac 3 days after death. The new drekavac is not in any
    way controlled by its maker, and is immediately capable of exercising its full
    powers, including creating spawn of its own. It does not possess any of the abilities
    it had in life.
  Disease (Su): |-
    Drekavacs are spirits of disease and contagion. While most drekavacs carry bubonic plague, drekavacs who died from other afflictions may carry those diseases instead. Any illness caused by a drekavac must be potentially fatal. Other diseases commonly carried include demon fever, filth fever, and slimy doom. If a drekavac is reduced to 0 hit points (from weapons or other sources, including channeled energy), all of the diseases it caused are cured, although the victims must recover from any effects normally, and slain victims are not restored.

    Bubonic plague: Touch-injury; save Fort DC 15; onset 1 day; frequency 1/day; effect 1d4 Con damage, 1 Cha damage, victim is fatigued; cure 2 consecutive saves.
  Diseased Shadow (Su): |-
    Any creature touched by a drekavac's shadow is also affected by the creature's disease ability. If there is a question about which way the drekavac's shadow falls, roll 1d8 to determine a random square around the creature. A character with a light source cannot be touched by the drekavac's shadow, but the light causes the shadow to fall directly opposite the character (unless there is another light source there as well). A drekavac can deliberately touch a creature with its shadow as a standard action by making a successful touch attack.

    A target missed by the drekavac's chilling grasp attack must make a DC 15 Reflex save to avoid being touched by the creature's shadow as well. This save DC is Charisma-based.
  Sunlight Aversion (Ex): Drekavacs hate natural sunlight and immediately flee from
    it. A drekavac caught in natural sunlight is staggered.
  Unnatural Aura (Su): Animals, wild or domesticated, can sense the unnatural presence
    of a drekavac at a distance of 30 feet. They do not willingly approach nearer
    than that and panic if forced to do so unless a master succeeds at a DC 25 Handle
    Animal, Ride, or wild empathy check. Panicked animals remain so as long as they
    are within 30 feet of the drekavac.
  Vulnerability to Magic (Ex): A remove curse or remove disease spell cast directly
    upon a drekavac (DC equal to the drekavac's disease ability) immediately destroys
    the creature, allowing the afflicted soul to move on. Destroying a drekavac with
    remove curse or remove disease does not cure any of the creature's diseases.
  Vulnerability to Salt (Ex): Drekavacs are vulnerable to salt that has been consecrated
    in the same fashion as holy water, and cannot cross an unbroken line of blessed
    salt. A handful of blessed salt thrown at a drekavac inflicts the same damage
    as a flask of holy water (Pathfinder RPG Core Rulebook 160).
desc_long: Drekavacs are the undead remains of children who perished from disease,
  particularly in plague-ridden areas where many such deaths occurred in a short period
  of time. Able to become as insubstantial as the mist rising from a graveyard on
  a cold, dark night, drekavacs are carriers of disease, seeking to infect the living
  with the afflictions that slew them. According to some stories, drekavacs only result
  from young plague victims who remain unburied or died bereft of the proper funeral
  rites; performing those rites may allow their spirits to rest and no longer haunt
  the world of the living.

---

# Drekavac
Dressed in graveyard rags, this pitiful creature cries out like a sick child. An oversized, bestial head perches atop its spindly, child-sized body, and its eyes are nothing but sunken pools of _[[items/Armor Magic Abilities/Shadow|shadow]]_ with no trace of life in them. A cloying mist wreathes its frail form, accompanied by the _[[universal monster rules/Stench|stench]]_ of death and disease.
**Source** Pathfinder #31: Stolen Land pg. 78
**XP** 800

NE Small undead
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +8
**Aura** _[[universal monster rules/Unnatural Aura|unnatural aura]]_ (30 ft.)

##### Defense

**AC** 15, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+1 Dex, +3 natural, +1 size)
**hp** 30 (4d8+12)
**Fort** +4, **Ref** +2, **Will** +7
**DR** 5/silver; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_
**Weaknesses** sunlight _[[spells/Aversion|aversion]]_, _[[curses/Vulnerability|vulnerability]]_ to magic, _vulnerability_ to salt

##### Offense
**Speed** 20 ft.
**Melee** chilling _[[spells/Grasp|grasp]]_ +5 touch (1d6 cold plus disease) or _shadow_ +5 touch (disease)
**Special Attacks** create spawn, disease, diseased _shadow_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +8)
At will - _[[spells/Gaseous Form|gaseous form]]_

##### Statistics
**Str** 10, **Dex** 12, **Con** —, **Int** 9, **Wis** 12, **Cha** 17
**Base Atk** +3; **CMB** +2; **CMD** 13
**Feats** _[[feats/Iron Will|Iron Will]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Intimidate +10, Perception +8, Stealth +12
**Languages** Common

##### Ecology

**Environment** any
**Organization** solitary or pack (2-5)
**Treasure** none

### Special Abilities

**Create Spawn (Su)** A child slain by a _[[monsters/Drekavac|drekavac]]_’s disease has a 1-in- 6 chance of rising as another _drekavac_ 3 days after death. The new _drekavac_ is not in any way controlled by its maker, and is immediately capable of exercising its full powers, including creating spawn of its own. It does not possess any of the abilities it had in life.

**Disease (Su)** Drekavacs are spirits of disease and _[[spells/Contagion|contagion]]_. While most drekavacs carry _[[diseases/Bubonic Plague|bubonic plague]]_, drekavacs who died from other afflictions may carry those diseases instead. Any illness caused by a _drekavac_ must be potentially fatal. Other diseases commonly carried include _[[diseases/Demon Fever|demon fever]]_, _[[diseases/Filth Fever|filth fever]]_, and _[[diseases/Slimy Doom|slimy doom]]_. If a _drekavac_ is reduced to 0 hit points (from weapons or other sources, including channeled energy), all of the diseases it caused are cured, although the victims must recover from any effects normally, and slain victims are not restored.

_Bubonic plague_: Touch—injury; save Fort DC 15; onset 1 day; frequency 1/day; effect 1d4 Con damage, 1 Cha damage, victim is _[[conditions/Fatigued|fatigued]]_; cure 2 consecutive saves.

**Diseased _Shadow_ (Su)** Any creature touched by a _drekavac_’s _shadow_ is also affected by the creature’s disease ability. If there is a question about which way the _drekavac_’s _shadow_ falls, roll 1d8 to determine a random square around the creature. A character with a light source cannot be touched by the _drekavac_’s _shadow_, but the light causes the _shadow_ to fall directly opposite the character (unless there is another light source there as well). A _drekavac_ can deliberately touch a creature with its _shadow_ as a standard action by making a successful touch attack.

A target missed by the _drekavac_’s chilling _grasp_ attack must make a DC 15 Reflex save to avoid being touched by the creature’s _shadow_ as well. This save DC is Charisma-based.
**Sunlight _Aversion_ (Ex)** Drekavacs hate natural sunlight and immediately flee from it. A _drekavac_ caught in natural sunlight is _[[conditions/Staggered|staggered]]_.

**_Unnatural Aura_ (Su)** Animals, wild or domesticated, can sense the unnatural presence of a _drekavac_ at a distance of 30 feet. They do not willingly approach nearer than that and panic if forced to do so unless a master succeeds at a DC 25 Handle Animal, Ride, or wild _[[feats/Empathy|empathy]]_ check. _[[conditions/Panicked|Panicked]]_ animals remain so as long as they are within 30 feet of the _drekavac_.

**_Vulnerability_ to Magic (Ex)** A _[[spells/Remove Curse|remove curse]]_ or _[[spells/Remove Disease|remove disease]]_ spell cast directly upon a _drekavac_ (DC equal to the _drekavac_’s disease ability) immediately destroys the creature, allowing the afflicted soul to move on. Destroying a _drekavac_ with _remove curse_ or _remove disease_ does not cure any of the creature’s diseases.

**_Vulnerability_ to Salt (Ex)** Drekavacs are vulnerable to salt that has been consecrated in the same fashion as _[[items/Mundane/Holy water|holy water]]_, and cannot cross an unbroken line of _[[feats/Blessed|blessed]]_ salt. A handful of _blessed_ salt thrown at a _drekavac_ inflicts the same damage as a _[[items/Mundane/Flask|flask]]_ of _holy water_ (Pathfinder RPG Core Rulebook 160).

##### Description

Drekavacs are the undead remains of children who perished from disease, particularly in plague-ridden areas where many such deaths occurred in a short period of time. Able to become as insubstantial as the mist rising from a graveyard on a cold, dark night, drekavacs are carriers of disease, seeking to infect the living with the afflictions that slew them. According to some stories, drekavacs only result from young plague victims who remain unburied or died bereft of the proper funeral rites; performing those rites may allow their spirits to rest and no longer haunt the world of the living.
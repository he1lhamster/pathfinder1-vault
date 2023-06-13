---
cssclass: [monsters]
title1: Sprite, Sprite Swarm
desc_short: 'Thousands of tiny, colorful winged humanoids crawl from every corner
  of the forest to form this buzzing, writhing swarm. '
title2: Sprite Swarm
CR: 5
sources:
- name: Fey Revisited
  page: 62
  link: http://paizo.com/products/btpy8xeb?Pathfinder-Campaign-Setting-Fey-Revisited
XP: 1600
alignment: CN
size: Diminutive
type: fey
subtypes:
- swarm
initiative:
  bonus: 7
senses:
  low-light vision: true
  detect evil: true
  detect good: true
AC:
  AC: 18
  touch: 18
  flat_footed: 14
  components:
    dex: 3
    dodge: 1
    size: 4
HP:
  HP: 45
  long: 10d6+10
saves:
  fort: 4
  ref: 10
  will: 7
defensive_abilities:
- swarm traits
DR:
- amount: 2
  weakness: cold iron
immunities:
- weapon damage
speeds:
  base: 15
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: swarm (2d6 plus distraction)
      entries:
      - - damage: 2d6
        - effect: distraction
      attack: swarm
  special:
  - angry glow
  - concentrated rush
  - distraction (DC 16)
space: 10
reach: 0
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: detect good
    source: default
    freq: Constant
  - superscripts:
    - UM
    name: mass daze
    source: default
    freq: 1/day
    DC: 14
  sources:
  - name: default
    CL: 5
    concentration: 5
ability_scores:
  STR: 3
  DEX: 17
  CON: 12
  INT: 6
  WIS: 11
  CHA: 10
BAB: 5
CMB:
CMD:
feats:
- name: Alertness
- name: Dodge
- name: Flyby Attack
- name: Improved Initiative
- name: Skill Focus (Perception)
skills:
  Fly: 30
  Intimidate: 10
  Perception: 14
  Sense Motive: 9
  Stealth: 28
languages:
- Common
- Sylvan
special_qualities:
- mob mentality
ecology:
  environment: temperate forests
  organization: solitary
  treasure_type: incidental
special_abilities:
  Angry Glow (Su): Once per minute, as a full-round action, the sprites that make
    up a sprite swarm may coordinate their luminous abilities to create a singular,
    searing glow. Creatures within 10 feet of a sprite swarm with line of sight must
    succeed at a DC 16 Fortitude save or be blinded for 1d4 rounds. A creature that
    succeeds at its save is dazzled for 1 round. The save DC is Constitution-based.
  Concentrated Rush (Ex): Once every 1d4 rounds, if more than one creature occupies
    a sprite swarm's space, the swarm may use its attack action to concentrate on
    one of these creatures to deal 4d6 points of damage in place of its normal swarm
    damage. Other creatures within the horde's space do not take swarm damage that
    round.
  Mob Mentality (Ex): As long as a sprite swarm has at least 10 hit points, it retains
    its Intelligence score and can act accordingly. Even so, it cannot be targeted
    by mind-affecting spells or effects that target a single creature. If its hit
    points fall below 10, the swarm is considered mindless as the individual creatures
    within begin to panic.
desc_long: |-
  When intruders threaten their beloved homes, sprite guards in large villages are taught to call for their fellow tribe members to form a vicious, enveloping swarm to drive back their enemies. Typically consisting of at least 5,000 sprites, these swarms are known for inf licting pain upon any creatures in their paths. Sprite swarms typically form only when the sprites' village is threatened by a large number of intruders or a single powerful foe; however, the malevolent sprites of Geb are quick to form swarms when faced with intrusion of any kind. 

  In some parts of Golarion where sprites are known to exist, those accused of crimes or other unacceptable behavior are sentenced to face a sprite swarm so that nature itself can judge them. If a sprite swarm forms to drive one of the accused away, he is guilty; if not, he is innocent. Most of those sent forth never return, having run afoul of the sprites' protective instincts, but occasionally the sprites allow someone they deem not a threat to live-quite independently of their actual guilt or innocence.

---

# Sprite, Sprite Swarm
Thousands of tiny, colorful winged humanoids crawl from every
corner of the forest to form this buzzing, writhing swarm.

**Source** Fey Revisited pg. 62
**XP** 1,600

CN Diminutive fey (swarm)
**Init** +7; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/Detect Evil|detect evil]]_, _[[spells/Detect Good|detect good]]_;
Perception +14

##### Defense

**AC** 18, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+3 Dex, +1 dodge, +4 size)
**hp** 45 (10d6+10)
**Fort** +4, **Ref** +10, **Will** +7
**Defensive Abilities** swarm traits
; **DR** 2/cold iron; **Immune** weapon damage

##### Offense
**Speed** 15 ft., fly 60 ft. (perfect)
**Melee** swarm (2d6 plus _[[universal monster rules/Distraction|distraction]]_)
**Space** 10 ft., **Reach** 0 ft.
**Special Attacks** angry glow, concentrated rush, _distraction_
(DC 16)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +5)
Constant—_detect evil_, _detect good_
1/day—mass _[[spells/Daze|daze]]_ (DC 14)

##### Statistics
**Str** 3, **Dex** 17, **Con** 12, **Int** 6, **Wis** 11, **Cha** 10
**Base Atk** +5; **CMB** —; **CMD** —
**Feats** _[[feats/Alertness|Alertness]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Initiative|Improved Initiative]]_, Skill
Focus (Perception)
**Skills** Fly +30, Intimidate +10, Perception +14, Sense Motive +9,
Stealth +28
**Languages** Common, Sylvan
**SQ** mob mentality

##### Ecology

**Environment** temperate forests
**Organization** solitary
**Treasure** incidental

### Special Abilities

**Angry Glow (Su)** Once per minute, as a full-round action,
the sprites that make up a _[[monsters/Sprite|sprite]]_ swarm may coordinate
their luminous abilities to create a singular, searing glow.
Creatures within 10 feet of a _sprite_ swarm with line of sight
must succeed at a DC 16 Fortitude save or be _[[conditions/Blinded|blinded]]_ for
 1d4 rounds. A creature that succeeds at its save is _[[conditions/Dazzled|dazzled]]_ for
 1 round. The save DC is Constitution-based.

**Concentrated Rush (Ex)** Once every 1d4 rounds, if more than
one creature occupies a _sprite_ swarm’s space, the swarm
may use its attack action to concentrate on one of these
creatures to deal 4d6 points of damage in place of its normal
swarm damage. Other creatures within the horde’s space do
not take swarm damage that round.

**Mob Mentality (Ex)** As long as a _sprite_ swarm has at least
 10 hit points, it retains its Intelligence score and can act
accordingly. Even so, it cannot be targeted by mind-affecting
spells or effects that target a single creature. If its hit points
fall below 10, the swarm is considered mindless as the
individual creatures within begin to panic.

##### Description

When intruders threaten their beloved homes, _sprite_
guards in large villages are taught to call for their fellow
tribe members to form a _[[items/Weapon Magic Abilities/Vicious|vicious]]_, enveloping swarm to
drive back their enemies. Typically consisting of at least
 5,000 sprites, these swarms are known for inf licting pain
upon any creatures in their paths. _Sprite_ swarms typically
form only when the sprites’ village is threatened by a large
number of intruders or a single powerful foe; however,
the _[[items/Armor Magic Abilities/Malevolent|malevolent]]_ sprites of Geb are quick to form swarms
when faced with intrusion of any kind.

In some parts of Golarion where sprites are
known to exist, those accused of crimes or other
unacceptable behavior are sentenced to face a _sprite_ swarm
so that nature itself can judge them. If a _sprite_ swarm
forms to drive one of the accused away, he is guilty; if
not, he is innocent. Most of those sent forth never return,
having run afoul of the sprites’ protective instincts, but
occasionally the sprites allow someone they deem not a
threat to live—quite independently of their actual guilt
or _[[spells/Innocence|innocence]]_.
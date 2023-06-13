---
cssclass: [monsters]
title1: Hunting Horror
desc_short: This vast draconic serpent has a pair of leathery wings that don't appear
  to be strong enough to allow the creature to fly.
title2: Hunting Horror
CR: 14
sources:
- name: 'Pathfinder #113: What Grows Within'
  page: 88
  link: http://paizo.com/products/btpy9qcl?Pathfinder-Adventure-Path-113-What-Grows-Within
XP: 38400
alignment: CE
size: Gargantuan
type: magical beast
initiative:
  bonus: 5
senses:
  darkvision: 60
  detect scrying: true
  low-light vision: true
  scent: true
  see in darkness: true
AC:
  AC: 29
  touch: 11
  flat_footed: 24
  components:
    dex: 5
    natural: 18
    size: -4
HP:
  HP: 202
  long: 15d10+120
  fast_healing: 10
saves:
  fort: 17
  ref: 14
  will: 11
defensive_abilities:
- freedom of movement
- no breath
DR:
- amount: 10
  weakness: magic and slashing
immunities:
- acid
- cold
SR: 25
weaknesses:
- light sensitivity
- susceptible to sunlight
speeds:
  base: 30
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: bite +23 (2d6+12)
      entries:
      - - damage: 2d6+12
      attack: bite
      bonus:
      - 23
    - text: tail slap +23 (2d8+12 plus grab)
      entries:
      - - damage: 2d8+12
        - effect: grab
      attack: tail slap
      bonus:
      - 23
    - text: 2 wings +21 (2d6+6)
      entries:
      - - damage: 2d6+6
      count: 2
      attack: wings
      bonus:
      - 21
  special:
  - constrict (2d8+18)
  - crush
  - squeezing coils
  - swallow whole (2d6+18 bludgeoning plus 6d6 acid damage, AC 19, 20 hp)
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: detect scrying
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: gaseous form
    source: default
    freq: At will
  - name: locate creature
    source: default
    freq: At will
  - name: locate object
    source: default
    freq: At will
  - name: telekinesis
    source: default
    freq: At will
    DC: 20
  - name: demand
    source: default
    freq: 3/day
    DC: 23
  - name: limited wish
    source: default
    freq: 3/day
    other: to duplicate sorcerer/wizard spells of 6th level or lower only
  - name: discern location
    source: default
    freq: 1/day
  - name: ethereal jaunt
    source: default
    freq: 1/day
  - name: scrying
    source: default
    freq: 1/day
    DC: 19
  - name: vision
    source: default
    freq: 1/day
  - name: interplanetary teleport
    source: default
    freq: 1/year
  sources:
  - name: default
    CL: 14
    concentration: 19
ability_scores:
  STR: 34
  DEX: 20
  CON: 27
  INT: 15
  WIS: 23
  CHA: 20
BAB: 15
CMB: 31
CMB_other: +33 bull rush
CMD: 46
CMD_other: 48 vs. bull rush
feats:
- name: Awesome Blow
- name: Combat Casting
- name: Combat Reflexes
- name: Flyby Attack
- name: Improved Bull Rush
- name: Multiattack
- name: Power Attack
- name: Snatch
skills:
  Fly: 20
  Knowledge (geography): 12
  Knowledge (local): 12
  Perception: 19
  Spellcraft: 20
  Survival: 27
  _racial_mods:
    Spellcraft:
      _: 8
    Survival:
      _: 8
languages:
- Aklo
- Common
- Draconic
special_qualities:
- answer beckoning
- contingency
- hunter
- manipulate magic
- powerful tail
ecology:
  environment: any
  organization: solitary, pair, or pack (3-6)
  treasure_type: standard
special_abilities:
  Answer Beckoning (Ex): Although a hunting horror is not an elemental or outsider,
    it can be conjured via gate, greater planar ally, or greater planar binding, provided
    the caster of the spell is a worshiper of one of the Great Old Ones or Outer Gods
    or specifically alters the words of the spell to invoke a hunting horror, and
    provided the spell is not cast in an area of direct sunlight. When invoking a
    hunting horror in this way, the spellcaster must succeed at a DC 30 Spellcraft
    check as part of the casting of the spell, or when the hunting horror arrives
    it is automatically free to act under its own will.
  Contingency: While the exact details of a particular hunting horror's contingency
    effect can vary wildly (as the monster has an immense range of potential spells
    to choose from due to its ability to manipulate magic), most settle for the simple
    but effective tactic of causing a greater invisibility spell to activate on the
    hunting horror as soon as it takes damage.
  Crush (Ex): A flying hunting horror can land on foes as a standard action, and then
    use its lengthy coils to crush them. This attack is effective only against creatures
    three or more size categories smaller than the hunting horror (Medium for most
    hunting horrors), and affects as many creatures as fit in the hunting horror's
    space. Any creature in the affected area must succeed at a DC 25 Reflex saving
    throw or be pinned, automatically taking 4d6+18 points of bludgeoning damage each
    round it is pinned. If the hunting horror chooses to maintain the pin, it must
    succeed at a combat maneuver check as normal. The save DC is Constitution-based.
  Hunter (Ex): Hunting horrors are efficient and talented at tracking prey, and Survival
    is a class skill for these creatures as a result. In addition, they gain a +8
    racial bonus on Survival checks. When a hunting horror succeeds at a Survival
    check to follow a creature's tracks, the hunting horror can declare that creature
    to be its prey. If there are multiple sets of tracks from a group of creatures
    traveling together, the hunting horror can choose which specific creature becomes
    its prey if it knows the target is among those in the group; otherwise, its chosen
    prey is determined randomly. The next time the hunting horror begins a battle
    against its prey, it gains a +10 bonus on its initiative check. In addition, its
    prey takes a -2 penalty on all saving throws against the hunting horror's spell-like
    abilities. A hunting horror can have only one creature as its designated prey
    at any one time, and if 24 hours pass without the hunting horror succeeding at
    a Survival check to follow that prey's trail, that creature ceases being the hunting
    horror's prey.
  Manipulate Magic (Sp): A hunting horror is gifted at manipulating magic to affect
    a wide range of spell-like abilities beyond those that it normally can access.
    In effect, this allows each hunting horror to use limited wish three times per
    day as a spell-like ability, but only to duplicate a sorcerer/wizard spell of
    6th level or lower. Hunting horrors typically use this ability to deal with foes
    who manage to stay at a distance, favoring potent attacks like chain lightning,
    disintegrate, and flesh to stone. Most save the third and final daily use for
    emergencies-teleport to escape from a battle gone unpredictably poorly, for example,
    or break enchantment or greater dispel magic to remove a debilitating effect.
    All hunting horrors use this ability to maintain a contingency effect on themselves
    as well.
  Powerful Tail (Ex): A hunting horror's tail slap is treated as a primary natural
    attack.
  Squeezing Coils (Ex): A creature that takes damage from a hunting horror's constrict
    ability after being struck by the hunting horror's tail slap attack must succeed
    at a DC 29 Fortitude saving throw or fall unconscious for 1d4 rounds. The save
    DC is Strength-based.
  Susceptible to Sunlight (Ex): While the glow of a distant star does not inconvenience
    a hunting horror, this creature cannot abide the light of a sun in relatively
    close proximity-including sunlight on a typical habitable planet such as Golarion.
    When in natural sunlight (but not in an area of daylight or similar spells), a
    hunting horror can't attack and is staggered. In sunlight, its fast healing ability
    doesn't function, it loses its damage reduction, and it takes 2d6 points of fire
    damage per round. In areas of natural sunlight, a hunting horror's light sensitivity
    increases to light blindness.
desc_long: |-
  Servitors of the Crawling Chaos Nyarlathotep, the serpentine hunting horrors excel at tracking and seeking prey, talents that often see them called on by cultists or spellcasters to hunt down enemies. They speak in great and powerful voices, when they deign to speak at all.

  A typical hunting horror is 60 feet long but weighs only 2 tons.

---

# Hunting Horror
This vast draconic serpent has a pair of leathery wings that don’t appear to be strong enough to allow the creature to fly.
**Source** Pathfinder #113: _[[spells/What Grows Within|What Grows Within]]_ pg. 88
**XP** 38,400
CE Gargantuan magical beast
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Scrying|detect scrying]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +19

##### Defense

**AC** 29, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+5 Dex, +18 natural, –4 size)
**hp** 202 (15d10+120); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +17, **Ref** +14, **Will** +11
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_, _[[universal monster rules/No Breath|no breath]]_; **DR** 10/magic and slashing; **Immune** acid, cold; **SR** 25
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_, susceptible to sunlight

##### Offense
**Speed** 30 ft., fly 60 ft. (perfect)
**Melee** bite +23 (2d6+12), tail slap +23 (2d8+12 plus _[[universal monster rules/Grab|grab]]_), 2 wings +21 (2d6+6)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (2d8+18), crush, squeezing coils, _[[universal monster rules/Swallow Whole|swallow whole]]_ (2d6+18 bludgeoning plus 6d6 acid damage, AC 19, 20 hp)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +19)
Constant—_detect scrying_, _freedom of movement_
At will—_[[spells/Gaseous Form|gaseous form]]_, _[[spells/Locate Creature|locate creature]]_, _[[spells/Locate Object|locate object]]_, _[[spells/Telekinesis|telekinesis]]_ (DC 20)
3/day—_[[spells/Demand|demand]]_ (DC 23), _[[spells/Limited Wish|limited wish]]_ (to duplicate sorcerer/wizard spells of 6th level or lower only)
1/day—_[[spells/Discern Location|discern location]]_, _[[spells/Ethereal Jaunt|ethereal jaunt]]_, _[[spells/Scrying|scrying]]_ (DC 19), _[[spells/Vision|vision]]_
1/year—_[[spells/Interplanetary Teleport|interplanetary teleport]]_

##### Statistics
**Str** 34, **Dex** 20, **Con** 27, **Int** 15, **Wis** 23, **Cha** 20
**Base Atk** +15; **CMB** +31 (+33 bull rush); **CMD** 46 (48 vs. bull rush)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Snatch|Snatch]]_
**Skills** Fly +20, Knowledge (geography) +12, Knowledge (local) +12, Perception +19, Spellcraft +20, Survival +27; **Racial Modifiers** +8 Spellcraft, +8 Survival
**Languages** Aklo, Common, Draconic
**SQ** answer beckoning, _[[spells/Contingency|contingency]]_, _[[classes/Hunter|hunter]]_, manipulate magic, powerful tail

##### Ecology

**Environment** any
**Organization** solitary, pair, or pack (3–6)
**Treasure** standard

### Special Abilities

**Answer Beckoning (Ex)** Although a _[[monsters/Hunting Horror|hunting horror]]_ is not an elemental or outsider, it can be conjured via _[[spells/Gate|gate]]_, greater _[[spells/Planar Ally|planar ally]]_, or greater _[[spells/Planar Binding|planar binding]]_, provided the caster of the spell is a worshiper of one of the Great Old Ones or Outer Gods or specifically alters the words of the spell to invoke a _hunting horror_, and provided the spell is not cast in an area of direct sunlight. When invoking a _hunting horror_ in this way, the spellcaster must succeed at a DC 30 Spellcraft check as part of the casting of the spell, or when the _hunting horror_ arrives it is automatically free to act under its own will.

**_Contingency_** While the exact details of a particular _hunting horror_’s _contingency_ effect can vary wildly (as the monster has an immense range of potential spells to choose from due to its ability to manipulate magic), most settle for the simple but effective tactic of causing a greater _[[spells/Invisibility|invisibility]]_ spell to activate on the _hunting horror_ as soon as it takes damage.

**Crush (Ex)** A flying _hunting horror_ can land on foes as a standard action, and then use its lengthy coils to crush them. This attack is effective only against creatures three or more size categories smaller than the _hunting horror_ (Medium for most hunting horrors), and affects as many creatures as fit in the _hunting horror_’s space. Any creature in the affected area must succeed at a DC 25 Reflex saving throw or be _[[conditions/Pinned|pinned]]_, automatically taking 4d6+18 points of bludgeoning damage each round it is _pinned_. If the _hunting horror_ chooses to maintain the pin, it must succeed at a combat maneuver check as normal. The save DC is Constitution-based.

**_Hunter_ (Ex)** Hunting horrors are efficient and talented at tracking prey, and Survival is a class skill for these creatures as a result. In addition, they gain a +8 racial bonus on Survival checks. When a _hunting horror_ succeeds at a Survival check to follow a creature’s tracks, the _hunting horror_ can declare that creature to be its prey. If there are multiple sets of tracks from a group of creatures traveling together, the _hunting horror_ can choose which specific creature becomes its prey if it knows the target is among those in the group; otherwise, its chosen prey is determined randomly. The next time the _hunting horror_ begins a battle against its prey, it gains a +10 bonus on its initiative check. In addition, its prey takes a –2 penalty on all saving throws against the _hunting horror_’s _spell-like abilities_. A _hunting horror_ can have only one creature as its designated prey at any one time, and if 24 hours pass without the _hunting horror_ succeeding at a Survival check to follow that prey’s trail, that creature ceases being the _hunting horror_’s prey.

**Manipulate Magic (Sp)** A _hunting horror_ is gifted at manipulating magic to affect a wide range of _spell-like abilities_ beyond those that it normally can access. In effect, this allows each _hunting horror_ to use _limited wish_ three times per day as a spell-like ability, but only to duplicate a sorcerer/wizard spell of 6th level or lower. Hunting horrors typically use this ability to deal with foes who manage to stay at a distance, favoring _[[items/Weapon Magic Abilities/Potent|potent]]_ attacks like _[[spells/Chain Lightning|chain lightning]]_, _[[spells/Disintegrate|disintegrate]]_, and _[[spells/Flesh to Stone|flesh to stone]]_. Most save the third and final daily use for emergencies—teleport to escape from a battle gone unpredictably poorly, for example, or _[[spells/Break Enchantment|break enchantment]]_ or greater _[[spells/Dispel Magic|dispel magic]]_ to remove a _[[items/Weapon Magic Abilities/Debilitating|debilitating]]_ effect. All hunting horrors use this ability to maintain a _contingency_ effect on themselves as well.

**Powerful Tail (Ex)** A _hunting horror_’s tail slap is treated as a primary natural attack.
**Squeezing Coils (Ex)** A creature that takes damage from a _hunting horror_’s _constrict_ ability after being struck by the _hunting horror_’s tail slap attack must succeed at a DC 29 Fortitude saving throw or fall _[[conditions/Unconscious|unconscious]]_ for 1d4 rounds. The save DC is Strength-based.
**Susceptible to Sunlight (Ex)** While the glow of a distant star does not inconvenience a _hunting horror_, this creature cannot abide the light of a sun in relatively close proximity—including sunlight on a typical habitable planet such as Golarion. When in natural sunlight (but not in an area of _[[spells/Daylight|daylight]]_ or similar spells), a _hunting horror_ can’t attack and is _[[conditions/Staggered|staggered]]_. In sunlight, its _fast healing_ ability doesn’t function, it loses its _[[universal monster rules/Damage Reduction|damage reduction]]_, and it takes 2d6 points of fire damage per round. In areas of natural sunlight, a _hunting horror_’s _light sensitivity_ increases to _[[universal monster rules/Light Blindness|light blindness]]_.

##### Description

Servitors of the Crawling Chaos Nyarlathotep, the serpentine hunting horrors excel at tracking and seeking prey, talents that often see them _[[items/Weapon Magic Abilities/Called|called]]_ on by cultists or spellcasters to hunt down enemies. They speak in great and powerful voices, when they deign to speak at all.

A typical _hunting horror_ is 60 feet long but weighs only 2 tons.
---
cssclass: [monsters]
title1: Cipactli
desc_short: This creature is covered in snapping jaws, from its massive, toothyhead
  to the various mouths that open in its body and tail.
title2: Cipactli
CR: 21
sources:
- name: Bestiary 6
  page: 56
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 409600
alignment: CN
size: Gargantuan
type: magical beast
subtypes:
- aquatic
initiative:
  bonus: 10
senses:
  darkvision: 180
  low-light vision: true
  scent: true
  tremorsense: 60
  true seeing: true
AC:
  AC: 37
  touch: 13
  flat_footed: 30
  components:
    dex: 6
    dodge: 1
    natural,-4 size: 24
HP:
  HP: 402
  long: 23d10+276
  regeneration: 20
  regeneration_weakness: special
saves:
  fort: 25
  ref: 19
  will: 18
  other: +8 vs. mind-affecting effects
DR:
- amount: 15
  weakness: cold iron and lawful
immunities:
- disease
- nonlethaldamage
- poison
resistances:
  acid: 20
  cold: 20
  electricity: 20
  fire: 20
SR: 32
speeds:
  base: 60
  other_semicolon: air walk
  swim: 60
attacks:
  melee:
  - - text: ravenous bite +30 (3d6+16/19-20 plus grab)
      entries:
      - - damage: 3d6+16
          crit_range: 19-20
        - effect: grab
      attack: ravenous bite
      bonus:
      - 30
    - text: 4 bites +30(2d6+11/19-20 plus grab)
      entries:
      - - damage: 2d6+11
          crit_range: 19-20
        - effect: grab
      count: 4
      attack: bites
      bonus:
      - 30
    - text: 2 claws +30 (2d6+11)
      entries:
      - - damage: 2d6+11
      count: 2
      attack: claws
      bonus:
      - 30
  special:
  - devour
  - fast swallow
  - frightening roar
  - grab(Colossal)
  - pounce
  - ravenous bite
  - swallow whole (see below,AC 22, 40 hp)
  - trample (2d8+16 plus grab, DC 32)
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: mind blank
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: control water
    source: default
    freq: At will
  - name: control weather
    source: default
    freq: At will
  - name: transmute rock to mud
    source: default
    freq: At will
  - name: horrid wilting
    source: default
    freq: 3/day
    DC: 26
  - name: incendiary cloud
    source: default
    freq: 3/day
    DC: 26
  - name: meteor swarm
    source: default
    freq: 3/day
    DC: 27
  - name: polar ray
    source: default
    freq: 3/day
  - name: vision
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 20
    concentration: 28
ability_scores:
  STR: 32
  DEX: 23
  CON: 34
  INT: 19
  WIS: 28
  CHA: 27
BAB: 23
CMB: 38
CMD: 55
feats:
- name: Combat Reflexes
- name: Critical Focus
- name: Dodge
- name: Greater Vital Strike
- name: Improved Critical (bite)
- name: Improved Critical (ravenous bite)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Iron Will
- name: Power Attack
- name: StaggeringCritical
- name: Vital Strike
skills:
  Climb: 37
  Intimidate: 31
  Knowledge (nature): 27
  Perception: 35
  Stealth: 20
    underwater: 28
  Swim: 45
  _racial_mods:
    Stealth:
      underwater: 8
languages:
- Aquan
- Common
- Draconic
- Terran
special_qualities:
- amphibious
- destructive
- hibernation
ecology:
  environment: any water
  organization: solitary
  treasure_type: standard
special_abilities:
  Devour (Su): Any time a cipactli kills or destroys a creature with its swallow whole
    ability, it gains a number of temporary hit points equal to 5 × the slain creature's
    Hit Dice.
  Destructive (Ex): A cipactli's natural attacks are treated as adamantine for the
    purpose of damaging objects.
  Frightening Roar (Su): As a standard action, a cipactli can bellow out a terrible,
    deafening roar. All creatures within 300 feet must succeed at a DC 33 Fortitude
    save or be permanently deafened and panicked for 1d4+4 rounds. Creatures that
    successfully save against this effect are instead shaken for 1d4+4 rounds. This
    is a sonic effect; the panicked and shaken effects are sonic mind-affecting fear
    effects. The save DC is Constitution-based.
  Hibernation (Ex): A cipactli can enter a state of hibernation at will as long as
    it is submerged underwater. Doing so takes 1 minute. While in this state, it can
    take no actions and is effectively helpless, as if it were in a deep sleep. It
    can remain in hibernation for as long as it wishes. While in this state, it does
    not need to eat or drink, nor does it age. If it is damaged while hibernating,
    it awakens immediately but must succeed at a DC 25 Will save to avoid being staggered
    for 1d6 rounds.
  Ravenous Bite (Ex): A cipactli adds 1-1/2 times its Strength bonus to the damage
    from its primary bite attack.
  Regeneration (Ex): A cipactli's regeneration can be suppressed by damage from mythic
    sources or by a critical hit from an effect that deals negative energy damage.
    Alternately, any amount of negative energy damage dealt to the cipactli's stomach
    from a swallowed creature suppresses its regeneration. A cipactli can regurgitate
    any number of creatures from its stomach as a move action.
  Swallow Whole (Su): |-
    A creature swallowed by a cipactli not only takes 20d6 points of bludgeoning, slashing, and piercing damage as the creature's mouth-lined gullet consumes its body, but also suffers an additional effect depending on the cipactli's dedicated focus (as listed below) each round. The save DCs for the following abilities are Constitution-based. 

    Consume Artistry: A cipactli created for the purpose of devouring the creations of mortals damages its victims' armor and weapons and any items it swallows. A cipactli can attempt a sunder combat maneuver check against one piece of equipment that each swallowed creature has as a free action that deals 3d6+12 points of damage. A construct swallowed by this type of cipactli takes 6d6 points of damage in addition to the 20d6 points of damage normally caused by the swallow whole ability. 

    Consume Clarity: A cipactli created for the purpose of consuming clarity causes its victims to experience distracting and confusing thoughts while imprisoned in its stomach. A swallowed creature must succeed at a DC 33 Will save or be confused for 1d4 rounds. A creature affected by this confusion effect adds 10 to its roll when determining the effects of the confusion effect. This is a mind-affecting effect. 

    Consume Grace: A cipactli created for the purpose of devouring grace causes its victims to become clumsy and careless. A swallowed creature must succeed at a DC 33 Fortitude save or take 1d6 points of Dexterity drain. Affected creatures also take a -4 penalty on Reflex saves for 1d3 days. This penalty on Reflex saves is a curse effect 

    Consume Lore: A cipactli created for the purpose of devouring lore strips knowledge from its victims. A swallowed creature must succeed at a DC 33 Will save or take 1d6 points of Intelligence drain. In addition, each round the creature is swallowed, it forgets up to 30 minutes of its memories as per modify memory. This experience typically results in erasing the strongest memories first, such as recently considered facts about the victim's current goals or precious formative memories. 

    Consume Rule: A cipactli created for the purpose of consuming the organizing principle of rule causes its victims to suffer feelings of worthlessness and incompetence. A swallowed creature must succeed at a DC 33 Will save or take 1d4 points of Wisdom drain and 1d4 points of Charisma drain. 

    Consume Valor: A cipactli created for devouring bravery causes its victims to suffer paralyzing fear. A swallowed creature must succeed at a DC 33 Will save or cower in fear for 1d4 rounds. This is a mind-affecting fear effect. 

    Consume Vitality: A cipactli created for the purpose of consuming vitality saps its victims of their strength and vigor. A swallowed creature must succeed at a DC 33 Fortitude save or take 1d4 points of Strength drain and 1d4 points of Constitution drain.
  Trample (Ex): When a cipactli deals damage to a foe with its trample special attack,
    it can immediately attempt to grapple the trampled foe with a -20 penalty on its
    combat maneuver check. If it succeeds at this check, it can immediately swallow
    the trampled creature whole.
desc_long: |-
  Ravenous forces of destruction, cipactlis are created by the gods to scour worlds of specific mortal qualities. It is believed that primal and destructive forces of nature spawned the first cipactli, and that it was wrought upon the world as an insatiable agent of annihilation. Stories claim that the gods saw fault in this creation and set a trap to destroy the first and most powerful cipactli, but such legends suggest that this destruction wasn't complete. Either the gods' methods were flawed or other divinities learned how to create new cipactlis, for now these beasts have spread throughout multiple worlds. 

  These monsters are individual creations of the gods and voracious devourers of particular elements of the universe. All cipactlis are attuned to certain aspects of their worlds, and when not slumbering in wait, they tear through mortal civilizations in a swath of destructive feasting. Thankfully, these creatures are extremely rare. 

  Essentially ageless, many a cipactli has been defeated by great heroes, only to have a portion of its body sink below the waters and regenerate. After such a defeat, a cipactli often goes into a state of hibernation that can last for centuries. 

  Though they are destructive creatures, they have immense knowledge of the world. Those who can calm them may learn secrets about the universe to which most mortals are not normally privy. 

  A cipactli is 50 feet long and weighs 18,000 pounds.

---

# Cipactli
This creature is covered in _[[feats/Snapping Jaws|snapping jaws]]_, from its massive, toothy

head to the various mouths that open in its body and tail.
**Source** Bestiary 6 pg. 56
**XP** 409,600

CN Gargantuan magical beast (aquatic)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 180 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_,

_[[universal monster rules/Tremorsense|tremorsense]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +35

##### Defense

**AC** 37, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+6 Dex, +1 dodge, +24 natural,

–4 size)
**hp** 402 (23d10+276); _[[universal monster rules/Regeneration|regeneration]]_ 20 (special)
**Fort** +25, **Ref** +19, **Will** +18; +8 vs. mind-affecting effects
**DR** 15/cold iron and lawful; **Immune** disease, nonlethal

damage, poison; **Resist** acid 20, cold 20, electricity 20,

fire 20; **SR** 32

##### Offense
**Speed** 60 ft., swim 60 ft.; _[[spells/Air Walk|air walk]]_
**Melee** _[[curses/Ravenous|ravenous]]_ bite +30 (3d6+16/19–20 plus _[[universal monster rules/Grab|grab]]_), 4 bites +30

(2d6+11/19–20 plus _grab_), 2 claws +30 (2d6+11)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** devour, _[[universal monster rules/Fast Swallow|fast swallow]]_, frightening roar, _grab_

(Colossal), _[[universal monster rules/Pounce|pounce]]_, _ravenous_ bite, _[[universal monster rules/Swallow Whole|swallow whole]]_ (see below,

AC 22, 40 hp), _[[universal monster rules/Trample|trample]]_ (2d8+16 plus _grab_, DC 32)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +28)
Constant—_air walk_, _[[spells/Mind Blank|mind blank]]_, _true seeing_ 
At will—_[[spells/Control Water|control water]]_, _[[spells/Control Weather|control weather]]_, _[[spells/Transmute Rock to Mud|transmute rock to mud]]_ 
3/day—_[[spells/Horrid Wilting|horrid wilting]]_ (DC 26), _[[spells/Incendiary Cloud|incendiary cloud]]_ (DC 26), _[[spells/Meteor Swarm|meteor swarm]]_ (DC 27), _[[spells/Polar Ray|polar ray]]_, _[[spells/Vision|vision]]_

##### Statistics
**Str** 32, **Dex** 23, **Con** 34, **Int** 19, **Wis** 28, **Cha** 27
**Base Atk** +23; **CMB** +38; **CMD** 55
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite, _ravenous_ bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, Staggering

Critical, _[[feats/Vital Strike|Vital Strike]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +37, Intimidate +31, Knowledge (nature) +27,

Perception +35, Stealth +20 (+28 _[[items/Weapon Magic Abilities/Underwater|underwater]]_), Swim +45;

**Racial Modifiers** +8 Stealth _underwater_
**Languages** Aquan, Common, Draconic, Terran
**SQ** _[[universal monster rules/Amphibious|amphibious]]_, destructive, hibernation

##### Ecology

**Environment** any water
**Organization** solitary
**Treasure** standard

### Special Abilities

**Devour (Su)** Any time a _[[monsters/Cipactli|cipactli]]_ kills or destroys a creature with its _swallow whole_ ability, it gains a number of temporary hit points equal to 5 × the slain creature's Hit Dice.

**Destructive (Ex)** A _cipactli_'s _[[universal monster rules/Natural Attacks|natural attacks]]_ are treated as adamantine for the purpose of damaging objects.

**Frightening Roar (Su)** As a standard action, a _cipactli_ can bellow out a terrible, deafening roar. All creatures within 300 feet must succeed at a DC 33 Fortitude save or be permanently _[[conditions/Deafened|deafened]]_ and _[[conditions/Panicked|panicked]]_ for 1d4+4 rounds. Creatures that successfully save against this effect are instead _[[conditions/Shaken|shaken]]_ for 1d4+4 rounds. This is a sonic effect; the _panicked_ and _shaken_ effects are sonic mind-affecting _[[universal monster rules/Fear|fear]]_ effects. The save DC is Constitution-based.

**Hibernation (Ex)** A _cipactli_ can enter a state of hibernation at will as long as it is submerged _underwater_. Doing so takes 1 minute. While in this state, it can take no actions and is effectively _[[conditions/Helpless|helpless]]_, as if it were in a deep sleep. It can remain in hibernation for as long as it wishes. While in this state, it does not need to eat or drink, nor does it age. If it is damaged while hibernating, it awakens immediately but must succeed at a DC 25 Will save to avoid being _[[conditions/Staggered|staggered]]_ for 1d6 rounds.

**_Ravenous_ Bite (Ex)** A _cipactli_ adds 1-1/2 times its Strength bonus to the damage from its primary bite attack.

**_Regeneration_ (Ex)** A _cipactli_'s _regeneration_ can be suppressed by damage from mythic sources or by a critical hit from an effect that deals negative energy damage. Alternately, any amount of negative energy damage dealt to the _cipactli_'s stomach from a swallowed creature suppresses its _regeneration_. A _cipactli_ can regurgitate any number of creatures from its stomach as a move action.
**_Swallow Whole_ (Su)** A creature swallowed by a _cipactli_ not only takes 20d6 points of bludgeoning, slashing, and piercing damage as the creature's mouth-lined gullet consumes its body, but also suffers an additional effect depending on the _cipactli_'s dedicated focus (as listed below) each round. The save DCs for the following abilities are Constitution-based.

Consume Artistry: A _cipactli_ created for the purpose of devouring the creations of mortals damages its victims' armor and weapons and any items it swallows. A _cipactli_ can attempt a sunder combat maneuver check against one piece of equipment that each swallowed creature has as a free action that deals 3d6+12 points of damage. A construct swallowed by this type of _cipactli_ takes 6d6 points of damage in addition to the 20d6 points of damage normally caused by the _swallow whole_ ability.

Consume _[[items/Weapon/Clarity|Clarity]]_: A _cipactli_ created for the purpose of consuming _clarity_ causes its victims to experience _[[items/Weapon Magic Abilities/Distracting|distracting]]_ and confusing thoughts while imprisoned in its stomach. A swallowed creature must succeed at a DC 33 Will save or be _[[conditions/Confused|confused]]_ for 1d4 rounds. A creature affected by this _[[spells/Confusion|confusion]]_ effect adds 10 to its roll when determining the effects of the _confusion_ effect. This is a mind-affecting effect.

Consume _[[spells/Grace|Grace]]_: A _cipactli_ created for the purpose of devouring _grace_ causes its victims to become clumsy and careless. A swallowed creature must succeed at a DC 33 Fortitude save or take 1d6 points of Dexterity drain. Affected creatures also take a –4 penalty on Reflex saves for 1d3 days. This penalty on Reflex saves is a curse effect

Consume Lore: A _cipactli_ created for the purpose of devouring lore strips knowledge from its victims. A swallowed creature must succeed at a DC 33 Will save or take 1d6 points of Intelligence drain. In addition, each round the creature is swallowed, it forgets up to 30 minutes of its memories as per _[[spells/Modify Memory|modify memory]]_. This experience typically results in erasing the strongest memories first, such as recently considered facts about the victim's current goals or precious formative memories.

Consume Rule: A _cipactli_ created for the purpose of consuming the organizing principle of rule causes its victims to suffer feelings of worthlessness and incompetence. A swallowed creature must succeed at a DC 33 Will save or take 1d4 points of Wisdom drain and 1d4 points of Charisma drain.

Consume Valor: A _cipactli_ created for devouring bravery causes its victims to suffer paralyzing _fear_. A swallowed creature must succeed at a DC 33 Will save or cower in _fear_ for 1d4 rounds. This is a mind-affecting _fear_ effect.

Consume Vitality: A _cipactli_ created for the purpose of consuming vitality saps its victims of their strength and _[[spells/Vigor|vigor]]_. A swallowed creature must succeed at a DC 33 Fortitude save or take 1d4 points of Strength drain and 1d4 points of Constitution drain.

**_Trample_ (Ex)** When a _cipactli_ deals damage to a foe with its _trample_ special attack, it can immediately attempt to grapple the trampled foe with a –20 penalty on its combat maneuver check. If it succeeds at this check, it can immediately swallow the trampled creature whole.

##### Description

_Ravenous_ forces of _[[spells/Destruction|destruction]]_, cipactlis are created by the gods to scour worlds of specific mortal qualities. It is believed that primal and destructive forces of nature spawned the first _cipactli_, and that it was wrought upon the world as an insatiable agent of annihilation. Stories claim that the gods _[[items/Mundane/Saw|saw]]_ fault in this creation and set a trap to destroy the first and most powerful _cipactli_, but such legends suggest that this _destruction_ wasn’t complete. Either the gods’ methods were flawed or other divinities learned how to create new cipactlis, for now these beasts have spread throughout multiple worlds.

These monsters are individual creations of the gods and voracious devourers of particular elements of the universe. All cipactlis are attuned to certain aspects of their worlds, and when not slumbering in wait, they tear through mortal civilizations in a swath of destructive feasting. Thankfully, these creatures are extremely rare.

Essentially ageless, many a _cipactli_ has been defeated by great heroes, only to have a portion of its body sink below the waters and _[[spells/Regenerate|regenerate]]_. After such a defeat, a _cipactli_ often goes into a state of hibernation that can last for centuries.

Though they are destructive creatures, they have immense knowledge of the world. Those who can calm them may learn secrets about the universe to which most mortals are not normally privy.

A _cipactli_ is 50 feet long and weighs 18,000 pounds.
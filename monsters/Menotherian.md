---
cssclass: [monsters]
title1: Menotherian
is_3.5: true
desc_short: This bear-sized creature looks like a gangly black wasp. Its wings are
  large and delicate, and fine hairs cover its joints and feet. Its front-most legs
  end in graceful articulate hands, and its jagged abdomen terminates in a wicked
  pair of stingers as long as a man's arm. Though its alien face has no human-like
  expression, intelligence gleams in its eyes.
title2: Menotherian
CR: 15
sources:
- name: 'Pathfinder #17: A Memory of Darkness'
  page: 86
  link: http://paizo.com/pathfinder/adventurePath/secondDarkness/v5748btpy86j6
alignment: Always CN
size: Large
type: outsider
subtypes:
- chaotic
- elf
- extraplanar
- shapechanger
initiative:
  bonus: 9
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 33
  touch: 14
  flat_footed: 28
  components:
    dex: 5
    natural: 19
    size: -1
HP:
  HP: 189
  long: 14d8+126
saves:
  fort: 17
  ref: 16
  will: 13
DR:
- amount: 15
  weakness: lawful
immunities:
- disease
- poison
resistances:
  electricity: 10
  fire: 10
SR: 30
speeds:
  base: 50
  climb: 20
  fly: 50
  fly_maneuverability: poor
attacks:
  melee:
  - - text: sting +22 (2d10+9 plus poison)
      entries:
      - - damage: 2d10+9
        - effect: poison
      attack: sting
      bonus:
      - 22
    - text: 2 claws +20 (1d4+4)
      entries:
      - - damage: 1d4+4
      count: 2
      attack: claws
      bonus:
      - 20
    - text: bite +20 (1d8+4)
      entries:
      - - damage: 1d8+4
      attack: bite
      bonus:
      - 20
  special:
  - alluring scent
  - mind control
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: dimension door
    source: default
    freq: At will
  - name: dispel magic
    source: default
    freq: At will
  - name: lover's vengeance
    source: default
    freq: At will
    DC: 18
    other: see page 62
  - name: message
    source: default
    freq: At will
  - name: neutralize poison
    source: default
    freq: At will
  - name: rage
    source: default
    freq: At will
  - name: secret speech
    source: default
    freq: At will
    DC: 17
    other: see page 62
  - name: crushing despair
    source: default
    freq: 5/day
    DC: 19
  - name: cat's grace
    source: default
    freq: 5/day
  - name: cure moderate wounds
    source: default
    freq: 5/day
    DC: 17
  - name: remove disease
    source: default
    freq: 5/day
  - name: suggestion
    source: default
    freq: 5/day
    DC: 18
  - name: summon swarm
    source: default
    freq: 5/day
  - name: telekinesis
    source: default
    freq: 5/day
  - name: teleport
    source: default
    freq: 5/day
  - name: wall of thorns
    source: default
    freq: 5/day
  - name: heal
    source: default
    freq: 1/day
    DC: 21
  - name: insect plague
    source: default
    freq: 1/day
  - name: scrying
    source: default
    freq: 1/day
    DC: 19
  sources:
  - name: default
    CL: 14
ability_scores:
  STR: 28
  DEX: 20
  CON: 28
  INT: 18
  WIS: 18
  CHA: 20
BAB: 14
grapple_3.5: 27
feats:
- name: Combat Reflexes
- name: Improved Initiative
- name: Lightning Reflexes
- name: Multiattack
- name: Power Attack
skills:
  Balance: 15
  Bluff: 22
  Climb: 14
  Concentration: 18
  Diplomacy: 26
  Gather Information: 10
  Heal: 14
  Intimidation: 24
  Jump: 26
  Knowledge (history): 9
  Knowledge (nature): 14
  Knowledge (the planes): 14
  Listen: 23
  Move Silently: 15
  Perform (dance): 10
  Sense Motive: 21
  Spellcraft: 14
  Spot: 23
languages:
- Abyssal
- Common
- Elven
special_qualities:
- telepathy 100 ft.
ecology:
  environment: any
  organization: solitary
  treasure_type: standard
  advancement_3.5:
  - type: size
    HD_min: 15
    size: Large
    HD_max: 20
  - type: size
    HD_min: 21
    size: Huge
    HD_max: 42
special_abilities:
  Alluring Scent (Ex): The Menotherian constantly exudes intoxicating pheromones that
    cause creatures in her vicinity to grow relaxed and react favorably toward her.
    Any creature within 30 feet of her must make a DC 26 Fortitude save or adjust
    its attitude one step closer to friendly; the creature makes a save on the first
    round of exposure and every minute thereafter. Creatures with the scent ability
    take a -4 penalty on their saving throws. The Menotherian prefers to let this
    ability take effect before trying to negotiate with others, though it works even
    in combat (in long-term battles, opponents have been known to ask to parlay with
    her after sufficient exposure). A creature ceases to attack her once its attitude
    shifts away from hostile (but if she attacks it again, its attitude resets to
    hostile). This is a mind-affecting poison effect. The save DC is Constitution-based.
  Alternate Form (Su): The Menotherian can change into her elf-like form or back again
    at will as a move-equivalent action. In her elf form she cannot use her natural
    attacks, implant swarms, or mind control, but can still use her spell-like abilities
    and alluring scent. She can also take the form of a giant wasp or a normal wasp,
    though she normally only uses these shapes as disguises rather than for battle.
  Implant Swarm (Ex): Once per day as a standard action, the Menotherian can use her
    stinger to implant a cluster of eggs in a target. The affected creature must make
    a DC 26 Fort save to avoid implantation; this DC is Constitution-based. The eggs
    gestate in 2d4 rounds, during which the target is nauseated. When the gestation
    period ends, the eggs hatch into a chaotic neutral hellwasp swarm with a hive
    mind. The swarm swiftly consumes the victim's innards, killing the host immediately,
    then inhabits and animates the body as a zombie-like creature. A remove disease
    spell rids a victim of the eggs during the gestation period, as does a DC 30 Heal
    check made as a fullround action that provokes attacks of opportunity.
  Mind Control (Su): The Menotherian can inject a concentrated form of its alluring
    scent directly into the brain of a helpless or willing humanoid creature. If the
    creature fails a DC 26 Fortitude save, the herald can control the target for the
    next 24 hours as if using dominate person, though the Menotherian must verbally
    give the target instructions.
  Poison (Su): Injury, Fortitude DC 26, initial damage 2d6 Dex, secondary damage 1d6
    Dex. The save DC is Constitution-based.
desc_long: |-
  The Menotherian is a personification of lust, vengeance, and trickery. She is the chief immortal agent of Calistria in the mortal world-bereft of morals, she seduces, tricks, or murders any creature necessary to complete her mission. In her true form she is a great wasp-like creature weighing just over 1,400 pounds. Though she can fly, her wings create a loud buzzing noise audible from over 500 feet away, so when she must be stealthy she walks or climbs. The Menotherian needs no armor, for her exoskeleton is as hard as adamantine. She observes her environment with an alien detachment, missing no detail but only acting when she feels the time is right.

   When subtlety is necessary, she can take the shape of an exotic elf of either gender, a giant wasp, or a normal wasp. Her humanoid form is almost a caricature of elven beauty, with long ears, narrow cheekbones, and long graceful limbs-if elves look more elven than half-elves, the Menotherian looks even more elven than true elves, as if elves are near-perfect mortal copies of the “true” elven ideal. In this form she lacks most of her combat ability, but can still seduce with her wits and good looks, or even use her pheromones on reluctant targets. The Book of Joy refers to hundreds of transparent, sealed chambers in Calistria's palace, each containing a sleeping creature resembling the Menotherian's elven form; the goddess awakens one of these any time she needs a new herald or wants to create another one of her succubus-like avengers.

---

# Menotherian
This bear-sized creature looks like a gangly black wasp. Its wings are large and delicate, and fine hairs cover its joints and feet. Its front-most legs end in graceful articulate hands, and its jagged abdomen terminates in a wicked pair of stingers as long as a man’s arm. Though its alien face has no human-like expression, intelligence gleams in its eyes.
**Source** Pathfinder #17: A Memory of _[[spells/Darkness|Darkness]]_ pg. 86
Always CN Large outsider (chaotic, elf, extraplanar, shapechanger)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Listen +23, Spot +23

##### Defense

**AC** 33, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+5 Dex, +19 natural, -1 size)
**hp** 189 (14d8+126)
**Fort** +17, **Ref** +16, **Will** +13
**DR** 15/lawful; **Immune** disease, poison; **Resist** electricity 10, fire 10; **SR** 30

##### Offense
**Speed** 50 ft., _[[universal monster rules/Climb|climb]]_ 20 ft., fly 50 ft. (poor)
**Melee** sting +22 (2d10+9 plus poison) and 2 claws +20 (1d4+4) and bite +20 (1d8+4)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** alluring _scent_, mind control
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th)
At will — _[[spells/Dimension Door|dimension door]]_, _[[spells/Dispel Magic|dispel magic]]_, lover’s _[[feats/Vengeance|vengeance]]_ (DC 18, see page 62), _[[spells/Message|message]]_, _[[spells/Neutralize Poison|neutralize poison]]_, _[[spells/Rage|rage]]_, _[[spells/Secret Speech|secret speech]]_ (DC 17, see page 62)
5/day — _[[spells/Crushing Despair|crushing despair]]_ (DC 19), cat’s _[[spells/Grace|grace]]_, _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (DC 17), _[[spells/Remove Disease|remove disease]]_, _[[spells/Suggestion|suggestion]]_ (DC 18), _[[spells/Summon Swarm|summon swarm]]_, _[[spells/Telekinesis|telekinesis]]_, teleport, _[[spells/Wall Of Thorns|wall of thorns]]_
1/day — _[[spells/Heal|heal]]_ (DC 21), _[[spells/Insect Plague|insect plague]]_, _[[spells/Scrying|scrying]]_ (DC 19)

##### Statistics
**Str** 28, **Dex** 20, **Con** 28, **Int** 18, **Wis** 18, **Cha** 20
**Base Atk** +14; **Grapple** +27
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Balance +15, Bluff +22, _Climb_ +14, Concentration +18, Diplomacy +26, Gather Information +10, _Heal_ +14, Intimidate +24, _[[spells/Jump|Jump]]_ +26, Knowledge (history) +9, Knowledge (nature) +14, Knowledge (the planes) +14, Listen +21, Move Silently +15, Perform (dance) +10, Sense Motive +21, Spellcraft +14, Spot +21
**Languages** Abyssal, Common, Elven
**SQ** _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** standard
**Advancement** 15-20 HD (Large), 21-42 HD (Huge)

### Special Abilities

**Alluring _Scent_ (Ex)** The _[[monsters/Menotherian|Menotherian]]_ constantly exudes intoxicating pheromones that cause creatures in her vicinity to grow relaxed and react favorably toward her. Any creature within 30 feet of her must make a DC 26 Fortitude save or adjust its attitude one step closer to friendly; the creature makes a save on the first round of exposure and every minute thereafter. Creatures with the _scent_ ability take a –4 penalty on their saving throws. The _Menotherian_ prefers to let this ability take effect before trying to negotiate with others, though it works even in combat (in long-term battles, opponents have been known to ask to parlay with her after sufficient exposure). A creature ceases to attack her once its attitude shifts away from hostile (but if she attacks it again, its attitude resets to hostile). This is a mind-affecting poison effect. The save DC is Constitution-based.

**Alternate Form (Su)** The _Menotherian_ can change into her elf-like form or back again at will as a move-equivalent action. In her elf form she cannot use her _[[universal monster rules/Natural Attacks|natural attacks]]_, implant swarms, or mind control, but can still use her _spell-like abilities_ and alluring _scent_. She can also take the form of a giant wasp or a normal wasp, though she normally only uses these shapes as disguises rather than for battle.

**Implant Swarm (Ex)** Once per day as a standard action, the _Menotherian_ can use her stinger to implant a cluster of eggs in a target. The affected creature must make a DC 26 Fort save to avoid implantation; this DC is Constitution-based. The eggs gestate in 2d4 rounds, during which the target is _[[conditions/Nauseated|nauseated]]_. When the gestation period ends, the eggs hatch into a chaotic neutral _[[monsters/Hellwasp Swarm|hellwasp swarm]]_ with a hive mind. The swarm swiftly consumes the victim’s innards, killing the host immediately, then inhabits and animates the body as a zombie-like creature. A _remove disease_ spell rids a victim of the eggs during the gestation period, as does a DC 30 _Heal_ check made as a fullround action that provokes attacks of opportunity.

**Mind Control (Su)** The _Menotherian_ can inject a concentrated form of its alluring _scent_ directly into the brain of a _[[conditions/Helpless|helpless]]_ or willing humanoid creature. If the creature fails a DC 26 Fortitude save, the herald can control the target for the next 24 hours as if using _[[spells/Dominate Person|dominate person]]_, though the _Menotherian_ must verbally give the target instructions.

**Poison (Su)** Injury, Fortitude DC 26, initial damage 2d6 Dex, secondary damage 1d6 Dex. The save DC is Constitution-based.

##### Description

The _Menotherian_ is a personification of lust, _vengeance_, and trickery. She is the chief immortal agent of Calistria in the mortal world—bereft of morals, she seduces, tricks, or murders any creature necessary to complete her mission. In her _[[spells/True Form|true form]]_ she is a great wasp-like creature weighing just over 1,400 pounds. Though she can fly, her wings create a loud buzzing noise audible from over 500 feet away, so when she must be _[[feats/Stealthy|stealthy]]_ she walks or climbs. The _Menotherian_ needs no armor, for her exoskeleton is as hard as adamantine. She observes her environment with an alien detachment, missing no detail but only acting when she feels the time is right.

When subtlety is necessary, she can take the shape of an exotic elf of either gender, a giant wasp, or a normal wasp. Her humanoid form is almost a caricature of elven beauty, with long ears, narrow cheekbones, and long graceful limbs—if elves look more elven than half-elves, the _Menotherian_ looks even more elven than true elves, as if elves are near-perfect mortal copies of the “true” elven ideal. In this form she lacks most of her combat ability, but can still seduce with her wits and good looks, or even use her pheromones on reluctant targets. The Book of Joy refers to hundreds of transparent, sealed chambers in Calistria’s palace, each containing a sleeping creature resembling the _Menotherian_’s elven form; the goddess awakens one of these any time she needs a new herald or wants to create another one of her succubus-like avengers.
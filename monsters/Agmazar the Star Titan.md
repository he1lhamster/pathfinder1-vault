---
cssclass: [monsters]
title1: Agmazar the Star Titan
desc_short: Stony segments cover this towering colossus like armor plates. Though
  it looks lifeless, its four arms move with supple grace.
title2: Agmazar the Star Titan
CR: 26
sources:
- name: Mythic Realms
  page: 46
  link: http://paizo.com/products/btpy90q7?Pathfinder-Campaign-Setting-Mythic-Realms
XP: 2457600
alignment: NE
size: Colossal
type: undead
subtypes:
- cold
- kaiju
initiative:
  bonus: 5
senses:
  creaturesense: true
  see in darkness: true
auras:
- name: frightful presence
  radius: 300
  DC: 39
- name: suffocation
  radius: 60
AC:
  AC: 40
  touch: 22
  flat_footed: 35
  components:
    deflection: 15
    dex: 5
    natural: 18
    size: -8
HP:
  HP: 615
  long: 30d8+480
  fast_healing: 30
saves:
  fort: 25
  ref: 15
  will: 27
defensive_abilities:
- channel resistance +4
- force field
- freedom of movement
DR:
- amount: 20
  weakness: epic
immunities:
- ability damage
- ability drain
- cold
- death effects
- disease
- energy drain
- fear
- undead traits
resistances:
  acid: 30
  electricity: 30
  fire: 30
  negative energy: 30
  sonic: 30
weaknesses:
- vulnerable to fire
speeds:
  base: 100
  climb: 50
attacks:
  melee:
  - - text: 4 slams +33 (4d12+27/19-20/×3 plus energy drain)
      entries:
      - - damage: 4d12+27
          crit_range: 19-20
          crit_multiplier: 3
        - effect: energy drain
      count: 4
      attack: slams
      bonus:
      - 33
  special:
  - channel negative energy (10d6, DC 35, 18/day)
  - energy drain (1 level, DC 40)
  - gravitic control
  - hurl foe
  - serpent arms
  - trample (4d6+27, DC 43)
space: 60
reach: 60
spell_like_abilities:
  entries:
  - name: freedom of movement
    source: default
    freq: Constant
  - name: quickened circle of death
    source: default
    freq: 3/day
    DC: 31
  - name: empowered horrid wilting
    source: default
    freq: 3/day
    DC: 33
  - name: waves of exhaustion
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 20
    concentration: 35
ability_scores:
  STR: 47
  DEX: 21
  CON:
  INT: 6
  WIS: 31
  CHA: 40
BAB: 22
CMB: 48
CMD: 86
feats:
- name: Bleeding Critical
- name: Blind-Fight
- name: Critical Focus
- name: Defensive Combat Training
- name: Empower Spell-Like Ability (horrid wilting)
- name: Improved Critical (slam)
- name: Power Attack
- name: Quick Channel
- name: Quicken Spell-Like Ability (circle of death)
- name: Sickening Critical
- name: Skill Focus (Perception)
- name: Snatch
- superscripts:
  - UM
  name: Thanatopic Spell
- name: Toughness
- name: Weapon Focus (slam)
skills:
  Climb: 30
  Intimidate: 36
  Knowledge (religion): 10
  Perception: 49
  Swim: 20
languages:
- Draconic (can't speak)
special_qualities:
- kaiju traits
- massive
- powerful blows
- recovery
special_abilities:
  Aura of Suffocation (Su): Agmazar's alien presence breaks down the atmosphere around
    it, causing the air to become thin and nearly unbreathable. Within 1 mile of Agmazar,
    breathing creatures are subject to fatigue and altitude sickness as if at high
    peak altitude (Pathfinder RPG Core Rulebook 430). Creatures within 60 feet of
    Agmazar must hold their breath or begin to suffocate (Core Rulebook 445).
  Channel Negative Energy (Su): Agmazar can channel negative energy as a 20th-level
    evil cleric. This ability requires no divine focus.
  Creaturesense (Ex): Agmazar has lifesense up to 120 feet. In addition, it can sense
    the presence and position of undead creatures within 1,200 feet as if it had blindsense.
  Force Field (Su): Agmazar is surrounded by a field of force that grants it a deflection
    bonus to AC equal to its Charisma bonus and resistance 30 against force effects.
    Its natural weapons are treated as force effects for dealing damage to incorporeal
    or ethereal targets. The first time each round Agmazar is targeted with a ranged
    attack, there's a 75% chance that attack is deflected by the force field, with
    a 50% chance of it being reflected back upon its originator and a 50% chance of
    it being deflected toward a random creature within 60 feet of Agmazar (or deflected
    harmlessly if no creature is within this range). This deflected attack uses the
    same attack roll result, caster level, and save DC as the original attack.
  Gravitic Control (Su): 'Agmazar can radically alter the effect of gravity, bending
    or even inverting gravity to suit its will. As a standard action, it can alter
    gravity for 2d6 rounds, choosing one of five effects (with effective caster level
    20). Only one type of gravitic control can be in effect at a time. Involuntary
    movement forced by gravitic control doesn't provoke attacks of opportunity. Agmazar
    and its serpent arms are immune to its gravitic control, except for gravitic deceleration.
    The save DCs are Charisma-based. Gravitic Acceleration: This ability functions
    as telekinesis (CMB +35, Will DC 40).Gravitic Attraction: This ability functions
    as repulsion but in reverse; any creature that fails its saving throw (Will DC
    40) can't move away from Agmazar. Each round it doesn't spend a move action resisting
    the attraction, it is pulled 1d6 × 5 feet toward Agmazar.Gravitic Deceleration:
    All creatures within 30 feet are affected as by feather fall. Flying creatures
    in this radius move at half speed, and a creature making a ranged weapon attack
    targeting a creature in the radius takes a -2 penalty on the attack roll.Gravitic
    Inversion: This ability functions as reverse gravity (Reflex DC 40), but Agmazar
    can concentrate on the spell. Each round it continues to do so, the radius of
    the effect doubles.Gravitic Repulsion: This ability functions as repulsion, but
    a creature that fails its saving throw (Will DC 40) not only can't move toward
    Agmazar, but is also pushed 1d6 × 5 feet away from the kaiju each round it doesn't
    spend a move action resisting the gravitic repulsion.'
  Powerful Blows (Ex): Agmazar adds 1-1/2 times its Strength bonus on damage rolls
    with slam attacks.
  Serpent Arms (Su): |-
    As a full-round action, Agmazar can detach and release one or two of the lower arms from its body, revealing that the joints buried into its torso are alien serpent heads. The arms move and fight independently as hollow serpents (Pathfinder RPG Bestiary 3 149), beginning on the round they're detached. For each arm it detaches, Agmazar takes 25 points of damage that can't be reduced.

    When a hollow serpent uses channel negative energy or a spell-like ability, it counts against Agmazar's uses of that ability. While its arms are detached, Agmazar's fast healing is reduced by 10 for each missing arm, and it can make slam attacks only with the arms still attached. If a hollow serpent is destroyed while separated, Agmazar can regrow its missing arm in 1 hour. Reattaching one or both lower arms is a full-round action and restores Agmazar's fast healing to the normal rate (though does not regain the hit points lost from detaching).
desc_long: |-
  Agmazar the Star Titan is a kaiju whose origins lie far from Golarion. It plummeted from the sky in 2456 by the Imperial Calendar (-44 ar) into the trackless green of the eastern Valashmai Jungles. Though many have searched for Agmazar's landing place, none have found it and survived with suff icient strength or sanity to report precisely where it is.

  However, Agmazar's entrance into the world hardly went unnoticed. In fact, its meteoric advent drew the attention of the great kaiju King Mogaru, who claimed the jungles at that time. In a cataclysmic battle that wiped out every living creature for miles, King Mogaru slew the invader from the stars and left the body burned and broken, after which he returned to his deep lake lair for a long rest.

  King Mogaru, however, didn't know the alien powers engrafted within the Star Titan- fail-safes created long ago by the Balance, its makers upon the planet Verces, who created it as an ultimate weapon against undead invaders from Eox. If Agmazar were killed, these unholy energies would raise it, not to life that might once again be snuffed out by the undead, but to titanic unlife that would make it an invincible weapon.

  After Agmazar had great victories, its overambitious creators launched it into space to take the fight to Eox itself. But the kaiju was intercepted in transit-a cabal of liches used a disguised interplanetary portal to shift Agmazar's trajectory from planetfall on Eox to instead land on Golarion.

  Confused by the richness of life on the planet and unable to escape Golarion's gravity, Agmazar was taken by surprise by Mogaru's onslaught. Its death activated its failsafe programming, but it found few undead within range of it senses. Though the kaiju destroyed undead wherever it found them, once it had exterminated all that it could find, it grew frustrated and its heart turned bitter.

  Agmazar now lies in wait most of the time, but lashes out even at the living if they disturb its watchful reverie. If a great necromantic power arises anywhere near Agmazar, it senses the threat and departs immediately to destroy it, treading a path of devastation as it seeks to fulfill the purpose it was given so long ago.

---

# Agmazar the Star Titan
Stony segments cover this towering colossus like armor plates. Though it looks lifeless, its four arms move with supple _[[spells/Grace|grace]]_.
**Source** Mythic Realms pg. 46
**XP** 2,457,600

NE Colossal undead (cold, kaiju)
**Init** +5; **Senses** creaturesense, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +49
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 39), _[[spells/Suffocation|suffocation]]_ (60 ft.)

##### Defense

**AC** 40, touch 22, _[[conditions/Flat-Footed|flat-footed]]_ 35 (+15 deflection, +5 Dex, +18 natural, –8 size)
**hp** 615 (30d8+480); _[[universal monster rules/Fast Healing|fast healing]]_ 30
**Fort** +25, **Ref** +15, **Will** +27
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4, force field, _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 20/epic; **Immune** ability damage, ability drain, cold, death effects, disease, _[[universal monster rules/Energy Drain|energy drain]]_, _[[universal monster rules/Fear|fear]]_, _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** acid 30, electricity 30, fire 30, negative energy 30, sonic 30
**Weaknesses** vulnerable to fire

##### Offense
**Speed** 100 ft., _[[universal monster rules/Climb|climb]]_ 50 ft.
**Melee** 4 slams +33 (4d12+27/19–20/×3 plus _energy drain_)
**Space** 60 ft., **Reach** 60 ft.
**Special Attacks** channel negative energy (10d6, DC 35, 18/day), _energy drain_ (1 level, DC 40), gravitic control, hurl foe, serpent arms, _[[universal monster rules/Trample|trample]]_ (4d6+27, DC 43)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +35)
Constant—_freedom of movement_
3/day—quickened _[[spells/Circle Of Death|circle of death]]_ (DC 31), empowered _[[spells/Horrid Wilting|horrid wilting]]_ (DC 33), _[[spells/Waves of Exhaustion|waves of exhaustion]]_

##### Statistics
**Str** 47, **Dex** 21, **Con** —, **Int** 6, **Wis** 31, **Cha** 40
**Base Atk** +22; **CMB** +48; **CMD** 86
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Defensive Combat Training|Defensive Combat Training]]_, _[[feats/Empower Spell-Like Ability|Empower Spell-Like Ability]]_ (_horrid wilting_), _[[feats/Improved Critical|Improved Critical]]_ (slam), _[[feats/Power Attack|Power Attack]]_, _[[feats/Quick Channel|Quick Channel]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_circle of death_), _[[feats/Sickening Critical|Sickening Critical]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Snatch|Snatch]]_, _[[feats/Thanatopic Spell|Thanatopic Spell]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (slam)
**Skills** _Climb_ +30, Intimidate +36, Knowledge (religion) +10, Perception +49, Swim +20
**Languages** Draconic (can’t speak)
**SQ** kaiju traits, massive, powerful blows, recovery

### Special Abilities

**Aura of _Suffocation_ (Su)** Agmazar’s alien presence breaks down the atmosphere around it, causing the air to become thin and nearly unbreathable. Within 1 mile of Agmazar, breathing creatures are subject to fatigue and altitude sickness as if at high peak altitude (Pathfinder RPG Core Rulebook 430). Creatures within 60 feet of Agmazar must hold their breath or begin to suffocate (Core Rulebook 445).

**Channel Negative Energy (Su)** Agmazar can channel negative energy as a 20th-level evil _[[classes/Cleric|cleric]]_. This ability requires no divine focus.

**Creaturesense (Ex)** Agmazar has _[[universal monster rules/Lifesense|lifesense]]_ up to 120 feet. In addition, it can sense the presence and position of undead creatures within 1,200 feet as if it had _[[universal monster rules/Blindsense|blindsense]]_.

**Force Field (Su)** Agmazar is surrounded by a field of force that grants it a _deflection_ bonus to AC equal to its Charisma bonus and _[[universal monster rules/Resistance|resistance]]_ 30 against force effects. Its natural weapons are treated as force effects for dealing damage to _[[universal monster rules/Incorporeal|incorporeal]]_ or ethereal targets. The first time each round Agmazar is targeted with a ranged attack, there’s a 75% chance that attack is deflected by the force field, with a 50% chance of it being reflected back upon its originator and a 50% chance of it being deflected toward a random creature within 60 feet of Agmazar (or deflected harmlessly if no creature is within this range). This deflected attack uses the same attack roll result, caster level, and save DC as the original attack.

**Gravitic Control (Su)** Agmazar can radically alter the effect of gravity, bending or even inverting gravity to suit its will. As a standard action, it can alter gravity for 2d6 rounds, choosing one of five effects (with effective caster level 20). Only one type of gravitic control can be in effect at a time. Involuntary movement forced by gravitic control doesn’t provoke attacks of opportunity. Agmazar and its serpent arms are immune to its gravitic control, except for gravitic deceleration. The save DCs are Charisma-based.

* Gravitic Acceleration: This ability functions as _[[spells/Telekinesis|telekinesis]]_ (CMB +35, Will DC 40).
* Gravitic Attraction: This ability functions as _[[spells/Repulsion|repulsion]]_ but in reverse; any creature that fails its saving throw (Will DC 40) can’t move away from Agmazar. Each round it doesn’t spend a move action resisting the attraction, it is pulled 1d6 × 5 feet toward Agmazar.
* Gravitic Deceleration: All creatures within 30 feet are affected as by _[[spells/Feather Fall|feather fall]]_. Flying creatures in this radius move at half speed, and a creature making a ranged weapon attack targeting a creature in the radius takes a –2 penalty on the attack roll.
* Gravitic Inversion: This ability functions as _[[spells/Reverse Gravity|reverse gravity]]_ (Reflex DC 40), but Agmazar can concentrate on the spell. Each round it continues to do so, the radius of the effect doubles.
* Gravitic _Repulsion_: This ability functions as _repulsion_, but a creature that fails its saving throw (Will DC 40) not only can’t move toward Agmazar, but is also pushed 1d6 × 5 feet away from the kaiju each round it doesn’t spend a move action resisting the gravitic _repulsion_.

**Powerful Blows (Ex)** Agmazar adds 1-1/2 times its Strength bonus on damage rolls with slam attacks.
**Serpent Arms (Su)** As a full-round action, Agmazar can detach and release one or two of the lower arms from its body, revealing that the joints buried into its torso are alien serpent heads. The arms move and fight independently as hollow serpents (Pathfinder RPG Bestiary 3 149), beginning on the round they’re detached. For each arm it detaches, Agmazar takes 25 points of damage that can’t be reduced.

When a _[[monsters/Hollow Serpent|hollow serpent]]_ uses channel negative energy or a spell-like ability, it counts against Agmazar’s uses of that ability. While its arms are detached, Agmazar’s _fast healing_ is reduced by 10 for each missing arm, and it can make slam attacks only with the arms still attached. If a _hollow serpent_ is destroyed while separated, Agmazar can regrow its missing arm in 1 hour. Reattaching one or both lower arms is a full-round action and restores Agmazar’s _fast healing_ to the normal rate (though does not regain the hit points lost from detaching).

##### Description

_[[monsters/Agmazar the Star Titan|Agmazar the Star Titan]]_ is a kaiju whose origins lie far from Golarion. It plummeted from the sky in 2456 by the Imperial Calendar (–44 ar) into the _[[items/Armor Magic Abilities/Trackless|trackless]]_ green of the eastern Valashmai Jungles. Though many have searched for Agmazar’s landing place, none have found it and survived with suff icient strength or sanity to report precisely where it is.

However, Agmazar’s entrance into the world hardly went unnoticed. In fact, its meteoric advent drew the attention of the great kaiju _[[npcs/King|King]]_ Mogaru, who claimed the jungles at that time. In a cataclysmic battle that wiped out every living creature for miles, _King_ Mogaru slew the invader from the stars and left the body burned and _[[conditions/Broken|broken]]_, after which he returned to his deep lake lair for a long rest.

_King_ Mogaru, however, didn’t know the alien powers engrafted within the Star Titan— fail-safes created long ago by the Balance, its makers upon the planet Verces, who created it as an ultimate weapon against undead invaders from Eox. If Agmazar were killed, these _[[items/Weapon Magic Abilities/Unholy|unholy]]_ energies would raise it, not to life that might once again be snuffed out by the undead, but to _[[items/Armor Magic Abilities/Titanic|titanic]]_ unlife that would make it an invincible weapon.

After Agmazar had great victories, its overambitious creators launched it into space to take the fight to Eox itself. But the kaiju was intercepted in transit—a cabal of liches used a disguised interplanetary portal to shift Agmazar’s trajectory from planetfall on Eox to instead land on Golarion.

_[[conditions/Confused|Confused]]_ by the richness of life on the planet and unable to escape Golarion’s gravity, Agmazar was taken by surprise by Mogaru’s _[[feats/Onslaught|onslaught]]_. Its death activated its failsafe programming, but it found few undead within range of it senses. Though the kaiju destroyed undead wherever it found them, once it had exterminated all that it could find, it grew frustrated and its heart turned _[[items/Armor Magic Abilities/Bitter|bitter]]_.

Agmazar now lies in wait most of the time, but lashes out even at the living if they disturb its watchful reverie. If a great necromantic power arises anywhere near Agmazar, it senses the threat and departs immediately to destroy it, treading a path of devastation as it seeks to fulfill the purpose it was given so long ago.
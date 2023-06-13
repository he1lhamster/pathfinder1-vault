---
cssclass: [monsters]
title1: Herald, Mother's Maw
desc_short: This skull is as large as an ogre and surrounded by buzzing flies. Its
  bat wings carry it through the air as easily as those of a vulture.
title2: Mother's Maw
CR: 15
sources:
- name: Inner Sea Gods
  page: 312
  link: http://paizo.com/products/btpy94wj?Pathfinder-Campaign-Setting-Inner-Sea-Gods-Hardcover
XP: 51200
alignment: NE
size: Large
type: undead
subtypes:
- evil
- extraplanar
- herald
initiative:
  bonus: 11
senses:
  darkvision: 60
  scent: true
  lifesense: true
auras:
- name: desecrate
  radius: 20
AC:
  AC: 30
  touch: 16
  flat_footed: 23
  components:
    dex: 7
    natural: 14
    size: -1
HP:
  HP: 189
  long: 18d8+108
  other: fast healing 5 or 20 (see devour soul)
saves:
  fort: 13
  ref: 16
  will: 19
defensive_abilities:
- channel resistance +4
- spell deflection
DR:
- amount: 15
  weakness: bludgeoning and good
immunities:
- cold
- electricity
- undead traits
resistances:
  fire: 30
SR: 26
speeds:
  base: 10
  fly: 40
  fly_maneuverability: average
attacks:
  melee:
  - - text: bite +24 (5d6+17/19-20 plus bleed, disease, drain, and grab)
      entries:
      - - damage: 5d6+17
          crit_range: 19-20
        - effect: bleed
        - effect: disease
        - effect: drain
        - effect: grab
      attack: bite
      bonus:
      - 24
  special:
  - breath weapon (60-ft. cone, 15d6 negative energy, Reflex DC 25 for half, usable
    every 1d4 rounds)
  - channel negative energy 9/day (DC 19, 6d6)
  - devour soul
  - disease
  - swallow whole (special, AC 17, 20 hp)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: desecrate
    source: default
    freq: Constant
  - name: contagion
    source: default
    freq: At will
    DC: 20
  - name: dimension door
    source: default
    freq: At will
  - name: ghoul hunger
    source: default
    freq: At will
    DC: 18
  - name: inflict critical wounds
    source: default
    freq: At will
    DC: 20
  - superscripts:
    - APG
    name: quickened vomit swarm
    source: default
    freq: At will
    paren_text: maggots, use army ant swarm
  - name: animate dead
    source: default
    freq: 1/day
  - name: create undead
    source: default
    freq: 1/day
  - name: eyebite
    source: default
    freq: 1/day
    DC: 22
  - name: plane shift
    source: default
    freq: 1/day
    DC: 22
  sources:
  - name: default
    CL: 15
    concentration: 21
ability_scores:
  STR: 33
  DEX: 25
  CON:
  INT: 21
  WIS: 20
  CHA: 22
BAB: 13
CMB: 25
CMD: 42
CMD_other: can't be tripped
feats:
- name: Cleave
- is_bonus: true
  name: Command Undead
- name: Critical Focus
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Iron Will
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
- name: Staggering Critical
- is_bonus: true
  name: Stunning Critical
skills:
  Acrobatics: 25
  Fly: 26
  Intimidate: 27
  Knowledge (planes): 23
  Knowledge (religion): 26
  Perception: 26
  Profession (cook): 23
  Sense Motive: 26
  Stealth: 24
languages:
- Abyssal
- Common
- Infernal
- Necril
special_qualities:
- deathless
ecology:
  environment: any (Abaddon)
  organization: solitary
  treasure_type: none
special_abilities:
  Deathless (Su): If destroyed, the herald it returns to unlife 1 hour later at 1
    hit point, allowing its fast healing to resume healing it. It can be permanently
    destroyed by positive energy, being reduced to 0 hit points in the area of a bless
    or hallow spell, or if 20 vials of holy water are sprinkled on its remains.
  Devour Soul (Su): A creature swallowed by the herald must save every round against
    slay living (DC 25, caster level 15th). The soul of a creature slain by this attack
    becomes trapped within the herald's skull, and the mangled corpse is immediately
    regurgitated. The creature cannot be brought back to life until the herald's destruction
    (or a spell deflection-see below) releases its soul. The Maw can hold only one
    soul at a time. The trapped essence provides the Maw with fast healing 20, lasting
    1 round for every Hit Die of the devoured soul. The trapped soul gains 1 permanent
    negative level for every round it spends within the Maw-these negative levels
    remain if the creature is brought back to life (but don't stack with any negative
    levels imparted by being brought back to life). A soul that is completely consumed
    may be restored to life only by a miracle or wish spell. The save DC is Charisma-based.
  Disease (Su): Mother's Maw bite attack carries mummy rot (Fortitude DC 25).
  Spell Deflection (Su): 'If any of the following spells is cast at the Maw and overcomes
    its spell resistance, it instead affects the devoured soul: banishment, chaos
    hammer, confusion, crushing despair, detect thoughts, dispel evil, dominate person,
    fear, geas/quest, holy word, hypnotism, imprisonment, magic jar, maze, suggestion,
    trap the soul, or any form of charm or compulsion. While none of these effects
    harms the soul, the caster must attempt a DC 25 caster level check when a spell
    is deflected- success indicates that the trapped soul is released from its prison
    and the creature whose body it belonged to can now be restored to life as normal.
    Mother's Maw can only benefit from this ability while it has a soul devoured.'
desc_long: This terror comes to the mortal realm at the command of the Pallid Princess.
  It's an unsubtle thing of ravenous hunger, with little purpose but to kill, eat,
  and animate corpses. Created from the skull of a fallen titan, Mother's Maw is as
  brilliant as a lich, but its only interest is satisfying its cravings for life and
  sensation. Urgathoa's herald measures nearly 13 feet in height and weighs 3,000
  pounds.

---

# Herald, Mother’s Maw
This skull is as large as an _[[monsters/Ogre|ogre]]_ and surrounded by buzzing flies. Its bat wings carry it through the air as easily as those of a _[[monsters/Vulture|vulture]]_.
**Source** Inner Sea Gods pg. 312
**XP** 51,200

NE Large undead (evil, extraplanar, herald)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_, _[[universal monster rules/Lifesense|lifesense]]_; Perception +26
**Aura** _[[spells/Desecrate|desecrate]]_ (20 ft.)

##### Defense

**AC** 30, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+7 Dex, +14 natural, –1 size)
**hp** 189 (18d8+108); _[[universal monster rules/Fast Healing|fast healing]]_ 5 or 20 (see devour soul)
**Fort** +13, **Ref** +16, **Will** +19
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4, spell deflection; **DR** 15/bludgeoning and good; **Immune** cold, electricity, _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** fire 30; **SR** 26

##### Offense
**Speed** 10 ft., fly 40 ft. (average)
**Melee** bite +24 (5d6+17/19–20 plus _[[universal monster rules/Bleed|bleed]]_, disease, drain, and _[[universal monster rules/Grab|grab]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, 15d6 negative energy, Reflex DC 25 for half, usable every 1d4 rounds), channel negative energy 9/day (DC 19, 6d6), devour soul, disease, _[[universal monster rules/Swallow Whole|swallow whole]]_ (special, AC 17, 20 hp)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +21)
Constant—_desecrate_
At will—_[[spells/Contagion|contagion]]_ (DC 20), _[[spells/Dimension Door|dimension door]]_, _[[spells/Ghoul Hunger|ghoul hunger]]_ (DC 18), _[[spells/Inflict Critical Wounds|inflict critical wounds]]_ (DC 20), quickened _[[spells/Vomit Swarm|vomit swarm]]_ (maggots, use army ant swarm)
1/day—_[[spells/Animate Dead|animate dead]]_, _[[spells/Create Undead|create undead]]_, _[[spells/Eyebite|eyebite]]_ (DC 22), _[[spells/Plane Shift|plane shift]]_ (DC 22)

##### Statistics
**Str** 33, **Dex** 25, **Con** —, **Int** 21, **Wis** 20, **Cha** 22
**Base Atk** +13; **CMB** +25; **CMD** 42 (can’t be tripped)
**Feats** _[[feats/Cleave|Cleave]]_, _[[spells/Command Undead|Command Undead]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Stunning Critical|Stunning Critical]]_
**Skills** Acrobatics +25, Fly +26, Intimidate +27, Knowledge (planes) +23, Knowledge (religion) +26, Perception +26, Profession (cook) +23, Sense Motive +26, Stealth +24
**Languages** Abyssal, Common, Infernal, Necril
**SQ** _[[spells/Deathless|deathless]]_

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary
**Treasure** none

### Special Abilities

**_Deathless_ (Su)** If destroyed, the herald it returns to unlife 1 hour later at 1 hit point, allowing its _fast healing_ to resume healing it. It can be permanently destroyed by positive energy, being reduced to 0 hit points in the area of a _[[spells/Bless|bless]]_ or _[[spells/Hallow|hallow]]_ spell, or if 20 vials of _[[items/Mundane/Holy water|holy water]]_ are sprinkled on its remains.

**Devour Soul (Su)** A creature swallowed by the herald must save every round against _[[spells/Slay Living|slay living]]_ (DC 25, caster level 15th). The soul of a creature slain by this attack becomes trapped within the herald’s skull, and the mangled corpse is immediately regurgitated. The creature cannot be brought back to life until the herald’s _[[spells/Destruction|destruction]]_ (or a spell _deflection_—see below) releases its soul. The Maw can hold only one soul at a time. The trapped essence provides the Maw with _fast healing_ 20, lasting 1 round for every Hit Die of the devoured soul. The trapped soul gains 1 permanent negative level for every round it spends within the Maw—these negative levels remain if the creature is brought back to life (but don’t stack with any negative levels imparted by being brought back to life). A soul that is completely consumed may be restored to life only by a _[[spells/Miracle|miracle]]_ or _[[spells/Wish|wish]]_ spell. The save DC is Charisma-based.

**Disease (Su)** Mother’s Maw bite attack carries _[[curses/Mummy rot|mummy rot]]_ (Fortitude DC 25).
**Spell _Deflection_ (Su)** If any of the following spells is cast at the Maw and overcomes its _[[universal monster rules/Spell Resistance|spell resistance]]_, it instead affects the devoured soul: _[[spells/Banishment|banishment]]_, _[[spells/Chaos Hammer|chaos hammer]]_, _[[spells/Confusion|confusion]]_, _[[spells/Crushing Despair|crushing despair]]_, _[[spells/Detect Thoughts|detect thoughts]]_, _[[spells/Dispel Evil|dispel evil]]_, _[[spells/Dominate Person|dominate person]]_, _[[universal monster rules/Fear|fear]]_, geas/quest, _[[spells/Holy Word|holy word]]_, _[[spells/Hypnotism|hypnotism]]_, _[[spells/Imprisonment|imprisonment]]_, _[[spells/Magic Jar|magic jar]]_, _[[spells/Maze|maze]]_, _[[spells/Suggestion|suggestion]]_, _[[spells/Trap the Soul|trap the soul]]_, or any form of charm or compulsion. While none of these effects harms the soul, the caster must attempt a DC 25 caster level check when a spell is deflected— success indicates that the trapped soul is released from its prison and the creature whose body it belonged to can now be restored to life as normal. Mother’s Maw can only benefit from this ability while it has a soul devoured.

##### Description

This terror comes to the mortal realm at the _[[spells/Command|command]]_ of the Pallid _[[npcs/Princess|Princess]]_. It’s an unsubtle thing of _[[curses/Ravenous|ravenous]]_ hunger, with little purpose but to kill, eat, and animate corpses. Created from the skull of a _[[monsters/Fallen|fallen]]_ titan, Mother’s Maw is as brilliant as a _[[monsters/Lich|lich]]_, but its only interest is satisfying its cravings for life and sensation. Urgathoa’s herald measures nearly 13 feet in height and weighs 3,000 pounds.
---
cssclass: [monsters]
title1: Akaruzug
desc_short: This stony guardian has been sculpted in the shape of a grim, horned angel,
  and a crucified corpse has been affixed to its chest.
title2: Akaruzug
CR: 15
sources:
- name: Curse of the Crimson Throne (PFRPG)
  page: 466
  link: http://paizo.com/products/btpy9nme?Pathfinder-Adventure-Path-Curse-of-the-Crimson-Throne
- name: 'Pathfinder #12: Crown of Fangs'
  page: 82
  link: http://paizo.com/pathfinder/adventurePath/curseOfTheCrimsonThrone/v5748btpy84el
XP: 51200
alignment: LE
size: Large
type: construct
initiative:
  bonus: 7
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: unhallow
  radius: 40
AC:
  AC: 30
  touch: 16
  flat_footed: 27
  components:
    deflection: 4
    dex: 3
    natural: 14
    size: -1
HP:
  HP: 220
  long: 20d10+110
saves:
  fort: 8
  ref: 11
  will: 10
defensive_abilities:
- soul shield
DR:
- amount: 15
  weakness: bludgeoning and good
immunities:
- construct traits
speeds:
  fly: 40
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 claws +27 (2d6+8/19-20)
      entries:
      - - damage: 2d6+8
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 27
    - text: gore +27 (2d8+8/19-20)
      entries:
      - - damage: 2d8+8
          crit_range: 19-20
      attack: gore
      bonus:
      - 27
    - text: 2 wings +22 (1d8+4)
      entries:
      - - damage: 1d8+4
      count: 2
      attack: wings
      bonus:
      - 22
  special:
  - soul steel
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: unhallow
    source: default
    freq: Constant
  - name: soul slave
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 20
    concentration: 24
ability_scores:
  STR: 26
  DEX: 17
  CON:
  INT: 15
  WIS: 18
  CHA: 19
BAB: 20
CMB: 29
CMD: 46
feats:
- name: Ability Focus (soul steal)
- name: Blinding Critical
- name: Combat Reflexes
- name: Critical Focus
- name: Great Fortitude
- name: Improved Critical (claws)
- name: Improved Critical (gore)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Power Attack
skills:
  Fly: 32
  Knowledge (religion): 22
  Perception: 24
  Sense Motive: 24
languages:
- Infernal
special_qualities:
- soul engine
ecology:
  environment: any ruins
  organization: solitary
  treasure_type: incidental
special_abilities:
  Soul Engine (Su): An akaruzug draws the energy it requires to function from a living
    creature crucified upon its frame. An active akaruzug (or another creature working
    with an inactive akaruzug) can spend 1 minute to bind a helpless or willing creature
    to the construct. Once the victim is restrained, the akaruzug can attempt to draw
    the creature's soul into it once per round as a free action- the victim can resist
    with a successful DC 24 Will save. On a failure, the victim dies and the akaruzug
    becomes active. If the body crucified upon an active akaruzug is removed, the
    soul within the construct is freed and the akaruzug deactivates after 1d4 rounds.
    An akaruzug's victim cannot be resurrected while its soul is trapped within the
    construct, but destroying an akaruzug releases a trapped soul. While an akaruzug
    is active, attacks and effects directed specifically at the victim crucified to
    the akaruzug treat the attack or effect as if it targeted the akaruzug instead.
    However, a creature can attempt to remove a crucified body from the construct,
    but doing so first requires the creature to successfully pin the akaruzug. Once
    this occurs, the creature can attempt a combat maneuver check to wrench the body
    free. On a success, the corpse is removed and the akaruzug deactivates in 1d4
    rounds. A deactivated akaruzug can take no action other than to attempt to draw
    in the soul of a creature crucified on its body to reactivate itself. It does
    not have an Intelligence score while deactivated, nor does it gain the benefit
    of any of its feats or skill ranks. It can't fly or move at all, and loses all
    benefits of its soul shield defensive ability. It retains its lawful evil alignment
    while deactivated. The save DC is Charisma-based.
  Soul Shield (Ex): As long as an akaruzug is active, it gains bonus hit points equal
    to its Charisma modifier × its Hit Dice (80 hit points for a typical akaruzug),
    and gains a deflection bonus equal to its Charisma modifier to its Armor Class
    (+4 for a typical akaruzug).
  Soul Slave (Sp): Using a trapped soul, an akaruzug can manifest a ghostly representation
    of its victim to attack its enemies. A soul slave appears as the akaruzug's victim
    did in life and wields a weapon favored by that individual, but otherwise functions
    as per spiritual ally cast by a 20thlevel caster (and, as such, has an attack
    of +24/+19/+14/+9 and deals 1d10+5 points of force damage on a hit).
  Soul Steal (Su): An akaruzug can draw additional soul energy into itself. Once every
    1d4 rounds, the construct can unleash a blast of soul essence that seeks to flense
    the life force of any living creature within a 20-foot burst. Any living creature
    in this area must succeed at a DC 24 Fortitude save or gain 1d4 negative levels.
    A victim can remove those negative levels 24 hours later with a successful DC
    24 Fortitude save. Each time an akaruzug successfully uses this ability, it regains
    a number of hit points equal to 5 times the number of creatures successfully affected
    by soul steal (regardless of how many negative levels any one creature suffers).
    The save DC is Charisma-based.
  Unhallow (Sp): An akaruzug emanates a 40-foot aura of unholy energy, as per unhallow.
    The construct's creator determines what, if any, additional spell effects are
    tied to the akaruzug's unhallow aura at the time of its creation. The construct
    benefits from any spell effects tied to its unhallow aura. Common choices are
    darkness, detect good, freedom of movement, and invisibility purge. If this effect
    is dispelled and the akaruzug uses the spell-like ability to reactivate the effect,
    it also reactivates the associated spell effect (if any) set by its creator.
desc_long: |-
  Akaruzugs are blasphemous constructs coveted by those who revel in the torment of their victims. Crafted in the appearance of grim, towering angels and creatures of warped beauty, these creations stand in mockery of light, life, and all that is good. By their very existence- powered by souls trapped in torment-they spread death and despair.

   Most akaruzugs are 15 feet tall or larger, and weigh upward of 3 tons, depending on the materials used in their creation.

---

# Akaruzug
This stony _[[items/Weapon Magic Abilities/Guardian|guardian]]_ has been sculpted in the shape of a grim, horned angel, and a crucified corpse has been affixed to its chest.
**Source** Curse of the Crimson Throne (PFRPG) pg. 466, Pathfinder #12: _[[items/Wondrous Item/Crown of Fangs|Crown of Fangs]]_ pg. 82
**XP** 51,200

LE Large construct
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +24
**Aura** _[[spells/Unhallow|unhallow]]_ (40 ft.)

##### Defense

**AC** 30, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+4 deflection, +3 Dex, +14 natural, –1 size)
**hp** 220 (20d10+110)
**Fort** +8, **Ref** +11, **Will** +10
**Defensive Abilities** soul _[[spells/Shield|shield]]_; **DR** 15/bludgeoning and good; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_

##### Offense
**Speed** fly 40 ft. (perfect)
**Melee** 2 claws +27 (2d6+8/19–20), gore +27 (2d8+8/19–20), 2 wings +22 (1d8+4)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** soul steel
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +24)
Constant—_unhallow_ 
1/day—soul _[[items/Mundane/Slave|slave]]_

##### Statistics
**Str** 26, **Dex** 17, **Con** —, **Int** 15, **Wis** 18, **Cha** 19
**Base Atk** +20; **CMB** +29; **CMD** 46
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (soul steal), _[[feats/Blinding Critical|Blinding Critical]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Critical|Improved Critical]]_ (claws), _Improved Critical_ (gore), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Fly +32, Knowledge (religion) +22, Perception +24, Sense Motive +24
**Languages** Infernal
**SQ** soul engine

##### Ecology

**Environment** any ruins
**Organization** solitary
**Treasure** incidental

### Special Abilities
**Soul Engine (Su)** An _[[monsters/Akaruzug|akaruzug]]_ draws the energy it requires to function from a living creature crucified upon its frame. An active _akaruzug_ (or another creature working with an inactive _akaruzug_) can spend 1 minute to bind a _[[conditions/Helpless|helpless]]_ or willing creature to the construct. Once the victim is restrained, the _akaruzug_ can attempt to draw the creature’s soul into it once per round as a free action— the victim can resist with a successful DC 24 Will save. On a failure, the victim dies and the _akaruzug_ becomes active. If the body crucified upon an active _akaruzug_ is removed, the soul within the construct is freed and the _akaruzug_ deactivates after 1d4 rounds. An _akaruzug_’s victim cannot be resurrected while its soul is trapped within the construct, but destroying an _akaruzug_ releases a trapped soul. While an _akaruzug_ is active, attacks and effects directed specifically at the victim crucified to the _akaruzug_ treat the attack or effect as if it targeted the _akaruzug_ instead. However, a creature can attempt to remove a crucified body from the construct, but doing so first requires the creature to successfully pin the _akaruzug_. Once this occurs, the creature can attempt a combat maneuver check to wrench the body free. On a success, the corpse is removed and the _akaruzug_ deactivates in 1d4 rounds. A deactivated _akaruzug_ can take no action other than to attempt to draw in the soul of a creature crucified on its body to reactivate itself. It does not have an Intelligence score while deactivated, nor does it gain the benefit of any of its feats or skill ranks. It can’t fly or move at all, and loses all benefits of its soul _shield_ defensive ability. It retains its lawful evil alignment while deactivated. The save DC is Charisma-based.
**Soul _Shield_ (Ex)** As long as an _akaruzug_ is active, it gains bonus hit points equal to its Charisma modifier × its Hit Dice (80 hit points for a typical _akaruzug_), and gains a _deflection_ bonus equal to its Charisma modifier to its Armor Class (+4 for a typical _akaruzug_).
**Soul _Slave_ (Sp)** Using a trapped soul, an _akaruzug_ can manifest a ghostly representation of its victim to attack its enemies. A soul _slave_ appears as the _akaruzug_’s victim did in life and wields a weapon favored by that individual, but otherwise functions as per _[[spells/Spiritual Ally|spiritual ally]]_ cast by a 20thlevel caster (and, as such, has an attack of +24/+19/+14/+9 and deals 1d10+5 points of force damage on a hit).
**Soul Steal (Su)** An _akaruzug_ can draw additional soul energy into itself. Once every 1d4 rounds, the construct can unleash a blast of soul essence that seeks to flense the life force of any living creature within a 20-foot burst. Any living creature in this area must succeed at a DC 24 Fortitude save or gain 1d4 negative levels. A victim can remove those negative levels 24 hours later with a successful DC 24 Fortitude save. Each time an _akaruzug_ successfully uses this ability, it regains a number of hit points equal to 5 times the number of creatures successfully affected by soul steal (regardless of how many negative levels any one creature suffers). The save DC is Charisma-based.

**_Unhallow_ (Sp)** An _akaruzug_ emanates a 40-foot aura of _[[items/Weapon Magic Abilities/Unholy|unholy]]_ energy, as per _unhallow_. The construct’s creator determines what, if any, additional spell effects are tied to the _akaruzug_’s _unhallow_ aura at the time of its creation. The construct benefits from any spell effects tied to its _unhallow_ aura. Common choices are _[[spells/Darkness|darkness]]_, _[[spells/Detect Good|detect good]]_, _[[spells/Freedom of Movement|freedom of movement]]_, and _[[spells/Invisibility Purge|invisibility purge]]_. If this effect is dispelled and the _akaruzug_ uses the spell-like ability to reactivate the effect, it also reactivates the associated spell effect (if any) set by its creator.

##### Description

Akaruzugs are blasphemous constructs coveted by those who revel in the torment of their victims. Crafted in the appearance of grim, towering angels and creatures of warped beauty, these creations stand in mockery of light, life, and all that is good. By their very existence— powered by souls trapped in torment—they spread death and despair.

Most akaruzugs are 15 feet tall or larger, and weigh upward of 3 tons, depending on the materials used in their creation.
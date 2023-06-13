---
cssclass: [monsters]
title1: Living Doldrums
desc_short: The air here is eerily still, and the normal sound of the wind is replaced
  by a barely audible hum.
title2: Living Doldrums
CR: 12
sources:
- name: 'Pathfinder #123: The Flooded Cathedral'
  page: 88
  link: http://paizo.com/products/btpy9uk2?Pathfinder-Adventure-Path-123-The-Flooded-Cathedral
XP: 19200
alignment: NE
size: Gargantuan
type: outsider
subtypes:
- air
- elemental
- extraplanar
initiative:
  bonus: 5
senses:
  darkvision: 60
auras:
- name: stagnant
  radius: 240
AC:
  AC: 8
  touch: 8
  flat_footed: 6
  components:
    dex: 1
    dodge: 1
    size: -4
HP:
  HP: 162
  long: 13d10+91
saves:
  fort: 11
  ref: 9
  will: 15
defensive_abilities:
- gaseous
- natural invisibility
DR:
- amount: 10
  weakness: magic
immunities:
- acid
- elemental traits
resistances:
  cold: 10
  electricity: 10
  fire: 10
weaknesses:
- vulnerability to magic wind
- vulnerability to sonic
speeds:
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 hypoxic touches +9 touch (6d6 and slowed)
      entries:
      - - damage: 6d6
        - effect: slowed
      count: 2
      attack: hypoxic touches
      bonus:
      - 9
      touch: true
  special:
  - hypoxic heart (DC 23, 6d6 and slowed)
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: detect thoughts
    source: default
    freq: At will
    DC: 19
  - name: crushing despair
    source: default
    freq: 3/day
    DC: 21
  - name: quickened murderous command
    source: default
    freq: 3/day
    DC: 18
  - name: quickened oppressive boredom
    source: default
    freq: 3/day
    DC: 19
  - name: quickened paranoia
    source: default
    freq: 3/day
    DC: 19
  - name: envious urge
    source: default
    freq: 1/day
    DC: 23
  - name: malicious spite
    source: default
    freq: 1/day
    DC: 21
  - name: song of discord
    source: default
    freq: 1/day
    DC: 22
  sources:
  - name: default
    CL: 13
    concentration: 20
ability_scores:
  STR:
  DEX: 13
  CON: 24
  INT: 9
  WIS: 24
  CHA: 24
BAB: 13
CMB: 17
CMD: 29
feats:
- name: Alertness
- name: Dodge
- name: Improved Initiative
- name: Mobility
- name: Quicken Spell-Like Ability (murderous command)
- name: Quicken Spell-Like Ability (oppressive boredom)
- name: Quicken Spell-Like Ability (paranoia)
skills:
  Fly: 19
  Knowledge (planes): 15
  Perception: 27
  Sense Motive: 27
  Stealth: 5
languages:
- Auran
- Common (can't speak any language)
- telepathy 100 ft.
ecology:
  environment: any air (Plane of Air)
  organization: solitary
  treasure_type: incidental
special_abilities:
  Gaseous (Ex): A living doldrums has a body composed of stagnant air. It can pass
    through small holes, narrow openings, and even mere cracks, but it cannot enter
    water or other liquid. It has no Strength score and cannot manipulate objects
    as a result.
  Hypoxic Heart (Ex): A living doldrums can engulf foes, as per the universal monster
    ability. A creature engulfed by a living doldrums doesn't gain the pinned condition
    and can move normally, but it is still in danger of suffocating. A creature that
    begins its turn engulfed takes 6d6 points of damage and must succeed at a DC 23
    Fortitude saving throw or be slowed (as per the spell slow). This condition lasts
    as long as the creature is in the living doldrums' space and for 1d4+1 rounds
    after it leaves. Creatures that don't breathe take no damage from the living doldrums'
    engulf attack and do not risk being slowed. The living doldrums extinguishes all
    nonmagical fires in its space. The save DC is Constitution-based.
  Hypoxic Touch (Ex): A living doldrums' touch attack hinders a creature's ability
    to breathe. A creature that takes damage from this attack must succeed at a DC
    23 Fortitude saving throw or be slowed (as per the spell slow) for 1 round. Creatures
    that don't breathe are immune to this attack. The save DC is Constitution-based.
  Natural Invisibility (Su): This ability is constantly in effect, even when the living
    doldrums is attacking, and is not subject to invisibility purge. Against foes
    that are unable to see invisible creatures, it gains an additional +20 bonus on
    Stealth checks when moving, or +40 when stationary; these bonuses are not included
    in the statistics above. Because of its size and pervasiveness within the area
    it occupies, a living doldrums gains only a 20% miss chance due to its invisibility.
  Stagnant Aura (Su): The air within 240 feet of a living doldrums is always still.
    Naturally occurring winds flow around this radius without disturbing anything
    inside (though precipitation falls as normal). Mundane attempts to create airflow
    within the aura (such as with a fan) are only half as strong as normal. Air elementals,
    gaseous creatures, and winged creatures (other than living doldrums) have their
    maneuverability reduced by one category within the aura. This aura does not inhibit
    magical air and wind effects.
  Vulnerability to Magic Wind (Ex): Damaging effects from moving air (such as a kineticist's
    air blast) deal 50% more damage to a living doldrums. A living doldrums that begins
    its turn in the area of a nondamaging magical wind effect takes 1d6 points of
    damage per spell level of the effect.
desc_long: When people imagine elementals that thrive on the Plane of Air, they are
  most likely to think of the spirits of rushing wind and thundering storm, but not
  all air elementals are so dynamic. Living doldrums are elementals that embody stagnant
  air. Those who can see invisible creatures describe the living doldrums as a cloud
  roughly 20 feet in diameter that resembles a knotted snake with a head at both ends.
  The scent of stale air lingers around a living doldrums, even if one only recently
  arrived to the area.

---

# Living Doldrums
The air here is eerily still, and the normal sound of the wind is replaced by a barely audible hum.
**Source** Pathfinder #123: The Flooded Cathedral pg. 88
**XP** 19,200

NE Gargantuan outsider (air, elemental, extraplanar)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +27
**Aura** stagnant (240 ft.)

##### Defense

**AC** 8, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 6 (+1 Dex, +1 dodge, –4 size)
**hp** 162 (13d10+91)
**Fort** +11, **Ref** +9, **Will** +15
**Defensive Abilities** gaseous, _[[universal monster rules/Natural Invisibility|natural invisibility]]_; **DR** 10/magic; **Immune** acid, elemental traits; **Resist** cold 10, electricity 10, fire 10
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to magic wind, _vulnerability_ to sonic

##### Offense
**Speed** fly 60 ft. (perfect)
**Melee** 2 hypoxic touches +9 touch (6d6 and slowed)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** hypoxic heart (DC 23, 6d6 and slowed)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +20)
At will—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 19) 
3/day—_[[spells/Crushing Despair|crushing despair]]_ (DC 21), quickened _[[spells/Murderous Command|murderous command]]_ (DC 18), quickened _[[spells/Oppressive Boredom|oppressive boredom]]_ (DC 19), quickened _[[spells/Paranoia|paranoia]]_ (DC 19) 
1/day—_[[spells/Envious Urge|envious urge]]_ (DC 23), _[[spells/Malicious Spite|malicious spite]]_ (DC 21), _[[spells/Song of Discord|song of discord]]_ (DC 22)

##### Statistics
**Str** —, **Dex** 13, **Con** 24, **Int** 9, **Wis** 24, **Cha** 24
**Base Atk** +13; **CMB** +17; **CMD** 29
**Feats** _[[feats/Alertness|Alertness]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_murderous command_, _oppressive boredom_, _paranoia_)
**Skills** Fly +19, Knowledge (planes) +15, Perception +27, Sense Motive +27, Stealth +5
**Languages** Auran, Common (can’t speak any language); _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any air (Plane of Air)
**Organization** solitary
**Treasure** incidental

### Special Abilities

**Gaseous (Ex)** A _[[monsters/Living Doldrums|living doldrums]]_ has a body composed of stagnant air. It can pass through small holes, narrow openings, and even mere cracks, but it cannot enter water or other liquid. It has no Strength score and cannot manipulate objects as a result.

**Hypoxic Heart (Ex)** A _living doldrums_ can _[[universal monster rules/Engulf|engulf]]_ foes, as per the universal monster ability. A creature engulfed by a _living doldrums_ doesn’t gain the _[[conditions/Pinned|pinned]]_ condition and can move normally, but it is still in danger of suffocating. A creature that begins its turn engulfed takes 6d6 points of damage and must succeed at a DC 23 Fortitude saving throw or be slowed (as per the spell _[[spells/Slow|slow]]_). This condition lasts as long as the creature is in the _living doldrums_’ space and for 1d4+1 rounds after it leaves. Creatures that don’t breathe take no damage from the _living doldrums_’ _engulf_ attack and do not risk being slowed. The _living doldrums_ extinguishes all nonmagical fires in its space. The save DC is Constitution-based.

**Hypoxic Touch (Ex)** A _living doldrums_’ touch attack hinders a creature’s ability to breathe. A creature that takes damage from this attack must succeed at a DC 23 Fortitude saving throw or be slowed (as per the spell _slow_) for 1 round. Creatures that don’t breathe are immune to this attack. The save DC is Constitution-based.

**_Natural Invisibility_ (Su)** This ability is constantly in effect, even when the _living doldrums_ is attacking, and is not subject to _[[spells/Invisibility Purge|invisibility purge]]_. Against foes that are unable to see _[[conditions/Invisible|invisible]]_ creatures, it gains an additional +20 bonus on Stealth checks when moving, or +40 when stationary; these bonuses are not included in the statistics above. Because of its size and pervasiveness within the area it occupies, a _living doldrums_ gains only a 20% miss chance due to its _[[spells/Invisibility|invisibility]]_.
**Stagnant Aura (Su)** The air within 240 feet of a _living doldrums_ is always still. Naturally occurring winds flow around this radius without disturbing anything inside (though precipitation falls as normal). Mundane attempts to create airflow within the aura (such as with a fan) are only half as strong as normal. Air elementals, gaseous creatures, and winged creatures (other than _living doldrums_) have their maneuverability reduced by one category within the aura. This aura does not inhibit magical air and wind effects.

**_Vulnerability_ to Magic Wind (Ex)** Damaging effects from moving air (such as a _[[classes/Kineticist|kineticist]]_’s air blast) deal 50% more damage to a _living doldrums_. A _living doldrums_ that begins its turn in the area of a nondamaging magical wind effect takes 1d6 points of damage per spell level of the effect.

##### Description

When people imagine elementals that thrive on the Plane of Air, they are most likely to think of the spirits of rushing wind and _[[items/Weapon Magic Abilities/Thundering|thundering]]_ storm, but not all air elementals are so dynamic. _Living doldrums_ are elementals that embody stagnant air. Those who can see _invisible_ creatures describe the _living doldrums_ as a cloud roughly 20 feet in diameter that resembles a knotted snake with a head at both ends. The _[[universal monster rules/Scent|scent]]_ of stale air lingers around a _living doldrums_, even if one only recently arrived to the area.
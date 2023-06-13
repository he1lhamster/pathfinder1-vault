---
cssclass: [monsters]
title1: Demon, Katpaskir
desc_short: Four clawed arms sprout from this fiend's chest like the limbs of a buried
  insect struggling to crawl free. Overlapping iridescent plates of chitin cascade
  down the monster's back, shrouding four membranous dragonfly wings.
title2: Katpaskir
CR: 18
sources:
- name: 'Pathfinder #78: City of Locusts'
  page: 86
  link: http://paizo.com/products/btpy93qo?Pathfinder-Adventure-Path-78-City-of-Locusts
XP: 153600
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 9
senses:
  darkvision: 60
  see invisibility: true
auras:
- name: distance distortion
  radius: 30
  DC: 26
AC:
  AC: 31
  touch: 15
  flat_footed: 26
  components:
    dex: 5
    natural: 16
HP:
  HP: 304
  long: 21d10+189
saves:
  fort: 16
  ref: 17
  will: 17
defensive_abilities:
- freedom of movement
DR:
- amount: 10
  weakness: cold iron and lawful
immunities:
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 29
speeds:
  base: 40
  burrow: 20
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: 2 claws +31 (2d6+10/19-20)
      entries:
      - - damage: 2d6+10
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 31
    - text: 4 talons +31 (1d8+10)
      entries:
      - - damage: 1d8+10
      count: 4
      attack: talons
      bonus:
      - 31
  special:
  - breaching
  - mirror of the tainted rift
spell_like_abilities:
  entries:
  - name: freedom of movement
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: blink
    source: default
    freq: At will
  - name: dimension door
    source: default
    freq: At will
  - name: dimensional anchor
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: plane shift
    source: default
    freq: At will
    DC: 23
  - name: banishment
    source: default
    freq: 3/day
    DC: 23
  - name: empowered disintegrate
    source: default
    freq: 3/day
    DC: 22
  - name: maze
    source: default
    freq: 3/day
  - name: gate
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 7
    summons:
    - name: fiendish army ant swarms
      amount: 1d4
      chance: 50%
  - name: summon monster IX
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 20
    concentration: 26
ability_scores:
  STR: 31
  DEX: 20
  CON: 28
  INT: 17
  WIS: 21
  CHA: 22
BAB: 21
CMB: 31
CMB_other: +35 sunder
CMD: 46
CMD_other: 48 vs. sunder
feats:
- name: Dimensional Agility
- name: Dimensional Assault
- name: Dimensional Dervish
- name: Dimensional Maneuvers
- name: Dimensional Savant
- name: Empower Spell-Like Ability (disintegrate)
- name: Greater Sunder
- name: Improved Critical (claw)
- name: Improved Initiative
- name: Improved Sunder
- name: Power Attack
skills:
  Bluff: 30
  Disable Device: 29
  Fly: 29
  Knowledge (arcana): 27
  Knowledge (planes): 31
  Perception: 37
  Sense Motive: 29
  Spellcraft: 27
  Use Magic Device: 30
  _racial_mods:
    Knowledge (planes):
      _: 4
    Perception:
      _: 8
languages:
- Abyssal
- Aklo
- Celestial
- Common
- telepathy 100 ft.
special_qualities:
- teleportation disruption
- warp sense
ecology:
  environment: any (Abyss)
  organization: solitary
  treasure_type: standard
special_abilities:
  Breaching (Su): When a katpaskir calls or summons a demon or creature with the fiendish
    simple template into an area where the summoned creature's entry would be blocked
    by a magical effect (such as magic circle against evil, forbiddance, or dimensional
    lock), it can force the caster or creator of the effect to attempt a caster level
    check against the katpaskir's spell resistance. On a failed check, the blocking
    effect is immediately and permanently negated.
  Distance Distortion (Su): Reality bends and warps within 30 feet of a katpaskir.
    The demon moves and attacks normally through this distorted area, but other creatures
    within this area treat all distances as if they were double the actual distance
    for all purposes, including movement, range for spells, and ranged attacks. In
    addition, a creature that begins its turn within this aura must succeed at a DC
    26 Will save or be slowed for 1 round (as the slow spell). Freedom of movement
    prevents the slow effect but not any of the other effects of the distance distortion
    aura. The save DC is Charisma-based.
  Mirror of the Tainted Rift (Su): When one or more creature with the celestial simple
    template is summoned as part of the spell or ability within 30 feet of a katpaskir,
    the katpaskir can, as an immediate action, summon an equal number of creatures
    of the same type with the fiendish simple template. If a good-aligned outsider
    is called or summoned within 30 feet of a katpaskir, it can duplicate the calling
    or summoning spell as an immediate action, calling or summoning one or more demons
    as if it had cast the same spell.
  Teleportation Disruption (Su): When a creature uses a teleportation effect to enter
    or leave a space within 30 feet of a katpaskir, the caster must immediately attempt
    a caster level check (DC equal to the katpaskir's spell resistance). On a failed
    check, the teleportation effect is negated. If it chooses, the katpaskir can instead
    redirect the arrival location of the teleportation effect to any unoccupied space
    within 120 feet.
  Warp Sense (Ex): A katpaskir can automatically sense disruptions in the planar fabric
    within 1 mile. The demon is immediately aware of any conjuration effect used within
    this area, and it also knows the direction and approximate distance. When a teleportation
    effect is used within 1 mile of a katpaskir (including arriving within this area
    from somewhere else), the demon can use clairaudience/clairvoyance as an immediate
    action centered on the point the teleportation effect originated from or the point
    the teleportation effect is directed at as long as the point is within 1 mile;
    if both points are within 1 mile, the katpaskir can use clairaudience/clairvoyance
    centered on both.
desc_long: Katpaskirs are a pox and pestilence upon not just the world, but reality
  itself. Just as bugs burrow into unwatched crevices, katpaskirs pry their way into
  other realms and dimensions. They gnaw and scratch and grind away at the edges of
  the universe, the planar junctures where the folds of creation bend in upon themselves.
  They have an uncanny sense for finding natural rifts, portals, and convergences,
  and they seek ever for ways to expand and untether these natural gates. By setting
  them loose to drift across the world, they unhinge the orderly substrate of the
  multiverse, casting all into primordial chaos as the planes unravel. Their voices
  are strange and echoing, like several voices sounding together, each distorted and
  cacophonous and rising and falling asynchronously in pitch and volume. When not
  actively engaged in a task, katpaskirs tend to stand perfectly still, with the exception
  of its insectlike limbs, which rhythmically stroke the air in front of them. When
  other creature come near-or if some teleporting creature triggers the demon's warp
  sense special ability-it snaps out of this self-imposed stasis, ready to attack.
  Katpaskirs are a little over 7 feet tall and weigh just less than 600 pounds.

---

# Demon, Katpaskir
Four clawed arms sprout from this fiend’s chest like the limbs of a buried insect struggling to crawl free. Overlapping iridescent plates of chitin cascade down the monster’s back, shrouding four membranous dragonfly wings.
**Source** Pathfinder #78: City of Locusts pg. 86
**XP** 153,600
CE Medium outsider (chaotic, demon, evil, extraplanar)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/See Invisibility|see invisibility]]_; Perception +37
**Aura** distance distortion (30 ft., DC 26)

##### Defense

**AC** 31, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+5 Dex, +16 natural)
**hp** 304 (21d10+189)
**Fort** +16, **Ref** +17, **Will** +17
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 10/cold iron and lawful; **Immune** electricity, poison; **Resist** acid 10, cold 10, fire 10; **SR** 29

##### Offense
**Speed** 40 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft., fly 60 ft. (average)
**Melee** 2 claws +31 (2d6+10/19–20), 4 talons +31 (1d8+10)
**Special Attacks** breaching, _[[items/Mundane/Mirror|mirror]]_ of the tainted rift
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +26)
Constant—_freedom of movement_, _see invisibility_
At will—_[[spells/Blink|blink]]_, _[[spells/Dimension Door|dimension door]]_, _[[spells/Dimensional Anchor|dimensional anchor]]_, greater teleport (self plus 50 lbs. of objects only), _[[spells/Plane Shift|plane shift]]_ (DC 23)
3/day—_[[spells/Banishment|banishment]]_ (DC 23), empowered _[[spells/Disintegrate|disintegrate]]_ (DC 22), _[[spells/Maze|maze]]_
1/day—_[[spells/Gate|gate]]_, _[[universal monster rules/Summon|summon]]_ (level 7, 1d4 fiendish army ant swarms 50%), _[[spells/Summon Monster IX|summon monster IX]]_

##### Statistics
**Str** 31, **Dex** 20, **Con** 28, **Int** 17, **Wis** 21, **Cha** 22
**Base Atk** +21; **CMB** +31 (+35 sunder); **CMD** 46 (48 vs. sunder)
**Feats** _[[feats/Dimensional Agility|Dimensional Agility]]_, _[[feats/Dimensional Assault|Dimensional Assault]]_, _[[feats/Dimensional Dervish|Dimensional Dervish]]_, _[[feats/Dimensional Maneuvers|Dimensional Maneuvers]]_, _[[feats/Dimensional Savant|Dimensional Savant]]_, _[[feats/Empower Spell-Like Ability|Empower Spell-Like Ability]]_ (_disintegrate_), _[[feats/Greater Sunder|Greater Sunder]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Bluff +30, Disable Device +29, Fly +29, Knowledge (arcana) +27, Knowledge (planes) +31, Perception +37, Sense Motive +29, Spellcraft +27, Use Magic Device +30; **Racial Modifiers** +4 Knowledge (planes), +8 Perception
**Languages** Abyssal, Aklo, Celestial, Common; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** teleportation _[[items/Weapon Magic Abilities/Disruption|disruption]]_, warp sense

##### Ecology

**Environment** any (Abyss)
**Organization** solitary
**Treasure** standard

### Special Abilities

**Breaching (Su)** When a katpaskir calls or summons a demon or creature with the fiendish simple template into an area where the summoned creature’s entry would be blocked by a magical effect (such as _[[spells/Magic Circle against Evil|magic circle against evil]]_, _[[spells/Forbiddance|forbiddance]]_, or _[[spells/Dimensional Lock|dimensional lock]]_), it can force the caster or creator of the effect to attempt a caster level check against the katpaskir’s _[[universal monster rules/Spell Resistance|spell resistance]]_. On a failed check, the blocking effect is immediately and permanently negated.

**Distance Distortion (Su)** Reality bends and warps within 30 feet of a katpaskir. The demon moves and attacks normally through this distorted area, but other creatures within this area treat all distances as if they were double the actual distance for all purposes, including movement, range for spells, and ranged attacks. In addition, a creature that begins its turn within this aura must succeed at a DC 26 Will save or be slowed for 1 round (as the _[[spells/Slow|slow]]_ spell). _Freedom of movement_ prevents the _slow_ effect but not any of the other effects of the distance distortion aura. The save DC is Charisma-based.

**_Mirror_ of the Tainted Rift (Su)** When one or more creature with the celestial simple template is summoned as part of the spell or ability within 30 feet of a katpaskir, the katpaskir can, as an immediate action, _summon_ an equal number of creatures of the same type with the fiendish simple template. If a good-aligned outsider is _[[items/Weapon Magic Abilities/Called|called]]_ or summoned within 30 feet of a katpaskir, it can duplicate the calling or summoning spell as an immediate action, calling or summoning one or more demons as if it had cast the same spell.

**Teleportation _Disruption_ (Su)** When a creature uses a teleportation effect to enter or leave a space within 30 feet of a katpaskir, the caster must immediately attempt a caster level check (DC equal to the katpaskir’s _spell resistance_). On a failed check, the teleportation effect is negated. If it chooses, the katpaskir can instead redirect the arrival location of the teleportation effect to any unoccupied space within 120 feet.

**Warp Sense (Ex)** A katpaskir can automatically sense disruptions in the _[[items/Weapon Magic Abilities/Planar|planar]]_ fabric within 1 mile. The demon is immediately aware of any conjuration effect used within this area, and it also knows the direction and approximate distance. When a teleportation effect is used within 1 mile of a katpaskir (including arriving within this area from somewhere else), the demon can use clairaudience/clairvoyance as an immediate action centered on the point the teleportation effect originated from or the point the teleportation effect is directed at as long as the point is within 1 mile; if both points are within 1 mile, the katpaskir can use clairaudience/clairvoyance centered on both.

##### Description

Katpaskirs are a pox and pestilence upon not just the world, but reality itself. Just as bugs _burrow_ into unwatched crevices, katpaskirs pry their way into other realms and dimensions. They gnaw and scratch and grind away at the edges of the universe, the _planar_ junctures where the folds of creation bend in upon themselves. They have an uncanny sense for finding natural rifts, portals, and convergences, and they seek ever for ways to expand and untether these natural gates. By setting them loose to drift across the world, they unhinge the orderly substrate of the multiverse, casting all into primordial chaos as the planes unravel. Their voices are strange and echoing, like several voices sounding together, each distorted and cacophonous and rising and falling asynchronously in pitch and volume. When not actively engaged in a task, katpaskirs tend to stand perfectly still, with the exception of its insectlike limbs, which rhythmically stroke the air in front of them. When other creature come near—or if some teleporting creature triggers the demon’s warp sense special ability—it snaps out of this self-imposed stasis, ready to attack. Katpaskirs are a little over 7 feet tall and weigh just less than 600 pounds.
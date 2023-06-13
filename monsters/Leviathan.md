---
cssclass: [monsters]
title1: Leviathan
desc_short: This impossibly enormous, whalelike monstrosity glares with a hundred
  red eyes, its cavernous maw lined with rows of sharp teeth.
title2: Leviathan
CR: 30
sources:
- name: Planar Adventures
  page: 240
  link: http://paizo.com/products/btpya1am
XP: 9830400
alignment: N
size: Colossal
type: magical beast
subtypes:
- water
initiative:
  bonus: 15
senses:
  low-light vision: true
  scent: true
  see in darkness: true
  true seeing: true
AC:
  AC: 48
  touch: 13
  flat_footed: 37
  components:
    dex: 11
    natural: 35
    size: -8
HP:
  HP: 765
  long: 34d10+578
saves:
  fort: 36
  ref: 30
  will: 24
defensive_abilities:
- all-around vision
- recovery
DR:
- amount: 20
  weakness: epic
immunities:
- ability damage
- ability drain
- bleed
- cold
- death effects
- disease
- energy drain
- fear
- paralysis
- sleep
resistances:
  acid: 30
  electricity: 30
  fire: 30
SR: 41
speeds:
  fly: 100
  fly_maneuverability: poor
  swim: 200
attacks:
  melee:
  - - text: bite +46 (10d8+30/19-20 plus disjoining bite and grab)
      entries:
      - - damage: 10d8+30
          crit_range: 19-20
        - effect: disjoining bite
        - effect: grab
      attack: bite
      bonus:
      - 46
    - text: slam +46 (10d6+30/19-20)
      entries:
      - - damage: 10d6+30
          crit_range: 19-20
      attack: slam
      bonus:
      - 46
    - text: tail slap +41 (6d10+30/19-20 plus dimensional vortex)
      entries:
      - - damage: 6d10+30
          crit_range: 19-20
        - effect: dimensional vortex
      attack: tail slap
      bonus:
      - 41
  special:
  - disjoining bite
  - eye beams
  - fast swallow
  - hurl foe
  - inhalation
  - pierce immunities
  - swallow whole
space: 100
reach: 100
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: plane shift
    source: default
    freq: 3/day
    DC: 27
  - name: tsunami
    source: default
    freq: 1/day
    DC: 29
  sources:
  - name: default
    CL: 30
    concentration: 40
ability_scores:
  STR: 50
  DEX: 33
  CON: 44
  INT: 15
  WIS: 32
  CHA: 31
BAB: 34
CMB: 62
CMB_other: +66 bull rush
CMD: 83
CMD_other: 85 vs. bull rush, can't be tripped
feats:
- name: Combat Reflexes
- name: Critical Focus
- name: Greater Bull Rush
- name: Greater Vital Strike
- name: Hover
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Improved Critical (slam)
- name: Improved Critical (tail slap)
- name: Improved Initiative
- name: Improved Iron Will
- name: Improved Vital Strike
- name: Iron Will
- name: Power Attack
- name: Staggering Critical
- name: Vital Strike
- name: Wingover
skills:
  Fly: 36
  Perception: 48
  Sense Motive: 45
  Swim: 65
languages:
- Aklo
- Common
- Sylvan
special_qualities:
- labyrinthine innards
- massive
- planar acclimation
- powerful blows (bite, slam, tail slap)
ecology:
  environment: any oceans (First World)
  organization: solitary (unique)
  treasure_type: triple
  treasure:
  - consists of swallowed treasure
special_abilities:
  Dimensional Vortex (Su): When Leviathan strikes a creature with its tail slap, the
    overwhelming blow tears at the underlying structure of reality. Leviathan can
    use its plane shift spell-like ability on creatures so struck as a free action;
    these uses of plane shift do not count against the daily limit of the spell-like
    ability.
  Disjoining Bite (Su): When Leviathan bites a creature, its jaws attempt to destroy
    magical effects in place on the target. The creature bitten must succeed at a
    DC 37 Will save or all spell effects in place on it are immediately destroyed
    (as per dispel magic). Leviathan can disjoin an existing spell effect by biting
    it, although doing so exposes Leviathan to the spell's effect as it bites. Likewise,
    Leviathan can attempt to disjoin a magic item by biting it. On a hit, the item
    must succeed at a DC 37 Will save or be permanently destroyed-note that even if
    the disjunction doesn't destroy the item, the damage dealt by Leviathan's bite
    might be sufficient to destroy the item. Leviathan's disjoining bite cannot destroy
    artifacts. The save DC is Charisma-based.
  Eye Beams (Su): As a standard action, Leviathan can fire prismatic beams of rippling
    light from its hundred eyes out to a range of 1,000 feet. While Leviathan cannot
    target a single creature with more than one eye beam at a time, it can split its
    100 beams any way it wants against visible targets in range. When Leviathan attacks
    with its eye beams, it must make a ranged touch attack with a +37 bonus to hit
    a target. On a hit, a creature must succeed at a DC 37 Will save or its mind is
    emptied, becoming affected as if by feeblemind, and its thoughts are drawn into
    Leviathan's own mind. As long as Leviathan is active, this effect can be removed
    only via miracle or wish; if Leviathan is defeated and forced into its comatose
    state (see Recovery below), the feeblemind effect can be cured as normal. Once
    a creature succeeds at a save against Leviathan's eye beams, it is immune to the
    eye beams for 24 hours. The save DC is Charisma-based.
  Flight (Su): Leviathan's ability to “swim” through the air is treated as a supernatural
    form of flight.
  Hurl Foe (Ex): When Leviathan damages a Huge or smaller foe with one of its natural
    attacks, it can attempt a combat maneuver check to hurl the foe as part of that
    attack. On a successful check, the foe is knocked back 10 feet in a direction
    of Leviathan's choice and falls prone. The distance the foe is hurled increases
    by 10 feet for every 5 points by which Leviathan's check result exceeds the foe's
    CMD. If an obstacle stops the hurled creature before it travels the whole distance,
    the hurled foe and the obstacle struck each take 1d6 points of damage per 10 feet
    of distance remaining, and the foe is knocked prone in the space adjacent to the
    obstacle.
  Inhalation (Ex): Once every 1d4 rounds as a standard action, Leviathan can inhale
    a massive amount of water, affecting an 80-foot-long cone. Huge or smaller creatures
    within this area of effect must each succeed at a DC 44 Reflex save to avoid being
    drawn into Leviathan's maw and automatically swallowed whole. The save DC is Constitution-based.
  Labyrinthine Innards (Su): Creatures swallowed by Leviathan find themselves separated
    from all other swallowed creatures in a twisting maze of passages within the Tane's
    digestive system. A swallowed creature can move freely through this fleshy maze
    and takes no damage from being swallowed, but it can't damage Leviathan from within
    if it attempts to escape. Instead, swallowed creatures must find an exit via one
    of the monster's hundred tear ducts by succeeding at a DC 20 Intelligence check
    as a full-round action, similar to maze. Teleportation effects do not function
    inside of Leviathan.
  Massive (Ex): Because Leviathan is so massive, it treats terrain features that form
    difficult terrain as normal terrain, though immense features like cities or forests
    still function as difficult terrain for the monster. A Huge or smaller creature
    can move through squares occupied by Leviathan and vice versa. Leviathan can make
    attacks of opportunity only against foes that are Huge or larger and can be flanked
    only by Huge or larger foes. Leviathan gains a bonus for being on higher ground
    only if its entire space is on higher ground than that of its target. It is possible
    for a Huge or smaller creature to climb Leviathan-this requires a successful DC
    30 Climb check, and unlike the normal rules regarding Leviathan and attacks of
    opportunity, a Small or larger creature that climbs Leviathan's body provokes
    an attack of opportunity from the monster.
  Pierce Immunities (Ex): Leviathan ignores all forms of damage reduction when it
    attacks a foe with its natural weapons, including DR/epic and DR/-.
  Planar Acclimation (Ex): Leviathan is always considered to be on its home plane,
    regardless of what plane it finds itself upon. It never gains the extraplanar
    subtype.
  Recovery (Ex): At the end of its turn, Leviathan can automatically shake off any
    one adverse condition other than dead. If it is affected by multiple adverse conditions,
    it chooses which one to end that round. Should Leviathan be slain, it is instead
    transported across time and space to a hidden spot in the First World's oceans
    at a point 1d100 years in the future, fully recovered but immobile. Leviathan
    awakens a century after the date of its “death,” but if its immobile body is discovered
    before it wakes from this deathlike state, it can be killed forever.
desc_long: |-
  The mighty Leviathan is the most powerful of the Tane, a group of destructive servitors of the Eldest. Left to its own devices, Leviathan remains in a slumber lasting for millennia or spends its waking time singing in the vast deeps of the First World's oceans. But the Eldest's planar upheavals, whims, or the ill-advised aggression of fools can arouse Leviathan as a weapon of devastation. Once awakened, Leviathan leaves cities and even entire nations destroyed in its planar wake, though it preserves the thoughts and memories of many of the fallen within its own mind, composing elegies to the lost. Some lucky few are spared Leviathan's wrath by gaining refuge within Zanziveil, the City of the Spared, a resplendent city of refugees ruled by a mysterious masked woman named Zizipal. Zanziveil itself exists in a strange demiplane accessible only via Leviathan's labyrinthine entrails, and many believe that Zizipal is a manifestation of Leviathan's remorse and curiosity.

   Over the eons, Leviathan has visited countless Material Plane worlds. Although often little remains physically of those Leviathan destroys, tales of the gargantuan creature's visits have a way of enduring in a society's oral history. As a result, many otherwise unconnected worlds share curiously similar mythologies of ancient cities or civilizations being destroyed by the legendary creature.

   Leviathan is an immense, whalelike beast, measuring nearly 150 feet long from head to tail.

---

# Leviathan
This impossibly enormous, whalelike monstrosity glares with a hundred red eyes, its cavernous maw lined with rows of sharp teeth.
**Source** _[[items/Weapon Magic Abilities/Planar|Planar]]_ Adventures pg. 240
**XP** 9,830,400

N Colossal magical beast (water)
**Init** +15; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_, _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/True Seeing|true seeing]]_; Perception +48

##### Defense

**AC** 48, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 37 (+11 Dex, +35 natural, –8 size)
**hp** 765 (34d10+578)
**Fort** +36, **Ref** +30, **Will** +24
**Defensive Abilities** _[[universal monster rules/All-Around Vision|all-around vision]]_, recovery; **DR** 20/epic; **Immune** ability damage, ability drain, _[[universal monster rules/Bleed|bleed]]_, cold, death effects, disease, _[[universal monster rules/Energy Drain|energy drain]]_, _[[universal monster rules/Fear|fear]]_, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **Resist** acid 30, electricity 30, fire 30; **SR** 41

##### Offense
**Speed** fly 100 ft. (poor), swim 200 ft.
**Melee** bite +46 (10d8+30/19–20 plus _[[items/Weapon Magic Abilities/Disjoining|disjoining]]_ bite and _[[universal monster rules/Grab|grab]]_), slam +46 (10d6+30/19–20), tail slap +41 (6d10+30/19–20 plus dimensional _[[spells/Vortex|vortex]]_)
**Space** 100 ft., **Reach** 100 ft.
**Special Attacks** _disjoining_ bite, eye beams, _[[universal monster rules/Fast Swallow|fast swallow]]_, hurl foe, inhalation, pierce immunities, _[[universal monster rules/Swallow Whole|swallow whole]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 30th; concentration +40)
Constant—_true seeing_
3/day—_[[spells/Plane Shift|plane shift]]_ (DC 27)
1/day—_[[spells/Tsunami|tsunami]]_ (DC 29)

##### Statistics
**Str** 50, **Dex** 33, **Con** 44, **Int** 15, **Wis** 32, **Cha** 31
**Base Atk** +34; **CMB** +62 (+66 bull rush); **CMD** 83 (85 vs. bull rush, can’t be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Bull Rush|Greater Bull Rush]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite, slam, tail slap), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Wingover|Wingover]]_
**Skills** Fly +36, Perception +48, Sense Motive +45, Swim +65
**Languages** Aklo, Common, Sylvan
**SQ** labyrinthine innards, massive, _planar_ acclimation, powerful blows (bite, slam, tail slap)

##### Ecology

**Environment** any oceans (First World)
**Organization** solitary (unique)
**Treasure** triple (consists of swallowed treasure)

### Special Abilities

**Dimensional _Vortex_ (Su)** When _[[monsters/Leviathan|Leviathan]]_ strikes a creature with its tail slap, the overwhelming blow tears at the underlying structure of reality. _Leviathan_ can use its _plane shift_ spell-like ability on creatures so struck as a free action; these uses of _plane shift_ do not count against the daily limit of the spell-like ability.

**_Disjoining_ Bite (Su)** When _Leviathan_ bites a creature, its jaws attempt to destroy magical effects in place on the target. The creature bitten must succeed at a DC 37 Will save or all spell effects in place on it are immediately destroyed (as per _[[spells/Dispel Magic|dispel magic]]_). _Leviathan_ can disjoin an existing spell effect by biting it, although doing so exposes _Leviathan_ to the spell’s effect as it bites. Likewise, _Leviathan_ can attempt to disjoin a magic item by biting it. On a hit, the item must succeed at a DC 37 Will save or be permanently destroyed—note that even if the disjunction doesn’t destroy the item, the damage dealt by _Leviathan_’s bite might be sufficient to destroy the item. _Leviathan_’s _disjoining_ bite cannot destroy artifacts. The save DC is Charisma-based.

**Eye Beams (Su)** As a standard action, _Leviathan_ can fire prismatic beams of rippling light from its hundred eyes out to a range of 1,000 feet. While _Leviathan_ cannot target a single creature with more than one eye beam at a time, it can _[[universal monster rules/Split|split]]_ its 100 beams any way it wants against visible targets in range. When _Leviathan_ attacks with its eye beams, it must make a ranged touch attack with a +37 bonus to hit a target. On a hit, a creature must succeed at a DC 37 Will save or its mind is emptied, becoming affected as if by _[[spells/Feeblemind|feeblemind]]_, and its thoughts are drawn into _Leviathan_’s own mind. As long as _Leviathan_ is active, this effect can be removed only via _[[spells/Miracle|miracle]]_ or _[[spells/Wish|wish]]_; if _Leviathan_ is defeated and forced into its comatose state (see Recovery below), the _feeblemind_ effect can be cured as normal. Once a creature succeeds at a save against _Leviathan_’s eye beams, it is immune to the eye beams for 24 hours. The save DC is Charisma-based.

**_[[universal monster rules/Flight|Flight]]_ (Su)** _Leviathan_’s ability to “swim” through the air is treated as a supernatural form of _flight_.

**Hurl Foe (Ex)** When _Leviathan_ damages a Huge or smaller foe with one of its _[[universal monster rules/Natural Attacks|natural attacks]]_, it can attempt a combat maneuver check to hurl the foe as part of that attack. On a successful check, the foe is knocked back 10 feet in a direction of _Leviathan_’s choice and falls _[[conditions/Prone|prone]]_. The distance the foe is hurled increases by 10 feet for every 5 points by which _Leviathan_’s check result exceeds the foe’s CMD. If an obstacle stops the hurled creature before it travels the whole distance, the hurled foe and the obstacle struck each take 1d6 points of damage per 10 feet of distance remaining, and the foe is knocked _prone_ in the space adjacent to the obstacle.

**Inhalation (Ex)** Once every 1d4 rounds as a standard action, _Leviathan_ can inhale a massive amount of water, affecting an 80-foot-long cone. Huge or smaller creatures within this area of effect must each succeed at a DC 44 Reflex save to avoid being drawn into _Leviathan_’s maw and automatically swallowed whole. The save DC is Constitution-based.

**Labyrinthine Innards (Su)** Creatures swallowed by _Leviathan_ find themselves separated from all other swallowed creatures in a twisting _[[spells/Maze|maze]]_ of passages within the Tane’s digestive system. A swallowed creature can move freely through this fleshy _maze_ and takes no damage from being swallowed, but it can’t damage _Leviathan_ from within if it attempts to escape. Instead, swallowed creatures must find an exit via one of the monster’s hundred tear ducts by succeeding at a DC 20 Intelligence check as a full-round action, similar to _maze_. Teleportation effects do not function inside of _Leviathan_.

**Massive (Ex)** Because _Leviathan_ is so massive, it treats terrain features that form difficult terrain as normal terrain, though immense features like cities or forests still function as difficult terrain for the monster. A Huge or smaller creature can move through squares occupied by _Leviathan_ and vice versa. _Leviathan_ can make attacks of opportunity only against foes that are Huge or larger and can be flanked only by Huge or larger foes. _Leviathan_ gains a bonus for being on higher ground only if its entire space is on higher ground than that of its target. It is possible for a Huge or smaller creature to _[[universal monster rules/Climb|climb]]_ _Leviathan_—this requires a successful DC 30 _Climb_ check, and unlike the normal rules regarding _Leviathan_ and attacks of opportunity, a Small or larger creature that climbs _Leviathan_’s body provokes an attack of opportunity from the monster.

**Pierce Immunities (Ex)** _Leviathan_ ignores all forms of _[[universal monster rules/Damage Reduction|damage reduction]]_ when it attacks a foe with its natural weapons, including DR/epic and DR/—.

**_Planar_ Acclimation (Ex)** _Leviathan_ is always considered to be on its home plane, regardless of what plane it finds itself upon. It never gains the extraplanar subtype.

**Recovery (Ex)** At the end of its turn, _Leviathan_ can automatically shake off any one adverse condition other than dead. If it is affected by multiple adverse conditions, it chooses which one to end that round. Should _Leviathan_ be slain, it is instead transported across time and space to a hidden spot in the First World’s oceans at a point 1d100 years in the future, fully recovered but immobile. _Leviathan_ awakens a century after the date of its “death,” but if its immobile body is discovered before it wakes from this deathlike state, it can be killed forever.

##### Description

The mighty _Leviathan_ is the most powerful of the Tane, a group of destructive servitors of the Eldest. Left to its own devices, _Leviathan_ remains in a slumber lasting for millennia or spends its waking time _[[items/Armor Magic Abilities/Singing|singing]]_ in the vast deeps of the First World’s oceans. But the Eldest’s _planar_ upheavals, whims, or the ill-advised aggression of fools can arouse _Leviathan_ as a weapon of devastation. Once awakened, _Leviathan_ leaves cities and even entire nations destroyed in its _planar_ wake, though it preserves the thoughts and memories of many of the _[[monsters/Fallen|fallen]]_ within its own mind, composing elegies to the lost. Some _[[feats/Lucky|lucky]]_ few are spared _Leviathan_’s wrath by gaining _[[spells/Refuge|refuge]]_ within Zanziveil, the City of the Spared, a resplendent city of refugees ruled by a mysterious masked woman named Zizipal. Zanziveil itself exists in a strange demiplane accessible only via _Leviathan_’s labyrinthine entrails, and many believe that Zizipal is a manifestation of _Leviathan_’s remorse and curiosity.

Over the eons, _Leviathan_ has visited countless Material Plane worlds. Although often little remains physically of those _Leviathan_ destroys, tales of the gargantuan creature’s visits have a way of enduring in a society’s oral history. As a result, many otherwise unconnected worlds share curiously similar mythologies of ancient cities or civilizations being destroyed by the legendary creature.

_Leviathan_ is an immense, whalelike beast, measuring nearly 150 feet long from head to tail.
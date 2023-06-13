---
cssclass: [monsters]
second_statblock: true
title1: Goblin, Goblin Vulture Pilot
title2: Goblin Vulture Pilot
CR: 3
sources:
- name: Monster Codex
  page: 109
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 800
race: Goblin
classes:
- alchemist (winged marauder) 4 (Pathfinder RPG Advanced Player's Guide 26, see page
  104)
alignment: NE
size: Small
type: humanoid
subtypes:
- goblinoid
initiative:
  bonus: 4
senses:
  darkvision: 60
AC:
  AC: 21
  touch: 15
  flat_footed: 17
  components:
    armor: 4
    dex: 4
    natural: 2
    size: 1
HP:
  HP: 38
  long: 4d8+17
saves:
  fort: 5
  ref: 8
  will: 2
  other: +2 against poison
speeds:
  base: 30
attacks:
  melee:
  - - text: dagger +3 (1d3-1/19-20)
      entries:
      - - damage: 1d3-1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 3
  ranged:
  - - text: bomb +9 (2d6+3 fire plus catch fire)
      entries:
      - - damage: 2d6+3
          type: fire
        - effect: catch fire
      attack: bomb
      bonus:
      - 9
  special:
  - bomb 7/day (2d6+3 fire and catch fire, DC 15, 10-ft. radius)
spells:
  entries:
  - name: false life
    source: Alchemist
    level: 2
  - superscripts:
    - UC
    name: touch injection
    source: Alchemist
    level: 2
  - superscripts:
    - APG
    name: bomber's eye
    source: Alchemist
    level: 1
  - name: bouncy body
    source: Alchemist
    level: 1
  - name: shield
    source: Alchemist
    level: 1
  - name: true strike
    source: Alchemist
    level: 1
  sources:
  - name: Alchemist
    type: prepared
    CL: 4
tactics:
  Before Combat: The vulture pilot drinks a bouncy body extract, a false life extract,
    and a potion of barkskin, then feeds a potion of barkskin to her vulture companion.
  During Combat: The pilot uses her bombs to scatter opponents on the ground, tanglefoot
    bags to hold tasty prizes in place, and alchemical splash weapons as the situation
    warrants.
  Base Statistics: Without barkskin and false life, the vulture pilot's statistics
    are AC 19, touch 15, flat-footed 15; hp 29.
ability_scores:
  STR: 8
  DEX: 18
  CON: 13
  INT: 16
  WIS: 12
  CHA: 6
BAB: 3
CMB: 1
CMD: 15
feats:
- name: Brew Potion
- name: Mounted Archery
- name: Mounted Combat
- name: Throw Anything
skills:
  Acrobatics: 8
  Climb: 3
  Craft (alchemy): 10
  Handle Animal: 2
  Perception: 8
  Ride: 12
  Stealth: 16
  _racial_mods:
    Ride:
      _: 4
    Stealth:
      _: 4
languages:
- Common
- Giant
- Gnoll
- Goblin
special_qualities:
- alchemy (alchemy crafting +4, identify potions)
- discoveries (explosive bomb, sipping pet)
- poison use
- swift alchemy
gear:
  combat:
  - potions of barkskin (2)
  - potions of cure light wounds (2)
  - acid (2)
  - alchemist's fire (2)
  - tanglefoot bags (2)
  other:
  - mwk mithral chain shirt
  - dagger
  - sunrods (2)
  - 293 gp
ecology:
  environment: temperate forest and plains (usually coastal regions)
desc_long: ''

---

# Goblin, Goblin Vulture Pilot

**Source** Monster Codex pg. 109
**XP** 800
_[[monsters/Goblin|Goblin]]_ _[[classes/Alchemist|alchemist]]_ (winged marauder) 4 (Pathfinder RPG Advanced Player’s Guide 26, see page 104)

NE Small humanoid (goblinoid)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +8

##### Defense

**AC** 21, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+4 armor, +4 Dex, +2 natural, +1 size)
**hp** 38 (4d8+17)
**Fort** +5, **Ref** +8, **Will** +2; +2 against poison

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +3 (1d3–1/19–20)
**Ranged** bomb +9 (2d6+3 fire plus catch fire)
**Special Attacks** bomb 7/day (2d6+3 fire and catch fire, DC 15, 10-ft. radius)
**_Alchemist_ Extracts Prepared **(CL 4th)
2nd—_[[spells/False Life|false life]]_, _[[spells/Touch Injection|touch injection]]_
1st—bomber’s eye, _[[spells/Bouncy Body|bouncy body]]_, _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_

### Tactics

**Before Combat** The _[[monsters/Vulture|vulture]]_ pilot drinks a _bouncy body_ extract, a _false life_ extract, and a potion of _[[spells/Barkskin|barkskin]]_, then feeds a potion of _barkskin_ to her _vulture_ companion.
 **During Combat** The pilot uses her bombs to scatter opponents on the ground, tanglefoot bags to hold tasty prizes in place, and alchemical splash weapons as the situation warrants.
 **Base Statistics** Without _barkskin_ and _false life_, the _vulture_ pilot’s statistics are **AC **19, touch 15, _flat-footed_ 15; **hp **29.

##### Statistics
**Str** 8, **Dex** 18, **Con** 13, **Int** 16, **Wis** 12, **Cha** 6
**Base Atk** +3; **CMB** +1; **CMD** 15
**Feats** _[[feats/Brew Potion|Brew Potion]]_, _[[feats/Mounted Archery|Mounted Archery]]_, _[[feats/Mounted Combat|Mounted Combat]]_, _[[feats/Throw Anything|Throw Anything]]_
**Skills** Acrobatics +8, _[[universal monster rules/Climb|Climb]]_ +3, Craft (alchemy) +10, Handle Animal +2, Perception +8, Ride +12, Stealth +16; **Racial Modifiers** +4 Ride, +4 Stealth
**Languages** Common, Giant, _[[monsters/Gnoll|Gnoll]]_, _Goblin_
**SQ** alchemy (alchemy crafting +4, _[[spells/Identify|identify]]_ potions), discoveries (explosive bomb, sipping pet), poison use, swift alchemy
**Combat Gear** potions of _barkskin_ (2), potions of _[[spells/Cure Light Wounds|cure light wounds]]_ (2), acid (2), _alchemist_’s fire (2), tanglefoot bags (2); **Other Gear** mwk mithral _[[items/Armor/Chain shirt|chain shirt]]_, _dagger_, sunrods (2), 293 gp

##### Ecology

**Environment** temperate forest and plains (usually coastal regions)

##### Description

## Giant _Vulture_

Giant _vulture_ animal companion
 N Medium animal
 **Init** +3; Senses _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +7

##### Defense

**AC** 19, touch 13, _flat-footed_ 16 (+3 Dex, +6 natural)
 **hp** 26 (4d8+8)
 **Fort **+6, **Ref **+7, **Will **+3, +4 vs. disease
 **Defensive Abilities** evasion

##### Offense
**Speed **10 ft., fly 50 ft. (average)
 **Melee **bite +5 (1d8+3)

### Tactics

**Base Statistics** Without _barkskin_, the giant _vulture_’s statistics are **AC **17, touch 13, _flat-footed_ 14.

##### Statistics
**Str **14, **Dex **16, **Con **14, **Int **2, **Wis **15, **Cha **7
 **Base Atk** +3; **CMB **+5; **CMD **18
 **Feats **_[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Power Attack|Power Attack]]_
 **Skills **Fly +10, Perception +7
 **SQ **tricks (attack, come, defend, down, _[[npcs/Guard|guard]]_, stay)
 **Gear **flying straps

Strapped to her giant _vulture_ companion, the _goblin_ _vulture_ pilot is a peerless scout and saboteur. Enemies find _goblin_ _vulture_ pilots tough to _[[feats/Pin Down|pin down]]_ as they lob explosive bombs from the air. _Vulture_ pilots are braver, more disciplined, and more patient than most goblins, as they have to sneak into giant _vulture_ nests to steal eggs, resist the temptation to eat those eggs, and raise the hatchlings to be loyal mounts. Many pilots die in flying accidents; the _[[feats/Lucky|lucky]]_ ones often discover how to craft extracts of _bouncy body_, _[[spells/Levitate|levitate]]_, or similar effects to help them survive the inevitable crashes.

_Goblin_ _vulture_ pilots take great pride in their abilities, and often wear their mounts’ feathers as headdresses or paint themselves with guano as marks of _[[spells/Status|status]]_.
---
cssclass: [monsters]
title1: Dragon (Imperial, Underworld), Adult Underworld Dragon
title2: Adult Underworld Dragon
CR: 11
sources:
- name: Bestiary 3
  page: 102
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 12800
alignment: LE
size: Large
type: dragon
subtypes:
- fire
initiative:
  bonus: 4
senses:
  dragon senses: true
  smoke vision: true
auras:
- name: frightful presence
  radius: 180
  DC: 20
AC:
  AC: 29
  touch: 9
  flat_footed: 29
  components:
    natural: 20
    size: -1
HP:
  HP: 161
  long: 14d12+70
saves:
  fort: 14
  ref: 9
  will: 12
DR:
- amount: 5
  weakness: magic
immunities:
- fire
- paralysis
- sleep
SR: 22
weaknesses:
- vulnerability to cold
speeds:
  base: 40
  burrow: 40
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +22 (2d6+12)
      entries:
      - - damage: 2d6+12
      attack: bite
      bonus:
      - 22
    - text: 2 claws +22 (1d8+8/19-20)
      entries:
      - - damage: 1d8+8
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 22
    - text: gore +21 (1d8+12)
      entries:
      - - damage: 1d8+12
      attack: gore
      bonus:
      - 21
    - text: tail slap +16 (1d8+12)
      entries:
      - - damage: 1d8+12
      attack: tail slap
      bonus:
      - 16
  special:
  - adamantine claws
  - breath weapon (80-ft. line, 12d6 fire damage, DC 22)
space: 10
reach: 5
reach_other: 10 ft. with bite and gore
spell_like_abilities:
  entries:
  - name: soften earth and stone
    source: default
    freq: At will
  - name: spike stones
    source: default
    freq: At will
    DC: 17
  - name: stone shape
    source: default
    freq: At will
  sources:
  - name: default
    CL: 14
    concentration: 17
spells:
  entries:
  - name: flaming sphere
    source: '?'
    level: 2
    DC: 15
  - name: scorching ray
    source: '?'
    level: 2
  - name: burning hands
    source: '?'
    level: 1
    DC: 14
  - name: cause fear
    source: '?'
    level: 1
    DC: 14
  - name: magic missile
    source: '?'
    level: 1
  - name: ray of enfeeblement
    source: '?'
    level: 1
    DC: 14
  - name: acid splash
    source: '?'
    level: 0
  - name: bleed
    source: '?'
    level: 0
    DC: 13
  - name: detect magic
    source: '?'
    level: 0
  - name: flare
    source: '?'
    level: 0
    DC: 13
  - name: read magic
    source: '?'
    level: 0
  - name: resistance
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 5
    concentration: 8
    slots:
      2: 5
      1: 7
      0: at-will
ability_scores:
  STR: 27
  DEX: 10
  CON: 21
  INT: 16
  WIS: 17
  CHA: 16
BAB: 14
CMB: 23
CMD: 33
CMD_other: 37 vs. trip
feats:
- name: Improved Critical (claws)
- name: Improved Initiative
- name: Improved Natural Armor
- name: Lunge
- name: Skill Focus (Stealth)
- name: Weapon Focus (bite)
- name: Weapon Focus (claw)
skills:
  Appraise: 20
  Bluff: 20
  Climb: 25
  Fly: 11
  Intimidate: 20
  Knowledge (dungeoneering): 20
  Knowledge (geography): 20
  Perception: 20
  Stealth: 19
languages:
- Common
- Draconic
- Ignan
- Terran
special_qualities:
- change shape
- underworld burrower
ecology:
  environment: any underground
  organization: solitary
  treasure_type: triple
desc_long: Underworld dragons-also called futsanglungs-are calculating, greedy creatures
  that carve great labyrinthine tunnels beneath the world, defending their hidden
  treasures. Preferring the earth to the heavens, they channel the fires of the world's
  core within their twisting, stonelike bodies and through flaming breath hot enough
  to turn granite into slag.

---

# Dragon (Imperial, Underworld), Adult Underworld Dragon

**Source** Bestiary 3 pg. 102
**XP** 12,800

LE Large dragon (fire)
**Init** +4; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_, smoke _[[spells/Vision|vision]]_; Perception +20
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 20)

##### Defense

**AC** 29, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 29 (+20 natural, –1 size)
**hp** 161 (14d12+70)
**Fort** +14, **Ref** +9, **Will** +12
**DR** 5/magic; **Immune** fire, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 22
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to cold

##### Offense
**Speed** 40 ft., _[[universal monster rules/Burrow|burrow]]_ 40 ft., fly 200 ft. (poor)
**Melee** bite +22 (2d6+12), 2 claws +22 (1d8+8/19–20), gore +21 (1d8+12), tail slap +16 (1d8+12)
**Space** 10 ft., **Reach** 5 ft. (10 ft. with bite and gore)
**Special Attacks** adamantine claws, _[[universal monster rules/Breath Weapon|breath weapon]]_ (80-ft. line, 12d6 fire damage, DC 22)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +17)
At will—_[[spells/Soften Earth and Stone|soften earth and stone]]_, _[[spells/Spike Stones|spike stones]]_ (DC 17), _[[spells/Stone Shape|stone shape]]_
**Spells Known **(CL 5th; concentration +8)
2nd (5/day)—_[[spells/Flaming Sphere|flaming sphere]]_ (DC 15), _[[spells/Scorching Ray|scorching ray]]_
1st (7/day)—_[[spells/Burning Hands|burning hands]]_ (DC 14), _[[spells/Cause Fear|cause fear]]_ (DC 14), _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 14)
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[universal monster rules/Bleed|bleed]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 13), _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_

##### Statistics
**Str** 27, **Dex** 10, **Con** 21, **Int** 16, **Wis** 17, **Cha** 16
**Base Atk** +14; **CMB** +23; **CMD** 33 (37 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Improved Critical|Improved Critical]]_ (claws), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Natural Armor|Improved Natural Armor]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth), _[[feats/Weapon Focus|Weapon Focus]]_ (bite, claw)
**Skills** Appraise +20, Bluff +20, _[[universal monster rules/Climb|Climb]]_ +25, Fly +11, Intimidate +20, Knowledge (dungeoneering, geography) +20, Perception +20, Stealth +19
**Languages** Common, Draconic, Ignan, Terran
**SQ** _[[universal monster rules/Change Shape|change shape]]_, underworld burrower

##### Ecology

**Environment** any underground
**Organization** solitary
**Treasure** triple

Underworld dragons—also _[[items/Weapon Magic Abilities/Called|called]]_ futsanglungs—are calculating, greedy creatures that carve great labyrinthine tunnels beneath the world, _[[items/Weapon Magic Abilities/Defending|defending]]_ their hidden treasures. Preferring the earth to the heavens, they channel the fires of the world’s core within their twisting, stonelike bodies and through _[[items/Weapon Magic Abilities/Flaming|flaming]]_ breath hot enough to turn granite into slag.
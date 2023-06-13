---
cssclass: [monsters]
title1: Daemon, Acrididaemon
desc_short: This wicked creature has the claws and mandibles of an enormous insect,
  and its lower body is made entirely of swarming locusts.
title2: Acrididaemon
CR: 14
sources:
- name: Feast of Dust
  page: 61
  link: http://paizo.com/products/btpy9grq?Pathfinder-Module-Feast-of-Dust
XP: 38400
alignment: NE
size: Large
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 10
senses:
  darkvision: 60
  detect good: true
  detect magic: true
  see invisibility: true
AC:
  AC: 28
  touch: 16
  flat_footed: 21
  components:
    dex: 6
    dodge: 1
    natural: 12
    size: -1
HP:
  HP: 200
  long: 16d10+112
saves:
  fort: 17
  ref: 18
  will: 11
immunities:
- acid
- death effects
- disease
- poison
resistances:
  cold: 10
  electricity: 10
  fire: 10
SR: 25
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +20 (2d6+5/19-20)
      entries:
      - - damage: 2d6+5
          crit_range: 19-20
      attack: bite
      bonus:
      - 20
    - text: 2 claws +20 (1d8+5)
      entries:
      - - damage: 1d8+5
      count: 2
      attack: claws
      bonus:
      - 20
  special:
  - biting locusts
  - distraction (DC 25; biting locusts attack only)
space: 10
reach: 10
reach_other: 5 ft. with bite
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - superscripts:
    - APG
    name: feast of ashes
    source: default
    freq: At will
    DC: 17
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - superscripts:
    - APG
    name: putrefy food and drink
    source: default
    freq: At will
  - superscripts:
    - APG
    name: sirocco
    source: default
    freq: 3/day
    DC: 21
  - name: summon swarm
    source: default
    freq: 3/day
  - name: horrid wilting
    source: default
    freq: 1/day
    DC: 23
  sources:
  - name: default
    CL: 14
    concentration: 19
ability_scores:
  STR: 20
  DEX: 23
  CON: 24
  INT: 14
  WIS: 18
  CHA: 21
BAB: 16
CMB: 22
CMD: 39
CMD_other: can't be tripped
feats:
- name: Blind-Fight
- name: Combat Reflexes
- name: Dodge
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Mobility
skills:
  Bluff: 20
  Fly: 15
  Intimidate: 21
  Knowledge (planes): 21
  Perception: 23
  Spellcraft: 18
  Stealth: 21
  Survival: 20
  Use Magic Device: 21
languages:
- Abyssal
- Draconic
- Infernal
- telepathy 100 ft.
special_qualities:
- swarmlike
ecology:
  environment: any (Abaddon)
  organization: solitary, pack (2-5), swarm (6-12)
  treasure_type: standard
special_abilities:
  Biting Locusts (Ex): An acrididaemon's lower body is composed entirely of buzzing
    and biting locusts. Medium or smaller creatures can share the space of an acrididaemon.
    An acrididaemon automatically deals 6d6 points of damage to any creature that
    begins its turn in the acrididaemon's space.
  SwarmLike (Ex): Much of an acrididaemon's body has no discernible anatomy. Any time
    a creature confirms a critical hit against an acrididaemon or hits one with a
    sneak attack, there is a 50% chance that the critical hit or sneak attack is negated
    and damage is instead rolled normally. An acrididaemon takes half again as much
    damage (+50%) from damaging area effects such as fireball and splash weapons.
desc_long: |-
  Servitors of the Horseman of Famine, acrididaemons travel in sky-darkening swarms that spread abject terror into the hearts of mortals they encounter. Part humanoid and part swarm, acrididaemons devour everything they can.

  These roaming terrors call no place home aside from the desolation of Abaddon. They wander the planes ravaging everything in their wake, and quickly abandon their ruined targets, like the parasitic paragons they were created to be.

  Acrididaemons delight in the suffering their predations bring. Though they often favor tactics that result in the devastation of whole settlements, it is not uncommon for one of these daemons to take a single creature prisoner. They enjoy slowly starving captives to death in forlorn redoubts where rescue is beyond hope.

---

# Daemon, Acrididaemon
This wicked creature has the claws and mandibles of an enormous insect, and its lower body is made entirely of swarming locusts.
**Source** Feast of Dust pg. 61
**XP** 38,400

NE Large outsider (daemon, evil, extraplanar)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +23

##### Defense

**AC** 28, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+6 Dex, +1 dodge, +12 natural, –1 size)
**hp** 200 (16d10+112)
**Fort** +17, **Ref** +18, **Will** +11
**Immune** acid, death effects, disease, poison; **Resist** cold 10, electricity 10, fire 10; **SR** 25

##### Offense
**Speed** 30 ft., fly 60 ft. (good)
**Melee** bite +20 (2d6+5/19–20), 2 claws +20 (1d8+5)
**Space** 10 ft., **Reach** 10 ft. (5 ft. with bite)
**Special Attacks** biting locusts, _[[universal monster rules/Distraction|distraction]]_ (DC 25; biting locusts attack only)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +19)
Constant—_detect good_, _detect magic_, _see invisibility_
At will—_[[spells/Feast Of Ashes|feast of ashes]]_ (DC 17), greater teleport (self plus 50 lbs. of objects only), _[[spells/Putrefy Food and Drink|putrefy food and drink]]_
3/day—_[[spells/Sirocco|sirocco]]_ (DC 21), _[[spells/Summon Swarm|summon swarm]]_
1/day—_[[spells/Horrid Wilting|horrid wilting]]_ (DC 23)

##### Statistics
**Str** 20, **Dex** 23, **Con** 24, **Int** 14, **Wis** 18, **Cha** 21
**Base Atk** +16; **CMB** +22; **CMD** 39 (can’t be tripped)
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_
**Skills** Bluff +20, Fly +15, Intimidate +21, Knowledge (planes) +21, Perception +23, Spellcraft +18, Stealth +21, Survival +20, Use Magic Device +21
**Languages** Abyssal, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** swarmlike

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary, pack (2–5), swarm (6–12)
**Treasure** standard

### Special Abilities

**Biting Locusts (Ex)** An acrididaemon’s lower body is composed entirely of buzzing and biting locusts. _[[classes/Medium|Medium]]_ or smaller creatures can share the space of an acrididaemon. An acrididaemon automatically deals 6d6 points of damage to any creature that begins its turn in the acrididaemon’s space.
**SwarmLike (Ex)** Much of an acrididaemon’s body has no discernible anatomy. Any time a creature confirms a critical hit against an acrididaemon or hits one with a sneak attack, there is a 50% chance that the critical hit or sneak attack is negated and damage is instead rolled normally. An acrididaemon takes half again as much damage (+50%) from damaging area effects such as _[[spells/Fireball|fireball]]_ and splash weapons.

##### Description

Servitors of the Horseman of _[[curses/Famine|Famine]]_, acrididaemons travel in sky-darkening swarms that spread abject terror into the hearts of mortals they encounter. Part humanoid and part swarm, acrididaemons devour everything they can.

These roaming terrors call no place home aside from the desolation of Abaddon. They wander the planes ravaging everything in their wake, and quickly abandon their ruined targets, like the parasitic paragons they were created to be.

Acrididaemons delight in the suffering their predations bring. Though they often favor tactics that result in the devastation of whole settlements, it is not uncommon for one of these daemons to take a single creature prisoner. They enjoy slowly starving captives to death in forlorn redoubts where rescue is beyond hope.
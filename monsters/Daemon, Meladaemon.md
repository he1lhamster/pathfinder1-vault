---
cssclass: [monsters]
title1: Daemon, Meladaemon
desc_short: 'This foul creature looks like an emaciated humanoid with the head of
  a jackal. '
title2: Meladaemon
CR: 11
sources:
- name: Bestiary 2
  page: 69
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
- name: Beyond the Vault of Souls
  page: 30
  link: http://paizo.com/store/paizo/pathfinder/modules/35E/v5748btpy88zo
XP: 12800
alignment: NE
size: Large
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 6
senses:
  darkvision: 60
  detect good: true
  detect magic: true
auras:
- name: consumptive aura
  radius: 20
AC:
  AC: 25
  touch: 15
  flat_footed: 19
  components:
    dex: 6
    natural: 10
    size: -1
HP:
  HP: 147
  long: 14d10+70
saves:
  fort: 11
  ref: 15
  will: 14
DR:
- amount: 10
  weakness: good
immunities:
- acid
- critical hits
- death effects
- disease
- poison
- sneak attack
resistances:
  cold: 10
  electricity: 10
  fire: 10
SR: 22
speeds:
  base: 30
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: bite +20 (2d8+6/19-20 plus disease)
      entries:
      - - damage: 2d8+6
          crit_range: 19-20
        - effect: disease
      attack: bite
      bonus:
      - 20
    - text: 2 claws +19 (2d6+6 plus hunger)
      entries:
      - - damage: 2d6+6
        - effect: hunger
      count: 2
      attack: claws
      bonus:
      - 19
space: 10
reach: 10
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
  - name: cause fear
    source: default
    freq: At will
    DC: 15
  - name: deeper darkness
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: blight
    source: default
    freq: 3/day
    DC: 19
  - name: diminish plants
    source: default
    freq: 3/day
  - name: quickened magic missile
    source: default
    freq: 3/day
  - name: horrid wilting
    source: default
    freq: 1/day
    DC: 22
  - name: waves of fatigue
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 11
    concentration: 15
ability_scores:
  STR: 22
  DEX: 22
  CON: 21
  INT: 21
  WIS: 17
  CHA: 18
BAB: 14
CMB: 21
CMD: 37
feats:
- name: Blind-Fight
- name: Combat Reflexes
- name: Great Fortitude
- name: Improved Critical (bite)
- name: Iron Will
- name: Quicken Spell-Like Ability (magic missile)
- name: Weapon Focus (bite)
skills:
  Bluff: 21
  Fly: 17
  Heal: 11
  Intimidate: 21
  Knowledge (planes): 22
  Knowledge (religion): 22
  Perception: 20
  Sense Motive: 20
  Spellcraft: 22
  Stealth: 19
  Survival: 20
  Use Magic Device: 14
languages:
- Abyssal
- Draconic
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Abaddon)
  organization: solitary, pack (2-5), or cabal (6-12)
  treasure_type: standard
special_abilities:
  Consumptive Aura (Su): A meladaemon radiates an aura of hunger to a radius of 20
    feet. Every round a creature begins its turn within this aura, it must succeed
    at a DC 22 Fortitude save or take 1d6 nonlethal damage and become fatigued from
    extreme hunger. Creatures that do not need to eat are immune to this effect. The
    save DC is Constitution-based.
  Disease (Ex): 'Daemonic wasting: Bite-injury; save Fort DC 22; onset 1 day; frequency
    1/day; effect 1d4 Con and 1d4 Cha damage; cure 2 consecutive saves. The save DC
    is Constitution-based.'
  Hunger (Su): A meladaemon's claw attack deals an additional 1d6 points of nonlethal
    damage as it causes sudden pangs of horrific hunger in its foe. Creatures that
    do not need to eat are immune to this effect.
desc_long: |-
  As personifications of death from starvation and thirst, these withered fiends spend their time destroying resources and spreading hunger. Deacons of the Horseman of Famine, these creatures visit worlds throughout the planes, destroying acres of crops and slaughtering livestock in order to harvest souls for their honored master. Meladaemons delight in the slow death of starvation, going so far as to experiment with various bodily deficiencies and mortal weaknesses. Arrogant and utterly bound to their patron, meladaemons rarely work with others of their kind and never serve any of the other three Horsemen except in the rarest of circumstances. 

  Meladaemons stand approximately 12 feet tall and weigh 350 pounds.

---

# Daemon, Meladaemon
This foul creature looks like an emaciated humanoid with the head of a _[[monsters/Jackal|jackal]]_.

**Source** Bestiary 2 pg. 69, Beyond the Vault of Souls pg. 30
**XP** 12,800

NE Large outsider (daemon, evil, extraplanar)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Magic|detect magic]]_; Perception +20
**Aura** consumptive aura (20 ft.)

##### Defense

**AC** 25, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+6 Dex, +10 natural, –1 size)
**hp** 147 (14d10+70)
**Fort** +11, **Ref** +15, **Will** +14
**DR** 10/good; **Immune** acid, critical hits, death effects, disease, poison, sneak attack; **Resist** cold 10, electricity 10, fire 10; **SR** 22

##### Offense
**Speed** 30 ft., fly 60 ft. (average)
**Melee** bite +20 (2d8+6/19–20 plus disease), 2 claws +19 (2d6+6 plus hunger)
**Space** 10 ft., **Reach** 10 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +15)
Constant—_detect good_, _detect magic_, _[[spells/See Invisibility|see invisibility]]_
At will—_[[spells/Cause Fear|cause fear]]_ (DC 15), _[[spells/Deeper Darkness|deeper darkness]]_, greater teleport (self plus 50 lbs. of objects only)
3/day—_[[spells/Blight|blight]]_ (DC 19), _[[spells/Diminish Plants|diminish plants]]_, quickened _[[spells/Magic Missile|magic missile]]_
1/day—_[[spells/Horrid Wilting|horrid wilting]]_ (DC 22), _[[spells/Waves of Fatigue|waves of fatigue]]_

##### Statistics
**Str** 22, **Dex** 22, **Con** 21, **Int** 21, **Wis** 17, **Cha** 18
**Base Atk** +14; **CMB** +21; **CMD** 37
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Iron Will|Iron Will]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_magic missile_), _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Bluff +21, Fly +17, _[[spells/Heal|Heal]]_ +11, Intimidate +21, Knowledge (planes) +22, Knowledge (religion) +22, Perception +20, Sense Motive +20, Spellcraft +22, Stealth +19, Survival +20, Use Magic Device +14
**Languages** Abyssal, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary, pack (2–5), or cabal (6–12)
**Treasure** standard

### Special Abilities

**Consumptive Aura (Su)** A meladaemon radiates an aura of hunger to a radius of 20 feet. Every round a creature begins its turn within this aura, it must succeed at a DC 22 Fortitude save or take 1d6 nonlethal damage and become _[[conditions/Fatigued|fatigued]]_ from extreme hunger. Creatures that do not need to eat are immune to this effect. The save DC is Constitution-based.

**Disease (Ex)** _[[diseases/Daemonic Wasting|Daemonic wasting]]_: Bite—injury; save Fort DC 22; onset 1 day; frequency 1/day; effect 1d4 Con and 1d4 Cha damage; cure 2 consecutive saves. The save DC is Constitution-based.

**Hunger (Su)** A meladaemon’s claw attack deals an additional 1d6 points of nonlethal damage as it causes sudden pangs of horrific hunger in its foe. Creatures that do not need to eat are immune to this effect.

##### Description

As personifications of death from starvation and thirst, these withered fiends spend their time destroying resources and spreading hunger. Deacons of the Horseman of _[[curses/Famine|Famine]]_, these creatures visit worlds throughout the planes, destroying acres of crops and slaughtering livestock in order to harvest souls for their honored master. Meladaemons delight in the _[[spells/Slow|slow]]_ death of starvation, going so far as to experiment with various bodily deficiencies and mortal weaknesses. Arrogant and utterly bound to their patron, meladaemons rarely work with others of their kind and never serve any of the other three Horsemen except in the rarest of circumstances.

Meladaemons stand approximately 12 feet tall and weigh 350 pounds.
---
cssclass: [monsters]
title1: Devil, Immolation Devil (Puragaus)
desc_short: 'Ash and embers encrust the smoldering humanoid frame of this imperious,
  dragon-winged devil. '
title2: Immolation Devil (Puragaus)
CR: 19
sources:
- name: Bestiary 2
  page: 87
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 204800
alignment: LE
size: Large
type: outsider
subtypes:
- devil
- evil
- extraplanar
- lawful
initiative:
  bonus: 8
senses:
  darkvision: 60
  true seeing: true
AC:
  AC: 36
  touch: 17
  flat_footed: 28
  components:
    dex: 8
    natural: 19
    size: -1
HP:
  HP: 315
  long: 18d10+216
  regeneration: 5
  regeneration_weakness: good weapons or good spells
saves:
  fort: 23
  ref: 19
  will: 14
DR:
- amount: 15
  weakness: good and silver
immunities:
- fire
- poison
resistances:
  acid: 10
  cold: 10
SR: 30
speeds:
  base: 30
  fly: 80
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +29 (2d6+12 plus burn)
      entries:
      - - damage: 2d6+12
        - effect: burn
      attack: bite
      bonus:
      - 29
    - text: 2 claw +29 (1d8+12 plus burn)
      entries:
      - - damage: 1d8+12
        - effect: burn
      count: 2
      attack: claw
      bonus:
      - 29
    - text: gore +29 (2d8+12 plus burn)
      entries:
      - - damage: 2d8+12
        - effect: burn
      attack: gore
      bonus:
      - 29
    - text: 2 wings +27 (1d8+6)
      entries:
      - - damage: 1d8+6
      count: 2
      attack: wings
      bonus:
      - 27
  special:
  - burn (2d6, DC 31)
  - hellfire
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: fire shield
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: fireball
    source: default
    freq: At will
    DC: 20
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: persistent image
    source: default
    freq: At will
    DC: 22
  - name: wall of fire
    source: default
    freq: At will
  - name: dictum
    source: default
    freq: 3/day
    DC: 24
  - name: firestorm
    source: default
    freq: 3/day
    DC: 25
  - name: mass charm monster
    source: default
    freq: 3/day
    DC: 25
  - name: summon
    source: default
    freq: 1/day
    level: 9
    summons:
    - name: any 2d4 devils of CR 10
      chance: 90%
    - name: lower
      chance: 90%
  sources:
  - name: default
    CL: 17
    concentration: 24
ability_scores:
  STR: 34
  DEX: 26
  CON: 35
  INT: 24
  WIS: 23
  CHA: 24
BAB: 18
CMB: 31
CMD: 49
feats:
- name: Blind-Fight
- name: Blinding Critical
- name: Combat Expertise
- name: Combat Reflexes
- name: Critical Focus
- name: Iron Will
- name: Multiattack
- name: Power Attack
- name: Stand Still
skills:
  Bluff: 28
  Diplomacy: 28
  Disable Device: 26
  Fly: 31
  Intimidate: 28
  Knowledge (arcana): 25
  Knowledge (nobility): 25
  Knowledge (engineering): 28
  Knowledge (planes): 28
  Perception: 27
  Sense Motive: 27
  Spellcraft: 28
  Stealth: 25
languages:
- Celestial
- Common
- Draconic
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Hell)
  organization: solitary, pair, or council (3-6)
  treasure_type: double
special_abilities:
  Hellfire (Su): Any fire damage caused by an immolation devil's abilities and spells
    is half fire damage, half unholy damage.
desc_long: |-
  Immolation devils are tyrant warlords and terrifying field generals among Hell's legions. While many other greater devils manipulate and corrupt subtly and from afar, puragaus surround themselves with lesser diabolical minions, lead interplanar incursions, hold infernal redoubts upon mortal worlds, or strike against any who would defy the will of Hell. 

  Immolation devils stand just over 10 feet tall, with wingspans nearing 20 feet, and weigh 900 pounds.

---

# Devil, Immolation Devil (Puragaus)
Ash and embers encrust the smoldering humanoid frame of this imperious, dragon-winged devil.

**Source** Bestiary 2 pg. 87
**XP** 204,800

LE Large outsider (devil, evil, extraplanar, lawful)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +27

##### Defense

**AC** 36, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+8 Dex, +19 natural, –1 size)
**hp** 315 (18d10+216); _[[universal monster rules/Regeneration|regeneration]]_ 5 (good weapons or good spells)
**Fort** +23, **Ref** +19, **Will** +14
**DR** 15/good and silver; **Immune** fire, poison; **Resist** acid 10, cold 10; **SR** 30

##### Offense
**Speed** 30 ft., fly 80 ft. (good)
**Melee** bite +29 (2d6+12 plus _[[universal monster rules/Burn|burn]]_), 2 claw +29 (1d8+12 plus _burn_), gore +29 (2d8+12 plus _burn_), 2 wings +27 (1d8+6)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _burn_ (2d6, DC 31), hellfire
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +24)
Constant—_[[spells/Fire Shield|fire shield]]_, _true seeing_
At will—_[[spells/Fireball|fireball]]_ (DC 20), greater teleport (self plus 50 lbs. of objects only), _[[spells/Persistent Image|persistent image]]_ (DC 22), _[[spells/Wall Of Fire|wall of fire]]_
3/day—_[[spells/Dictum|dictum]]_ (DC 24), firestorm (DC 25), mass _[[spells/Charm Monster|charm monster]]_ (DC 25)
1/day—_[[universal monster rules/Summon|summon]]_ (level 9, any 2d4 devils of CR 10 or lower, 90%)

##### Statistics
**Str** 34, **Dex** 26, **Con** 35, **Int** 24, **Wis** 23, **Cha** 24
**Base Atk** +18; **CMB** +31; **CMD** 49
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Blinding Critical|Blinding Critical]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Stand Still|Stand Still]]_
**Skills** Bluff +28, Diplomacy +28, Disable Device +26, Fly +31, Intimidate +28, Knowledge (arcana, nobility) +25, Knowledge (engineering, planes) +28, Perception +27, Sense Motive +27, Spellcraft +28, Stealth +25
**Languages** Celestial, Common, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Hell)
**Organization** solitary, pair, or council (3–6)
**Treasure** double

### Special Abilities

**Hellfire (Su)** Any fire damage caused by an immolation devil’s abilities and spells is half fire damage, half _[[items/Weapon Magic Abilities/Unholy|unholy]]_ damage.

##### Description

Immolation devils are tyrant warlords and terrifying field generals among Hell’s legions. While many other greater devils manipulate and corrupt subtly and from afar, puragaus surround themselves with lesser diabolical minions, lead interplanar incursions, hold infernal redoubts upon mortal worlds, or strike against any who would defy the will of Hell.

Immolation devils stand just over 10 feet tall, with wingspans nearing 20 feet, and weigh 900 pounds.
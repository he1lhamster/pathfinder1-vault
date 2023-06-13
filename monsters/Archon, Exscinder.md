---
cssclass: [monsters]
title1: Archon, Exscinder
desc_short: This massive humanoid figure has no mouth, and carries a burning sword
  that matches its flaming wings.
title2: Exscinder
CR: 12
sources:
- name: Bestiary 5
  page: 34
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 19200
alignment: LG
size: Huge
type: outsider
subtypes:
- archon
- extraplanar
- good
- lawful
initiative:
  bonus: 8
senses:
  darkvision: 60
  low-light vision: true
  true seeing: true
AC:
  AC: 29
  touch: 12
  flat_footed: 25
  components:
    dex: 4
    natural: 17
    size: -2
    deflection vs. evil: 2
HP:
  HP: 147
  long: 14d10+70
saves:
  fort: 16
  ref: 10
  will: 16
  other: +4 vs. poison
DR:
- amount: 10
  weakness: evil
immunities:
- acid
- cold
- fire
- electricity
- petrification
SR: 23
speeds:
  base: 30
  fly: 90
  fly_maneuverability: good
attacks:
  melee:
  - - text: +3 flaming longsword +25/+20/+15 (3d6+15/19-20 plus 1d6 fire)
      entries:
      - - damage: 3d6+15
          crit_range: 19-20
        - damage: 1d6
          type: fire
      attack: +3 flaming longsword
      bonus:
      - 25
      - 20
      - 15
  special:
  - censor text
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: cure light wounds
    source: default
    freq: At will
  - name: detect thoughts
    source: default
    freq: At will
    DC: 17
  - name: discern lies
    source: default
    freq: At will
    DC: 19
  - name: hold monster
    source: default
    freq: At will
    DC: 20
  - name: holy smite
    source: default
    freq: At will
    DC: 19
  - name: invisibility
    source: default
    freq: At will
    other: self only
  - name: locate creature
    source: default
    freq: At will
  - name: locate object
    source: default
    freq: At will
  - name: modify memory
    source: default
    freq: At will
    DC: 19
  - name: protection from evil
    source: default
    freq: At will
    DC: 16
  - name: repress memory
    source: default
    freq: At will
    DC: 21
  - name: stabilize
    source: default
    freq: At will
  - name: zone of truth
    source: default
    freq: At will
    DC: 17
  - name: dispel evil
    source: default
    freq: 3/day
    DC: 20
  - name: fireball
    source: default
    freq: 3/day
    DC: 18
  - name: flame strike
    source: default
    freq: 3/day
    DC: 20
  - name: plane shift
    source: default
    freq: 3/day
    DC: 20
  - name: discern location
    source: default
    freq: 1/day
    DC: 23
  - name: find the path
    source: default
    freq: 1/day
    DC: 21
  sources:
  - name: default
    CL: 15
    concentration: 20
ability_scores:
  STR: 30
  DEX: 19
  CON: 20
  INT: 16
  WIS: 25
  CHA: 21
BAB: 14
CMB: 26
CMD: 40
feats:
- name: Alertness
- name: Cleave
- name: Combat Reflexes
- name: Great Fortitude
- name: Improved Initiative
- name: Lightning Reflexes
- name: Power Attack
skills:
  Intimidate: 22
  Knowledge (arcana): 20
  Knowledge (history): 20
  Knowledge (planes): 20
  Knowledge (religion): 20
  Knowledge (geography): 17
  Linguistics: 10
  Perception: 28
  Sense Motive: 28
  Spellcraft: 10
languages:
- Abyssal
- Aklo
- Celestial
- Common
- Draconic
- Dwarven
- Elven
- Gnome
- Infernal
- telepathy 100 ft.
- truespeech
special_qualities:
- change size
- no breath
ecology:
  environment: any (Heaven)
  organization: solitary, pair, or inquisition (3-6)
  treasure_type: standard
  treasure:
  - +3 flaming longsword
  - other treasure
special_abilities:
  Censor Text (Su): An exscinder can attempt to magically steal or modify any text
    within 100 feet as a standard action. Against an unattended text, it automatically
    succeeds. A creature in possession of a text can attempt a DC 22 Will save to
    negate this ability. A stolen text teleports directly into the exscinder's hand.
    A modified text is permanently revised according to the exscinder's wishes-this
    change is detectable with magic, but can't be dispelled or reversed short of a
    wish or miracle. The save DC is Charisma-based.
  Change Size (Su): An exscinder can change its form to a Large, Medium, or Small
    version of itself. This does not change its ability scores; it adjusts only its
    size (and thus its weapon damage).
desc_long: Exscinders are Heaven's censors, scouring the planes for texts containing
  information too evil or dangerous to be allowed to exist. Exscinders care little
  for individual lives or everyday heresies, remaining staunchly focused on protecting
  mortalkind as a whole from corruption.

---

# Archon, Exscinder
This massive humanoid figure has no mouth, and carries a _[[items/Weapon Magic Abilities/Burning|burning]]_ sword that matches its _[[items/Weapon Magic Abilities/Flaming|flaming]]_ wings.
**Source** Bestiary 5 pg. 34
**XP** 19,200

LG Huge outsider (archon, extraplanar, good, lawful)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/True Seeing|true seeing]]_; Perception +28

##### Defense

**AC** 29, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+4 Dex, +17 natural, -2 size; +2 deflection vs. evil)
**hp** 147 (14d10+70)
**Fort** +16, **Ref** +10, **Will** +16; +4 vs. poison
**DR** 10/evil; **Immune** acid, cold, fire, electricity, petrification; **SR** 23

##### Offense
**Speed** 30 ft., fly 90 ft. (good)
**Melee** +3 _flaming_ _[[items/Weapon/Longsword|longsword]]_ +25/+20/+15 (3d6+15/19-20 plus 1d6 fire)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** censor text
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +20)
Constant—_[[spells/Detect Evil|detect evil]]_, _true seeing_
At will—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 17), _[[spells/Discern Lies|discern lies]]_ (DC 19), _[[spells/Hold Monster|hold monster]]_ (DC 20), _[[spells/Holy Smite|holy smite]]_ (DC 19), _[[spells/Invisibility|invisibility]]_ (self only), _[[spells/Locate Creature|locate creature]]_, _[[spells/Locate Object|locate object]]_, _[[spells/Modify Memory|modify memory]]_ (DC 19), _[[spells/Protection From Evil|protection from evil]]_ (DC 16), _[[spells/Repress Memory|repress memory]]_ (DC 21), stabilize, _[[spells/Zone of Truth|zone of truth]]_ (DC 17)
3/day—_[[spells/Dispel Evil|dispel evil]]_ (DC 20), _[[spells/Fireball|fireball]]_ (DC 18), _[[spells/Flame Strike|flame strike]]_ (DC 20), _[[spells/Plane Shift|plane shift]]_ (DC 20)
1/day—_[[spells/Discern Location|discern location]]_ (DC 23), _[[spells/Find the Path|find the path]]_ (DC 21)

##### Statistics
**Str** 30, **Dex** 19, **Con** 20, **Int** 16, **Wis** 25, **Cha** 21
**Base Atk** +14; **CMB** +26; **CMD** 40
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Intimidate +22, Knowledge (arcana, history, planes, religion) +20, Knowledge (geography) +17, Linguistics +10, Perception +28, Sense Motive +28, Spellcraft +10
**Languages** Abyssal, Aklo, Celestial, Common, Draconic, Dwarven, Elven, Gnome, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft., truespeech
**SQ** change size, _[[universal monster rules/No Breath|no breath]]_

##### Ecology

**Environment** any (Heaven)
**Organization** solitary, pair, or inquisition (3-6)
**Treasure** standard (+3 _flaming_ _longsword_, other treasure)

### Special Abilities

**Censor Text (Su)** An exscinder can attempt to magically steal or modify any text within 100 feet as a standard action. Against an unattended text, it automatically succeeds. A creature in _[[spells/Possession|possession]]_ of a text can attempt a DC 22 Will save to negate this ability. A stolen text teleports directly into the exscinder’s hand. A modified text is permanently revised according to the exscinder’s wishes—this change is detectable with magic, but can’t be dispelled or reversed short of a _[[spells/Wish|wish]]_ or _[[spells/Miracle|miracle]]_. The save DC is Charisma-based.

**Change Size (Su)** An exscinder can change its form to a Large, _[[classes/Medium|Medium]]_, or Small version of itself. This does not change its ability scores; it adjusts only its size (and thus its weapon damage).

##### Description

Exscinders are Heaven’s censors, scouring the planes for texts containing information too evil or dangerous to be allowed to exist. Exscinders care little for individual lives or everyday heresies, remaining staunchly focused on protecting mortalkind as a whole from corruption.
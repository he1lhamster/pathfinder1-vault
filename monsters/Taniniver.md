---
cssclass: [monsters]
title1: Taniniver
desc_short: This legless, winged, white-eyed dragon is covered in patches of diseased
  flesh, squirming with maggots and oozing pus.
title2: Taniniver
CR: 18
sources:
- name: Bestiary 4
  page: 258
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 153600
alignment: NE
size: Huge
type: dragon
initiative:
  bonus: 4
senses:
  darkvision: 120
  deathwatch: true
auras:
- name: frightful presence
  radius: 180
  DC: 25
AC:
  AC: 33
  touch: 8
  flat_footed: 33
  components:
    natural: 25
    size: -2
HP:
  HP: 270
  long: 20d12+140
saves:
  fort: 21
  ref: 12
  will: 15
defensive_abilities:
- negative energy affinity
DR:
- amount: 15
  weakness: good and magic
immunities:
- paralysis
- sleep
- visual effects
resistances:
  acid: 30
  cold: 30
  electricity: 30
  fire: 30
SR: 29
speeds:
  base: 30
  fly: 200
  fly_maneuverability: clumsy
attacks:
  melee:
  - - text: bite +30 (4d6+11 plus disease)
      entries:
      - - damage: 4d6+11
        - effect: disease
      attack: bite
      bonus:
      - 30
    - text: 2 claws +30 (2d8+11 plus disease)
      entries:
      - - damage: 2d8+11
        - effect: disease
      count: 2
      attack: claws
      bonus:
      - 30
    - text: tail slap +24 (2d8+5 plus disease)
      entries:
      - - damage: 2d8+5
        - effect: disease
      attack: tail slap
      bonus:
      - 24
  special:
  - breath weapon (60-ft. cone, 1d6 Str drain plus mummy rot, Fortitude DC 27 negates,
    usable every 1d4 rounds)
space: 15
reach: 10
reach_other: 15 ft. with bite
spell_like_abilities:
  entries:
  - name: deathwatch
    source: default
    freq: Constant
  - name: animate dead
    source: default
    freq: 3/day
  - name: inflict serious wounds
    source: default
    freq: 3/day
    DC: 18
  - name: eyebite
    source: default
    freq: 1/day
    DC: 21
  - name: horrid wilting
    source: default
    freq: 1/day
    DC: 23
  - name: symbol of pain
    source: default
    freq: 1/day
    DC: 20
  sources:
  - name: default
    CL: 20
    concentration: 25
ability_scores:
  STR: 33
  DEX: 11
  CON: 25
  INT: 18
  WIS: 17
  CHA: 20
BAB: 20
CMB: 33
CMD: 43
CMD_other: can't be tripped
feats:
- name: Cleave
- name: Combat Reflexes
- name: Critical Focus
- name: Great Fortitude
- name: Improved Initiative
- name: Power Attack
- name: Sickening Critical
- name: Vital Strike
- name: Weapon Focus (bite)
- name: Weapon Focus (claw)
skills:
  Bluff: 28
  Fly: -12
  Heal: 26
  Intimidate: 28
  Knowledge (arcana): 27
  Knowledge (religion): 27
  Perception: 26
  Sense Motive: 26
  Spellcraft: 27
  Stealth: 15
  Use Magic Device: 28
languages:
- Common
- Draconic
- Undercommon
ecology:
  environment: any land or underground
  organization: solitary
  treasure_type: standard
special_abilities:
  Breath Weapon (Ex): A taniniver's breath weapon is a hideous gray cloud of disease
    particles. Any creature in the area must succeed at a DC 27 Fortitude save or
    contract mummy rot (Pathfinder RPG Bestiary 210). The disease is contracted immediately
    (the onset period does not apply) and is an instantaneous effect. Ongoing saving
    throws against the disease use the dragon's breath weapon DC. The save DC is Constitution-based.
  Disease (Ex): 'A taniniver's natural attacks infect its opponent with a random disease
    from the following list: blinding sickness, bubonic plague, cackle fever, leprosy,
    mindfire, or shakes. The initial saving throw against these diseases uses the
    breath weapon's DC.'
desc_long: Taninivers are a degenerate race of diseased dragons. A taniniver's body
  is alive but constantly rotting. Wracked by never-ending pain, with the stench of
  its own decaying flesh so strong it nearly overwhelms the vile creature's enhanced
  senses, the foul taniniver spends most of its time in magical research to reverse
  the progression of its diseases or, failing that, to stave off further deterioration.
  Taninivers often ally with cults of undeath or dragonkind.

---

# Taniniver
This legless, winged, white-eyed dragon is covered in patches of diseased flesh, squirming with maggots and oozing pus.
**Source** Bestiary 4 pg. 258
**XP** 153,600

NE Huge dragon
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[spells/Deathwatch|deathwatch]]_; Perception +26
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (180 ft., DC 25)

##### Defense

**AC** 33, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 33 (+25 natural, –2 size)
**hp** 270 (20d12+140)
**Fort** +21, **Ref** +12, **Will** +15
**Defensive Abilities** _[[universal monster rules/Negative Energy Affinity|negative energy affinity]]_; **DR** 15/good and magic; **Immune** _[[universal monster rules/Paralysis|paralysis]]_, sleep, visual effects; **Resist** acid 30, cold 30, electricity 30, fire 30; **SR** 29

##### Offense
**Speed** 30 ft., fly 200 ft. (clumsy)
**Melee** bite +30 (4d6+11 plus disease), 2 claws +30 (2d8+11 plus disease), tail slap +24 (2d8+5 plus disease)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, 1d6 Str drain plus _[[curses/Mummy rot|mummy rot]]_, Fortitude DC 27 negates, usable every 1d4 rounds)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +25)
Constant—_deathwatch_
3/day—_[[spells/Animate Dead|animate dead]]_, _[[spells/Inflict Serious Wounds|inflict serious wounds]]_ (DC 18)
1/day—_[[spells/Eyebite|eyebite]]_ (DC 21), _[[spells/Horrid Wilting|horrid wilting]]_ (DC 23), _[[spells/Symbol of Pain|symbol of pain]]_ (DC 20)

##### Statistics
**Str** 33, **Dex** 11, **Con** 25, **Int** 18, **Wis** 17, **Cha** 20
**Base Atk** +20; **CMB** +33; **CMD** 43 (can’t be tripped)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Sickening Critical|Sickening Critical]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite), _Weapon Focus_ (claw)
**Skills** Bluff +28, Fly –12, _[[spells/Heal|Heal]]_ +26, Intimidate +28, Knowledge (arcana) +27, Knowledge (religion) +27, Perception +26, Sense Motive +26, Spellcraft +27, Stealth +15, Use Magic Device +28
**Languages** Common, Draconic, Undercommon

##### Ecology

**Environment** any land or underground
**Organization** solitary
**Treasure** standard

### Special Abilities

**_Breath Weapon_ (Ex)** A _[[monsters/Taniniver|taniniver]]_’s _breath weapon_ is a hideous _[[monsters/Gray|gray]]_ cloud of disease particles. Any creature in the area must succeed at a DC 27 Fortitude save or contract _mummy rot_ (Pathfinder RPG Bestiary 210). The disease is contracted immediately (the onset period does not apply) and is an instantaneous effect. Ongoing saving throws against the disease use the dragon’s _breath weapon_ DC. The save DC is Constitution-based.

**Disease (Ex)** A _taniniver_’s _[[universal monster rules/Natural Attacks|natural attacks]]_ infect its opponent with a random disease from the following list: _[[diseases/Blinding Sickness|blinding sickness]]_, _[[diseases/Bubonic Plague|bubonic plague]]_, _[[diseases/Cackle Fever|cackle fever]]_, _[[diseases/Leprosy|leprosy]]_, _[[diseases/Mindfire|mindfire]]_, or _[[diseases/Shakes|shakes]]_. The initial saving throw against these diseases uses the _breath weapon_’s DC.

##### Description

Taninivers are a degenerate race of diseased dragons. A _taniniver_’s body is alive but constantly rotting. Wracked by never-ending pain, with the _[[universal monster rules/Stench|stench]]_ of its own decaying flesh so strong it nearly overwhelms the vile creature’s enhanced senses, the foul _taniniver_ spends most of its time in magical research to reverse the progression of its diseases or, failing that, to stave off further deterioration. Taninivers often ally with cults of undeath or dragonkind.
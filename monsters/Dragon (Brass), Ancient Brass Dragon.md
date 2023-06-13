---
cssclass: [monsters]
title1: Dragon (Brass), Ancient Brass Dragon
title2: Ancient Brass Dragon
CR: 16
sources:
- name: Pathfinder RPG Bestiary
  page: 103
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 76800
alignment: CG
size: Huge
type: dragon
subtypes:
- fire
initiative:
  bonus: 4
senses:
  dragon senses: true
auras:
- name: fire
  radius: 10
  other:
  - 1d6 fire
- name: frightful presence
  radius: 300
  DC: 26
AC:
  AC: 38
  touch: 8
  flat_footed: 38
  components:
    natural: 30
    size: -2
HP:
  HP: 297
  long: 22d12+154
saves:
  fort: 20
  ref: 13
  will: 18
DR:
- amount: 15
  weakness: magic
immunities:
- fire
- paralysis
- sleep
SR: 27
weaknesses:
- vulnerability to cold
speeds:
  base: 60
  burrow: 30
  fly: 200
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +31 (2d8+16)
      entries:
      - - damage: 2d8+16
      attack: bite
      bonus:
      - 31
    - text: 2 claws +31 (2d6+11)
      entries:
      - - damage: 2d6+11
      count: 2
      attack: claws
      bonus:
      - 31
    - text: 2 wings +29 (1d8+5)
      entries:
      - - damage: 1d8+5
      count: 2
      attack: wings
      bonus:
      - 29
    - text: tail slap +29 (2d6+16)
      entries:
      - - damage: 2d6+16
      attack: tail slap
      bonus:
      - 29
  special:
  - breath weapon (100-ft. line, DC 28, 20d4 fire)
  - crush
  - desert wind
  - sandstorm
  - sleep breath
spell_like_abilities:
  entries:
  - name: control weather
    source: default
    freq: At will
  - name: control winds
    source: default
    freq: At will
  - name: endure elements
    source: default
    freq: At will
  - name: speak with animals
    source: default
    freq: At will
  - name: suggestion
    source: default
    freq: At will
    DC: 18
  sources:
  - name: default
    CL: 22
spells:
  entries:
  - name: g. teleport
    source: '?'
    level: 7
  - name: power word blind
    source: '?'
    level: 7
  - name: forceful hand
    source: '?'
    level: 6
  - name: geas
    source: '?'
    level: 6
  - name: greater dispel magic
    source: '?'
    level: 6
  - name: contact other plane
    source: '?'
    level: 5
  - name: dominate person
    source: '?'
    level: 5
    DC: 22
  - name: mirage arcana
    source: '?'
    level: 5
  - name: prying eyes
    source: '?'
    level: 5
  - name: charm monster
    source: '?'
    level: 4
    DC: 21
  - name: confusion
    source: '?'
    level: 4
    DC: 21
  - name: dimensional anchor
    source: '?'
    level: 4
  - name: locate creature
    source: '?'
    level: 4
  - name: displacement
    source: '?'
    level: 3
  - name: heroism
    source: '?'
    level: 3
  - name: hold person
    source: '?'
    level: 3
    DC: 20
  - name: tongues
    source: '?'
    level: 3
  - name: alter self
    source: '?'
    level: 2
  - name: detect thoughts
    source: '?'
    level: 2
    DC: 17
  - name: locate object
    source: '?'
    level: 2
  - name: resist energy
    source: '?'
    level: 2
  - name: see invisibility
    source: '?'
    level: 2
  - name: alarm
    source: '?'
    level: 1
  - name: charm person
    source: '?'
    level: 1
    DC: 18
  - name: protection from evil
    source: '?'
    level: 1
  - name: shield
    source: '?'
    level: 1
  - name: ventriloquism
    source: '?'
    level: 1
  - name: arcane mark
    source: '?'
    level: 0
  - name: dancing lights
    source: '?'
    level: 0
  - name: d. magic
    source: '?'
    level: 0
  - name: d. poison
    source: '?'
    level: 0
  - name: ghost sound
    source: '?'
    level: 0
    DC: 15
  - name: mage hand
    source: '?'
    level: 0
  - name: message
    source: '?'
    level: 0
  - name: prestidigitation
    source: '?'
    level: 0
  - name: r. magic
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 15
    slots:
      7: 4
      6: 6
      5: 7
      4: 7
      3: 7
      2: 7
      1: 8
      0: at-will
ability_scores:
  STR: 33
  DEX: 10
  CON: 25
  INT: 20
  WIS: 21
  CHA: 20
BAB: 22
CMB: 35
CMD: 45
CMD_other: 49 vs. trip
feats:
- name: Alertness
- name: Flyby Attack
- name: Greater Spell Focus (enchant)
- name: Hover
- name: Improved Initiative
- name: Improved Vital Strike
- name: Multiattack
- name: Power Attack
- name: Quicken Spell
- name: Spell Focus (enchant)
- name: Vital Strike
skills:
  Bluff: 30
  Diplomacy: 30
  Fly: 17
  Heal: 30
  Knowledge (local): 30
  Knowledge (history): 30
  Linguistics: 30
  Perception: 34
  Sense Motive: 34
  Spellcraft: 30
  Survival: 30
languages:
- Common
- Draconic
- plus any 22 others
special_qualities:
- move sand
ecology:
  environment: warm deserts
desc_long: Consummate conversationalists, brass dragons prefer to talk instead of
  fight. Brass dragons lair near humanoid settlements, where they can hear the most
  recent news and gossip.

---

# Dragon (Brass), Ancient Brass Dragon

**Source** Pathfinder RPG Bestiary pg. 103
**XP** 76,800

CG Huge dragon (fire)
**Init** +4; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +34
**Aura** fire (10 ft., 1d6 fire), _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 26)

##### Defense

**AC** 38, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 38 (+30 natural, –2 size)
**hp** 297 (22d12+154)
**Fort** +20, **Ref** +13, **Will** +18
**DR** 15/magic; **Immune** fire, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 27
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to cold

##### Offense
**Speed** 60 ft., _[[universal monster rules/Burrow|burrow]]_ 30 ft., fly 200 ft. (poor)
**Melee** bite +31 (2d8+16), 2 claws +31 (2d6+11), 2 wings +29 (1d8+5), tail slap +29 (2d6+16)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (100-ft. line, DC 28, 20d4 fire), crush, desert wind, sandstorm, sleep breath
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 22th)
At will—_[[spells/Control Weather|control weather]]_, _[[spells/Control Winds|control winds]]_, _[[spells/Endure Elements|endure elements]]_, _[[spells/Speak with Animals|speak with animals]]_, _[[spells/Suggestion|suggestion]]_ (DC 18)
**Spells Known **(CL 15th)
7th (4/day)—g. teleport, _[[spells/Power Word Blind|power word blind]]_
6th (6/day)—_[[spells/Forceful Hand|forceful hand]]_, geas, greater _[[spells/Dispel Magic|dispel magic]]_
5th (7/day)—_[[spells/Contact Other Plane|contact other plane]]_, _[[spells/Dominate Person|dominate person]]_ (DC 22), _[[spells/Mirage Arcana|mirage arcana]]_, _[[spells/Prying Eyes|prying eyes]]_
4th (7/day)—_[[spells/Charm Monster|charm monster]]_ (DC 21), _[[spells/Confusion|confusion]]_ (DC 21), _[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Locate Creature|locate creature]]_
3rd (7/day)—_[[spells/Displacement|displacement]]_, _[[spells/Heroism|heroism]]_, _[[spells/Hold Person|hold person]]_ (DC 20), _[[spells/Tongues|tongues]]_
2nd (7/day)—_[[spells/Alter Self|alter self]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 17), _[[spells/Locate Object|locate object]]_, _[[spells/Resist Energy|resist energy]]_, _[[spells/See Invisibility|see invisibility]]_
1st (8/day)—_[[spells/Alarm|alarm]]_, _[[spells/Charm Person|charm person]]_ (DC 18), _[[spells/Protection From Evil|protection from evil]]_, _[[spells/Shield|shield]]_, _[[spells/Ventriloquism|ventriloquism]]_
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[spells/Dancing Lights|dancing lights]]_, d. magic, d. poison, _[[spells/Ghost Sound|ghost sound]]_ (DC 15), _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_, r. magic

##### Statistics
**Str** 33, **Dex** 10, **Con** 25, **Int** 20, **Wis** 21, **Cha** 20
**Base Atk** +22; **CMB** +35; **CMD** 45 (49 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (enchant), _[[feats/Hover|Hover]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Spell Focus|Spell Focus]]_ (enchant), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Bluff +30, Diplomacy +30, Fly +17, _[[spells/Heal|Heal]]_ +30, Knowledge (local, history) +30, Linguistics +30, Perception +34, Sense Motive +34, Spellcraft +30, Survival +30
**Languages** Common, Draconic, plus any 22 others
**SQ** move sand

##### Ecology

**Environment** warm deserts

Consummate conversationalists, brass dragons prefer to talk instead of fight. Brass dragons lair near humanoid settlements, where they can hear the most recent news and gossip.
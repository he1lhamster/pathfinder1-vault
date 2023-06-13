---
cssclass: [monsters]
title1: Dragon (Black), Ancient Black Dragon
title2: Ancient Black Dragon
CR: 16
sources:
- name: Pathfinder RPG Bestiary
  page: 93
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 76800
alignment: CE
size: Huge
type: dragon
subtypes:
- water
initiative:
  bonus: 4
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 300
  DC: 25
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
- acid
- paralysis
- sleep
SR: 27
speeds:
  base: 60
  fly: 200
  fly_maneuverability: poor
  swim: 60
attacks:
  melee:
  - - text: bite +32 (2d8+16 plus 4d6 acid)
      entries:
      - - damage: 2d8+16
        - damage: 4d6
          type: acid
      attack: bite
      bonus:
      - 32
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
    - text: tail +29 (2d6+16)
      entries:
      - - damage: 2d6+16
      attack: tail
      bonus:
      - 29
  special:
  - acid pool (50-ft. radius)
  - acidic bite
  - breath weapon (100-ft. line, DC 28, 20d6 acid)
  - corrupt water
  - crush
space: 15
reach: 10
reach_other: 15 ft. with bite
spell_like_abilities:
  entries:
  - name: darkness
    source: default
    freq: At will
    other: 100-ft. radius
  - name: insect plague
    source: default
    freq: At will
  - name: plant growth
    source: default
    freq: At will
  sources:
  - name: default
    CL: 22
spells:
  entries:
  - name: cone of cold
    source: '?'
    level: 5
    DC: 19
  - name: wall of force
    source: '?'
    level: 5
  - name: arcane eye
    source: '?'
    level: 4
  - name: black tentacles
    source: '?'
    level: 4
  - name: dimension door
    source: '?'
    level: 4
  - name: dispel magic
    source: '?'
    level: 3
  - name: heroism
    source: '?'
    level: 3
  - name: hold person
    source: '?'
    level: 3
    DC: 17
  - name: slow
    source: '?'
    level: 3
    DC: 17
  - name: blur
    source: '?'
    level: 2
  - name: glitterdust
    source: '?'
    level: 2
    DC: 16
  - name: invisibility
    source: '?'
    level: 2
  - name: summon swarm
    source: '?'
    level: 2
  - name: whispering wind
    source: '?'
    level: 2
  - name: alarm
    source: '?'
    level: 1
  - name: mage armor
    source: '?'
    level: 1
  - name: magic missile
    source: '?'
    level: 1
  - name: obscuring mist
    source: '?'
    level: 1
  - name: true strike
    source: '?'
    level: 1
  - name: dancing lights
    source: '?'
    level: 0
  - name: detect magic
    source: '?'
    level: 0
  - name: light
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: mending
    source: '?'
    level: 0
  - name: message
    source: '?'
    level: 0
  - name: prestidigitation
    source: '?'
    level: 0
  - name: read magic
    source: '?'
    level: 0
  - name: resistance
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 11
    slots:
      5: 4
      4: 7
      3: 7
      2: 7
      1: 7
      0: at-will
ability_scores:
  STR: 33
  DEX: 10
  CON: 25
  INT: 18
  WIS: 21
  CHA: 18
BAB: 22
CMB: 35
CMD: 45
CMD_other: 49 vs. trip
feats:
- name: Alertness
- name: Combat Expertise
- name: Flyby Attack
- name: Greater Vital Strike
- name: Improved Initiative
- name: Improved Vital Strike
- name: Multiattack
- name: Power Attack
- name: Skill Focus (Stealth)
- name: Vital Strike
- name: Weapon Focus (bite)
skills:
  Fly: 17
  Handle Animal: 26
  Intimidate: 29
  Knowledge (arcana): 29
  Knowledge (history): 29
  Knowledge (geography): 29
  Perception: 34
  Spellcraft: 29
  Stealth: 23
  Swim: 44
languages:
- Common
- Draconic
- Giant
- Goblin
- Orc
special_qualities:
- speak with reptiles
- swamp stride
- water breathing
ecology:
  environment: warm marshes
desc_long: Lording over the darkest swamps and marshes, black dragons are the undisputed
  masters of their domain, ruling through cruelty and intimidation. Those who dwell
  within a black dragon's reach live in fear. Black dragons tend to make their lairs
  in remote parts of the swamp, preferably in caves at the bottom of dark and fetid
  pools. Inside, they pile up their filthy treasure and sleep amid the roots and muck.
  Black dragons prefer their food a bit rotten and will often allow a meal to sit
  in a pool for days before consuming it. Black dragons prefer treasures that do not
  rot or decay, making their hoard, full of coins, gemstones, jewelry, and other objects
  made from stone or metal.

---

# Dragon (Black), Ancient Black Dragon

**Source** Pathfinder RPG Bestiary pg. 93
**XP** 76,800
CE Huge dragon (water)
**Init** +4; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +34
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 25)

##### Defense

**AC** 38, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 38 (+30 natural, –2 size)
**hp** 297 (22d12+154)
**Fort** +20, **Ref** +13, **Will** +18
**DR** 15/magic; **Immune** acid, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 27

##### Offense
**Speed** 60 ft., fly 200 ft. (poor), swim 60 ft.
**Melee** bite +32 (2d8+16 plus 4d6 acid), 2 claws +31 (2d6+11), 2 wings +29 (1d8+5), tail +29 (2d6+16)
**Space** 15 ft., **Reach** 10 ft. (15 ft. with bite)
**Special Attacks** acid pool (50-ft. radius), acidic bite, _[[universal monster rules/Breath Weapon|breath weapon]]_ (100-ft. line, DC 28, 20d6 acid), corrupt water, crush
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 22nd)
At will—_[[spells/Darkness|darkness]]_ (100-ft. radius), _[[spells/Insect Plague|insect plague]]_, _[[spells/Plant Growth|plant growth]]_
**Spells Known **(CL 11th)
5th (4/day)—_[[spells/Cone of Cold|cone of cold]]_ (DC 19), _[[spells/Wall Of Force|wall of force]]_
4th (7/day)—_[[spells/Arcane Eye|arcane eye]]_, _[[spells/Black Tentacles|black tentacles]]_, _[[spells/Dimension Door|dimension door]]_
3rd (7/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Heroism|heroism]]_, _[[spells/Hold Person|hold person]]_ (DC 17), _[[spells/Slow|slow]]_ (DC 17)
2nd (7/day)—_[[spells/Blur|blur]]_, _[[spells/Glitterdust|glitterdust]]_ (DC 16), _[[spells/Invisibility|invisibility]]_, _[[spells/Summon Swarm|summon swarm]]_, _[[spells/Whispering Wind|whispering wind]]_
1st (7/day)—_[[spells/Alarm|alarm]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_

##### Statistics
**Str** 33, **Dex** 10, **Con** 25, **Int** 18, **Wis** 21, **Cha** 18
**Base Atk** +22; **CMB** +35; **CMD** 45 (49 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth), _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Fly +17, Handle Animal +26, Intimidate +29, Knowledge (arcana) +29, Knowledge (history) +29, Knowledge (geography) +29, Perception +34, Spellcraft +29, Stealth +23, Swim +44
**Languages** Common, Draconic, Giant, _[[monsters/Goblin|Goblin]]_, _[[monsters/Orc|Orc]]_
**SQ** speak with reptiles, swamp stride, _[[universal monster rules/Water Breathing|water breathing]]_

##### Ecology

**Environment** warm marshes

Lording over the darkest swamps and marshes, black dragons are the undisputed masters of their domain, ruling through _[[feats/Cruelty|cruelty]]_ and intimidation. Those who dwell within a black dragon’s reach live in _[[universal monster rules/Fear|fear]]_. Black dragons tend to make their lairs in remote parts of the swamp, preferably in caves at the bottom of dark and fetid pools. Inside, they pile up their filthy treasure and sleep amid the roots and muck. Black dragons prefer their food a bit rotten and will often allow a meal to sit in a pool for days before consuming it. Black dragons prefer treasures that do not rot or decay, making their hoard, full of coins, gemstones, _[[items/Mundane/Jewelry|jewelry]]_, and other objects made from stone or metal.
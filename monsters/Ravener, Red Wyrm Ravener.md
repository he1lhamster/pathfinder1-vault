---
cssclass: [monsters]
title1: Ravener, Red Wyrm Ravener
desc_short: This immense skeletal dragon rears up to its full, towering height, bones
  glowing and shimmering with vile green energy.
title2: Red Wyrm Ravener
CR: 22
sources:
- name: Bestiary 2
  page: 230
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 614400
alignment: CE
size: Gargantuan
type: undead
subtypes:
- fire
initiative:
  bonus: 3
senses:
  blindsense: 120
  darkvision: 240
  smoke vision: true
auras:
- name: cowering fear
- name: fire
- name: frightful presence
  radius: 330
  DC: 31
AC:
  AC: 45
  touch: 9
  flat_footed: 45
  components:
    deflection: 4
    dex: -1
    natural: 36
    size: -4
HP:
  HP: 337
  long: 27d8+216
saves:
  fort: 23
  ref: 14
  will: 23
defensive_abilities:
- channel resistance +4
- soul ward (27 hp)
DR:
- amount: 20
  weakness: good
immunities:
- fire
- undead traits
SR: 33
weaknesses:
- vulnerability to cold
speeds:
  base: 40
  fly: 250
  fly_maneuverability: clumsy
attacks:
  melee:
  - - text: bite +40 (4d6+24/17-20)
      entries:
      - - damage: 4d6+24
          crit_range: 17-20
      attack: bite
      bonus:
      - 40
    - text: 2 claws +40 (2d8+16/19-20)
      entries:
      - - damage: 2d8+16
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 40
    - text: tail slap +38 (2d8+24/19-20)
      entries:
      - - damage: 2d8+24
          crit_range: 19-20
      attack: tail slap
      bonus:
      - 38
    - text: 2 wings +38 (2d6+8/19-20)
      entries:
      - - damage: 2d6+8
          crit_range: 19-20
      count: 2
      attack: wings
      bonus:
      - 38
  special:
  - breath weapon (60-ft. cone, DC 31, 22d10 fire and 2 negative levels)
  - crush
  - manipulate flames
  - melt stone
  - soul consumption
  - soul magic
  - tail sweep
space: 20
reach: 15
reach_other: 20 ft. with bite
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: At will
  - name: find the path
    source: default
    freq: At will
  - name: pyrotechnics
    source: default
    freq: At will
    DC: 20
  - name: suggestion
    source: default
    freq: At will
    DC: 21
  - name: wall of fire
    source: default
    freq: At will
  sources:
  - name: default
    CL: 27
    concentration: 35
spells:
  entries:
  - name: energy drain
    source: Sorcerer
    level: 9
  - name: time stop
    source: Sorcerer
    level: 9
  - name: wish
    source: Sorcerer
    level: 9
  - name: dimensional lock
    source: Sorcerer
    level: 8
  - name: horrid wilting
    source: Sorcerer
    level: 8
    DC: 26
  - name: maze
    source: Sorcerer
    level: 8
  - name: forcecage
    source: Sorcerer
    level: 7
    DC: 25
  - name: greater teleport
    source: Sorcerer
    level: 7
  - name: spell turning
    source: Sorcerer
    level: 7
  - name: chain lightning
    source: Sorcerer
    level: 6
    DC: 24
  - name: greater dispel magic
    source: Sorcerer
    level: 6
  - name: true seeing
    source: Sorcerer
    level: 6
  - name: cone of cold
    source: Sorcerer
    level: 5
    DC: 23
  - name: dominate person
    source: Sorcerer
    level: 5
    DC: 23
  - name: feeblemind
    source: Sorcerer
    level: 5
    DC: 23
  - name: wall of force
    source: Sorcerer
    level: 5
  - name: charm monster
    source: Sorcerer
    level: 4
    DC: 22
  - name: confusion
    source: Sorcerer
    level: 4
    DC: 22
  - name: greater invisibility
    source: Sorcerer
    level: 4
  - name: solid fog
    source: Sorcerer
    level: 4
  - name: displacement
    source: Sorcerer
    level: 3
  - name: haste
    source: Sorcerer
    level: 3
  - name: slow
    source: Sorcerer
    level: 3
    DC: 21
  - name: vampiric touch
    source: Sorcerer
    level: 3
  - name: detect thoughts
    source: Sorcerer
    level: 2
    DC: 20
  - name: false life
    source: Sorcerer
    level: 2
  - name: mirror image
    source: Sorcerer
    level: 2
  - name: see invisibility
    source: Sorcerer
    level: 2
  - name: web
    source: Sorcerer
    level: 2
    DC: 20
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: ray of enfeeblement
    source: Sorcerer
    level: 1
    DC: 19
  - name: shield
    source: Sorcerer
    level: 1
  - name: true strike
    source: Sorcerer
    level: 1
  - name: arcane mark
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: mending
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  - name: ray of frost
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: touch of fatigue
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 20
    concentration: 28
ability_scores:
  STR: 45
  DEX: 8
  CON:
  INT: 24
  WIS: 25
  CHA: 26
BAB: 27
CMB: 48
CMD: 57
CMD_other: 61 vs. trip
feats:
- name: Cleave
- name: Critical Focus
- name: Greater Vital Strike
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Iron Will
- name: Improved Vital Strike
- name: Iron Will
- name: Multiattack
- name: Power Attack
- name: Quicken Spell
- name: Staggering Critical
- name: Stunning Critical
- name: Vital Strike
skills:
  Appraise: 37
  Bluff: 37
  Diplomacy: 37
  Fly: 13
  Intimidate: 45
  Knowledge (arcana): 37
  Knowledge (history): 37
  Knowledge (religion): 34
  Perception: 45
  Sense Motive: 37
  Spellcraft: 37
  Stealth: 25
languages:
- Abyssal
- Aklo
- Common
- Draconic
- Elven
- Giant
- Infernal
ecology:
  environment: warm mountains
  organization: solitary
  treasure_type: triple
desc_long: |-
  Most evil dragons spend their lifetimes coveting and amassing wealth, but when the end draws near, some come to realize that all the wealth in the world cannot forestall death. Faced with this truth, most dragons vent their frustration on the countryside, ravaging the world before their passing. Yet some seek a greater solution to the problem and decide instead to linger on, hoarding life as they once hoarded gold. These foul wyrms attract the attention of dark powers, and through the blackest of necromantic rituals are transformed into undead dragons known as raveners.

  Although its body quickly rots away, a ravener does not care for the needs of the flesh. It seeks only to consume life, be it from wild animals, would-be dragonslayers, or even other dragons. A ravener is often on the move, changing lairs frequently as its territories become devoid of life.

  The ravener presented here is built from a red dragon wyrm.

---

# Ravener, Red Wyrm Ravener
This immense skeletal dragon rears up to its full, towering height, bones glowing and shimmering with vile green energy.
**Source** Bestiary 2 pg. 230
**XP** 614,400
CE Gargantuan undead (fire)
**Init** +3; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 120 ft., _[[spells/Darkvision|darkvision]]_ 240 ft., smoke _[[spells/Vision|vision]]_; Perception +45
**Aura** _[[conditions/Cowering|cowering]]_ _[[universal monster rules/Fear|fear]]_, fire, _[[universal monster rules/Frightful Presence|frightful presence]]_ (330 ft., DC 31)

##### Defense

**AC** 45, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 45 (+4 deflection, –1 Dex, +36 natural, –4 size)
**hp** 337 (27d8+216)
**Fort** +23, **Ref** +14, **Will** +23
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4, soul ward (27 hp); **DR** 20/good; **Immune** fire, _[[universal monster rules/Undead Traits|undead traits]]_; **SR** 33
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to cold

##### Offense
**Speed** 40 ft., fly 250 ft. (clumsy)
**Melee** bite +40 (4d6+24/17–20), 2 claws +40 (2d8+16/19–20), tail slap +38 (2d8+24/19–20), 2 wings +38 (2d6+8/19–20)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, DC 31, 22d10 fire and 2 negative levels), crush, manipulate flames, melt stone, soul _[[feats/Consumption|consumption]]_, soul magic, tail sweep
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 27th, concentration +35)
At will—_[[spells/Detect Magic|detect magic]]_, _[[spells/Find the Path|find the path]]_, _[[spells/Pyrotechnics|pyrotechnics]]_ (DC 20), _[[spells/Suggestion|suggestion]]_ (DC 21), _[[spells/Wall Of Fire|wall of fire]]_
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 20th, concentration +28)
9th—_[[universal monster rules/Energy Drain|energy drain]]_, _[[spells/Time Stop|time stop]]_, _[[spells/Wish|wish]]_
8th—_[[spells/Dimensional Lock|dimensional lock]]_, _[[spells/Horrid Wilting|horrid wilting]]_ (DC 26), _[[spells/Maze|maze]]_
7th—_[[spells/Forcecage|forcecage]]_ (DC 25), greater teleport, _[[spells/Spell Turning|spell turning]]_
6th—_[[spells/Chain Lightning|chain lightning]]_ (DC 24), greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/True Seeing|true seeing]]_
5th—_[[spells/Cone of Cold|cone of cold]]_ (DC 23), _[[spells/Dominate Person|dominate person]]_ (DC 23), _[[spells/Feeblemind|feeblemind]]_ (DC 23), _[[spells/Wall Of Force|wall of force]]_
4th—_[[spells/Charm Monster|charm monster]]_ (DC 22), _[[spells/Confusion|confusion]]_ (DC 22), greater _[[spells/Invisibility|invisibility]]_, _[[spells/Solid Fog|solid fog]]_
3rd—_[[spells/Displacement|displacement]]_, _[[spells/Haste|haste]]_, _[[spells/Slow|slow]]_ (DC 21), _[[spells/Vampiric Touch|vampiric touch]]_
2nd—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 20), _[[spells/False Life|false life]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/See Invisibility|see invisibility]]_, web (DC 20)
1st—_[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 19), _[[spells/Shield|shield]]_, _[[spells/True Strike|true strike]]_
0—_[[spells/Arcane Mark|arcane mark]]_, _detect magic_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_

##### Statistics
**Str** 45, **Dex** 8, **Con** —, **Int** 24, **Wis** 25, **Cha** 26
**Base Atk** +27; **CMB** +48; **CMD** 57 (61 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Stunning Critical|Stunning Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Appraise +37, Bluff +37, Diplomacy +37, Fly +13, Intimidate +45, Knowledge (arcana) +37, Knowledge (history) +37, Knowledge (religion) +34, Perception +45, Sense Motive +37, Spellcraft +37, Stealth +25
**Languages** Abyssal, Aklo, Common, Draconic, Elven, Giant, Infernal

##### Ecology

**Environment** warm mountains
**Organization** solitary
**Treasure** triple

##### Description

Most evil dragons spend their lifetimes coveting and amassing wealth, but when the end draws near, some come to realize that all the wealth in the world cannot forestall death. Faced with this truth, most dragons vent their frustration on the countryside, ravaging the world before their passing. Yet some seek a greater solution to the problem and decide instead to linger on, hoarding life as they once hoarded gold. These foul wyrms attract the attention of dark powers, and through the blackest of necromantic rituals are transformed into undead dragons known as raveners.

Although its body quickly rots away, a ravener does not care for the needs of the flesh. It seeks only to consume life, be it from wild animals, would-be dragonslayers, or even other dragons. A ravener is often on the move, changing lairs frequently as its territories become devoid of life.

The ravener presented here is built from a red dragon wyrm.
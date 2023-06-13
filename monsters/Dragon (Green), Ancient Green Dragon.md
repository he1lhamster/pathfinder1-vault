---
cssclass: [monsters]
title1: Dragon (Green), Ancient Green Dragon
title2: Ancient Green Dragon
CR: 17
sources:
- name: Pathfinder RPG Bestiary
  page: 97
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 102400
alignment: LE
size: Gargantuan
type: dragon
subtypes:
- air
initiative:
  bonus: -1
senses:
  dragon senses: true
auras:
- name: frightful presence
  radius: 300
  DC: 26
AC:
  AC: 36
  touch: 5
  flat_footed: 36
  components:
    dex: -1
    natural: 31
    size: -4
HP:
  HP: 310
  long: 23d12+161
saves:
  fort: 20
  ref: 12
  will: 20
DR:
- amount: 15
  weakness: magic
immunities:
- acid
- paralysis
- sleep
SR: 28
speeds:
  base: 40
  fly: 250
  fly_maneuverability: clumsy
  swim: 40
attacks:
  melee:
  - - text: bite +31 (4d6+18/19-20)
      entries:
      - - damage: 4d6+18
          crit_range: 19-20
      attack: bite
      bonus:
      - 31
    - text: 2 claws +31 (2d8+12/19-20)
      entries:
      - - damage: 2d8+12
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 31
    - text: 2 wings +29 (2d6+6)
      entries:
      - - damage: 2d6+6
      count: 2
      attack: wings
      bonus:
      - 29
    - text: tail slap +29 (2d8+18)
      entries:
      - - damage: 2d8+18
      attack: tail slap
      bonus:
      - 29
  special:
  - breath weapon (60-ft. cone, DC 28, 20d6 acid)
  - crush (Medium creatures, DC 28, 4d6+18)
  - miasma
  - tail sweep
space: 20
reach: 15
reach_other: 20 ft. with bite
spell_like_abilities:
  entries:
  - name: charm person
    source: default
    freq: At will
    DC: 16
  - name: dominate person
    source: default
    freq: At will
    DC: 20
  - name: entangle
    source: default
    freq: At will
    DC: 16
  - name: plant growth
    source: default
    freq: At will
  - name: suggestion
    source: default
    freq: At will
    DC: 18
  sources:
  - name: default
    CL: 23
spells:
  entries:
  - name: disintegrate
    source: '?'
    level: 6
    DC: 21
  - name: true seeing
    source: '?'
    level: 6
  - name: polymorph
    source: '?'
    level: 5
  - name: summon monster V
    source: '?'
    level: 5
  - name: teleport
    source: '?'
    level: 5
  - name: dimension door
    source: '?'
    level: 4
  - name: ice storm
    source: '?'
    level: 4
  - name: scrying
    source: '?'
    level: 4
    DC: 19
  - name: stoneskin
    source: '?'
    level: 4
  - name: dispel magic
    source: '?'
    level: 3
  - name: displacement
    source: '?'
    level: 3
  - name: fireball
    source: '?'
    level: 3
    DC: 18
  - name: haste
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
  - name: mirror image
    source: '?'
    level: 2
  - name: see invisibility
    source: '?'
    level: 2
  - name: magic missile
    source: '?'
    level: 1
  - name: shield
    source: '?'
    level: 1
  - name: silent image
    source: '?'
    level: 1
    DC: 16
  - name: summon monster I
    source: '?'
    level: 1
  - name: ventriloquism
    source: '?'
    level: 1
    DC: 16
  - name: dancing lights
    source: '?'
    level: 0
  - name: detect magic
    source: '?'
    level: 0
  - name: ghost sound
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: message
    source: '?'
    level: 0
  - name: prestidigitation
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 13
    slots:
      6: 4
      5: 7
      4: 7
      3: 7
      2: 7
      1: 7
      0: at-will
ability_scores:
  STR: 35
  DEX: 8
  CON: 25
  INT: 20
  WIS: 21
  CHA: 20
BAB: 23
CMB: 39
CMD: 48
CMD_other: 52 vs. trip
feats:
- name: Alertness
- name: Bleeding Critical
- name: Cleave
- name: Critical Focus
- name: Flyby Attack
- name: Great Cleave
- name: Improved Critical (bite)
- name: Improved Critical (claws)
- name: Improved Sunder
- name: Iron Will
- name: Multiattack
- name: Power Attack
skills:
  Fly: 9
  Knowledge (arcane): 31
  Knowledge (local): 31
  Knowledge (nature): 31
  Knowledge (planes): 31
  Perception: 35
  Spellcraft: 31
  Stealth: 13
  Survival: 31
  Swim: 46
  Use Magic Device: 31
languages:
- Abyssal
- Common
- Draconic
- Elven
- Giant
- Sylvan
special_qualities:
- camouflage
- trackless step
- water breathing
- woodland stride
ecology:
  environment: temperate forests
desc_long: Green dragons dwell in the ancient forests of the world, prowling under
  towering canopies in search of prey. Of all the chromatic dragons, green dragons
  are perhaps the easiest to deal with diplomatically.

---

# Dragon (Green), Ancient Green Dragon

**Source** Pathfinder RPG Bestiary pg. 97
**XP** 102,400

LE Gargantuan dragon (air)
**Init** –1; **Senses** _[[universal monster rules/Dragon Senses|dragon senses]]_; Perception +35
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (300 ft., DC 26)

##### Defense

**AC** 36, touch 5, _[[conditions/Flat-Footed|flat-footed]]_ 36 (–1 Dex, +31 natural, –4 size)
**hp** 310 (23d12+161)
**Fort** +20, **Ref** +12, **Will** +20
**DR** 15/magic; **Immune** acid, _[[universal monster rules/Paralysis|paralysis]]_, sleep; **SR** 28

##### Offense
**Speed** 40 ft., fly 250 ft. (clumsy), swim 40 ft.
**Melee** bite +31 (4d6+18/19–20), 2 claws +31 (2d8+12/19–20), 2 wings +29 (2d6+6), tail slap +29 (2d8+18)
**Space** 20 ft., **Reach** 15 ft. (20 ft. with bite)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, DC 28, 20d6 acid), crush (Medium creatures, DC 28, 4d6+18), miasma, tail sweep
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 23rd)
At will—_[[spells/Charm Person|charm person]]_ (DC 16), _[[spells/Dominate Person|dominate person]]_ (DC 20), _[[spells/Entangle|entangle]]_ (DC 16), _[[spells/Plant Growth|plant growth]]_, _[[spells/Suggestion|suggestion]]_ (DC 18)
**Spells Known **(CL 13th)
6th (4/day)—_[[spells/Disintegrate|disintegrate]]_ (DC 21), _[[spells/True Seeing|true seeing]]_
5th (7/day)—_[[spells/Polymorph|polymorph]]_, _[[spells/Summon Monster V|summon monster V]]_, teleport
4th (7/day)—_[[spells/Dimension Door|dimension door]]_, _[[spells/Ice Storm|ice storm]]_, _[[spells/Scrying|scrying]]_ (DC 19), _[[spells/Stoneskin|stoneskin]]_
3rd (7/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Displacement|displacement]]_, _[[spells/Fireball|fireball]]_ (DC 18), _[[spells/Haste|haste]]_
2nd (7/day)—_[[spells/Alter Self|alter self]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 17), _[[spells/Locate Object|locate object]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/See Invisibility|see invisibility]]_
1st (7/day)—_[[spells/Magic Missile|magic missile]]_, _[[spells/Shield|shield]]_, _[[spells/Silent Image|silent image]]_ (DC 16), _[[spells/Summon Monster I|summon monster I]]_, _[[spells/Ventriloquism|ventriloquism]]_ (DC 16)
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_

##### Statistics
**Str** 35, **Dex** 8, **Con** 25, **Int** 20, **Wis** 21, **Cha** 20
**Base Atk** +23; **CMB** +39; **CMD** 48 (52 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite, claws), _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Fly +9, Knowledge (arcane) +31, Knowledge (local) +31, Knowledge (nature) +31, Knowledge (planes) +31, Perception +35, Spellcraft +31, Stealth +13, Survival +31, Swim +46, Use Magic Device +31
**Languages** Abyssal, Common, Draconic, Elven, Giant, Sylvan
**SQ** camouflage, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, _[[universal monster rules/Water Breathing|water breathing]]_, woodland stride

##### Ecology

**Environment** temperate forests

Green dragons dwell in the ancient forests of the world, prowling under towering canopies in search of prey. Of all the chromatic dragons, green dragons are perhaps the easiest to deal with diplomatically.
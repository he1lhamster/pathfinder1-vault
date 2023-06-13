---
cssclass: [monsters]
title1: Telgrodradt
desc_short: This monster resembles a gigantic, writhing grub, its translucent flesh
  rippling disgustingly. It has four elongated tentacles and a toothy maw.
title2: Telgrodradt
CR: 6
sources:
- name: 'Pathfinder #100: A Song of Silver'
  page: 120
  link: http://paizo.com/products/btpy9grm?Pathfinder-Adventure-Path-100-A-Song-of-Silver
XP: 2400
alignment: NE
size: Large
type: aberration
initiative:
  bonus: 6
senses:
  darkvision: 60
AC:
  AC: 19
  touch: 11
  flat_footed: 17
  components:
    dex: 2
    natural: 8
    size: -1
HP:
  HP: 67
  long: 9d8+27
saves:
  fort: 6
  ref: 5
  will: 7
defensive_abilities:
- negative energy affinity
speeds:
  base: 30
  burrow: 10
attacks:
  melee:
  - - text: 2 claws +10 (1d6+4)
      entries:
      - - damage: 1d6+4
      count: 2
      attack: claws
      bonus:
      - 10
    - text: bite +9 (1d8+4 plus disease)
      entries:
      - - damage: 1d8+4
        - effect: disease
      attack: bite
      bonus:
      - 9
  ranged:
  - - text: negative energy ray +7 touch (3d6 negative energy)
      entries:
      - - damage: 3d6
          type: negative energy
      attack: negative energy ray
      bonus:
      - 7
      touch: true
  special:
  - create thralls
  - disease
  - negative energy ray
space: 10
reach: 10
reach_other: 5 ft. with bite
spell_like_abilities:
  entries:
  - name: curse water
    source: default
    freq: At will
  - name: detect undead
    source: default
    freq: At will
  - name: darkness
    source: default
    freq: 3/day
  - name: death knell
    source: default
    freq: 3/day
  - name: inflict moderate wounds
    source: default
    freq: 3/day
    DC: 14
  - name: animate dead
    source: default
    freq: 1/day
  - name: desecrate
    source: default
    freq: 1/day
  - name: see invisibility
    source: default
    freq: 1/day
  - name: silence
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 9
    concentration: 11
ability_scores:
  STR: 18
  DEX: 15
  CON: 16
  INT: 9
  WIS: 13
  CHA: 14
BAB: 6
CMB: 11
CMD: 23
feats:
- name: Blind-Fight
- name: Combat Reflexes
- name: Improved Initiative
- name: Power Attack
- name: Weapon Focus (claw)
skills:
  Intimidate: 8
  Knowledge (religion): 8
  Perception: 10
  Stealth: 10
languages:
- Necril
- Undercommon
ecology:
  environment: underground
  organization: solitary, pair, gathering (3-12), or settlement (12-30 telgrodradts
    and 200-500 zombies and skeletons)
  treasure_type: standard
special_abilities:
  Create Thralls (Su): 'Any creature that dies from the disease a telgrodradt transmits
    rises in 24 hours as if it were raised by animate dead (CL 9th). This ability
    can create only exoskeletons (Pathfinder Adventure Path #91: Battle of Bloodmarch
    Hill 84), skeletons, or zombies. This is determined by the amount of flesh left
    on the corpse and the corpse's creature type. While a telgrodradt has no natural
    ability to control these mindless undead, the undead created in this manner don't
    attack or otherwise intentionally harm the telgrodradt.'
  Disease (Su): Bite-injury; save Fort DC 17; onset 1d3 days; frequency 1 day; effect
    1 Con damage; cure 2 consecutive saves.
  Negative Energy Ray (Su): A telgrodradt can fire a sickly purple beam of negative
    energy from its eyes at a single target within 60 feet. If the telgrodradt successfully
    hits, the target takes 3d6 points of negative energy damage. This ray can also
    heal undead creatures. A telgrodradt can't target itself with this ability, but
    it can be healed by the negative energy rays of other telgrodradts.
desc_long: These strange Darklands creatures savor the flesh of the undead, while
  at the same time being one step in the grave themselves. Mistaken for undead by
  those who encounter them and inscrutable to most living things, telgrodradts straddle
  a strange line between worlds. These strange abominations look like a nightmarish
  fusion of insect, humanoid, and corpse. Telgrodradts have six multi-jointed appendages
  that they use to skitter about and burrow, as well as four hooked, probing tentacles
  that act as antennae. A typical telgrodradt stretches 14 feet from head to tail
  and weighs upward of 2,500 pounds, though larger and smaller specimens do exist.

---

# Telgrodradt
This monster resembles a gigantic, writhing grub, its translucent flesh rippling disgustingly. It has four elongated tentacles and a toothy maw.
**Source** Pathfinder #100: A Song of Silver pg. 120
**XP** 2,400

NE Large aberration
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +10

##### Defense

**AC** 19, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+2 Dex, +8 natural, –1 size)
**hp** 67 (9d8+27)
**Fort** +6, **Ref** +5, **Will** +7
**Defensive Abilities** _[[universal monster rules/Negative Energy Affinity|negative energy affinity]]_

##### Offense
**Speed** 30 ft., _[[universal monster rules/Burrow|burrow]]_ 10 ft.
**Melee** 2 claws +10 (1d6+4), bite +9 (1d8+4 plus disease)
**Ranged** negative energy ray +7 touch (3d6 negative energy)
**Space** 10 ft., **Reach** 10 ft. (5 ft. with bite)
**Special Attacks** create thralls, disease, negative energy ray
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +11)
At will—_[[spells/Curse Water|curse water]]_, _[[spells/Detect Undead|detect undead]]_
3/day—_[[spells/Darkness|darkness]]_, _[[spells/Death Knell|death knell]]_, _[[spells/Inflict Moderate Wounds|inflict moderate wounds]]_ (DC 14)
1/day—_[[spells/Animate Dead|animate dead]]_, _[[spells/Desecrate|desecrate]]_, _[[spells/See Invisibility|see invisibility]]_, _[[spells/Silence|silence]]_

##### Statistics
**Str** 18, **Dex** 15, **Con** 16, **Int** 9, **Wis** 13, **Cha** 14
**Base Atk** +6; **CMB** +11; **CMD** 23
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Intimidate +8, Knowledge (religion) +8, Perception +10, Stealth +10
**Languages** Necril, Undercommon

##### Ecology

**Environment** underground
**Organization** solitary, pair, gathering (3–12), or settlement (12–30 telgrodradts and 200–500 zombies and skeletons)
**Treasure** standard

### Special Abilities

**Create Thralls (Su)** Any creature that dies from the disease a _[[monsters/Telgrodradt|telgrodradt]]_ transmits rises in 24 hours as if it were raised by _animate dead_ (CL 9th). This ability can create only exoskeletons (Pathfinder Adventure Path #91: Battle of Bloodmarch Hill 84), skeletons, or zombies. This is determined by the amount of flesh left on the corpse and the corpse’s creature type. While a _telgrodradt_ has no natural ability to control these mindless undead, the undead created in this manner don’t attack or otherwise intentionally _[[spells/Harm|harm]]_ the _telgrodradt_.

**Disease (Su)** Bite—injury; save Fort DC 17; onset 1d3 days; frequency 1 day; effect 1 Con damage; cure 2 consecutive saves.

**Negative Energy Ray (Su)** A _telgrodradt_ can fire a sickly purple beam of negative energy from its eyes at a single target within 60 feet. If the _telgrodradt_ successfully hits, the target takes 3d6 points of negative energy damage. This ray can also _[[spells/Heal|heal]]_ undead creatures. A _telgrodradt_ can’t target itself with this ability, but it can be healed by the negative energy rays of other telgrodradts.

##### Description

These strange Darklands creatures savor the flesh of the undead, while at the same time being one step in the grave themselves. Mistaken for undead by those who encounter them and inscrutable to most living things, telgrodradts straddle a strange line between worlds. These strange abominations look like a nightmarish fusion of insect, humanoid, and corpse. Telgrodradts have six multi-jointed appendages that they use to skitter about and _burrow_, as well as four hooked, probing tentacles that act as antennae. A typical _telgrodradt_ stretches 14 feet from head to tail and weighs upward of 2,500 pounds, though larger and smaller specimens do exist.
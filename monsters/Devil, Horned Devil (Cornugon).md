---
cssclass: [monsters]
title1: Devil, Horned Devil (Cornugon)
desc_short: Bristling with terrible spines and a crown of deadly horns, this leering
  winged terror wields a whirling barbed chain.
title2: Horned Devil (Cornugon)
CR: 16
sources:
- name: Pathfinder RPG Bestiary
  page: 76
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 76800
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
  see in darkness: true
auras:
- name: fear aura
  radius: 5
  DC: 23
AC:
  AC: 35
  touch: 17
  flat_footed: 27
  components:
    dex: 8
    natural: 18
    size: -1
HP:
  HP: 217
  long: 15d10+135
  regeneration: 5
  regeneration_weakness: good weapons, good spells
saves:
  fort: 18
  ref: 17
  will: 13
DR:
- amount: 10
  weakness: good and silver
immunities:
- fire
- poison
resistances:
  acid: 10
  cold: 10
SR: 27
speeds:
  base: 30
  fly: 50
  fly_maneuverability: average
attacks:
  melee:
  - - text: +1 unholy spiked chain +26/+21/+16 (2d6+11 plus stun)
      entries:
      - - damage: 2d6+11
        - effect: stun
      attack: +1 unholy spiked chain
      bonus:
      - 26
      - 21
      - 16
    - text: bite +22 (2d8+5)
      entries:
      - - damage: 2d8+5
      attack: bite
      bonus:
      - 22
    - text: tail +22 (2d6+5 plus infernal wound)
      entries:
      - - damage: 2d6+5
        - effect: infernal wound
      attack: tail
      bonus:
      - 22
  - - text: 2 claws +24 (2d6+10)
      entries:
      - - damage: 2d6+10
      count: 2
      attack: claws
      bonus:
      - 24
    - text: bite +24 (2d8+10)
      entries:
      - - damage: 2d8+10
      attack: bite
      bonus:
      - 24
    - text: tail +22 (2d6+5 plus infernal wound)
      entries:
      - - damage: 2d6+5
        - effect: infernal wound
      attack: tail
      bonus:
      - 22
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: dispel chaos
    source: default
    freq: At will
    DC: 21
  - name: dispel good
    source: default
    freq: At will
    DC: 21
  - name: magic circle against good
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: persistent image
    source: default
    freq: At will
    DC: 21
  - name: fireball
    source: default
    freq: 3/day
    DC: 19
  - name: lightning bolt
    source: default
    freq: 3/day
    DC: 19
  - name: summon
    source: default
    freq: 1/day
    level: 6
    summons:
    - name: barbed devils
      amount: 3
      chance: 35%
  sources:
  - name: default
    CL: 16
ability_scores:
  STR: 31
  DEX: 27
  CON: 28
  INT: 14
  WIS: 22
  CHA: 23
BAB: 15
CMB: 26
CMD: 44
feats:
- name: Improved Bull Rush
- name: Improved Sunder
- name: Improved Vital Strike
- name: Iron Will
- name: Multiattack
- name: Power Attack
- name: Vital Strike
- name: Weapon Focus (spiked chain)
skills:
  Bluff: 24
  Diplomacy: 21
  Fly: 15
  Intimidate: 24
  Knowledge (planes): 20
  Perception: 24
  Sense Motive: 21
  Spellcraft: 20
  Stealth: 22
languages:
- Celestial
- Common
- Draconic
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Hell)
  organization: solitary, pair, or wing (3-10)
  treasure_type: standard
  treasure:
  - +1 unholy spiked chain
  - other treasure
special_abilities:
  Infernal Wound (Su): The damage a horned devil deals with its tail causes persistent
    wounds that deal 2d6 points of bleed damage. Bleeding caused in this way is difficult
    to staunch-a DC 26 Heal check stops the damage, and any attempt to heal a creature
    suffering from an infernal wound must succeed on a DC 26 caster level check or
    the spell does not function. Success indicates the healing works normally and
    stops all bleed effects.
  Stun (Su): Whenever a horned devil hits with a spiked chain attack, the opponent
    must succeed on a DC 27 Fortitude save or be stunned for 1d4 rounds. This ability
    is a function of the horned devil, not of the spiked chain. The save DC is Strength-based.
desc_long: |-
  Among the deadliest of the archdevils' warriors and able commanders of lesser fiends, horned devils spread the rule of Hell wherever they tread. These greater devils are trained, forged, and reforged to be among the most lethal, merciless, and obedient warriors in the multiverse. While rank-and-file horned devils are called cornugons, the greatest of their kind are known as malebranche.

  A typical horned devil rises to a hulking 9 feet tall, bears 14-foot-wide wings, and weighs 700 pounds.

---

# Devil, Horned Devil (Cornugon)
Bristling with terrible spines and a crown of _[[feats/Deadly Horns|deadly horns]]_, this leering winged terror wields a whirling barbed chain.
**Source** Pathfinder RPG Bestiary pg. 76
**XP** 76,800

LE Large outsider (devil, evil, extraplanar, lawful)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +24
**Aura** _[[universal monster rules/Fear|fear]]_ aura (5 ft., DC 23)

##### Defense

**AC** 35, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+8 Dex, +18 natural, –1 size)
**hp** 217 (15d10+135); _[[universal monster rules/Regeneration|regeneration]]_ 5 (good weapons, good spells)
**Fort** +18, **Ref** +17, **Will** +13
**DR** 10/good and silver; **Immune** fire, poison; **Resist** acid 10, cold 10; **SR** 27

##### Offense
**Speed** 30 ft., fly 50 ft. (average)
**Melee** +1 _[[items/Weapon Magic Abilities/Unholy|unholy]]_ _[[items/Weapon/Spiked chain|spiked chain]]_ +26/+21/+16 (2d6+11 plus stun), bite +22 (2d8+5), tail +22 (2d6+5 plus infernal wound) or 2 claws +24 (2d6+10), bite +24 (2d8+10), tail +22 (2d6+5 plus infernal wound)
**Space** 10 ft., **Reach** 10 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th)
At will—_[[spells/Dispel Chaos|dispel chaos]]_ (DC 21), _[[spells/Dispel Good|dispel good]]_ (DC 21), _[[spells/Magic Circle against Good|magic circle against good]]_, greater teleport (self plus 50 lbs. of objects only), _[[spells/Persistent Image|persistent image]]_ (DC 21)
3/day—_[[spells/Fireball|fireball]]_ (DC 19), _[[spells/Lightning Bolt|lightning bolt]]_ (DC 19)
1/day—_[[universal monster rules/Summon|summon]]_ (level 6, 3 barbed devils, 35%)

##### Statistics
**Str** 31, **Dex** 27, **Con** 28, **Int** 14, **Wis** 22, **Cha** 23
**Base Atk** +15; **CMB** +26; **CMD** 44
**Feats** _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_spiked chain_)
**Skills** Bluff +24, Diplomacy +21, Fly +15, Intimidate +24, Knowledge (planes) +20, Perception +24, Sense Motive +21, Spellcraft +20, Stealth +22
**Languages** Celestial, Common, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Hell)
**Organization** solitary, pair, or wing (3–10)
**Treasure** standard (+1 _unholy_ _spiked chain_, other treasure)

### Special Abilities

**Infernal Wound (Su)** The damage a horned devil deals with its tail causes persistent wounds that deal 2d6 points of _[[universal monster rules/Bleed|bleed]]_ damage. Bleeding caused in this way is difficult to staunch—a DC 26 _[[spells/Heal|Heal]]_ check stops the damage, and any attempt to _heal_ a creature suffering from an infernal wound must succeed on a DC 26 caster level check or the spell does not function. Success indicates the healing works normally and stops all _bleed_ effects.
**Stun (Su)** Whenever a horned devil hits with a _spiked chain_ attack, the opponent must succeed on a DC 27 Fortitude save or be _[[conditions/Stunned|stunned]]_ for 1d4 rounds. This ability is a function of the horned devil, not of the _spiked chain_. The save DC is Strength-based.

##### Description

Among the deadliest of the archdevils’ warriors and able commanders of lesser fiends, horned devils spread the rule of Hell wherever they tread. These greater devils are trained, forged, and reforged to be among the most lethal, merciless, and obedient warriors in the multiverse. While rank-and-file horned devils are _[[items/Weapon Magic Abilities/Called|called]]_ cornugons, the greatest of their kind are known as malebranche.

A typical horned devil rises to a hulking 9 feet tall, bears 14-foot-wide wings, and weighs 700 pounds.
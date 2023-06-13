---
cssclass: [monsters]
title1: Azi, Sruvara
is_3.5: true
desc_short: Hissing poison drips from the many-fanged maw of this monstrous serpent.
  Its body like that of some gigantic venomous snake, this sinister wyrm-like beast
  undulates with frightening speed, and two pairs of lean wings rise from the base
  of a thick neck supporting a powerful, draconic visage.
title2: Sruvara
CR: 15
sources:
- name: 'Pathfinder #24: The Final Wish'
  page: 80
  link: http://paizo.com/pathfinder/adventurePath/legacyOfFire/v5748btpy89a2
alignment: NE
size: Huge
type: dragon
initiative:
  bonus: 12
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 34
  touch: 16
  flat_footed: 26
  components:
    dex: 8
    natural: 18
    size: -2
HP:
  HP: 243
  long: 18d12+126
saves:
  fort: 18
  ref: 21
  will: 13
DR:
- amount: 10
  weakness: magic
immunities:
- disease
- paralysis effects
- poison
- sleep
resistances:
  acid: 10
  fire: 10
SR: 25
speeds:
  base: 60
  climb: 30
  fly: 120
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +24 (2d8+8 plus poison)
      entries:
      - - damage: 2d8+8
        - effect: poison
      attack: bite
      bonus:
      - 24
    - text: 2 claws +22 (2d6+4)
      entries:
      - - damage: 2d6+4
      count: 2
      attack: claws
      bonus:
      - 22
    - text: sting +22 (2d6+4 plus poison)
      entries:
      - - damage: 2d6+4
        - effect: poison
      attack: sting
      bonus:
      - 22
  special:
  - breath weapon
  - noxious cloud
  - poison
space: 15
reach: 10
reach_other: bite 15 ft.
spell_like_abilities:
  entries:
  - name: acid arrow
    source: default
    freq: At will
  - name: curse water
    source: default
    freq: At will
  - name: detect thoughts
    source: default
    freq: At will
    DC: 17
  - name: major image
    source: default
    freq: At will
    DC: 18
  - name: ventriloquism
    source: default
    freq: At will
    DC: 15
  - name: blindness/deafness
    source: default
    freq: 3/day
    DC: 17
  - name: confusion
    source: default
    freq: 3/day
    DC: 19
  - name: dimension door
    source: default
    freq: 3/day
  - name: displacement
    source: default
    freq: 3/day
    DC: 18
  - name: acid fog
    source: default
    freq: 1/day
  - name: gaseous form
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 16
ability_scores:
  STR: 27
  DEX: 26
  CON: 25
  INT: 12
  WIS: 15
  CHA: 20
BAB: 18
grapple_3.5: 34
feats:
- name: Blind-Fight
- name: Combat Expertise
- name: Combat Reflexes
- name: Improved Initiative
- name: Improved Trip
- name: Lightning Reflexes
- name: Multiattack
skills:
  Appraise: 12
  Balance: 19
  Bluff: 26
  Climb: 26
  Hide: 21
  Intimidation: 18
  Jump: 30
  Knowledge (arcana): 11
  Listen: 13
  Move Silently: 29
  Spot: 12
languages:
- Common
- Draconic
- Infernal
ecology:
  environment: warm marshes
  organization: solitary
  treasure_type: standard
  advancement_3.5:
  - type: size
    HD_min: 19
    size: Huge
    HD_max: 27
  - type: size
    HD_min: 28
    size: Gargantuan
    HD_max: 36
special_abilities:
  Breath Weapon (Su): |-
    A sruvara can spit forth a stream of poison so corrupt it can sear skin and dissolve metal (100- foot line, once every 1d4 rounds, damage 12d8 acid, Reflex DC 26 half ). Any creature damaged by an sruvara's breath must make an additional DC 26 Fortitude save or be poisoned (initial and secondary damage 1d4 Con). This poison is so concentrated that even living creatures normally immune to poison-such as high-level druids and monks, wearers of magic items like a periapt of proof against poison, demons, or other creatures-must still save against this poison. Nonliving creatures like constructs and undead remain immune to this poison.

    Additionally, the first creature struck by a sruvara's line of poison that fails its Reflex save takes a concentrated burst of the poison, instantly causing its armor to corrode, completely destroying it. Magic armor must succeed on an additional DC 26 Reflex save to resist being dissolved.

    All save DCs are Constitution-based.
  Cursed to Corruption (Su): Sruvaras spread the taint of evil wherever they go, and
    delight in few things more than tarnishing the gleam of true innocence with their
    corruption. Once every minute, a sruvara can spit a blasphemous curse. The target
    must make a DC 24 Will save or have an angry blemish rise upon its skin in the
    form of some foul sigil. This mark is treated in all ways as a foul version of
    the spell mark of justice, cursing the target to avoid performing some benevolent
    act the sruvara deems ironic or otherwise fitting. The save DC is Charisma-based.
  Noxious Cloud (Su): The greenish tinge on the sruvara's scales is in fact a potent
    poison (inhaled, Fortitude DC 26, initial 1d6 Wis, secondary 2d6 Wis). As a standard
    action, a sruvara can violently shake its body, freeing the poison from its scales,
    causing a noxious, mind-numbing cloud to erupt around its body. This cloud extends
    10 feet from the creature and is treated as a poisonous form of obscuring mist
    that persists for 1d4 rounds. All creatures nearby the azi when it creates the
    cloud or who end their turn in the cloud are subject to its poison. Creatures
    who do not breathe are immune. The save DC is Constitution-based.
  Poison (Ex): Injury, Fortitude DC 26, initial and secondary damage 1d6 Str. The
    save DC is Constitution based.
desc_long: |-
  Though the smallest of the azi, sruvaras rival their brethren in potency. Their sleek build and stealthy manner allows them to stalk prey like the most deft jungle hunters, while their innate cunning and sadism make them blights upon whatever land they choose to despoil. While many azi are arrogant and greedy, sruvara are maniacal and cruel, reveling in the screams of long-tortured victims and the plight of parched villagers forced to choose between watering themselves or their children. One ancient legend told among desert claims the sruvara sprang from the lips of Ahriman himself as he uttered his first curse, a thing of living venom that would poison the world for all time.

  A sruvara's scales look like ridges of slate or flat gray metal. Between these scales, an organic olive-colored powder creeps like toxic verdigris. A typical adult sruvara measures 26 feet from the tip of its tapered snout to the toxic tip of its stinger, with most of this length accounted for by its long neck and tail. A sruvara stands 8 feet at the shoulder. Large yet thin, the average sruvara weighs only 2,200 pounds.

---

# Azi, Sruvara
Hissing poison drips from the many-fanged maw of this monstrous serpent. Its body like that of some gigantic venomous snake, this sinister wyrm-like beast undulates with frightening speed, and two pairs of lean wings rise from the base of a thick neck supporting a powerful, draconic visage.
**Source** Pathfinder #24: The Final _[[spells/Wish|Wish]]_ pg. 80

NE Huge dragon
**Init** +12; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Listen +13, Spot +12

##### Defense

**AC** 34, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+8 Dex, +18 natural, -2 size)
**hp** 243 (18d12+126)
**Fort** +18, **Ref** +21, **Will** +13
**DR** 10/magic; **Immune** disease, _[[universal monster rules/Paralysis|paralysis]]_ effects, poison, sleep; **Resist** acid 10, fire 10; **SR** 25

##### Offense
**Speed** 60 ft., _[[universal monster rules/Climb|climb]]_ 30 ft., fly 120 ft. (good)
**Melee** bite +24 (2d8+8 plus poison) and 2 claws +22 (2d6+4) and sting +22 (2d6+4 plus poison)
**Space** 15 ft., **Reach** 10 ft. (bite 15 ft.)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_, noxious cloud, poison
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th)
At will — _[[spells/Acid Arrow|acid arrow]]_, _[[spells/Curse Water|curse water]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 17), _[[spells/Major Image|major image]]_ (DC 18), _[[spells/Ventriloquism|ventriloquism]]_ (DC 15)
3/day — blindness/deafness (DC 17), _[[spells/Confusion|confusion]]_ (DC 19), _[[spells/Dimension Door|dimension door]]_, _[[spells/Displacement|displacement]]_ (DC 18)
1/day — _[[spells/Acid Fog|acid fog]]_, _[[spells/Gaseous Form|gaseous form]]_

##### Statistics
**Str** 27, **Dex** 26, **Con** 25, **Int** 12, **Wis** 15, **Cha** 20
**Base Atk** +18; **Grapple** +34
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_
**Skills** Appraise +12, Balance +19, Bluff +26, _Climb_ +26, Hide +21, Intimidate +18, _[[spells/Jump|Jump]]_ +30, Knowledge (arcana) +11, Listen +13, Move Silently +29, Spot +12
**Languages** Common, Draconic, Infernal

##### Ecology

**Environment** warm marshes
**Organization** solitary
**Treasure** standard
**Advancement** 19-27 HD (Huge), 28-36 HD (Gargantuan)

### Special Abilities

**_Breath Weapon_ (Su)** A sruvara can spit forth a stream of poison so corrupt it can sear skin and dissolve metal (100- foot line, once every 1d4 rounds, damage 12d8 acid, Reflex DC 26 half ). Any creature damaged by an sruvara’s breath must make an additional DC 26 Fortitude save or be poisoned (initial and secondary damage 1d4 Con). This poison is so concentrated that even living creatures normally immune to poison—such as high-level druids and monks, wearers of magic items like a _[[items/Wondrous Item/Periapt of Proof against Poison|periapt of proof against poison]]_, demons, or other creatures—must still save against this poison. Nonliving creatures like constructs and undead remain immune to this poison.

Additionally, the first creature struck by a sruvara’s line of poison that fails its Reflex save takes a concentrated burst of the poison, instantly causing its armor to corrode, completely destroying it. Magic armor must succeed on an additional DC 26 Reflex save to resist being dissolved.

All save DCs are Constitution-based.

**Cursed to Corruption (Su)** Sruvaras spread the taint of evil wherever they go, and delight in few things more than tarnishing the gleam of true _[[spells/Innocence|innocence]]_ with their corruption. Once every minute, a sruvara can spit a blasphemous curse. The target must make a DC 24 Will save or have an angry blemish rise upon its skin in the form of some foul sigil. This mark is treated in all ways as a foul version of the spell _[[spells/Mark of Justice|mark of justice]]_, cursing the target to avoid performing some _[[items/Weapon Magic Abilities/Benevolent|benevolent]]_ act the sruvara deems ironic or otherwise _[[items/Armor Magic Abilities/Fitting|fitting]]_. The save DC is Charisma-based.

**Noxious Cloud (Su)** The greenish tinge on the sruvara’s scales is in fact a _[[items/Weapon Magic Abilities/Potent|potent]]_ poison (inhaled, Fortitude DC 26, initial 1d6 Wis, secondary 2d6 Wis). As a standard action, a sruvara can violently shake its body, freeing the poison from its scales, causing a noxious, mind-numbing cloud to erupt around its body. This cloud extends 10 feet from the creature and is treated as a poisonous form of _[[spells/Obscuring Mist|obscuring mist]]_ that persists for 1d4 rounds. All creatures nearby the azi when it creates the cloud or who end their turn in the cloud are subject to its poison. Creatures who do not breathe are immune. The save DC is Constitution-based.

**Poison (Ex)** Injury, Fortitude DC 26, initial and secondary damage 1d6 Str. The save DC is Constitution based.

##### Description

Though the smallest of the azi, sruvaras _[[feats/Rival|rival]]_ their brethren in potency. Their sleek build and _[[feats/Stealthy|stealthy]]_ manner allows them to stalk prey like the most deft jungle hunters, while their innate _[[items/Weapon Magic Abilities/Cunning|cunning]]_ and sadism make them blights upon whatever land they choose to despoil. While many azi are arrogant and greedy, sruvara are maniacal and _[[items/Weapon Magic Abilities/Cruel|cruel]]_, reveling in the screams of long-tortured victims and the plight of _[[curses/Parched|parched]]_ villagers forced to choose between watering themselves or their children. One ancient legend told among desert claims the sruvara sprang from the lips of Ahriman himself as he uttered his first curse, a thing of living venom that would poison the world for all time.

A sruvara’s scales look like ridges of slate or flat _[[monsters/Gray|gray]]_ metal. Between these scales, an organic olive-colored _[[items/Mundane/Powder|powder]]_ creeps like _[[items/Weapon Magic Abilities/Toxic|toxic]]_ verdigris. A typical adult sruvara measures 26 feet from the tip of its tapered snout to the _toxic_ tip of its stinger, with most of this length accounted for by its long neck and tail. A sruvara stands 8 feet at the shoulder. Large yet thin, the average sruvara weighs only 2,200 pounds.
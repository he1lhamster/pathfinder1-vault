---
cssclass: [monsters]
title1: Bolla
desc_short: This immense serpent is covered in dull red fur; the four vestigial legs
  sprouting from its sides don't quite touch the ground.
title2: Bolla
CR: 14
sources:
- name: 'Pathfinder #136: Temple of the Peacock Spirit'
  page: 88
  link: https://paizo.com/products/btpya0b5
XP: 38400
alignment: NE
size: Huge
type: magical beast
initiative:
  bonus: 3
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 29
  touch: 11
  flat_footed: 26
  components:
    dex: 3
    natural: 18
    size: -2
HP:
  HP: 207
  long: 18d10+108
saves:
  fort: 17
  ref: 14
  will: 12
defensive_abilities:
- all-around vision
DR:
- amount: 10
  weakness: magic
resistances:
  acid: 20
  electricity: 20
weaknesses:
- blindness vulnerability
speeds:
  base: 40
  burrow: 30
attacks:
  melee:
  - - text: bite +24 (4d8+8 plus grab and lethargy curse)
      entries:
      - - damage: 4d8+8
        - effect: grab
        - effect: lethargy curse
      attack: bite
      bonus:
      - 24
    - text: tail slap +19 (2d6+4)
      entries:
      - - damage: 2d6+4
      attack: tail slap
      bonus:
      - 19
  special:
  - darting strike
  - lethargy curse
  - swallow whole (4d8+12 bludgeoning and lethargy curse, AC 19, 20 hp)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: call lightning storm
    source: default
    freq: 1/day
    DC: 19
  - name: horrid wilting
    source: default
    freq: 1/day
    DC: 22
  sources:
  - name: default
    CL: 18
    concentration: 22
ability_scores:
  STR: 27
  DEX: 16
  CON: 22
  INT: 13
  WIS: 18
  CHA: 19
BAB: 18
CMB: 28
CMB_other: +32 grapple
CMD: 41
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Following Step
- name: Greater Vital Strike
- name: Improved Vital Strike
- name: Iron Will
- name: Power Attack
- name: Step Up
- name: Step Up and Strike
- name: Vital Strike
skills:
  Perception: 29
  Stealth: 16
  Survival: 22
  _racial_mods:
    Perception:
      _: 4
languages:
- Abyssal
- Thassilonian (can't speak)
ecology:
  environment: cold or temperate mountains
  organization: solitary
  treasure_type: standard
special_abilities:
  Blindness Vulnerability (Ex): A bolla takes a -4 penalty on saving throws against
    spells and effects that would blind it.
  Darting Strike (Ex): When a bolla hits with an attack of opportunity, it can move
    up to 15 feet as an immediate action. This movement does not provoke attacks of
    opportunity.
  Lethargy Curse (Su): |-
    A creature bitten or swallowed by a bolla is affected by a curse of overwhelming lethargy.
     Bolla Lethargy: Bite-injury; save Fort DC 23; frequency 1/round; effect 3d10 nonlethal damage and fatigued; cure 2 consecutive saves. A creature that falls unconscious while subject to this curse stops taking nonlethal damage, falls asleep, and cannot be woken until the curse is removed. The victim ages normally, but does not require any nourishment. The save DC is Charisma-based.
desc_long: |-
  Resembling immense serpents or wingless dragons, bollas are remorseless gluttons that spend much of their time hibernating in remote mountain ranges. They have little concern for other creatures except as food, but particularly prize the taste of intelligent prey. Fortunately, the creatures are as lazy as they are hungry; despite their aggressive dispositions, they rarely rouse themselves from their mountain lairs to assail the smorgasbord of civilization.

   Bollas have exceptionally keen vision, thanks to their silvery compound eyes. When disturbed, they often feign sleep or sluggishness to lure intruders close before lashing out with surprising speed. Their bite inflicts a magical lethargy on foes, making targets easy meals for the gluttonous beasts.

   A typical bolla is 30 feet long and weighs 2 tons. 

---

# Bolla
This immense serpent is covered in dull red fur; the four vestigial legs sprouting from its sides don’t quite touch the ground.
**Source** Pathfinder #136: Temple of the Peacock Spirit pg. 88
**XP** 38,400

NE Huge magical beast
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +29

##### Defense

**AC** 29, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+3 Dex, +18 natural, –2 size)
**hp** 207 (18d10+108)
**Fort** +17, **Ref** +14, **Will** +12
**Defensive Abilities** _[[universal monster rules/All-Around Vision|all-around vision]]_; **DR** 10/magic; **Resist** acid 20, electricity 20
**Weaknesses** blindness _[[curses/Vulnerability|vulnerability]]_

##### Offense
**Speed** 40 ft., _[[universal monster rules/Burrow|burrow]]_ 30 ft.
**Melee** bite +24 (4d8+8 plus _[[universal monster rules/Grab|grab]]_ and _[[curses/Lethargy|lethargy]]_ curse), tail slap +19 (2d6+4)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** darting strike, _lethargy_ curse, _[[universal monster rules/Swallow Whole|swallow whole]]_ (4d8+12 bludgeoning and _lethargy_ curse, AC 19, 20 hp)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +22)
1/day—_[[spells/Call Lightning Storm|call lightning storm]]_ (DC 19), _[[spells/Horrid Wilting|horrid wilting]]_ (DC 22)

##### Statistics
**Str** 27, **Dex** 16, **Con** 22, **Int** 13, **Wis** 18, **Cha** 19
**Base Atk** +18; **CMB** +28 (+32 grapple); **CMD** 41 (can't be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Following Step|Following Step]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Step Up|Step Up]]_, _[[feats/Step Up and Strike|Step Up and Strike]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Perception +29, Stealth +16, Survival +22; **Racial Modifiers** +4 Perception
**Languages** Abyssal, Thassilonian (can’t speak)

##### Ecology

**Environment** cold or temperate mountains
**Organization** solitary
**Treasure** standard

### Special Abilities

**Blindness _Vulnerability_ (Ex)** A _[[monsters/Bolla|bolla]]_ takes a –4 penalty on saving throws against spells and effects that would blind it.

**Darting Strike (Ex)** When a _bolla_ hits with an attack of opportunity, it can move up to 15 feet as an immediate action. This movement does not provoke attacks of opportunity.

**_Lethargy_ Curse (Su)** A creature bitten or swallowed by a _bolla_ is affected by a curse of overwhelming _lethargy_.
 _Bolla_ _Lethargy_: Bite—injury; save Fort DC 23; frequency 1/round; effect 3d10 nonlethal damage and _[[conditions/Fatigued|fatigued]]_; cure 2 consecutive saves. A creature that falls _[[conditions/Unconscious|unconscious]]_ while subject to this curse stops taking nonlethal damage, falls asleep, and cannot be woken until the curse is removed. The victim ages normally, but does not require any nourishment. The save DC is Charisma-based.

##### Description

Resembling immense serpents or wingless dragons, bollas are remorseless gluttons that spend much of their time hibernating in remote mountain ranges. They have little concern for other creatures except as food, but particularly prize the taste of intelligent prey. Fortunately, the creatures are as lazy as they are hungry; despite their aggressive dispositions, they rarely rouse themselves from their mountain lairs to assail the smorgasbord of civilization.

Bollas have exceptionally _[[items/Weapon Magic Abilities/Keen|keen]]_ _[[spells/Vision|vision]]_, thanks to their silvery compound eyes. When disturbed, they often feign sleep or sluggishness to lure intruders close before lashing out with surprising speed. Their bite inflicts a magical _lethargy_ on foes, making targets easy meals for the gluttonous beasts.

A typical _bolla_ is 30 feet long and weighs 2 tons.
---
cssclass: [monsters]
title1: Pavbagha
desc_short: This majestic tiger has white fur with deep blue stripes. It glows with
  divine radiance and radiates an aura of calm.
title2: Pavbagha
CR: 4
sources:
- name: Inner Sea Gods
  page: 295
  link: http://paizo.com/products/btpy94wj?Pathfinder-Campaign-Setting-Inner-Sea-Gods-Hardcover
XP: 1200
alignment: LN
size: Large
type: outsider
subtypes:
- extraplanar
- lawful
initiative:
  bonus: 5
senses:
  darkvision: 60
  low-light vision: true
  scent: true
auras:
- name: courage
  radius: 10
AC:
  AC: 16
  touch: 10
  flat_footed: 15
  components:
    dex: 1
    natural: 6
    size: -1
HP:
  HP: 37
  long: 5d10+10
saves:
  fort: 6
  ref: 4
  will: 7
DR:
- amount: 5
  weakness: chaotic
immunities:
- fear
SR: 15
speeds:
  base: 40
attacks:
  melee:
  - - text: bite +6 (1d8+2 plus grab)
      entries:
      - - damage: 1d8+2
        - effect: grab
      attack: bite
      bonus:
      - 6
    - text: 2 claws +7 (1d6+2 plus grab)
      entries:
      - - damage: 1d6+2
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 7
  special:
  - pounce
  - rake (2 claws +7, 1d6+2)
  - stunning claw (4/day, DC 15)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: feather fall
    source: default
    freq: At will
    other: self only
  - name: guidance
    source: default
    freq: At will
  - name: light
    source: default
    freq: At will
  - name: channel vigor
    source: default
    freq: 3/day
  - name: cure light wounds
    source: default
    freq: 3/day
  - name: true strike
    source: default
    freq: 3/day
  - name: bull's strength
    source: default
    freq: 1/day
  - name: dimension door
    source: default
    freq: 1/day
    other: self plus 50 lbs. of objects only
  sources:
  - name: default
    CL: 6
    concentration: 6
ability_scores:
  STR: 15
  DEX: 13
  CON: 14
  INT: 10
  WIS: 17
  CHA: 10
BAB: 5
CMB: 8
CMB_other: +12 grapple
CMD: 19
CMD_other: 23 vs. trip
feats:
- name: Improved Initiative
- name: Lightning Reflexes
- name: Weapon Focus (claw)
skills:
  Acrobatics: 13
    when jumping: 17
  Knowledge (history): 8
  Knowledge (religion): 8
  Perception: 11
  Stealth: 9
    in tall grass: 13
  Swim: 10
  _racial_mods:
    Acrobatics:
      _: 4
      when jumping: 8
    Stealth:
      _: 4
      in tall grass: 8
languages:
- Celestial
- Common
- Draconic
special_qualities:
- fade
ecology:
  environment: any (Axis)
  organization: solitary, pair, or pride (3-5)
  treasure_type: standard
special_abilities:
  Aura of Courage (Su): A pavbagha is immune to fear, magical or otherwise. Each ally
    within 10 feet of it gains a +4 morale bonus on saving throws against fear effects.
    This ability functions only while the pavbagha is conscious, not if it's unconscious
    or dead.
  Fade (Su): As a standard action, a pavbagha can fade from sight, as invisibility,
    for up to 10 rounds per day. These rounds need not be consecutive.
  Stunning Claw (Ex): This ability functions like the Stunning Fist feat, except the
    pavbagha uses a claw attack instead of an unarmed strike. The servitor can use
    this ability five times per day. A successful DC 15 Fortitude saving throw negates
    this effect. The save DC is Wisdom-based.
desc_long: |-
  A pavbagha is the reincarnated soul of an enlightened mortal worshiper of Irori transformed into the shape of a white tiger. Having lived one full mortal lifetime (if not more), it is patient, calm, and wise. It prefers to draw on its experience to guide and instruct mortals on ways to better themselves. Many enemies mistake a pavbagha's inner peace for weakness or pacifism, but the servitor was a warrior and a fierce predator in previous lives, and it quickly leaps into battle to defend its students or confront those who would dare destroy knowledge.

  Pavbaghas patrol the borders of Irori's realm, alert for disturbances in the Serene Circle or forbidden natives of Axis who venture too close to the god's territory. Fulfilling the roles of guardians in the mortal world pleases pavbaghas, whether they're looking after a special person or watching over a sacred site. Although they don't need to eat, they enjoy the challenge and exercise of hunting and stalking prey. Rather than killing its catch, a pavbagha usually lays a single paw upon its target before allowing the creature to run away, secure in its triumph.

  Some pavbaghas serve in temples and monasteries dedicated to Irori, where they help in training students in physical combat, particularly in how to deal with monsters and other dangerous beasts. Others guide students in meditation, helping them unravel those quandaries they might have on the path to perfection. Still other pavbaghas that make their homes in monasteries on the Material Plane focus their efforts on attending to those who visit Iroran shrines and temples looking for divine assistance.

  A pavbagha measures about 10 to 12 feet long and weighs between 750 and 900 pounds.

---

# Pavbagha
This majestic _[[monsters/Tiger|tiger]]_ has white fur with deep blue stripes. It glows with divine _[[items/Weapon/Radiance|radiance]]_ and radiates an aura of calm.
**Source** Inner Sea Gods pg. 295
**XP** 1,200

LN Large outsider (extraplanar, lawful)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +11
**Aura** courage (10 ft.)

##### Defense

**AC** 16, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+1 Dex, +6 natural, –1 size)
**hp** 37 (5d10+10)
**Fort** +6, **Ref** +4, **Will** +7
**DR** 5/chaotic; **Immune** _[[universal monster rules/Fear|fear]]_; **SR** 15

##### Offense
**Speed** 40 ft.
**Melee** bite +6 (1d8+2 plus _[[universal monster rules/Grab|grab]]_), 2 claws +7 (1d6+2 plus _grab_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Pounce|pounce]]_, _[[universal monster rules/Rake|rake]]_ (2 claws +7, 1d6+2), stunning claw (4/day, DC 15)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +6)
At will—_[[spells/Feather Fall|feather fall]]_ (self only), _[[spells/Guidance|guidance]]_, light
3/day—_[[spells/Channel Vigor|channel vigor]]_, _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/True Strike|true strike]]_
1/day—bull’s strength, _[[spells/Dimension Door|dimension door]]_ (self plus 50 lbs. of objects only)

##### Statistics
**Str** 15, **Dex** 13, **Con** 14, **Int** 10, **Wis** 17, **Cha** 10
**Base Atk** +5; **CMB** +8 (+12 grapple); **CMD** 19 (23 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Acrobatics +13 (+17 when jumping), Knowledge (history, religion) +8, Perception +11, Stealth +9 (+13 in tall grass), Swim +10; **Racial Modifiers** +4 Acrobatics (+8 when jumping), +4 Stealth (+8 in tall grass)
**Languages** Celestial, Common, Draconic
**SQ** fade

##### Ecology

**Environment** any (Axis)
**Organization** solitary, pair, or pride (3–5)
**Treasure** standard

### Special Abilities

**Aura of Courage (Su)** A _[[monsters/Pavbagha|pavbagha]]_ is immune to _fear_, magical or otherwise. Each ally within 10 feet of it gains a +4 morale bonus on saving throws against _fear_ effects. This ability functions only while the _pavbagha_ is conscious, not if it’s _[[conditions/Unconscious|unconscious]]_ or dead.

**Fade (Su)** As a standard action, a _pavbagha_ can fade from sight, as _[[spells/Invisibility|invisibility]]_, for up to 10 rounds per day. These rounds need not be consecutive.
**Stunning Claw (Ex)** This ability functions like the _[[feats/Stunning Fist|Stunning Fist]]_ feat, except the _pavbagha_ uses a claw attack instead of an unarmed strike. The servitor can use this ability five times per day. A successful DC 15 Fortitude saving throw negates this effect. The save DC is Wisdom-based.

##### Description

A _pavbagha_ is the reincarnated soul of an enlightened mortal worshiper of Irori transformed into the shape of a white _tiger_. Having lived one full mortal lifetime (if not more), it is patient, calm, and wise. It prefers to draw on its experience to guide and instruct mortals on ways to better themselves. Many enemies mistake a _pavbagha_’s inner peace for weakness or pacifism, but the servitor was a warrior and a fierce predator in previous lives, and it quickly leaps into battle to defend its students or confront those who would dare destroy knowledge.

Pavbaghas patrol the borders of Irori’s realm, alert for disturbances in the Serene Circle or forbidden natives of Axis who venture too close to the god’s territory. Fulfilling the roles of guardians in the mortal world pleases pavbaghas, whether they’re looking after a special person or watching over a _[[items/Weapon Magic Abilities/Sacred|sacred]]_ site. Although they don’t need to eat, they enjoy the challenge and exercise of hunting and _[[items/Weapon Magic Abilities/Stalking|stalking]]_ prey. Rather than killing its catch, a _pavbagha_ usually lays a single paw upon its target before allowing the creature to run away, secure in its triumph.

Some pavbaghas serve in temples and monasteries dedicated to Irori, where they help in _[[items/Weapon Magic Abilities/Training|training]]_ students in physical combat, particularly in how to deal with monsters and other dangerous beasts. Others guide students in meditation, helping them unravel those quandaries they might have on the path to perfection. Still other pavbaghas that make their homes in monasteries on the Material Plane focus their efforts on attending to those who visit Iroran shrines and temples looking for divine assistance.

A _pavbagha_ measures about 10 to 12 feet long and weighs between 750 and 900 pounds.
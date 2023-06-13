---
cssclass: [monsters]
title1: Deep One, Deep One Hybrid
desc_short: This elderly man's wide-mouthed, staring countenance and webbed hands
  suggest a sinister taint in his bloodline.
title2: Deep One Hybrid
CR: 1/2
sources:
- name: Bestiary 5
  page: 70
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 200
race: Deep
classes:
- one hybrid cleric 1
alignment: CE
size: Medium
type: humanoid
subtypes:
- deep one
- human
initiative:
  bonus: 4
senses:
  low-light vision: true
AC:
  AC: 13
  touch: 10
  flat_footed: 13
  components:
    armor: 2
    natural: 1
HP:
  HP: 12
  long: 1d8+4
saves:
  fort: 5
  ref: 0
  will: 5
speeds:
  base: 20
  swim: 30
attacks:
  melee:
  - - text: mwk dagger +2 (1d4+1/19-20)
      entries:
      - - damage: 1d4+1
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 2
  special:
  - channel negative energy 2/day (DC 9, 1d6)
spell_like_abilities:
  entries:
  - name: touch of chaos
    source: default
    freq: 6/day
  - name: vision of madness
    source: default
    freq: 6/day
  sources:
  - name: default
    CL: 1
    concentration: 4
spells:
  entries:
  - name: cause fear
    source: Cleric
    level: 1
    DC: 14
  - name: cure light wounds
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: lesser confusion
    source: Cleric
    level: 1
    DC: 14
  - name: bleed
    source: Cleric
    level: 0
    DC: 13
  - name: light
    source: Cleric
    level: 0
  - name: resistance
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 1
    concentration: 4
    slots:
      0: at-will
    domains:
    - chaos
    - madness
ability_scores:
  STR: 13
  DEX: 10
  CON: 17
  INT: 10
  WIS: 16
  CHA: 8
BAB: 0
CMB: 1
CMD: 11
feats:
- name: Improved Initiative
skills:
  Knowledge (religion): 4
  Perception: 4
  Swim: 9
  _racial_mods:
    Swim:
      _: 8
languages:
- Aklo
- Common
special_qualities:
- final change
- sea longing
- take to the water
ecology:
  environment: any urban
  organization: solitary, cult (2-12), or township (13+)
  treasure_type: NPC Gear
  treasure:
  - mwk dagger
  - leather armor
  - other treasure
special_abilities:
  Final Change (Su): 'A deep one hybrid ages at the same rate as a half-orc. A mere
    1d12 months after a deep one hybrid reaches venerable age (at 60 years old), it
    dies a painful, agonizing death, only to have its body transform into that of
    a mature deep one. This transformation functions as the reincarnate spell, with
    the newly formed deep one gaining the following modifications to its physical
    ability scores: +6 Strength, -2 Dexterity, and +6 Constitution.'
  Sea Longing (Ex): Every 24 hours a deep one hybrid spends in an area more than 10
    miles from the sea, it must succeed at a DC 20 Will save or take 1 point of Wisdom
    drain.
  Take to the Water (Ex): A deep one hybrid can hold its breath 10 times longer than
    a human can, and gains a +2 bonus on Initiative checks and Reflex saving throws
    while swimming. A deep one hybrid has a swim speed of 30 feet, and gains a +8
    racial bonus on all Swim checks.
desc_long: Deep one hybrids are the spawn of humans and deep ones. They are most comfortable
  with others of their kind, and typically cluster in small, insular settlements where
  they can assume positions of authority. They keep any humans within their towns
  subservient and cowed, making sure those other residents know better than to act
  against local laws. Though deep ones are devoutly religious, they usually cloak
  their true beliefs under a facade of more conventional worship, believing that by
  doing so they can avoid suspicion from visitors and nearby societies.

---

# Deep One, Deep One Hybrid
This elderly man’s wide-mouthed, staring countenance and webbed hands suggest a sinister taint in his bloodline.
**Source** Bestiary 5 pg. 70
**XP** 200
_[[monsters/Deep One|Deep one]]_ hybrid _[[classes/Cleric|cleric]]_ 1
CE Medium humanoid (_deep one_, human)
**Init** +4; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +4

##### Defense

**AC** 13, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+2 armor, +1 natural)
**hp** 12 (1d8+4)
**Fort** +5, **Ref** +0, **Will** +5

##### Offense
**Speed** 20 ft., swim 30 ft.
**Melee** mwk _[[items/Weapon/Dagger|dagger]]_ +2 (1d4+1/19-20)
**Special Attacks** channel negative energy 2/day (DC 9, 1d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 1st; concentration +4)
6/day—touch of chaos, _[[spells/Vision|vision]]_ of madness
**_Cleric_ Spells Prepared **(CL 1st; concentration +4)
1st—_[[spells/Cause Fear|cause fear]]_ (DC 14), _[[spells/Cure Light Wounds|cure light wounds]]_, lesser _[[spells/Confusion|confusion]]_ (DC 14)
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 13), light, _[[universal monster rules/Resistance|resistance]]_
**D** domain spell; **Domains** Chaos, Madness

##### Statistics
**Str** 13, **Dex** 10, **Con** 17, **Int** 10, **Wis** 16, **Cha** 8
**Base Atk** +0; **CMB** +1; **CMD** 11
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_
**Skills** Knowledge (religion) +4, Perception +4, Swim +9; **Racial Modifiers** +8 Swim
**Languages** Aklo, Common
**SQ** final change, sea longing, take to the water

##### Ecology

**Environment** any urban
**Organization** solitary, cult (2-12), or township (13+)
**Treasure** NPC gear (mwk _dagger_, _[[items/Armor/Leather armor|leather armor]]_, other treasure)

### Special Abilities

**Final Change (Su)** A _deep one_ hybrid ages at the same rate as a half-orc. A mere 1d12 months after a _deep one_ hybrid reaches venerable age (at 60 years old), it dies a painful, agonizing death, only to have its body transform into that of a mature _deep one_. This _[[spells/Transformation|transformation]]_ functions as the _[[spells/Reincarnate|reincarnate]]_ spell, with the newly formed _deep one_ gaining the following modifications to its physical ability scores: +6 Strength, -2 Dexterity, and +6 Constitution.
**Sea Longing (Ex)** Every 24 hours a _deep one_ hybrid spends in an area more than 10 miles from the sea, it must succeed at a DC 20 Will save or take 1 point of Wisdom drain.

**Take to the Water (Ex)** A _deep one_ hybrid can hold its breath 10 times longer than a human can, and gains a +2 bonus on Initiative checks and Reflex saving throws while swimming. A _deep one_ hybrid has a swim speed of 30 feet, and gains a +8 racial bonus on all Swim checks.

##### Description

_Deep one_ hybrids are the spawn of humans and deep ones. They are most comfortable with others of their kind, and typically cluster in small, insular settlements where they can assume positions of authority. They keep any humans within their towns subservient and cowed, making sure those other residents know better than to act against local laws. Though deep ones are devoutly religious, they usually cloak their true beliefs under a facade of more conventional worship, believing that by doing so they can avoid suspicion from visitors and nearby societies.
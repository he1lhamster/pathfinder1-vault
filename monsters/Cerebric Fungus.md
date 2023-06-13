---
cssclass: [monsters]
title1: Cerebric Fungus
desc_short: A swollen, brainlike bulb encrusted with fungal shelves squats atop several
  ropy legs. A wide mouth bisects the bulb's crown.
title2: Cerebric Fungus
CR: 3
sources:
- name: Bestiary 3
  page: 52
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 800
alignment: N
size: Medium
type: plant
initiative:
  bonus: 4
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: unsettling appearance
  radius: 60
  DC: 14
AC:
  AC: 15
  touch: 10
  flat_footed: 15
  components:
    natural: 5
HP:
  HP: 30
  long: 4d8+12
  fast_healing: 2
saves:
  fort: 7
  ref: 1
  will: 6
defensive_abilities:
- otherworldly mind
immunities:
- plant traits
resistances:
  cold: 5
weaknesses:
- vulnerable to sonic
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +5 (1d6+2)
      entries:
      - - damage: 1d6+2
      attack: bite
      bonus:
      - 5
    - text: 2 tendrils +3 (1d4+1 plus pull)
      entries:
      - - damage: 1d4+1
        - effect: pull
      count: 2
      attack: tendrils
      bonus:
      - 3
  special:
  - pull (tendril, 5 ft.)
  - star-shriek
space: 5
reach: 5
reach_other: 15 ft. with tendrils
spell_like_abilities:
  entries:
  - name: detect thoughts
    source: default
    freq: Constant
    DC: 14
  - name: touch of madness
    source: default
    freq: At will
    DC: 14
  - name: calm emotions
    source: default
    freq: 3/day
    DC: 14
  - name: touch of idiocy
    source: default
    freq: 3/day
    DC: 14
  sources:
  - name: default
    CL: 4
    concentration: 6
ability_scores:
  STR: 14
  DEX: 11
  CON: 16
  INT: 15
  WIS: 20
  CHA: 15
BAB: 3
CMB: 5
CMD: 15
CMD_other: 21 vs. trip
feats:
- name: Improved Initiative
- name: Multiattack
skills:
  Bluff: 6
  Diplomacy: 6
  Perception: 12
  Stealth: 7
languages:
- telepathy 100 ft.
ecology:
  environment: any
  organization: solitary, pair, or colony (3-12)
  treasure_type: standard
special_abilities:
  Otherworldly Mind (Ex): Any creature attempting to contact a cerebric fungus's mind
    or read its thoughts with a divination spell or similar ability must succeed at
    a DC 16 Will save or be overwhelmed by the alien thoughts in the creature's head.
    Those who fail take 1d6 points of nonlethal damage and are confused for 1d6 rounds,
    and the divination effect immediately ends. The save is Charisma-based and includes
    a +2 racial bonus.
  Star-Shriek (Ex): Once per day as a full-round action, a cerebric fungus can unleash
    a shrill scream of madness. All creatures (except other cerebric fungi) within
    30 feet must make a DC 15 Will save or be nauseated for 1d4 rounds. This is a
    sonic, mind-affecting effect. The save DC is Constitution-based.
  Touch of Madness (Sp): The cerebric fungus may daze one living creature by making
    a successful touch attack. The target creature must succeed at a DC 14 Will save,
    or it becomes dazed for 1 round per caster level (4 rounds for most cerebric fungi).
    The dazed subject is not stunned (so attackers get no special advantage against
    it). This is a mind-affecting enchantment, equivalent to a 2nd-level spell.
  Unsettling Appearance (Su): A cerebric fungus constantly scans the minds of those
    around it, projecting around itself a confusing collage of images gleaned from
    their thoughts. Creatures within 60 feet that can see the fungus must succeed
    at a DC 14 Will save or take a -2 penalty on attack rolls. This is a mind-affecting
    effect. The save DC is Charisma-based.
desc_long: |-
  Cerebric fungi are a race of carnivorous, intelligent fungi native to a distant planet. Although they are one of the lowliest life forms on their homeworld, the fungi still possess an alien intellect far beyond that of most terrestrial creatures. Cerebric fungi display great curiosity about other races and species when they visit other worlds, asking endless, apparently senseless, questions and engaging in disturbing experiments. Some eccentric scholars claim to have learned unsettling secrets from these interrogations.

  Although capable of fine manipulation with their prehensile filaments, cerebric fungi normally forgo the use of weapons in favor of their natural attacks.

---

# Cerebric Fungus
A swollen, brainlike bulb encrusted with fungal shelves squats atop several ropy legs. A wide mouth bisects the bulb’s crown.
**Source** Bestiary 3 pg. 52
**XP** 800

N Medium plant
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +12
**Aura** unsettling appearance (60 ft., DC 14)

##### Defense

**AC** 15, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+5 natural)
**hp** 30 (4d8+12); _[[universal monster rules/Fast Healing|fast healing]]_ 2
**Fort** +7, **Ref** +1, **Will** +6
**Defensive Abilities** otherworldly mind; **Immune** _[[universal monster rules/Plant Traits|plant traits]]_; **Resist** cold 5
**Weaknesses** vulnerable to sonic

##### Offense
**Speed** 30 ft.
**Melee** bite +5 (1d6+2), 2 tendrils +3 (1d4+1 plus _[[universal monster rules/Pull|pull]]_)
**Space** 5 ft., **Reach** 5 ft. (15 ft. with tendrils)
**Special Attacks** _pull_ (tendril, 5 ft.), star-shriek
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +6)
Constant—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 14)
At will—touch of madness (DC 14)
3/day—_[[spells/Calm Emotions|calm emotions]]_ (DC 14), _[[spells/Touch of Idiocy|touch of idiocy]]_ (DC 14)

##### Statistics
**Str** 14, **Dex** 11, **Con** 16, **Int** 15, **Wis** 20, **Cha** 15
**Base Atk** +3; **CMB** +5; **CMD** 15 (21 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Multiattack|Multiattack]]_
**Skills** Bluff +6, Diplomacy +6, Perception +12, Stealth +7
**Languages** _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any
**Organization** solitary, pair, or colony (3–12)
**Treasure** standard

### Special Abilities

**Otherworldly Mind (Ex) **Any creature attempting to contact a _[[monsters/Cerebric Fungus|cerebric fungus]]_’s mind or read its thoughts with a _[[spells/Divination|divination]]_ spell or similar ability must succeed at a DC 16 Will save or be overwhelmed by the alien thoughts in the creature’s head. Those who fail take 1d6 points of nonlethal damage and are _[[conditions/Confused|confused]]_ for 1d6 rounds, and the _divination_ effect immediately ends. The save is Charisma-based and includes a +2 racial bonus.
**Star-Shriek (Ex)** Once per day as a full-round action, a _cerebric fungus_ can unleash a shrill scream of madness. All creatures (except other cerebric fungi) within 30 feet must make a DC 15 Will save or be _[[conditions/Nauseated|nauseated]]_ for 1d4 rounds. This is a sonic, mind-affecting effect. The save DC is Constitution-based.

**Touch of Madness (Sp)** The _cerebric fungus_ may _[[spells/Daze|daze]]_ one living creature by making a successful touch attack. The target creature must succeed at a DC 14 Will save, or it becomes _[[conditions/Dazed|dazed]]_ for 1 round per caster level (4 rounds for most cerebric fungi). The _dazed_ subject is not _[[conditions/Stunned|stunned]]_ (so attackers get no special advantage against it). This is a mind-affecting enchantment, equivalent to a 2nd-level spell.

**Unsettling Appearance (Su)** A _cerebric fungus_ constantly scans the minds of those around it, projecting around itself a confusing collage of images gleaned from their thoughts. Creatures within 60 feet that can see the fungus must succeed at a DC 14 Will save or take a –2 penalty on attack rolls. This is a mind-affecting effect. The save DC is Charisma-based.

##### Description

Cerebric fungi are a race of carnivorous, intelligent fungi native to a distant planet. Although they are one of the lowliest life forms on their homeworld, the fungi still possess an alien intellect far beyond that of most terrestrial creatures. Cerebric fungi display great curiosity about other races and species when they visit other worlds, asking endless, apparently senseless, questions and engaging in disturbing experiments. Some eccentric scholars claim to have learned unsettling secrets from these interrogations.

Although capable of fine manipulation with their _[[items/Weapon Magic Abilities/Prehensile|prehensile]]_ filaments, cerebric fungi normally forgo the use of weapons in favor of their _[[universal monster rules/Natural Attacks|natural attacks]]_.
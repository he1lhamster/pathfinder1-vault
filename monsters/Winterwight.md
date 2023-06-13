---
cssclass: [monsters]
title1: Winterwight
desc_short: Human-sized and of a deathly blue color, this long-taloned skeletal creature
  is partially encased in jagged sheets of ice.
title2: Winterwight
CR: 17
sources:
- name: Bestiary 2
  page: 283
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 102400
alignment: CE
size: Medium
type: undead
subtypes:
- cold
initiative:
  bonus: 10
senses:
  darkvision: 60
auras:
- name: cold
  radius: 10
AC:
  AC: 32
  touch: 16
  flat_footed: 26
  components:
    dex: 6
    natural: 16
HP:
  HP: 270
  long: 20d8+180
  fast_healing: 10
saves:
  fort: 15
  ref: 14
  will: 16
defensive_abilities:
- channel resistance +4
DR:
- amount: 15
  weakness: bludgeoning and good
immunities:
- cold
- undead traits
SR: 28
weaknesses:
- vulnerability to fire
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +30 (2d8+15 plus blightfire)
      entries:
      - - damage: 2d8+15
        - effect: blightfire
      attack: bite
      bonus:
      - 30
    - text: 2 claws +30 (2d6+15 plus blightfire)
      entries:
      - - damage: 2d6+15
        - effect: blightfire
      count: 2
      attack: claws
      bonus:
      - 30
  special:
  - rend (2 claws 2d8+22)
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: cone of cold
    source: default
    freq: At will
    DC: 24
  - name: dimension door
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: sleet storm
    source: default
    freq: At will
  - name: wall of ice
    source: default
    freq: At will
  - name: polar ray
    source: default
    freq: 3/day
  - name: control weather
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 17
    concentration: 26
ability_scores:
  STR: 40
  DEX: 23
  CON:
  INT: 11
  WIS: 18
  CHA: 29
BAB: 15
CMB: 30
CMD: 46
feats:
- name: Blind-Fight
- name: Combat Reflexes
- name: Critical Focus
- name: Greater Vital Strike
- name: Improved Initiative
- name: Improved Vital Strike
- name: Lightning Reflexes
- name: Power Attack
- name: Staggering Critical
- name: Vital Strike
skills:
  Acrobatics: 26
  Intimidate: 32
  Perception: 27
  Stealth: 29
languages:
- Common
ecology:
  environment: any cold land
  organization: solitary, pair, or incursion (3-6)
  treasure_type: standard
special_abilities:
  Aura of Cold (Su): Winterwights are surrounded by a 10-foot radius of deathly chill.
    Any creatures within this area during the winterwight's turn takes 2d10 points
    of cold damage. All creatures of the cold subtype within this area (including
    the winterwight) are treated as having fast healing 10.
  Blightfire (Su): Whenever a winterwight damages a creature with a bite or claw,
    the wound erupts with tongues of black fire. For the next 5 rounds, the victim
    must make a DC 29 Fortitude saving throw at the start of its turn or take 1d6
    points of Constitution drain. The winterwight gains 10 temporary hit points each
    time the creature fails a saving throw against blightfire. A creature cannot be
    affected by more than one instance of blightfire at a time. The save DC is Charisma-based.
desc_long: |-
  The winterwight is an undead horror born from the coldest depths of the negative energy plane. Infused with the dark, cold magic that permeates this realm of death, the winterwight takes the form of a skeleton coated in armor of jagged ice.

  Though it resembles an ordinary skeleton from a distance, the winterwight's frame is much sturdier than the average humanoid's, its frozen armor intertwining with its bone structure to form an incredibly hardy chassis. Sometimes called hatewraiths because of their insatiable lust for suffering, these frozen horrors are often found in areas that suffer from magical cold or frozen climates.

  Winterwights are 7 feet tall and weigh 250 pounds.

---

# Winterwight
Human-sized and of a deathly blue color, this long-taloned skeletal creature is partially encased in jagged sheets of ice.
**Source** Bestiary 2 pg. 283
**XP** 102,400
CE Medium undead (cold)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +27
**Aura** cold (10 ft.)

##### Defense

**AC** 32, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+6 Dex, +16 natural)
**hp** 270 (20d8+180); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +15, **Ref** +14, **Will** +16
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4; **DR** 15/bludgeoning and good; **Immune** cold, _[[universal monster rules/Undead Traits|undead traits]]_; **SR** 28
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to fire

##### Offense
**Speed** 30 ft.
**Melee** bite +30 (2d8+15 plus blightfire), 2 claws +30 (2d6+15 plus blightfire)
**Special Attacks** _[[universal monster rules/Rend|rend]]_ (2 claws 2d8+22)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +26)
Constant—_[[spells/Air Walk|air walk]]_
At will—_[[spells/Cone of Cold|cone of cold]]_ (DC 24), _[[spells/Dimension Door|dimension door]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Sleet Storm|sleet storm]]_, _[[spells/Wall Of Ice|wall of ice]]_
3/day—_[[spells/Polar Ray|polar ray]]_
1/day—_[[spells/Control Weather|control weather]]_

##### Statistics
**Str** 40, **Dex** 23, **Con** —, **Int** 11, **Wis** 18, **Cha** 29
**Base Atk** +15; **CMB** +30; **CMD** 46
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +26, Intimidate +32, Perception +27, Stealth +29
**Languages** Common

##### Ecology

**Environment** any cold land
**Organization** solitary, pair, or incursion (3–6)
**Treasure** standard

### Special Abilities

**Aura of Cold (Su)** Winterwights are surrounded by a 10-foot radius of deathly chill. Any creatures within this area during the _[[monsters/Winterwight|winterwight]]_’s turn takes 2d10 points of cold damage. All creatures of the cold subtype within this area (including the _winterwight_) are treated as having _fast healing_ 10.

**Blightfire (Su)** Whenever a _winterwight_ damages a creature with a bite or claw, the wound erupts with _[[spells/Tongues|tongues]]_ of black fire. For the next 5 rounds, the victim must make a DC 29 Fortitude saving throw at the start of its turn or take 1d6 points of Constitution drain. The _winterwight_ gains 10 temporary hit points each time the creature fails a saving throw against blightfire. A creature cannot be affected by more than one instance of blightfire at a time. The save DC is Charisma-based.

##### Description

The _winterwight_ is an undead horror born from the coldest depths of the negative energy plane. Infused with the dark, cold magic that permeates this realm of death, the _winterwight_ takes the form of a skeleton coated in armor of jagged ice.

Though it resembles an ordinary skeleton from a distance, the _winterwight_’s frame is much sturdier than the average humanoid’s, its frozen armor intertwining with its bone structure to form an incredibly hardy chassis. Sometimes _[[items/Weapon Magic Abilities/Called|called]]_ hatewraiths because of their insatiable lust for suffering, these frozen horrors are often found in areas that suffer from magical cold or frozen climates.

Winterwights are 7 feet tall and weigh 250 pounds.
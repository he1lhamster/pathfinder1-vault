---
cssclass: [monsters]
title1: Guardian Doll
desc_short: This strange doll is clad in traditional Irriseni peasant clothing, and
  its eyes glisten with a disturbing curiosity.
title2: Guardian Doll
CR: 3
sources:
- name: Irrisen - Land of Eternal Winter
  page: 58
  link: http://paizo.com/products/btpy8w7f?Pathfinder-Campaign-Setting-Irrisen-Land-of-Eternal-Winter
XP: 800
alignment: NE
size: Tiny
type: construct
subtypes:
- cold
initiative:
  bonus: 7
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 16
  touch: 15
  flat_footed: 13
  components:
    dex: 3
    natural: 1
    size: 2
HP:
  HP: 22
  long: 4d10
saves:
  fort: 1
  ref: 4
  will: 2
DR:
- amount: 5
  weakness: magic
immunities:
- cold
- construct traits
SR: 14
weaknesses:
- susceptible to mind-affecting effects
- vulnerable to fire
speeds:
  base: 30
attacks:
  melee:
  - - text: doll's dagger +10 (1d2-1/19-20 plus 1d6 cold and paralysis)
      entries:
      - - damage: 1d2-1
          crit_range: 19-20
        - damage: 1d6
          type: cold
        - effect: paralysis
      attack: doll's dagger
      bonus:
      - 10
spell_like_abilities:
  entries:
  - name: ray of frost
    source: default
    freq: At will
  - name: alarm
    source: default
    freq: 3/day
  - name: charm person
    source: default
    freq: 3/day
    DC: 11
  - name: light
    source: default
    freq: 3/day
  - name: mage hand
    source: default
    freq: 3/day
  - name: open/close
    source: default
    freq: 3/day
  - name: prestidigitation
    source: default
    freq: 3/day
  - superscripts:
    - UC
    name: frost fall
    source: default
    freq: 1/day
    DC: 12
  - name: levitate
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 4
    concentration: 4
ability_scores:
  STR: 8
  DEX: 17
  CON:
  INT: 13
  WIS: 12
  CHA: 10
BAB: 4
CMB: 5
CMD: 11
feats:
- name: Improved Initiative
- name: Weapon Finesse
skills:
  Escape Artist: 5
  Linguistics: 3
  Perception: 5
  Stealth: 15
languages:
- Common
- Hallit
- Skald
special_qualities:
- soul focus
ecology:
  environment: any cold
  organization: solitary, pair, or coven (3-8)
  treasure_type: standard
special_abilities:
  Doll's Dagger (Su): The dagger wielded by a guardian doll is treated as a masterwork
    weapon and delivers 1d6 points of cold damage in addition to its normal damage.
    Those struck by the dagger must succeed at a DC 12 Fortitude save or be paralyzed
    by the supernatural cold of the weapon for 1d4 rounds. If the guardian doll is
    destroyed, its weapon becomes a useless child's toy. The save DC is Charisma-based.
  Soul Focus (Su): The soul bound to the doll lives within a focus integrated into
    the doll or its apparel, typically one of the doll's eyes or a gem embedded into
    its neck or chest. As long as this soul focus remains intact, it can be used to
    animate another doll, using the same cost as creating a new construct. Once bound
    into the soul focus, the soul continues to learn. If it is put into a new doll
    body, the soul retains its personality and memories from its previous bodies.
    A soul focus has hardness 8, 12 hit points, and a break DC of 20.
  Susceptible to Mind-Affecting Effects (Ex): Like a soulbound doll, a guardian doll
    is susceptible to mind-affecting effects. However, due to the singular purpose
    with which it is imbued, its saves against such effects are made with a +1 racial
    bonus.
desc_long: Guardian dolls are constructs created by the White Witches to serve as
  spies and sentries at places that require evervigilant wardens-especially the wintry
  nation's borders. Similar to soulbound dolls (Pathfinder RPG Bestiary 2 255), these
  strange automatons are infused with fragments of the souls of living beings slain
  during the dolls' creation. The doll is sentient, and though a small part of the
  soul's original personality remains, the witchery employed largely strips it of
  its individuality. Many guardian dolls sit inside another form of construct-a sentinel
  hut- and stand vigil at one of Irrisen's borders and monitoring those who would
  enter. Others are sent on scouting missions or to spy on targets, usually posing
  as inanimate dolls to hide their true nature.

---

# Guardian Doll
This strange doll is clad in traditional Irriseni peasant clothing, and its eyes glisten with a disturbing curiosity.
**Source** Irrisen - Land of Eternal Winter pg. 58
**XP** 800

NE Tiny construct (cold)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +5

##### Defense

**AC** 16, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+3 Dex, +1 natural, +2 size)
**hp** 22 (4d10)
**Fort** +1, **Ref** +4, **Will** +2
**DR** 5/magic; **Immune** cold, _[[universal monster rules/Construct Traits|construct traits]]_; **SR** 14
**Weaknesses** susceptible to mind-affecting effects, vulnerable to fire

##### Offense
**Speed** 30 ft.
**Melee** doll’s _[[items/Weapon/Dagger|dagger]]_ +10 (1d2–1/19–20 plus 1d6 cold and _[[universal monster rules/Paralysis|paralysis]]_)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +4)
At will—_[[spells/Ray of Frost|ray of frost]]_
3/day—_[[spells/Alarm|alarm]]_, _[[spells/Charm Person|charm person]]_ (DC 11), light, _[[spells/Mage Hand|mage hand]]_, open/close, _[[spells/Prestidigitation|prestidigitation]]_
1/day—_[[spells/Frost Fall|frost fall]]_ (DC 12), _[[spells/Levitate|levitate]]_

##### Statistics
**Str** 8, **Dex** 17, **Con** —, **Int** 13, **Wis** 12, **Cha** 10
**Base Atk** +4; **CMB** +5; **CMD** 11
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Escape Artist +5, Linguistics +3, Perception +5, Stealth +15
**Languages** Common, Hallit, _[[classes/Skald|Skald]]_
**SQ** soul focus

##### Ecology

**Environment** any cold
**Organization** solitary, pair, or coven (3–8)
**Treasure** standard

### Special Abilities

**Doll’s _Dagger_ (Su)** The _dagger_ wielded by a _[[monsters/Guardian Doll|guardian doll]]_ is treated as a masterwork weapon and delivers 1d6 points of cold damage in addition to its normal damage. Those struck by the _dagger_ must succeed at a DC 12 Fortitude save or be _[[conditions/Paralyzed|paralyzed]]_ by the supernatural cold of the weapon for 1d4 rounds. If the _guardian doll_ is destroyed, its weapon becomes a useless child’s toy. The save DC is Charisma-based.
**Soul Focus (Su) **The soul bound to the doll lives within a focus integrated into the doll or its apparel, typically one of the doll’s eyes or a gem embedded into its neck or chest. As long as this soul focus remains intact, it can be used to animate another doll, using the same cost as creating a new construct. Once bound into the soul focus, the soul continues to learn. If it is put into a new doll body, the soul retains its personality and memories from its previous bodies. A soul focus has hardness 8, 12 hit points, and a break DC of 20.
**Susceptible to Mind-Affecting Effects (Ex)** Like a _[[monsters/Soulbound Doll|soulbound doll]]_, a _guardian doll_ is susceptible to mind-affecting effects. However, due to the singular purpose with which it is imbued, its saves against such effects are made with a +1 racial bonus.

##### Description

_[[items/Weapon Magic Abilities/Guardian|Guardian]]_ dolls are constructs created by the White Witches to serve as spies and sentries at places that require evervigilant wardens—especially the wintry nation’s borders. Similar to soulbound dolls (Pathfinder RPG Bestiary 2 255), these strange automatons are infused with fragments of the souls of living beings slain during the dolls’ creation. The doll is sentient, and though a small part of the soul’s original personality remains, the witchery employed largely strips it of its individuality. Many _guardian_ dolls sit inside another form of construct—a _[[monsters/Sentinel Hut|sentinel hut]]_— and stand vigil at one of Irrisen’s borders and monitoring those who would enter. Others are sent on scouting missions or to spy on targets, usually posing as inanimate dolls to hide their true nature.
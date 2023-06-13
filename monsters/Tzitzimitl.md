---
cssclass: [monsters]
title1: Tzitzimitl
desc_short: Crusted with rock, this immense skeletal figure flies swiftly through
  the air, strange gasses clinging to its nightmarish form.
title2: Tzitzimitl
CR: 19
sources:
- name: Bestiary 3
  page: 276
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 204800
alignment: NE
size: Gargantuan
type: undead
initiative:
  bonus: 9
senses:
  arcane sight: true
  darkvision: 60
  true seeing: true
AC:
  AC: 35
  touch: 11
  flat_footed: 30
  components:
    dex: 5
    natural: 24
    size: -4
HP:
  HP: 319
  long: 22d8+220
  fast_healing: 15
saves:
  fort: 17
  ref: 14
  will: 19
defensive_abilities:
- channel resistance +4
- light to dark
DR:
- amount: 15
  weakness: bludgeoning and good
immunities:
- cold
- electricity
- undead traits
resistances:
  fire: 15
SR: 30
speeds:
  base: 50
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +26 (2d8+14 plus 3d6 electricity and energy drain)
      entries:
      - - damage: 2d8+14
        - damage: 3d6
          type: electricity
        - effect: energy drain
      attack: bite
      bonus:
      - 26
    - text: 2 claws +27 (2d6+14/19-20 plus 3d6 electricity)
      entries:
      - - damage: 2d6+14
          crit_range: 19-20
        - damage: 3d6
          type: electricity
      count: 2
      attack: claws
      bonus:
      - 27
  ranged:
  - - text: eye beam +17 touch (10d6 electricity and 10d6 force)
      entries:
      - - damage: 10d6
          type: electricity
        - damage: 10d6
          type: force
      attack: eye beam
      bonus:
      - 17
      touch: true
  special:
  - eclipse
  - energy drain (2 levels, DC 31)
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: arcane sight
    source: default
    freq: Constant
  - name: fly
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: bestow curse
    source: default
    freq: At will
    DC: 24
  - name: deeper darkness
    source: default
    freq: At will
  - name: animate dead
    source: default
    freq: 3/day
  - name: contagion
    source: default
    freq: 3/day
    DC: 24
  - name: greater teleport
    source: default
    freq: 3/day
  - name: haste
    source: default
    freq: 3/day
  - name: create undead
    source: default
    freq: 1/day
  - name: temporal stasis
    source: default
    freq: 1/day
    DC: 28
  - name: wail of the banshee
    source: default
    freq: 1/day
    DC: 29
  sources:
  - name: default
    CL: 19
    concentration: 29
ability_scores:
  STR: 39
  DEX: 21
  CON:
  INT: 20
  WIS: 23
  CHA: 30
BAB: 16
CMB: 29
CMD: 44
feats:
- name: Awesome Blow
- name: Combat Reflexes
- name: Improved Bull Rush
- name: Improved Critical (claw)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Point-Blank Shot
- name: Power Attack
- name: Precise Shot
- name: Vital Strike
- name: Weapon Focus (claw)
skills:
  Fly: 35
  Knowledge (arcana): 28
  Knowledge (nature): 27
  Knowledge (planes): 25
  Knowledge (religion): 30
  Perception: 31
  Sense Motive: 31
  Spellcraft: 23
  Survival: 21
  Use Magic Device: 30
languages:
- Abyssal
- Aklo
- Celestial
- Common
ecology:
  environment: any
  organization: solitary
  treasure_type: standard
special_abilities:
  Eclipse (Su): Anytime a tzitzimitl casts deeper darkness, any creatures in the area
    of darkness when it is created take 8d6 points of cold damage (DC 31 Fortitude
    for half). Any creature that takes damage from this effect becomes staggered as
    long as it remains in the area of darkness and for 1d4 rounds after it leaves
    that area. The save DC is Charisma-based.
  Eye Beam (Su): As a standard action, a tzitzimitl can fire a glowing beam of force
    from its eyes at a range of 100 feet as a ranged touch attack dealing 10d6 points
    of force damage and 10d6 points of electricity damage.
  Light to Dark (Su): As an immediate action up to three times per day, a tzitzimitl
    can convert a positive energy effect that affects it into negative energy. Doing
    so transforms the entire effect, such that it affects other creatures as well.
    A tzitzimitl can transform channeled positive energy in this way even if the positive
    energy would not otherwise harm it.
desc_long: |-
  Enigmatic creatures of darkness, some cultures claim tzitzimitls attack and consume entire suns to “shut down worlds” in preparation for the end of days. Sages say that these creatures come from the cold, dark places between the stars, and that in the darkness of any eclipse, one can see their immense, world-darkening shadows.

  Some claim ancient and forgotten deities of death and destruction created the first tzitzimitls as instruments of apocalypse, while others speculate they come from faraway worlds where immense planets teem with creatures of this scale, and that the immortal dead of these dark globes are banished to other worlds to spread devastation.

  Tzitzimitls as a whole offer neither affirmation nor denial for these claims, and in fact seem to glory in such legends. Certainly, the arrival of a tzitzimitl upon a world heralds the advent of a time of great trouble, although whether or not the tzitzimitl actually presages such dark times or is the cause of them is a matter of debate. On some planets, tzitzimitls have already arrived, yet they lie dormant in ancient tombs, imprisoned ages ago by heroes who are long forgotten today.

  A tzitzimitl is 50 feet tall.

---

# Tzitzimitl
Crusted with rock, this immense skeletal figure flies swiftly through the air, strange gasses clinging to its nightmarish form.
**Source** Bestiary 3 pg. 276
**XP** 204,800

NE Gargantuan undead
**Init** +9; **Senses** _[[spells/Arcane Sight|arcane sight]]_, _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +31

##### Defense

**AC** 35, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+5 Dex, +24 natural, –4 size)
**hp** 319 (22d8+220); _[[universal monster rules/Fast Healing|fast healing]]_ 15
**Fort** +17, **Ref** +14, **Will** +19
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4, light to dark; **DR** 15/bludgeoning and good; **Immune** cold, electricity, _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** fire 15; **SR** 30

##### Offense
**Speed** 50 ft., fly 60 ft. (good)
**Melee** bite +26 (2d8+14 plus 3d6 electricity and _[[universal monster rules/Energy Drain|energy drain]]_), 2 claws +27 (2d6+14/19–20 plus 3d6 electricity)
**Ranged** eye beam +17 touch (10d6 electricity and 10d6 force)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** eclipse, _energy drain_ (2 levels, DC 31)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 19th; concentration +29)
Constant—_arcane sight_, fly, _true seeing_
At will—_[[spells/Bestow Curse|bestow curse]]_ (DC 24), _[[spells/Deeper Darkness|deeper darkness]]_
3/day—_[[spells/Animate Dead|animate dead]]_, _[[spells/Contagion|contagion]]_ (DC 24), greater teleport, _[[spells/Haste|haste]]_
1/day—_[[spells/Create Undead|create undead]]_, _[[spells/Temporal Stasis|temporal stasis]]_ (DC 28), _[[spells/Wail of the Banshee|wail of the banshee]]_ (DC 29)

##### Statistics
**Str** 39, **Dex** 21, **Con** —, **Int** 20, **Wis** 23, **Cha** 30
**Base Atk** +16; **CMB** +29; **CMD** 44
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Fly +35, Knowledge (arcana) +28, Knowledge (nature) +27, Knowledge (planes) +25, Knowledge (religion) +30, Perception +31, Sense Motive +31, Spellcraft +23, Survival +21, Use Magic Device +30
**Languages** Abyssal, Aklo, Celestial, Common

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** standard

### Special Abilities

**Eclipse (Su) **Anytime a _[[monsters/Tzitzimitl|tzitzimitl]]_ casts _deeper darkness_, any creatures in the area of _[[spells/Darkness|darkness]]_ when it is created take 8d6 points of cold damage (DC 31 Fortitude for half). Any creature that takes damage from this effect becomes _[[conditions/Staggered|staggered]]_ as long as it remains in the area of _darkness_ and for 1d4 rounds after it leaves that area. The save DC is Charisma-based.

**Eye Beam (Su)** As a standard action, a _tzitzimitl_ can fire a glowing beam of force from its eyes at a range of 100 feet as a ranged touch attack dealing 10d6 points of force damage and 10d6 points of electricity damage.

**Light to Dark (Su)** As an immediate action up to three times per day, a _tzitzimitl_ can convert a positive energy effect that affects it into negative energy. Doing so transforms the entire effect, such that it affects other creatures as well. A _tzitzimitl_ can transform channeled positive energy in this way even if the positive energy would not otherwise _[[spells/Harm|harm]]_ it.

##### Description

Enigmatic creatures of _darkness_, some cultures claim tzitzimitls attack and consume entire suns to “shut down worlds” in preparation for the end of days. Sages say that these creatures come from the cold, dark places between the stars, and that in the _darkness_ of any eclipse, one can see their immense, world-darkening shadows.

Some claim ancient and forgotten deities of death and _[[spells/Destruction|destruction]]_ created the first tzitzimitls as instruments of apocalypse, while others speculate they come from faraway worlds where immense planets teem with creatures of this scale, and that the immortal dead of these dark globes are banished to other worlds to spread devastation.

Tzitzimitls as a whole offer neither affirmation nor denial for these claims, and in fact seem to glory in such legends. Certainly, the arrival of a _tzitzimitl_ upon a world heralds the advent of a time of great trouble, although whether or not the _tzitzimitl_ actually presages such dark times or is the cause of them is a matter of debate. On some planets, tzitzimitls have already arrived, yet they lie dormant in ancient tombs, imprisoned ages ago by heroes who are long forgotten today.

A _tzitzimitl_ is 50 feet tall.
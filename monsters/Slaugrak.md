---
cssclass: [monsters]
title1: Slaugrak
desc_short: This hulking reptilian humanoid's torso bristles with twitching vestigial
  limbs, milk-white eyes, and drooling half-formed mouths. The creature's oversized
  maw is filled with curved teeth reminiscent of sickle blades.
title2: Slaugrak
CR: 6
sources:
- name: Monster Codex
  page: 220
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 2400
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- evil
- extraplanar
- native
initiative:
  bonus: 1
senses:
  darkvision: 120
  see in darkness: true
auras:
- name: stench
  radius: 30
  DC: 17
  duration: 10 rounds
AC:
  AC: 19
  touch: 10
  flat_footed: 18
  components:
    dex: 1
    natural: 9
    size: -1
HP:
  HP: 68
  long: 8d10+24
saves:
  fort: 9
  ref: 7
  will: 5
DR:
- amount: 10
  weakness: cold iron or good
immunities:
- acid
- poison
resistances:
  cold: 10
  electricity: 10
  fire: 10
weaknesses:
- sunlight powerlessness
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +13 (1d10+5/19-20 plus 1d6 acid and corrupting bite)
      entries:
      - - damage: 1d10+5
          crit_range: 19-20
        - damage: 1d6
          type: acid
        - effect: corrupting bite
      attack: bite
      bonus:
      - 13
    - text: 2 claws +12 (1d6+5)
      entries:
      - - damage: 1d6+5
      count: 2
      attack: claws
      bonus:
      - 12
  special:
  - corrupting bite
  - vicious jaws
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: deeper darkness
    source: default
    freq: 1/day
  - name: slow
    source: default
    freq: 1/day
    DC: 15
  - name: unholy blight
    source: default
    freq: 1/day
    DC: 16
  sources:
  - name: default
    CL: 8
    concentration: 10
ability_scores:
  STR: 20
  DEX: 12
  CON: 17
  INT: 5
  WIS: 13
  CHA: 14
BAB: 8
CMB: 14
CMD: 25
feats:
- name: Diehard
- name: Endurance
- name: Iron Will
- name: Weapon Focus (bite)
skills:
  Climb: 12
  Intimidate: 13
  Stealth: 8
    in rocky areas: 12
  Swim: 12
  Perception: 1
  _racial_mods:
    Stealth:
      in rocky areas: 4
languages:
- Abyssal
ecology:
  environment: any underground
  organization: solitary
  treasure_type: incidental
special_abilities:
  Corrupting Bite (Su): A slaugrak's caustic saliva is infused with the corrupting
    power of the Abyss. Any living creature that takes acid damage from a slaugrak's
    bite must succeed at a DC 17 Fortitude save or take 2 points of Constitution bleed
    damage as its blood boils and its internal organs liquefy. Creatures without a
    discernible anatomy (blood and internal organs) are immune to the Constitution
    bleed. The save DC is Constitution-based.
  Vicious Jaws (Ex): A slaugrak's bite attack threatens a critical hit on a roll of
    19-20.
desc_long: |-
  The taint of demonkind has long corrupted the troglodyte bloodline. Each generation a few mutant creatures marked with the taint of the Abyss are born, and fiendish deformities and stillbirths reeking of brimstone are all too common. The rapacious slaugrak is one of these fiendish mutants.

  A slaugrak is born with an unnatural and incessant hunger for living flesh. Young slaugraks grow at an unnatural rate, reaching full and awful maturity in just 2 weeks. From birth, a slaugrak is little more than a walking collection of fangs and claws with no thought other than to slay and eat. Slaugraks are sterile and solitary, holding no special love for troglodytes. A well-fed captive slaugrak might form an affectionate bond with its troglodyte keeper, but this affection merely makes the slaugrak more likely to eat its keeper last.

  A typical slaugrak stands 12 to 14 feet tall and weighs 6,000 pounds.

---

# Slaugrak
This hulking reptilian humanoid’s torso bristles with twitching vestigial limbs, milk-white eyes, and drooling half-formed mouths. The creature’s oversized maw is filled with curved teeth reminiscent of _[[items/Weapon/Sickle|sickle]]_ blades.
**Source** Monster Codex pg. 220
**XP** 2,400
CE Large outsider (chaotic, evil, extraplanar, native)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +1
**Aura** _[[universal monster rules/Stench|stench]]_ (30 ft., DC 17, 10 rounds)

##### Defense

**AC** 19, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+1 Dex, +9 natural, –1 size)
**hp** 68 (8d10+24)
**Fort** +9, **Ref** +7, **Will** +5
**DR** 10/cold iron or good; **Immune** acid, poison; **Resist** cold 10, electricity 10, fire 10
**Weaknesses** _[[universal monster rules/Sunlight Powerlessness|sunlight powerlessness]]_

##### Offense
**Speed** 30 ft.
**Melee** bite +13 (1d10+5/19–20 plus 1d6 acid and corrupting bite), 2 claws +12 (1d6+5)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** corrupting bite, _[[items/Weapon Magic Abilities/Vicious|vicious]]_ jaws
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +10)
1/day—_[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Slow|slow]]_ (DC 15), _[[spells/Unholy Blight|unholy blight]]_ (DC 16)

##### Statistics
**Str** 20, **Dex** 12, **Con** 17, **Int** 5, **Wis** 13, **Cha** 14
**Base Atk** +8; **CMB** +14; **CMD** 25
**Feats** _[[feats/Diehard|Diehard]]_, _[[feats/Endurance|Endurance]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** _[[universal monster rules/Climb|Climb]]_ +12, Intimidate +13, Stealth +8 (+12 in rocky areas), Swim +12; **Racial Modifiers** +4 Stealth in rocky areas
**Languages** Abyssal

##### Ecology

**Environment** any underground
**Organization** solitary
**Treasure** incidental

### Special Abilities

**Corrupting Bite (Su)** A _[[monsters/Slaugrak|slaugrak]]_’s caustic saliva is infused with the corrupting power of the Abyss. Any living creature that takes acid damage from a _slaugrak_’s bite must succeed at a DC 17 Fortitude save or take 2 points of Constitution _[[universal monster rules/Bleed|bleed]]_ damage as its blood boils and its internal organs _[[spells/Liquefy|liquefy]]_. Creatures without a discernible anatomy (blood and internal organs) are immune to the Constitution _bleed_. The save DC is Constitution-based.

**_Vicious_ Jaws (Ex)** A _slaugrak_’s bite attack threatens a critical hit on a roll of 19–20.

##### Description

The taint of demonkind has long corrupted the _[[monsters/Troglodyte|troglodyte]]_ bloodline. Each generation a few mutant creatures marked with the taint of the Abyss are born, and fiendish deformities and stillbirths reeking of brimstone are all too common. The rapacious _slaugrak_ is one of these fiendish mutants.

A _slaugrak_ is born with an unnatural and incessant hunger for living flesh. Young slaugraks grow at an unnatural rate, reaching full and awful maturity in just 2 weeks. From birth, a _slaugrak_ is little more than a walking collection of fangs and claws with no thought other than to slay and eat. Slaugraks are sterile and solitary, holding no special love for troglodytes. A well-fed captive _slaugrak_ might form an affectionate bond with its _troglodyte_ keeper, but this affection merely makes the _slaugrak_ more likely to eat its keeper last.

A typical _slaugrak_ stands 12 to 14 feet tall and weighs 6,000 pounds.
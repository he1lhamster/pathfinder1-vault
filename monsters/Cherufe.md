---
cssclass: [monsters]
title1: Cherufe
desc_short: This towering reptilian humanoid seems to be made of obsidian scales over
  a molten magma core.
title2: Cherufe
CR: 13
sources:
- name: Bestiary 5
  page: 55
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 25600
alignment: NE
size: Huge
type: magical beast
subtypes:
- fire
initiative:
  bonus: 5
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 24
  touch: 9
  flat_footed: 23
  components:
    dex: 1
    natural: 15
    size: -2
HP:
  HP: 189
  long: 18d10+90
saves:
  fort: 16
  ref: 14
  will: 10
defensive_abilities:
- fire healing
DR:
- amount: 10
  weakness: '-'
immunities:
- fire
weaknesses:
- vulnerable to cold
speeds:
  base: 50
  swim: 30
attacks:
  melee:
  - - text: 2 claws +25 (2d6+8 plus burn)
      entries:
      - - damage: 2d6+8
        - effect: burn
      count: 2
      attack: claws
      bonus:
      - 25
    - text: bite +25 (2d8+8 plus burn)
      entries:
      - - damage: 2d8+8
        - effect: burn
      attack: bite
      bonus:
      - 25
  ranged:
  - - text: rock +19 (2d8+10 plus burn)
      entries:
      - - damage: 2d8+10
        - effect: burn
      attack: rock
      bonus:
      - 19
  special:
  - burn (2d6 fire, DC 24)
  - heat
  - rock throwing (120 ft.)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: earthquake
    source: default
    freq: 1/month
  sources:
  - name: default
    CL: 18
    concentration: 18
ability_scores:
  STR: 26
  DEX: 13
  CON: 20
  INT: 11
  WIS: 14
  CHA: 11
BAB: 18
CMB: 28
CMD: 39
feats:
- name: Diehard
- name: Endurance
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
- name: Weapon Focus (bite)
- name: Weapon Focus (claw)
- name: Weapon Focus (rock)
skills:
  Climb: 23
  Perception: 17
  Swim: 30
languages:
- Common
ecology:
  environment: any mountains
  organization: solitary
  treasure_type: standard
special_abilities:
  Fire Healing (Ex): Any source that normally deals fire damage to a cherufe instead
    heals 1 point of damage for every 3 points of damage the attack would otherwise
    deal. If the amount of healing would cause the cherufe to exceed its full normal
    hit points, it gains any excess as temporary hit points. These temporary hit points
    don't stack.
  Heat (Su): Cherufes transfer their heat to any weapons, including their rock throwing,
    causing burn.
desc_long: |-
  Cherufes make their homes in the caverns of active volcanoes, where they have not only adapted to survive in these extreme conditions, but actually thrive in the pools of molten lava found therein. The cherufe's unique physiology lets it feed off of radiating heat, providing sustenance for the creature as well as mending its wounds. The hotter the source, the faster a cherufe recovers.

  Some cultures worship cherufes, likening them to gods or great dragons. A cherufe's depraved and often malicious personality means that it particularly enjoys receiving sacrificial victims. The creature will often toy with an unfortunate sacrifice for days before finally decapitating the corpse and immolating the head. Cherufes cow nearby settlements with threats of earthquakes and volcanic eruptions, though the creatures have little desire to cause such havoc in their own homes and usually exaggerate the power they possess.

  A cherufe stands about 18 feet tall and weighs close to 8,000 pounds. As long as it remains near a heat source, a cherufe can live for hundreds or even thousands of years. Due to these long lifespans, nearby humanoids often believe the creatures immortal, and spread legends about the “gods of the volcanoes.” If taken away from a source of intense heat, a cherufe slowly withers and dies, leaving behind a stony shell of a carcass.

---

# Cherufe
This towering reptilian humanoid seems to be made of obsidian scales over a molten magma core.
**Source** Bestiary 5 pg. 55
**XP** 25,600

NE Huge magical beast (fire)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +17

##### Defense

**AC** 24, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+1 Dex, +15 natural, -2 size)
**hp** 189 (18d10+90)
**Fort** +16, **Ref** +14, **Will** +10
**Defensive Abilities** fire healing; **DR** 10/—; **Immune** fire
**Weaknesses** vulnerable to cold

##### Offense
**Speed** 50 ft., swim 30 ft.
**Melee** 2 claws +25 (2d6+8 plus _[[universal monster rules/Burn|burn]]_), bite +25 (2d8+8 plus _burn_)
**Ranged** rock +19 (2d8+10 plus _burn_)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _burn_ (2d6 fire, DC 24), _[[universal monster rules/Heat|heat]]_, _[[universal monster rules/Rock Throwing|rock throwing]]_ (120 ft.)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +18)
1/month—_[[spells/Earthquake|earthquake]]_

##### Statistics
**Str** 26, **Dex** 13, **Con** 20, **Int** 11, **Wis** 14, **Cha** 11
**Base Atk** +18; **CMB** +28; **CMD** 39
**Feats** _[[feats/Diehard|Diehard]]_, _[[feats/Endurance|Endurance]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite), _Weapon Focus_ (claw), _Weapon Focus_ (rock)
**Skills** _[[universal monster rules/Climb|Climb]]_ +23, Perception +17, Swim +30
**Languages** Common

##### Ecology

**Environment** any mountains
**Organization** solitary
**Treasure** standard

### Special Abilities

**Fire Healing (Ex)** Any source that normally deals fire damage to a _[[monsters/Cherufe|cherufe]]_ instead heals 1 point of damage for every 3 points of damage the attack would otherwise deal. If the amount of healing would cause the _cherufe_ to exceed its full normal hit points, it gains any excess as temporary hit points. These temporary hit points don't stack.

**_Heat_ (Su)** Cherufes transfer their _heat_ to any weapons, including their _rock throwing_, causing _burn_.

##### Description

Cherufes make their homes in the caverns of active volcanoes, where they have not only adapted to survive in these extreme conditions, but actually thrive in the pools of molten lava found therein. The _cherufe_’s unique physiology lets it feed off of radiating _heat_, providing sustenance for the creature as well as _[[spells/Mending|mending]]_ its wounds. The hotter the source, the faster a _cherufe_ recovers.

Some cultures worship cherufes, likening them to gods or great dragons. A _cherufe_’s depraved and often malicious personality means that it particularly enjoys receiving sacrificial victims. The creature will often toy with an unfortunate _[[spells/Sacrifice|sacrifice]]_ for days before finally decapitating the corpse and immolating the head. Cherufes cow nearby settlements with threats of earthquakes and _[[items/Armor Magic Abilities/Volcanic|volcanic]]_ eruptions, though the creatures have little desire to cause such havoc in their own homes and usually exaggerate the power they possess.

A _cherufe_ stands about 18 feet tall and weighs close to 8,000 pounds. As long as it remains near a _heat_ source, a _cherufe_ can live for hundreds or even thousands of years. Due to these long lifespans, nearby humanoids often believe the creatures immortal, and spread legends about the “gods of the volcanoes.” If taken away from a source of intense _heat_, a _cherufe_ slowly withers and dies, leaving behind a stony shell of a carcass.
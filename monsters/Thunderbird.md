---
cssclass: [monsters]
title1: Thunderbird
desc_short: This enormous bird has feathers the color of a stormy sky, a resemblance
  enhanced by the lightning that dances over its body.
title2: Thunderbird
CR: 11
sources:
- name: Bestiary 2
  page: 264
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 12800
alignment: N
size: Gargantuan
type: magical beast
initiative:
  bonus: 7
senses:
  darkvision: 60
  low-light vision: true
  stormsight: true
auras:
- name: storm aura
  radius: 100
AC:
  AC: 25
  touch: 10
  flat_footed: 21
  components:
    dex: 3
    dodge: 1
    natural: 15
    size: -4
HP:
  HP: 147
  long: 14d10+70
saves:
  fort: 14
  ref: 12
  will: 9
immunities:
- electricity
- sonic
speeds:
  base: 30
  fly: 120
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 claws +18 (2d6+8/19-20 plus grab)
      entries:
      - - damage: 2d6+8
          crit_range: 19-20
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 18
    - text: bite +18 (2d8+8/19-20)
      entries:
      - - damage: 2d8+8
          crit_range: 19-20
      attack: bite
      bonus:
      - 18
  ranged:
  - - text: thunderbolt +13 ranged touch (6d6 electricity and 6d6 sonic)
      entries:
      - - damage: 6d6
          type: electricity
        - damage: 6d6
          type: sonic
      attack: thunderbolt
      bonus:
      - 13
      touch: true
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: control weather
    source: default
    freq: At will
  sources:
  - name: default
    CL: 11
    concentration: 12
ability_scores:
  STR: 26
  DEX: 17
  CON: 21
  INT: 12
  WIS: 16
  CHA: 13
BAB: 14
CMB: 26
CMB_other: +30 grapple
CMD: 40
feats:
- name: Critical Focus
- name: Dodge
- name: Improved Critical (bite)
- name: Improved Critical (claw)
- name: Improved Initiative
- name: Iron Will
- name: Power Attack
skills:
  Acrobatics: 13
  Fly: 11
  Perception: 20
  Perform (sing): 8
  Sense Motive: 10
languages:
- Auran
ecology:
  environment: any hills or mountains
  organization: solitary
  treasure_type: none
special_abilities:
  Thunderbolt (Su): A thunderbird can fire a ray of thunder and lightning from its
    outspread wings as a standard action. This attack has a range of 200 feet with
    no range increment, and requires a ranged touch attack to hit. A creature critically
    hit by a thunderbolt is stunned and deafened for 1 round if it fails a DC 22 Fortitude
    save. The save DC is Constitution-based.
  Storm Aura (Su): A thunderbird is surrounded by a 100-foot-radius spread of severe
    winds that blow out from the center, dissipating swiftly at the limit of the aura's
    range. In this area, ranged weapons (but not siege weapons) take a -4 penalty
    on attack rolls, Fly checks are made at a -4 penalty, and exposed flames are extinguished.
    Small creatures must make a DC 10 Strength check (if on the ground) or a DC 20
    Fly check to move toward the thunderbird, while Tiny or smaller creatures can
    be knocked backward (1d4 × 10 feet if they are on the ground and fail a DC 15
    Strength check, or 2d6 × 10 feet if they are flying and fail a DC 25 Fly check).
    Creatures on the ground that are pushed back take 1d4 points of nonlethal damage
    per 10 feet, and flying creatures that are pushed back take 2d6 points of nonlethal
    damage regardless of the distance they are pushed. In addition, once every 1d4
    rounds, a bolt of lightning strikes a random creature (other than the thunderbird)
    within the area of its storm aura. This bolt of lightning deals 12d6 points of
    electricity damage (DC 22 Reflex halves). The save DC for the lightning bolt is
    Constitution-based, while those for resisting the wind effects are fixed.
  Stormsight (Ex): A thunderbird ignores all vision penalties and concealment from
    weather effects, including those created by fog cloud, obscuring mist, and similar
    spells.
desc_long: |-
  Thunderbirds bring the storm on their wings. In times of drought, they are welcomed with joy and celebration. In other times, they are placated with gifts in hopes that they might leave quickly before flooding begins. When angered, thunderbirds can call down hurricanes and lay waste to entire villages, so in regions where these birds dwell, many villages maintain extensive rituals designed to appease and honor the local thunderbirds.

  Thunderbirds nest near the base of waterfalls, where the constant thrum of crashing water prepares the hatchlings for a life at the heart of a storm. Once the chicks have hatched, their parents carry the offspring to nests at the top of mountains, where the young are struck by their first bolts of lightning and learn the mysteries of the storm.

---

# Thunderbird
This enormous bird has feathers the color of a stormy sky, a resemblance enhanced by the lightning that dances over its body.
**Source** Bestiary 2 pg. 264
**XP** 12,800

N Gargantuan magical beast
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, stormsight; Perception +20
**Aura** storm aura (100 ft.)

##### Defense

**AC** 25, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+3 Dex, +1 dodge, +15 natural, –4 size)
**hp** 147 (14d10+70)
**Fort** +14, **Ref** +12, **Will** +9
**Immune** electricity, sonic

##### Offense
**Speed** 30 ft., fly 120 ft. (good)
**Melee** 2 claws +18 (2d6+8/19–20 plus _[[universal monster rules/Grab|grab]]_), bite +18 (2d8+8/19–20)
**Ranged** thunderbolt +13 ranged touch (6d6 electricity and 6d6 sonic)
**Space** 20 ft., **Reach** 20 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +12)
At will—_[[spells/Control Weather|control weather]]_

##### Statistics
**Str** 26, **Dex** 17, **Con** 21, **Int** 12, **Wis** 16, **Cha** 13
**Base Atk** +14; **CMB** +26 (+30 grapple); **CMD** 40
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _Improved Critical_ (claw), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Acrobatics +13, Fly +11, Perception +20, Perform (sing) +8, Sense Motive +10
**Languages** Auran

##### Ecology

**Environment** any hills or mountains
**Organization** solitary
**Treasure** none

### Special Abilities

**Thunderbolt (Su)** A _[[monsters/Thunderbird|thunderbird]]_ can fire a ray of thunder and lightning from its outspread wings as a standard action. This attack has a range of 200 feet with no range increment, and requires a ranged touch attack to hit. A creature critically hit by a thunderbolt is _[[conditions/Stunned|stunned]]_ and _[[conditions/Deafened|deafened]]_ for 1 round if it fails a DC 22 Fortitude save. The save DC is Constitution-based.
**Storm Aura (Su) **A _thunderbird_ is surrounded by a 100-foot-radius spread of severe winds that blow out from the center, dissipating swiftly at the limit of the aura’s range. In this area, ranged weapons (but not siege weapons) take a –4 penalty on attack rolls, Fly checks are made at a –4 penalty, and exposed flames are extinguished. Small creatures must make a DC 10 Strength check (if on the ground) or a DC 20 Fly check to move toward the _thunderbird_, while Tiny or smaller creatures can be knocked backward (1d4 × 10 feet if they are on the ground and fail a DC 15 Strength check, or 2d6 × 10 feet if they are flying and fail a DC 25 Fly check). Creatures on the ground that are pushed back take 1d4 points of nonlethal damage per 10 feet, and flying creatures that are pushed back take 2d6 points of nonlethal damage regardless of the distance they are pushed. In addition, once every 1d4 rounds, a bolt of lightning strikes a random creature (other than the _thunderbird_) within the area of its storm aura. This bolt of lightning deals 12d6 points of electricity damage (DC 22 Reflex halves). The save DC for the _[[spells/Lightning Bolt|lightning bolt]]_ is Constitution-based, while those for resisting the wind effects are fixed.
**Stormsight (Ex)** A _thunderbird_ ignores all _[[spells/Vision|vision]]_ penalties and concealment from weather effects, including those created by _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Obscuring Mist|obscuring mist]]_, and similar spells.

##### Description

Thunderbirds bring the storm on their wings. In times of drought, they are welcomed with joy and celebration. In other times, they are placated with gifts in hopes that they might leave quickly before flooding begins. When angered, thunderbirds can call down hurricanes and lay waste to entire villages, so in regions where these birds dwell, many villages maintain extensive rituals designed to appease and honor the local thunderbirds.

Thunderbirds nest near the base of waterfalls, where the constant thrum of crashing water prepares the hatchlings for a life at the heart of a storm. Once the chicks have hatched, their parents carry the offspring to nests at the top of mountains, where the young are struck by their first bolts of lightning and learn the mysteries of the storm.
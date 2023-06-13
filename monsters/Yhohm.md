---
cssclass: [monsters]
title1: Yhohm
desc_short: This beautiful dove is as bright as the sun and the size of an eagle,
  surrounded by an aura of blazing white flames.
title2: Yhohm
CR: 4
sources:
- name: Inner Sea Gods
  page: 307
  link: http://paizo.com/products/btpy94wj?Pathfinder-Campaign-Setting-Inner-Sea-Gods-Hardcover
XP: 1200
alignment: NG
size: Tiny
type: outsider
subtypes:
- extraplanar
- fire
- good
initiative:
  bonus: 6
senses:
  darkvision: 60
  low-light vision: true
  detect poison: true
auras:
- name: shroud of flame
  radius: 10
  DC: 14
  duration: 10 rounds
AC:
  AC: 18
  touch: 15
  flat_footed: 15
  components:
    dex: 2
    dodge: 1
    natural: 3
    size: 2
HP:
  HP: 37
  long: 5d10+10
  regeneration: 1
  regeneration_weakness: cold or evil
saves:
  fort: 6
  ref: 3
  will: 6
  other: +4 vs. poison
defensive_abilities:
- self-resurrection
DR:
- amount: 5
  weakness: evil
immunities:
- fire
- petrification
resistances:
  electricity: 10
SR: 15
weaknesses:
- vulnerable to cold
speeds:
  base: 10
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: 2 talons +9 (1d2 plus 1d6 fire)
      entries:
      - - damage: 1d2
        - damage: 1d6
          type: fire
      count: 2
      attack: talons
      bonus:
      - 9
    - text: bite +9 (1d3 plus 1d6 fire)
      entries:
      - - damage: 1d3
        - damage: 1d6
          type: fire
      attack: bite
      bonus:
      - 9
  special:
  - holy fire
space: 2.5
reach: 0
spell_like_abilities:
  entries:
  - name: detect poison
    source: default
    freq: Constant
  - name: light
    source: default
    freq: At will
  - name: purify food and drink
    source: default
    freq: At will
  - name: stabilize
    source: default
    freq: At will
  - name: virtue
    source: default
    freq: At will
  - name: cure light wounds
    source: default
    freq: 3/day
  - name: daylight
    source: default
    freq: 3/day
  - name: flaming sphere
    source: default
    freq: 3/day
    DC: 14
  - name: dimension door
    source: default
    freq: 1/day
    other: self only
  - name: lesser restoration
    source: default
    freq: 1/day
  - name: see invisibiliity
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 5
    concentration: 7
ability_scores:
  STR: 10
  DEX: 15
  CON: 14
  INT: 10
  WIS: 15
  CHA: 14
BAB: 5
CMB: 5
CMD: 18
feats:
- name: Dodge
- name: Improved Initiative
- name: Weapon Finesse
skills:
  Fly: 14
  Heal: 10
  Knowledge (religion): 8
  Perception: 10
  Perform (sing): 10
  Stealth: 18
languages:
- Celestial
ecology:
  environment: any (Nirvana)
  organization: solitary, pair, or flight (3-5)
  treasure_type: none
special_abilities:
  Holy Fire (Su): Like a flame strike, half the fire damage from a yhohm's fire attacks
    is fire damage; the other half is divine power and is not subject to fire immunity
    or resistance.
  Self-Resurrection (Su): A slain yhohm remains dead for only 1d4 rounds unless its
    body is completely destroyed by an effect such as disintegrate. Otherwise, a fully
    healed yhohm emerges from the remains 1d4 rounds after death, as if brought back
    to life via resurrection. The yhohm gains 1 permanent negative level when this
    occurs. A yhohm can self-resurrect only once per year. If a yhohm dies a second
    time before that year passes, its death is permanent. A yhohm that dies within
    the area of a desecrate spell cannot self-resurrect until the desecrate effect
    ends, at which point the yhohm immediately resurrects. A yhohm brought back to
    life by other means never gains negative levels as a result.
  Shroud of Flame (Su): A yhohm can cause its feathers to burst into fire as a free
    action. As long as its feathers are burning, it deals an additional 1d6 points
    of fire damage with each natural attack, and any creature within 5 feet must attempt
    a DC 14 Reflex save each round or take 1d6 points of fire damage at the start
    of its turn. A creature that attacks the yhohm with a natural or non-reach melee
    weapon takes 1d6 points of fire damage (no save) with each successful hit. The
    save DC is Constitution-based.
desc_long: |-
  A yhohm is a spirit of holy fire that serves the Dawnflower. According to the faithful, each time a phoenix is reborn, a portion of its soul incarnates in Nirvana as a yhohm. Eternally young and obsessed with life, a yhohm is a creature of healing, joyful song, and cleansing fire. While far less intimidating and wise than true phoenixes, yhohms prove far more carefree, as though a great weight has been lifted from their souls. Despite that, many yhohms also harbor a deep sadness, as though they have left some great work undone.

  A yhohm looks like a white dove, but is as large as an eagle, with eyes like burning coals that shine with the light of the sun. The presence of evil fills it with righteous indignation. It does not need to eat, but enjoys the taste of roasted berries and nuts. A yhohm measures just under 2 feet long and weighs about 4 pounds.

---

# Yhohm
This beautiful dove is as bright as the sun and the size of an _[[monsters/Eagle|eagle]]_, surrounded by an aura of blazing white flames.
**Source** Inner Sea Gods pg. 307
**XP** 1,200

NG Tiny outsider (extraplanar, fire, good)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/Detect Poison|detect poison]]_; Perception +10
**Aura** shroud of flame (10 ft., DC 14, 10 rounds)

##### Defense

**AC** 18, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+2 Dex, +1 dodge, +3 natural, +2 size)
**hp** 37 (5d10+10); _[[universal monster rules/Regeneration|regeneration]]_ 1 (cold or evil)
**Fort** +6, **Ref** +3, **Will** +6; +4 vs. poison
**Defensive Abilities** self-resurrection; **DR** 5/evil; **Immune** fire, petrification; **Resist** electricity 10; **SR** 15
**Weaknesses** vulnerable to cold

##### Offense
**Speed** 10 ft., fly 60 ft. (average)
**Melee** 2 talons +9 (1d2 plus 1d6 fire), bite +9 (1d3 plus 1d6 fire)
**Space** 2-1/2 ft., **Reach** 0 ft.
**Special Attacks** holy fire
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +7)
Constant—_detect poison_
At will—light, _[[spells/Purify Food and Drink|purify food and drink]]_, stabilize, _[[spells/Virtue|virtue]]_
3/day—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Daylight|daylight]]_, _[[spells/Flaming Sphere|flaming sphere]]_ (DC 14)
1/day—_[[spells/Dimension Door|dimension door]]_ (self only), lesser _[[spells/Restoration|restoration]]_, see invisibiliity

##### Statistics
**Str** 10, **Dex** 15, **Con** 14, **Int** 10, **Wis** 15, **Cha** 14
**Base Atk** +5; **CMB** +5; **CMD** 18
**Feats** _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Fly +14, _[[spells/Heal|Heal]]_ +10, Knowledge (religion) +8, Perception +10, Perform (sing) +10, Stealth +18
**Languages** Celestial

##### Ecology

**Environment** any (Nirvana)
**Organization** solitary, pair, or _[[universal monster rules/Flight|flight]]_ (3–5)
**Treasure** none

### Special Abilities

**Holy Fire (Su)** Like a _[[spells/Flame Strike|flame strike]]_, half the fire damage from a _[[monsters/Yhohm|yhohm]]_’s fire attacks is fire damage; the other half is _[[spells/Divine Power|divine power]]_ and is not subject to fire _[[universal monster rules/Immunity|immunity]]_ or _[[universal monster rules/Resistance|resistance]]_.
**Self-Resurrection (Su)** A slain _yhohm_ remains dead for only 1d4 rounds unless its body is completely destroyed by an effect such as _[[spells/Disintegrate|disintegrate]]_. Otherwise, a fully healed _yhohm_ emerges from the remains 1d4 rounds after death, as if brought back to life via _[[spells/Resurrection|resurrection]]_. The _yhohm_ gains 1 permanent negative level when this occurs. A _yhohm_ can self-resurrect only once per year. If a _yhohm_ dies a second time before that year passes, its death is permanent. A _yhohm_ that dies within the area of a _[[spells/Desecrate|desecrate]]_ spell cannot self-resurrect until the _desecrate_ effect ends, at which point the _yhohm_ immediately resurrects. A _yhohm_ brought back to life by other means never gains negative levels as a result.
**Shroud of Flame (Su)** A _yhohm_ can cause its feathers to burst into fire as a free action. As long as its feathers are _[[items/Weapon Magic Abilities/Burning|burning]]_, it deals an additional 1d6 points of fire damage with each natural attack, and any creature within 5 feet must attempt a DC 14 Reflex save each round or take 1d6 points of fire damage at the start of its turn. A creature that attacks the _yhohm_ with a natural or non-reach melee weapon takes 1d6 points of fire damage (no save) with each successful hit. The save DC is Constitution-based.

##### Description

A _yhohm_ is a spirit of holy fire that serves the Dawnflower. According to the faithful, each time a _[[monsters/Phoenix|phoenix]]_ is reborn, a portion of its soul incarnates in Nirvana as a _yhohm_. Eternally young and obsessed with life, a _yhohm_ is a creature of healing, joyful song, and _[[spells/Cleansing Fire|cleansing fire]]_. While far less intimidating and wise than true phoenixes, yhohms prove far more carefree, as though a great weight has been lifted from their souls. Despite that, many yhohms also harbor a deep sadness, as though they have left some great work undone.

A _yhohm_ looks like a white dove, but is as large as an _eagle_, with eyes like _burning_ coals that shine with the light of the sun. The presence of evil fills it with _[[items/Armor Magic Abilities/Righteous|righteous]]_ indignation. It does not need to eat, but enjoys the taste of roasted berries and nuts. A _yhohm_ measures just under 2 feet long and weighs about 4 pounds.
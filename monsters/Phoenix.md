---
cssclass: [monsters]
title1: Phoenix
desc_short: This flaming bird burns as brightly as the sun.
title2: Mythic Phoenix
CR: 18
MR: 7
sources:
- name: Mythic Adventures
  page: 214
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 153600
alignment: NG
size: Gargantuan
type: magical beast
subtypes:
- fire
- mythic
initiative:
  bonus: 12
senses:
  darkvision: 60
  detect magic: true
  detect poison: true
  low-light vision: true
  see invisibility: true
  true seeing: true
auras:
- name: shroud of flame
  radius: 20
  other:
  - 4d6 fire
  DC: 26
AC:
  AC: 37
  touch: 16
  flat_footed: 27
  components:
    dex: 8
    dodge: 2
    natural: 21
    size: -4
HP:
  HP: 280
  long: 20d10+170
  regeneration: 10
  regeneration_weakness: cold or evil
saves:
  fort: 17
  ref: 20
  will: 14
defensive_abilities:
- self-resurrection
DR:
- amount: 15
  weakness: epic and evil
immunities:
- fire
SR: 29
weaknesses:
- vulnerable to cold
speeds:
  base: 30
  fly: 90
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +25 (3d6+9 plus burn)
      entries:
      - - damage: 3d6+9
        - effect: burn
      attack: bite
      bonus:
      - 25
    - text: 2 talons +25 (2d8+9/19-20 plus burn plus grab)
      entries:
      - - damage: 2d8+9
          crit_range: 19-20
        - effect: burn
        - effect: grab
      count: 2
      attack: talons
      bonus:
      - 25
  special:
  - burn (2d6, DC 25)
  - incinerate
  - mythic power (7/day, surge +1d10)
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: detect poison
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: continual flame
    source: default
    freq: At will
  - name: cure critical wounds
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: remove curse
    source: default
    freq: At will
  - name: wall of fire
    source: default
    freq: At will
  - name: fire storm
    source: default
    freq: 3/day
    DC: 24
  - name: greater restoration
    source: default
    freq: 3/day
  - name: heal
    source: default
    freq: 3/day
  - name: mass cure critical wounds
    source: default
    freq: 3/day
  - name: quickened wall of fire
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 18
    concentration: 24
ability_scores:
  STR: 29
  DEX: 27
  CON: 20
  INT: 25
  WIS: 22
  CHA: 22
BAB: 20
CMB: 33
CMB_other: +37 grapple
CMD: 53
feats:
- name: Blinding Critical
- is_mythic: true
  name: Combat Reflexes
- name: Critical Focus
- is_mythic: true
  name: Dodge
- name: Flyby Attack
- name: Improved Critical (talons)
- name: Improved Initiative
- is_mythic: true
  name: Iron Will
- is_mythic: true
  name: Mobility
- name: Quicken Spell-Like Ability (wall of fire)
skills:
  Acrobatics: 31
  Diplomacy: 26
  Fly: 29
  Intimidate: 26
  Knowledge (nature): 27
  Knowledge (any two others): 27
  Perception: 37
  Sense Motive: 26
  _racial_mods:
    Perception:
      _: 8
languages:
- Auran
- Celestial
- Common
- Ignan
special_qualities:
- death throes
- mirror dodge (see page 18)
- parry spell (see page 30)
ecology:
  environment: warm desert and hills
  organization: solitary
  treasure_type: standard
special_abilities:
  Death Throes (Su): When killed, a mythic phoenix explodes in a blinding flash that
    deals 75 points of damage (half of this is fire damage, the other half is holy
    damage) to anything within 50 feet (Reflex DC 25 for half). The save DC is Constitution-based.
  Incinerate (Su): Any creature killed by fire damage from a mythic phoenix is entirely
    destroyed, leaving behind only a trace of fine ash. The creature's magical equipment
    is unaffected.
  Self-Resurrection (Su): Unless its body is completely destroyed by an effect such
    as disintegrate, a slain mythic phoenix remains dead for only 1d4 rounds, emerging
    fully healed from its remains as if brought back to life via resurrection. A phoenix
    can self-resurrect only once per year. If a phoenix dies a second time before
    that year passes, its death is permanent. A mythic phoenix that dies within the
    area of a mythic desecrate spell cannot self-resurrect until the spell ends, at
    which point the phoenix immediately resurrects. A phoenix brought back to life
    by other means never gains negative levels as a result.
  Shroud of Flame (Su): A mythic phoenix can cause its feathers to burst into fire
    as a free action. As long as its feathers are burning, any creature within reach
    must succeed at a DC 25 Reflex save each round to avoid taking 4d6 points of fire
    damage at the start of its turn. A creature that attacks the phoenix with natural
    or non-reach melee weapons takes 1d6 points of fire damage (no save) with each
    successful hit. The save DC is Constitution-based.
desc_long: A mythic phoenix is appointed by the gods to watch over the birth, death,
  and renewal of significant things-such as heroes, religions, or even entire worlds.
  It uses its powers to destroy evils that would interfere with the great cycle.

---

# Phoenix
This immense bird seems to be made of living flame. It spreads its wings and gives vent to a musical cry as it takes to the air.
**Source** Pathfinder RPG Bestiary pg. 227
**XP** 51,200

NG Gargantuan magical beast (fire)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +37
**Aura** shroud of flame (20 ft., 4d6 fire, DC 25)

##### Defense

**AC** 28, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+7 Dex, +1 dodge, +14 natural, –4 size)
**hp** 210 (20d10+100); _[[universal monster rules/Regeneration|regeneration]]_ 10 (cold or evil)
**Fort** +17, **Ref** +19, **Will** +14
**Defensive Abilities** self-resurrection; **DR** 15/evil; **Immune** fire; **Resist** 26
**Weaknesses** vulnerable to cold

##### Offense
**Speed** 30 ft., fly 90 ft. (good)
**Melee** 2 talons +24 (2d6+8/19–20 plus 1d6 fire) and bite +24 (2d8+8 plus 1d6 fire)
**Space** 20 ft., **Reach** 20 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th)
Constant—_detect magic_, _detect poison_, _see invisibility_
At will—_[[spells/Continual Flame|continual flame]]_, _[[spells/Cure Critical Wounds|cure critical wounds]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Remove Curse|remove curse]]_, _[[spells/Wall Of Fire|wall of fire]]_
3/day—_[[spells/Fire Storm|fire storm]]_ (DC 24), greater _[[spells/Restoration|restoration]]_, _[[spells/Heal, Mass|heal, mass]]_ _cure critical wounds_, quickened _wall of fire_

##### Statistics
**Str** 27, **Dex** 25, **Con** 20, **Int** 23, **Wis** 22, **Cha** 22
**Base Atk** +20; **CMB** +32; **CMD** 50
**Feats** _[[feats/Blinding Critical|Blinding Critical]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Critical|Improved Critical]]_ (talon), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_wall of fire_)
**Skills** Acrobatics +30, Diplomacy +26, Fly +28, Intimidate +26, Knowledge (nature plus any one other) +26, Perception +37, Sense Motive +26; **Racial Modifiers** +8 Perception
**Languages** Auran, Celestial, Common, Ignan

##### Ecology

**Environment** warm desert and hills
**Organization** solitary
**Treasure** standard

### Special Abilities
**Self-Resurrection (Su) **A slain _[[monsters/Phoenix|phoenix]]_ remains dead for only 1d4 rounds unless its body is completely destroyed by an effect such as _[[spells/Disintegrate|disintegrate]]_. Otherwise, a fully healed _phoenix_ emerges from the remains 1d4 rounds after death, as if brought back to life via _[[spells/Resurrection|resurrection]]_. The _phoenix_ gains 1 permanent negative level when this occurs, although most use greater _restoration_ to remove this negative level as soon as possible. A _phoenix_ can self-resurrect only once per year. If a _phoenix_ dies a second time before that year passes, its death is permanent. A _phoenix_ that dies within the area of a _[[spells/Desecrate|desecrate]]_ spell cannot self-resurrect until the _desecrate_ effect ends, at which point the _phoenix_ immediately resurrects. A _phoenix_ brought back to life by other means never gains negative levels as a result.
**Shroud of Flame (Su)** A _phoenix_ can cause its feathers to burst into fire as a free action. As long as its feathers are _[[items/Weapon Magic Abilities/Burning|burning]]_, it inflicts an additional 1d6 points of fire damage with each natural attack, and any creature within reach (20 feet for most phoenixes) must make a DC 25 Reflex save each round to avoid taking 4d6 points of fire damage at the start of its turn. A creature that attacks the _phoenix_ with natural or non-reach melee weapons takes 1d6 points of fire damage (no save) with each successful hit. The save DC is Constitution-based.

##### Description

The _phoenix_ is a legendary bird of fire that dwells in the most remote parts of the desert. As the birds are known to be great scholars, many seekers of rare lore search out particular phoenixes for advice. Yet it is the _phoenix_’s ability to rebirth itself from its own dead body for which the creature is best known.

The _phoenix_ is a _[[items/Weapon Magic Abilities/Benevolent|benevolent]]_ creature, aiding those who do good and actively harming those who do evil.
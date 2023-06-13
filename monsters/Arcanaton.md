---
cssclass: [monsters]
title1: Arcanaton
is_3.5: true
desc_short: This fiery sphere of energy pulses like an ember in a warm hearth. Three
  silver eyes swim across the globe's surface, widening and narrowing as they consider
  their prey, and three whip-like tentacles slowly twitch in the manner of a cat's
  tail.
title2: Arcanaton
CR: 9
sources:
- name: Guardians of Dragonfall
  page: 29
  link: http://paizo.com/store/paizo/pathfinder/modules/35E/v5748btpy811p
alignment: N
size: Medium
type: outsider
initiative:
  bonus: 10
senses:
  darkvision: 60
AC:
  AC: 22
  touch: 20
  flat_footed: 16
  components:
    deflection: 4
    dex: 6
    natural: 2
HP:
  HP: 76
  long: 9d8+36
saves:
  fort: 10
  ref: 12
  will: 8
defensive_abilities:
- arcane consumption
- immunity to magic
speeds:
  fly: 90
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 3 tentacles +15 (1d8+2) plus arcane consumption
      entries:
      - - damage: 1d8+2
        - effect: arcane consumption
      count: 3
      attack: tentacles
      bonus:
      - 15
  ranged:
  - - text: arcane fire +15 touch (9d6)
      entries:
      - - damage: 9d6
      attack: arcane fire
      bonus:
      - 15
      touch: true
  special:
  - arcane consumption
  - arcane fire
space: 5
reach: 10
ability_scores:
  STR: 14
  DEX: 23
  CON: 18
  INT: 9
  WIS: 14
  CHA: 19
BAB: 9
grapple_3.5: 11
feats:
- name: Alertness
- name: Flyby Attack
- name: Improved Initiative
- name: Weapon Finesse
skills:
  Concentration: 17
  Knowledge (arcana): 12
  Listen: 17
  Search: 12
  Spellcraft: 12
  Spot: 17
  Use Magic Device: 17
special_qualities:
- arcane consumption
ecology:
  environment: any
  organization: solitary or cluster (2-5)
  treasure_type: none
  advancement_3.5:
  - type: size
    HD_min: 10
    size: Medium
    HD_max: 18
  - type: size
    HD_min: 19
    size: Large
    HD_max: 27
special_abilities:
  Arcane Consumption (Su): A successful tentacle attack by an arcanaton conveys the
    effects of a targeted dispel magic (9th level caster), affecting worn magical
    protections first and proceeding to spells in effect on the target once all worn
    magical protections have been suppressed. Any magic weapon or magic object touching
    an arcanaton (including melee attacks) is treated as the subject of a targeted
    dispel magic (9th level caster). Each successful suppression of a magic item or
    spell dispelled grants the arcanaton 3 temporary hp.
  Arcane Fire (Su): An arcanaton can fire a bolt of raw magical energy as a standard
    action. The bolt is a ranged touch attack with 190 ft. range that deals 9d6 points
    of damage.
  Immunity to Magic (Ex): An arcanaton is immune to any spell or spell-like ability
    that allows spell resistance. In addition, certain spells and effects function
    differently against the creature, as noted here. A magical attack that dispels
    magical effects, such as dispel magic, slows an arcanaton (as the slow spell)
    for 2d6 rounds, with no saving throw. If an arcanaton contacts an antimagic field,
    it is stunned for 1d4 rounds, with no saving throw.
desc_long: |-
  Arcanatons are elementals of magic, the raw stuff of dweomer given sentience. Their origin is unknown, and while legends indicate their summoning and binding was once commonplace, it is now a lost art. They seek out areas of active magic and consume what they can, but they are not unreasoning parasites, and some mages report successfully appeasing an arcanaton and sending it on its way.

  Environment: Any area of high magic.

  Typical Physical Characteristics: Arcanatons measure five to six feet in diameter, with tentacles seven to ten feet in length. They are weightless. Their coloration intensifies after consuming magical energy, and pales when they are deprived of it.

---

# Arcanaton
This fiery sphere of energy pulses like an ember in a warm hearth. Three silver eyes swim across the globe’s surface, widening and narrowing as they consider their prey, and three whip-like tentacles slowly twitch in the manner of a cat’s tail.
**Source** Guardians of Dragonfall pg. 29

N Medium outsider
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Listen +17, Spot +17

##### Defense

**AC** 22, touch 20, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+4 _[[spells/Deflection|deflection]]_, +6 Dex, +2 natural)
**hp** 76 (9d8+36)
**Fort** +10, **Ref** +12, **Will** +8
**Defensive Abilities** arcane _[[feats/Consumption|consumption]]_, _[[universal monster rules/Immunity|immunity]]_ to magic

##### Offense
**Speed** fly 90 ft. (perfect)
**Melee** 3 tentacles +15 (1d8+2) plus arcane _consumption_
**Ranged** arcane fire +15 touch (9d6)
**Space** 5 ft., **Reach** 10 ft.
**Special Attacks** arcane _consumption_, arcane fire

##### Statistics
**Str** 14, **Dex** 23, **Con** 18, **Int** 9, **Wis** 14, **Cha** 19
**Base Atk** +9; **Grapple** +11
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Concentration +17, Knowledge (arcana) +12, Listen +17, Search +12, Spellcraft +12, Spot +17, Use Magic Device +17
**SQ** arcane _consumption_

##### Ecology

**Environment** any
**Organization** solitary or cluster (2-5)
**Treasure** none
**Advancement** 10-18 HD (_Medium_), 19-27 HD (Large)

### Special Abilities

**Arcane _Consumption_ (Su)** A successful tentacle attack by an _[[monsters/Arcanaton|arcanaton]]_ conveys the effects of a targeted _[[spells/Dispel Magic|dispel magic]]_ (9th level caster), affecting worn magical protections first and proceeding to spells in effect on the target once all worn magical protections have been suppressed. Any _[[spells/Magic Weapon|magic weapon]]_ or magic object touching an _arcanaton_ (including melee attacks) is treated as the subject of a targeted _dispel magic_ (9th level caster). Each successful suppression of a magic item or spell dispelled grants the _arcanaton_ 3 temporary hp.

**Arcane Fire (Su)** An _arcanaton_ can fire a bolt of raw magical energy as a standard action. The bolt is a ranged touch attack with 190 ft. range that deals 9d6 points of damage.

**_Immunity_ to Magic (Ex)** An _arcanaton_ is immune to any spell or spell-like ability that allows _[[universal monster rules/Spell Resistance|spell resistance]]_. In addition, certain spells and effects function differently against the creature, as noted here. A magical attack that dispels magical effects, such as _dispel magic_, slows an _arcanaton_ (as the _[[spells/Slow|slow]]_ spell) for 2d6 rounds, with no saving throw. If an _arcanaton_ contacts an _[[spells/Antimagic Field|antimagic field]]_, it is _[[conditions/Stunned|stunned]]_ for 1d4 rounds, with no saving throw.

##### Description

Arcanatons are elementals of magic, the raw stuff of dweomer given sentience. Their origin is _[[monsters/Unknown|unknown]]_, and while legends indicate their summoning and _[[spells/Binding|binding]]_ was once commonplace, it is now a lost art. They seek out areas of active magic and consume what they can, but they are not unreasoning parasites, and some mages report successfully appeasing an _arcanaton_ and _[[spells/Sending|sending]]_ it on its way.

**Environment**: Any area of high magic.

**Typical Physical Characteristics**: Arcanatons measure five to six feet in diameter, with tentacles seven to ten feet in length. They are weightless. Their coloration intensifies after consuming magical energy, and pales when they are deprived of it.
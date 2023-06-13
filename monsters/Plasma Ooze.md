---
cssclass: [monsters]
title1: Plasma Ooze
desc_short: This amorphous blob of violet energy ripples like a globe of floating
  liquid. It periodically lashes out with tendrils of blue light.
title2: Plasma Ooze
CR: 16
sources:
- name: Bestiary 3
  page: 220
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 76800
alignment: N
size: Gargantuan
type: ooze
initiative:
  bonus: 0
senses:
  blindsight: 60
auras:
- name: magnetic pulse
  radius: 30
  DC: 27
AC:
  AC: 6
  touch: 6
  flat_footed: 6
  components:
    size: -4
HP:
  HP: 241
  long: 21d8+147
saves:
  fort: 14
  ref: 7
  will: 2
defensive_abilities:
- split (slashing or sonic, 46 hp)
DR:
- amount: 15
  weakness: '-'
immunities:
- acid
- electricity
- fire
- bludgeoning and piercing damage
- ooze traits
resistances:
  cold: 30
speeds:
  fly: 30
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: slam +24 (4d6+19 plus 4d6 electricity, 4d6 fire, and grab)
      entries:
      - - damage: 4d6+19
        - damage: 4d6
          type: electricity
        - damage: 4d6
          type: fire
        - effect: grab
      attack: slam
      bonus:
      - 24
  ranged:
  - - text: 1d4 plasma rays +11 touch (4d6 electricity plus 4d6 fire)
      entries:
      - - damage: 4d6
          type: electricity
        - damage: 4d6
          type: fire
      count: 1d4
      attack: plasma rays
      bonus:
      - 11
      touch: true
  special:
  - constrict (4d6+19 plus 4d6 electricity and 4d6 fire)
  - engulf (DC 33, 4d6 electricity plus 4d6 fire)
space: 20
reach: 20
ability_scores:
  STR: 36
  DEX: 11
  CON: 24
  INT:
  WIS: 1
  CHA: 1
BAB: 15
CMB: 32
CMB_other: +36 grapple
CMD: 42
CMD_other: can't be tripped
skills:
  Fly: 2
  Perception: -5
special_qualities:
- no breath
ecology:
  environment: any
  organization: solitary
  treasure_type: none
special_abilities:
  Magnetic Pulse (Su): A plasma ooze is surrounded by an aura of magnetism that allows
    it to attract metallic objects and creatures. At the start of the ooze's turn
    as a free action, the ooze makes a combat maneuver check against all metallic
    creatures, all creatures wearing metal armor, and all creatures wielding metal
    weapons within 30 feet. If it beats the CMD of a metal or armored creature with
    this check, that creature is pulled 10 feet closer to the ooze and cannot move
    away from the ooze for 1 round. If this causes the creature to move into a square
    occupied by the plasma ooze, the ooze can attempt to engulf that creature as a
    free action. If it beats the CMD of a creature wielding a metal weapon, that weapon
    is disarmed and pulled 10 feet closer to the ooze. Unattended metal objects of
    size Large or smaller are automatically pulled toward a plasma ooze. This magnetism
    is supernatural in nature and affects all metal objects.
  Plasma Ray (Su): As a standard action, a plasma ooze can fire 1d4 plasma rays at
    up to 4 separate targets within 60 feet (no more than one ray can attack a single
    creature). Each ray deals 4d6 points of electricity damage and 4d6 points of fire
    damage on a hit.
desc_long: |-
  Massive and devastating, plasma oozes are mysterious, extraterrestrial beings made of superheated electromagnetic sludge. While their origin is not fully known, it is widely accepted that plasma oozes are not from this world. Some scholars believe they dwell in the sun, while others maintain they hail from the Plane of Fire. That plasma oozes have been encountered in both of these locations does little to help solve the debate.

  A plasma ooze flies by somehow interacting with gravity and magnetic waves, drifting through the air in a manner similar to the way a jellyfish swims in water. This creature's only real purpose is to consume, and it prefers to do so by drawing prey into its fiery, electrified core. Scholars find it curious that while a plasma ooze can only attract and repel metallic substances, the thing can only digest organic matter, and rather slowly at that.

  Survivors of plasma ooze attacks are rare, but such victims describe the pain of being struck by one's rays as like being pulled apart piece by piece. Wounds left by a plasma ooze's touch resemble hideously melted burn scars.

  A plasma ooze is 20 feet in diameter and weighs 6,000 pounds.

---

# Plasma Ooze
This _[[universal monster rules/Amorphous|amorphous]]_ blob of violet energy ripples like a globe of floating liquid. It periodically lashes out with tendrils of blue light.
**Source** Bestiary 3 pg. 220
**XP** 76,800

N Gargantuan ooze
**Init** +0; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 60 ft.; Perception –5
**Aura** magnetic pulse (30 ft., DC 27)

##### Defense

**AC** 6, touch 6, _[[conditions/Flat-Footed|flat-footed]]_ 6 (–4 size)
**hp** 241 (21d8+147)
**Fort** +14, **Ref** +7, **Will** +2
**Defensive Abilities** _[[universal monster rules/Split|split]]_ (slashing or sonic, 46 hp); **DR** 15/—; **Immune** acid, electricity, fire, bludgeoning and piercing damage, ooze traits; **Resist** cold 30

##### Offense
**Speed** fly 30 ft. (perfect)
**Melee** slam +24 (4d6+19 plus 4d6 electricity, 4d6 fire, and _[[universal monster rules/Grab|grab]]_)
**Ranged** 1d4 plasma rays +11 touch (4d6 electricity plus 4d6 fire)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (4d6+19 plus 4d6 electricity and 4d6 fire), _[[universal monster rules/Engulf|engulf]]_ (DC 33, 4d6 electricity plus 4d6 fire)

##### Statistics
**Str** 36, **Dex** 11, **Con** 24, **Int** —, **Wis** 1, **Cha** 1
**Base Atk** +15; **CMB** +32 (+36 grapple); **CMD** 42 (can’t be tripped)
**Skills** Fly +2
**SQ** _[[universal monster rules/No Breath|no breath]]_

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** none

### Special Abilities

**Magnetic Pulse (Su) **A _[[monsters/Plasma Ooze|plasma ooze]]_ is surrounded by an aura of magnetism that allows it to attract metallic objects and creatures. At the start of the ooze’s turn as a free action, the ooze makes a combat maneuver check against all metallic creatures, all creatures wearing metal armor, and all creatures wielding metal weapons within 30 feet. If it beats the CMD of a metal or armored creature with this check, that creature is pulled 10 feet closer to the ooze and cannot move away from the ooze for 1 round. If this causes the creature to move into a square occupied by the _plasma ooze_, the ooze can attempt to _engulf_ that creature as a free action. If it beats the CMD of a creature wielding a metal weapon, that weapon is disarmed and pulled 10 feet closer to the ooze. Unattended metal objects of size Large or smaller are automatically pulled toward a _plasma ooze_. This magnetism is supernatural in nature and affects all metal objects.

**Plasma Ray (Su)** As a standard action, a _plasma ooze_ can fire 1d4 plasma rays at up to 4 separate targets within 60 feet (no more than one ray can attack a single creature). Each ray deals 4d6 points of electricity damage and 4d6 points of fire damage on a hit.

##### Description

Massive and devastating, plasma oozes are mysterious, extraterrestrial beings made of superheated electromagnetic sludge. While their origin is not fully known, it is widely accepted that plasma oozes are not from this world. Some scholars believe they dwell in the sun, while others maintain they hail from the Plane of Fire. That plasma oozes have been encountered in both of these locations does little to help solve the debate.

A _plasma ooze_ flies by somehow interacting with gravity and magnetic waves, drifting through the air in a manner similar to the way a jellyfish swims in water. This creature’s only real purpose is to consume, and it prefers to do so by drawing prey into its fiery, electrified core. Scholars find it curious that while a _plasma ooze_ can only attract and repel metallic substances, the thing can only digest organic matter, and rather slowly at that.

Survivors of _plasma ooze_ attacks are rare, but such victims describe the pain of being struck by one’s rays as like being pulled apart piece by piece. Wounds left by a _plasma ooze_’s touch resemble hideously melted _[[universal monster rules/Burn|burn]]_ scars.

A _plasma ooze_ is 20 feet in diameter and weighs 6,000 pounds.
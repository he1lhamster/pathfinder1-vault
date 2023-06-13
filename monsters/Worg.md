---
cssclass: [monsters]
title1: Worg
desc_short: A terrifying darkness surrounds this giant wolf.
title2: Mythic Worg
CR: 3
MR: 1
sources:
- name: Mythic Adventures
  page: 222
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 800
alignment: NE
size: Medium
type: magical beast
subtypes:
- mythic
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
  scent: true
auras:
- name: darkness
  radius: 30
  other:
  - 1 step
AC:
  AC: 15
  touch: 12
  flat_footed: 13
  components:
    dex: 2
    natural: 3
HP:
  HP: 36
  long: 4d10+14
saves:
  fort: 5
  ref: 6
  will: 3
speeds:
  base: 50
attacks:
  melee:
  - - text: bite +7 (1d8+4 plus trip)
      entries:
      - - damage: 1d8+4
        - effect: trip
      attack: bite
      bonus:
      - 7
  special:
  - fear cone (30 ft., DC 12)
  - mythic power (1/day, surge +1d6)
ability_scores:
  STR: 17
  DEX: 15
  CON: 13
  INT: 6
  WIS: 14
  CHA: 10
BAB: 4
CMB: 7
CMD: 19
CMD_other: 23 vs. trip
feats:
- name: Run
- is_mythic: true
  name: Skill Focus (Perception)
skills:
  Perception: 11
  Stealth: 9
  Survival: 5
  _racial_mods:
    Perception:
      _: 2
    Stealth:
      _: 2
    Survival:
      _: 2
languages:
- Common
- Goblin
ecology:
  environment: temperate forests and plains
  organization: solitary, pair, or pack (3-11)
  treasure_type: incidental
special_abilities:
  Darkness Aura (Su): As a free action, a mythic worg can activate its darkness aura,
    which reduces the light level within 30 feet of it by one step. This never reduces
    the light level to supernatural darkness. Multiple worgs within range can reduce
    the light level multiple steps. Because a mythic worg has darkvision and low-light
    vision, this ability never interferes with its own vision. It can end this ability
    as a free action.
desc_long: A mythic worg is a creature of fear and foul darkness, usually born under
  an ominous new moon or by the intervention of a deity of shadows and terror. Many
  serve vampires, protecting their masters from hunters and hazardous daylight.

---

# Worg
This unusually large _[[monsters/Wolf|wolf]]_ has an evil, almost intelligent light shining in its deep red eyes.
**Source** Pathfinder RPG Bestiary pg. 280
**XP** 600

NE Medium magical beast
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +11

##### Defense

**AC** 14, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+2 Dex, +2 natural)
**hp** 26 (4d10+4)
**Fort** +5, **Ref** +6, **Will** +3

##### Offense
**Speed** 50 ft.
**Melee** bite +7 (1d6+4 plus _[[universal monster rules/Trip|trip]]_)

##### Statistics
**Str** 17, **Dex** 15, **Con** 13, **Int** 6, **Wis** 14, **Cha** 10
**Base Atk** +4; **CMB** +7; **CMD** 19 (23 vs. _trip_)
**Feats** Run, _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** Perception +11, Stealth +9, Survival +5; **Racial Modifiers** +2 Perception, +2 Stealth, +2 Survival
**Languages** Common, _[[monsters/Goblin|Goblin]]_

##### Ecology

**Environment** temperate forests and plains
**Organization** solitary, pair, or pack (3–11)
**Treasure** incidental

##### Description

Worgs are oversized, evil, intelligent wolves often found dwelling amid goblins or other savage races. A typical _[[monsters/Worg|worg]]_ has _[[monsters/Gray|gray]]_ or black fur, stands 3 feet tall at the shoulder, and weighs 300 pounds.

Worgs hunt in packs, running down and surrounding their prey like common wolves, but their intelligence and ability to speak make them better at coordinating their attacks. They sometimes use one packmate as a decoy, pretending to be a humanoid calling for help in order to lure intelligent prey into an ambush. Worgs that travel with goblins often allow them to ride on their backs, but in such situations it is usually the _worg_ that is the master, not the rider.
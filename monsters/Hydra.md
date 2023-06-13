---
cssclass: [monsters]
title1: Hydra
desc_short: This seven-headed serpent has serrated fangs, and moves with incredible
  speed despite its massive bulk.
title2: Mythic Hydra
CR: 9
MR: 3
sources:
- name: Mythic Adventures
  page: 204
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 6400
alignment: N
size: Huge
type: magical beast
subtypes:
- mythic
initiative:
  bonus:
  - 1
  - -19
  ability: dual initiative
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 20
  touch: 9
  flat_footed: 19
  components:
    dex: 1
    natural: 11
    size: -2
HP:
  HP: 117
  long: 7d10+79
  fast_healing: 7
saves:
  fort: 10
  ref: 8
  will: 4
DR:
- amount: 5
  weakness: epic
speeds:
  base: 40
  swim: 40
attacks:
  melee:
  - - text: 7 bites +8 (1d8+3 plus bleed)
      entries:
      - - damage: 1d8+3
        - effect: bleed
      count: 7
      attack: bites
      bonus:
      - 8
  special:
  - bleed (1)
  - mythic power (3/day, surge +1d6)
  - pounce
  - push (bite, 10 ft.)
space: 15
reach: 15
ability_scores:
  STR: 17
  DEX: 12
  CON: 20
  INT: 2
  WIS: 11
  CHA: 9
BAB: 7
CMB: 12
CMD: 23
CMD_other: can't be tripped
feats:
- is_mythic: true
  name: Combat Reflexes
- name: Iron Will
- name: Lightning Reflexes
- is_mythic: true
  name: Toughness
skills:
  Perception: 12
  Swim: 11
  _racial_mods:
    Perception:
      _: 2
special_qualities:
- hydra traits
- regenerate head
ecology:
  environment: temperate marshes
  organization: solitary
  treasure_type: standard
special_abilities:
  Fast Healing (Ex): A mythic hydra's fast healing ability is equal to its current
    number of heads (minimum fast healing 5). This fast healing applies only to damage
    dealt to the hydra's body.
  Hydra Traits (Ex): A mythic hydra can be killed by severing all of its heads or
    slaying its body. Any attack that is not an attempt to sever a head affects the
    body, including area attacks or attacks that cause piercing or bludgeoning damage.
    To sever a head, an opponent must make a sunder attempt with a slashing weapon
    targeting a head. A head is considered a separate weapon with hardness 0 and hit
    points equal to the hydra's Hit Dice. To sever a head, an opponent must deal enough
    damage to reduce the head's hit points to 0 or fewer. Severing a head deals damage
    to the hydra's body equal to the hydra's current Hit Dice. A hydra can't attack
    with a severed head, but takes no other penalties.
  Regenerate Head (Ex): When a mythic hydra's head is destroyed, two heads regrow
    in 1d4 rounds. A mythic hydra can't have more than twice its original number of
    heads at any one time. To prevent new heads from growing, at least 5 points of
    acid or fire damage must be dealt to the stump (a touch attack to hit) before
    they appear. Acid or fire damage from area attacks can affect stumps and the body
    simultaneously. A hydra doesn't die from losing heads until all its heads are
    cut off and the stumps are seared by acid or fire.
desc_long: A mythic hydra is a deadly combination of bites, lunges, speed, and durability.
  Descended from the very first of its kind, it may run wild. Or created whole by
  some divine agent, it could be placed as a guardian of a sacred site or a portal
  to the underworld. Some mythic hydras are reputed to have poisonous breath and blood,
  or to be so toxic that they corrupt the ground they crawl upon.

---

# Hydra
Multiple angry snake-like heads rise from the sleek, serpentine body of this terrifying monster.
**Source** Pathfinder RPG Bestiary pg. 178
**XP** 1,200

N Huge magical beast
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +10

##### Defense

**AC** 15, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+1 Dex, +6 natural, –2 size)
**hp** 47 (5d10+20); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +8, **Ref** +7, **Will** +3

##### Offense
**Speed** 20 ft., swim 20 ft.
**Melee** 5 bites +6 (1d8+3)
**Space** 15 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Pounce|pounce]]_

##### Statistics
**Str** 17, **Dex** 12, **Con** 18, **Int** 2, **Wis** 11, **Cha** 9
**Base Atk** +5; **CMB** +10; **CMD** 21 (can’t be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Perception +10, Swim +11; **Racial Modifiers** +2 Perception
**SQ** _[[monsters/Hydra|hydra]]_ traits, _[[spells/Regenerate|regenerate]]_ head

##### Ecology

**Environment** temperate marshes
**Organization** solitary
**Treasure** standard

### Special Abilities

**_Fast Healing_ (Ex)** A _hydra_’s _fast healing_ ability is equal to its current number of heads (minimum _fast healing_ 5). This _fast healing_ applies only to damage inflicted on the _hydra_’s body.

**_Hydra_ Traits (Ex)** A _hydra_ can be killed by severing all of its heads or slaying its body. Any attack that is not an attempt to sever a head affects the body, including area attacks or attacks that cause piercing or bludgeoning damage. To sever a head, an opponent must make a sunder attempt with a slashing weapon targeting a head. A head is considered a separate weapon with hardness 0 and hit points equal to the _hydra_’s HD. To sever a head, an opponent must inflict enough damage to reduce the head’s hit points to 0 or less. Severing a head deals damage to the _hydra_’s body equal to the _hydra_’s current HD. A _hydra_ can’t attack with a severed head, but takes no other penalties.

**_Regenerate_ Head (Ex)** When a _hydra_’s head is destroyed, two heads regrow in 1d4 rounds. A _hydra_ cannot have more than twice its original number of heads at any one time. To prevent new heads from _[[items/Weapon Magic Abilities/Growing|growing]]_, at least 5 points of acid or fire damage must be dealt to the stump (a touch attack to hit) before they appear. Acid or fire damage from area attacks can affect stumps and the body simultaneously. A _hydra_ doesn’t die from losing its heads until all are cut off and the stumps seared by acid or fire.

##### Description

You can make more powerful hydras by increasing their Hit Dice—each added HD increases the _hydra_’s statistics as appropriate, but also gives it one additional head and a +1 increase to its natural armor. A _hydra_’s CR increases by +1 for each Hit Die it gains.

**Cryohydra/Pyrohydra (+2 CR)**: Variants of the standard _hydra_, the cryohydra lives in cold marshes or on glaciers, while the pyrohydra prefers deserts or _[[items/Armor Magic Abilities/Volcanic|volcanic]]_ mountains. A cryohydra gains the Cold subtype, while a pyrohydra gains the Fire subtype. Each of its heads has a _[[universal monster rules/Breath Weapon|breath weapon]]_ (15-ft. cone, 3d6 cold damage [cryohydra] or 3d6 fire damage [pyrohydra], Reflex half) useable every 1d4 rounds. The save DC is 10 + 1/2 the _hydra_’s HD + the _hydra_’s Con modifier. Although fire attacks cannot prevent a pyrohydra’s neck stump from _growing_ new heads (since it is immune to fire), 5 points of cold damage does. Acid works normally on both _hydra_ variants.
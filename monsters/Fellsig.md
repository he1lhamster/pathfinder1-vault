---
cssclass: [monsters]
title1: Fellsig
desc_short: This squat figure's rough-hewn visage is frozen in a mask of pain, while
  the cracks in its dark stone body glow with a fiery inner heat.
title2: Fellsig
CR: 3
sources:
- name: Andoran, Birthplace of Freedom
  page: 55
  link: http://paizo.com/products/btpy9dz4?Pathfinder-Campaign-Setting-Andoran-Birthplace-of-Freedom
XP: 800
alignment: NE
size: Medium
type: undead
subtypes:
- fire
initiative:
  bonus: 0
senses:
  darkvision: 60
  tremorsense: 30
AC:
  AC: 15
  touch: 10
  flat_footed: 15
  components:
    natural: 5
HP:
  HP: 27
  long: 5d8+5
saves:
  fort: 2
  ref: 1
  will: 5
defensive_abilities:
- molten heart
immunities:
- fire
- undead traits
weaknesses:
- vulnerable to cold
speeds:
  base: 20
attacks:
  melee:
  - - text: slam +6 (1d4+4 plus burn)
      entries:
      - - damage: 1d4+4
        - effect: burn
      attack: slam
      bonus:
      - 6
  ranged:
  - - text: lava ball +3 ranged touch (1d6 fire plus burn)
      entries:
      - - damage: 1d6
          type: fire
        - effect: burn
      attack: lava ball
      bonus:
      - 3
      touch: true
  special:
  - burn (1d6, DC 13)
  - eruption
  - lava ball
spell_like_abilities:
  entries:
  - name: pyrotechnics
    source: default
    freq: 5/day
  - name: burning hands
    source: default
    freq: 3/day
    DC: 12
  sources:
  - name: default
    CL: 5
    concentration: 6
ability_scores:
  STR: 16
  DEX: 10
  CON:
  INT: 8
  WIS: 13
  CHA: 12
BAB: 3
CMB: 6
CMB_other: +8 bull rush
CMD: 16
CMD_other: 18 vs. bull rush
feats:
- name: Blind-Fight
- name: Improved Bull Rush
- name: Power Attack
skills:
  Craft (any): 6
  Intimidate: 9
  Perception: 9
languages:
- Dwarven
- Ignan
ecology:
  environment: any mountains or underground
  organization: solitary, pair, or flow (3-8)
  treasure_type: standard
special_abilities:
  Lava Ball (Su): As a full-round action, a fellsig can regurgitate a ball of lava
    into its fist and hurl it with a range increment of 30 feet. Any creature struck
    must succeed at a DC 13 Reflex save or catch fire and take 1d6 points of fire
    damage at the start of its turn for an additional 1d4 rounds. The save DC is Charisma-based.
  Molten Heart (Ex): Beneath the slabs of igneous rock that compose a fellsig's body
    are organs of superheated rock and fumes. A creature that confirms a critical
    hit against a fellsig in melee is struck by a jet of flaming ash that deals 2d6
    points of fire damage (Reflex DC 13 half).
desc_long: |-
  First created in catastrophic event known as the Rending, the molten undead known as fellsigs have wandered Darkmoon Vale for centuries. When Droskar's Crag erupted and buried entire dwarven settlements under choking ash, boiling mud, noxious fumes, and seething magma, the violence and suffering caused many of the volcano's victims to rise after death, cursed to visit their own fiery deaths upon the living. Fellsigs are made up of the very materials that took their lives, and their existence is a constant reminder of all that was lost in the fiery cataclysm of the Rending. Most fellsigs are morose creatures, bemoaning the destruction of their homeland and carrying on a shadowy imitation of their former lives amid the scorched ruins they inhabit. The sight of life and joy often enrages them with vindictive jealousy for those spared the fellsigs' own cruel fate.

  Fellsigs have sympathy for those exhibiting obvious signs of burn damage, however, and using the Diplomacy skill can sometimes convince these stony, smoldering monsters to aid such creatures. Similarly, fellsigs hold no special hatred for creatures of the fire subtype, and on occasion they can be convinced to serve such creatures as guards or even artisans, though such alliances are tenuous at best.

---

# Fellsig
This squat figure’s rough-hewn visage is frozen in a _[[items/Mundane/Mask|mask]]_ of pain, while the cracks in its dark stone body glow with a fiery inner _[[universal monster rules/Heat|heat]]_.
**Source** Andoran, Birthplace of _[[spells/Freedom|Freedom]]_ pg. 55
**XP** 800

NE Medium undead (fire)
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Tremorsense|tremorsense]]_ 30 ft.; Perception +9

##### Defense

**AC** 15, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+5 natural)
**hp** 27 (5d8+5)
**Fort** +2, **Ref** +1, **Will** +5
**Defensive Abilities** molten heart; **Immune** fire, _[[universal monster rules/Undead Traits|undead traits]]_
**Weaknesses** vulnerable to cold

##### Offense
**Speed** 20 ft.
**Melee** slam +6 (1d4+4 plus _[[universal monster rules/Burn|burn]]_)
**Ranged** lava ball +3 ranged touch (1d6 fire plus _burn_)
**Special Attacks** _burn_ (1d6, DC 13), eruption, lava ball
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +6)
5/day—_[[spells/Pyrotechnics|pyrotechnics]]_
3/day—_[[spells/Burning Hands|burning hands]]_ (DC 12)

##### Statistics
**Str** 16, **Dex** 10, **Con** —, **Int** 8, **Wis** 13, **Cha** 12
**Base Atk** +3; **CMB** +6 (+8 bull rush); **CMD** 16 (18 vs. bull rush)
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Craft (any) +6, Intimidate +9, Perception +9
**Languages** Dwarven, Ignan

##### Ecology

**Environment** any mountains or underground
**Organization** solitary, pair, or flow (3–8)
**Treasure** standard

### Special Abilities

**Lava Ball (Su)** As a full-round action, a _[[monsters/Fellsig|fellsig]]_ can regurgitate a ball of lava into its fist and hurl it with a range increment of 30 feet. Any creature struck must succeed at a DC 13 Reflex save or catch fire and take 1d6 points of fire damage at the start of its turn for an additional 1d4 rounds. The save DC is Charisma-based.

**Molten Heart (Ex)** Beneath the slabs of igneous rock that compose a _fellsig_’s body are organs of superheated rock and fumes. A creature that confirms a critical hit against a _fellsig_ in melee is struck by a _[[universal monster rules/Jet|jet]]_ of _[[items/Weapon Magic Abilities/Flaming|flaming]]_ ash that deals 2d6 points of fire damage (Reflex DC 13 half).

##### Description

First created in catastrophic event known as the Rending, the molten undead known as fellsigs have wandered Darkmoon Vale for centuries. When Droskar’s Crag erupted and buried entire dwarven settlements under choking ash, boiling mud, noxious fumes, and seething magma, the violence and suffering caused many of the volcano’s victims to rise after death, cursed to visit their own fiery deaths upon the living. Fellsigs are made up of the very materials that took their lives, and their existence is a constant reminder of all that was lost in the fiery cataclysm of the Rending. Most fellsigs are morose creatures, bemoaning the _[[spells/Destruction|destruction]]_ of their homeland and carrying on a shadowy imitation of their former lives amid the scorched ruins they inhabit. The sight of life and joy often enrages them with vindictive jealousy for those spared the fellsigs’ own _[[items/Weapon Magic Abilities/Cruel|cruel]]_ fate.

Fellsigs have _[[spells/Sympathy|sympathy]]_ for those exhibiting obvious signs of _burn_ damage, however, and using the Diplomacy skill can sometimes convince these stony, smoldering monsters to aid such creatures. Similarly, fellsigs hold no special hatred for creatures of the fire subtype, and on occasion they can be convinced to serve such creatures as guards or even artisans, though such alliances are tenuous at best.
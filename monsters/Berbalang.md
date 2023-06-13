---
cssclass: [monsters]
title1: Berbalang
desc_short: This hunched, bat-winged horror moves with an uncanny grace, its glowing
  eyes and long tongue presenting a frightening visage.
title2: Berbalang
CR: 6
sources:
- name: Bestiary 3
  page: 40
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 2400
alignment: CE
size: Medium
type: undead
initiative:
  bonus: 4
senses:
  darkvision: 60
AC:
  AC: 20
  touch: 15
  flat_footed: 15
  components:
    dex: 4
    dodge: 1
    natural: 5
HP:
  HP: 68
  long: 8d8+32
saves:
  fort: 6
  ref: 6
  will: 9
defensive_abilities:
- projection
DR:
- amount: 10
  weakness: good or silver
immunities:
- undead traits
speeds:
  base: 40
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 1 bite +9 (1d6+3 plus paralysis)
      entries:
      - - damage: 1d6+3
        - effect: paralysis
      count: 1
      attack: bite
      bonus:
      - 9
    - text: 2 claws +9 (1d6+3 plus paralysis)
      entries:
      - - damage: 1d6+3
        - effect: paralysis
      count: 2
      attack: claws
      bonus:
      - 9
  - - text: incorporeal touch +10 (1d4 Con damage)
      entries:
      - - damage: 1d4
          type: Con damage
      attack: incorporeal touch
      bonus:
      - 10
  special:
  - paralysis (1d4+1 rounds, DC 18)
spell_like_abilities:
  entries:
  - name: bleed
    source: default
    freq: At will
  - name: ghost sound
    source: default
    freq: At will
    DC: 14
  - name: alter self
    source: default
    freq: 3/day
  - name: charm person
    source: default
    freq: 3/day
    DC: 15
  sources:
  - name: default
    CL: 9
    concentration: 13
ability_scores:
  STR: 17
  DEX: 19
  CON:
  INT: 13
  WIS: 16
  CHA: 18
BAB: 6
CMB: 9
CMD: 26
feats:
- name: Defensive Combat Training
- name: Dodge
- name: Flyby Attack
- name: Mobility
skills:
  Bluff: 10
  Escape Artist: 10
  Fly: 17
  Knowledge (local): 5
  Knowledge (religion): 6
  Perception: 14
  Stealth: 15
languages:
- Common
ecology:
  environment: any land
  organization: solitary or pack (2-8)
  treasure_type: standard
special_abilities:
  Projection (Su): 'Once per day as a full-round action, a berbalang can enter a trance
    that separates the creature's spirit from its body. This splits the berbalang's
    current hit points in half between its body and its spirit. The berbalang's spirit
    body gains the incorporeal subtype and special ability; otherwise, it retains
    the same statistics as its physical self with the following changes: AC 19, touch
    19, flat-footed 14 (+4 Dex, +4 deflection, +1 dodge), single incorporeal touch
    attack that deals 1d4 Constitution damage on a hit as its sole attack. This spirit
    projection can travel no more than 1 mile away from the berbalang's body. Because
    the creature is only partially in existence when in this state, its body gains
    displacement as the spell. When separated in this way, the berbalang's body is
    unconscious and helpless. If the berbalang's body is injured while in this state,
    the separated projection immediately returns to its body, and the body loses displacement.
    If the physical body is slain, the spirit body immediately dies as well. If the
    spirit is reduced to 0 or fewer hit points, it returns to the body immediately.
    A berbalang in spirit form can end the effect at any time as a standard action,
    at which point the spirit immediately returns to the body. When a berbalang's
    spirit form returns to the body, add both the spirit body's hit points and the
    physical body's hit points back together to determine the creature's current hit
    point total.'
desc_long: Berbalangs prefer to make their homes within a day's travel of humanoid
  settlements. These lairs are well hidden and sometimes protected by other undead
  creatures. Some berbalangs set themselves up as secluded shamans or wise old crones,
  using alter self to appear human. Ultimately cowardly, berbalangs rarely attack
  a settlement directly, preferring to pluck its meals from those who stray too far
  from civilization. A berbalang stands as tall as a human and rarely weighs more
  than 100 pounds.

---

# Berbalang
This hunched, bat-winged horror moves with an uncanny _[[spells/Grace|grace]]_, its glowing eyes and long tongue presenting a frightening visage.
**Source** Bestiary 3 pg. 40
**XP** 2,400
CE Medium undead
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +14

##### Defense

**AC** 20, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 Dex, +1 _[[feats/Dodge|dodge]]_, +5 natural)
**hp** 68 (8d8+32)
**Fort** +6, **Ref** +6, **Will** +9
**Defensive Abilities** projection; **DR** 10/good or silver; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 40 ft., fly 60 ft. (good)
**Melee** 1 bite +9 (1d6+3 plus _[[universal monster rules/Paralysis|paralysis]]_), 2 claws +9 (1d6+3 plus _paralysis_) or _[[universal monster rules/Incorporeal|incorporeal]]_ touch +10 (1d4 Con damage)
**Special Attacks** _paralysis_ (1d4+1 rounds, DC 18)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +13)
At will—_[[universal monster rules/Bleed|bleed]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 14)
3/day—_[[spells/Alter Self|alter self]]_, _[[spells/Charm Person|charm person]]_ (DC 15)

##### Statistics
**Str** 17, **Dex** 19, **Con** —, **Int** 13, **Wis** 16, **Cha** 18
**Base Atk** +6; **CMB** +9; **CMD** 26
**Feats** _[[feats/Defensive Combat Training|Defensive Combat Training]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Mobility|Mobility]]_
**Skills** Bluff +10, Escape Artist +10, Fly +17, Knowledge (local) +5, Knowledge (religion) +6, Perception +14, Stealth +15
**Languages** Common

##### Ecology

**Environment** any land
**Organization** solitary or pack (2–8)
**Treasure** standard

### Special Abilities

**Projection (Su)** Once per day as a full-round action, a _[[monsters/Berbalang|berbalang]]_ can enter a trance that separates the creature’s spirit from its body. This splits the _berbalang_’s current hit points in half between its body and its spirit. The _berbalang_’s spirit body gains the _incorporeal_ subtype and special ability; otherwise, it retains the same statistics as its physical self with the following changes: AC 19, touch 19, _flat-footed_ 14 (+4 Dex, +4 _[[spells/Deflection|deflection]]_, +1 _dodge_), single _incorporeal_ touch attack that deals 1d4 Constitution damage on a hit as its sole attack. This spirit projection can travel no more than 1 mile away from the _berbalang_’s body. Because the creature is only partially in existence when in this state, its body gains _[[spells/Displacement|displacement]]_ as the spell. When separated in this way, the _berbalang_’s body is _[[conditions/Unconscious|unconscious]]_ and _[[conditions/Helpless|helpless]]_. If the _berbalang_’s body is injured while in this state, the separated projection immediately returns to its body, and the body loses _displacement_. If the physical body is slain, the spirit body immediately dies as well. If the spirit is reduced to 0 or fewer hit points, it returns to the body immediately. A _berbalang_ in spirit form can end the effect at any time as a standard action, at which point the spirit immediately returns to the body. When a _berbalang_’s spirit form returns to the body, add both the spirit body’s hit points and the physical body’s hit points back together to determine the creature’s current hit point total.

##### Description

Berbalangs prefer to make their homes within a day’s travel of humanoid settlements. These lairs are well hidden and sometimes protected by other undead creatures. Some berbalangs set themselves up as secluded shamans or wise old crones, using _alter self_ to appear human. Ultimately cowardly, berbalangs rarely attack a settlement directly, preferring to pluck its meals from those who stray too far from civilization. A _berbalang_ stands as tall as a human and rarely weighs more than 100 pounds.
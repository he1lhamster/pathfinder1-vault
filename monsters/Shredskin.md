---
cssclass: [monsters]
title1: Shredskin
desc_short: This floating creature looks like an orc's animate, hollow skin. Its upper
  half is intact, but its lower half is in tatters.
title2: Shredskin
CR: 2
sources:
- name: Bestiary 4
  page: 243
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 600
alignment: NE
size: Small
type: undead
initiative:
  bonus: 2
senses:
  darkvision: 60
  detect undead: true
AC:
  AC: 14
  touch: 13
  flat_footed: 12
  components:
    dex: 2
    natural: 1
    size: 1
HP:
  HP: 22
  long: 4d8+4
saves:
  fort: 2
  ref: 3
  will: 4
defensive_abilities:
- amorphous
immunities:
- undead traits
speeds:
  fly: 40
  fly_maneuverability: average
attacks:
  melee:
  - - text: bite +6 (1d4)
      entries:
      - - damage: 1d4
      attack: bite
      bonus:
      - 6
    - text: 2 claws +6 (1d4 plus grab)
      entries:
      - - damage: 1d4
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 6
  special:
  - constrict (1d4)
  - control body
  - enshroud
  - grab (Medium)
spell_like_abilities:
  entries:
  - name: detect undead
    source: default
    freq: Constant
  - name: command undead
    source: default
    freq: 1/day
    DC: 13
  sources:
  - name: default
    CL: 3
    concentration: 4
ability_scores:
  STR: 10
  DEX: 15
  CON:
  INT: 6
  WIS: 10
  CHA: 13
BAB: 3
CMB: 4
CMB_other: +8 grapple
CMD: 14
CMD_other: can't be tripped
feats:
- name: Agile Maneuvers
- name: Weapon Finesse
skills:
  Fly: 4
  Perception: 7
  Stealth: 13
languages:
- Common (can't speak)
special_qualities:
- compression
ecology:
  environment: any land
  organization: solitary or pack (2-5)
  treasure_type: incidental
special_abilities:
  Control Body (Su): A shredskin can wrap itself around a corpse (or a corporeal undead
    it controls using command undead). When wrapping a host body in this way, the
    shredskin gains Strength 14 or the host body's Strength, whichever is higher,
    but cannot use its grab or enshroud abilities which doing so. Attacks targeted
    at the shredskin deal half damage to it and half damage to the host body; area
    attacks deal normal damage to both the shredskin and its host. If the host is
    destroyed, the shredskin unwraps itself as a free action on its next turn. A typical
    Medium corpse has 15 hit points for this purpose, while a Small corpse has 10
    hit points. A shredskin can only use this ability on a generally humanoid-shaped
    creature (two arms, one head, humanoid torso) of Medium or Small size.
  Enshroud (Ex): A shredskin that successfully pins a creature can wrap itself around
    that target like a shirt. The target gains the pinned condition, but the shredskin
    has neither the grappled or pinned condition, and can move itself and the target
    as if it controlled the target's body. The shredskin deals constrict damage to
    the target on its turn each round (no combat maneuver check needed). Attacking
    the shredskin while it's using this ability damages both it and the target as
    described in the control body ability. The shredskin can release the target as
    a free action.
desc_long: |-
  A shredskin is a wretched undead creature created either when a humanoid is skinned alive to be preserved as a trophy or otherwise killed in a terrifying way that leaves much of its upper half unharmed, such as being dissolved feet-first in acid. A fragment of the creature's soul animates the skin and seeks vengeance on those who created it, all the while trying to find a comfortable body for it to use as it did when it was alive. A shredskin may attack on its own and try to squeeze the life out of a living humanoid to use it as a body, or it might control another undead such as a skeleton, zombie, or ghoul, covering it like a morbid costume. In either case, it abandons its borrowed body if it finds a better one or the old one is destroyed. A shredskin is usually recognizable by creatures who knew it in life.

  Because it lacks a lower half, a shredskin is 3-4 feet tall and weighs only 10-15 pounds.

---

# Shredskin
This floating creature looks like an _[[monsters/Orc|orc]]_’s animate, hollow skin. Its upper half is intact, but its lower half is in tatters.
**Source** Bestiary 4 pg. 243
**XP** 600

NE Small undead
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Undead|detect undead]]_; Perception +7

##### Defense

**AC** 14, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+2 Dex, +1 natural, +1 size)
**hp** 22 (4d8+4)
**Fort** +2, **Ref** +3, **Will** +4
**Defensive Abilities** _[[universal monster rules/Amorphous|amorphous]]_; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** fly 40 ft. (average)
**Melee** bite +6 (1d4), 2 claws +6 (1d4 plus _[[universal monster rules/Grab|grab]]_)
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (1d4), control body, enshroud, _grab_ (Medium)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd; concentration +4)
Constant—_detect undead_
1/day—_[[spells/Command Undead|command undead]]_ (DC 13)

##### Statistics
**Str** 10, **Dex** 15, **Con** —, **Int** 6, **Wis** 10, **Cha** 13
**Base Atk** +3; **CMB** +4 (+8 grapple); **CMD** 14 (can’t be tripped)
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Fly +4, Perception +7, Stealth +13
**Languages** Common (can’t speak)
**SQ** _[[universal monster rules/Compression|compression]]_

##### Ecology

**Environment** any land
**Organization** solitary or pack (2–5)
**Treasure** incidental

### Special Abilities

**Control Body (Su)** A _[[monsters/Shredskin|shredskin]]_ can wrap itself around a corpse (or a corporeal undead it controls using _command undead_). When wrapping a host body in this way, the _shredskin_ gains Strength 14 or the host body’s Strength, whichever is higher, but cannot use its _grab_ or enshroud abilities which doing so. Attacks targeted at the _shredskin_ deal half damage to it and half damage to the host body; area attacks deal normal damage to both the _shredskin_ and its host. If the host is destroyed, the _shredskin_ unwraps itself as a free action on its next turn. A typical _Medium_ corpse has 15 hit points for this purpose, while a Small corpse has 10 hit points. A _shredskin_ can only use this ability on a generally humanoid-shaped creature (two arms, one head, humanoid torso) of _Medium_ or Small size.

**Enshroud (Ex)** A _shredskin_ that successfully pins a creature can wrap itself around that target like a shirt. The target gains the _[[conditions/Pinned|pinned]]_ condition, but the _shredskin_ has neither the _[[conditions/Grappled|grappled]]_ or _pinned_ condition, and can move itself and the target as if it controlled the target’s body. The _shredskin_ deals _constrict_ damage to the target on its turn each round (no combat maneuver check needed). Attacking the _shredskin_ while it’s using this ability damages both it and the target as described in the control body ability. The _shredskin_ can release the target as a free action.

##### Description

A _shredskin_ is a wretched undead creature created either when a humanoid is skinned alive to be preserved as a trophy or otherwise killed in a terrifying way that leaves much of its upper half unharmed, such as being dissolved feet-first in acid. A fragment of the creature’s soul animates the skin and seeks _[[feats/Vengeance|vengeance]]_ on those who created it, all the while trying to find a comfortable body for it to use as it did when it was alive. A _shredskin_ may attack on its own and try to _[[spells/Squeeze|squeeze]]_ the life out of a living humanoid to use it as a body, or it might control another undead such as a skeleton, zombie, or _[[monsters/Ghoul|ghoul]]_, covering it like a morbid costume. In either case, it abandons its borrowed body if it finds a better one or the old one is destroyed. A _shredskin_ is usually recognizable by creatures who knew it in life.

Because it lacks a lower half, a _shredskin_ is 3–4 feet tall and weighs only 10–15 pounds.
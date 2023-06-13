---
cssclass: [monsters]
title1: Azgenzak
desc_short: 'This undulating, amorphous sac is a turgid, brown-black mass scarcely
  hiding a seething jumble of rounded subcutaneous masses churning within. One end
  opens into a yawning maw, revealing a fiery cauldron of innumerable, lidless eyeballs
  of every size, shape, and color, each wreathed in sooty orange flame. '
title2: Azgenzak
CR: 8
sources:
- name: 'Pathfinder #69: Maiden, Mother, Crone'
  page: 82
  link: http://paizo.com/products/btpy8xbz?Pathfinder-Adventure-Path-69-Maiden-Mother-Crone
XP: 4800
alignment: NE
size: Large
type: aberration
subtypes:
- aquatic
initiative:
  bonus: 3
senses:
  all-around vision: true
  darkvision: 60
  low-light vision: true
auras:
- name: frightful presence
  radius: 30
  DC: 16
  other:
  - inverted form only
AC:
  AC: 22
  touch: 12
  flat_footed: 19
  components:
    dex: 3
    natural: 10
    size: -1
HP:
  HP: 95
  long: 10d8+50
saves:
  fort: 8
  ref: 6
  will: 8
defensive_abilities:
- amorphous
immunities:
- fire
- poison
speeds:
  base: 20
  swim: 20
attacks:
  melee:
  - - text: 3 slams +11 (1d6+4 plus burn and grab)
      entries:
      - - damage: 1d6+4
        - effect: burn
        - effect: grab
      count: 3
      attack: slams
      bonus:
      - 11
  special:
  - burn (1d6, DC 20)
  - burning blindness
  - constrict (1d6+4)
  - swallow whole (2d6 fire, AC 15, 9 hp)
  - swarming pyrocules
space: 10
reach: 5
ability_scores:
  STR: 18
  DEX: 17
  CON: 20
  INT: 7
  WIS: 13
  CHA: 12
BAB: 7
CMB: 12
CMB_other: +16 grapple
CMD: 25
feats:
- name: Blind-Fight
- name: Nimble Moves
- name: Skill Focus (Perception)
- name: Step Up
- name: Weapon Focus (slam)
skills:
  Climb: 8
  Perception: 20
  Stealth: 10
    when underwater: 18
  Swim: 16
  _racial_mods:
    Stealth:
      when underwater: 8
languages:
- Aklo
special_qualities:
- amphibious
- compression
- inversion
ecology:
  environment: warm and temperate fresh water and swamps
  organization: solitary
  treasure_type: incidental
special_abilities:
  Burning Blindness (Su): When an azgenzak confirms a critical hit or a creature fails
    its save against the distraction attack of its swarming pyrocules, the azgenzak
    attempts to pluck out one of the target's eyes (Fortitude DC 20 negates). If the
    save fails, the target takes 1d6 additional points of fire damage, is sickened
    by pain for 1d4 rounds, and becomes permanently dazzled. If this results in the
    loss of all of the target's eyes, it is permanently blinded.
  Inversion (Ex): As a move action, an azgenzak can invert its sac-like body, turning
    itself inside out and exposing its innumerable burning eyes. Doing so surrounds
    the azgenzak with a fiery aura and activates its frightful presence ability. These
    abilities are suppressed when the azgenzak is not inverted. When it's inverted,
    creatures adjacent to the azgenzak take 2d6 points of fire damage and risk catching
    on fire. A successful DC 16 Reflex save halves this damage and keeps the creature
    from catching on fire. An inverted azgenzak loses its racial bonus to Stealth
    underwater and takes a further -10 penalty on Stealth checks. In addition, when
    inverted, an azgenzak can't swallow its victim whole; however, if it begins its
    turn with a creature grappled, it can revert itself as a move action and then
    use its swallow whole ability. A creature swallowed by an azgenzak is subject
    to its fiery aura and frightful presence even when the azgenzak is not inverted.
  Swarming Pyrocules (Su): As a full-round action, an azgenzak can disgorge a swarm
    of burning eyeballs. This swarm has the same statistics as a bat swarm (Pathfinder
    RPG Bestiary 30), except it lacks the wounding special ability, which is replaced
    by the azgenzak's burn ability and immunity to fire. An azgenzak using this ability
    takes 2d6 points of damage (though damage dealt to the swarming pyrocules does
    not damage the azgenzak). The swarming pyrocules can't survive long separated
    from the azgenzak, and take 1 point of damage each round at the end of its turn.
    The swarming pyrocules can be reabsorbed by the azgenzak as a full-round action,
    healing the creature of 1d6 points of damage.
desc_long: 'Azgenzaks, also called more prosaically “sacks of burning eyes,” are shapeless
  predators of unfathomable appetites and undeniable malevolence. They might have
  congealed into existence within some forgotten crack of the Outer Rifts, escaping
  (or being set loose) into the Material Plane ages ago. However, many theorize that
  these beings are entirely natural, primeval creatures that fell into savagery or
  never evolved from their primitive state in the first place. Azgenzaks are roughly
  8 feet in diameter and weigh over 800 pounds. '

---

# Azgenzak
This undulating, _[[universal monster rules/Amorphous|amorphous]]_ sac is a turgid, brown-black mass
scarcely hiding a seething jumble of rounded subcutaneous
masses churning within. One end opens into a yawning maw,
revealing a fiery _[[items/Mundane/Cauldron|cauldron]]_ of innumerable, lidless eyeballs of
every size, shape, and color, each wreathed in sooty orange flame.

**Source** Pathfinder #69: Maiden, Mother, Crone pg. 82
**XP** 4,800

NE Large aberration (aquatic)
**Init** +3; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[spells/Darkvision|darkvision]]_ 60 ft., low-light
_[[spells/Vision|vision]]_; Perception +20
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (30 ft., DC 16, inverted form only)

##### Defense

**AC** 22, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+3 Dex, +10 natural, –1 size)
**hp** 95 (10d8+50)
**Fort** +8, **Ref** +6, **Will** +8
**Defensive Abilities** _amorphous_; **Immune** fire, poison

##### Offense
**Speed** 20 ft., swim 20 ft.
**Melee** 3 slams +11 (1d6+4 plus _[[universal monster rules/Burn|burn]]_ and _[[universal monster rules/Grab|grab]]_)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** _burn_ (1d6, DC 20), _[[items/Weapon Magic Abilities/Burning|burning]]_ blindness,
_[[universal monster rules/Constrict|constrict]]_ (1d6+4), _[[universal monster rules/Swallow Whole|swallow whole]]_ (2d6 fire, AC 15, 9 hp),
swarming pyrocules

##### Statistics
**Str** 18, **Dex** 17, **Con** 20, **Int** 7, **Wis** 13, **Cha** 12
**Base Atk** +7; **CMB** +12 (+16
grapple); **CMD** 25
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, Nimble
Moves, _[[feats/Skill Focus|Skill Focus]]_
(Perception), _[[feats/Step Up|Step Up]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (slam)
**Skills** _[[universal monster rules/Climb|Climb]]_ +8, Perception +20, Stealth +10 (+18 when
_[[items/Weapon Magic Abilities/Underwater|underwater]]_), Swim +16; **Racial Modifiers** +8 Stealth when
_underwater_
**Languages** Aklo
**SQ** _[[universal monster rules/Amphibious|amphibious]]_, _[[universal monster rules/Compression|compression]]_, inversion

##### Ecology

**Environment** warm and temperate fresh water and swamps
**Organization** solitary
**Treasure** incidental

### Special Abilities

**_Burning_ Blindness (Su)** When an _[[monsters/Azgenzak|azgenzak]]_ confirms a critical
hit or a creature fails its save against the _[[universal monster rules/Distraction|distraction]]_ attack
of its swarming pyrocules, the _azgenzak_ attempts to pluck
out one of the target’s eyes (Fortitude DC 20 negates). If
the save fails, the target takes 1d6 additional points of fire
damage, is _[[conditions/Sickened|sickened]]_ by pain for 1d4 rounds, and becomes
permanently _[[conditions/Dazzled|dazzled]]_. If this results in the loss of all of the
target’s eyes, it is permanently _[[conditions/Blinded|blinded]]_.

**Inversion (Ex)** As a move action, an _azgenzak_ can invert its
sac-like body, turning itself inside out and exposing its
innumerable _burning_ eyes. Doing so surrounds the _azgenzak_
with a fiery aura and activates its _frightful presence_ ability.
These abilities are suppressed when the _azgenzak_ is not
inverted. When it’s inverted, creatures adjacent to the
_azgenzak_ take 2d6 points of fire damage and risk catching
on fire. A successful DC 16 Reflex save halves this damage
and keeps the creature from catching on fire. An inverted
_azgenzak_ loses its racial bonus to Stealth _underwater_ and
takes a further –10 penalty on Stealth checks. In addition,
when inverted, an _azgenzak_ can’t swallow its victim whole;
however, if it begins its turn with a creature _[[conditions/Grappled|grappled]]_, it
can revert itself as a move action and then use its swallow
whole ability. A creature swallowed by an _azgenzak_ is
subject to its fiery aura and _frightful presence_ even when
the _azgenzak_ is not inverted.
**Swarming Pyrocules (Su)** As a full-round action, an
_azgenzak_ can disgorge a swarm of _burning_
eyeballs. This swarm has the same
statistics as a bat swarm (Pathfinder
RPG Bestiary 30), except
it lacks the _[[items/Weapon Magic Abilities/Wounding|wounding]]_
special ability, which
is replaced by
the _azgenzak_’s
_burn_ ability and
_[[universal monster rules/Immunity|immunity]]_ to fire.
An _azgenzak_
using this
ability takes
 2d6 points of
damage (though
damage dealt
to the swarming
pyrocules does not damage the _azgenzak_). The swarming
pyrocules can’t survive long separated from the _azgenzak_,
and take 1 point of damage each round at the end of its
turn. The swarming pyrocules can be reabsorbed by the
_azgenzak_ as a full-round action, healing the creature of 1d6
points of damage.

##### Description

Azgenzaks, also _[[items/Weapon Magic Abilities/Called|called]]_ more prosaically “sacks of _burning_
eyes,” are shapeless predators of unfathomable appetites
and undeniable malevolence. They might have congealed
into existence within some forgotten crack of the Outer
Rifts, escaping (or being set loose) into the Material Plane
ages ago. However, many theorize that these beings are
entirely natural, primeval creatures that fell into savagery
or never evolved from their primitive state in the first
place. Azgenzaks are roughly 8 feet in diameter and weigh
over 800 pounds.
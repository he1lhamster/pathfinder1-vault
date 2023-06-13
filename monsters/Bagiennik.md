---
cssclass: [monsters]
title1: Bagiennik
desc_short: This small, lizardlike creature has a humanoid upper body and a long tail
  with frilled extensions.
title2: Bagiennik
CR: 6
sources:
- name: Bestiary 5
  page: 40
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 2400
alignment: CN
size: Small
type: fey
subtypes:
- aquatic
initiative:
  bonus: 2
senses:
  disease scent: true
AC:
  AC: 17
  touch: 13
  flat_footed: 15
  components:
    dex: 2
    natural: 4
    size: 1
HP:
  HP: 66
  long: 12d6+24
saves:
  fort: 5
  ref: 10
  will: 8
DR:
- amount: 5
  weakness: cold iron
resistances:
  acid: 5
  fire: 5
speeds:
  base: 30
  swim: 40
attacks:
  melee:
  - - text: 2 claws +9 (1d4-1)
      entries:
      - - damage: 1d4-1
      count: 2
      attack: claws
      bonus:
      - 9
  ranged:
  - - text: nasal spray +10 touch (3d6 fire, 3d6 acid, and nasal burn)
      entries:
      - - damage: 3d6
          type: fire
        - damage: 3d6
          type: acid
        - effect: nasal burn
      attack: nasal spray
      bonus:
      - 10
      touch: true
spell_like_abilities:
  entries:
  - name: cure light wounds
    source: default
    freq: 3/day
  - name: remove disease
    source: default
    freq: 3/day
  - name: cure moderate wounds
    source: default
    freq: 1/day
  - name: remove blindness/deafness
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 7
    concentration: 10
ability_scores:
  STR: 8
  DEX: 14
  CON: 13
  INT: 15
  WIS: 10
  CHA: 17
BAB: 6
CMB: 4
CMD: 16
feats:
- name: Alertness
- name: Self-Sufficient
- name: Skill Focus (Heal)
- name: Toughness
- name: Weapon Finesse
- name: Weapon Focus (nasal spray)
skills:
  Bluff: 10
  Diplomacy: 12
  Escape Artist: 9
  Heal: 22
  Knowledge (arcana): 5
  Knowledge (nature): 12
  Perception: 19
  Sense Motive: 11
  Stealth: 21
  Survival: 8
  Swim: 22
  Use Magic Device: 18
languages:
- Common
- Sylvan
special_qualities:
- amphibious
ecology:
  environment: cold rivers
  organization: solitary, pair, or gang (3-8)
  treasure_type: none
special_abilities:
  Disease Scent (Ex): A bagiennik can smell a diseased creature as if using the scent
    ability. It can discern whether the diseased creature is the source of a disease
    or merely a carrier; in the latter case, the bagiennik often seeks out the creature
    and attempts to purge its maladies.
  Nasal Burn (Su): A bagiennik's nasal spray deals 1d6 points of fire damage to victims
    in subsequent rounds after it strikes a target (as per the burn universal monster
    ability), but it can also cure other maladies. Each round in which a victim takes
    damage from a bagiennik's nasal spray, that victim can attempt a DC 17 Fortitude
    save. If the victim succeeds at this save, it heals 1 point of ability damage
    to an ability score of its choice. If the result exceeds the DC by 5 or more,
    the victim can also attempt to remove a single disease or poison currently affecting
    her as per remove disease or neutralize poison (caster level 7th). If the damage
    from the bagiennik's nasal burn is reduced or negated in any way, the victim can't
    attempt this special Fortitude save that round. The save DC is Constitution-based.
desc_long: |-
  Bagienniks are small, amphibious fey that hide in tall reeds along rivers. They frequently dig into the silt beneath the pools of hot springs, where they take long naps in the warm and comforting waters and play pranks on foolish bathers who swim too close to the bagienniks' hiding spots. Despite their capricious nature, the creatures are sought for their healing abilities. They delight in curing maladies and burning away infirmities with their caustic nasal spray.

  A local bagiennik is considered a boon in many river towns. Citizens of such settlements often venture to the rivers with offerings, hoping to encourage the fey to stay close and heal their families. A bagiennik that finds a generous town might invite its extended family to settle in, testing the patience and largesse of its hosts.

---

# Bagiennik
This small, lizardlike creature has a humanoid upper body and a long tail with frilled extensions.
**Source** Bestiary 5 pg. 40
**XP** 2,400

CN Small fey (aquatic)
**Init** +2; **Senses** disease _[[universal monster rules/Scent|scent]]_; Perception +19

##### Defense

**AC** 17, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+2 Dex, +4 natural, +1 size)
**hp** 66 (12d6+24)
**Fort** +5, **Ref** +10, **Will** +8
**DR** 5/cold iron; **Resist** acid 5, fire 5

##### Offense
**Speed** 30 ft., swim 40 ft.
**Melee** 2 claws +9 (1d4-1)
**Ranged** nasal spray +10 touch (3d6 fire, 3d6 acid, and nasal _[[universal monster rules/Burn|burn]]_)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +10)
3/day—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Remove Disease|remove disease]]_
1/day—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_, remove blindness/deafness

##### Statistics
**Str** 8, **Dex** 14, **Con** 13, **Int** 15, **Wis** 10, **Cha** 17
**Base Atk** +6; **CMB** +4; **CMD** 16
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Self-Sufficient|Self-Sufficient]]_, _[[feats/Skill Focus|Skill Focus]]_ (_[[spells/Heal|Heal]]_), _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (nasal spray)
**Skills** Bluff +10, Diplomacy +12, Escape Artist +9, _Heal_ +22, Knowledge (arcana) +5, Knowledge (nature) +12, Perception +19, Sense Motive +11, Stealth +21, Survival +8, Swim +22, Use Magic Device +18
**Languages** Common, Sylvan
**SQ** _[[universal monster rules/Amphibious|amphibious]]_

##### Ecology

**Environment** cold rivers
**Organization** solitary, pair, or gang (3-8)
**Treasure** none

### Special Abilities

**Disease _Scent_ (Ex)** A _[[monsters/Bagiennik|bagiennik]]_ can smell a diseased creature as if using the _scent_ ability. It can discern whether the diseased creature is the source of a disease or merely a carrier; in the latter case, the _bagiennik_ often seeks out the creature and attempts to purge its maladies.

**Nasal _Burn_ (Su)** A _bagiennik_’s nasal spray deals 1d6 points of fire damage to victims in subsequent rounds after it strikes a target (as per the _burn_ universal monster ability), but it can also cure other maladies. Each round in which a victim takes damage from a _bagiennik_’s nasal spray, that victim can attempt a DC 17 Fortitude save. If the victim succeeds at this save, it heals 1 point of ability damage to an ability score of its choice. If the result exceeds the DC by 5 or more, the victim can also attempt to remove a single disease or poison currently affecting her as per _remove disease_ or _[[spells/Neutralize Poison|neutralize poison]]_ (caster level 7th). If the damage from the _bagiennik_’s nasal _burn_ is reduced or negated in any way, the victim can’t attempt this special Fortitude save that round. The save DC is Constitution-based.

##### Description

Bagienniks are small, _amphibious_ fey that hide in tall reeds along rivers. They frequently dig into the silt beneath the pools of hot springs, where they take long naps in the warm and comforting waters and play pranks on foolish bathers who swim too close to the bagienniks’ hiding spots. Despite their capricious nature, the creatures are sought for their healing abilities. They delight in curing maladies and _[[items/Weapon Magic Abilities/Burning|burning]]_ away infirmities with their caustic nasal spray.

A local _bagiennik_ is considered a boon in many river towns. Citizens of such settlements often venture to the rivers with offerings, hoping to encourage the fey to stay close and _heal_ their families. A _bagiennik_ that finds a generous town might invite its extended family to settle in, testing the patience and largesse of its hosts.
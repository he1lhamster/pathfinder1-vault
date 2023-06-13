---
cssclass: [monsters]
title1: Melacage
desc_short: This ethereal ball of faces hovers in the middle of the air. Tears stream
  from every one of the faces' eyes, but the drops fade to nothing before they reach
  the ground.
title2: Melacage
CR: 5
sources:
- name: "Pathfinder #140: Eulogy for Roslar's Coffer"
  page: 88
  link: https://paizo.com/products/btq01x4b
XP: 1600
alignment: NE
size: Medium
type: undead
subtypes:
- incorporeal
initiative:
  bonus: 9
senses:
  darkvision: 60
auras:
- name: life-draining aura
  radius: 30
AC:
  AC: 18
  touch: 18
  flat_footed: 13
  components:
    deflection: 3
    dex: 5
HP:
  HP: 52
  long: 7d8+21
saves:
  fort: 5
  ref: 7
  will: 6
defensive_abilities:
- incorporeal
- rejuvenation
immunities:
- undead traits
speeds:
  base: 30
  base_other: while corporeal
  fly: 30
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: incorporeal touch +10 (4d6 plus despair)
      entries:
      - - damage: 4d6
        - effect: despair
      attack: incorporeal touch
      bonus:
      - 10
  - - text: 2 bites +10 (1d10+5 plus despair) (while corporeal)
      entries:
      - - damage: 1d10+5
        - effect: despair
      count: 2
      attack: bites
      bonus:
      - 10
      restriction: while corporeal
  special:
  - despair
ability_scores:
  STR: '- (20 while corporeal)'
  DEX: 20
  CON:
  INT: 11
  WIS: 13
  CHA: 16
BAB: 5
CMB: 10
CMD: 23
CMD_other: 25 while corporeal
feats:
- name: Blind-Fight
- name: Combat Reflexes
- name: Improved Initiative
- name: Step Up
skills:
  Fly: 23
  Intimidate: 13
  Perception: 11
  Stealth: 15
languages:
- Common
ecology:
  environment: any
  organization: solitary, village (2-5), or city (10-20)
  treasure_type: incidental
special_abilities:
  Despair (Su): A creature hit by a melacage's natural attacks must succeed at a DC
    16 Will save or be overwhelmed by sadness for 1d6 rounds. Affected creatures take
    a -2 penalty on ability checks, saving throws, attack and weapon damage rolls,
    and skill checks. This is an emotion and mind-affecting effect. The save DC is
    Charisma-based.
  Life-Draining Aura (Su): At the start of a melacage's turn, each creature within
    30 feet that is affected by the melacage's despair ability takes 1d4 points of
    negative energy damage, and the melacage becomes corporeal for 1 round. It loses
    the incorporeal subtype and gains a Strength score of 20. Its deflection bonus
    to AC becomes a natural armor bonus, and its incorporeal touch attack is replaced
    with two bite attacks. It loses its fly speed and gains a base speed of 30 feet.
    A creature within the melacage's aura at the start of the melacage's turn can
    allow itself to be affected by the melacage's despair ability (as if it had failed
    the Will save) in order to trigger this ability.
  Rejuvenation (Su): A melacage exists because it is not aware of how it died. Explaining
    to a melacage how it died destroys it permanently. If the melacage is destroyed
    but it still does not know the circumstances of its death, it rejuvenates fully
    in 1d10 days.
desc_long: |-
  In a world with powerful spells, silent monsters, and a long history that can often affect the present in unexpected ways, death-even mass death-can sometimes come as a surprise. While souls may move on, the sudden feelings of loss and confusion can be left in the world as psychic imprints, and if enough of those feelings exist in one place, they can combine into a melacage. A melacage stays near the place where it formed, trying to transfer its crippling depression to a living creature so that it can become corporeal and investigate the cause of its death.

   An average melacage is around 2 feet in diameter, with four to five humanoid faces on the outside of its body.

---

# Melacage
This ethereal ball of faces hovers in the middle of the air. Tears stream from every one of the faces’ eyes, but the drops fade to nothing before they reach the ground.
**Source** Pathfinder #140: Eulogy for Roslar's Coffer pg. 88
**XP** 1,600

NE Medium undead (_[[universal monster rules/Incorporeal|incorporeal]]_)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +11
**Aura** life-draining aura (30 ft.)

##### Defense

**AC** 18, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+3 _[[spells/Deflection|deflection]]_, +5 Dex)
**hp** 52 (7d8+21)
**Fort** +5, **Ref** +7, **Will** +6
**Defensive Abilities** _incorporeal_, rejuvenation; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 30 ft. (while corporeal), fly 30 ft. (perfect)
**Melee** _incorporeal_ touch +10 (4d6 plus despair) or 2 bites +10 (1d10+5 plus despair) (while corporeal)
**Special Attacks** despair

##### Statistics
**Str** — (20 while corporeal), **Dex** 20, **Con** —, **Int** 11, **Wis** 13, **Cha** 16
**Base Atk** +5; **CMB** +10; **CMD** 23 (25 while corporeal)
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Step Up|Step Up]]_
**Skills** Fly +23, Intimidate +13, Perception +11, Stealth +15
**Languages** Common

##### Ecology

**Environment** any
**Organization** solitary, village (2-5), or city (10-20)
**Treasure** incidental

### Special Abilities

**Despair (Su)** A creature hit by a _[[monsters/Melacage|melacage]]_’s _[[universal monster rules/Natural Attacks|natural attacks]]_ must succeed at a DC 16 Will save or be overwhelmed by sadness for 1d6 rounds. Affected creatures take a –2 penalty on ability checks, saving throws, attack and weapon damage rolls, and skill checks. This is an emotion and mind-affecting effect. The save DC is Charisma-based.

**Life-Draining Aura (Su)** At the start of a _melacage_’s turn, each creature within 30 feet that is affected by the _melacage_’s despair ability takes 1d4 points of negative energy damage, and the _melacage_ becomes corporeal for 1 round. It loses the _incorporeal_ subtype and gains a Strength score of 20. Its _deflection_ bonus to AC becomes a natural armor bonus, and its _incorporeal_ touch attack is replaced with two bite attacks. It loses its fly speed and gains a base speed of 30 feet. A creature within the _melacage_’s aura at the start of the _melacage_’s turn can allow itself to be affected by the _melacage_’s despair ability (as if it had failed the Will save) in order to trigger this ability.

**Rejuvenation (Su)** A _melacage_ exists because it is not aware of how it died. Explaining to a _melacage_ how it died destroys it permanently. If the _melacage_ is destroyed but it still does not know the circumstances of its death, it rejuvenates fully in 1d10 days.

##### Description

In a world with powerful spells, silent monsters, and a long history that can often affect the present in unexpected ways, death—even mass death—can sometimes come as a surprise. While souls may move on, the sudden feelings of loss and _[[spells/Confusion|confusion]]_ can be left in the world as _[[classes/Psychic|psychic]]_ imprints, and if enough of those feelings exist in one place, they can combine into a _melacage_. A _melacage_ stays near the place where it formed, trying to transfer its crippling depression to a living creature so that it can become corporeal and investigate the cause of its death.

An average _melacage_ is around 2 feet in diameter, with four to five humanoid faces on the outside of its body.
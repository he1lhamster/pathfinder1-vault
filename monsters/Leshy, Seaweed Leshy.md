---
cssclass: [monsters]
title1: Leshy, Seaweed Leshy
desc_short: This vaguely humanoid plant creature has a body formed of soggy green
  seaweed and wears crude armor made from seashells.
title2: Seaweed Leshy
CR: 3
sources:
- name: Bestiary 3
  page: 180
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 800
alignment: N
size: Small
type: plant
subtypes:
- aquatic
- leshy
- shapechanger
initiative:
  bonus: 1
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 15
  touch: 12
  flat_footed: 14
  components:
    armor: 1
    dex: 1
    natural: 2
    size: 1
HP:
  HP: 30
  long: 4d8+12
saves:
  fort: 6
  ref: 2
  will: 3
immunities:
- electricity
- sonic
- plant traits
speeds:
  base: 20
  swim: 20
attacks:
  melee:
  - - text: slam +4 (1d6)
      entries:
      - - damage: 1d6
      attack: slam
      bonus:
      - 4
  ranged:
  - - text: water jet +5 touch (1 plus blind)
      entries:
      - - damage: '1'
        - effect: blind
      attack: water jet
      bonus:
      - 5
      touch: true
spell_like_abilities:
  entries:
  - name: pass without trace
    source: default
    freq: Constant
  - name: entangle
    source: default
    freq: 1/day
    other: in water only
    DC: 12
  sources:
  - name: default
    CL: 8
    concentration: 9
ability_scores:
  STR: 10
  DEX: 13
  CON: 14
  INT: 9
  WIS: 15
  CHA: 12
BAB: 3
CMB: 2
CMD: 13
feats:
- name: Ability Focus (water jet)
- name: Toughness
skills:
  Perception: 7
  Stealth: 9
    in water: 13
  Survival: 3
    in water: 7
  Swim: 8
  _racial_mods:
    Stealth:
      in water: 4
    Survival:
      in water: 4
languages:
- Druidic
- Sylvan
- plantspeech (seaweed)
special_qualities:
- air cyst
- amphibious
- change shape (Small seaweed; tree shape)
- verdant burst
ecology:
  environment: any ocean or coastline
  organization: solitary or patch (2-16)
  treasure_type: standard
special_abilities:
  Air Cyst (Su): Seaweed leshys constantly grow small bulbs filled with air. As a
    move action, they can detach a bulb and give it to another creature. If consumed
    as a standard action, this air cyst grants water breathing (as the spell) for
    10 minutes. Seaweed leshys can have a maximum of four usable air cysts at any
    one time, and air cysts regrow at a rate of one per 24 hours.
  Water Jet (Ex): A seaweed leshy can expel a high-pressure jet of water from its
    mouth to a range of 30 feet. It must make a ranged touch attack to strike a target-if
    it hits, the blast deals 1 point of bludgeoning damage (this damage is not modified
    by Strength). In addition, the creature hit must make a DC 15 Fortitude save or
    be blinded by the water for 1 round. The save DC is Dexterity-based.
desc_long: |-
  Seaweed leshys usually dwell along coastlines, happily splashing and playing in tide pools, but they are equally at home at sea, floating among large kelp beds. Although perfectly capable of existing out of water indefinitely, seaweed leshys prefer to limit their time away from the sea almost out of a sense of pride. Most seaweed leshys take a dim view of freshwater plant life, to the point of mocking such plants in the same way an urbanite might talk down to folk who live in more rural areas. Rumors of freshwater leshys are a sure way to bring peals of mocking laughter from a seaweed leshy.

  Seaweed leshys resemble miniature, waterlogged green humans grown from leafy green seaweed, with skinny arms and legs, webbed hands and feet, and long strands of brown, green, or red seaweed for hair. They wear armor made from a pair of large clam shells or from several smaller shells tied together. This armor functions as a suit of masterwork padded armor for a seaweed leshy, but not for any other creature.

  Patient and thoughtful by inclination (save for matters associated with those silly freshwater leshys), seaweed leshys believe that in time nature brings what is needed by the ebb and flow of the tide or the steady flow of the river. They counsel against hasty decisions and rash actions, always preferring to wait and see what another day might bring.

---

# Leshy, Seaweed Leshy
This vaguely humanoid plant creature has a body formed of soggy green seaweed and wears crude armor made from seashells.
**Source** Bestiary 3 pg. 180
**XP** 800

N Small plant (aquatic, leshy, shapechanger)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +7

##### Defense

**AC** 15, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+1 armor, +1 Dex, +2 natural, +1 size)
**hp** 30 (4d8+12)
**Fort** +6, **Ref** +2, **Will** +3
**Immune** electricity, sonic, _[[universal monster rules/Plant Traits|plant traits]]_

##### Offense
**Speed** 20 ft., swim 20 ft.
**Melee** slam +4 (1d6)
**Ranged** water _[[universal monster rules/Jet|jet]]_ +5 touch (1 plus blind)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +9)
Constant—_[[spells/Pass without Trace|pass without trace]]_
1/day—_[[spells/Entangle|entangle]]_ (in water only, DC 12)

##### Statistics
**Str** 10, **Dex** 13, **Con** 14, **Int** 9, **Wis** 15, **Cha** 12
**Base Atk** +3; **CMB** +2; **CMD** 13
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (water _jet_), _[[feats/Toughness|Toughness]]_
**Skills** Perception +7, Stealth +9 (+13 in water), Survival +3 (+7 in water), Swim +8; **Racial Modifiers** +4 Stealth and Survival in water
**Languages** Druidic, Sylvan; plantspeech (seaweed)
**SQ** air cyst, _[[universal monster rules/Amphibious|amphibious]]_, _[[universal monster rules/Change Shape|change shape]]_ (Small seaweed; _[[spells/Tree Shape|tree shape]]_), verdant burst

##### Ecology

**Environment** any ocean or coastline
**Organization** solitary or patch (2–16)
**Treasure** standard

### Special Abilities

**Air Cyst (Su)** Seaweed leshys constantly grow small bulbs filled with air. As a move action, they can detach a bulb and give it to another creature. If consumed as a standard action, this air cyst grants _[[universal monster rules/Water Breathing|water breathing]]_ (as the spell) for 10 minutes. Seaweed leshys can have a maximum of four usable air cysts at any one time, and air cysts regrow at a rate of one per 24 hours.

**Water _Jet_ (Ex)** A seaweed leshy can expel a high-pressure _jet_ of water from its mouth to a range of 30 feet. It must make a ranged touch attack to strike a target—if it hits, the blast deals 1 point of bludgeoning damage (this damage is not modified by Strength). In addition, the creature hit must make a DC 15 Fortitude save or be _[[conditions/Blinded|blinded]]_ by the water for 1 round. The save DC is Dexterity-based.

##### Description

Seaweed leshys usually dwell along coastlines, happily splashing and playing in tide pools, but they are equally at home at sea, floating among large kelp beds. Although perfectly capable of existing out of water indefinitely, seaweed leshys prefer to limit their time away from the sea almost out of a sense of pride. Most seaweed leshys take a dim view of freshwater plant life, to the point of mocking such plants in the same way an urbanite might talk down to folk who live in more rural areas. Rumors of freshwater leshys are a sure way to bring peals of mocking laughter from a seaweed leshy.

Seaweed leshys resemble miniature, waterlogged green humans grown from leafy green seaweed, with skinny arms and legs, webbed hands and feet, and long strands of brown, green, or red seaweed for hair. They wear armor made from a pair of large clam shells or from several smaller shells tied together. This armor functions as a suit of masterwork _[[items/Armor/Padded armor|padded armor]]_ for a seaweed leshy, but not for any other creature.

Patient and thoughtful by inclination (save for matters associated with those silly freshwater leshys), seaweed leshys believe that in time nature brings what is needed by the ebb and flow of the tide or the steady flow of the river. They counsel against hasty decisions and rash actions, always preferring to wait and see what another day might bring.
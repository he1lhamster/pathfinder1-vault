---
cssclass: [monsters]
title1: Protean, Naunet
desc_short: Tentacles tipped with snapping jaws emerge from this serpentine creature's
  back, complementing the vicious maw in its reptilian face.
title2: Naunet
CR: 7
sources:
- name: Bestiary 2
  page: 216
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
- name: 'Pathfinder #22: The End of Eternity'
  page: 86
  link: http://paizo.com/pathfinder/adventurePath/legacyOfFire/v5748btpy87ux
XP: 3200
alignment: CN
size: Large
type: outsider
subtypes:
- chaotic
- extraplanar
- protean
- shapechanger
initiative:
  bonus: 7
senses:
  blindsense: 30
  darkvision: 60
  detect law: true
AC:
  AC: 20
  touch: 12
  flat_footed: 17
  components:
    dex: 3
    natural: 8
    size: -1
HP:
  HP: 94
  long: 9d10+45
saves:
  fort: 11
  ref: 11
  will: 6
defensive_abilities:
- amorphous anatomy
- freedom of movement
DR:
- amount: 5
  weakness: lawful
immunities:
- acid
- polymorph
resistances:
  electricity: 10
  sonic: 10
SR: 18
speeds:
  base: 30
  fly: 30
  fly_maneuverability: perfect
  swim: 30
attacks:
  melee:
  - - text: bite +14 (1d8+5)
      entries:
      - - damage: 1d8+5
      attack: bite
      bonus:
      - 14
    - text: tail slap +11 (1d6+2 plus grab)
      entries:
      - - damage: 1d6+2
        - effect: grab
      attack: tail slap
      bonus:
      - 11
    - text: 2 tentacles +11 (1d6+2 plus confusion)
      entries:
      - - damage: 1d6+2
        - effect: confusion
      count: 2
      attack: tentacles
      bonus:
      - 11
  special:
  - adaptive strike
  - coalesce chaos
  - constrict (1d6+5)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect law
    source: default
    freq: Constant
  - name: acid arrow
    source: default
    freq: At will
  - name: fog cloud
    source: default
    freq: At will
  - name: dimension door
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: shatter
    source: default
    freq: At will
    DC: 14
  - name: chaos hammer
    source: default
    freq: 1/day
    DC: 16
  sources:
  - name: default
    CL: 7
    concentration: 9
ability_scores:
  STR: 20
  DEX: 17
  CON: 20
  INT: 11
  WIS: 16
  CHA: 15
BAB: 9
CMB: 15
CMD: 28
feats:
- name: Combat Reflexes
- name: Improved Initiative
- name: Lightning Reflexes
- name: Multiattack
- name: Weapon Focus (bite)
skills:
  Acrobatics: 15
  Fly: 9
  Intimidate: 14
  Perception: 15
  Stealth: 11
  Survival: 15
  Swim: 25
languages:
- Abyssal
- Protean
special_qualities:
- change shape (polymorph)
ecology:
  environment: any (Limbo)
  organization: solitary, pair, or cacophony (3-12)
  treasure_type: none
special_abilities:
  Adaptive Strike (Su): A naunet's natural weapons count as magical and chaotic for
    the purposes of overcoming damage reduction. As a free action once per round,
    a naunet may infuse all of its natural attacks with adamantine, silver, or cold
    iron, thereby allowing it to overcome damage reduction of those types as well.
  Coalesce Chaos (Su): Once per day as a standard action, three or more naunets working
    together can create a roiling cloud of multicolored chaos matter. This effect
    is identical to solid fog (CL 12th) and lasts for 2d6 rounds. If six or more naunets
    are present, the coalesced chaos instead functions as acid fog (CL 12th).
  Confusion (Su): A creature struck by a naunet's tentacle attack is infused with
    raw chaos, and must make a DC 19 Will save or be confused for 1 round. Rounds
    of confusion dealt in this manner stack. A creature with a chaotic component to
    its alignment gains a +4 bonus on saves against this effect, and creatures with
    the chaotic subtype are immune. This is a mind-affecting effect. The save DC is
    Constitution-based.
desc_long: |-
  Far more bestial than their kin, naunets are the lowest caste of the true proteans, the shock troops of their race and roving marauders in the cause of chaos. Primarily found in the shifting borderlands between Limbo and other planes, naunets are driven half-insane by the stability and stasis of such areas, and frequently rampage through the edges of other planes, tearing up the very fabric of reality itself and returning vast swaths of land to the beautiful, formless potentiality of their home.

  A naunet is 12 feet long and weighs 900 pounds.

---

# Protean, Naunet
Tentacles tipped with _[[feats/Snapping Jaws|snapping jaws]]_ emerge from this serpentine creature’s back, complementing the _[[items/Weapon Magic Abilities/Vicious|vicious]]_ maw in its reptilian face.
**Source** Bestiary 2 pg. 216, Pathfinder #22: The End of Eternity pg. 86
**XP** 3,200

CN Large outsider (chaotic, extraplanar, protean, shapechanger)
**Init** +7; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 30 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Law|detect law]]_; Perception +15

##### Defense

**AC** 20, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+3 Dex, +8 natural, –1 size)
**hp** 94 (9d10+45)
**Fort** +11, **Ref** +11, **Will** +6
**Defensive Abilities** _[[universal monster rules/Amorphous|amorphous]]_ anatomy, _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 5/lawful; **Immune** acid, _[[spells/Polymorph|polymorph]]_; **Resist** electricity 10, sonic 10; **SR** 18

##### Offense
**Speed** 30 ft., fly 30 ft. (perfect), swim 30 ft.
**Melee** bite +14 (1d8+5) , tail slap +11 (1d6+2 plus _[[universal monster rules/Grab|grab]]_), 2 tentacles +11 (1d6+2 plus _[[spells/Confusion|confusion]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** adaptive strike, coalesce chaos, _[[universal monster rules/Constrict|constrict]]_ (1d6+5)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +9)
Constant—_detect law_
At will—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Dimension Door|dimension door]]_ (self plus 50 lbs. of objects only), _[[spells/Shatter|shatter]]_ (DC 14)
1/day—_[[spells/Chaos Hammer|chaos hammer]]_ (DC 16)

##### Statistics
**Str** 20, **Dex** 17, **Con** 20, **Int** 11, **Wis** 16, **Cha** 15
**Base Atk** +9; **CMB** +15; **CMD** 28
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Acrobatics +15, Fly +9, Intimidate +14, Perception +15, Stealth +11, Survival +15, Swim +25
**Languages** Abyssal, Protean
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_polymorph_)

##### Ecology

**Environment** any (Limbo)
**Organization** solitary, pair, or cacophony (3–12)
**Treasure** none

### Special Abilities

**Adaptive Strike (Su)** A naunet’s natural weapons count as magical and chaotic for the purposes of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_. As a free action once per round, a naunet may infuse all of its _[[universal monster rules/Natural Attacks|natural attacks]]_ with adamantine, silver, or cold iron, thereby allowing it to overcome _damage reduction_ of those types as well.

**Coalesce Chaos (Su)** Once per day as a standard action, three or more naunets working together can create a roiling cloud of multicolored chaos matter. This effect is identical to _[[spells/Solid Fog|solid fog]]_ (CL 12th) and lasts for 2d6 rounds. If six or more naunets are present, the coalesced chaos instead functions as _[[spells/Acid Fog|acid fog]]_ (CL 12th).

**_Confusion_ (Su)** A creature struck by a naunet’s tentacle attack is infused with raw chaos, and must make a DC 19 Will save or be _[[conditions/Confused|confused]]_ for 1 round. Rounds of _confusion_ dealt in this manner stack. A creature with a chaotic component to its alignment gains a +4 bonus on saves against this effect, and creatures with the chaotic subtype are immune. This is a mind-affecting effect. The save DC is Constitution-based.

##### Description

Far more bestial than their kin, naunets are the lowest caste of the true proteans, the _[[items/Weapon Magic Abilities/Shock|shock]]_ troops of their race and roving marauders in the cause of chaos. Primarily found in the shifting borderlands between Limbo and other planes, naunets are driven half-insane by the stability and stasis of such areas, and frequently rampage through the edges of other planes, tearing up the very fabric of reality itself and returning vast swaths of land to the beautiful, formless potentiality of their home.

A naunet is 12 feet long and weighs 900 pounds.
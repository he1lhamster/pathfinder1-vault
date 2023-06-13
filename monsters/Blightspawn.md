---
cssclass: [monsters]
title1: Blightspawn
desc_short: This human-sized, mosquito-like creature has a long, flexible proboscis
  that ends in a murderous stinger.
title2: Blightspawn
CR: 5
sources:
- name: Bestiary 5
  page: 43
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 1600
alignment: CE
size: Medium
type: aberration
initiative:
  bonus: 8
senses:
  darkvision: 60
  scent: true
auras:
- name: stagnation
  radius: 20
  DC: 16
AC:
  AC: 18
  touch: 14
  flat_footed: 14
  components:
    dex: 4
    natural: 4
HP:
  HP: 52
  long: 7d8+21
  fast_healing: 3
saves:
  fort: 5
  ref: 8
  will: 8
DR:
- amount: 5
  weakness: magic
immunities:
- acid
- cold
- poison
speeds:
  base: 30
  climb: 30
  fly: 50
  fly_maneuverability: average
attacks:
  melee:
  - - text: sting +11 (2d6+9/19-20 plus attach and poison)
      entries:
      - - damage: 2d6+9
          crit_range: 19-20
        - effect: attach
        - effect: poison
      attack: sting
      bonus:
      - 11
  special:
  - blood drain (1d2 Constitution)
space: 5
reach: 10
spell_like_abilities:
  entries:
  - name: freedom of movement
    source: default
    freq: Constant
  - name: pass without trace
    source: default
    freq: Constant
  - name: bestow curse
    source: default
    freq: 1/day
    DC: 16
  - name: blur
    source: default
    freq: 1/day
  - name: contagion
    source: default
    freq: 1/day
    DC: 16
  - name: diminish plants
    source: default
    freq: 1/day
  - name: gust of wind
    source: default
    freq: 1/day
  - name: hold monster
    source: default
    freq: 1/day
    DC: 17
  sources:
  - name: default
    CL: 5
    concentration: 7
ability_scores:
  STR: 23
  DEX: 18
  CON: 16
  INT: 7
  WIS: 16
  CHA: 15
BAB: 5
CMB: 11
CMB_other: +15 to maintain a grapple
CMD: 25
CMD_other: 33 vs. trip
feats:
- name: Flyby Attack
- name: Improved Initiative
- name: Lightning Reflexes
- name: Power Attack
skills:
  Climb: 14
  Fly: 14
  Perception: 13
languages:
- Aklo (can't speak)
special_qualities:
- no breath
ecology:
  environment: any swamps
  organization: solitary
  treasure_type: standard
special_abilities:
  Poison (Su): Sting-injury; save Fort DC 16; frequency 1/round for 6 rounds; effect
    1d4 Wisdom damage and confusion for 1 round; cure 2 saves. The save DC is Constitution-based.
  Stagnation Aura (Su): A blightspawn's stagnation aura causes lethargy and torpor
    in those who approach it, sapping their energy and speed. When a creature comes
    within 20 feet of a blightspawn, it must succeed at a DC 16 Will save or be affected
    as per the slow spell for as long as the creature remains within the blightspawn's
    aura and for an additional 1d3 rounds after leaving it. Once a creature successfully
    saves against the aura, it is immune to that particular blightspawn's aura for
    24 hours; otherwise, reentering the aura forces a creature to save again. In addition,
    this aura fouls liquids of all types within the area. A creature that drinks anything
    in a blightspawn's aura (including potions and alchemical elixirs) must succeed
    at a DC 16 Fortitude save or be nauseated for 1d3 rounds. The save DCs are Constitution-based.
desc_long: |-
  Blightspawn must gestate in the body of a true believer until they're released at the host's death or during a ritual, and so are most often found in places where cults that worship parasitic demons or devils are strong. To the faithful, being host to an immature blightspawn is a great honor, for they believe that when the monster bursts from the host's body, the host's consciousness lives on in some way in the blightspawn's mind, almost as if the host had reincarnated into the monster. The fact that cultists who die giving hideous birth to a blightspawn can't be resurrected lends a bit of weight to this notion, even if the blightspawn themselves have nothing to say on the topic.

  A host carrying an immature blightspawn functions normally in all ways until the creature emerges-except that the host can pass on new blightspawn to his or her children. A blightspawn's gestation can last for decades, and a child separated from infected parents might live her entire life without knowing what awaits her upon death. When a blightspawn emerges from its host, it is fully grown, although its gore-soaked wings can't be used for flight for 1d4 rounds after emerging.

---

# Blightspawn
This human-sized, mosquito-like creature has a long, flexible proboscis that ends in a murderous stinger.
**Source** Bestiary 5 pg. 43
**XP** 1,600
CE Medium aberration
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +13
**Aura** stagnation (20 ft., DC 16)

##### Defense

**AC** 18, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+4 Dex, +4 natural)
**hp** 52 (7d8+21); _[[universal monster rules/Fast Healing|fast healing]]_ 3
**Fort** +5, **Ref** +8, **Will** +8
**DR** 5/magic; **Immune** acid, cold, poison

##### Offense
**Speed** 30 ft., _[[universal monster rules/Climb|climb]]_ 30 ft., fly 50 ft. (average)
**Melee** sting +11 (2d6+9/19-20 plus _[[universal monster rules/Attach|attach]]_ and poison)
**Space** 5 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Blood Drain|blood drain]]_ (1d2 Constitution)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +7)
Constant—_[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Pass without Trace|pass without trace]]_
1/day—_[[spells/Bestow Curse|bestow curse]]_ (DC 16), _[[spells/Blur|blur]]_, _[[spells/Contagion|contagion]]_ (DC 16), _[[spells/Diminish Plants|diminish plants]]_, _[[spells/Gust Of Wind|gust of wind]]_, _[[spells/Hold Monster|hold monster]]_ (DC 17)

##### Statistics
**Str** 23, **Dex** 18, **Con** 16, **Int** 7, **Wis** 16, **Cha** 15
**Base Atk** +5; **CMB** +11 (+15 to maintain a grapple); **CMD** 25 (33 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** _Climb_ +14, Fly +14, Perception +13
**Languages** Aklo (can’t speak)
**SQ** _[[universal monster rules/No Breath|no breath]]_

##### Ecology

**Environment** any swamps
**Organization** solitary
**Treasure** standard

### Special Abilities

**Poison (Su)** Sting—injury; save Fort DC 16; frequency 1/round for 6 rounds; effect 1d4 Wisdom damage and _[[spells/Confusion|confusion]]_ for 1 round; cure 2 saves. The save DC is Constitution-based.
**Stagnation Aura (Su)** A _[[monsters/Blightspawn|blightspawn]]_’s stagnation aura causes _[[curses/Lethargy|lethargy]]_ and torpor in those who approach it, _[[items/Weapon Magic Abilities/Sapping|sapping]]_ their energy and speed. When a creature comes within 20 feet of a _blightspawn_, it must succeed at a DC 16 Will save or be affected as per the _[[spells/Slow|slow]]_ spell for as long as the creature remains within the _blightspawn_’s aura and for an additional 1d3 rounds after leaving it. Once a creature successfully saves against the aura, it is immune to that particular _blightspawn_’s aura for 24 hours; otherwise, reentering the aura forces a creature to save again. In addition, this aura fouls liquids of all types within the area. A creature that drinks anything in a _blightspawn_’s aura (including potions and alchemical elixirs) must succeed at a DC 16 Fortitude save or be _[[conditions/Nauseated|nauseated]]_ for 1d3 rounds. The save DCs are Constitution-based.

##### Description

_Blightspawn_ must gestate in the body of a true believer until they’re released at the host’s death or during a ritual, and so are most often found in places where cults that worship parasitic demons or devils are strong. To the faithful, being host to an immature _blightspawn_ is a great honor, for they believe that when the monster bursts from the host’s body, the host’s consciousness lives on in some way in the _blightspawn_’s mind, almost as if the host had reincarnated into the monster. The fact that cultists who die giving hideous birth to a _blightspawn_ can’t be resurrected lends a bit of weight to this notion, even if the _blightspawn_ themselves have nothing to say on the topic.

A host carrying an immature _blightspawn_ functions normally in all ways until the creature emerges—except that the host can pass on new _blightspawn_ to his or her children. A _blightspawn_’s gestation can last for decades, and a child separated from infected parents might live her entire life without knowing what awaits her upon death. When a _blightspawn_ emerges from its host, it is fully grown, although its gore-soaked wings can’t be used for _[[universal monster rules/Flight|flight]]_ for 1d4 rounds after emerging.
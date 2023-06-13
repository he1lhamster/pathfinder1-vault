---
cssclass: [monsters]
title1: Blightspawn of Ghlaunder
desc_short: This human-sized, mosquito-like creature has a long, flexible proboscis
  that ends in a murderous stinger.
title2: Blightspawn of Ghlaunder
CR: 5
sources:
- name: Feast of Ravenmoor
  page: 29
  link: http://paizo.com/products/btpy8mw2?Pathfinder-Module-Feast-of-Ravenmoor
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
  - - text: sting +10 (2d6+7/19-20 plus attach and poison)
      entries:
      - - damage: 2d6+7
          crit_range: 19-20
        - effect: attach
        - effect: poison
      attack: sting
      bonus:
      - 10
  special:
  - blood drain (1d2 Con)
  - stagnation gaze
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
  STR: 21
  DEX: 18
  CON: 16
  INT: 7
  WIS: 16
  CHA: 15
BAB: 5
CMB: 10
CMB_other: +14 to maintain a grapple
CMD: 24
CMD_other: 32 vs. trip
feats:
- name: Flyby Attack
- name: Improved Initiative
- name: Lightning Reflexes
- name: Power Attack
skills:
  Climb: 13
  Fly: 14
  Perception: 13
languages:
- Aklo (cannot speak)
special_qualities:
- no breath
special_abilities:
  Poison (Su): Sting-injury; save Fort DC 16; frequency 1/round for 6 rounds; effect
    1d4 Wisdom damage and confusion for 1 round; cure 2 saves. The save DC is Constitution-based.
  Stagnation Aura (Su): A blightspawn's stagnation aura causes lethargy and torpor
    in those who approach it, sapping energy and speed. When a creature comes within
    20 feet of a blightspawn, it must make a DC 16 Will save to avoid being affected
    as per the spell slow, for as long as the creature remains within the blightspawn's
    aura and for an additional 1d3 rounds after leaving it. Once a creature successfully
    saves against the aura, it is immune to that particular blightspawn's aura for
    24 hours; otherwise, re-entering the aura forces a creature to save again. In
    addition, this aura fouls liquids of all types within the area. A creature that
    drinks anything in a blightspawn's aura (including potions and alchemical elixirs)
    must make a DC 14 Fortitude save or be nauseated for 1d3 rounds. The save DC is
    Constitution-based.
desc_long: The blightspawn of Ghlaunder are found most often in places where the Gossamer
  King's cult is strong, for these creatures must gestate in the body of one of the
  parasite god's true believers. To the faithful of Ghlaunder, being host to an immature
  blightspawn is a great honor, for when the monster bursts from the body of its host,
  the host's consciousness lives on in some way in the blightspawn's mind, almost
  as if the host had reincarnated into the monster. That cultists who die giving hideous
  birth to a blightspawn cannot be resurrected lends a bit of weight to this notion,
  even if the blightspawn themselves have nothing to say on the topic. A cultist carrying
  an immature blightspawn functions normally in all ways until the creature emerges
  (typically upon the cultist's death, or at the culmination of certain vile rituals)-except
  that until then, the cultist can pass on new blightspawn to his or her children.
  A blightspawn's gestation can last for decades, and in cases in which a child is
  separated from infected parents, the child might live her entire life without knowing
  the truth of what awaits her upon death. When a blightspawn emerges from its host,
  it is immediately fully grown, although its gore-wet wings cannot be used for flight
  for 1d4 rounds after emerging.

---

# Blightspawn of Ghlaunder
This human-sized, mosquito-like creature has a long, flexible proboscis that ends in a murderous stinger.
**Source** Feast of Ravenmoor pg. 29
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
**Melee** sting +10 (2d6+7/19–20 plus _[[universal monster rules/Attach|attach]]_ and poison)
**Space** 5 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Blood Drain|blood drain]]_ (1d2 Con), stagnation _[[universal monster rules/Gaze|gaze]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +7)
Constant—_[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Pass without Trace|pass without trace]]_
1/day—_[[spells/Bestow Curse|bestow curse]]_ (DC 16), _[[spells/Blur|blur]]_, _[[spells/Contagion|contagion]]_ (DC 16), _[[spells/Diminish Plants|diminish plants]]_, _[[spells/Gust Of Wind|gust of wind]]_, _[[spells/Hold Monster|hold monster]]_ (DC 17)

##### Statistics
**Str** 21, **Dex** 18, **Con** 16, **Int** 7, **Wis** 16, **Cha** 15
**Base Atk** +5; **CMB** +10 (+14 to maintain a grapple); **CMD** 24 (32 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** _Climb_ +13, Fly +14, Perception +13
**Languages** Aklo (cannot speak)
**SQ** _[[universal monster rules/No Breath|no breath]]_

### Special Abilities

**Poison (Su)** Sting—injury; save Fort DC 16; frequency 1/round for 6 rounds; effect 1d4 Wisdom damage and _[[spells/Confusion|confusion]]_ for 1 round; cure 2 saves. The save DC is Constitution-based.
**Stagnation Aura (Su) **A _[[monsters/Blightspawn|blightspawn]]_’s stagnation aura causes _[[curses/Lethargy|lethargy]]_ and torpor in those who approach it, _[[items/Weapon Magic Abilities/Sapping|sapping]]_ energy and speed. When a creature comes within 20 feet of a _blightspawn_, it must make a DC 16 Will save to avoid being affected as per the spell _[[spells/Slow|slow]]_, for as long as the creature remains within the _blightspawn_’s aura and for an additional 1d3 rounds after leaving it. Once a creature successfully saves against the aura, it is immune to that particular _blightspawn_’s aura for 24 hours; otherwise, re-entering the aura forces a creature to save again. In addition, this aura fouls liquids of all types within the area. A creature that drinks anything in a _blightspawn_’s aura (including potions and alchemical elixirs) must make a DC 14 Fortitude save or be _[[conditions/Nauseated|nauseated]]_ for 1d3 rounds. The save DC is Constitution-based.

##### Description

The _[[monsters/Blightspawn of Ghlaunder|blightspawn of Ghlaunder]]_ are found most often in places where the Gossamer _[[npcs/King|King]]_’s cult is strong, for these creatures must gestate in the body of one of the parasite god’s true believers. To the faithful of Ghlaunder, being host to an immature _blightspawn_ is a great honor, for when the monster bursts from the body of its host, the host’s consciousness lives on in some way in the _blightspawn_’s mind, almost as if the host had reincarnated into the monster. That cultists who die giving hideous birth to a _blightspawn_ cannot be resurrected lends a bit of weight to this notion, even if the _blightspawn_ themselves have nothing to say on the topic. A _[[npcs/Cultist|cultist]]_ carrying an immature _blightspawn_ functions normally in all ways until the creature emerges (typically upon the _cultist_’s death, or at the culmination of certain vile rituals)—except that until then, the _cultist_ can pass on new _blightspawn_ to his or her children. A _blightspawn_’s gestation can last for decades, and in cases in which a child is separated from infected parents, the child might live her entire life without knowing the truth of what awaits her upon death. When a _blightspawn_ emerges from its host, it is immediately fully grown, although its gore-wet wings cannot be used for _[[universal monster rules/Flight|flight]]_ for 1d4 rounds after emerging.
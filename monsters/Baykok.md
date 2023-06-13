---
cssclass: [monsters]
title1: Baykok
desc_short: This howling corpse swoops through the air with hideously elongated legs
  and a bow made of bone.
title2: Baykok
CR: 9
sources:
- name: Bestiary 3
  page: 35
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 6400
alignment: NE
size: Medium
type: undead
initiative:
  bonus: 10
senses:
  darkvision: 60
AC:
  AC: 24
  touch: 17
  flat_footed: 17
  components:
    dex: 6
    dodge: 1
    natural: 7
HP:
  HP: 97
  long: 15d8+30
saves:
  fort: 7
  ref: 11
  will: 9
immunities:
- undead traits
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 claws +14 (1d6+3)
      entries:
      - - damage: 1d6+3
      count: 2
      attack: claws
      bonus:
      - 14
  ranged:
  - - text: +1 composite longbow +19/+14/+9 (1d8+4/19-20/×3 plus 1d6 negative energy
        and paralysis)
      entries:
      - - damage: 1d8+4
          crit_range: 19-20
          crit_multiplier: 3
        - damage: 1d6
          type: negative energy
        - effect: paralysis
      attack: +1 composite longbow
      bonus:
      - 19
      - 14
      - 9
  special:
  - devour soul
  - dread howl
  - infused arrows
ability_scores:
  STR: 17
  DEX: 22
  CON:
  INT: 11
  WIS: 10
  CHA: 15
BAB: 11
CMB: 14
CMD: 31
feats:
- name: Dodge
- name: Improved Critical (composite longbow)
- name: Improved Initiative
- name: Mobility
- name: Point-Blank Shot
- name: Precise Shot
- name: Rapid Shot
- name: Weapon Focus (composite longbow)
skills:
  Fly: 28
  Intimidate: 20
  Perception: 18
  Stealth: 24
languages:
- Common
ecology:
  environment: any
  organization: solitary, gang (2-5), or flight (6-12)
  treasure_type: standard
  treasure:
  - +1 composite longbow [+3 Str]
  - other treasure
special_abilities:
  Devour Soul (Su): A baykok can take a standard action to devour the soul of an adjacent
    dead or dying creature. A dying creature can resist this attack with a DC 19 Fortitude
    save. If it fails, the target is instantly slain. If the creature is already dead,
    it does not make a saving throw, although the body cannot be more than 1 hour
    dead. A creature subjected to this attack cannot be brought back to life via raise
    dead (resurrection and more powerful effects work normally). When a baykok devours
    a soul in this way, it heals 5d6+10 points of damage and becomes hasted for 4
    rounds (as if affected by haste). This is a death effect. The save DC is Charisma-based.
  Dread Howl (Su): Once per day, a baykok can unleash a blood-curdling howl. Any living
    creature within a 30-foot-radius burst becomes paralyzed with fear for 1 round
    unless it resists with a DC 19 Will save. Any creature that makes this saving
    throw is instead shaken for 1 round. This is a fear effect. The DC is Charisma-based.
  Infused Arrows (Su): A baykok creates arrows of bone as it fires its bow-it need
    not carry arrows as ammunition. These bone arrows do normal damage for arrows
    fired from the bow, but gain a +1 enhancement bonus on attack and damage rolls.
    In addition, each arrow deals an additional 1d6 points of negative energy on a
    hit. Further, the first creature struck in a round by a baykok's arrow must make
    a DC 19 Fortitude save to avoid being paralyzed for 1d3 rounds. A baykok can fire
    normal arrows from its bow if it wishes-such arrows, however, do not gain the
    special negative energy damage or paralysis effects. The DC is Charisma-based.
desc_long: |-
  When hunters become utterly obsessed with the chase and indulge excessively in the savagery of the kill, their souls become progressively tainted. When such remorseless hunters perish before they can capture and kill their quarry, they sometimes rise from death as baykoks-flying undead horrors that kill purely for the ecstasy that only murder can bring them.

  Unlike many undead who feed on and hate all living things, a baykok seeks always to prove its mastery of the hunt. Though thoroughly wicked, baykoks often ignore all but the most powerful-looking foe in a group, only picking off lesser creatures if they dare to get between the baykok and its true prey. When it finally lays low its quarry, the baykok swoops down on the victim to devour the creature's soul in an attempt to make sure the creature never returns to seek revenge.

---

# Baykok
This howling corpse swoops through the air with hideously elongated legs and a bow made of bone.
**Source** Bestiary 3 pg. 35
**XP** 6,400

NE Medium undead
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +18

##### Defense

**AC** 24, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+6 Dex, +1 _[[feats/Dodge|dodge]]_, +7 natural)
**hp** 97 (15d8+30)
**Fort** +7, **Ref** +11, **Will** +9
**Immune** _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 30 ft., fly 60 ft. (good)
**Melee** 2 claws +14 (1d6+3)
**Ranged** +1 _[[items/Weapon/Composite longbow|composite longbow]]_ +19/+14/+9 (1d8+4/19–20/×3 plus 1d6 negative energy and _[[universal monster rules/Paralysis|paralysis]]_)
**Special Attacks** devour soul, dread howl, infused arrows

##### Statistics
**Str** 17, **Dex** 22, **Con** —, **Int** 11, **Wis** 10, **Cha** 15
**Base Atk** +11; **CMB** +14; **CMD** 31
**Feats** _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (_composite longbow_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_composite longbow_)
**Skills** Fly +28, Intimidate +20, Perception +18, Stealth +24
**Languages** Common

##### Ecology

**Environment** any
**Organization** solitary, gang (2–5), or _[[universal monster rules/Flight|flight]]_ (6–12)
**Treasure** standard (+1 _composite longbow_ [+3 Str], other treasure)

### Special Abilities

**Devour Soul (Su)** A _[[monsters/Baykok|baykok]]_ can take a standard action to devour the soul of an adjacent dead or _[[conditions/Dying|dying]]_ creature. A _dying_ creature can resist this attack with a DC 19 Fortitude save. If it fails, the target is instantly slain. If the creature is already dead, it does not make a saving throw, although the body cannot be more than 1 hour dead. A creature subjected to this attack cannot be brought back to life via _[[spells/Raise Dead|raise dead]]_ (_[[spells/Resurrection|resurrection]]_ and more powerful effects work normally). When a _baykok_ devours a soul in this way, it heals 5d6+10 points of damage and becomes hasted for 4 rounds (as if affected by _[[spells/Haste|haste]]_). This is a death effect. The save DC is Charisma-based.

**Dread Howl (Su)** Once per day, a _baykok_ can unleash a blood-curdling howl. Any living creature within a 30-foot-radius burst becomes _[[conditions/Paralyzed|paralyzed]]_ with _[[universal monster rules/Fear|fear]]_ for 1 round unless it resists with a DC 19 Will save. Any creature that makes this saving throw is instead _[[conditions/Shaken|shaken]]_ for 1 round. This is a _fear_ effect. The DC is Charisma-based.

**Infused Arrows (Su)** A _baykok_ creates arrows of bone as it fires its bow—it need not carry arrows as ammunition. These bone arrows do normal damage for arrows fired from the bow, but gain a +1 enhancement bonus on attack and damage rolls. In addition, each arrow deals an additional 1d6 points of negative energy on a hit. Further, the first creature struck in a round by a _baykok_’s arrow must make a DC 19 Fortitude save to avoid being _paralyzed_ for 1d3 rounds. A _baykok_ can fire normal arrows from its bow if it wishes—such arrows, however, do not gain the special negative energy damage or _paralysis_ effects. The DC is Charisma-based.

##### Description

When hunters become utterly obsessed with the chase and indulge excessively in the savagery of the kill, their souls become progressively tainted. When such remorseless hunters perish before they can capture and kill their quarry, they sometimes rise from death as baykoks—flying undead horrors that kill purely for the ecstasy that only murder can bring them.

Unlike many undead who feed on and hate all living things, a _baykok_ seeks always to prove its mastery of the hunt. Though thoroughly wicked, baykoks often ignore all but the most powerful-looking foe in a group, only picking off lesser creatures if they dare to get between the _baykok_ and its true prey. When it finally lays low its quarry, the _baykok_ swoops down on the victim to devour the creature’s soul in an attempt to make sure the creature never returns to seek revenge.
---
cssclass: [monsters]
title1: Indarugant
desc_short: Taut, leathery skin clings to the skeleton of this giant, whose hide garments
  only partially conceal the simple geometric tattoos and ancient battle scars that
  decorate his flesh.
title2: Indarugant
CR: 14
sources:
- name: 'Pathfinder #94: Ice Tomb of the Giant Queen'
  page: 86
  link: http://paizo.com/products/btpy9dz6?Pathfinder-Adventure-Path-94-Ice-Tomb-of-the-Giant-Queen
XP: 38400
alignment: CE
size: Huge
type: undead
initiative:
  bonus: 2
senses:
  darkvision: 60
AC:
  AC: 29
  touch: 11
  flat_footed: 26
  components:
    armor: 4
    dex: 2
    dodge: 1
    natural: 14
    size: -2
HP:
  HP: 190
  long: 20d8+100
saves:
  fort: 10
  ref: 10
  will: 16
defensive_abilities:
- channel resistance +4
DR:
- amount: 5
  weakness: '-'
immunities:
- cold
- undead traits
SR: 25
speeds:
  base: 30
  base_other: 40 ft. without armor
attacks:
  melee:
  - - text: battleaxe +23/+18/+13 (3d6+15/19-20/×3)
      entries:
      - - damage: 3d6+15
          crit_range: 19-20
          crit_multiplier: 3
      attack: battleaxe
      bonus:
      - 23
      - 18
      - 13
  - - text: 2 slams +23 (1d8+10 plus curse of frozen flesh)
      entries:
      - - damage: 1d8+10
        - effect: curse of frozen flesh
      count: 2
      attack: slams
      bonus:
      - 23
  ranged:
  - - text: rock +16 (2d6+10)
      entries:
      - - damage: 2d6+10
      attack: rock
      bonus:
      - 16
  special:
  - curse of frozen flesh
  - lingering curses
  - rock throwing (120 ft.)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - superscripts:
    - APG
    name: ill omen
    source: default
    freq: At will
  - name: bestow curse
    source: default
    freq: 3/day
    DC: 18
  - name: blindness/deafness
    source: default
    freq: 3/day
    DC: 17
  - name: cone of cold
    source: default
    freq: 1/day
    DC: 19
  sources:
  - name: default
    CL: 15
    concentration: 19
ability_scores:
  STR: 31
  DEX: 14
  CON:
  INT: 12
  WIS: 19
  CHA: 19
BAB: 15
CMB: 27
CMD: 40
feats:
- name: Combat Reflexes
- name: Dodge
- name: Intimidating Prowess
- name: Lightning Reflexes
- name: Mobility
- name: Point-Blank Shot
- name: Power Attack
- name: Precise Shot
- name: Toughness
- name: Vital Strike
skills:
  Climb: 17
  Intimidate: 37
  Knowledge (religion): 7
  Perception: 27
  Sense Motive: 17
  Stealth: 14
  Survival: 24
languages:
- Common
- Giant
ecology:
  environment: cold mountains
  organization: solitary or warband (1 indarugant and 2-6 taiga giants)
  treasure_type: standard
  treasure:
  - hide armor
  - spear
special_abilities:
  Curse of Frozen Flesh (Su): Slam-contact; save Will DC 24; effect Creature gains
    vulnerability to cold. Anytime the cursed creature fails a saving throw against
    a spell or effect with the cold descriptor, it is also slowed for 1d4 rounds.
  Lingering Curses (Su): An indarugant is an accursed creature, and so has dominion
    over misfortune and curses. An indarugant can apply the effects of its curse of
    frozen flesh with its bestow curse spell-like ability (in place of bestow curse's
    normal effects). Additionally, the DC of any attempt to remove a curse inflicted
    by the indarugant increases by 5. If a caster level check to remove an indarugant's
    curse fails by 5 or more, the curse appears to be lifted and is temporarily suppressed
    until the next time the victim enters combat or is otherwise faced with a life-threatening
    situation (subject to the GM's discretion).
desc_long: |-
  In times of need, the taiga giants of Varisia turn to the spirits of their ancestors for aid, relying on signs and omens from the spirit world to guide them out of danger. Yet sometimes the power and insight of these ancestral spirits is not enough. When invaders overhunt the land, when disease and pestilence run rampant, or when war and slavery threaten to decimate whole tribes, some giants seek a different sort of aid-one that comes at a far higher price. High above the snow line, trapped within ancient glacial floes, the indarugants wait to be unleashed so they might once again bring disaster and ruin to the enemies of their tribes.

  Most indarugants resemble the desiccated corpses of taiga giants, though other types of giants may become indarugants as well. After taiga giants, stone giants are the most likely to follow through with this ritual, though by doing so they risk being shunned by neighboring tribes.

  Indarugants stand 20 feet tall, but weigh only 3,000 pounds due to the lack of water in their shriveled, skeletal bodies. The ritual that creates an indarugant involves marking and maiming the body of the candidate, and many still bear these fading tattoos and ancient scars.

---

# Indarugant
Taut, leathery skin clings to the skeleton of this giant, whose hide garments only partially conceal the simple geometric tattoos and ancient battle scars that decorate his flesh.
**Source** Pathfinder #94: Ice Tomb of the Giant Queen pg. 86
**XP** 38,400
CE Huge undead
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +27

##### Defense

**AC** 29, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+4 armor, +2 Dex, +1 dodge, +14 natural, –2 size)
**hp** 190 (20d8+100)
**Fort** +10, **Ref** +10, **Will** +16
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4; **DR** 5/—; **Immune** cold, _[[universal monster rules/Undead Traits|undead traits]]_; **SR** 25

##### Offense
**Speed** 30 ft. (40 ft. without armor)
**Melee** _[[items/Weapon/Battleaxe|battleaxe]]_ +23/+18/+13 (3d6+15/19–20/×3) or 2 slams +23 (1d8+10 plus curse of frozen flesh)
**Ranged** rock +16 (2d6+10)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** curse of frozen flesh, lingering curses, _[[universal monster rules/Rock Throwing|rock throwing]]_ (120 ft.)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +19)
At will—_[[spells/Ill Omen|ill omen]]_
3/day—_[[spells/Bestow Curse|bestow curse]]_ (DC 18), blindness/deafness (DC 17)
1/day—_[[spells/Cone of Cold|cone of cold]]_ (DC 19)

##### Statistics
**Str** 31, **Dex** 14, **Con** —, **Int** 12, **Wis** 19, **Cha** 19
**Base Atk** +15; **CMB** +27; **CMD** 40
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Intimidating Prowess|Intimidating Prowess]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +17, Intimidate +37, Knowledge (religion) +7, Perception +27, Sense Motive +17, Stealth +14, Survival +24
**Languages** Common, Giant

##### Ecology

**Environment** cold mountains
**Organization** solitary or warband (1 _[[monsters/Indarugant|indarugant]]_ and 2–6 taiga giants)
**Treasure** standard (_[[items/Armor/Hide armor|hide armor]]_, _[[items/Weapon/Spear|spear]]_)

### Special Abilities

**Curse of Frozen Flesh (Su)** Slam—contact; save Will DC 24; effect Creature gains _[[curses/Vulnerability|vulnerability]]_ to cold. Anytime the cursed creature fails a saving throw against a spell or effect with the cold descriptor, it is also slowed for 1d4 rounds.

**Lingering Curses (Su)** An _indarugant_ is an _[[feats/Accursed|accursed]]_ creature, and so has dominion over misfortune and curses. An _indarugant_ can apply the effects of its curse of frozen flesh with its _bestow curse_ spell-like ability (in place of _bestow curse_’s normal effects). Additionally, the DC of any attempt to remove a curse inflicted by the _indarugant_ increases by 5. If a caster level check to remove an _indarugant_’s curse fails by 5 or more, the curse appears to be lifted and is temporarily suppressed until the next time the victim enters combat or is otherwise faced with a life-threatening situation (subject to the GM’s discretion).

##### Description

In times of need, the taiga giants of Varisia turn to the spirits of their ancestors for aid, relying on signs and omens from the spirit world to guide them out of danger. Yet sometimes the power and insight of these ancestral spirits is not enough. When invaders overhunt the land, when disease and pestilence run rampant, or when war and slavery threaten to decimate whole tribes, some giants seek a different sort of aid—one that comes at a far higher price. High above the snow line, trapped within ancient glacial floes, the indarugants wait to be unleashed so they might once again bring disaster and ruin to the enemies of their tribes.

Most indarugants resemble the desiccated corpses of taiga giants, though other types of giants may become indarugants as well. After taiga giants, stone giants are the most likely to follow through with this ritual, though by doing so they risk being shunned by neighboring tribes.

Indarugants stand 20 feet tall, but weigh only 3,000 pounds due to the lack of water in their shriveled, skeletal bodies. The ritual that creates an _indarugant_ involves marking and maiming the body of the candidate, and many still bear these fading tattoos and ancient scars.
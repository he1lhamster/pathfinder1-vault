---
cssclass: [monsters]
title1: Troll
desc_short: This giant humanoid has massive tusks, warty green hide sprouting bone
  spikes, and forearms thicker than its meaty legs.
title2: Mythic Troll
CR: 6
MR: 2
sources:
- name: Mythic Adventures
  page: 219
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 2400
alignment: CE
size: Large
type: humanoid
subtypes:
- giant
- mythic
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 18
  touch: 11
  flat_footed: 16
  components:
    dex: 2
    natural: 7
    size: -1
HP:
  HP: 79
  long: 6d8+52
  regeneration: 5
  regeneration_weakness: acid or fire, see primal vigor
saves:
  fort: 11
  ref: 4
  will: 3
defensive_abilities:
- primal vigor
DR:
- amount: 5
  weakness: epic
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +9 (1d8+6)
      entries:
      - - damage: 1d8+6
      attack: bite
      bonus:
      - 9
    - text: 2 claws +9 (1d6+6)
      entries:
      - - damage: 1d6+6
      count: 2
      attack: claws
      bonus:
      - 9
  special:
  - feral savagery (rend)
  - mythic power (2/day, surge +1d6)
  - rend (2 claws, 1d6+9 plus bleed 5 plus feral savagery)
space: 10
reach: 10
ability_scores:
  STR: 23
  DEX: 14
  CON: 23
  INT: 6
  WIS: 9
  CHA: 6
BAB: 4
CMB: 11
CMD: 23
feats:
- name: Intimidating Prowess
- is_mythic: true
  name: Iron Will
- name: Skill Focus (Perception)
skills:
  Intimidate: 10
  Perception: 8
languages:
- Giant
ecology:
  environment: cold mountains
  organization: solitary or gang (2-4)
  treasure_type: standard
special_abilities:
  Primal Vigor (Su): If a mythic troll takes damage during a round, its regeneration
    increases by 5 at the start of its next turn, to a maximum of 25. If the troll
    is at full hit points at the start of its turn, its regeneration decreases by
    5, to a minimum of 5. Damaging the troll with acid or fire only partially suppresses
    its regeneration. On its turn following this damage, the troll regenerates only
    half the normal number of hit points (for example, a troll with regeneration 15
    would heal 7 hit points) and can die normally on that round.
desc_long: A mythic troll's skin is nearly as hard as stone, with bony growths, ornamental
  head spikes, and oversized teeth adding to its already grotesque visage.

---

# Troll
This tall creature has rough, green hide. Its hands end in claws, and its bestial face has a hideous, tusked underbite.
**Source** Pathfinder RPG Bestiary pg. 268
**XP** 1,600
CE Large humanoid (giant)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +8

##### Defense

**AC** 16, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+2 Dex, +5 natural, –1 size)
**hp** 63 (6d8+36); _[[universal monster rules/Regeneration|regeneration]]_ 5 (acid or fire)
**Fort** +11, **Ref** +4, **Will** +3

##### Offense
**Speed** 30 ft.
**Melee** bite +8 (1d8+5), 2 claws +8 (1d6+5)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Rend|rend]]_ (2 claws, 1d6+7)

##### Statistics
**Str** 21, **Dex** 14, **Con** 23, **Int** 6, **Wis** 9, **Cha** 6
**Base Atk** +4; **CMB** +10; **CMD** 22
**Feats** _[[feats/Intimidating Prowess|Intimidating Prowess]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** Intimidate +9, Perception +8
**Languages** Giant

##### Ecology

**Environment** cold mountains
**Organization** solitary or gang (2–4)
**Treasure** standard

##### Description

Trolls possess incredibly sharp claws and amazing regenerative powers, allowing them to recover from nearly any wound. They are stooped, fantastically ugly, and astonishingly strong—combined with their claws, their strength allows them to literally tear apart flesh to feed their voracious appetites. Trolls stand about 14 feet tall, but their hunched postures often make them appear shorter. An adult _[[monsters/Troll|troll]]_ weighs around 1,000 pounds.

A _troll_’s appetite and its regenerative powers make it a fearless combatant, ever prepared to charge headlong at the nearest living creature and attack with all of its fury. Only fire seems to cause a _troll_ to hesitate, but even this mortal threat is not enough to stop a _troll_’s advance. Those who commonly battle with trolls know to locate and _[[universal monster rules/Burn|burn]]_ any pieces after a fight, for even the smallest scrap of flesh can regrow a full-size _troll_ given enough time. Fortunately, only the largest part of a _troll_ regrows in this way.

Despite their _[[feats/Cruelty|cruelty]]_ in combat, trolls are surprisingly tender and kind to their own young. Female trolls work as a group, spending a great deal of time teaching young trolls to hunt and fend for themselves before _[[spells/Sending|sending]]_ them off to find their own territories. A male _troll_ tends to live a solitary existence, partnering with a female for only a brief time to mate. All trolls spend most of their time hunting for food, as they must consume vast amounts each day or face starvation. Due to this need, most trolls stake out large territories as their own, and fights between rivals are quite common. While these are usually nonlethal, trolls are aware of each others’ weaknesses and will use such knowledge to kill their own kind if food is scarce.
---
cssclass: [monsters]
title1: Giant, Wood Giant
desc_short: Standing tall and graceful, this sharp-eared giant's skin is pale. Its
  large brow gives it a somewhat primitive visage.
title2: Wood Giant
CR: 6
sources:
- name: Bestiary 2
  page: 132
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 2400
alignment: CG
size: Large
type: humanoid
subtypes:
- giant
initiative:
  bonus: 5
senses:
  low-light vision: true
AC:
  AC: 20
  touch: 14
  flat_footed: 15
  components:
    armor: 2
    dex: 5
    natural: 4
    size: -1
HP:
  HP: 67
  long: 9d8+27
saves:
  fort: 9
  ref: 8
  will: 7
defensive_abilities:
- rock catching
speeds:
  base: 40
attacks:
  melee:
  - - text: longsword +10/+5 (2d6+5/19-20)
      entries:
      - - damage: 2d6+5
          crit_range: 19-20
      attack: longsword
      bonus:
      - 10
      - 5
  - - text: 2 slams +10 (1d6+5)
      entries:
      - - damage: 1d6+5
      count: 2
      attack: slams
      bonus:
      - 10
  ranged:
  - - text: mwk composite longbow +9/+9/+4 (2d6+5/×3)
      entries:
      - - damage: 2d6+5
          crit_multiplier: 3
      attack: mwk composite longbow
      bonus:
      - 9
      - 9
      - 4
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: pass without trace
    source: default
    freq: Constant
  - name: speak with animals
    source: default
    freq: Constant
  - name: charm animal
    source: default
    freq: 3/day
    DC: 12
  - name: quench
    source: default
    freq: 3/day
  - name: tree shape
    source: default
    freq: 3/day
  - name: enlarge person
    source: default
    freq: 1/day
    other: self only
  - name: spike growth
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 7
    concentration: 8
ability_scores:
  STR: 20
  DEX: 21
  CON: 17
  INT: 14
  WIS: 15
  CHA: 12
BAB: 6
CMB: 12
CMD: 27
feats:
- name: Deadly Aim
- name: Iron Will
- name: Point-Blank Shot
- name: Precise Shot
- name: Rapid Shot
skills:
  Acrobatics: 11
    when jumping: 15
  Climb: 14
  Knowledge (nature): 8
  Perception: 11
  Profession (farmer): 8
  Stealth: 7
    in forests: 11
  Survival: 8
  _racial_mods:
    Stealth:
      in forests: 4
languages:
- Common
- Giant
- Sylvan
- speak with animals
ecology:
  environment: temperate forests
  organization: solitary, gang (2-4), hunting party (5-9, plus 1-4 dire wolves), or
    clan (10-40, plus 35% noncombatants, 1-3 druids or witches of 2nd-4th level, 1
    ranger chieftain of 3rd-7th level, 4-10 dire wolves, and 2-8 giant eagles)
  treasure_type: standard
  treasure:
  - leather armor
  - longsword
  - masterwork composite longbow with 20 arrows
  - other treasure
desc_long: |-
  Wood giants are the wardens of the deepest, wildest portions of the world's forests. Unlike many of their kin, wood giants are slow to anger, peaceful, and artistic, and display an infinite patience in their duty. A wood giant's role is to preserve and protect the wilderness-a role they believe that nature itself granted them, the proof of which manifests in their magical abilities tied to the natural world.

  Wood giant culture is as complex as their forest homes. Much of a tribe's time is spent tending to a forest's health: planting new trees, clearing away dead brush, and hunting abominations that pervert the natural order. Individuals may even cultivate their forest homes into elaborate demesnes, mazes, or living temples. They are an isolated race, only rarely meeting to trade with other tribes or the occasional elven settlement. While primarily good-natured, wood giants are distrustful of outsiders and prone to great melancholies.

  Small clans claim enormous tracts of wooded land, but rarely build permanent homes. Members may spread out over their entire region by day only to gather and bed down, exposed to the elements, after sundown. In harsh weather, tribes cluster close together in the densest thickets with their backs turned outward.

  Wood giants stand 14 feet tall and weigh 1,200 pounds. They are vegetarians by choice, resorting to eating meat only when no other option is available.

---

# Giant, Wood Giant
_[[feats/Standing Tall|Standing tall]]_ and graceful, this sharp-eared giant’s skin is pale. Its large brow gives it a somewhat primitive visage.
**Source** Bestiary 2 pg. 132
**XP** 2,400

CG Large humanoid (giant)
**Init** +5; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +11

##### Defense

**AC** 20, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+2 armor, +5 Dex, +4 natural, –1 size)
**hp** 67 (9d8+27)
**Fort** +9, **Ref** +8, **Will** +7
**Defensive Abilities** _[[universal monster rules/Rock Catching|rock catching]]_

##### Offense
**Speed** 40 ft.
**Melee** _[[items/Weapon/Longsword|longsword]]_ +10/+5 (2d6+5/19–20) or 2 slams +10 (1d6+5)
**Ranged** mwk _[[items/Weapon/Composite longbow|composite longbow]]_ +9/+9/+4 (2d6+5/×3)
**Space** 10 ft., **Reach** 10 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +8)
Constant—_[[spells/Pass without Trace|pass without trace]]_, _[[spells/Speak with Animals|speak with animals]]_
3/day—_[[spells/Charm Animal|charm animal]]_ (DC 12), _[[spells/Quench|quench]]_, _[[spells/Tree Shape|tree shape]]_
1/day—_[[spells/Enlarge Person|enlarge person]]_ (self only), _[[spells/Spike Growth|spike growth]]_

##### Statistics
**Str** 20, **Dex** 21, **Con** 17, **Int** 14, **Wis** 15, **Cha** 12
**Base Atk** +6; **CMB** +12; **CMD** 27
**Feats** _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_
**Skills** Acrobatics +11 (+15 when jumping), _[[universal monster rules/Climb|Climb]]_ +14, Knowledge (nature) +8, Perception +11, Profession (farmer) +8, Stealth +7 (+11 in forests), Survival +8; **Racial Modifiers** +4 Stealth in forests
**Languages** Common, Giant, Sylvan; _speak with animals_

##### Ecology

**Environment** temperate forests
**Organization** solitary, gang (2–4), hunting party (5–9, plus 1–4 dire wolves), or clan (10–40, plus 35% noncombatants, 1–3 druids or witches of 2nd–4th level, 1 _[[classes/Ranger|ranger]]_ chieftain of 3rd–7th level, 4–10 dire wolves, and 2–8 giant eagles)
**Treasure** standard (_[[items/Armor/Leather armor|leather armor]]_, _longsword_, masterwork _composite longbow_ with 20 arrows, other treasure)

##### Description

Wood giants are the wardens of the deepest, wildest portions of the world’s forests. Unlike many of their kin, wood giants are _[[spells/Slow|slow]]_ to anger, _[[items/Weapon Magic Abilities/Peaceful|peaceful]]_, and artistic, and display an infinite patience in their duty. A wood giant’s role is to _[[spells/Preserve|preserve]]_ and protect the wilderness—a role they believe that nature itself granted them, the proof of which manifests in their magical abilities tied to the natural world.

Wood giant culture is as complex as their forest homes. Much of a tribe’s time is spent tending to a forest’s health: planting new trees, clearing away dead brush, and hunting abominations that pervert the natural order. Individuals may even cultivate their forest homes into elaborate demesnes, mazes, or living temples. They are an isolated race, only rarely meeting to trade with other tribes or the occasional elven settlement. While primarily good-natured, wood giants are distrustful of outsiders and _[[conditions/Prone|prone]]_ to great melancholies.

Small clans claim enormous tracts of wooded land, but rarely build permanent homes. Members may spread out over their entire region by day only to gather and bed down, exposed to the elements, after sundown. In harsh weather, tribes cluster close together in the densest thickets with their backs turned outward.

Wood giants stand 14 feet tall and weigh 1,200 pounds. They are vegetarians by choice, resorting to eating meat only when no other option is available.
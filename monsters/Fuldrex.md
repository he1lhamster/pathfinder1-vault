---
cssclass: [monsters]
title1: Fuldrex
desc_short: This minuscule, fleshy plant creature has mottled, green-andblack skin
  and tiny eyes that peer malevolently from beneath layers of dripping, fungal hair.
title2: Fuldrex
CR: 11
sources:
- name: 'Pathfinder #119: Prisoners of the Blight'
  page: 84
  link: http://paizo.com/products/btpy9npn
XP: 12800
alignment: NE
size: Small
type: plant
initiative:
  bonus: 5
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 27
  touch: 12
  flat_footed: 26
  components:
    dex: 1
    natural: 15
    size: 1
HP:
  HP: 168
  long: 16d8+96
saves:
  fort: 16
  ref: 8
  will: 6
immunities:
- electricity
- plant traits
- sonic
weaknesses:
- light sensitivity
speeds:
  base: 20
attacks:
  melee:
  - - text: bite +21 (2d6+8/19-20)
      entries:
      - - damage: 2d6+8
          crit_range: 19-20
      attack: bite
      bonus:
      - 21
    - text: 3 slams +21 (1d8+8 plus choking fungus)
      entries:
      - - damage: 1d8+8
        - effect: choking fungus
      count: 3
      attack: slams
      bonus:
      - 21
  special:
  - choking fungus
  - rotten flesh
spell_like_abilities:
  entries:
  - name: pass without trace
    source: default
    freq: Constant
  - name: entangle
    source: default
    freq: 3/day
    other: underground only
    DC: 13
  sources:
  - name: default
    CL: 10
    concentration: 12
ability_scores:
  STR: 26
  DEX: 12
  CON: 22
  INT: 7
  WIS: 13
  CHA: 15
BAB: 12
CMB: 19
CMD: 30
feats:
- name: Alertness
- name: Combat Reflexes
- name: Diehard
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Lightning Reflexes
- name: Lunge
- name: Power Attack
skills:
  Perception: 14
  Sense Motive: 3
  Stealth: 16
    when underground: 20
  _racial_mods:
    Stealth:
      when underground: 4
languages:
- Abyssal
- Sylvan
special_qualities:
- change shape (Small fungus; tree shape)
ecology:
  environment: temperate forests or underground
  organization: solitary, pair, or infestation (8-12)
  treasure_type: standard
special_abilities:
  Choking Fungus (Ex): When a fuldrex hits a target with its slam attack, it releases
    minuscule, virulent spores that seek to propagate in the victim's lungs. A creature
    struck by the fuldrex's slam attack takes 1d6 points of Constitution damage and
    is staggered for 1d4 rounds while it painfully coughs out the intrusive fungus.
    A victim that succeeds at a DC 24 Fortitude saving throw is staggered for only
    1 round and doesn't take ability damage. A creature affected by this ability is
    immune to additional instances of choking fungus as long as it remains staggered
    from the effect. This is a disease effect that affects only creatures that breathe.
    The saving throw is Fortitude-based.
  Rotten Flesh (Ex): The fleshy fungus that makes up a fuldrex's body is fetid and
    foul. Whenever a fuldrex takes damage from a slashing weapon, its flesh releases
    a noxious cloud of gas. Creatures within 10 feet of the fuldrex must succeed at
    a DC 26 Fortitude saving throw or be nauseated for 1 round.
desc_long: |-
  Fuldrexes are mean, territorial creatures that, despite naturally taking the shape of small humanoids, seem to share more physical characteristics with fungi than anything else. Layers of thin, spotted, fibrous flesh cover their bodies like skin; their chubby fingers seem more like mushroom stalks than digits; and where hair might normally grow instead drips lacy growths that would seem more at home growing along the walls of a cave. Fuldrexes crave warm, dark, isolated places, and react violently when disturbed. The exception is when a much more powerful creature-particularly a fungal creature (see pages 116-117 of the Pathfinder RPG Bestiary 4)-enters their demesne with an overwhelming display of might. In this case, the cowardly and dull creatures are apt to prostrate themselves before their better, vowing to serve and venerate it as other creatures might worship a deity.

   Fuldrexes are notorious shapechangers that can appear to be naturally occurring fungi whenever they wish. They often use this ability to blend in with their surroundings before ambushing their enemies, or simply to fade from sight when a major threat barrels their way. In its natural form, a fuldrex stands 2-1/2 feet tall and weighs 50 pounds.

---

# Fuldrex
This minuscule, fleshy plant creature has mottled, green-andblack skin and tiny eyes that peer malevolently from beneath layers of dripping, fungal hair.
**Source** Pathfinder #119: Prisoners of the _[[spells/Blight|Blight]]_ pg. 84
**XP** 12,800

NE Small plant
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +14

##### Defense

**AC** 27, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+1 Dex, +15 natural, +1 size)
**hp** 168 (16d8+96)
**Fort** +16, **Ref** +8, **Will** +6
**Immune** electricity, _[[universal monster rules/Plant Traits|plant traits]]_, sonic
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_

##### Offense
**Speed** 20 ft.
**Melee** bite +21 (2d6+8/19–20), 3 slams +21 (1d8+8 plus choking fungus)
**Special Attacks** choking fungus, rotten flesh
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +12)
Constant—_[[spells/Pass without Trace|pass without trace]]_
3/day—_[[spells/Entangle|entangle]]_ (underground only; DC 13)

##### Statistics
**Str** 26, **Dex** 12, **Con** 22, **Int** 7, **Wis** 13, **Cha** 15
**Base Atk** +12; **CMB** +19; **CMD** 30
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Diehard|Diehard]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Perception +14, Sense Motive +3, Stealth +16 (+20 when underground); **Racial Modifiers** +4 Stealth when underground
**Languages** Abyssal, Sylvan
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (Small fungus; _[[spells/Tree Shape|tree shape]]_)

##### Ecology

**Environment** temperate forests or underground
**Organization** solitary, pair, or infestation (8–12)
**Treasure** standard

### Special Abilities

**Choking Fungus (Ex)** When a _[[monsters/Fuldrex|fuldrex]]_ hits a target with its slam attack, it releases minuscule, _[[items/Weapon Magic Abilities/Virulent|virulent]]_ spores that seek to propagate in the victim’s lungs. A creature struck by the _fuldrex_’s slam attack takes 1d6 points of Constitution damage and is _[[conditions/Staggered|staggered]]_ for 1d4 rounds while it painfully coughs out the intrusive fungus. A victim that succeeds at a DC 24 Fortitude saving throw is _staggered_ for only 1 round and doesn’t take ability damage. A creature affected by this ability is immune to additional instances of choking fungus as long as it remains _staggered_ from the effect. This is a disease effect that affects only creatures that breathe. The saving throw is Fortitude-based.

**Rotten Flesh (Ex)** The fleshy fungus that makes up a _fuldrex_’s body is fetid and foul. Whenever a _fuldrex_ takes damage from a slashing weapon, its flesh releases a noxious cloud of gas. Creatures within 10 feet of the _fuldrex_ must succeed at a DC 26 Fortitude saving throw or be _[[conditions/Nauseated|nauseated]]_ for 1 round.

##### Description

Fuldrexes are mean, territorial creatures that, despite naturally taking the shape of small humanoids, seem to share more physical characteristics with fungi than anything else. Layers of thin, spotted, fibrous flesh cover their bodies like skin; their chubby fingers seem more like mushroom stalks than digits; and where hair might normally grow instead drips lacy growths that would seem more at home _[[items/Weapon Magic Abilities/Growing|growing]]_ along the walls of a cave. Fuldrexes crave warm, dark, isolated places, and react violently when disturbed. The exception is when a much more powerful creature—particularly a fungal creature (see pages 116–117 of the Pathfinder RPG Bestiary 4)—enters their demesne with an overwhelming display of might. In this case, the cowardly and dull creatures are apt to prostrate themselves before their better, vowing to serve and venerate it as other creatures might worship a deity.

Fuldrexes are notorious shapechangers that can appear to be naturally occurring fungi whenever they _[[spells/Wish|wish]]_. They often use this ability to _[[spells/Blend|blend]]_ in with their surroundings before ambushing their enemies, or simply to fade from sight when a major threat barrels their way. In its natural form, a _fuldrex_ stands 2-1/2 feet tall and weighs 50 pounds.
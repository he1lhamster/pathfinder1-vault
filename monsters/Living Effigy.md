---
cssclass: [monsters]
title1: Living Effigy
desc_short: Carved from gray stone, this enormous figure is shaped like the head of
  some primordial giant.
title2: Living Effigy
CR: 8
sources:
- name: 'Pathfinder #94: Ice Tomb of the Giant Queen'
  page: 88
  link: http://paizo.com/products/btpy9dz6?Pathfinder-Adventure-Path-94-Ice-Tomb-of-the-Giant-Queen
XP: 4800
alignment: N
size: Huge
type: construct
initiative:
  bonus: -2
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 20
  touch: 6
  flat_footed: 20
  components:
    dex: -2
    natural: 14
    size: -2
HP:
  HP: 95
  long: 10d10+40
saves:
  fort: 3
  ref: 1
  will: 6
DR:
- amount: 10
  weakness: adamantine
immunities:
- construct traits
weaknesses:
- susceptible to mind-affecting effects
speeds:
  base: 0
  fly: 10
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: slam +13 (2d8+7/19-20)
      entries:
      - - damage: 2d8+7
          crit_range: 19-20
      attack: slam
      bonus:
      - 13
  special:
  - charming gaze
space: 15
reach: 5
spell_like_abilities:
  entries:
  - name: detect thoughts
    source: default
    freq: At will
    DC: 15
  - name: obscuring mist
    source: default
    freq: At will
  - name: sound burst
    source: default
    freq: At will
    DC: 15
  - name: calm emotions
    source: default
    freq: 3/day
    DC: 15
  - name: crushing despair
    source: default
    freq: 3/day
    DC: 17
  - name: good hope
    source: default
    freq: 3/day
  - name: empowered sound burst
    source: default
    freq: 3/day
    DC: 15
  - name: stone shape
    source: default
    freq: 3/day
  - superscripts:
    - APG
    name: thundering drums
    source: default
    freq: 3/day
    DC: 16
  - superscripts:
    - APG
    name: arcane concordance
    source: default
    freq: 1/day
  - name: fear
    source: default
    freq: 1/day
    DC: 17
  - superscripts:
    - UM
    name: witness
    source: default
    freq: 1/day
    DC: 16
  - name: dream
    source: default
    freq: 1/week
  - name: nightmare
    source: default
    freq: 1/week
    DC: 18
  sources:
  - name: default
    CL: 10
    concentration: 13
ability_scores:
  STR: 20
  DEX: 7
  CON:
  INT: 13
  WIS: 16
  CHA: 17
BAB: 10
CMB: 17
CMD: 25
CMD_other: can't be tripped
feats:
- name: Empower Spell-Like Ability (sound burst)
- name: Hover
- name: Improved Critical (slam)
- name: Skill Focus (Intimidate)
- name: Skill Focus (Perception)
skills:
  Fly: 2
  Intimidate: 12
  Knowledge (history): 10
  Knowledge (religion): 10
  Perception: 19
  Sense Motive: 8
  Spellcraft: 6
  _racial_mods:
    Knowledge (history):
      _: 4
    Knowledge (religion):
      _: 4
languages:
- Common
- Giant
special_qualities:
- preserved mind
- silent watcher
- statue
ecology:
  environment: any
  organization: solitary
  treasure_type: incidental
  treasure:
  - offerings
  - 2 eye gems worth 500 gp each
special_abilities:
  Charming Gaze (Su): As charm person with a range of 30 feet (Will DC 18 negates).
    The save DC is Charisma-based.
  Preserved Mind (Ex): A living effigy is inhabited by an entrenched spirit that holds
    on to some aspects of its former intellect. A living effigy can choose two Knowledge
    skills, typically Knowledge (history) and Knowledge (religion). These Knowledge
    skills are class skills for the living effigy, and it gains a +4 racial bonus
    on checks with these skills.
  Shape Self (Sp): Three times a day, a living effigy can shift its facial expression
    as if using stone shape, even though the construct exceeds the volume the spell
    can usually affect and is a creature rather than an object.
  Silent Watcher (Su): As a standard action, a living effigy can use greater teleport
    (self only) as long as there are no creatures with an Intelligence score higher
    than 2 within 150 feet that can see the effigy. When using this ability, the living
    effigy can travel up to 10 miles from its settlement.
  Statue (Ex): A living effigy can remain perfectly still and emulate a statue. An
    observer must succeed at a DC 25 Perception check to notice that the living effigy
    is alive. If a living effigy initiates combat from this pose, it gains a +6 bonus
    on its initiative check.
  Susceptible to Mind-Affecting Effects (Ex): Unlike most constructs, a living effigy
    isn't immune to mind-affecting effects.
desc_long: |-
  Resting among countless tribes across the world are strange icons and statues dedicated to the memories of ancient leaders or spiritual guides. Sometimes such figures hide greater intellects, inhabiting essences that watch over nearby settlements. Known as living effigies, these stone statues are possessed by the spirits of deceased chieftains and shamans who managed to partially cheat death by imparting a portion of their souls into stone images. Each living effigy is unique in its features-some resemble the heads of great giants, while others are busts of other creatures. Twin gems are embedded in the eyes of each living effigy; they glow a vibrant color whenever the statue uses one of its many magical abilities.

  A living effigy's personality is as unique as its countenance, as the souls inhabiting the massive stones range from kind protectors wishing to continue their vigil over a settlement to brutal tyrants wishing only to reign past death. A living effigy stands 15 feet tall and weighs 40 tons.

---

# Living Effigy
Carved from _[[monsters/Gray|gray]]_ stone, this enormous figure is shaped like the head of some primordial giant.
**Source** Pathfinder #94: Ice Tomb of the Giant Queen pg. 88
**XP** 4,800

N Huge construct
**Init** –2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +19

##### Defense

**AC** 20, touch 6, _[[conditions/Flat-Footed|flat-footed]]_ 20 (–2 Dex, +14 natural, –2 size)
**hp** 95 (10d10+40)
**Fort** +3, **Ref** +1, **Will** +6
**DR** 10/adamantine; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_
**Weaknesses** susceptible to mind-affecting effects

##### Offense
**Speed** 0 ft., fly 10 ft. (perfect)
**Melee** slam +13 (2d8+7/19–20)
**Space** 15 ft., **Reach** 5 ft.
**Special Attacks** charming _[[universal monster rules/Gaze|gaze]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +13)
At will—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 15), _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Sound Burst|sound burst]]_ (DC 15)
3/day—_[[spells/Calm Emotions|calm emotions]]_ (DC 15), _[[spells/Crushing Despair|crushing despair]]_ (DC 17), _[[spells/Good Hope|good hope]]_, empowered _sound burst_ (DC 15), _[[spells/Stone Shape|stone shape]]_, _[[spells/Thundering Drums|thundering drums]]_ (DC 16)
1/day—_[[spells/Arcane Concordance|arcane concordance]]_, _[[universal monster rules/Fear|fear]]_ (DC 17), _[[spells/Witness|witness]]_ (DC 16)
1/week—_[[spells/Dream|dream]]_, _[[spells/Nightmare|nightmare]]_ (DC 18)

##### Statistics
**Str** 20, **Dex** 7, **Con** —, **Int** 13, **Wis** 16, **Cha** 17
**Base Atk** +10; **CMB** +17; **CMD** 25 (can’t be tripped)
**Feats** _[[feats/Empower Spell-Like Ability|Empower Spell-Like Ability]]_ (_sound burst_), _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (slam), _[[feats/Skill Focus|Skill Focus]]_ (Intimidate), _Skill Focus_ (Perception)
**Skills** Fly +2, Intimidate +12, Knowledge (history) +10, Knowledge (religion) +10, Perception +19, Sense Motive +8, Spellcraft +6; **Racial Modifiers** +4 Knowledge (history), +4 Knowledge (religion)
**Languages** Common, Giant
**SQ** preserved mind, silent _[[monsters/Watcher|watcher]]_, _[[spells/Statue|statue]]_

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** incidental (offerings, 2 eye gems worth 500 gp each)

### Special Abilities

**Charming _Gaze_ (Su)** As _[[spells/Charm Person|charm person]]_ with a range of 30 feet (Will DC 18 negates). The save DC is Charisma-based.

**Preserved Mind (Ex)** A _[[monsters/Living Effigy|living effigy]]_ is inhabited by an entrenched spirit that holds on to some aspects of its former intellect. A _living effigy_ can choose two Knowledge skills, typically Knowledge (history) and Knowledge (religion). These Knowledge skills are class skills for the _living effigy_, and it gains a +4 racial bonus on checks with these skills.
**Shape Self (Sp)** Three times a day, a _living effigy_ can shift its facial expression as if using _stone shape_, even though the construct exceeds the volume the spell can usually affect and is a creature rather than an object.
**Silent _Watcher_ (Su)** As a standard action, a _living effigy_ can use greater teleport (self only) as long as there are no creatures with an Intelligence score higher than 2 within 150 feet that can see the effigy. When using this ability, the _living effigy_ can travel up to 10 miles from its settlement.
**_Statue_ (Ex)** A _living effigy_ can remain perfectly still and emulate a _statue_. An observer must succeed at a DC 25 Perception check to notice that the _living effigy_ is alive. If a _living effigy_ initiates combat from this pose, it gains a +6 bonus on its initiative check.
**Susceptible to Mind-Affecting Effects (Ex)** Unlike most constructs, a _living effigy_ isn’t immune to mind-affecting effects.

##### Description

Resting among countless tribes across the world are strange icons and statues dedicated to the memories of ancient leaders or spiritual guides. Sometimes such figures hide greater intellects, inhabiting essences that watch over nearby settlements. Known as living effigies, these stone statues are possessed by the spirits of deceased chieftains and shamans who managed to partially cheat death by imparting a portion of their souls into stone images. Each _living effigy_ is unique in its features—some resemble the heads of great giants, while others are busts of other creatures. Twin gems are embedded in the eyes of each _living effigy_; they glow a vibrant color whenever the _statue_ uses one of its many magical abilities.

A _living effigy_’s personality is as unique as its countenance, as the souls inhabiting the massive stones range from kind protectors wishing to continue their vigil over a settlement to brutal tyrants wishing only to reign past death. A _living effigy_ stands 15 feet tall and weighs 40 tons.
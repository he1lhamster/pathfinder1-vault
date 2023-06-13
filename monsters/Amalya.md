---
cssclass: [monsters]
title1: Amalya
desc_short: 'This lithe, otherworldly woman has with deep brown eyes and dark green
  hair that cascades past her waist. She's adorned in trinkets made from a great white
  pine's needles and cones. '
title2: Amalya
CR: 6
sources:
- name: Fey Revisited
  page: 8
  link: http://paizo.com/products/btpy8xeb?Pathfinder-Campaign-Setting-Fey-Revisited
XP: 2400
race: Dryad
classes:
- druid 3 (Pathfinder RPG Bestiary 116)
alignment: CG
size: Medium
type: fey
initiative:
  bonus: 5
senses:
  low-light vision: true
AC:
  AC: 19
  touch: 16
  flat_footed: 14
  components:
    deflection: 1
    dex: 5
    natural: 3
HP:
  HP: 73
  long: 6d6+3d8+39
  HD: 9
saves:
  fort: 10
  ref: 11
  will: 12
DR:
- amount: 5
  weakness: cold iron
weaknesses:
- tree dependent
speeds:
  base: 30
attacks:
  melee:
  - - text: club +5 (1d6)
      entries:
      - - damage: 1d6
      attack: club
      bonus:
      - 5
    - text: dagger +10 (1d4)
      entries:
      - - damage: 1d4
      attack: dagger
      bonus:
      - 10
  ranged:
  - - text: mwk longbow +11 (1d8/×3)
      entries:
      - - damage: 1d8
          crit_multiplier: 3
      attack: mwk longbow
      bonus:
      - 11
spell_like_abilities:
  entries:
  - name: speak with plants
    source: default
    freq: Constant
  - name: entangle
    source: default
    freq: At will
    DC: 16
  - name: tree shape
    source: default
    freq: At will
  - name: wood shape
    source: default
    freq: At will
    other: 1 lb. only
  - name: charm person
    source: default
    freq: 3/day
    DC: 16
  - name: deep slumber
    source: default
    freq: 3/day
    DC: 18
  - name: tree stride
    source: default
    freq: 3/day
  - name: suggestion
    source: default
    freq: 1/day
    DC: 18
  sources:
  - name: default
    CL: 6
    concentration: 11
spells:
  entries:
  - is_domain_spell: true
    name: barkskin
    source: Druid
    level: 2
  - name: lesser restoration
    source: Druid
    level: 2
  - name: summon swarm
    source: Druid
    level: 2
  - name: cure light wounds
    source: Druid
    level: 1
  - is_domain_spell: true
    name: enlarge person
    source: Druid
    level: 1
  - name: obscuring mist
    source: Druid
    level: 1
  - name: shillelagh
    source: Druid
    level: 1
  - name: create water
    source: Druid
    level: 0
  - name: guidance
    source: Druid
    level: 0
  - name: mending
    source: Druid
    level: 0
  - name: stabilize
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 3
    concentration: 7
    slots:
      0: at-will
ability_scores:
  STR: 10
  DEX: 21
  CON: 17
  INT: 12
  WIS: 19
  CHA: 20
BAB: 5
CMB: 5
CMD: 21
feats:
- name: Great Fortitude
- name: Self-Sufficient
- name: Stealthy
- name: Toughness
- name: Weapon Finesse
skills:
  Climb: 9
  Craft (wood): 19
  Escape Artist: 19
  Handle Animal: 14
  Heal: 6
  Knowledge (nature): 12
  Perception: 13
  Stealth: 19
  Survival: 17
  _racial_mods:
    Craft (wood):
      _: 6
languages:
- Abyssal
- Common
- Druidic
- Elven
- Sylvan
- speak with plants
special_qualities:
- enlarge (7/day)
- nature bond (Plant domain [Growth subdomain])
- nature sense
- trackless step
- tree meld
- wild empathy +14
- woodcraft
- woodland stride
gear:
  combat:
  - potions of cure moderate wounds (2)
  - potion of remove curse
  - scrolls of resist energy (2)
  - wand of calm animals (24 charges)
  other:
  - club
  - dagger
  - mwk longbow with 20 arrows
  - ring of protection +1
  - pinecone amulet (divine focus)
  - wooden art objects worth 600 gp
  - 35 gp
desc_long: A still untainted fey in the northern stretch of the Shudderwood, Amalya
  is a bastion of nature among a perverse land, where denizens are beginning to succumb
  to the Worldwound's demonic hordes. To survive, she has formed a particularly close
  bond with her natural surroundings. She's studied the earth's struggle to survive
  against the Worldwound's onslaught; this scholarly curiosity has granted her powerful
  spells that she uses to protect herself, her tree, and the forest's remaining natural
  creatures. Given the danger she faces daily, Amalya is better at hiding than most
  dryads-however, the prevalence of half-fiends and other unspeakably abhorrent creatures
  also makes her a pragmatist of the highest order. She allies with like-minded adventurers
  who can stave off these threats more readily than others do of her kind.

---

# Amalya
This lithe, otherworldly woman has with deep brown eyes and
dark green hair that cascades past her waist. She’s adorned in
trinkets made from a great white pine’s needles and cones.

**Source** Fey Revisited pg. 8
**XP** 2,400
_[[monsters/Dryad|Dryad]]_ _[[classes/Druid|druid]]_ 3 (Pathfinder RPG Bestiary 116)

CG Medium fey
**Init** +5; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +13

##### Defense

**AC** 19, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+1 _[[spells/Deflection|deflection]]_, +5 Dex, +3 natural)
**hp** 73 (9 HD; 6d6+3d8+39)
**Fort** +10, **Ref** +11, **Will** +12
**DR** 5/cold iron
**Weaknesses** tree dependent

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Club|club]]_ +5 (1d6), _[[items/Weapon/Dagger|dagger]]_ +10 (1d4)
**Ranged** mwk _[[items/Weapon/Longbow|longbow]]_ +11 (1d8/×3)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +11)
Constant—_[[spells/Speak with Plants|speak with plants]]_
At will—_[[spells/Entangle|entangle]]_ (DC 16), _[[spells/Tree Shape|tree shape]]_, _[[spells/Wood Shape|wood shape]]_ (1 lb. only)
3/day—_[[spells/Charm Person|charm person]]_ (DC 16), _[[spells/Deep Slumber|deep slumber]]_ (DC 18), _[[spells/Tree Stride|tree stride]]_
1/day—_[[spells/Suggestion|suggestion]]_ (DC 18)
**_Druid_ Spells Prepared **(CL 3rd; concentration +7)
2nd—_[[spells/Barkskin|barkskin]]_, lesser _[[spells/Restoration|restoration]]_, _[[spells/Summon Swarm|summon swarm]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Enlarge Person|enlarge person]]_, _[[spells/Obscuring Mist|obscuring mist]]_,
_[[spells/Shillelagh|shillelagh]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Guidance|guidance]]_, _[[spells/Mending|mending]]_, stabilize

##### Statistics
**Str** 10, **Dex** 21, **Con** 17, **Int** 12, **Wis** 19, **Cha** 20
**Base Atk** +5; **CMB** +5; **CMD** 21
**Feats** _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Self-Sufficient|Self-Sufficient]]_, _[[feats/Stealthy|Stealthy]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +9, Craft (wood) +19, Escape Artist +19, Handle
Animal +14, _[[spells/Heal|Heal]]_ +6, Knowledge (nature) +12, Perception +13,
Stealth +19, Survival +17; **Racial Modifiers** +6 Craft (wood)
**Languages** Abyssal, Common, Druidic, Elven, Sylvan; speak
with plants
**SQ** enlarge (7/day), nature bond (Plant domain [Growth
subdomain]), nature sense, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, tree meld, wild
_[[feats/Empathy|empathy]]_ +14, woodcraft, woodland stride
**Combat Gear** potions of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (2), potion
of _[[spells/Remove Curse|remove curse]]_, scrolls of _[[spells/Resist Energy|resist energy]]_ (2), wand of calm
animals (24 charges); **Other Gear** _club_, _dagger_, mwk
_longbow_ with 20 arrows, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, pinecone
amulet (divine focus), wooden art objects worth 600 gp,
 35 gp

##### Description

A still untainted fey in the northern stretch of the
Shudderwood, _[[monsters/Amalya|Amalya]]_ is a _[[items/Armor Magic Abilities/Bastion|bastion]]_ of nature among a
perverse land, where denizens are beginning to succumb
to the Worldwound’s demonic hordes. To survive, she
has formed a particularly close bond with her natural
surroundings. She’s studied the earth’s struggle to survive
against the Worldwound’s _[[feats/Onslaught|onslaught]]_; this scholarly
curiosity has granted her powerful spells that she uses
to protect herself, her tree, and the forest’s remaining
natural creatures. Given the danger she faces daily, _Amalya_
is better at hiding than most dryads—however, the
prevalence of half-fiends and other unspeakably abhorrent
creatures also makes her a pragmatist of the highest order.
She allies with like-minded adventurers who can stave off
these threats more readily than others do of her kind.
---
cssclass: [monsters]
title1: Leshy, Leaf Leshy
desc_short: This little plant person is clad in a winglike leaf cloak and pinecone
  armor, wielding a twig as a makeshift spear.
title2: Leaf Leshy
CR: 1/2
sources:
- name: Bestiary 3
  page: 179
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 200
alignment: N
size: Small
type: plant
subtypes:
- leshy
- shapechanger
initiative:
  bonus: 1
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 13
  touch: 12
  flat_footed: 12
  components:
    armor: 1
    dex: 1
    size: 1
HP:
  HP: 5
  long: 1d8+1
saves:
  fort: 3
  ref: 1
  will: 1
immunities:
- electricity
- sonic
- plant traits
speeds:
  base: 20
  other_semicolon: glide
  climb: 10
  fly: 10
  fly_maneuverability: clumsy
attacks:
  melee:
  - - text: shortspear +2 (1d4-2/19-20)
      entries:
      - - damage: 1d4-2
          crit_range: 19-20
      attack: shortspear
      bonus:
      - 2
  ranged:
  - - text: seedpods +2 touch (1 plus deafen)
      entries:
      - - damage: '1'
        - effect: deafen
      attack: seedpods
      bonus:
      - 2
      touch: true
spell_like_abilities:
  entries:
  - name: pass without trace
    source: default
    freq: Constant
  sources:
  - name: default
    CL: 2
    concentration: 3
ability_scores:
  STR: 6
  DEX: 13
  CON: 12
  INT: 5
  WIS: 12
  CHA: 13
BAB: 0
CMB: -3
CMD: 8
feats:
- name: Weapon Finesse
skills:
  Fly: -1
  Stealth: 5
    in forests and jungles: 9
  Survival: 1
    in forests and jungles: 5
  Perception: 1
  _racial_mods:
    Stealth:
      in forests and jungles: 4
    Survival:
      in forests and jungles: 4
languages:
- Druidic
- Sylvan
- plantspeech (trees)
special_qualities:
- change shape (Small tree; tree shape)
- verdant burst
ecology:
  environment: any forest or hill
  organization: solitary or grove (2-16)
  treasure_type: standard
special_abilities:
  Glide (Ex): A leaf leshy cannot use its fly speed to hover. When flying, a leaf
    leshy must end its movement at least 5 feet lower in elevation than it started.
  Seedpods (Ex): Leaf leshys sprout explosive acorns, pine cones, or other seedpods,
    and can hurl these as ranged attacks. A seedpod has a range increment of 10 feet
    and detonates on contact to deal 1 point of bludgeoning damage (this damage is
    not modified by Strength). Anyone struck by a seedpod must succeed at a DC 11
    Fortitude save or be deafened for 1 round. The save DC is Constitution-based.
desc_long: |-
  Leaf leshys tend to the well-being of trees, whether natural stands or cultivated orchards. In appearance, they have soft, pulpy-looking bodies and wear clothing made of dozens of leaves. Larger leaves cover their shoulders, often giving them the appearance of wearing cloaks, and most adorn their relatively featureless heads with helmets made from pine cones, nuts, or fruit rinds. This leafy layer of clothing functions as masterwork padded armor for a leaf leshy, but not for any other creature.

  Leaf leshys love to play at war. When not laboring on their trees, they wheedle any companions to engage in mock duels with their twig spears, resorting to private weapon drills when they must. In actual battle, they are much more cautious, sticking to cover and harrying their foes with hit-and-run tactics, as they have a strongly developed sense of self-preservation.

---

# Leshy, Leaf Leshy
This little plant person is clad in a winglike leaf cloak and pinecone armor, wielding a twig as a makeshift _[[items/Weapon/Spear|spear]]_.
**Source** Bestiary 3 pg. 179
**XP** 200

N Small plant (leshy, shapechanger)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +1

##### Defense

**AC** 13, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+1 armor, +1 Dex, +1 size)
**hp** 5 (1d8+1)
**Fort** +3, **Ref** +1, **Will** +1
**Immune** electricity, sonic, _[[universal monster rules/Plant Traits|plant traits]]_

##### Offense
**Speed** 20 ft., _[[universal monster rules/Climb|climb]]_ 10 ft., fly 10 ft. (clumsy); _[[spells/Glide|glide]]_
**Melee** _[[items/Weapon/Shortspear|shortspear]]_ +2 (1d4–2/19–20)
**Ranged** seedpods +2 touch (1 plus deafen)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 2nd; concentration +3)
Constant—_[[spells/Pass without Trace|pass without trace]]_

##### Statistics
**Str** 6, **Dex** 13, **Con** 12, **Int** 5, **Wis** 12, **Cha** 13
**Base Atk** +0; **CMB** –3; **CMD** 8
**Feats** _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Fly –1, Stealth +5 (+9 in forests and jungles), Survival +1 (+5 in forests and jungles); **Racial Modifiers** +4 Stealth and Survival in forests and jungles
**Languages** Druidic, Sylvan; plantspeech (trees)
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (Small tree; _[[spells/Tree Shape|tree shape]]_), verdant burst

##### Ecology

**Environment** any forest or hill
**Organization** solitary or grove (2–16)
**Treasure** standard

### Special Abilities

**_Glide_ (Ex)** A leaf leshy cannot use its fly speed to _[[feats/Hover|hover]]_. When flying, a leaf leshy must end its movement at least 5 feet lower in elevation than it started.
**Seedpods (Ex)** Leaf leshys sprout explosive acorns, pine cones, or other seedpods, and can hurl these as ranged attacks. A seedpod has a range increment of 10 feet and detonates on contact to deal 1 point of bludgeoning damage (this damage is not modified by Strength). Anyone struck by a seedpod must succeed at a DC 11 Fortitude save or be _[[conditions/Deafened|deafened]]_ for 1 round. The save DC is Constitution-based.

##### Description

Leaf leshys tend to the well-being of trees, whether natural stands or cultivated orchards. In appearance, they have soft, pulpy-looking bodies and wear clothing made of dozens of leaves. Larger leaves cover their shoulders, often giving them the appearance of wearing cloaks, and most adorn their relatively featureless heads with helmets made from pine cones, nuts, or fruit rinds. This leafy layer of clothing functions as masterwork _[[items/Armor/Padded armor|padded armor]]_ for a leaf leshy, but not for any other creature.

Leaf leshys love to play at war. When not laboring on their trees, they wheedle any companions to engage in mock duels with their twig spears, resorting to private weapon drills when they must. In actual battle, they are much more cautious, sticking to cover and harrying their foes with hit-and-run tactics, as they have a strongly developed sense of self-preservation.
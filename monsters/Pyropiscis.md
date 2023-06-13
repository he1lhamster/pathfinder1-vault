---
cssclass: [monsters]
title1: Pyropiscis
desc_short: Glowing-hot plates of iron cover the head of this immense, primordial
  lungfish, and lava spills from between its jagged teeth.
title2: Pyropiscis
CR: 8
sources:
- name: 'Pathfinder #95: Anvil of Fire'
  page: 90
  link: http://paizo.com/products/btpy9et7?Pathfinder-Adventure-Path-95-Anvil-of-Fire
XP: 4800
alignment: N
size: Large
type: magical beast
subtypes:
- fire
initiative:
  bonus: 6
senses:
  darkvision: 60
  low-light vision: true
  tremorsense: 60
AC:
  AC: 22
  touch: 11
  flat_footed: 20
  components:
    armor: 11
    dex: 2
    size: -1
HP:
  HP: 105
  long: 10d10+50
saves:
  fort: 11
  ref: 9
  will: 5
DR:
- amount: 5
  weakness: adamantine
immunities:
- fire
weaknesses:
- lava dependency
- vulnerable to cold
speeds:
  base: 10
  other_semicolon: sprint
  burrow: 60
  burrow_other: through lava or magma only
attacks:
  melee:
  - - text: bite +17 (2d8+10/19-20 plus burn and grab)
      entries:
      - - damage: 2d8+10
          crit_range: 19-20
        - effect: burn
        - effect: grab
      attack: bite
      bonus:
      - 17
  ranged:
  - - text: lava bomb +11 (3d6 plus 2d6 fire)
      entries:
      - - damage: 3d6
        - damage: 2d6
          type: fire
      attack: lava bomb
      bonus:
      - 11
  special:
  - burn (1d6, DC 19)
  - searing bite
space: 10
reach: 10
ability_scores:
  STR: 24
  DEX: 14
  CON: 18
  INT: 2
  WIS: 15
  CHA: 6
BAB: 10
CMB: 18
CMB_other: +22 grapple
CMD: 30
feats:
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Lunge
- name: Toughness
- name: Weapon Focus (bite)
skills:
  Perception: 10
  Stealth: 6
    in lava: 14
  _racial_mods:
    Stealth:
      in lava: 8
special_qualities:
- hibernation
ecology:
  environment: warm mountains or underground
  organization: solitary, pack (3-6), or school (12-20)
  treasure_type: none
special_abilities:
  Hibernation (Ex): A pyropiscis can enter a state of hibernation for an indefinite
    period of time in order to survive longer periods away from a source of lava.
    Entering a state of hibernation takes 1 hour, during which the pyropiscis encases
    itself in a thick layer of igneous stone. While hibernating, a pyropiscis doesn't
    need to breathe, drink, or eat. The stone casing has hardness 8 and 90 hit points.
    As long as the casing remains intact, the pyropiscis within remains unharmed.
    The pyropiscis remains in a state of hibernation until it senses lava (or another
    source of extreme heat) nearby, at which point it breaks out of its case over
    the course of 1d4 minutes.
  Lava Bomb (Ex): Like an active volcano, a pyropiscis can spit a lava bomb-a blob
    of molten rock-as a ranged attack (range increment 30 feet). If a lava bomb hits,
    it deals 3d6 points of bludgeoning damage and 2d6 points of fire damage to its
    target.
  Lava Dependency (Ex): A pyropiscis can breathe indefinitely while submerged in lava.
    It can survive out of lava for 1 hour per point of Constitution. Beyond this limit,
    the pyropiscis runs the risk of suffocation, as if it were drowning.
  Searing Bite (Ex): A pyropiscis's searinghot jaws are designed to bind readily to
    flesh, giving it a firm grasp on its prey. This functions as the constrict ability,
    except that a pyropiscis deals 2d6 points of fire damage when it makes a successful
    grapple check, rather than dealing bludgeoning damage.
  Sprint (Ex): Once per minute, a pyropiscis may sprint, increasing its land speed
    to 40 feet for 1 round.
desc_long: |-
  Few environments are more inhospitable to life than the depths of a volcano, where magma surges through the rock like blood through veins. Of the creatures that do live in this hellish landscape, few are better adapted than the pyropiscis. Pyropiscises depend on this deadly environment of extreme temperatures and choking gases for their very lives. While they have a fishlike appearance, pyropiscises do not swim-their bodies are far too dense to float in water or similar liquids. Instead, pyropiscises rely on their powerful muscles and sharp scales to burrow through molten rock.

  A typical pyropiscis measures over 12 feet long, and weighs almost 4,000 pounds. Brilliant red scales glow and pulse with terrible heat, protecting those portions of their bodies not covered in blackened iron plates.

---

# Pyropiscis
Glowing-hot plates of iron cover the head of this immense, primordial lungfish, and lava spills from between its jagged teeth.
**Source** Pathfinder #95: _[[items/Mundane/Anvil|Anvil]]_ of Fire pg. 90
**XP** 4,800

N Large magical beast (fire)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 60 ft.; Perception +10

##### Defense

**AC** 22, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+11 armor, +2 Dex, –1 size)
**hp** 105 (10d10+50)
**Fort** +11, **Ref** +9, **Will** +5
**DR** 5/adamantine; **Immune** fire
**Weaknesses** lava dependency, vulnerable to cold

##### Offense
**Speed** 10 ft., _[[universal monster rules/Burrow|burrow]]_ 60 ft. (through lava or magma only); sprint
**Melee** bite +17 (2d8+10/19–20 plus _[[universal monster rules/Burn|burn]]_ and _[[universal monster rules/Grab|grab]]_)
**Ranged** lava bomb +11 (3d6 plus 2d6 fire)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _burn_ (1d6, DC 19), searing bite

##### Statistics
**Str** 24, **Dex** 14, **Con** 18, **Int** 2, **Wis** 15, **Cha** 6
**Base Atk** +10; **CMB** +18 (+22 grapple); **CMD** 30
**Feats** _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Perception +10, Stealth +6 (+14 in lava); **Racial Modifiers** +8 Stealth in lava
**SQ** hibernation

##### Ecology

**Environment** warm mountains or underground
**Organization** solitary, pack (3–6), or school (12–20)
**Treasure** none

### Special Abilities

**Hibernation (Ex)** A _[[monsters/Pyropiscis|pyropiscis]]_ can enter a state of hibernation for an indefinite period of time in order to survive longer periods away from a source of lava. Entering a state of hibernation takes 1 hour, during which the _pyropiscis_ encases itself in a thick layer of igneous stone. While hibernating, a _pyropiscis_ doesn’t need to breathe, drink, or eat. The stone casing has hardness 8 and 90 hit points. As long as the casing remains intact, the _pyropiscis_ within remains unharmed. The _pyropiscis_ remains in a state of hibernation until it senses lava (or another source of extreme _[[universal monster rules/Heat|heat]]_) nearby, at which point it breaks out of its case over the course of 1d4 minutes.

**Lava Bomb (Ex)** Like an active volcano, a _pyropiscis_ can spit a lava bomb—a blob of molten rock—as a ranged attack (range increment 30 feet). If a lava bomb hits, it deals 3d6 points of bludgeoning damage and 2d6 points of fire damage to its target.

**Lava Dependency (Ex)** A _pyropiscis_ can breathe indefinitely while submerged in lava. It can survive out of lava for 1 hour per point of Constitution. Beyond this limit, the _pyropiscis_ runs the risk of _[[spells/Suffocation|suffocation]]_, as if it were drowning.
**Searing Bite (Ex)** A _pyropiscis_’s searinghot jaws are designed to bind readily to flesh, giving it a firm _[[spells/Grasp|grasp]]_ on its prey. This functions as the _[[universal monster rules/Constrict|constrict]]_ ability, except that a _pyropiscis_ deals 2d6 points of fire damage when it makes a successful grapple check, rather than dealing bludgeoning damage.
**Sprint (Ex)** Once per minute, a _pyropiscis_ may sprint, increasing its land speed to 40 feet for 1 round.

##### Description

Few environments are more inhospitable to life than the depths of a volcano, where magma surges through the rock like blood through veins. Of the creatures that do live in this hellish landscape, few are better adapted than the _pyropiscis_. Pyropiscises depend on this _[[items/Weapon Magic Abilities/Deadly|deadly]]_ environment of extreme temperatures and choking gases for their very lives. While they have a fishlike appearance, pyropiscises do not swim—their bodies are far too dense to float in water or similar liquids. Instead, pyropiscises rely on their powerful muscles and sharp scales to _burrow_ through molten rock.

A typical _pyropiscis_ measures over 12 feet long, and weighs almost 4,000 pounds. Brilliant red scales glow and pulse with terrible _heat_, protecting those portions of their bodies not covered in blackened iron plates.
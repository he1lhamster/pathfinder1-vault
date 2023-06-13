---
cssclass: [monsters]
title1: Giant, Moon Giant
desc_short: This giant's gray skin sparkles as if with reflected light and is pocked
  with what look like impact craters on its rocklike surface.
title2: Moon Giant
CR: 15
sources:
- name: Bestiary 5
  page: 122
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 51200
alignment: LN
size: Huge
type: humanoid
subtypes:
- giant
initiative:
  bonus: 8
senses:
  low-light vision: true
  true seeing: true
auras:
- name: lunar
  radius: 60
  DC: 23
AC:
  AC: 32
  touch: 12
  flat_footed: 28
  components:
    dex: 4
    natural: 20
    size: -2
HP:
  HP: 220
  long: 21d8+126
saves:
  fort: 15
  ref: 13
  will: 18
defensive_abilities:
- improved rock catching
resistances:
  cold: 30
  fire: 30
speeds:
  base: 50
attacks:
  melee:
  - - text: 2 slams +29 (3d6+16)
      entries:
      - - damage: 3d6+16
      count: 2
      attack: slams
      bonus:
      - 29
  ranged:
  - - text: rock +19/+14/+9 (2d6+24 plus impact crater)
      entries:
      - - damage: 2d6+24
        - effect: impact crater
      attack: rock
      bonus:
      - 19
      - 14
      - 9
  special:
  - impact crater
  - rock throwing (180 ft.)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: dancing lights
    source: default
    freq: At will
  - name: detect magic
    source: default
    freq: At will
  - name: message
    source: default
    freq: At will
  - name: clairaudience/clairvoyance
    source: default
    freq: 3/day
  - name: control water
    source: default
    freq: 3/day
  - name: divination
    source: default
    freq: 3/day
  - name: commune
    source: default
    freq: 1/day
  - name: dream
    source: default
    freq: 1/day
  - name: scrying
    source: default
    freq: 1/day
    DC: 18
  sources:
  - name: default
    CL: 20
    concentration: 23
ability_scores:
  STR: 42
  DEX: 19
  CON: 22
  INT: 16
  WIS: 19
  CHA: 17
BAB: 15
CMB: 33
CMD: 47
feats:
- name: Combat Reflexes
- name: Far Shot
- name: Great Fortitude
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Point-Blank Shot
- name: Power Attack
- name: Precise Shot
- name: Quick Draw
- name: Weapon Focus (rock)
skills:
  Knowledge (arcana): 24
  Knowledge (nature): 24
  Perception: 28
  Sense Motive: 25
  Stealth: 17
    in rocky terrain: 25
  _racial_mods:
    Stealth:
      in rocky terrain: 8
languages:
- Common
- Giant
- Terran
ecology:
  environment: warm hills or mountains
  organization: solitary, pair, or cult (2-5 plus 35% noncombatants and one oracle
    of 4th-7th level)
  treasure_type: standard
special_abilities:
  Lunar Aura (Su): |-
    Creatures within 60 feet of a moon giant are affected by its lunar aura as long as they remain with range (Will DC 23 negates). The giant can choose one of the following effects.

     Waning: Affected creatures are calmed as per calm emotions. Aggressive action against a calmed creature breaks the effect for that creature only. A lycanthrope that fails its save is also affected by the true form spell.

     Waxing: Affected creatures are enraged as per rage. A lycanthrope that fails its save is also affected by the true form spell, except it is forced to revert to its hybrid form instead of its human form.

     A creature that succeeds at its save against the aura is immune to that particular moon giant's lunar aura for 24 hours. A moon giant can activate, suppress, or change the effect of the aura as a free action, and the giant can choose whether to include itself as part of the same free action. The save DC is Charisma-based.
  Impact Crater (Ex): When a moon giant throws a rock, it creates an area of difficult
    terrain in a 10-foot radius around the spot where the rock landed. If the rock
    was thrown at a creature, the giant can choose the point of origin for this radius
    anywhere within the target's space. If the moon giant misses with a rock attack,
    roll to determine where the rock lands as if it were a splash weapon.
  Improved Rock Catching (Ex): A moon giant gains rock catching, and it additionally
    receives a +4 racial bonus on its Reflex save when attempting to catch a thrown
    rock.
desc_long: |-
  Moon giants dwell in rocky badlands and other scarred, deserted places. They revere the moon, stars, and comets and seek wisdom in these celestial bodies' movements. Though they are normally placid scholars, more likely to enter a lively philosophical debate with other creatures than a brawl, moon giants can become violent when disturbed or when under the influence of a bad moon.

   Most moon giants stand about 24 feet tall and weigh almost 18,000 pounds.

---

# Giant, Moon Giant
This giant’s _[[monsters/Gray|gray]]_ skin sparkles as if with reflected light and is pocked with what look like _[[items/Weapon Magic Abilities/Impact|impact]]_ craters on its rocklike surface.
**Source** Bestiary 5 pg. 122
**XP** 51,200

LN Huge humanoid (giant)
**Init** +8; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/True Seeing|true seeing]]_; Perception +28
**Aura** lunar (60 ft., DC 23)

##### Defense

**AC** 32, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+4 Dex, +20 natural, –2 size)
**hp** 220 (21d8+126)
**Fort** +15, **Ref** +13, **Will** +18
**Defensive Abilities** improved _[[universal monster rules/Rock Catching|rock catching]]_; **Resist** cold 30, fire 30

##### Offense
**Speed** 50 ft.
**Melee** 2 slams +29 (3d6+16)
**Ranged** rock +19/+14/+9 (2d6+24 plus _impact_ crater)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _impact_ crater, _[[universal monster rules/Rock Throwing|rock throwing]]_ (180 ft.)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +23)
Constant—_true seeing_
At will—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Message|message]]_
3/day—clairaudience/clairvoyance, _[[spells/Control Water|control water]]_, _[[spells/Divination|divination]]_
1/day—_[[spells/Commune|commune]]_, _[[spells/Dream|dream]]_, _[[spells/Scrying|scrying]]_ (DC 18)

##### Statistics
**Str** 42, **Dex** 19, **Con** 22, **Int** 16, **Wis** 19, **Cha** 17
**Base Atk** +15; **CMB** +33; **CMD** 47
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Far Shot|Far Shot]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Quick Draw|Quick Draw]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (rock)
**Skills** Knowledge (arcana, nature) +24, Perception +28, Sense Motive +25, Stealth +17 (+25 in rocky terrain); **Racial Modifiers** +8 Stealth in rocky terrain
**Languages** Common, Giant, Terran

##### Ecology

**Environment** warm hills or mountains
**Organization** solitary, pair, or cult (2–5 plus 35% noncombatants and one _[[classes/Oracle|oracle]]_ of 4th–7th level)
**Treasure** standard

### Special Abilities

**Lunar Aura (Su)** Creatures within 60 feet of a moon giant are affected by its lunar aura as long as they remain with range (Will DC 23 negates). The giant can choose one of the following effects.

Waning: Affected creatures are calmed as per _[[spells/Calm Emotions|calm emotions]]_. Aggressive action against a calmed creature breaks the effect for that creature only. A lycanthrope that fails its save is also affected by the _[[spells/True Form|true form]]_ spell.

Waxing: Affected creatures are enraged as per _[[spells/Rage|rage]]_. A lycanthrope that fails its save is also affected by the _true form_ spell, except it is forced to revert to its hybrid form instead of its human form.

A creature that succeeds at its save against the aura is immune to that particular moon giant’s lunar aura for 24 hours. A moon giant can activate, suppress, or change the effect of the aura as a free action, and the giant can choose whether to include itself as part of the same free action. The save DC is Charisma-based.

**_Impact_ Crater (Ex)** When a moon giant throws a rock, it creates an area of difficult terrain in a 10-foot radius around the spot where the rock landed. If the rock was thrown at a creature, the giant can choose the point of origin for this radius anywhere within the target’s space. If the moon giant misses with a rock attack, roll to determine where the rock lands as if it were a splash weapon.

**Improved _Rock Catching_ (Ex)** A moon giant gains _rock catching_, and it additionally receives a +4 racial bonus on its Reflex save when attempting to catch a thrown rock.

##### Description

Moon giants dwell in rocky badlands and other scarred, deserted places. They revere the moon, stars, and comets and seek wisdom in these celestial bodies’ movements. Though they are normally placid scholars, more likely to enter a lively philosophical debate with other creatures than a brawl, moon giants can become violent when disturbed or when under the influence of a bad moon.

Most moon giants stand about 24 feet tall and weigh almost 18,000 pounds.
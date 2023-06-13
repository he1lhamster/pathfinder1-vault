---
cssclass: [monsters]
title1: Ghoran
desc_short: The humanoid creature's taut green shell extends like a cowl from chin
  to brow, wreathing a face of brilliant flower petals.
title2: Ghoran
CR: 1
sources:
- name: Bestiary 5
  page: 119
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
- name: Inner Sea Bestiary
  page: 14
  link: http://paizo.com/products/btpy8v2x?Pathfinder-Campaign-Setting-Inner-Sea-Bestiary
XP: 400
race: Ghoran
classes:
- bard 1
alignment: N
size: Medium
type: plant
initiative:
  bonus: 1
senses:
  low-light vision: true
AC:
  AC: 13
  touch: 11
  flat_footed: 12
  components:
    dex: 1
    natural: 2
HP:
  HP: 12
  long: 1d8+4
saves:
  fort: 3
  ref: 3
  will: 3
immunities:
- plant traits
weaknesses:
- delicious
- light dependent
speeds:
  base: 30
attacks:
  melee:
  - - text: rapier +1 (1d6-1/18-20)
      entries:
      - - damage: 1d6-1
          crit_range: 18-20
      attack: rapier
      bonus:
      - 1
  special:
  - bardic performance 7 rounds/day (countersong, distraction, fascinate, inspire
    courage +1)
spell_like_abilities:
  entries:
  - name: detect poison
    source: default
    freq: 1/day
  - name: goodberry
    source: default
    freq: 1/day
  - name: purify food and drink
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 1
    concentration: 4
spells:
  entries:
  - name: charm person
    source: Bard
    level: 1
    DC: 14
  - name: sleep
    source: Bard
    level: 1
    DC: 14
  - name: daze
    source: Bard
    level: 0
    DC: 13
  - name: light
    source: Bard
    level: 0
  - name: mending
    source: Bard
    level: 0
  - name: message
    source: Bard
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 1
    concentration: 4
    slots:
      1: 2
      0: at-will
ability_scores:
  STR: 8
  DEX: 13
  CON: 16
  INT: 8
  WIS: 12
  CHA: 17
BAB: 0
CMB: -1
CMD: 10
feats:
- name: Weapon Finesse
skills:
  Bluff: 7
  Knowledge (history): 4
  Knowledge (local): 4
  Perception: 5
  Perform (sing): 7
languages:
- Common
- Sylvan
special_qualities:
- bardic knowledge +1
- ghorus seed
- past-life knowledge
ecology:
  environment: any
  organization: solitary, pair, or plot (3-12)
  treasure_type: NPC Gear
  treasure:
  - rapier
  - other treasure
special_abilities:
  Delicious (Ex): Ghorans take a -2 penalty on Escape Artist and combat maneuver checks
    to escape a grapple against any creature that has a bite attack with the grab
    ability.
  Ghorus Seed (Ex): As a full-round action, a ghoran can expel its ghorus seed from
    an orifice in its abdomen. If planted in fertile ground and left undisturbed for
    2d6 days, the seed grows into a healthy duplicate of the original ghoran, save
    that the duplicate can reallocate all of its skill ranks upon sprouting. Once
    a ghoran expels its seed, it gains 1 negative level, and it dies as soon as its
    duplicate sprouts. This duplicate replaces the previous ghoran character.
  Light Dependent: Ghorans take 1d4 points of Constitution damage each day they go
    without exposure to sunlight.
  Past-Life Knowledge (Ex): Ghorans remember memories encoded in their ghorus seed.
    They treat all Knowledge skills as class skills.
desc_long: Ghorans arose from plant life created by advanced druidic magic to be an
  especially hardy and adaptive food source for humans. Over the centuries, the plants
  evolved sentience and ambulatory bodies that mimicked the appearance of humanoids
  as a method to discourage their enemies from hunting them and improve their chances
  of survival. Their creators did not imbue them with the ability to create more of
  the ghorus seeds that give them life, so ghorans are fanatically protective of these
  seeds and consider destroying them the worst of crimes.

---

# Ghoran
The humanoid creature’s taut green shell extends like a cowl from chin to brow, wreathing a face of brilliant flower petals.
**Source** Bestiary 5 pg. 119, Inner Sea Bestiary pg. 14
**XP** 400
_[[monsters/Ghoran|Ghoran]]_ _[[classes/Bard|bard]]_ 1

N Medium plant
**Init** +1; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +5

##### Defense

**AC** 13, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+1 Dex, +2 natural)
**hp** 12 (1d8+4)
**Fort** +3, **Ref** +3, **Will** +3
**Immune** _[[universal monster rules/Plant Traits|plant traits]]_
**Weaknesses** delicious, light dependent

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Rapier|rapier]]_ +1 (1d6–1/18–20)
**Special Attacks** bardic performance 7 rounds/day (countersong, _[[universal monster rules/Distraction|distraction]]_, fascinate, inspire courage +1)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 1st; concentration +4)
1/day—_[[spells/Detect Poison|detect poison]]_, _[[spells/Goodberry|goodberry]]_, _[[spells/Purify Food and Drink|purify food and drink]]_
**Spells Known **(CL 1st; concentration +4)
1st (2/day)—_[[spells/Charm Person|charm person]]_ (DC 14), sleep (DC 14)
0 (at will)—_[[spells/Daze|daze]]_ (DC 13), light, _[[spells/Mending|mending]]_, _[[spells/Message|message]]_

##### Statistics
**Str** 8, **Dex** 13, **Con** 16, **Int** 8, **Wis** 12, **Cha** 17
**Base Atk** +0; **CMB** –1; **CMD** 10
**Feats** _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +7, Knowledge (history) +4, Knowledge (local) +4, Perception +5, Perform (sing) +7
**Languages** Common, Sylvan
**SQ** bardic knowledge +1, ghorus seed, past-life knowledge

##### Ecology

**Environment** any
**Organization** solitary, pair, or plot (3–12)
**Treasure** NPC gear (_rapier_, other treasure)

### Special Abilities

**Delicious (Ex)** Ghorans take a –2 penalty on Escape Artist and combat maneuver checks to escape a grapple against any creature that has a bite attack with the _[[universal monster rules/Grab|grab]]_ ability.

**Ghorus Seed (Ex)** As a full-round action, a _ghoran_ can expel its ghorus seed from an orifice in its abdomen. If planted in fertile ground and left undisturbed for 2d6 days, the seed grows into a healthy duplicate of the original _ghoran_, save that the duplicate can reallocate all of its skill ranks upon sprouting. Once a _ghoran_ expels its seed, it gains 1 negative level, and it dies as soon as its duplicate sprouts. This duplicate replaces the previous _ghoran_ character.

**Light Dependent** Ghorans take 1d4 points of Constitution damage each day they go without exposure to sunlight.

**Past-Life Knowledge (Ex)** Ghorans remember memories encoded in their ghorus seed. They treat all Knowledge skills as class skills.

##### Description

Ghorans arose from plant life created by advanced druidic magic to be an especially hardy and adaptive food source for humans. Over the centuries, the plants evolved sentience and ambulatory bodies that mimicked the appearance of humanoids as a method to discourage their enemies from hunting them and improve their chances of survival. Their creators did not imbue them with the ability to create more of the ghorus seeds that give them life, so ghorans are fanatically protective of these seeds and consider destroying them the worst of crimes.
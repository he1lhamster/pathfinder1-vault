---
cssclass: [monsters]
title1: Lion
desc_short: This great cat's muscles flex visibly under its skin as it bares its fangs
  and shakes its thick mane of hair.
title2: Lion
CR: 3
sources:
- name: Pathfinder RPG Bestiary
  page: 193
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 800
alignment: N
size: Large
type: animal
initiative:
  bonus: 7
senses:
  low-light vision: true
  scent: true
AC:
  AC: 15
  touch: 12
  flat_footed: 12
  components:
    dex: 3
    natural: 3
    size: -1
HP:
  HP: 32
  long: 5d8+10
saves:
  fort: 6
  ref: 7
  will: 2
speeds:
  base: 40
attacks:
  melee:
  - - text: bite +7 (1d8+5 plus grab)
      entries:
      - - damage: 1d8+5
        - effect: grab
      attack: bite
      bonus:
      - 7
    - text: 2 claws +7 (1d4+5)
      entries:
      - - damage: 1d4+5
      count: 2
      attack: claws
      bonus:
      - 7
  special:
  - pounce
  - rake (2 claws +7, 1d4+5)
space: 10
reach: 5
ability_scores:
  STR: 21
  DEX: 17
  CON: 15
  INT: 2
  WIS: 12
  CHA: 6
BAB: 3
CMB: 9
CMB_other: +13 grapple
CMD: 22
CMD_other: 26 vs. trip
feats:
- name: Improved Initiative
- name: Run
- name: Skill Focus (Perception)
skills:
  Acrobatics: 11
  Perception: 9
  Stealth: 8
    in undergrowth: 12
  _racial_mods:
    Acrobatics:
      _: 4
    Stealth:
      _: 4
      in undergrowth: 8
ecology:
  environment: warm plains
  organization: solitary, pair, or pride (3-10)
  treasure_type: none
desc_long: |-
  Male lions are 5 to 8 feet long and weigh 330 to 550 pounds. Females are slightly smaller but use the same statistics.

  Lions are usually the top animal predators in their territories, though they resort to scavenging if convenient or necessary. They may kill other predators (such as leopards and hyenas) that encroach upon their haunts, but rarely eat these kills unless game is scarce. Most lions do not selectively hunt humanoids, but occasionally one learns what easy kills they are and becomes a man-eater.

  Lions prefer plains but can adapt to living in shallow caves as long as there's a large and stable supply of prey to keep them fed.

---

# Lion
This great cat’s muscles flex visibly under its skin as it bares its fangs and _[[diseases/Shakes|shakes]]_ its thick mane of hair.
**Source** Pathfinder RPG Bestiary pg. 193
**XP** 800

N Large animal
**Init** +7; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +9

##### Defense

**AC** 15, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+3 Dex, +3 natural, –1 size)
**hp** 32 (5d8+10)
**Fort** +6, **Ref** +7, **Will** +2

##### Offense
**Speed** 40 ft.
**Melee** bite +7 (1d8+5 plus _[[universal monster rules/Grab|grab]]_), 2 claws +7 (1d4+5)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** _[[universal monster rules/Pounce|pounce]]_, _[[universal monster rules/Rake|rake]]_ (2 claws +7, 1d4+5)

##### Statistics
**Str** 21, **Dex** 17, **Con** 15, **Int** 2, **Wis** 12, **Cha** 6
**Base Atk** +3; **CMB** +9 (+13 grapple); **CMD** 22 (26 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, Run, _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** Acrobatics +11, Perception +9, Stealth +8 (+12 in undergrowth); **Racial Modifiers** +4 Acrobatics, +4 Stealth (+8 in undergrowth)

##### Ecology

**Environment** warm plains
**Organization** solitary, pair, or pride (3–10)
**Treasure** none

##### Description

Male lions are 5 to 8 feet long and weigh 330 to 550 pounds. Females are slightly smaller but use the same statistics.

Lions are usually the top animal predators in their territories, though they resort to scavenging if convenient or necessary. They may kill other predators (such as leopards and hyenas) that encroach upon their haunts, but rarely eat these kills unless game is scarce. Most lions do not selectively hunt humanoids, but occasionally one learns what easy kills they are and becomes a man-eater.

Lions prefer plains but can adapt to living in shallow caves as long as there’s a large and _[[conditions/Stable|stable]]_ supply of prey to keep them fed.
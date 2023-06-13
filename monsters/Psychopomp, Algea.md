---
cssclass: [monsters]
title1: Psychopomp, Algea
desc_short: This shrill swarm of whip-poor-wills flies in a spiral, theirairborne
  antics infused with streamers of pale blue mist.
title2: Algea
CR: 11
sources:
- name: Bestiary 6
  page: 217
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 12800
alignment: N
size: Diminutive
type: outsider
subtypes:
- extraplanar
- psychopomp
- swarm
initiative:
  bonus: 14
senses:
  darkvision: 60
  greater arcane sight: true
  low-lightvision: true
  spiritsense: true
auras:
- name: grief
  radius: 30
  DC: 24
AC:
  AC: 24
  touch: 24
  flat_footed: 14
  components:
    dex: 10
    size: 4
HP:
  HP: 149
  long: 13d10+78
saves:
  fort: 12
  ref: 20
  will: 16
defensive_abilities:
- swarm traits
immunities:
- death effects,disease
- poison
- weapon damage
resistances:
  acid: 10
  cold: 10
  electricity: 10
  fire: 10
  sonic: 10
SR: 22
speeds:
  base: 20
  fly: 80
  fly_maneuverability: good
attacks:
  melee:
  - - text: swarm (3d6 plus distraction)
      entries:
      - - damage: 3d6
        - effect: distraction
      attack: swarm
  special:
  - distraction (DC 22)
  - drain magic
  - soul cage
space: 10
reach: 0
spell_like_abilities:
  entries:
  - name: greater arcane sight
    source: default
    freq: Constant
  - name: mass invisibility
    source: default
    freq: At will
    other: self only
  - name: speak with dead
    source: default
    freq: At will
    DC: 21
  - name: call spirit
    source: default
    freq: 3/day
    DC: 23
  - name: confusion
    source: default
    freq: 3/day
    DC: 22
  - name: plane shift
    source: default
    freq: 1/day
    other: swarm counts as one creature
    DC: 27
  sources:
  - name: default
    CL: 11
    concentration: 19
ability_scores:
  STR: 8
  DEX: 30
  CON: 23
  INT: 15
  WIS: 23
  CHA: 26
BAB: 13
CMB:
CMD:
feats:
- name: Alertness
- name: Combat Casting
- name: Great Fortitude
- name: Improved GreatFortitude
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
skills:
  Acrobatics: 26
  Fly: 36
  Knowledge (planes): 18
  Knowledge (religion): 18
  Perception: 26
  Sense Motive: 26
  Spellcraft: 18
  Stealth: 38
languages:
- Abyssal
- Aklo
- Celestial
- Infernal
special_qualities:
- spirit touch
ecology:
  environment: any (Boneyard)
  organization: solitary or spiral (2-6 swarms)
  treasure_type: none
special_abilities:
  Aura of Grief (Su): Each creature within 30 feet of an algea must succeed at a DC
    24 Will save at the start of its turn or become stricken with intense grief for
    1 round. A creature so affected can take no actions, takes a -2 penalty to AC,
    and loses its Dexterity bonus (if any). Once a creature successfully saves against
    this effect, it is immune to all algeas' auras of grief for 24 hours. Although
    this is an emotion and mind-affecting effect, it can still affect undead, despite
    their usual immunities to such effects. The save DC is Charisma-based.
  Drain Magic (Su): Whenever the algea deals swarm damage to a creature, it also dispels
    an active spell on the creature or one of the creature's items as per a targeted
    dispel magic (CL 11th). The algea can choose which effect to dispel for each creature,
    targeting the most troublesome first.
  Soul Cage (Su): An algea's distraction ability works against creatures normally
    immune to nausea. An incorporeal creature that fails its save against an algea's
    distraction is trapped within the algea's space for 1 round, during which it can't
    move out of that space (even via teleportation effects and the like). If the algea
    uses plane shift on any trapped creatures, they take a -4 penalty to save against
    the effect.
desc_long: Algeas protect (and in some cases retrieve) souls that are at risk of being
  claimed by other entities, particularly spellcasters who dabbled with otherworldly
  forces but never officially pledged their souls. Algeas are particularly focused
  on intervening and “rescuing” souls in danger of being trapped within the Material
  Plane by powerful entities like the Great Old Ones or false prophets who have deluded
  minions into worshiping them as living gods.

---

# Psychopomp, Algea
This shrill swarm of whip-poor-wills flies in a spiral, their

airborne antics infused with streamers of pale blue mist.
**Source** Bestiary 6 pg. 217
**XP** 12,800

N Diminutive outsider (extraplanar, psychopomp, swarm)
**Init** +14; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., greater _[[spells/Arcane Sight|arcane sight]]_, low-light

_[[spells/Vision|vision]]_, spiritsense; Perception +26
**Aura** grief (30 ft., DC 24)

##### Defense

**AC** 24, touch 24, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+10 Dex, +4 size)
**hp** 149 (13d10+78)
**Fort** +12, **Ref** +20, **Will** +16
**Defensive Abilities** swarm traits; **Immune** death effects,

disease, poison, weapon damage; **Resist** acid 10, cold 10,

electricity 10, fire 10, sonic 10; **SR** 22

##### Offense
**Speed** 20 ft., fly 80 ft. (good)
**Melee** swarm (3d6 plus _[[universal monster rules/Distraction|distraction]]_)
**Space** 10 ft., **Reach** 0 ft.
**Special Attacks** _distraction_ (DC 22), drain magic, soul cage
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +19)
Constant—greater _arcane sight_ 
At will—mass _[[spells/Invisibility|invisibility]]_ (self only), _[[spells/Speak with Dead|speak with dead]]_ (DC 21) 
3/day—_[[spells/Call Spirit|call spirit]]_ (DC 23), _[[spells/Confusion|confusion]]_ (DC 22) 
1/day—_[[spells/Plane Shift|plane shift]]_ (swarm counts as one creature; DC 27)

##### Statistics
**Str** 8, **Dex** 30, **Con** 23, **Int** 15, **Wis** 23, **Cha** 26
**Base Atk** +13; **CMB** —; **CMD** —
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Great Fortitude|Great Fortitude]]_, Improved Great

Fortitude, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Acrobatics +26, Fly +36, Knowledge (planes, religion) +18,

Perception +26, Sense Motive +26, Spellcraft +18, Stealth +38
**Languages** Abyssal, Aklo, Celestial, Infernal
**SQ** spirit touch

##### Ecology

**Environment** any (Boneyard)
**Organization** solitary or spiral (2–6 swarms)
**Treasure** none

### Special Abilities

**Aura of Grief (Su)** Each creature within 30 feet of an algea must succeed at a DC 24 Will save at the start of its turn or become stricken with intense grief for 1 round. A creature so affected can take no actions, takes a –2 penalty to AC, and loses its Dexterity bonus (if any). Once a creature successfully saves against this effect, it is immune to all algeas’ auras of grief for 24 hours. Although this is an emotion and mind-affecting effect, it can still affect undead, despite their usual immunities to such effects. The save DC is Charisma-based.

**Drain Magic (Su)** Whenever the algea deals swarm damage to a creature, it also dispels an active spell on the creature or one of the creature’s items as per a targeted _[[spells/Dispel Magic|dispel magic]]_ (CL 11th). The algea can choose which effect to dispel for each creature, targeting the most troublesome first.
**Soul Cage (Su)** An algea’s _distraction_ ability works against creatures normally immune to nausea. An _[[universal monster rules/Incorporeal|incorporeal]]_ creature that fails its save against an algea’s _distraction_ is trapped within the algea’s space for 1 round, during which it can’t move out of that space (even via teleportation effects and the like). If the algea uses _plane shift_ on any trapped creatures, they take a –4 penalty to save against the effect.

##### Description

Algeas protect (and in some cases retrieve) souls that are at risk of being claimed by other entities, particularly spellcasters who dabbled with otherworldly forces but never officially pledged their souls. Algeas are particularly focused on intervening and “rescuing” souls in danger of being trapped within the Material Plane by powerful entities like the Great Old Ones or false prophets who have deluded minions into worshiping them as living gods.
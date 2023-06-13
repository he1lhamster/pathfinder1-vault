---
cssclass: [monsters]
title1: Bramble Throne
desc_short: The low branches of this stout tree form the shape of a throne. Gold-trimmed
  leaves and thick vines grow on the branches.
title2: Bramble Throne
CR: 16
sources:
- name: 'Pathfinder #132: The Six-Legend Soul'
  page: 82
  link: http://paizo.com/products/btpy9xdq?Pathfinder-Adventure-Path-The-SixLegend-Soul
XP: 76800
alignment: N
size: Huge
type: plant
initiative:
  bonus: 10
senses:
  low-light vision: true
  thoughtsense: true
  tremorsense: 120
auras:
- name: supplication
  radius: 30
  DC: 24
AC:
  AC: 30
  touch: 14
  flat_footed: 24
  components:
    dex: 6
    natural: 16
    size: -2
HP:
  HP: 230
  long: 20d8+140
saves:
  fort: 19
  ref: 12
  will: 12
immunities:
- plant traits
speeds:
  base: 10
attacks:
  melee:
  - - text: bite +25 (2d6+11 plus grab)
      entries:
      - - damage: 2d6+11
        - effect: grab
      attack: bite
      bonus:
      - 25
    - text: 4 vines +25 (1d8+11 plus bleed and grab)
      entries:
      - - damage: 1d8+11
        - effect: bleed
        - effect: grab
      count: 4
      attack: vines
      bonus:
      - 25
  special:
  - bleed (2d6)
  - blood drain (1d4 Constitution)
  - puppet ruler
space: 15
reach: 10
reach_other: 20 ft. with vines
spell_like_abilities:
  entries:
  - name: thoughtsense
    source: default
    freq: Constant
  sources:
  - name: default
    CL: 20
    concentration: 24
psychic_magic:
  entries:
  - name: dominate person
    PE: 5
    DC: 19
  - name: greater command
    PE: 5
    DC: 19
  - name: paranoia
    PE: 2
    DC: 16
  sources:
  - name: default
    CL: 16
    concentration: 20
  PE: 30
ability_scores:
  STR: 33
  DEX: 22
  CON: 25
  INT: 4
  WIS: 18
  CHA: 19
BAB: 15
CMB: 28
CMB_other: +30 bull rush
CMD: 44
CMD_other: 46 vs. bull rush, can't be tripped
feats:
- name: Awesome Blow
- name: Combat Reflexes
- name: Improved Bull Rush
- name: Improved Initiative
- name: Improved Vital Strike
- name: Iron Will
- name: Power Attack
- name: Vital Strike
- name: Weapon Focus (bite)
- name: Weapon Focus (vines)
skills:
  Perception: 17
  Stealth: 11
languages:
- Common
ecology:
  environment: temperate forests
  organization: solitary
  treasure_type: standard
special_abilities:
  Puppet Ruler (Su): As a full-round action, a bramble throne can thrust psychically
    empowered tendrils into any Small, Medium, or Large creature seated on its throne
    that has been dead for less than 1 minute. The corpse becomes a zombie-like creature,
    but it isn't treated as being undead and is immune to spells and effects that
    affect only undead (including damage from positive energy). The puppet ruler shares
    the bramble throne's space, moves with it, and can make attacks independently
    of the bramble throne. If the bramble throne removes its tendrils as a move action,
    or if the puppet ruler is removed from the throne, it reverts to an ordinary corpse.
    The puppet ruler has cover while on the throne, but attackers can otherwise attack
    either the bramble throne or the puppet ruler freely. Area-effect spells affect
    both the bramble throne and puppet ruler. Killing the bramble throne destroys
    the puppet ruler.
  Supplication Aura (Su): While the bramble throne is using its puppet ruler ability,
    any creature that begins its turn within 30 feet of the bramble throne must succeed
    at a DC 24 Will save or fall prone and become fascinated by the puppet on the
    throne for 1 round, viewing it as a ruler worthy of adoration. A creature affected
    by this ability does not view either the bramble throne or the puppet as a potential
    threat, but an attack by either the bramble throne or the puppet ends the fascination.
    This is a mindaffecting effect. The save DC is Charisma-based.
  Vines (Ex): A bramble throne's barbed vines are primary natural attacks that deal
    bludgeoning and piercing damage. A bramble throne doesn't gain the grappled condition
    when grappling enemies with its vines and can maintain grapples with any number
    of its vines with the same standard action.
desc_long: |-
  Bramble thrones grow where the blood of power-hungry rulers has been spilled, and particularly where the bodies of these grasping monarchs have been laid to rest. A ruler's obsession over the power of a throne can be so powerful that it leaches into the soil, infusing a growing tree with a psychic fixation on the trappings of rule and powers of domination. As the plant grows, its branches form into the shape of the ruler's throne and its leaves sprout in regal colors such as gold and violet.

   A bramble throne's wide trunk typically rises only 2 feet above ground before branching into a throne 8 feet wide and 10 feet high. Leaves surround the throne like an ornate canopy, and several thick, barbed vines wind around the entire tree. A bramble throne can slowly pull itself along the ground with these vines, although it more frequently uses them to lash out at creatures that stray within the range of its psychic senses. If it kills an intelligent creature, it seats the corpse upon the throne, using invasive tendrils to give the corpse the semblance of animation and regal authority. With a corpse seated upon it, a bramble throne can compel other creatures to make the obeisance it craves.

   Bramble thrones retain an echo of the ruler's imperious nature, allowing it to speak basic commands such as “approach,” “bow,” and “kneel” through a jagged, mouth-like slit in its trunk. Bramble thrones speak whatever languages the ruler knew in life.

   Bramble thrones grow up to 12 feet wide and 20 feet high and weigh about 4,000 pounds.

---

# Bramble Throne
The low branches of this stout tree form the shape of a throne. Gold-trimmed leaves and thick vines grow on the branches.
**Source** Pathfinder #132: The Six-Legend Soul pg. 82
**XP** 76,800

N Huge plant
**Init** +10; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Thoughtsense|thoughtsense]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 120 ft.; Perception +17
**Aura** supplication (30 ft., DC 24)

##### Defense

**AC** 30, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+6 Dex, +16 natural, –2 size)
**hp** 230 (20d8+140)
**Fort** +19, **Ref** +12, **Will** +12
**Immune** _[[universal monster rules/Plant Traits|plant traits]]_

##### Offense
**Speed** 10 ft.
**Melee** bite +25 (2d6+11 plus _[[universal monster rules/Grab|grab]]_), 4 vines +25 (1d8+11 plus _[[universal monster rules/Bleed|bleed]]_ and _grab_)
**Space** 15 ft., **Reach** 10 ft. (20 ft. with vines)
**Special Attacks** _bleed_ (2d6), _[[universal monster rules/Blood Drain|blood drain]]_ (1d4 Constitution), puppet ruler
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +24)
Constant—_thoughtsense_
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_** (CL 16th; concentration +20)
30 PE—_[[spells/Dominate Person|dominate person]]_ (5 PE, DC 19), greater _[[spells/Command|command]]_ (5 PE, DC 19), _[[spells/Paranoia|paranoia]]_ (2 PE, DC 16)

##### Statistics
**Str** 33, **Dex** 22, **Con** 25, **Int** 4, **Wis** 18, **Cha** 19
**Base Atk** +15; **CMB** +28 (+30 bull rush); **CMD** 44 (46 vs. bull rush, can’t be tripped)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite, vines)
**Skills** Perception +17, Stealth +11
**Languages** Common

##### Ecology

**Environment** temperate forests
**Organization** solitary
**Treasure** standard

### Special Abilities

**Puppet Ruler (Su)** As a full-round action, a _[[monsters/Bramble Throne|bramble throne]]_ can thrust psychically empowered tendrils into any Small, Medium, or Large creature seated on its throne that has been dead for less than 1 minute. The corpse becomes a zombie-like creature, but it isn’t treated as being undead and is immune to spells and effects that affect only undead (including damage from positive energy). The puppet ruler shares the _bramble throne_’s space, moves with it, and can make attacks independently of the _bramble throne_. If the _bramble throne_ removes its tendrils as a move action, or if the puppet ruler is removed from the throne, it reverts to an ordinary corpse. The puppet ruler has cover while on the throne, but attackers can otherwise attack either the _bramble throne_ or the puppet ruler freely. Area-effect spells affect both the _bramble throne_ and puppet ruler. Killing the _bramble throne_ destroys the puppet ruler.
**Supplication Aura (Su)** While the _bramble throne_ is using its puppet ruler ability, any creature that begins its turn within 30 feet of the _bramble throne_ must succeed at a DC 24 Will save or fall _[[conditions/Prone|prone]]_ and become _[[conditions/Fascinated|fascinated]]_ by the puppet on the throne for 1 round, viewing it as a ruler worthy of _[[spells/Adoration|adoration]]_. A creature affected by this ability does not view either the _bramble throne_ or the puppet as a potential threat, but an attack by either the _bramble throne_ or the puppet ends the fascination. This is a mindaffecting effect. The save DC is Charisma-based.

**Vines (Ex)** A _bramble throne_’s barbed vines are primary _[[universal monster rules/Natural Attacks|natural attacks]]_ that deal bludgeoning and piercing damage. A _bramble throne_ doesn’t gain the _[[conditions/Grappled|grappled]]_ condition when grappling enemies with its vines and can maintain grapples with any number of its vines with the same standard action.

##### Description

Bramble thrones grow where the blood of power-hungry rulers has been spilled, and particularly where the bodies of these grasping monarchs have been laid to rest. A ruler’s obsession over the power of a throne can be so powerful that it leaches into the soil, infusing a _[[items/Weapon Magic Abilities/Growing|growing]]_ tree with a _[[classes/Psychic|psychic]]_ fixation on the trappings of rule and powers of domination. As the plant grows, its branches form into the shape of the ruler’s throne and its leaves sprout in regal colors such as gold and violet.

A _bramble throne_’s wide trunk typically rises only 2 feet above ground before branching into a throne 8 feet wide and 10 feet high. Leaves surround the throne like an ornate canopy, and several thick, barbed vines wind around the entire tree. A _bramble throne_ can slowly _[[universal monster rules/Pull|pull]]_ itself along the ground with these vines, although it more frequently uses them to lash out at creatures that stray within the range of its _psychic_ senses. If it kills an intelligent creature, it seats the corpse upon the throne, using invasive tendrils to give the corpse the semblance of animation and regal authority. With a corpse seated upon it, a _bramble throne_ can compel other creatures to make the obeisance it craves.

Bramble thrones retain an _[[spells/Echo|echo]]_ of the ruler’s imperious nature, allowing it to speak basic commands such as “approach,” “bow,” and “kneel” through a jagged, mouth-like slit in its trunk. Bramble thrones speak whatever languages the ruler knew in life.

Bramble thrones grow up to 12 feet wide and 20 feet high and weigh about 4,000 pounds.
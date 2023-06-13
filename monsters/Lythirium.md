---
cssclass: [monsters]
title1: Lythirium
desc_short: This wolflike creature's body is composed of thick vines, fine vegetation
  that almost resembles fur, and enormous thorns. Its eyes shine with a green glow,
  and prickly vines cover the immense, antlerlike growths on its head.
title2: Lythirium
CR: 11
sources:
- name: 'Pathfinder #105: The Inferno Gate'
  page: 86
  link: http://paizo.com/products/btpy9jb9?Pathfinder-Adventure-Path-105-The-Inferno-Gate
XP: 12800
alignment: NG
size: Large
type: plant
initiative:
  bonus: 4
senses:
  darkvision: 60
  low-light vision: true
  scent: true
AC:
  AC: 26
  touch: 14
  flat_footed: 21
  components:
    dex: 4
    dodge: 1
    natural: 12
    size: -1
HP:
  HP: 136
  long: 16d8+64
saves:
  fort: 14
  ref: 11
  will: 8
immunities:
- plant traits
resistances:
  cold: 10
weaknesses:
- vulnerable to fire
speeds:
  base: 40
attacks:
  melee:
  - - text: gore +21 (2d8+9 plus rampant growth)
      entries:
      - - damage: 2d8+9
        - effect: rampant growth
      attack: gore
      bonus:
      - 21
    - text: bite +21 (2d8+9)
      entries:
      - - damage: 2d8+9
      attack: bite
      bonus:
      - 21
  special:
  - powerful charge (gore, 4d8+13)
  - rampant growth
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: speak with plants
    source: default
    freq: Constant
  - name: detect evil
    source: default
    freq: At will
  - name: command plants
    source: default
    freq: 3/day
    DC: 16
  - name: tree stride
    source: default
    freq: 1/day
  - name: wall of thorns
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 13
    concentration: 15
ability_scores:
  STR: 28
  DEX: 19
  CON: 18
  INT: 12
  WIS: 17
  CHA: 15
BAB: 12
CMB: 22
CMD: 37
feats:
- name: Combat Reflexes
- name: Dodge
- name: Lightning Reflexes
- name: Mobility
- name: Power Attack
- name: Spring Attack
- name: Weapon Focus (bite)
- name: Weapon Focus (gore)
skills:
  Acrobatics: 8
    when jumping: 12
  Diplomacy: 10
  Intimidate: 10
  Knowledge (nature): 5
  Perception: 22
  Sense Motive: 7
  Stealth: 5
  Survival: 5
  _racial_mods:
    Acrobatics:
      when jumping: 4
languages:
- Common
- Sylvan
special_qualities:
- thorny body
- verdant glide
ecology:
  environment: cold or temperate forests
  organization: solitary, pair, or pack
  treasure_type: standard
special_abilities:
  Rampant Growth (Ex): A lythirium's antlers teem with constantly growing thorny vines
    that can entangle creatures and make them bleed. When a lythirium hits a creature
    with its gore attack, that creature is entangled for 1d4 rounds and takes 1d6
    points of bleed damage. A successful DC 22 Reflex saving throw negates the entangled
    condition and reduces the bleed damage to 1d3 points. The save is Constitution-based.
  Thorny Body (Ex): A creature that strikes a lythirium with a natural weapon or an
    unarmed strike takes 2d8 points of piercing damage and is exposed to the lythirium's
    rampant growth. A creature that successfully grapples a lythirium takes 2d8 points
    of damage and is exposed to its rampant growth at the start of the grapple each
    round it maintains the grapple.
  Verdant Glide (Ex): A lythirium can move through any sort of undergrowth (such as
    natural thorns, briars, overgrown areas, and similar terrain) at its normal speed
    and without taking damage or suffering any other impairment. It ignores any magically
    manipulated overgrowth with thorns, briars, or other natural growth that would
    normally impede its motion.
desc_long: |-
  Savage hunters of those who would harm their habitats, lythiriums prowl Golarion's densest forests, seeking to protect the wild, untouched natural growth they hold sacred. While they have lived on the Material Plane for millennia, lythiriums are actually descended from primordial beasts native to the First World-creatures that fused plant and animal so seamlessly they seemed both and neither simultaneously. Peering out of seedpod eyes that radiate a soft green glow, lythiriums have exceptionally keen senses; they are not shy about preserving their forests, and they deliver their warnings in rasping voices reminiscent of leaves blowing across the earth.

   At its haunches, a lythirium measures 6 feet in height, with thorns, vines, and flowering blossoms inching ever higher. Its massive body is a matrix of vines, roots, and fine, furry moss and lichens. Immense branches shape its powerful chest and limbs. From thorny head to tail, a lythirium measures 9 feet in length; it can weigh as much as 900 pounds.

---

# Lythirium
This wolflike creature’s body is composed of thick vines, fine vegetation that almost resembles fur, and enormous thorns. Its eyes shine with a green glow, and prickly vines cover the immense, antlerlike growths on its head.
**Source** Pathfinder #105: The Inferno _[[spells/Gate|Gate]]_ pg. 86
**XP** 12,800

NG Large plant
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +22

##### Defense

**AC** 26, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+4 Dex, +1 dodge, +12 natural, –1 size)
**hp** 136 (16d8+64)
**Fort** +14, **Ref** +11, **Will** +8
**Immune** _[[universal monster rules/Plant Traits|plant traits]]_; **Resist** cold 10
**Weaknesses** vulnerable to fire

##### Offense
**Speed** 40 ft.
**Melee** gore +21 (2d8+9 plus rampant growth), bite +21 (2d8+9)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Powerful Charge|powerful charge]]_ (gore, 4d8+13), rampant growth
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +15)
Constant—_[[spells/Speak with Plants|speak with plants]]_
At will—_[[spells/Detect Evil|detect evil]]_
3/day—_[[spells/Command Plants|command plants]]_ (DC 16)
1/day—_[[spells/Tree Stride|tree stride]]_, _[[spells/Wall Of Thorns|wall of thorns]]_

##### Statistics
**Str** 28, **Dex** 19, **Con** 18, **Int** 12, **Wis** 17, **Cha** 15
**Base Atk** +12; **CMB** +22; **CMD** 37
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite), _Weapon Focus_ (gore)
**Skills** Acrobatics +8 (+12 when jumping), Diplomacy +10, Intimidate +10, Knowledge (nature) +5, Perception +22, Sense Motive +7, Stealth +5, Survival +5; **Racial Modifiers** +4 Acrobatics when jumping
**Languages** Common, Sylvan
**SQ** thorny body, verdant _[[spells/Glide|glide]]_

##### Ecology

**Environment** cold or temperate forests
**Organization** solitary, pair, or pack
**Treasure** standard

### Special Abilities

**Rampant Growth (Ex)** A _[[monsters/Lythirium|lythirium]]_’s antlers teem with constantly _[[items/Weapon Magic Abilities/Growing|growing]]_ thorny vines that can _[[spells/Entangle|entangle]]_ creatures and make them _[[universal monster rules/Bleed|bleed]]_. When a _lythirium_ hits a creature with its gore attack, that creature is _[[conditions/Entangled|entangled]]_ for 1d4 rounds and takes 1d6 points of _bleed_ damage. A successful DC 22 Reflex saving throw negates the _entangled_ condition and reduces the _bleed_ damage to 1d3 points. The save is Constitution-based.

**Thorny Body (Ex)** A creature that strikes a _lythirium_ with a natural weapon or an unarmed strike takes 2d8 points of piercing damage and is exposed to the _lythirium_’s rampant growth. A creature that successfully grapples a _lythirium_ takes 2d8 points of damage and is exposed to its rampant growth at the start of the grapple each round it maintains the grapple.

**Verdant _Glide_ (Ex)** A _lythirium_ can move through any sort of undergrowth (such as natural thorns, briars, overgrown areas, and similar terrain) at its normal speed and without taking damage or suffering any other impairment. It ignores any magically manipulated overgrowth with thorns, briars, or other natural growth that would normally impede its motion.

##### Description

Savage hunters of those who would _[[spells/Harm|harm]]_ their habitats, lythiriums prowl Golarion’s densest forests, seeking to protect the wild, untouched natural growth they hold _[[items/Weapon Magic Abilities/Sacred|sacred]]_. While they have lived on the Material Plane for millennia, lythiriums are actually descended from primordial beasts native to the First World—creatures that fused plant and animal so seamlessly they seemed both and neither simultaneously. Peering out of seedpod eyes that radiate a soft green glow, lythiriums have exceptionally _[[spells/Keen Senses|keen senses]]_; they are not shy about preserving their forests, and they deliver their warnings in rasping voices reminiscent of leaves blowing across the earth.

At its haunches, a _lythirium_ measures 6 feet in height, with thorns, vines, and flowering blossoms inching ever higher. Its massive body is a matrix of vines, roots, and fine, furry moss and lichens. Immense branches shape its powerful chest and limbs. From thorny head to tail, a _lythirium_ measures 9 feet in length; it can weigh as much as 900 pounds.
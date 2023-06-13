---
cssclass: [monsters]
title1: Gloomwasp
desc_short: The stinger and antennae of this dog-sized wasp pulsate with a dim, violet
  light.
title2: Gloomwasp
CR: 6
sources:
- name: Down the Blighted Path
  page: 55
  link: http://paizo.com/products/btpy9j6u?Pathfinder-Module-Down-the-Blighted-Path
XP: 2400
alignment: N
size: Small
type: magical beast
initiative:
  bonus: 5
senses:
  darkvision: 60
  low-light vision: true
  see invisibility: true
AC:
  AC: 23
  touch: 17
  flat_footed: 17
  components:
    dex: 5
    dodge: 1
    natural: 6
    size: 1
HP:
  HP: 59
  long: 7d10+21
saves:
  fort: 8
  ref: 10
  will: 4
defensive_abilities:
- shadow blending
immunities:
- poison
weaknesses:
- light blindness
speeds:
  base: 10
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: sting +9 (1d6+1 plus blacklight)
      entries:
      - - damage: 1d6+1
        - effect: blacklight
      attack: sting
      bonus:
      - 9
  ranged:
  - - text: 2 light rays +13 (1d6/×4 plus blacklight)
      entries:
      - - damage: 1d6
          crit_multiplier: 4
        - effect: blacklight
      count: 2
      attack: light rays
      bonus:
      - 13
  special:
  - blacklight
  - light ray
spell_like_abilities:
  entries:
  - name: see invisibility
    source: default
    freq: Constant
  - name: dancing lights
    source: default
    freq: 1/day
  - superscripts:
    - APG
    name: dust of twilight
    source: default
    freq: 1/day
    DC: 15
  - name: light
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 7
    concentration: 10
ability_scores:
  STR: 12
  DEX: 21
  CON: 16
  INT: 5
  WIS: 14
  CHA: 17
BAB: 7
CMB: 7
CMD: 23
feats:
- name: Dodge
- name: Flyby Attack
- name: Point-Blank Shot
- name: Rapid Shot
skills:
  Fly: 16
  Perception: 12
  Stealth: 14
  _racial_mods:
    Perception:
      _: 4
languages:
- Undercommon (can't speak)
special_qualities:
- corrupt light
ecology:
  environment: any underground
  organization: solitary, cluster (2-6), or nest (7-24)
  treasure_type: none
special_abilities:
  Blacklight (Ex): |-
    A strange, radiant energy empowers gloomwasps, and infests their natural attacks. A creature exposed to a gloomwasp's strange radiation emits a violet light for 1 minute (as if affected by faerie fire) and must make a successful DC 16 Fortitude saving throw or suffer low radiation poisoning. The save DC is Constitutionbased. Radiation functions similarly to poison. All radiation damage is a poison effect, and as such it can be removed with any effect that neutralizes poison.

     Low radiation poisoning-blacklight; save Fort DC 16, frequency 1/day initial effect 1 Constitution drain, secondary effect 1 Strength damage; cure 2 consecutive saves.
  Corrupt Light (Su): Three gloomwasps can focus their light rays on a single light
    source within 30 feet, such as a lantern, a torch, or a continual flame, as a
    full-round action. The affected light source becomes corrupted, shedding only
    dim light and exposing all creatures within range to the gloomwasps' blacklight.
    An attended light source resists this effect with a successful DC 19 Will saving
    throw. The effect immediately ends if any of the participating gloomwasps are
    slain, stunned, or otherwise prevented from using their light rays. The save DC
    is Constitution-based and includes a +2 racial bonus.
  Light Ray (Ex): A gloomwasp can fire beams of ultraviolet light from its antennae.
    These light rays have a maximum range of 30 feet, overcome damage reduction of
    any type, and deal double damage to fungi, mold, oozes, undead, and creatures
    with the light sensitivity or light blindness weakness.
  Shadow Blending (Su): Attacks against a gloomwasp in dim light have a 50% miss chance
    instead of the normal 20% miss chance. This ability does not grant total concealment;
    it only increases the miss chance.
desc_long: |-
  Infused with shadow magic and wielding light as a weapon, these aggressive hunters prowl the endless, twisting caverns and canyons of Sekamina. Gloomwasps are the result of giant vermin exposed to the flesh-altering radiations of the Darklands, becoming vibrantly colorful if highly toxic additions to the strange ecosystem that thrives below Golarion's surface. They hunt by using their natural glow to attract curious creatures and travelers, then lash out with beams of energy. Gloomwasps often need only strike their victims a few times, then follow them for days while the lingering radiation slowly saps their prey's ability to flee or fight back.

  Surprisingly intelligent and tenacious, a small band of migrating gloomwasps can quickly become a full infestation. They build faintly radioactive nests high into cave ceilings, narrow tunnels, and hollow rock formations, where they nurse their drab, rat-sized grubs on a steady diet of regurgitated blood. The grubs eventually seal themselves within hexagonal cells, emerging weeks later as adult gloomwasps.

  While relatively fragile, gloomwasps' intelligence makes them formidable. They communicate with a system of dance, light flashes, and pheromones, and work together effectively to overwhelm prey of superior size and strength, including humanoids.

---

# Gloomwasp
The stinger and antennae of this dog-sized wasp pulsate with a dim, violet light.
**Source** Down the Blighted Path pg. 55
**XP** 2,400

N Small magical beast
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +12

##### Defense

**AC** 23, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+5 Dex, +1 dodge, +6 natural, +1 size)
**hp** 59 (7d10+21)
**Fort** +8, **Ref** +10, **Will** +4
**Defensive Abilities** _[[items/Armor Magic Abilities/Shadow Blending|shadow blending]]_; **Immune** poison
**Weaknesses** _[[universal monster rules/Light Blindness|light blindness]]_

##### Offense
**Speed** 10 ft., fly 60 ft. (good)
**Melee** sting +9 (1d6+1 plus blacklight)
**Ranged** 2 light rays +13 (1d6/×4 plus blacklight)
**Special Attacks** blacklight, light ray
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +10)
Constant—_see invisibility_
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Dust Of Twilight|dust of twilight]]_ (DC 15), light

##### Statistics
**Str** 12, **Dex** 21, **Con** 16, **Int** 5, **Wis** 14, **Cha** 17
**Base Atk** +7; **CMB** +7; **CMD** 23
**Feats** _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_
**Skills** Fly +16, Perception +12, Stealth +14; **Racial Modifiers** +4 Perception
**Languages** Undercommon (can’t speak)
**SQ** corrupt light

##### Ecology

**Environment** any underground
**Organization** solitary, cluster (2–6), or nest (7–24)
**Treasure** none

### Special Abilities

**Blacklight (Ex)** A strange, _[[items/Armor Magic Abilities/Radiant|radiant]]_ energy empowers gloomwasps, and infests their _[[universal monster rules/Natural Attacks|natural attacks]]_. A creature exposed to a _[[monsters/Gloomwasp|gloomwasp]]_’s strange radiation emits a violet light for 1 minute (as if affected by _[[spells/Faerie Fire|faerie fire]]_) and must make a successful DC 16 Fortitude saving throw or suffer low radiation _[[items/Armor Magic Abilities/Poisoning|poisoning]]_. The save DC is Constitutionbased. Radiation functions similarly to poison. All radiation damage is a poison effect, and as such it can be removed with any effect that neutralizes poison.

Low radiation _poisoning_—blacklight; save Fort DC 16, frequency 1/day initial effect 1 Constitution drain, secondary effect 1 Strength damage; cure 2 consecutive saves.

**Corrupt Light (Su)** Three gloomwasps can focus their light rays on a single light source within 30 feet, such as a lantern, a _[[items/Mundane/Torch|torch]]_, or a _[[spells/Continual Flame|continual flame]]_, as a full-round action. The affected light source becomes corrupted, shedding only dim light and exposing all creatures within range to the gloomwasps’ blacklight. An attended light source resists this effect with a successful DC 19 Will saving throw. The effect immediately ends if any of the participating gloomwasps are slain, _[[conditions/Stunned|stunned]]_, or otherwise prevented from using their light rays. The save DC is Constitution-based and includes a +2 racial bonus.

**Light Ray (Ex)** A _gloomwasp_ can fire beams of ultraviolet light from its antennae. These light rays have a maximum range of 30 feet, overcome _[[universal monster rules/Damage Reduction|damage reduction]]_ of any type, and deal double damage to fungi, mold, oozes, undead, and creatures with the _[[universal monster rules/Light Sensitivity|light sensitivity]]_ or _light blindness_ weakness.
**_Shadow Blending_ (Su)** Attacks against a _gloomwasp_ in dim light have a 50% miss chance instead of the normal 20% miss chance. This ability does not grant total concealment; it only increases the miss chance.

##### Description

Infused with _[[items/Armor Magic Abilities/Shadow|shadow]]_ magic and wielding light as a weapon, these aggressive hunters prowl the endless, twisting caverns and canyons of Sekamina. Gloomwasps are the result of _[[spells/Giant Vermin|giant vermin]]_ exposed to the flesh-altering radiations of the Darklands, becoming vibrantly colorful if highly _[[items/Weapon Magic Abilities/Toxic|toxic]]_ additions to the strange ecosystem that thrives below Golarion’s surface. They hunt by using their natural glow to attract curious creatures and travelers, then lash out with beams of energy. Gloomwasps often need only strike their victims a few times, then follow them for days while the lingering radiation slowly saps their prey’s ability to flee or fight back.

Surprisingly intelligent and tenacious, a small band of migrating gloomwasps can quickly become a full infestation. They build faintly radioactive nests high into cave ceilings, narrow tunnels, and hollow rock formations, where they nurse their drab, rat-sized grubs on a steady diet of regurgitated blood. The grubs eventually seal themselves within hexagonal cells, emerging weeks later as adult gloomwasps.

While relatively fragile, gloomwasps’ intelligence makes them formidable. They communicate with a system of dance, light flashes, and pheromones, and work together effectively to _[[feats/Overwhelm|overwhelm]]_ prey of superior size and strength, including humanoids.
---
cssclass: [monsters]
title1: Death Coach
desc_short: Two spectral horses pull this ornate, ghostly carriage, whose windows
  are blocked by dark, heavy curtains.
title2: Death Coach
CR: 14
sources:
- name: Bestiary 5
  page: 67
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 38400
alignment: NE
size: Huge
type: undead
subtypes:
- incorporeal
initiative:
  bonus: 14
senses:
  darkvision: 60
  deathwatch: true
  lifesense: true
auras:
- name: aura of doom
  radius: 30
  DC: 26
AC:
  AC: 27
  touch: 27
  flat_footed: 16
  components:
    deflection: 8
    dex: 10
    dodge: 1
    size: -2
HP:
  HP: 212
  long: 17d8+136
saves:
  fort: 13
  ref: 15
  will: 14
defensive_abilities:
- channel resistance +4
- incorporeal
immunities:
- undead traits
speeds:
  base: 40
  other_semicolon: soulbound gallop
  fly: 30
  fly_maneuverability: average
attacks:
  melee:
  - - text: incorporeal touch +20 (17d6 negative energy)
      entries:
      - - damage: 17d6
          type: negative energy
      attack: incorporeal touch
      bonus:
      - 20
  special:
  - collect soul
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: ghost sound
    source: default
    freq: At will
    DC: 18
  - name: scare
    source: default
    freq: At will
    DC: 20
  - name: distracting cacophony
    source: default
    freq: At will
    DC: 21
  - name: quickened fear
    source: default
    freq: 3/day
    DC: 22
  - name: phantasmal killer
    source: default
    freq: 3/day
    DC: 22
  sources:
  - name: default
    CL: 16
    concentration: 24
ability_scores:
  STR:
  DEX: 30
  CON:
  INT: 15
  WIS: 18
  CHA: 27
BAB: 12
CMB: 24
CMD: 43
CMD_other: can't be tripped
feats:
- name: Combat Reflexes
- name: Dodge
- name: Improved Initiative
- name: Lightning Stance
- name: Mobility
- name: Quicken Spell-Like Ability (fear)
- name: Skill Focus (Intimidate)
- name: Skill Focus (Perception)
- name: Wind Stance
skills:
  Fly: 26
  Intimidate: 34
  Knowledge (geography): 9
  Knowledge (history): 9
  Knowledge (local): 9
  Knowledge (nobility): 9
  Perception: 30
  Sense Motive: 13
  Survival: 21
languages:
- Abyssal
- Common
- Infernal (can't speak any language)
ecology:
  environment: any
  organization: solitary
  treasure_type: standard
special_abilities:
  Aura of Doom (Su): The death coach's aura acts like an aura of doom with a radius
    of 30 feet. A creature that succeeds at its save is immune to that death coach's
    aura for 24 hours. This is a mind-affecting fear effect. The save DC is Charisma-based.
  Collect Soul (Su): When a death coach deals damage to a creature with its touch
    attack, it can immediately attempt to collect the creature's soul, forcing the
    creature to attempt a DC 24 Fortitude save. Creatures under the effects of a fear
    effect take a -4 penalty on this save. A creature that succeeds at its save takes
    3d6+16 points of damage. On a failed save, the creature takes 160 points of damage
    (as if affected by a CL 16 finger of death). The soul of a creature slain by this
    attack becomes trapped in the death coach's interior. A trapped soul can be restored
    to life only by a miracle or wish. This is a death effect, and a creature that
    succeeds at its save is immune to that death coach's collect soul ability for
    24 hours. The save DC is Charisma-based.
  Soulbound Gallop (Su): When the death coach has trapped a soul with its collect
    soul ability, all of its movement speeds double. The doubling occurs before applying
    any other effects that increase its speed.
desc_long: Fearsome phantasmal carriages pulled by ghostly horses, death coaches appear
  without warning to collect and carry off unwilling mortal souls to the afterlife,
  slaying their victims first if need be.

---

# Death Coach
Two spectral horses _[[universal monster rules/Pull|pull]]_ this ornate, ghostly carriage, whose windows are blocked by dark, heavy curtains.
**Source** Bestiary 5 pg. 67
**XP** 38,400

NE Huge undead (_[[universal monster rules/Incorporeal|incorporeal]]_)
**Init** +14; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Deathwatch|deathwatch]]_, _[[universal monster rules/Lifesense|lifesense]]_; Perception +30
**Aura** _[[spells/Aura of Doom|aura of doom]]_ (30 ft., DC 26)

##### Defense

**AC** 27, touch 27, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+8 deflection, +10 Dex, +1 _[[feats/Dodge|Dodge]]_, -2 size)
**hp** 212 (17d8+136)
**Fort** +13, **Ref** +15, **Will** +14
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4, _incorporeal_; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 40 ft., fly 30 ft. (average); soulbound gallop
**Melee** _incorporeal_ touch +20 (17d6 negative energy)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** collect soul
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +24)
At will—_[[spells/Ghost Sound|ghost sound]]_ (DC 18), _[[spells/Scare|scare]]_ (DC 20), _[[spells/Distracting Cacophony|distracting cacophony]]_ (DC 21)
3/day—quickened _[[universal monster rules/Fear|fear]]_ (DC 22), _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 22)

##### Statistics
**Str** —, **Dex** 30, **Con** —, **Int** 15, **Wis** 18, **Cha** 27
**Base Atk** +12; **CMB** +24; **CMD** 43 (can’t be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Stance|Lightning Stance]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_fear_), _[[feats/Skill Focus|Skill Focus]]_ (Intimidate), _Skill Focus_ (Perception), _[[feats/Wind Stance|Wind Stance]]_
**Skills** Fly +26, Intimidate +34, Knowledge (geography, history, local, nobility) +9, Perception +30, Sense Motive +13, Survival +21
**Languages** Abyssal, Common, Infernal (can’t speak any language)

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** standard

### Special Abilities

**_Aura of Doom_ (Su)** The _[[monsters/Death Coach|death coach]]_’s aura acts like an _aura of doom_ with a radius of 30 feet. A creature that succeeds at its save is immune to that _death coach_’s aura for 24 hours. This is a mind-affecting _fear_ effect. The save DC is Charisma-based.

**Collect Soul (Su)** When a _death coach_ deals damage to a creature with its touch attack, it can immediately attempt to collect the creature’s soul, forcing the creature to attempt a DC 24 Fortitude save. Creatures under the effects of a _fear_ effect take a -4 penalty on this save. A creature that succeeds at its save takes 3d6+16 points of damage. On a failed save, the creature takes 160 points of damage (as if affected by a CL 16 _[[spells/Finger Of Death|finger of death]]_). The soul of a creature slain by this attack becomes trapped in the _death coach_’s interior. A trapped soul can be restored to life only by a _[[spells/Miracle|miracle]]_ or _[[spells/Wish|wish]]_. This is a death effect, and a creature that succeeds at its save is immune to that _death coach_’s collect soul ability for 24 hours. The save DC is Charisma-based.
**Soulbound Gallop (Su)** When the _death coach_ has trapped a soul with its collect soul ability, all of its movement speeds double. The doubling occurs before applying any other effects that increase its speed.

##### Description

Fearsome _[[items/Armor Magic Abilities/Phantasmal|phantasmal]]_ carriages pulled by ghostly horses, death coaches appear without warning to collect and carry off unwilling mortal souls to the afterlife, slaying their victims first if need be.
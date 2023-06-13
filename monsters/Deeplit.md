---
cssclass: [monsters]
title1: Deeplit
desc_short: This granite-skinned humanoid stands as tall as a dwarf, though a flickering
  flame hovers where its head should be.
title2: Deeplit
CR: 5
sources:
- name: Down the Blighted Path
  page: 53
  link: http://paizo.com/products/btpy9j6u?Pathfinder-Module-Down-the-Blighted-Path
XP: 1600
alignment: NE
size: Medium
type: undead
initiative:
  bonus: 2
senses:
  darkvision: 60
auras:
- name: palelight
  radius: 20
  DC: 16
AC:
  AC: 19
  touch: 12
  flat_footed: 17
  components:
    armor: 4
    dex: 2
    natural: 3
HP:
  HP: 52
  long: 7d8+21
saves:
  fort: 5
  ref: 4
  will: 8
immunities:
- blindness
- undead traits
weaknesses:
- pattern susceptibility
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk heavy pick +13 (1d6+10/×4)
      entries:
      - - damage: 1d6+10
          crit_multiplier: 4
      attack: mwk heavy pick
      bonus:
      - 13
  ranged:
  - - text: rock +7 (1d4+7)
      entries:
      - - damage: 1d4+7
      attack: rock
      bonus:
      - 7
  special:
  - consume light
ability_scores:
  STR: 25
  DEX: 14
  CON:
  INT: 10
  WIS: 16
  CHA: 17
BAB: 5
CMB: 12
CMB_other: +14 sunder
CMD: 24
CMD_other: 26 vs. sunder
feats:
- name: Cleave
- name: Improved Sunder
- name: Power Attack
- name: Throw Anything
skills:
  Climb: 16
  Knowledge (dungeoneering): 7
  Perception: 13
  Profession (miner): 10
languages:
- Dwarven
- Undercommon (can't speak)
ecology:
  environment: any underground
  organization: solitary, pair, or team (3-12)
  treasure_type: standard
special_abilities:
  Consume Light (Su): A deeplit can inhale nearby lights as a standard action. The
    deeplit makes a single Charisma check against all light sources within 20 feet
    (DC = 10 + the flame's spell level; nonmagical torches and lanterns have a DC
    of 10, while alchemical light sources have a DC of 11). Affected light sources
    are immediately extinguished. If the deeplit consumes a light source that is at
    least normal brightness, it can either immediately regurgitate or swallow the
    light as a free action. Regurgitating the light deals 2d6 points of fire damage
    to all creatures in a 15-foot cone, and blinds affected creatures for 1d6 rounds.
    A successful DC 16 Reflex saving throw halves the damage and dazzles victims instead
    of blinding them. Swallowing the light enhances the deeplit's palelight aura for
    1d6 rounds. The save DC is Charisma-based. Deeplit are immune to this ability,
    and to any damage inflicted by regurgitated light.
  Palelight Aura (Su): A deeplit's flaming head emits dim light in a 20-foot radius.
    When a deeplit swallows light, its head instead emits bright light over the same
    area for 1d6 rounds. Any living creatures within the area of this unholy light
    become fatigued for 1 hour (Fortitude DC 16 negates). A creature that successfully
    saves against a deeplit's palelight aura can't be affected by that same deeplit's
    aura for 24 hours. Its save DC is Charisma-based.
  Pattern Susceptibility (Ex): Pattern effects and spells affect deeplits normally,
    ignoring the normal undead immunity to mind-affecting effects.
desc_long: |-
  Deeplits spawn from unfortunate creatures lost underground. Many were dwarves who fell during the Quest for Sky, but miners and explorers may also succumb to similar fates. Deeplits dig through caves and mines, yearning to see sunlight one last time, but are cursed to repeat the same confused paths they followed in life.

  Deeplits paradoxically crave the light other undead despise. Thanks to their long exposure to lightless realms, deeplits find bright lights euphoric.

---

# Deeplit
This granite-skinned humanoid stands as tall as a dwarf, though a flickering flame hovers where its head should be.
**Source** Down the Blighted Path pg. 53
**XP** 1,600

NE Medium undead
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +13
**Aura** palelight (20 ft., DC 16)

##### Defense

**AC** 19, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+4 armor, +2 Dex, +3 natural)
**hp** 52 (7d8+21)
**Fort** +5, **Ref** +4, **Will** +8
**Immune** blindness, _[[universal monster rules/Undead Traits|undead traits]]_
**Weaknesses** pattern susceptibility

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Heavy pick|heavy pick]]_ +13 (1d6+10/×4)
**Ranged** rock +7 (1d4+7)
**Special Attacks** consume light

##### Statistics
**Str** 25, **Dex** 14, **Con** —, **Int** 10, **Wis** 16, **Cha** 17
**Base Atk** +5; **CMB** +12 (+14 sunder); **CMD** 24 (26 vs. sunder)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Throw Anything|Throw Anything]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +16, Knowledge (dungeoneering) +7, Perception +13, Profession (_[[npcs/Miner|miner]]_) +10
**Languages** Dwarven, Undercommon (can’t speak)

##### Ecology

**Environment** any underground
**Organization** solitary, pair, or team (3–12)
**Treasure** standard

### Special Abilities

**Consume Light (Su)** A _[[monsters/Deeplit|deeplit]]_ can inhale nearby lights as a standard action. The _deeplit_ makes a single Charisma check against all light sources within 20 feet (DC = 10 + the flame’s spell level; nonmagical torches and lanterns have a DC of 10, while alchemical light sources have a DC of 11). Affected light sources are immediately extinguished. If the _deeplit_ consumes a light source that is at least normal brightness, it can either immediately regurgitate or swallow the light as a free action. Regurgitating the light deals 2d6 points of fire damage to all creatures in a 15-foot cone, and blinds affected creatures for 1d6 rounds. A successful DC 16 Reflex saving throw halves the damage and dazzles victims instead of _[[items/Armor Magic Abilities/Blinding|blinding]]_ them. Swallowing the light enhances the _deeplit_’s palelight aura for 1d6 rounds. The save DC is Charisma-based. _Deeplit_ are immune to this ability, and to any damage inflicted by regurgitated light.

**Palelight Aura (Su)** A _deeplit_’s _[[items/Weapon Magic Abilities/Flaming|flaming]]_ head emits dim light in a 20-foot radius. When a _deeplit_ swallows light, its head instead emits bright light over the same area for 1d6 rounds. Any living creatures within the area of this _[[items/Weapon Magic Abilities/Unholy|unholy]]_ light become _[[conditions/Fatigued|fatigued]]_ for 1 hour (Fortitude DC 16 negates). A creature that successfully saves against a _deeplit_’s palelight aura can’t be affected by that same _deeplit_’s aura for 24 hours. Its save DC is Charisma-based.

**Pattern Susceptibility (Ex)** Pattern effects and spells affect deeplits normally, ignoring the normal undead _[[universal monster rules/Immunity|immunity]]_ to mind-affecting effects.

##### Description

Deeplits spawn from unfortunate creatures lost underground. Many were dwarves who fell during the Quest for Sky, but miners and explorers may also succumb to similar fates. Deeplits dig through caves and mines, yearning to see sunlight one last time, but are cursed to repeat the same _[[conditions/Confused|confused]]_ paths they followed in life.

Deeplits paradoxically crave the light other undead despise. Thanks to their long exposure to lightless realms, deeplits find bright lights euphoric.